#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script d'analyse des données de Pattes & Papilles
Auteur : Agent Analyste
Description : Calculs statistiques du churn, signaux précurseurs,
              motifs de départ, impact chiffre d'affaires et génération
              des graphiques conformes à la charte visuelle.
Règle usine : Noms de variables en anglais, commentaires en français.
"""

import os
import re
import base64
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Configuration des répertoires de travail
DATA_DIR = "donnees"
OUTPUT_DIR = "chantier/analyse"
DASHBOARD_PATH = "chantier/livrables/tableau-de-bord.html"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Charte graphique officielle de Pattes & Papilles
COLOR_PRIMARY = "#1E4636"      # Vert sapin (titres, barres standard, éléments phares)
COLOR_ACCENT = "#D9734E"       # Terracotta (chiffre clé à retenir, alertes)
COLOR_BG = "#FBF5EC"           # Crème (fond neutre de la marque)
COLOR_SECONDARY = "#E8B04B"    # Moutarde (accents secondaires, alertes modérées)
COLOR_MUTED = "#8C9B90"        # Gris vert doux (comparatifs neutres)
COLOR_LIGHT_ACCENT = "#F2A88D" # Terracotta clair

# Paramétrage global pour matplotlib
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = COLOR_PRIMARY
plt.rcParams['axes.linewidth'] = 0.8
plt.rcParams['text.color'] = COLOR_PRIMARY
plt.rcParams['axes.labelcolor'] = COLOR_PRIMARY
plt.rcParams['xtick.color'] = COLOR_PRIMARY
plt.rcParams['ytick.color'] = COLOR_PRIMARY


def load_datasets():
    """
    Chargement et nettoyage initial des données.
    Application stricte de la règle : dédoublonnage de customer_id avant tout calcul.
    """
    customers_path = os.path.join(DATA_DIR, "customers.csv")
    orders_path = os.path.join(DATA_DIR, "orders.csv")
    products_path = os.path.join(DATA_DIR, "products.csv")
    marketing_path = os.path.join(DATA_DIR, "marketing_monthly.csv")
    support_path = os.path.join(DATA_DIR, "abonnes_support.csv")

    customers_raw = pd.read_csv(customers_path)
    orders_df = pd.read_csv(orders_path)
    products_df = pd.read_csv(products_path)
    marketing_df = pd.read_csv(marketing_path)
    support_df = pd.read_csv(support_path)

    # Règle d'or : suppression des doublons de customer_id avant tout calcul
    initial_rows = len(customers_raw)
    duplicates_count = customers_raw.duplicated(subset=['customer_id']).sum()
    customers_df = customers_raw.drop_duplicates(subset=['customer_id']).copy()
    print(f"Nettoyage : {initial_rows} lignes chargées, {duplicates_count} doublons supprimés -> {len(customers_df)} clients uniques.")

    # Harmonisation et typage des dates
    customers_df['signup_date_dt'] = pd.to_datetime(customers_df['signup_date'])
    customers_df['last_order_date_dt'] = pd.to_datetime(customers_df['last_order_date'])
    orders_df['order_date_dt'] = pd.to_datetime(orders_df['order_date'])

    return customers_df, orders_df, products_df, marketing_df, support_df, duplicates_count


def compute_core_metrics(customers_df, orders_df):
    """
    Calcul rigoureux des indicateurs clés demandés pour l'analyse du churn.
    """
    metrics = {}

    # 1. Périmètre global et churn par formule
    total_customers = len(customers_df)
    total_churned = int(customers_df['churned'].sum())
    global_churn_rate = total_churned / total_customers

    plan_breakdown = customers_df.groupby('plan')['churned'].agg(['count', 'sum', 'mean']).to_dict(orient='index')

    metrics['global'] = {
        'total_customers': total_customers,
        'total_churned': total_churned,
        'global_churn_rate': global_churn_rate,
        'by_plan': plan_breakdown
    }

    # 2. Churn selon la date de dernière commande (avant/après le 1er mars 2026)
    customers_df['last_order_before_march'] = customers_df['last_order_date_dt'] < '2026-03-01'
    last_order_march_summary = customers_df.groupby('last_order_before_march')['churned'].agg(['count', 'sum', 'mean']).to_dict(orient='index')

    # Détail par mois de dernière commande
    customers_df['last_order_month'] = customers_df['last_order_date_dt'].dt.to_period('M').astype(str)
    monthly_last_order = customers_df.groupby('last_order_month')['churned'].agg(['count', 'sum', 'mean']).to_dict(orient='index')

    # Cohortes d'inscription (avant/après le 1er mars 2026)
    customers_df['signup_before_march'] = customers_df['signup_date_dt'] < '2026-03-01'
    signup_march_summary = customers_df.groupby('signup_before_march')['churned'].agg(['count', 'sum', 'mean']).to_dict(orient='index')

    metrics['dates'] = {
        'last_order_before_march': last_order_march_summary,
        'monthly_last_order': monthly_last_order,
        'signup_before_march': signup_march_summary
    }

    # 3. Churn par canal d'acquisition (brut et nettoyé)
    channel_raw = customers_df.groupby('acquisition_channel')['churned'].agg(['count', 'sum', 'mean']).to_dict(orient='index')
    customers_df['channel_clean'] = customers_df['acquisition_channel'].replace({
        'Paid Social': 'paid_social',
        'Facebook': 'paid_social'
    })
    channel_clean = customers_df.groupby('channel_clean')['churned'].agg(['count', 'sum', 'mean']).to_dict(orient='index')

    metrics['channels'] = {
        'raw': channel_raw,
        'clean': channel_clean
    }

    # 4. Churn par espèce animale (brut et nettoyé)
    species_raw = customers_df.groupby('pet_species')['churned'].agg(['count', 'sum', 'mean']).to_dict(orient='index')
    customers_df['species_clean'] = customers_df['pet_species'].replace({'chat': 'cat'})
    species_clean = customers_df.groupby('species_clean')['churned'].agg(['count', 'sum', 'mean']).to_dict(orient='index')

    metrics['species'] = {
        'raw': species_raw,
        'clean': species_clean
    }

    # 5. Churn par rythme de livraison (abonnés uniquement)
    sub_df = customers_df[customers_df['plan'] == 'subscription']
    delivery_weeks_summary = sub_df.groupby('delivery_weeks')['churned'].agg(['count', 'sum', 'mean']).to_dict(orient='index')
    metrics['delivery_weeks'] = delivery_weeks_summary

    # 6. Churn par remise de bienvenue
    discount_summary = customers_df.groupby('welcome_discount_pct')['churned'].agg(['count', 'sum', 'mean']).to_dict(orient='index')
    metrics['welcome_discount'] = discount_summary

    # 7. Signaux précurseurs
    # Livraisons sautées sur 90j (abonnés)
    skipped_summary = sub_df.groupby('skipped_deliveries_90d')['churned'].agg(['count', 'sum', 'mean']).to_dict(orient='index')

    # Retards de livraison sur 12 mois
    late_summary_all = customers_df.groupby('late_deliveries_12m')['churned'].agg(['count', 'sum', 'mean']).to_dict(orient='index')
    late_summary_sub = sub_df.groupby('late_deliveries_12m')['churned'].agg(['count', 'sum', 'mean']).to_dict(orient='index')

    # Tickets service client sur 12 mois
    support_summary_all = customers_df.groupby('support_tickets_12m')['churned'].agg(['count', 'sum', 'mean']).to_dict(orient='index')
    support_summary_sub = sub_df.groupby('support_tickets_12m')['churned'].agg(['count', 'sum', 'mean']).to_dict(orient='index')

    # Note du dernier avis
    review_summary = customers_df.groupby('last_review_score', dropna=False)['churned'].agg(['count', 'sum', 'mean']).to_dict(orient='index')

    # Taux d'ouverture e-mail sur 90j
    email_active = customers_df[customers_df['newsletter_optin'] == 'yes']
    email_retained = email_active[email_active['churned'] == 0]['email_open_rate_90d'].mean()
    email_churned = email_active[email_active['churned'] == 1]['email_open_rate_90d'].mean()

    metrics['signals'] = {
        'skipped_deliveries_sub': skipped_summary,
        'late_deliveries_all': late_summary_all,
        'late_deliveries_sub': late_summary_sub,
        'support_tickets_all': support_summary_all,
        'support_tickets_sub': support_summary_sub,
        'review_score': review_summary,
        'email_open_rate': {
            'retained_mean': float(email_retained),
            'churned_mean': float(email_churned),
            'optin_count': len(email_active)
        }
    }

    # 8. Motifs de départ déclarés
    churned_customers = customers_df[customers_df['churned'] == 1]
    reasons_all = churned_customers['churn_reason'].fillna('Non renseigné').value_counts().to_dict()
    reasons_known = churned_customers['churn_reason'].dropna().value_counts().to_dict()

    metrics['churn_reasons'] = {
        'all': reasons_all,
        'known': reasons_known
    }

    # 9. Chiffre d'affaires perdu (12 mois glissants dans orders.csv : 2025-07-01 au 2026-06-30)
    orders_12m = orders_df[(orders_df['order_date_dt'] >= '2025-07-01') & (orders_df['order_date_dt'] <= '2026-06-30')]
    orders_12m_cust = orders_12m.merge(customers_df[['customer_id', 'churned', 'plan']], on='customer_id', how='left')

    ca_total_12m = float(orders_12m['line_total_eur'].sum())
    ca_churned_12m = float(orders_12m_cust[orders_12m_cust['churned'] == 1]['line_total_eur'].sum())
    ca_retained_12m = float(orders_12m_cust[orders_12m_cust['churned'] == 0]['line_total_eur'].sum())

    ca_churned_sub = float(orders_12m_cust[(orders_12m_cust['churned'] == 1) & (orders_12m_cust['plan'] == 'subscription')]['line_total_eur'].sum())
    ca_churned_oneoff = float(orders_12m_cust[(orders_12m_cust['churned'] == 1) & (orders_12m_cust['plan'] == 'one_off')]['line_total_eur'].sum())

    # Dépense cumulée vie entière (total_spent_eur)
    lifetime_total = float(customers_df['total_spent_eur'].sum())
    lifetime_churned = float(customers_df[customers_df['churned'] == 1]['total_spent_eur'].sum())
    lifetime_retained = float(customers_df[customers_df['churned'] == 0]['total_spent_eur'].sum())

    lifetime_churned_sub = float(customers_df[(customers_df['churned'] == 1) & (customers_df['plan'] == 'subscription')]['total_spent_eur'].sum())
    lifetime_churned_oneoff = float(customers_df[(customers_df['churned'] == 1) & (customers_df['plan'] == 'one_off')]['total_spent_eur'].sum())

    metrics['financials'] = {
        'ca_total_12m': ca_total_12m,
        'ca_churned_12m': ca_churned_12m,
        'ca_retained_12m': ca_retained_12m,
        'ca_churned_sub': ca_churned_sub,
        'ca_churned_oneoff': ca_churned_oneoff,
        'churned_ca_share_pct': (ca_churned_12m / ca_total_12m) * 100,
        'lifetime_total': lifetime_total,
        'lifetime_churned': lifetime_churned,
        'lifetime_retained': lifetime_retained,
        'lifetime_churned_sub': lifetime_churned_sub,
        'lifetime_churned_oneoff': lifetime_churned_oneoff
    }

    # 10. Recette Saumon Chat du 4 mai 2026 (références P026 et P027)
    salmon_orders_post = orders_df[(orders_df['product_id'].isin(['P026', 'P027'])) & (orders_df['order_date_dt'] >= '2026-05-04')]
    salmon_customers = salmon_orders_post['customer_id'].unique()
    salmon_cust_df = customers_df[customers_df['customer_id'].isin(salmon_customers)]

    salmon_refusals = int((salmon_cust_df['churn_reason'] == 'pet_refused_food').sum())
    total_refusals = int((customers_df['churn_reason'] == 'pet_refused_food').sum())

    metrics['salmon_crisis'] = {
        'unique_customers': len(salmon_cust_df),
        'churned_count': int(salmon_cust_df['churned'].sum()),
        'churn_rate': float(salmon_cust_df['churned'].mean()),
        'salmon_refusals': salmon_refusals,
        'total_refusals': total_refusals,
        'refusal_share_pct': (salmon_refusals / total_refusals) * 100 if total_refusals > 0 else 0
    }

    return metrics


def generate_chart_1_monthly_churn(customers_df):
    """
    Graphique 1 : Évolution du taux de churn selon le mois de dernière commande.
    Titre-conclusion clair selon la charte.
    """
    fig, ax = plt.subplots(figsize=(10, 5.5), facecolor=COLOR_BG)
    ax.set_facecolor(COLOR_BG)

    # Sélection des mois du premier semestre 2026
    cust_filtered = customers_df[customers_df['last_order_month'].isin([
        '2026-01', '2026-02', '2026-03', '2026-04', '2026-05', '2026-06'
    ])].copy()

    monthly_stats = cust_filtered.groupby('last_order_month')['churned'].agg(['count', 'mean']).reset_index()
    monthly_stats['rate_pct'] = monthly_stats['mean'] * 100

    labels = ['Janv 2026', 'Févr 2026', 'Mars 2026\n(+5% prix)', 'Avr 2026', 'Mai 2026\n(Saumon)', 'Juin 2026']
    x = np.arange(len(labels))
    rates = monthly_stats['rate_pct'].values

    # Couleurs : gris neutre pour avant-mars, terracotta pour mars/avril, vert sapin pour mai/juin
    colors = [COLOR_MUTED, COLOR_MUTED, COLOR_ACCENT, COLOR_ACCENT, COLOR_PRIMARY, COLOR_PRIMARY]

    bars = ax.bar(x, rates, color=colors, width=0.55, edgecolor=COLOR_PRIMARY, linewidth=1)

    for bar, rate in zip(bars, rates):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2, f"{rate:.1f} %",
                ha='center', va='bottom', fontsize=11, fontweight='bold', color=COLOR_PRIMARY)

    ax.set_title("88 % des clients dont la dernière commande remonte avant mars ont résilié",
                 fontsize=13, fontweight='bold', pad=20, color=COLOR_PRIMARY)
    ax.set_ylabel("Taux de départ (churn) (%)", fontsize=11, fontweight='bold', labelpad=10)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=10)
    ax.set_ylim(0, 105)
    ax.grid(axis='y', linestyle='--', alpha=0.3, color=COLOR_PRIMARY)

    # Ligne moyenne globale
    ax.axhline(32.24, color=COLOR_ACCENT, linestyle=':', linewidth=1.5, label="Moyenne globale (32,2 %)")
    ax.legend(loc='upper right', frameon=False, fontsize=10)

    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)

    plt.tight_layout()
    output_path = os.path.join(OUTPUT_DIR, "graphique_1_churn_mensuel_hausse_prix.png")
    plt.savefig(output_path, dpi=300, facecolor=COLOR_BG)
    plt.close()
    print(f"Graphique 1 généré : {output_path}")


def generate_chart_2_welcome_discount(customers_df):
    """
    Graphique 2 : Taux de churn selon la remise de bienvenue.
    Titre-conclusion clair selon la charte.
    """
    fig, ax = plt.subplots(figsize=(8, 5.5), facecolor=COLOR_BG)
    ax.set_facecolor(COLOR_BG)

    disc_stats = customers_df.groupby('welcome_discount_pct')['churned'].agg(['count', 'mean']).reset_index()
    disc_stats['rate_pct'] = disc_stats['mean'] * 100

    labels = [f"Sans remise\n(n={disc_stats.loc[0, 'count']})",
              f"Remise 20 %\n(n={disc_stats.loc[1, 'count']})",
              f"Remise 30 %\n(n={disc_stats.loc[2, 'count']})"]
    x = np.arange(len(labels))
    rates = disc_stats['rate_pct'].values

    # Couleurs : terracotta pour 30% (valeur à retenir), vert sapin pour le reste
    colors = [COLOR_PRIMARY, COLOR_PRIMARY, COLOR_ACCENT]

    bars = ax.bar(x, rates, color=colors, width=0.5, edgecolor=COLOR_PRIMARY, linewidth=1)

    for bar, rate in zip(bars, rates):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1.5, f"{rate:.1f} %",
                ha='center', va='bottom', fontsize=12, fontweight='bold', color=COLOR_PRIMARY)

    ax.set_title("La remise de 30 % attire des profils presque deux fois plus volatils",
                 fontsize=13, fontweight='bold', pad=20, color=COLOR_PRIMARY)
    ax.set_ylabel("Taux de churn (%)", fontsize=11, fontweight='bold', labelpad=10)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=11)
    ax.set_ylim(0, 60)
    ax.grid(axis='y', linestyle='--', alpha=0.3, color=COLOR_PRIMARY)

    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)

    plt.tight_layout()
    output_path = os.path.join(OUTPUT_DIR, "graphique_2_churn_remise_bienvenue.png")
    plt.savefig(output_path, dpi=300, facecolor=COLOR_BG)
    plt.close()
    print(f"Graphique 2 généré : {output_path}")


def generate_chart_3_acquisition_channels(customers_df):
    """
    Graphique 3 : Taux de churn comparé selon le canal d'acquisition.
    Titre-conclusion clair selon la charte.
    """
    fig, ax = plt.subplots(figsize=(10, 5.5), facecolor=COLOR_BG)
    ax.set_facecolor(COLOR_BG)

    channel_map = {
        'influencer': 'Influenceurs',
        'paid_social': 'Social payant (Meta)',
        'paid_search': 'Google Ads (Search)',
        'direct': 'Accès direct',
        'organic_search': 'SEO (Naturel)',
        'referral': 'Parrainage'
    }

    ch_stats = customers_df.groupby('channel_clean')['churned'].agg(['count', 'mean']).reset_index()
    ch_stats['channel_label'] = ch_stats['channel_clean'].map(channel_map)
    ch_stats['rate_pct'] = ch_stats['mean'] * 100
    ch_stats = ch_stats.sort_values('rate_pct', ascending=True)

    y = np.arange(len(ch_stats))
    rates = ch_stats['rate_pct'].values
    labels = [f"{lbl} ({cnt})" for lbl, cnt in zip(ch_stats['channel_label'], ch_stats['count'])]

    colors = []
    for code in ch_stats['channel_clean']:
        if code == 'influencer':
            colors.append(COLOR_ACCENT)
        elif code == 'referral':
            colors.append(COLOR_PRIMARY)
        elif code == 'paid_social':
            colors.append(COLOR_SECONDARY)
        else:
            colors.append(COLOR_MUTED)

    bars = ax.barh(y, rates, color=colors, height=0.55, edgecolor=COLOR_PRIMARY, linewidth=1)

    for bar, rate in zip(bars, rates):
        ax.text(bar.get_width() + 0.8, bar.get_y() + bar.get_height()/2, f"{rate:.1f} %",
                ha='left', va='center', fontsize=11, fontweight='bold', color=COLOR_PRIMARY)

    ax.set_title("L'influence et le social payant enregistrent les plus fortes pertes",
                 fontsize=13, fontweight='bold', pad=20, color=COLOR_PRIMARY)
    ax.set_xlabel("Taux de churn (%)", fontsize=11, fontweight='bold', labelpad=10)
    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=11)
    ax.set_xlim(0, 55)
    ax.grid(axis='x', linestyle='--', alpha=0.3, color=COLOR_PRIMARY)

    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)

    plt.tight_layout()
    output_path = os.path.join(OUTPUT_DIR, "graphique_3_churn_canaux_acquisition.png")
    plt.savefig(output_path, dpi=300, facecolor=COLOR_BG)
    plt.close()
    print(f"Graphique 3 généré : {output_path}")


def generate_chart_4_churn_reasons(customers_df):
    """
    Graphique 4 : Répartition des motifs déclarés par les clients partis.
    Titre-conclusion clair selon la charte.
    """
    fig, ax = plt.subplots(figsize=(10, 6), facecolor=COLOR_BG)
    ax.set_facecolor(COLOR_BG)

    churned_df = customers_df[customers_df['churned'] == 1]
    reasons_count = churned_df['churn_reason'].value_counts()

    reason_labels_fr = {
        'price': 'Prix trop élevé',
        'other': 'Autre raison',
        'delivery_issues': 'Problèmes de livraison',
        'switched_competitor': 'Passage à la concurrence',
        'pet_refused_food': 'Refus de la nourriture',
        'too_much_stock': 'Trop de croquettes en stock',
        'moved_to_vet_diet': 'Régime vétérinaire médical',
        'pet_deceased': 'Décès de l\'animal'
    }

    df_reasons = pd.DataFrame({
        'reason': reasons_count.index,
        'count': reasons_count.values,
        'label': [reason_labels_fr.get(k, k) for k in reasons_count.index]
    }).sort_values('count', ascending=True)

    y = np.arange(len(df_reasons))
    counts = df_reasons['count'].values
    labels = df_reasons['label'].values

    colors = []
    for r in df_reasons['reason']:
        if r == 'price':
            colors.append(COLOR_ACCENT)
        elif r in ['delivery_issues', 'pet_refused_food']:
            colors.append(COLOR_SECONDARY)
        elif r == 'switched_competitor':
            colors.append(COLOR_LIGHT_ACCENT)
        else:
            colors.append(COLOR_MUTED)

    bars = ax.barh(y, counts, color=colors, height=0.6, edgecolor=COLOR_PRIMARY, linewidth=1)

    total_known = counts.sum()
    for bar, count in zip(bars, counts):
        pct = (count / total_known) * 100
        ax.text(bar.get_width() + 2, bar.get_y() + bar.get_height()/2, f"{count} ({pct:.1f} %)",
                ha='left', va='center', fontsize=10, fontweight='bold', color=COLOR_PRIMARY)

    ax.set_title("Le prix et la logistique représentent 44 % des motifs de départ connus",
                 fontsize=13, fontweight='bold', pad=20, color=COLOR_PRIMARY)
    ax.set_xlabel(f"Nombre de départs déclarés (total connu = {total_known})", fontsize=11, fontweight='bold', labelpad=10)
    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=11)
    ax.set_xlim(0, 165)
    ax.grid(axis='x', linestyle='--', alpha=0.3, color=COLOR_PRIMARY)

    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)

    plt.tight_layout()
    output_path = os.path.join(OUTPUT_DIR, "graphique_4_motifs_depart_churn.png")
    plt.savefig(output_path, dpi=300, facecolor=COLOR_BG)
    plt.close()
    print(f"Graphique 4 généré : {output_path}")


def generate_chart_5_precursor_signals(customers_df):
    """
    Graphique 5 : Risque de churn selon les signaux précurseurs (sauts de livraison et tickets SAV).
    Titre-conclusion clair selon la charte.
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.5), facecolor=COLOR_BG)
    
    # 5a. Livraisons sautées (Abonnés uniquement)
    ax1.set_facecolor(COLOR_BG)
    sub_df = customers_df[customers_df['plan'] == 'subscription'].copy()
    skip_stats = sub_df.groupby('skipped_deliveries_90d')['churned'].agg(['count', 'mean']).reset_index()
    skip_stats['rate_pct'] = skip_stats['mean'] * 100

    labels_skip = [f"0 saut\n(n={int(skip_stats.loc[0, 'count'])})",
                   f"1 saut\n(n={int(skip_stats.loc[1, 'count'])})",
                   f"2 sauts\n(n={int(skip_stats.loc[2, 'count'])})"]
    x1 = np.arange(len(labels_skip))
    colors1 = [COLOR_PRIMARY, COLOR_SECONDARY, COLOR_ACCENT]
    bars1 = ax1.bar(x1, skip_stats['rate_pct'], color=colors1, width=0.5, edgecolor=COLOR_PRIMARY, linewidth=1)

    for bar, rate in zip(bars1, skip_stats['rate_pct']):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, f"{rate:.1f} %",
                 ha='center', va='bottom', fontsize=11, fontweight='bold', color=COLOR_PRIMARY)

    ax1.set_title("Livraisons décalées (90 j)\nRisque +143 % dès 2 sauts", fontsize=11, fontweight='bold', pad=12, color=COLOR_PRIMARY)
    ax1.set_ylabel("Taux de churn abonnés (%)", fontsize=10, fontweight='bold')
    ax1.set_xticks(x1)
    ax1.set_xticklabels(labels_skip, fontsize=10)
    ax1.set_ylim(0, 42)
    ax1.grid(axis='y', linestyle='--', alpha=0.3, color=COLOR_PRIMARY)
    for spine in ['top', 'right']:
        ax1.spines[spine].set_visible(False)

    # 5b. Tickets support sur 12 mois (Abonnés uniquement)
    ax2.set_facecolor(COLOR_BG)
    sub_df['ticket_group'] = pd.cut(sub_df['support_tickets_12m'], bins=[-1, 0, 1, 10], labels=['0 ticket', '1 ticket', '2+ tickets'])
    tick_stats = sub_df.groupby('ticket_group', observed=False)['churned'].agg(['count', 'mean']).reset_index()
    tick_stats['rate_pct'] = tick_stats['mean'] * 100

    labels_tick = [f"0 ticket\n(n={tick_stats.loc[0, 'count']})",
                   f"1 ticket\n(n={tick_stats.loc[1, 'count']})",
                   f"2+ tickets\n(n={tick_stats.loc[2, 'count']})"]
    x2 = np.arange(len(labels_tick))
    colors2 = [COLOR_PRIMARY, COLOR_SECONDARY, COLOR_ACCENT]
    bars2 = ax2.bar(x2, tick_stats['rate_pct'], color=colors2, width=0.5, edgecolor=COLOR_PRIMARY, linewidth=1)

    for bar, rate in zip(bars2, tick_stats['rate_pct']):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, f"{rate:.1f} %",
                 ha='center', va='bottom', fontsize=11, fontweight='bold', color=COLOR_PRIMARY)

    ax2.set_title("Tickets service client (12 m)\nRisque accru de 33 % dès 2 tickets", fontsize=11, fontweight='bold', pad=12, color=COLOR_PRIMARY)
    ax2.set_ylabel("Taux de churn abonnés (%)", fontsize=10, fontweight='bold')
    ax2.set_xticks(x2)
    ax2.set_xticklabels(labels_tick, fontsize=10)
    ax2.set_ylim(0, 42)
    ax2.grid(axis='y', linestyle='--', alpha=0.3, color=COLOR_PRIMARY)
    for spine in ['top', 'right']:
        ax2.spines[spine].set_visible(False)

    fig.suptitle("Décaler deux livraisons ou accumuler les tickets SAV double le risque de départ",
                 fontsize=13, fontweight='bold', y=1.02, color=COLOR_PRIMARY)

    plt.tight_layout()
    output_path = os.path.join(OUTPUT_DIR, "graphique_5_signaux_precurseurs.png")
    plt.savefig(output_path, dpi=300, facecolor=COLOR_BG, bbox_inches='tight')
    plt.close()
    print(f"Graphique 5 généré : {output_path}")


def generate_chart_6_salmon_crisis(customers_df, orders_df):
    """
    Graphique 6 : Focus sur l'impact de la recette Saumon Chat du 4 mai 2026.
    Titre-conclusion clair selon la charte.
    """
    fig, ax = plt.subplots(figsize=(9, 5.5), facecolor=COLOR_BG)
    ax.set_facecolor(COLOR_BG)

    # Acheteurs de saumon post-mai
    salmon_orders = orders_df[(orders_df['product_id'].isin(['P026', 'P027'])) & 
                              (orders_df['order_date_dt'] >= '2026-05-04')]
    salmon_custs = set(salmon_orders['customer_id'].unique())
    
    # Acheteurs chats autres recettes
    cat_custs = customers_df[customers_df['species_clean'] == 'cat']
    cat_other_custs = cat_custs[~cat_custs['customer_id'].isin(salmon_custs)]
    dog_custs = customers_df[customers_df['species_clean'] == 'dog']

    salmon_df = customers_df[customers_df['customer_id'].isin(salmon_custs)]

    groups = [
        ("Chiens (global)", float(dog_custs['churned'].mean()) * 100, len(dog_custs), COLOR_MUTED),
        ("Chats autres recettes", float(cat_other_custs['churned'].mean()) * 100, len(cat_other_custs), COLOR_PRIMARY),
        ("Chats Saumon post-4 mai", float(salmon_df['churned'].mean()) * 100, len(salmon_df), COLOR_ACCENT)
    ]

    labels = [f"{g[0]}\n(n={g[2]})" for g in groups]
    rates = [g[1] for g in groups]
    colors = [g[3] for g in groups]
    x = np.arange(len(groups))

    bars = ax.bar(x, rates, color=colors, width=0.5, edgecolor=COLOR_PRIMARY, linewidth=1)

    for bar, rate in zip(bars, rates):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1.5, f"{rate:.1f} %",
                ha='center', va='bottom', fontsize=12, fontweight='bold', color=COLOR_PRIMARY)

    ax.set_title("La nouvelle recette saumon chat culmine à 49 % de churn et 80 % des rejets",
                 fontsize=13, fontweight='bold', pad=20, color=COLOR_PRIMARY)
    ax.set_ylabel("Taux de churn (%)", fontsize=11, fontweight='bold', labelpad=10)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=11)
    ax.set_ylim(0, 65)
    ax.grid(axis='y', linestyle='--', alpha=0.3, color=COLOR_PRIMARY)

    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)

    plt.tight_layout()
    output_path = os.path.join(OUTPUT_DIR, "graphique_6_impact_recette_saumon.png")
    plt.savefig(output_path, dpi=300, facecolor=COLOR_BG)
    plt.close()
    print(f"Graphique 6 généré : {output_path}")


def main():
    print("--- Chargement des fichiers et dédoublonnage ---")
    customers_df, orders_df, products_df, marketing_df, support_df, duplicates_count = load_datasets()
    
    print("--- Calcul des indicateurs clés ---")
    metrics = compute_core_metrics(customers_df, orders_df)
    
    print("\n================ SYNTHÈSE DES MÉTRIQUES (DÉDOUBLONNÉES) ================")
    print(f"Clients uniques analysés : {metrics['global']['total_customers']} (après retrait de {duplicates_count} doublons)")
    print(f"Total churnés : {metrics['global']['total_churned']} ({metrics['global']['global_churn_rate']*100:.2f} %)")
    print(f"Churn Abonnement : {metrics['global']['by_plan']['subscription']['mean']*100:.2f} % (n={metrics['global']['by_plan']['subscription']['count']})")
    print(f"Churn Ponctuel : {metrics['global']['by_plan']['one_off']['mean']*100:.2f} % (n={metrics['global']['by_plan']['one_off']['count']})")
    
    print(f"\nCA total 12m (orders.csv) : {metrics['financials']['ca_total_12m']:.2f} €")
    print(f"CA perdu avec les churnés 12m : {metrics['financials']['ca_churned_12m']:.2f} € ({metrics['financials']['churned_ca_share_pct']:.2f} %)")
    print(f"  - Dont abonnés partis : {metrics['financials']['ca_churned_sub']:.2f} €")
    print(f"  - Dont ponctuels partis : {metrics['financials']['ca_churned_oneoff']:.2f} €")
    print(f"Dépense cumulée historique vie entière perdue : {metrics['financials']['lifetime_churned']:.2f} €")
    
    print("\n--- Génération des 6 graphiques conformes à la charte ---")
    generate_chart_1_monthly_churn(customers_df)
    generate_chart_2_welcome_discount(customers_df)
    generate_chart_3_acquisition_channels(customers_df)
    generate_chart_4_churn_reasons(customers_df)
    generate_chart_5_precursor_signals(customers_df)
    generate_chart_6_salmon_crisis(customers_df, orders_df)
    print("Tous les graphiques ont été régénérés avec succès.")
    
    print("\n--- Intégration dans le tableau de bord HTML ---")
    update_dashboard_html()


def update_dashboard_html():
    """
    Met à jour les images encodées en base64 dans le tableau de bord HTML autonome.
    Garantit une page sans dépendances locales manquantes lisible par la direction marketing.
    """
    if not os.path.exists(DASHBOARD_PATH):
        print(f"Avertissement : Le fichier {DASHBOARD_PATH} n'existe pas encore.")
        return

    chart_files = [
        "graphique_1_churn_mensuel_hausse_prix.png",
        "graphique_2_churn_remise_bienvenue.png",
        "graphique_3_churn_canaux_acquisition.png",
        "graphique_4_motifs_depart_churn.png",
        "graphique_5_signaux_precurseurs.png",
        "graphique_6_impact_recette_saumon.png"
    ]

    b64_images = []
    for cf in chart_files:
        fpath = os.path.join(OUTPUT_DIR, cf)
        if os.path.exists(fpath):
            with open(fpath, "rb") as img_file:
                b64_images.append(base64.b64encode(img_file.read()).decode('utf-8'))
        else:
            print(f"Erreur : image manquante {fpath}")
            return

    with open(DASHBOARD_PATH, "r", encoding="utf-8") as f:
        html_content = f.read()

    def replace_b64(match):
        idx = replace_b64.counter
        replace_b64.counter += 1
        if idx < len(b64_images):
            return f'src="data:image/png;base64,{b64_images[idx]}"'
        return match.group(0)

    replace_b64.counter = 0
    updated_html = re.sub(r'src="data:image/png;base64,[^"]+"', replace_b64, html_content)

    with open(DASHBOARD_PATH, "w", encoding="utf-8") as f:
        f.write(updated_html)

    print(f"Tableau de bord HTML autonome mis à jour avec les 6 graphiques intégrés : {DASHBOARD_PATH}")


if __name__ == "__main__":
    main()
