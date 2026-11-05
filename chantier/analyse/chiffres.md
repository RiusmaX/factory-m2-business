# Socle des chiffres clés de l'analyse du churn

Ce document consigne l'ensemble des métriques extraites et calculées des bases de données de Pattes & Papilles au 30 juin 2026. Conformément aux règles de l'usine, chaque valeur mentionne sa source exacte (fichier et calcul). Il constitue le référentiel chiffré unique pour le stratège, le rédacteur, le designer et le contrôleur.

---

## 1. Périmètre d'observation, représentativité et dédoublonnage

Conformément à la règle impérative de l'analyste (« *Supprime les doublons de customer_id avant tout calcul* »), le fichier brut `customers.csv` contenant 2 000 lignes a été assaini.

| Périmètre | Effectif brut | Doublons retirés | Effectif analysé | Source | Définition et méthode |
|---|---|---|---|---|---|
| Clients de l'échantillon | 2 000 lignes | 15 doublons stricts | **1 985 clients uniques** | `donnees/customers.csv` | `customers_raw.drop_duplicates(subset=['customer_id'])`. Les 15 doublons étaient des réplications parfaites de 15 identifiants clients. |
| Commandes associées (12 mois) | 23 184 lignes | 0 doublon | 12 673 commandes | `donnees/orders.csv` | Lignes de commandes entre le 1er juillet 2025 et le 30 juin 2026 associées aux clients de l'échantillon. |
| Portefeuille global actif | ~ 18 000 clients | - | 18 000 clients | `donnees/dictionnaire.md` (point 3) | Base totale des clients actifs à 12 mois de la marque (facteur multiplicateur de ~9,07 par rapport aux 1 985 clients uniques). |
| Portefeuille joignable e-mail | 13 200 clients | - | 13 200 clients | `corpus/barometre-clients-2026.md` (ligne 7) | Base interrogée lors du baromètre de satisfaction de mars 2026. |
| Part des abonnés dans l'échantillon | 65,10 % (brut) | - | **65,14 %** (1 293 / 1 985) | `donnees/customers.csv` | `(customers['plan'] == 'subscription').sum() / 1985` |
| Part des abonnés dans le portefeuille global | 44,00 % | - | 44,00 % | `corpus/barometre-clients-2026.md` (ligne 9) | Donnée de cadrage du baromètre de mars 2026. Surreprésentation voulue des abonnés dans l'échantillon. |

---

## 2. Taux de churn global et par formule

Le statut de départ (`churned = 1`) mesure les résiliations d'abonnements ou l'absence de réachat des clients ponctuels intervenues entre le 1er juillet et le 30 septembre 2026.

| Formule | Total clients | Clients churnés | Taux de churn | Fichier source et formule de calcul |
|---|---|---|---|---|
| **Global (échantillon assaini)** | **1 985** | **640** | **32,24 %** | `customers.csv` : `churned.sum() / len(customers)` (640 / 1 985) |
| *Rappel sur données brutes non dédoublonnées* | *2 000* | *647* | *32,35 %* | *Pour mémoire (647 / 2 000)* |
| **Abonnement (`subscription`)** | **1 293** | **197** | **15,24 %** | `customers.csv` : `churned[plan=='subscription'].sum() / 1293` |
| **Achat ponctuel (`one_off`)** | **692** | **443** | **64,02 %** | `customers.csv` : `churned[plan=='one_off'].sum() / 692` |

Le modèle économique d'abonnement protège la fidélité : le churn des clients sans abonnement (64,02 %) est 4,2 fois plus élevé que celui des abonnés (15,24 %).

---

## 3. Dynamique temporelle et rupture du 1er mars 2026

Le 1er mars 2026, Pattes & Papilles a augmenté ses tarifs de 5 %, puis a changé de prestataire de transport le 2 mars 2026.

### Selon la date de dernière commande (`last_order_date`)

| Période de dernière commande | Total clients | Churnés | Taux de churn | Fichier source et calcul |
|---|---|---|---|---|
| **Avant le 1er mars 2026** | **146** | **129** | **88,36 %** | `customers.csv` : `last_order_date < '2026-03-01'` |
| - Dont abonnés | 12 | 10 | 83,33 % | `customers.csv` : filtre `plan == 'subscription'` |
| - Dont achats ponctuels | 134 | 119 | 88,81 % | `customers.csv` : filtre `plan == 'one_off'` |
| **À partir du 1er mars 2026** | **1 839** | **511** | **27,79 %** | `customers.csv` : `last_order_date >= '2026-03-01'` |
| - Dont abonnés | 1 281 | 187 | 14,60 % | `customers.csv` : filtre `plan == 'subscription'` |
| - Dont achats ponctuels | 558 | 324 | 58,06 % | `customers.csv` : filtre `plan == 'one_off'` |

### Détail mensuel selon la dernière commande passée

| Mois de dernière commande | Total clients | Clients churnés | Taux de churn | Contexte opérationnel de la marque |
|---|---|---|---|---|
| Octobre 2025 | 1 | 1 | 100,00 % | Inactivité prolongée (> 8 mois) |
| Décembre 2025 | 8 | 8 | 100,00 % | Inactivité prolongée (> 6 mois) |
| Janvier 2026 | 64 | 59 | 92,19 % | Inactivité hivernale |
| Février 2026 | 73 | 61 | 83,56 % | Dernières commandes avant hausse tarifaire |
| Mars 2026 | 87 | 60 | 68,97 % | Hausse de 5 % et transition transporteur |
| Avril 2026 | 149 | 90 | 60,40 % | Retards de livraison et désorganisation logistique |
| Mai 2026 | 420 | 127 | 30,24 % | Lancement de la recette chat au saumon (4 mai) |
| Juin 2026 | 1 182 | 234 | 19,80 % | Commandes récentes à la date de clôture de la photo |
| Août 2026 | 1 | 0 | 0,00 % | Commande résiduelle post-périmètre (`PP-021844`) |

### Selon la cohorte d'inscription (`signup_date`)

| Cohorte d'inscription | Total clients | Churnés | Taux de churn | Fichier source et calcul |
|---|---|---|---|---|
| Inscrits avant le 1er mars 2026 | 1 621 | 450 | 27,76 % | `customers.csv` : `signup_date < '2026-03-01'` |
| Inscrits à partir du 1er mars 2026 | 364 | 190 | 52,20 % | `customers.csv` : `signup_date >= '2026-03-01'` |

Le churn des nouveaux inscrits ayant rejoint la marque après le 1er mars 2026 a presque doublé (+88 % d'augmentation relative, passant de 27,76 % à 52,20 %).

---

## 4. Churn par canal d'acquisition et coûts marketing

### Échantillon clients (`donnees/customers.csv`)

| Canal d'acquisition | Clients | Churnés | Taux de churn | Traitement de la donnée |
|---|---|---|---|---|
| `influencer` | 182 | 83 | **45,60 %** | Canal le plus volatil |
| `paid_social` (nettoyé) | 650 | 243 | **37,38 %** | Regroupe `paid_social` (643), `Facebook` (4) et `Paid Social` (3) |
| - `paid_social` (brut) | 643 | 241 | 37,48 % | Libellé normalisé |
| - `Facebook` (brut) | 4 | 1 | 25,00 % | Variante |
| - `Paid Social` (brut) | 3 | 1 | 33,33 % | Variante |
| `paid_search` | 368 | 122 | **33,15 %** | Google Ads |
| `direct` | 154 | 44 | **28,57 %** | Trafic direct / notoriété de marque |
| `organic_search` | 317 | 85 | **26,81 %** | Référencement naturel |
| `referral` | 314 | 63 | **20,06 %** | Parrainage : canal le plus fidèle et pérenne |

### Coûts d'acquisition globaux (`donnees/marketing_monthly.csv`)

| Période et canal | Dépenses (€) | Nouveaux clients | Coût d'acquisition (CAC) | Fichier source |
|---|---|---|---|---|
| Année 2025 complète (global) | 449 256 € | 7 485 clients | 60,02 € | `marketing_monthly.csv` (total 2025) |
| Premier semestre 2026 (global) | 242 451 € | 3 674 clients | 65,99 € | `marketing_monthly.csv` (janvier à juin 2026) |
| **Détail S1 2026 par canal :** | | | | |
| - `influencer` | 44 217 € | 441 clients | **100,27 €** | Canal le plus cher et le moins fidèle (45,6 % churn) |
| - `paid_social` | 134 943 € | 1 543 clients | **87,45 €** | Premier poste budgétaire, forte attrition (37,4 % churn) |
| - `paid_search` | 53 092 € | 735 clients | **72,23 €** | Coût d'acquisition intermédiaire |
| - `referral` | 10 199 € | 331 clients | **30,81 €** | Le canal le plus vertueux (faible coût, 20 % churn) |
| - `organic_search` | 0 € | 404 clients | **0,00 €** | Aucun achat d'espace |
| - `direct` | 0 € | 220 clients | **0,00 €** | Aucun achat d'espace |

---

## 5. Churn par espèce animale et formule

### Espèce de l'animal (`pet_species`)

| Espèce | Clients | Churnés | Taux de churn | Fichier source et traitement |
|---|---|---|---|---|
| **Chats (`cat` nettoyé)** | **830** | **328** | **39,52 %** | `customers.csv` : regroupe `cat` (825) et `chat` (5) |
| - `cat` (brut) | 825 | 328 | 39,76 % | Libellé anglais |
| - `chat` (brut) | 5 | 0 | 0,00 % | Variante française |
| **Chiens (`dog`)** | **1 155** | **312** | **27,01 %** | `customers.csv` : libellé unique |

Les possesseurs de chats subissent une attrition supérieure de 12,5 points à celle des propriétaires de chiens, directement exacerbée par les problématiques de néophobie et de transition alimentaire.

### Rythme de livraison des abonnés (`delivery_weeks`)

| Rythme d'expédition | Abonnés | Churnés | Taux de churn | Fichier source |
|---|---|---|---|---|
| 4 semaines | 374 | 49 | 13,10 % | `customers.csv` (`plan == 'subscription'`) |
| 5 semaines | 549 | 93 | 16,94 % | `customers.csv` (`plan == 'subscription'`) |
| 6 semaines | 370 | 55 | 14,86 % | `customers.csv` (`plan == 'subscription'`) |
| *Non renseigné (achats ponctuels)* | *692* | *443* | *64,02 %* | `customers.csv` (`delivery_weeks` vide par conception) |

---

## 6. Churn selon le niveau de remise de bienvenue

| Niveau de remise de bienvenue | Clients | Churnés | Taux de churn | Fichier source et observations |
|---|---|---|---|---|
| 0 % (aucune remise) | 614 | 166 | 27,04 % | `customers.csv` : `welcome_discount_pct == 0` |
| 20 % (parrainage ou code BIENVENUE20) | 901 | 243 | 26,97 % | `customers.csv` : `welcome_discount_pct == 20` |
| **30 % (code BIENVENUE30 / influenceurs)** | **470** | **231** | **49,15 %** | `customers.csv` : `welcome_discount_pct == 30` |

La remise de 30 % attire une population opportuniste ("chasseurs de promotions") dont le taux de churn atteint 49,15 %, soit un risque accru de 82 % par rapport aux remises de 20 % ou aux recrutements à plein tarif.

---

## 7. Signaux précurseurs de départ

### Livraisons sautées sur 90 jours (`skipped_deliveries_90d`)
*Champ réservé aux 1 293 abonnés ; vide pour les 692 achats ponctuels.*

| Nombre de sauts (90 j) | Effectif abonnés | Churnés | Taux de churn | Sur-risque relatif |
|---|---|---|---|---|
| 0 livraison décalée | 983 | 135 | 13,73 % | Base de référence |
| 1 livraison décalée | 292 | 56 | 19,18 % | +39,7 % de risque par rapport à 0 saut |
| **2 livraisons décalées** | **18** | **6** | **33,33 %** | **+142,7 % de risque** (taux multiplié par 2,43) |
| Moyenne globale sauts | 1 293 | 0,253 saut | Churnés : 0,345 saut vs Retenus : 0,236 saut (+46,2 %) |

### Retards de livraison sur 12 mois (`late_deliveries_12m`)

| Retards (12 mois) | Population | Effectif | Churnés | Taux de churn | Fichier source |
|---|---|---|---|---|---|
| 0 retard | Ensemble clients | 1 350 | 479 | 35,48 % | `customers.csv` |
| 1 retard | Ensemble clients | 510 | 139 | 27,25 % | `customers.csv` |
| 2 retards | Ensemble clients | 98 | 20 | 20,41 % | `customers.csv` |
| 3 retards | Ensemble clients | 25 | 2 | 8,00 % | `customers.csv` |
| 4 retards | Ensemble clients | 2 | 0 | 0,00 % | `customers.csv` |
| **Sous-ensemble Abonnés :** | | | | | |
| 0 retard | Abonnés | 745 | 116 | 15,57 % | `customers.csv` |
| 1 retard | Abonnés | 423 | 58 | 13,71 % | `customers.csv` |
| 2 retards | Abonnés | 98 | 21 | 21,43 % | Sur-risque de +38 % vs 0 retard |
| 3 ou 4 retards | Abonnés | 27 | 2 | 7,41 % | Volume résiduel très engagé |

*Note méthodologique : la variable mesure le cumul historique sur 12 mois. Les clients ponctuels ne passant qu'une commande n'ont pas l'opportunité de cumuler des retards mais churnent fortement par nature.*

### Réclamations au service client sur 12 mois (`support_tickets_12m`)

| Tickets support (12 mois) | Population | Effectif | Churnés | Taux de churn | Fichier source |
|---|---|---|---|---|---|
| 0 ticket | Abonnés | 816 | 117 | 14,34 % | `customers.csv` |
| 1 ticket | Abonnés | 319 | 50 | 15,67 % | `customers.csv` |
| 2 tickets | Abonnés | 115 | 21 | 18,26 % | Sur-risque de +27,3 % |
| 3 tickets et plus | Abonnés | 43 | 9 | 20,93 % | Sur-risque de +46,0 % |
| Moyenne tickets abonnés | Abonnés | 1 293 | Churnés : 0,619 ticket vs Retenus : 0,516 ticket (+20,0 %) |

### Note du dernier avis déposé (`last_review_score`)
*Renseignée pour 878 clients uniques sur 1 985 (1 107 clients sans avis déposé).*

| Note déposée | Effectif | Churnés | Taux de churn | Interprétation |
|---|---|---|---|---|
| 1 étoile | 8 | 3 | 37,50 % | Forte insatisfaction |
| 2 étoiles | 50 | 22 | 44,00 % | Forte insatisfaction |
| **Total 1 et 2 étoiles** | **58** | **25** | **43,10 %** | **Niveau d'attrition maximal** |
| 3 étoiles | 191 | 73 | 38,22 % | Satisfaction mitigée |
| 4 étoiles | 323 | 107 | 33,13 % | Satisfaction moyenne |
| 5 étoiles | 306 | 72 | 23,53 % | Clients promoteurs |
| Note moyenne globale | 878 | 3,99 / 5 | Churnés : 3,81 / 5 vs Retenus : 4,08 / 5 |

### Taux d'ouverture des e-mails sur 90 jours (`email_open_rate_90d`)
*Renseigné pour les 1 188 clients uniques inscrits à la newsletter (`newsletter_optin == 'yes'`).*

- Moyenne des clients fidèles (`churned = 0`) : **48,87 %** (médiane 49,0 %)
- Moyenne des clients churnés (`churned = 1`) : **38,99 %** (médiane 38,0 %)
- Décrochage mesuré : baisse de **9,88 points** d'engagement par e-mail chez les futurs résiliataires.

---

## 8. Motifs de départ déclarés (`churn_reason`)

Sur les 640 clients churnés uniques, **522 ont déclaré un motif explicite** (118 départs sans motif renseigné, soit 18,44 %).

| Rang | Motif de résiliation | Clients | Part des départs connus (n=522) | Part du churn total (n=640) | Analyse de la cause opérationnelle |
|---|---|---|---|---|---|
| 1 | `price` | **142** | **27,20 %** | **22,19 %** | Prix jugé trop élevé suite à la hausse de 5 % du 1er mars |
| 2 | `other` | 94 | 18,01 % | 14,69 % | Motifs divers non catégorisés |
| 3 | `delivery_issues` | **86** | **16,48 %** | **13,44 %** | Retards et avaries du nouveau transporteur (2 mars) |
| 4 | `switched_competitor` | 85 | 16,28 % | 13,28 % | Défection au profit d'un concurrent |
| 5 | `pet_refused_food` | **75** | **14,37 %** | **11,72 %** | Rejet alimentaire (crise de la recette chat au saumon) |
| 6 | `too_much_stock` | 23 | 4,41 % | 3,59 % | Rythme de livraison inadapté / accumulation |
| 7 | `moved_to_vet_diet` | 9 | 1,72 % | 1,41 % | Pathologie nécessitant une alimentation médicalisée |
| 8 | `pet_deceased` | 8 | 1,53 % | 1,25 % | Décès de l'animal de compagnie |
| - | *Non renseigné* | 118 | - | 18,44 % | Résiliation sans réponse à l'enquête |

Les trois causes directement activables par l'entreprise (`price`, `delivery_issues`, `pet_refused_food`) totalisent **303 départs**, soit **58,05 % des motifs exprimés**.

---

## 9. Focus spécifique : la crise de la recette chat au saumon (4 mai 2026)

Le 4 mai 2026, Pattes & Papilles a modifié la composition de ses croquettes chat au saumon (`products.csv` : références `P026` 1,5 kg et `P027` 3 kg).

| Métrique d'impact | Valeur | Fichier et formule de calcul |
|---|---|---|
| Clients uniques ayant commandé du saumon post-4 mai | **241 clients** | `orders.csv` : `product_id.isin(['P026', 'P027'])` et `order_date >= '2026-05-04'` croisé avec `customers.csv` |
| Clients churnés dans cette cohorte | **119 clients** | `customers.csv` : `churned == 1` parmi ces 241 clients |
| **Taux de churn de la cohorte Saumon post-mai** | **49,38 %** | Calcul : 119 / 241 (vs 27,0 % pour les chiens et 39,5 % pour l'ensemble des chats) |
| Clients ayant résilié pour motif `pet_refused_food` dans ce groupe | **60 clients** | `customers.csv` : `churn_reason == 'pet_refused_food'` parmi ces 241 clients |
| Total des départs pour `pet_refused_food` sur tout l'échantillon | 75 clients | `customers.csv` : `(churn_reason == 'pet_refused_food').sum()` |
| **Part du saumon post-mai dans tous les refus alimentaires** | **80,00 %** | Calcul : 60 / 75. Exactement 4 départs sur 5 pour rejet de nourriture sont imputables à cette seule recette. |
| Demandes de remboursement d'articles (`quantity < 0`) | 14 remboursements | `orders.csv` : 7 remboursements sur `P026` et 7 sur `P027`. Ces deux références sont les plus remboursées de toute la marque. |

---

## 10. Churn selon le niveau de revenu du foyer (`household_income_band`)

La directrice marketing s'interrogeait sur l'impact de la hausse tarifaire de 5 % sur les foyers modestes.

| Tranche de revenu mensuel net | Clients | Churnés | Taux de churn | Écart à la moyenne globale |
|---|---|---|---|---|
| **Moins de 2 000 € (`<2000`)** | **239** | **102** | **42,68 %** | **+10,44 points** vs moyenne globale (32,24 %) |
| De 2 000 à 3 000 € (`2000-3000`) | 412 | 120 | 29,13 % | -3,11 points vs moyenne globale |
| De 3 000 à 4 500 € (`3000-4500`) | 462 | 130 | 28,14 % | -4,10 points vs moyenne globale |
| Plus de 4 500 € (`>4500`) | 282 | 93 | 32,98 % | +0,74 point vs moyenne globale |
| Non renseigné / non apparié | 590 | 195 | 33,05 % | Équivalent à la moyenne globale |

La sensibilité au prix est confirmée empiriquement : le taux de churn des ménages gagnant moins de 2 000 € par mois est supérieur de 14,54 points à celui de la tranche 3 000-4 500 €.

---

## 11. Chiffre d'affaires perdu et impact financier

### Chiffre d'affaires sur 12 mois glissants (`donnees/orders.csv`)
*Période d'observation : du 1er juillet 2025 au 30 juin 2026 inclus.*

| Indicateur financier | Montant (€ TTC) | Part du total | Source et formule de calcul |
|---|---|---|---|
| CA total 12 mois de l'échantillon | **810 532,63 €** | 100,00 % | `orders.csv` : somme de `line_total_eur` sur la période 12 mois |
| CA des clients conservés (`churned = 0`) | 656 925,18 € | 81,05 % | `orders.csv` croisé avec `customers.csv` (`churned == 0`) |
| **CA annuel perdu avec les clients partis (`churned = 1`)** | **153 607,45 €** | **18,95 %** | `orders.csv` croisé avec `customers.csv` (`churned == 1`) |
| - Dont abonnés résiliés (197 clients) | 81 820,63 € | 53,27 % de la perte | Dépense annuelle moyenne : 415,33 € par abonné parti |
| - Dont achats ponctuels partis (443 clients) | 71 786,82 € | 46,73 % de la perte | Dépense annuelle moyenne : 162,05 € par ponctuel parti |

*Note de complétude : 2 commandes résiduelles de juillet et novembre 2026 (53,82 € passées par des clients fidèles) portent le total exhaustif du fichier à 810 586,45 €.*

### Dépense totale cumulée vie entière (`donnees/customers.csv`)

| Indicateur lifetime | Montant (€ TTC) | Source et calcul |
|---|---|---|
| Dépense cumulée totale (1 985 clients uniques) | 2 018 989,01 € | `customers.csv` : somme de `total_spent_eur` |
| Dépense cumulée des 1 345 clients fidèles | 1 697 884,70 € | `customers.csv` : `total_spent_eur[churned == 0].sum()` |
| **Dépense cumulée des 640 clients partis** | **321 104,31 €** | `customers.csv` : `total_spent_eur[churned == 1].sum()` |
| - Dont 197 abonnés résiliés | 218 527,27 € | Dépense moyenne vie entière : 1 109,28 € par abonné |
| - Dont 443 clients ponctuels partis | 102 577,04 € | Dépense moyenne vie entière : 231,55 € par ponctuel |

### Clés d'extrapolation pour le business case

1. **Extrapolation brute au ratio de portefeuille (×9,07) :**
   - Rapport entre les 18 000 clients actifs et l'échantillon de 1 985 clients : facteur de 9,068.
   - Perte annuelle brute extrapolée : 153 607,45 € × 9,068 = **1 392 908 €**.
2. **Pondération nécessaire par la structure réelle du portefeuille :**
   - L'échantillon comporte 65,14 % d'abonnés, alors que le portefeuille global réel n'en compte que 44,00 % (`corpus/barometre-clients-2026.md`, ligne 9).
   - Le stratège devra appliquer un redressement de structure pour pondérer la perte des abonnés (panier annuel de 415,33 €) et celle des ponctuels (162,05 €).

---

## 12. Profil des 20 clients à risque prioritaires (`donnees/abonnes_support.csv`)

Le fichier `abonnes_support.csv` répertorie 20 clients à risque critique désignés pour une intervention personnalisée d'urgence.

| Caractéristique | Répartition | Détail des profils |
|---|---|---|
| Formule d'achat | 10 abonnements, 10 achats ponctuels | Le plan relationnel doit adapter sa posture aux 10 acheteurs sans formule récurrente |
| Espèce animale | 13 chats (65 %), 7 chiens (35 %) | Surreprésentation massive des félins, cohérente avec la crise du saumon |
| Segments relationnels | 7 « En sommeil »<br>4 « Nouveaux ou occasionnels récents »<br>4 « À risque (bons clients qui s'éloignent) »<br>3 « Fidèles »<br>2 « Champions » | Les clients « Champions » (`PP-013744`, `PP-017578`) et « Fidèles » (`PP-011401`, `PP-012566`, `PP-015094`) représentent une valeur stratégique maximale |
| Signaux d'alerte déclarés | 5 « une seule commande »<br>4 « commandes qui s'espacent »<br>4 « un retard ou une réclamation récente »<br>3 « contacts fréquents au support »<br>2 « livraisons en retard répétées »<br>1 « aucune commande depuis 176 jours »<br>1 « ouvre peu les e-mails (18 %) » | Les incidents logistiques et les sollicitations SAV répétées constituent les alertes majeures |

---

## 13. Ce que les données ne permettent pas de dire

Conformément à la règle méthodologique de l'analyste, voici les limites strictes du jeu de données et ce qu'il est rigoureusement interdit d'extrapoler sans hypothèses documentées :

1. **Absence de marge unitaire et de rentabilité nette :**
   - `products.csv` indique uniquement le prix de vente catalogue TTC (`price_eur`). Aucun coût de revient (COGS), aucun coût matière, ni aucune marge brute unitaire ne figurent dans les données.
   - Par conséquent, il est impossible de calculer la perte de marge nette sans une hypothèse explicite posée par le stratège (ex. marge brute standard de 60 % ou 65 %).

2. **Absence des coûts logistiques et SAV unitaires :**
   - Les fichiers ne mentionnent ni le coût d'une livraison standard, ni le surcoût d'un retard, ni le coût unitaire de traitement d'un ticket de support client, ni le coût d'une réexpédition ou d'un dédommagement.
   - Les coûts du service client et du transporteur ne peuvent être modélisés que par des hypothèses paramétriques externes.

3. **Biais d'échantillonnage de la base clients :**
   - L'échantillon de 1 985 clients n'est pas un miroir parfait des 18 000 clients actifs de la marque. Il surreprésente délibérément les abonnés (65,14 % contre 44,00 % dans le baromètre global). Toute extrapolation directe sans redressement biaise l'estimation vers le haut.

4. **Variables structurellement non renseignées pour les clients ponctuels :**
   - Les colonnes `skipped_deliveries_90d` et `delivery_weeks` sont vides (`NaN`) pour les achats ponctuels (`one_off`). Ces valeurs manquantes traduisent une inapplicabilité fonctionnelle et ne doivent en aucun cas être traitées comme des valeurs nulles (0).

5. **Complétude partielle des avis et des revenus :**
   - La note d'avis (`last_review_score`) n'est renseignée que pour 878 clients sur 1 985 (44,2 %). Les répondants présentent un biais d'auto-sélection (surreprésentation des avis très positifs ou très négatifs).
   - La tranche de revenu (`household_income_band`) est manquante pour 590 clients (29,7 %) et provient d'un fichier courtier de 2025 estimé, non d'une déclaration fiscale certifiée.

6. **Absence du texte des réclamations et des échanges support :**
   - `customers.csv` fournit uniquement le nombre de tickets support (`support_tickets_12m`), sans détail textuel ni motif qualitatif. En dehors de `churn_reason` renseigné lors de la résiliation, le contenu précis des litiges SAV reste inaccessible dans les données tabulaires.

7. **Causalité vs corrélation :**
   - La concordance temporelle entre la hausse de prix du 1er mars, la bascule transporteur du 2 mars et l'augmentation des départs démontre une corrélation forte, mais les données ne mesurent pas les facteurs exogènes (inflation générale, concurrence extérieure accrue, saisonnalité estivale).
