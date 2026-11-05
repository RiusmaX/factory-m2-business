# Script de contrôle indépendant et de recalcul exhaustif des chiffres
# Antigravity - Rôle Contrôleur des chiffres
# Ce script lit exclusivement donnees/ et vérifie la totalité des chiffres cités.

import pandas as pd
import numpy as np

def run_audit():
    print("================================================================================")
    print("AUDIT INDÉPENDANT DES CHIFFRES - PATTES & PAPILLES")
    print("================================================================================\n")

    # 1. Chargement des données brutes
    customers_raw = pd.read_csv('donnees/customers.csv')
    orders_raw = pd.read_csv('donnees/orders.csv')
    products_raw = pd.read_csv('donnees/products.csv')
    marketing_raw = pd.read_csv('donnees/marketing_monthly.csv')
    abonnes_support_raw = pd.read_csv('donnees/abonnes_support.csv')

    # Dédoublonnage
    customers_unique = customers_raw.drop_duplicates(subset=['customer_id']).copy()
    orders_unique = orders_raw[orders_raw['customer_id'].isin(customers_unique['customer_id'])].copy()

    # Normalisation des libellés de canaux
    customers_unique['clean_channel'] = customers_unique['acquisition_channel'].replace({
        'Paid Social': 'paid_social',
        'Facebook': 'paid_social'
    })

    # Normalisation des espèces
    customers_unique['clean_species'] = customers_unique['pet_species'].replace({
        'chat': 'cat'
    })

    # 2. Vérification des volumes de base
    print("--- 1. VOLUMES DE BASE ---")
    print(f"Lignes brutes customers : {len(customers_raw)}")
    print(f"Doublons supprimés : {len(customers_raw) - len(customers_unique)}")
    print(f"Clients uniques : {len(customers_unique)}")
    print(f"Lignes orders : {len(orders_raw)}")
    print(f"Commandes uniques (order_id) : {orders_raw['order_id'].nunique()}")

    # 3. Répartition abonnés / ponctuels et Churn
    print("\n--- 2. CHURN PAR FORMULE (PLAN) ---")
    total_clients = len(customers_unique)
    total_churn = customers_unique['churned'].sum()
    print(f"Total clients : {total_clients}, Départs : {total_churn}, Taux global : {total_churn/total_clients:.4%}")

    sub = customers_unique[customers_unique['plan'] == 'subscription']
    sub_count = len(sub)
    sub_churn = sub['churned'].sum()
    sub_rate = sub_churn / sub_count
    print(f"Abonnés : {sub_count} ({sub_count/total_clients:.4%}), Départs : {sub_churn}, Taux : {sub_rate:.4%}")

    oneoff = customers_unique[customers_unique['plan'] == 'one_off']
    oneoff_count = len(oneoff)
    oneoff_churn = oneoff['churned'].sum()
    oneoff_rate = oneoff_churn / oneoff_count
    print(f"Ponctuels : {oneoff_count} ({oneoff_count/total_clients:.4%}), Départs : {oneoff_churn}, Taux : {oneoff_rate:.4%}")
    print(f"Ratio churn ponctuel vs abonné : {oneoff_rate / sub_rate:.4f}")

    # 4. Rupture de mars 2026
    print("\n--- 3. DATE D'INSCRIPTION ---")
    customers_unique['signup_dt'] = pd.to_datetime(customers_unique['signup_date'])
    pre_mar = customers_unique[customers_unique['signup_dt'] < '2026-03-01']
    post_mar = customers_unique[customers_unique['signup_dt'] >= '2026-03-01']
    print(f"Pré-mars : {len(pre_mar)} clients, {pre_mar['churned'].sum()} départs, Taux : {pre_mar['churned'].mean():.4%}")
    print(f"Post-mars : {len(post_mar)} clients, {post_mar['churned'].sum()} départs, Taux : {post_mar['churned'].mean():.4%}")
    print(f"Hausse relative : {(post_mar['churned'].mean() - pre_mar['churned'].mean()) / pre_mar['churned'].mean():.4%}")

    # 5. Canaux d'acquisition et CAC S1 2026
    print("\n--- 4. CANAUX D'ACQUISITION & CAC S1 2026 ---")
    marketing_s1 = marketing_raw[(marketing_raw['month'] >= '2026-01') & (marketing_raw['month'] <= '2026-06')]
    cac = marketing_s1.groupby('channel').agg(spend=('spend_eur', 'sum'), new_cust=('new_customers', 'sum')).reset_index()
    cac['cac_eur'] = np.where(cac['new_cust'] > 0, cac['spend'] / cac['new_cust'], 0.0)

    for ch, grp in customers_unique.groupby('clean_channel'):
        c_count = len(grp)
        c_churn = grp['churned'].sum()
        c_rate = c_churn / c_count
        cac_val = cac[cac['channel'] == ch]['cac_eur'].values[0] if len(cac[cac['channel'] == ch]) > 0 else 0.0
        print(f"Canal {ch:15s} | Clients: {c_count:4d} | Churn: {c_churn:3d} ({c_rate:6.2%}) | CAC S1: {cac_val:6.2f} €")

    # 6. Remise de bienvenue
    print("\n--- 5. REMISE DE BIENVENUE ---")
    for disc, grp in customers_unique.groupby('welcome_discount_pct'):
        d_count = len(grp)
        d_churn = grp['churned'].sum()
        d_rate = d_churn / d_count
        print(f"Remise {disc:2d}% | Clients: {d_count:4d} | Churn: {d_churn:3d} ({d_rate:6.2%})")

    # 7. Espèce
    print("\n--- 6. ESPÈCE ANIMALE ---")
    for sp, grp in customers_unique.groupby('clean_species'):
        s_count = len(grp)
        s_churn = grp['churned'].sum()
        s_rate = s_churn / s_count
        print(f"Espèce {sp:4s} | Clients: {s_count:4d} | Churn: {s_churn:3d} ({s_rate:6.2%})")

    # 8. Signaux précurseurs (abonnés)
    print("\n--- 7. SIGNAUX PRÉCURSEURS (ABONNÉS) ---")
    print("Sauts de livraison 90j :")
    for sk, grp in sub.groupby('skipped_deliveries_90d'):
        print(f"  Saut {sk:.0f} | Clients: {len(grp):4d} | Churn: {grp['churned'].sum():3d} ({grp['churned'].mean():6.2%})")
    print(f"  Total >= 1 saut : {len(sub[sub['skipped_deliveries_90d'] >= 1])} ({len(sub[sub['skipped_deliveries_90d'] >= 1])/len(sub):.2%})")

    print("Retards subis 12m :")
    for lt, grp in sub.groupby('late_deliveries_12m'):
        print(f"  Retard {lt:.0f} | Clients: {len(grp):4d} | Churn: {grp['churned'].sum():3d} ({grp['churned'].mean():6.2%})")
    print(f"  Total >= 2 retards : {len(sub[sub['late_deliveries_12m'] >= 2])}")

    print("Réclamations support 12m :")
    for tk, grp in sub.groupby('support_tickets_12m'):
        print(f"  Tickets {tk:.0f} | Clients: {len(grp):4d} | Churn: {grp['churned'].sum():3d} ({grp['churned'].mean():6.2%})")
    print(f"  Total >= 2 tickets : {len(sub[sub['support_tickets_12m'] >= 2])}")
    print(f"  Total >= 3 tickets : {len(sub[sub['support_tickets_12m'] >= 3])}")

    print("Avis clients (1-2 étoiles) :")
    rev = customers_unique[customers_unique['last_review_score'].notna()]
    rev_low = rev[rev['last_review_score'].isin([1, 2])]
    print(f"  Répondants : {len(rev)} ({len(rev)/len(customers_unique):.2%})")
    print(f"  Avis 1-2 étoiles : {len(rev_low)} | Churn : {rev_low['churned'].sum()} ({rev_low['churned'].mean():6.2%})")

    print("Ouverture e-mails :")
    news = customers_unique[customers_unique['newsletter_optin'] == 'yes']
    open_loyal = news[news['churned'] == 0]['email_open_rate_90d'].mean()
    open_churn = news[news['churned'] == 1]['email_open_rate_90d'].mean()
    print(f"  Inscrits : {len(news)} | Fidèles: {open_loyal:.2%} | Churnés: {open_churn:.2%} | Chute: {(open_loyal - open_churn)*100:.2f} pts")

    # 9. Motifs déclarés
    print("\n--- 8. MOTIFS DÉCLARÉS ---")
    reasons = customers_unique[customers_unique['churned'] == 1]['churn_reason'].dropna()
    print(f"Total motifs connus : {len(reasons)}")
    for r, count in reasons.value_counts().items():
        print(f"  Motif {r:20s} : {count:3d} ({count/len(reasons):6.2%})")

    # 10. Recette Saumon
    print("\n--- 9. RECETTE SAUMON (P026, P027) APRÈS 4 MAI ---")
    orders_unique['order_dt'] = pd.to_datetime(orders_unique['order_date'])
    salm_orders = orders_unique[(orders_unique['product_id'].isin(['P026', 'P027'])) & (orders_unique['order_dt'] >= '2026-05-04')]
    salm_cust_ids = salm_orders['customer_id'].unique()
    salm_cust = customers_unique[customers_unique['customer_id'].isin(salm_cust_ids)]
    salm_churn = salm_cust['churned'].sum()
    salm_refused = (salm_cust['churn_reason'] == 'pet_refused_food').sum()
    all_refused = (customers_unique['churn_reason'] == 'pet_refused_food').sum()
    salm_refunds = orders_unique[(orders_unique['product_id'].isin(['P026', 'P027'])) & (orders_unique['quantity'] < 0)]
    print(f"  Clients saumon post-mai : {len(salm_cust)}")
    print(f"  Départs : {salm_churn} ({salm_churn/len(salm_cust):.2%})")
    print(f"  Motif pet_refused_food : {salm_refused} sur {all_refused} au total ({salm_refused/all_refused:.2%})")
    print(f"  Demandes de remboursement P026/P027 : {len(salm_refunds)}")

    # 11. Revenus modestes (< 2000 €)
    print("\n--- 10. FOYERS MODESTES (< 2 000 €) ---")
    low_inc = customers_unique[customers_unique['household_income_band'] == '<2000']
    print(f"  Clients : {len(low_inc)}, Départs : {low_inc['churned'].sum()} ({low_inc['churned'].mean():.2%})")

    # 12. Impact financier sur l'échantillon
    print("\n--- 11. IMPACT FINANCIER ÉCHANTILLON ---")
    ca_total = orders_unique['line_total_eur'].sum()
    sub_churn_ids = sub[sub['churned'] == 1]['customer_id']
    oneoff_churn_ids = oneoff[oneoff['churned'] == 1]['customer_id']
    ca_sub_churn = orders_unique[orders_unique['customer_id'].isin(sub_churn_ids)]['line_total_eur'].sum()
    ca_oneoff_churn = orders_unique[orders_unique['customer_id'].isin(oneoff_churn_ids)]['line_total_eur'].sum()
    print(f"  CA total 12m commandes : {ca_total:.2f} €")
    print(f"  CA perdu abonnés (197 clients) : {ca_sub_churn:.2f} € (Panier moyen: {ca_sub_churn/len(sub_churn_ids):.2f} €)")
    print(f"  CA perdu ponctuels (443 clients) : {ca_oneoff_churn:.2f} € (Panier moyen: {ca_oneoff_churn/len(oneoff_churn_ids):.2f} €)")
    print(f"  Total CA annuel perdu : {ca_sub_churn + ca_oneoff_churn:.2f} € ({ (ca_sub_churn + ca_oneoff_churn)/ca_total:.2%})")

    # 13. Business Case
    print("\n--- 12. BUSINESS CASE (PORTFOLIO 18 000 CLIENTS) ---")
    n_active = 18000
    n_sub_active = 18000 * 0.44
    n_oneoff_active = 18000 * 0.56
    basket_sub = ca_sub_churn / len(sub_churn_ids)
    basket_oneoff = ca_oneoff_churn / len(oneoff_churn_ids)
    spontaneous_sub_churn = n_sub_active * (len(sub_churn_ids) / len(sub))
    loss_tendential = spontaneous_sub_churn * basket_sub
    print(f"  Abonnés actifs réels : {n_sub_active:.0f}")
    print(f"  Ponctuels actifs réels : {n_oneoff_active:.0f}")
    print(f"  Départs spontanés abonnés : {spontaneous_sub_churn:.2f} (arrondi à {round(spontaneous_sub_churn)})")
    print(f"  Perte tendancielle abonnés : {loss_tendential:.2f} €")

    # Scénario prudent
    saved_sub_p = round(round(spontaneous_sub_churn) * 0.15)
    ca_sub_saved_p = saved_sub_p * 415.33
    conv_oneoff_p = round(n_oneoff_active * 0.02)
    ca_conv_p = conv_oneoff_p * 415.33
    total_ca_p = ca_sub_saved_p + ca_conv_p
    margin_p = total_ca_p * 0.60
    net_p = margin_p - 30000
    roi_p = net_p / 30000
    print(f"  Scénario prudent : CA = {total_ca_p:.2f} €, Marge = {margin_p:.2f} €, Net = {net_p:.2f} €, ROI = {roi_p:.2%}")

    # Scénario central
    saved_sub_c = round(round(spontaneous_sub_churn) * 0.25)
    ca_sub_saved_c = saved_sub_c * 415.33
    conv_oneoff_c = round(n_oneoff_active * 0.04)
    ca_conv_c = conv_oneoff_c * 415.33
    total_ca_c = ca_sub_saved_c + ca_conv_c
    margin_c = total_ca_c * 0.60
    net_c = margin_c - 30000
    roi_c = net_c / 30000
    print(f"  Scénario central : CA = {total_ca_c:.2f} €, Marge = {margin_c:.2f} €, Net = {net_c:.2f} €, ROI = {roi_c:.2%}")

if __name__ == '__main__':
    run_audit()
