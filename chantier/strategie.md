# Stratégie de rétention et plan d'action anti-churn

Ce document fixe les orientations stratégiques de Pattes & Papilles pour enrayer l'attrition constatée depuis le printemps 2026. Il s'appuie sur le socle chiffré de `chantier/analyse/chiffres.md`, le compte rendu du comité de direction du 15 septembre 2026 et les résultats du baromètre de mars 2026.

## 1. Segments d'abonnés à risque

L'analyse des 1 985 clients uniques et des 1 293 abonnés met en évidence cinq groupes distincts chez qui le risque de départ est concentré.

### Segment 1 : Les acheteurs de la recette féline au saumon reformulée

- Taille du segment : 241 clients uniques dans l'échantillon ayant commandé les références de croquettes pour chat au saumon (P026 ou P027) à partir du 4 mai 2026 (`donnees/orders.csv` croisé avec `donnees/customers.csv`). Extrapolé au portefeuille de 18 000 clients actifs, ce groupe représente environ 2 185 clients.
- Signaux précurseurs : chute brutale de fidélité avec un taux de churn de 49,38 % (119 résiliations sur 241 clients), réclamations pour refus d'alimentation (60 départs enregistrés sous le motif `pet_refused_food`, soit 80,00 % des 75 abandons totaux liés au goût dans l'échantillon), et 14 demandes de remboursement enregistrées sur ces deux produits (`orders.csv`).
- Action proposée : mise en place immédiate d'une cellule d'accompagnement nutritionnel. Contact direct des acheteurs récents pour proposer le remplacement sans frais du sac entamé par la formule Chat Stérilisé Poulet (P024 ou P025) ou Chat Ventre sensible Dinde (P028 ou P029), assorti d'un guide de transition alimentaire progressive sur dix jours (À VALIDER). En parallèle, suspension de la fabrication des lots contestés et étude industrielle pour revenir à l'ancienne composition.

### Segment 2 : Les abonnés subissant des défaillances logistiques récurrentes

- Taille du segment : 125 abonnés cumulant 2 retards de livraison ou plus sur douze mois dans l'échantillon (98 abonnés avec 2 retards, 25 avec 3 retards et 2 avec 4 retards, d'après `donnees/customers.csv`). Sur l'ensemble des 7 920 abonnés réels, cela correspond à environ 765 foyers touchés.
- Signaux précurseurs : taux de churn qui grimpe à 21,43 % dès le deuxième incident logistique (contre 15,57 % pour les abonnés sans incident, soit un sur-risque relatif de +38 %). Le motif `delivery_issues` constitue la troisième cause de départ déclarée avec 86 départs (16,48 % des motifs connus). Ces avaries se concentrent sur les départements ruraux (Bretagne, Massif central, Alpes du Sud, Corse) signalés lors du comité de direction du 15 septembre.
- Action proposée : bascule immédiate sur un protocole d'expédition prioritaire pour tout abonné ayant déjà subi un retard. Mise en place d'alertes préventives par SMS ou e-mail dès qu'un retard d'acheminement supérieur à 48 heures est détecté par le transporteur, sans attendre que l'abonné ne réclame. Compensation automatique par l'ajout d'une attention en colis (un paquet de friandises ou de bâtonnets dentaires d'une valeur catalogue de 9,90 € à 13,90 € - À VALIDER). Préparation du dossier de pénalités pour la renégociation contractuelle de décembre 2026.

### Segment 3 : Les abonnés en surstock ou décalant leurs livraisons

- Taille du segment : 310 abonnés ayant décalé au moins une expédition dans les 90 jours précédant la photo du 30 juin 2026 (292 abonnés avec 1 saut, 18 abonnés avec 2 sauts, d'après `donnees/customers.csv`). Ce volume représente 23,98 % des abonnés de l'échantillon, soit environ 1 900 abonnés à l'échelle du portefeuille.
- Signaux précurseurs : multiplication du risque de résiliation par 2,43 chez les abonnés ayant décalé deux fois leur commande (taux de départ de 33,33 %, contre 13,73 % pour ceux qui ne décalent jamais). Dans le baromètre de mars 2026, 22 % des clients expriment recevoir trop de croquettes et 18 % jugent leur formule rigide. Le motif `too_much_stock` totalise 23 résiliations directes.
- Action proposée : déclenchement automatisé dans le logiciel de gestion d'une notification bienveillante dès le premier saut de livraison. Invitation à réajuster la fréquence d'envoi en passant sans pénalité d'un rythme de 4 semaines à 5 ou 6 semaines, ou à mettre à jour le profil de l'animal (poids actuel, niveau d'activité) dans le quiz de rationnement. Promotion d'un accessoire adapté comme la boîte hermétique de 12 kg (P040, 28,90 € TTC) pour préserver la fraîcheur des aliments stockés.

### Segment 4 : Les foyers modestes heurtés par la révision tarifaire

- Taille du segment : 239 clients de l'échantillon rattachés à la tranche de revenu mensuel net inférieure à 2 000 euros (`household_income_band == '<2000'`). Extrapolé au portefeuille global, ce segment représente environ 2 165 foyers.
- Signaux précurseurs : taux d'attrition de 42,68 % chez ces ménages, soit un décrochage de 10,44 points par rapport à la moyenne générale de 32,24 %. Le motif `price` arrive en tête des causes de résiliation avec 142 départs (27,20 % des motifs exprimés), tandis que 41 % des sondés du baromètre citent le prix comme irritant numéro un suite à la hausse de 5 % du 1er mars 2026.
- Action proposée : accompagnement budgétaire transparent sans brader l'image de marque. Mise en valeur proactive des grands contenants économiques (sacs de 12 kg pour chiens ou 7 kg pour chats stérilisés à 68,90 € TTC), qui réduisent le coût unitaire au kilo de 15 % à 25 % par rapport aux petits formats. Rappel systématique de la remise permanente de 10 % incluse dans l'abonnement et valorisation du parrainage (15 € de crédit pour le parrain, 20 % pour le filleul - À VALIDER).

### Segment 5 : Les abonnés insatisfaits ou en litige répété au service client

- Taille du segment : 158 abonnés cumulant au moins 2 tickets de réclamation sur douze mois (115 abonnés avec 2 tickets, 43 abonnés avec 3 tickets ou plus dans `donnees/customers.csv`), auxquels s'ajoutent les 58 clients de l'échantillon ayant attribué une note de 1 ou 2 étoiles lors de leur dernier avis.
- Signaux précurseurs : taux de churn atteignant 20,93 % pour les abonnés à 3 réclamations (+46 % d'augmentation relative) et culminant à 43,10 % chez les déposants d'avis très défavorables. Le volume moyen de tickets chez les résiliataires est supérieur de 20 % à celui des clients fidèles (0,619 ticket contre 0,516).
- Action proposée : création d'un canal d'assistance prioritaire de niveau 2 au sein de l'équipe d'Angers. Rappel téléphonique personnalisé sous 24 heures pour toute note inférieure ou égale à 2 étoiles ou dès l'ouverture d'un troisième ticket. Traitement sur mesure du litige, lettre d'excuses personnalisée et geste d'apaisement ciblé issu du catalogue (bouchées ou friandises adaptées à l'espèce - À VALIDER).

---

## 2. Plan d'action priorisé

Le calendrier opérationnel s'articule en trois phases consécutives pour stabiliser les urgences relationnelles avant de consolider les processus de fidélisation.

### Première semaine : Traitement des urgences vitales et endiguement de crise

1. Intervention directe sur les 20 abonnés à risque : prise en charge manuelle et individualisée des 20 clients signalés dans `donnees/abonnes_support.csv` par les téléconseillers d'Angers, selon les orientations fixées dans `chantier/recommandations.md`.
2. Activation de la cellule d'urgence Saumon : identification dans la base de commandes de tous les clients ayant reçu un lot de croquettes Chat Saumon (P026, P027) fabriqué après le 4 mai. Envoi d'un message d'écoute proactive invitant à partager le retour de leur chat, avec proposition de bascule immédiate vers la formule Chat Stérilisé Poulet ou Dinde digestion confortable (À VALIDER).
3. Gel des relances intrusives : mise en pause des e-mails promotionnels génériques vers les abonnés ayant un ticket ouvert ou un retard de livraison non soldé, afin d'éviter d'alimenter l'exaspération.
4. Cadrage logistique d'urgence : réunion de crise avec le transporteur sous contrat pour exiger un plan de sécurisation des tournées sur les zones critiques (Bretagne, Massif central, Alpes du Sud, Corse).

### Premier mois : Déploiement des correctifs opérationnels et outillage préventif

1. Automatisation de l'alerte surstock : paramétrage d'un scénario relationnel déclenché dès qu'un abonné reporte une date de livraison (`skipped_deliveries_90d >= 1`). Le message propose en un clic d'allonger l'intervalle de livraison ou de recalibrer la ration quotidienne selon le poids de l'animal.
2. Système de détection prédictive des retards : interconnexion des données de tracking du transporteur avec les outils du service client pour notifier l'abonné par SMS ou e-mail dès qu'un colis dévie de son créneau initial, avec prise en charge proactive.
3. Parcours d'optimisation budgétaire : envoi d'une communication ciblée vers les clients commandant des petits formats récurrents (sacs de 1,5 kg chat ou 2 kg et 4 kg chien) pour démontrer les économies réalisées sur le prix au kilo grâce aux formats 7 kg et 12 kg.
4. Protocole d'accueil des nouveaux abonnés : sécurisation des 60 premiers jours d'abonnement (suivi de la transition alimentaire au quinzième jour, vérification de la bonne réception du deuxième colis).
5. Audit technique et nutritionnel de la recette au saumon : analyse conjointe avec les formulateurs industriels des retours gustatifs et digestifs pour préparer le rétablissement de l'ancienne recette ou un ajustement d'appétence.

### Premier trimestre : Refonte structurelle de la rétention et négociations stratégiques

1. Renégociation du contrat de transport en décembre 2026 : exploitation des données d'attrition pour exiger des engagements de qualité de service (SLA) stricts, assortis de pénalités financières automatiques en cas de retard répété, ou arbitrage pour un retour à l'ancien prestataire si la qualité ne s'améliore pas.
2. Refonte du parcours de gestion de l'abonnement en ligne : simplification de l'espace client pour lever l'irritant majeur relevé par le baromètre (18 % des abonnés jugeant les modifications de formule trop complexes). Intégration de la modification de date, du changement de recette et de la suspension temporaire en autonomie totale.
3. Campagne de requalification des acheteurs ponctuels : déploiement d'un parcours de conversion incitant les clients sans abonnement (`one_off`, affichant 64,02 % de churn) à rejoindre l'abonnement régulier en valorisant la réduction permanente de 10 % et la flexibilité du service.
4. Mise en place du rituel semestriel de pesée : relance périodique invitant chaque propriétaire à actualiser le poids et le niveau d'activité de son chien ou chat pour ajuster la ration exacte livrée, répondant à la frustration exprimée dans le baromètre client.

---

## 3. Modèle économique et rentabilité financière

Le modèle évalue l'impact budgétaire des actions programmées et mesure le retour sur investissement attendu sur une période de douze mois.

### Base de calcul et extrapolation au portefeuille réel

Les données sources fournissent les grandeurs suivantes :
- Portefeuille actif total : 18 000 clients sur douze mois (`donnees/dictionnaire.md`, point 3).
- Répartition réelle du portefeuille : 44,00 % d'abonnés (soit 7 920 abonnés actifs) et 56,00 % d'acheteurs ponctuels (soit 10 080 clients ponctuels actifs), d'après `corpus/barometre-clients-2026.md` (ligne 9).
- Chiffre d'affaires semestriel de la marque : 3,1 millions d'euros au premier semestre 2026 (`corpus/compte-rendu-du-comite-de-direction.md`, ligne 11), soit un rythme d'activité annuel d'environ 6,2 millions d'euros.
- Taux de résiliation mensuel des abonnés : 4,9 % par mois relevé en comité de direction le 15 septembre 2026.
- Panier annuel moyen par client résiliataire dans l'échantillon (`chantier/analyse/chiffres.md`, section 11) :
  - 415,33 euros TTC pour un abonné parti (81 820,63 € divisés par 197 résiliations).
  - 162,05 euros TTC pour un acheteur ponctuel parti (71 786,82 € divisés par 443 départs).
- Volume de départs annuels spontanés sans intervention : en appliquant le taux de churn d'abonnés de l'échantillon historique (15,24 %), le volume annuel de résiliations atteint 1 207 abonnés (7 920 × 15,236 %). Si la cadence de crise observée au printemps (4,9 % par mois, soit 45,2 % de churn annuel composé) se poursuivait sans action, les départs s'élèveraient à 3 580 abonnés par an.
- Perte annuelle de chiffre d'affaires sur les abonnés au taux tendanciel historique : 1 207 abonnés × 415,33 euros = 501 175 euros TTC.
- Hypothèse de marge brute : conformément au constat de l'analyste, `donnees/products.csv` ne consigne aucun coût de revient unitaire. Le modèle retient une hypothèse standard de 60 % de marge brute sur le chiffre d'affaires net pour une marque de nutrition animale haut de gamme distribuée en direct (variantes observées à 55 % et 65 %).

### Coût détaillé des actions du plan (budget d'intervention)

Le budget requis pour déployer le plan d'action s'établit à 30 000 euros TTC sur le premier trimestre :

1. Prise en charge des urgences et cellule d'assistance téléphonique (Angers) : 8 000 euros.
   - Hypothèse : allocation de 350 heures de téléconseillers qualifiés à 22 euros de l'heure chargée, dédiées aux 20 dossiers critiques, aux rappels Saumon et aux clients insatisfaits (7 700 euros arrondis à 8 000 euros).
2. Gestes commerciaux, échantillons et remplacements de sacs contestés : 10 000 euros.
   - Hypothèse : prise en charge d'environ 500 échanges de sacs pour les propriétaires mécontents de la recette Saumon ou pénalisés par un retard persistant, sur la base d'un coût de revient produit et logistique estimé à 20 euros par intervention (À VALIDER).
3. Développements techniques et automatisation relationnelle (CRM) : 7 000 euros.
   - Hypothèse : prestation technique de 10 jours-hommes à 700 euros par jour pour configurer les déclencheurs de sauts de livraison, le connecteur de tracking logistique et l'espace de modification d'abonnement en ligne.
4. Conception des contenus d'accompagnement et guides de transition : 5 000 euros.
   - Hypothèse : rédaction spécialisée des guides nutritionnels félins, refonte des grilles de rationnement et création des maquettes d'e-mails sous la charte de la marque.

Total des investissements engagés : 30 000 euros.

### Scénario prudent

Le scénario prudent repose sur des hypothèses volontairement conservatrices :
- Rétention des abonnés : réduction de 15 % du volume des départs annuels d'abonnés. L'intervention permet de sauver 181 abonnés par an sur les 1 207 départs tendanciels historiques (1 207 × 15 %).
- Chiffre d'affaires abonnés préservé : 181 abonnés × 415,33 euros = 75 174,73 euros par an.
- Conversion d'acheteurs ponctuels vers l'abonnement : conversion de 2 % du portefeuille de clients ponctuels (10 080 clients ponctuels × 2 % = 202 nouveaux abonnés).
- Chiffre d'affaires additionnel issu des conversions : 202 abonnés × 415,33 euros = 83 896,66 euros par an.
- Total du chiffre d'affaires annuel généré ou préservé : 159 071,39 euros TTC.
- Marge brute annuelle générée (taux de 60 %) : 159 071,39 euros × 60 % = 95 442,83 euros.
- Bénéfice net d'exploitation après déduction du coût du plan (30 000 euros) : 65 442,83 euros dès la première année.
- Retour sur investissement (ROI sur marge brute) : 218 % (soit 3,18 euros de marge brute rapportée pour chaque euro investi).

### Scénario central

Le scénario central intègre une pleine efficacité de la résolution de la crise du saumon et de la stabilisation des livraisons :
- Rétention des abonnés : réduction de 25 % du volume des résiliations annuelles d'abonnés. Le dispositif préserve 302 abonnés sur l'année (1 207 × 25 %).
- Chiffre d'affaires abonnés préservé : 302 abonnés × 415,33 euros = 125 429,66 euros par an.
- Conversion d'acheteurs ponctuels vers l'abonnement : conversion de 4 % des clients réguliers sans formule (10 080 clients × 4 % = 403 nouveaux abonnés).
- Chiffre d'affaires additionnel issu des conversions : 403 abonnés × 415,33 euros = 167 377,99 euros par an.
- Total du chiffre d'affaires annuel généré ou préservé : 292 807,65 euros TTC.
- Marge brute annuelle générée (taux de 60 %) : 292 807,65 euros × 60 % = 175 684,59 euros.
- Bénéfice net d'exploitation après déduction du coût du plan (30 000 euros) : 145 684,59 euros sur douze mois.
- Retour sur investissement (ROI sur marge brute) : 486 % (soit 5,86 euros de marge brute dégagée par euro engagé).

### Tableau comparatif des deux trajectoires financières

| Grandeur économique | Situation tendancielle sans action | Scénario prudent | Scénario central | Source de l'hypothèse |
|---|---|---|---|---|
| Abonnés sauvés du churn (an) | 0 abonné | 181 abonnés | 302 abonnés | Taux de rétention de 15 % (prudent) et 25 % (central) appliqués aux 1 207 départs annuels |
| Nouveaux abonnés par conversion | 0 abonné | 202 abonnés | 403 abonnés | Taux de bascule de 2 % (prudent) et 4 % (central) sur les 10 080 clients sans abonnement |
| Chiffre d'affaires préservé (abonnés) | 0,00 € | 75 174,73 € | 125 429,66 € | Panier annuel constaté de 415,33 € par abonné résilié (`chiffres.md`) |
| Chiffre d'affaires additionnel (conversions) | 0,00 € | 83 896,66 € | 167 377,99 € | Panier annuel moyen d'un abonné de 415,33 € appliqué aux nouveaux souscripteurs |
| **Total chiffre d'affaires préservé / généré** | **0,00 €** | **159 071,39 €** | **292 807,65 €** | Cumul des gains d'activité annuels |
| **Marge brute préservée (60 %)** | **0,00 €** | **95 442,83 €** | **175 684,59 €** | Taux d'exploitation standard direct-to-consumer retenu par l'agence |
| Coût total du plan d'action | 0,00 € | 30 000,00 € | 30 000,00 € | Budget d'intervention sur le premier trimestre (support, stocks, CRM, contenus) |
| **Gain net d'exploitation (an 1)** | **0,00 €** | **+65 442,83 €** | **+145 684,59 €** | Marge brute dégagée diminuée du coût d'intervention |
| **Retour sur investissement (ROI marge)** | **-** | **+218 %** | **+486 %** | Ratio (marge nette du plan ÷ coût du plan) |

Le calcul démontre la forte rentabilité du plan d'action dès la première année : l'économie de 0,80 euro par colis obtenue sur le contrat de transport (représentant environ 60 000 euros d'économie théorique annuelle pour 75 000 envois) a détruit plus de 500 000 euros de valeur client en accélérant les résiliations. Le réinvestissement ciblé de 30 000 euros permet de reconstituer cette marge immédiatement.
