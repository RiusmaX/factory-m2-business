# Dossier stratégique anti-churn de la marque Pattes & Papilles

Ce dossier présente l'analyse quantitative du churn de la marque Pattes & Papilles, la segmentation des populations fragilisées, le plan de redressement opérationnel et le modèle financier associé. Tous les chiffres cités sont issus exclusivement du référentiel audité de l'entreprise.

---

## 1. Le constat, chiffré

La croissance de l'entreprise s'est arrêtée au printemps 2026 sous l'effet conjugué de deux décisions opérationnelles majeures : la révision tarifaire de 5 % appliquée le 1er mars 2026, suivie dès le lendemain du changement de prestataire logistique le 2 mars 2026. Deux mois plus tard, la modification de la formule de croquettes pour chat au saumon le 4 mai 2026 a déclenché une crise de consommation chez les possesseurs de félins.

Le traitement rigoureux des fichiers internes impose d'assainir la table des clients. Le fichier brut comprend 2 000 lignes, au sein desquelles 15 doublons stricts ont été supprimés pour isoler 1 985 clients uniques. Ces clients totalisent 12 673 commandes sur les douze mois glissants courant du 1er juillet 2025 au 30 juin 2026, issues des 23 184 lignes de la base des commandes. L'échantillon analysé compte 1 293 abonnés, soit 65,14 % de son effectif, alors que le portefeuille global actif de 18 000 clients n'en compte que 44,00 % selon le baromètre de mars 2026. Cette surreprésentation impose de redresser systématiquement les calculs lors des extrapolations.

Le taux de churn global de cet échantillon atteint 32,24 % avec 640 départs constatés entre le 1er juillet et le 30 septembre 2026. Ce niveau d'attrition masque une disparité fondamentale entre les formules commerciales :

| Formule commerciale | Clients | Départs | Taux de churn | Source |
|---|---|---|---|---|
| Abonnement régulier | 1 293 | 197 | 15,24 % | donnees/customers.csv |
| Achat ponctuel sans engagement | 692 | 443 | 64,02 % | donnees/customers.csv |
| Total échantillon dédoublonné | 1 985 | 640 | 32,24 % | donnees/customers.csv |

L'abonnement constitue le rempart principal contre l'attrition. Un client sans engagement présente un risque de départ 4,2 fois supérieur à celui d'un abonné.

La rupture temporelle du début d'année est flagrante. Chez les clients inscrits avant le 1er mars 2026, le taux d'attrition s'établit à 27,76 % avec 450 départs sur 1 621 inscrits. Pour les nouveaux venus ayant rejoint la marque à compter du 1er mars 2026, ce taux bondit à 52,20 %, soit 190 départs sur 364 clients. Le churn des nouvelles recrues a presque doublé en affichant une progression relative de 88 %.

Le canal de recrutement conditionne fortement la longévité de la relation :

| Canal d'acquisition | Clients | Départs | Taux de churn | Coût d'acquisition S1 2026 | Source |
|---|---|---|---|---|---|
| Partenariats influenceurs | 182 | 83 | 45,60 % | 100,27 € | customers.csv et marketing_monthly.csv |
| Réseaux sociaux payants | 650 | 243 | 37,38 % | 87,45 € | customers.csv et marketing_monthly.csv |
| Référencement payant Google | 368 | 122 | 33,15 % | 72,23 € | customers.csv et marketing_monthly.csv |
| Visites directes | 154 | 44 | 28,57 % | 0,00 € | customers.csv et marketing_monthly.csv |
| Référencement naturel | 317 | 85 | 26,81 % | 0,00 € | customers.csv et marketing_monthly.csv |
| Parrainage entre proches | 314 | 63 | 20,06 % | 30,81 € | customers.csv et marketing_monthly.csv |

Le parrainage s'affirme comme le canal le plus vertueux. Il offre le coût d'acquisition le plus bas (30,81 €) et le taux de churn le plus faible (20,06 %). À l'opposé, les partenariats d'influenceurs absorbent 100,27 € par recrutement pour déboucher sur une défection record de 45,60 %.

Cette fragilité des recrutements promotionnels se vérifie au travers de la remise de bienvenue :

| Remise de bienvenue accordée | Clients | Départs | Taux de churn | Source |
|---|---|---|---|---|
| Plein tarif (0 % de remise) | 614 | 166 | 27,04 % | donnees/customers.csv |
| Remise standard de 20 % | 901 | 243 | 26,97 % | donnees/customers.csv |
| Remise agressive de 30 % | 470 | 231 | 49,15 % | donnees/customers.csv |

La remise de 30 % induit une hausse du risque d'attrition de 82 % par rapport aux clients recrutés à plein tarif. Elle attire des consommateurs opportunistes qui résilient dès leur premier sac épuisé.

L'espèce de l'animal révèle une vulnérabilité marquée chez les félins. Les propriétaires de chats enregistrent un taux de résiliation de 39,52 % (328 départs sur 830 foyers), contre 27,01 % chez les possesseurs de chiens (312 départs sur 1 155 foyers). L'écart atteint 12,5 points.

Les signaux précurseurs identifiés dans les données permettent de repérer la dérive bien avant la rupture :

| Signal précurseur mesuré | Population | Modalité | Taux de churn | Écart ou sur-risque | Source |
|---|---|---|---|---|---|
| Sauts de livraison (90 jours) | 1 293 abonnés | 0 saut | 13,73 % | Référence | customers.csv |
| Sauts de livraison (90 jours) | 1 293 abonnés | 1 saut | 19,18 % | +39,7 % de risque | customers.csv |
| Sauts de livraison (90 jours) | 1 293 abonnés | 2 sauts | 33,33 % | Risque multiplié par 2,43 | customers.csv |
| Retards subis (12 mois) | 1 293 abonnés | 0 retard | 15,61 % | Référence | customers.csv |
| Retards subis (12 mois) | 1 293 abonnés | 2 retards | 21,00 % | +34,5 % de sur-risque | customers.csv |
| Réclamations support (12 mois) | 1 293 abonnés | 0 ticket | 14,34 % | Référence | customers.csv |
| Réclamations support (12 mois) | 1 293 abonnés | 2 tickets | 18,26 % | +27,3 % de sur-risque | customers.csv |
| Réclamations support (12 mois) | 1 293 abonnés | 3 tickets et plus | 20,93 % | +46,0 % de sur-risque | customers.csv |
| Note d'avis client | 879 répondants | 1 ou 2 étoiles | 43,86 % | Maximum d'attrition | customers.csv |
| Consultation des e-mails | 1 189 inscrits | Taux moyen | 39,13 % | Chute de 9,83 points vs fidèles | customers.csv |

Un abonné qui décale deux fois ses commandes voit sa probabilité de départ plus que doubler. L'engagement par e-mail décroche nettement : il tombe de 48,96 % chez les clients fidèles à 39,13 % chez les clients perdus.

L'examen des motifs déclarés par 522 résiliataires sur les 640 départs confirme l'impact direct de la gestion interne :

| Motif déclaré de départ | Départs | Part des motifs connus | Explication de gestion | Source |
|---|---|---|---|---|
| Prix trop élevé | 142 | 27,20 % | Hausse de 5 % mal acceptée | customers.csv |
| Autres motifs non précisés | 94 | 18,01 % | Motifs divers | customers.csv |
| Défaillances de livraison | 86 | 16,48 % | Retards du nouveau transporteur | customers.csv |
| Passage à la concurrence | 85 | 16,28 % | Défection externe | customers.csv |
| Refus de la nourriture | 75 | 14,37 % | Rejet de la recette saumon | customers.csv |
| Stock excessif à domicile | 23 | 4,41 % | Fréquence de livraison rigide | customers.csv |
| Régime vétérinaire requis | 9 | 1,72 % | Pathologie animale | customers.csv |
| Décès de l'animal | 8 | 1,53 % | Événement naturel | customers.csv |

Les trois causes directement activables par la marque (prix, livraison et refus alimentaire) totalisent 303 résiliations, soit 58,05 % des motifs exprimés.

La crise de la recette chat au saumon illustre cette dégradation. Depuis la modification du 4 mai 2026 sur les références P026 et P027, 241 clients uniques ont commandé ce produit. Parmi eux, 119 ont déjà quitté la marque, soit un taux d'attrition de 49,38 %. Dans cette cohorte, 60 clients ont explicitement invoqué le motif du refus alimentaire. À eux seuls, ils représentent 80,00 % des 75 départs totaux imputés au goût dans tout l'échantillon. Quatorze demandes de remboursement ont été enregistrées sur ces deux références dans la table des commandes.

La hausse des tarifs a frappé les budgets modestes de plein fouet. Les foyers dont le revenu net mensuel est inférieur à 2 000 euros subissent un churn de 42,68 % (102 départs sur 239 foyers), soit 10,44 points de plus que la moyenne globale de 32,24 %.

Le coût financier de cette attrition s'élève à 153 607,45 euros de chiffre d'affaires annuel perdu sur l'échantillon, calculé sur un volume d'affaires global de 810 532,63 euros TTC (18,95 % d'érosion). Les 197 abonnés résiliés pèsent pour 81 820,63 euros de perte, avec un panier annuel moyen de 415,33 euros. Les 443 acheteurs ponctuels représentent 71 786,82 euros, avec une dépense annuelle moyenne de 162,05 euros.

---

## 2. Les segments à risque

L'audit des 1 985 profils permet de circonscrire cinq segments prioritaires pour guider les opérations de reconquête.

### Acheteurs de la recette chat au saumon modifiée

Ce groupe comprend 241 clients dans l'échantillon, soit environ 2 185 foyers à l'échelle des 18 000 clients actifs. Leur taux de churn culmine à 49,38 %. Le signal déclencheur réside dans l'achat des références P026 ou P027 postérieur au 4 mai 2026, suivi d'une absence de renouvellement ou d'une note de réclamation. La solution consiste à bloquer les réexpéditions de cette formule, à proposer l'échange gracieux du sac restant contre la recette Chat Stérilisé Poulet ou Ventre sensible Dinde, et à fournir un protocole de transition digestive sur dix jours (À VALIDER).

### Abonnés touchés par des anomalies logistiques répétées

Ce segment réunit 127 abonnés de l'échantillon cumulant au moins deux retards de livraison sur l'année, ce qui représente environ 778 abonnés sur le portefeuille global. Dès le deuxième retard, leur taux d'attrition passe à 21,00 %, en sur-risque relatif de 34,5 % par rapport aux abonnés servis à l'heure. Le motif logistique regroupe 86 résiliations déclarées. L'intervention impose un étiquetage prioritaire des colis en entrepôt, une notification SMS proactive dès qu'un retard dépasse 48 heures, et l'ajout d'une compensation matérielle dans le colis comme un sachet de friandises au canard (À VALIDER).

### Abonnés en situation de surstockage

Ce segment rassemble 310 abonnés ayant décalé au moins une expédition au cours des 90 derniers jours, soit 23,98 % des abonnés de l'échantillon et près de 1 900 foyers sur l'ensemble du fichier. Le risque de résiliation grimpe à 33,33 % chez ceux qui ont sauté deux livraisons, ce qui multiplie la probabilité par 2,43. Le surstock génère 23 abandons directs. L'action préconisée repose sur un message automatisé dès le premier décalage pour inviter l'abonné à passer à un rythme d'envoi de cinq ou six semaines, ou à réajuster le calcul de la ration selon le niveau d'activité réel de l'animal.

### Foyers modestes fragilisés par le relèvement des prix

Ce groupe compte 239 clients dont le revenu mensuel est inférieur à 2 000 euros (environ 2 165 foyers dans le portefeuille global). Leur taux de churn atteint 42,68 %, soit plus de dix points au-dessus de la moyenne. Le prix constitue le motif numéro un de résiliation avec 142 mentions. Le plan d'action prévoit la promotion pédagogique des grands conditionnements de 12 kg pour chiens ou 7 kg pour chats, dont le prix au kilo est inférieur de 15 % à 25 % à celui des petits formats, tout en rappelant la remise automatique de 10 % attachée à l'abonnement.

### Clients mécontents et réclamants récurrents

Ce segment rassemble 158 abonnés totalisant deux réclamations ou plus sur douze mois, ainsi que les 57 clients uniques ayant noté leur expérience 1 ou 2 étoiles. Leur propension au départ s'élève à 20,93 % pour trois tickets et culmine à 43,86 % pour les avis très négatifs. Le traitement requiert une ligne directe d'assistance gérée par les téléconseillers d'Angers, un rappel téléphonique sous 24 heures pour chaque note inférieure à 3 étoiles, et un geste d'apaisement issu du catalogue sous forme de produit offert (À VALIDER).

---

## 3. Le plan d'action

Le déploiement des mesures s'échelonne sur trois temporalités pour stopper l'hémorragie immédiate avant de consolider les processus récurrents.

### Actions immédiates de la première semaine

La première mesure consiste à prendre en charge manuellement les 20 dossiers critiques répertoriés dans la base de support. Chaque client fait l'objet d'un message sur mesure ou d'un appel téléphonique conduit par l'équipe d'Angers selon les directives fixées.

La deuxième mesure active une cellule d'écoute dédiée aux clients ayant acheté la formule chat au saumon depuis mai. Chaque foyer reçoit une proposition de bascule vers une autre protéine familière avec prise en charge du sac de remplacement (À VALIDER).

La troisième mesure suspend temporairement les sollicitations promotionnelles automatisées vers tout abonné ayant un ticket de litige ouvert ou un retard de livraison non résolu, afin de ne pas alimenter son mécontentement.

La quatrième mesure organise une réunion de recadrage avec le prestataire de transport pour instaurer une surveillance stricte des départements ruraux en souffrance logistique.

### Déploiements opérationnels du premier mois

L'équipe technique automatise le parcours relationnel lié au surstock. Dès qu'un abonné reporte une commande, l'interface lui propose d'allonger la durée de son cycle de livraison sans démarche complexe.

Un dispositif de suivi prédictif des livraisons est raccordé au service client. L'abonné est prévenu par message avant même de constater un décalage de distribution, ce qui désamorce les tensions.

Une campagne d'information budgétaire valorise les sacs grand format auprès des acheteurs réguliers de petits volumes, en démontrant les économies réalisables au kilo.

Le parcours d'accueil des nouveaux abonnés est renforcé sur les soixante premiers jours pour s'assurer de l'adaptation de l'animal et de la ponctualité du deuxième envoi.

Un audit gustatif et industriel de la recette féline au saumon est conduit avec le laboratoire de fabrication pour planifier le retour à l'ancienne composition.

### Refontes structurelles du premier trimestre

La direction renégocie le contrat de transport en décembre 2026. Le nouveau cahier des charges introduit des pénalités financières automatiques en cas de non-respect des délais impartis et réserve l'option d'un retour à l'ancien prestataire si les résultats ne s'améliorent pas.

L'espace client web fait l'objet d'une simplification ergonomique complète. La modification de la date d'envoi, l'ajustement des quantités et le changement de recette deviennent réalisables en deux clics sans passer par le support.

Un protocole de fidélisation cible les acheteurs ponctuels pour leur démontrer l'avantage financier de l'abonnement permanent avec sa réduction de 10 %.

Un rituel de pesée semestrielle invite les propriétaires à mettre à jour le gabarit de leur compagnon afin de recalibrer les rations exactes et prévenir tout encombrement de croquettes à domicile.

---

## 4. Le business case

Le modèle financier projette les retombées économiques sur une période de douze mois en s'appuyant sur la structure réelle du portefeuille de l'entreprise.

### Paramètres et hypothèses de modélisation

Les bases chiffrées du calcul reposent sur les grandeurs suivantes :
- Portefeuille actif : 18 000 clients sur un an.
- Structure réelle de clientèle : 44,00 % d'abonnés (7 920 clients) et 56,00 % d'acheteurs ponctuels (10 080 clients).
- Chiffre d'affaires semestriel de la marque : 3,1 millions d'euros au premier semestre 2026, soit une base annuelle d'environ 6,2 millions d'euros.
- Panier annuel moyen par client résilié : 415,33 euros TTC pour un abonné et 162,05 euros TTC pour un acheteur ponctuel.
- Volume spontané de départs d'abonnés sans intervention : 1 207 résiliations annuelles au taux historique de 15,24 % (7 920 × 15,236 %).
- Perte annuelle tendancielle sur les abonnés : 501 175 euros TTC (1 207 × 415,33 €).
- Hypothèse de marge brute : taux moyen de 60 % retenu en l'absence de coût de revient dans le catalogue.

### Budget d'investissement opérationnel

Le coût total du plan de redressement s'établit à 30 000 euros TTC sur le premier trimestre :

| Poste budgétaire | Montant (€ TTC) | Détail des moyens alloués |
|---|---|---|
| Cellule d'assistance téléphonique (Angers) | 8 000 € | 350 heures de téléconseillers qualifiés à 22 € de l'heure chargée |
| Gestes commerciaux et échanges de sacs | 10 000 € | Prise en charge d'environ 500 remplacements de sacs et friandises (À VALIDER) |
| Développements CRM et outils informatiques | 7 000 € | 10 jours de prestation technique pour automatiser les alertes et l'espace client |
| Rédaction des guides et contenus conseils | 5 000 € | Création des supports de transition alimentaire et refonte des chartes |
| Total des investissements | 30 000 € | Budget global d'intervention |

### Scénario prudent

Le scénario prudent retient des gains très mesurés :
- Réduction de 15 % du volume des départs d'abonnés : 181 abonnés conservés sur l'année (1 207 × 15 %).
- Chiffre d'affaires abonnés préservé : 75 174,73 euros TTC (181 × 415,33 €).
- Conversion de 2 % des clients ponctuels vers l'abonnement : 202 nouveaux abonnés (10 080 × 2 %).
- Chiffre d'affaires additionnel des conversions : 83 896,66 euros TTC (202 × 415,33 €).
- Chiffre d'affaires total généré ou sauvé : 159 071,39 euros TTC.
- Marge brute dégagée (au taux de 60 %) : 95 442,83 euros.
- Gain net d'exploitation après déduction des 30 000 euros engagés : 65 442,83 euros.
- Retour sur investissement : 218 % (chaque euro investi rapporte 3,18 euros de marge brute).

### Scénario central

Le scénario central intègre la résolution complète des blocages logistiques et du rejet de la formule saumon :
- Réduction de 25 % du volume des résiliations d'abonnés : 302 abonnés retenus (1 207 × 25 %).
- Chiffre d'affaires abonnés préservé : 125 429,66 euros TTC (302 × 415,33 €).
- Conversion de 4 % des acheteurs ponctuels vers l'abonnement : 403 nouveaux abonnés (10 080 × 4 %).
- Chiffre d'affaires additionnel des conversions : 167 377,99 euros TTC (403 × 415,33 €).
- Chiffre d'affaires total généré ou sauvé : 292 807,65 euros TTC.
- Marge brute dégagée (au taux de 60 %) : 175 684,59 euros.
- Gain net d'exploitation après déduction des 30 000 euros engagés : 145 684,59 euros.
- Retour sur investissement : 486 % (chaque euro investi rapporte 5,86 euros de marge brute).

---

## 5. Ce que l'IA a fait, ce que l'humain a validé

La collaboration entre les traitements automatisés et le discernement humain a respecté un partage strict des rôles tout au long de la mission.

### Réalisations prises en charge par les outils automatisés

Les modèles informatiques ont effectué le nettoyage systématique de la base de données en supprimant les 15 doublons de clients et en réagrégeant les 23 184 lignes d'achats en 12 673 commandes réelles.

Ils ont calculé l'intégralité des indicateurs statistiques de churn, identifié les corrélations temporelles autour des événements de mars et mai 2026, et isolé les facteurs précurseurs comme les sauts de livraison ou les réclamations.

Ils ont produit les simulations arithmétiques du business case selon plusieurs variantes de marge et de conversion.

Ils ont préparé le premier jet rédactionnel des vingt messages personnalisés destinés aux abonnés de la liste de support, en respectant la charte relationnelle de la marque et en intégrant les mentions de désinscription obligatoires.

### Validations et décisions assurées par l'équipe humaine

Le contrôleur de gestion a audité de manière indépendante chaque calcul, formule et rapprochement de chiffres pour garantir la cohérence absolue avec les tables sources.

La déléguée à la protection des données a examiné chaque courriel préparé afin de certifier l'absence de fuite de données personnelles, l'exclusion des scores de profilage internes et la parfaite conformité avec le code des postes et des communications électroniques sur les profils en achat ponctuel.

Le relecteur éditorial a vérifié la tenue du style, l'élimination des automatismes d'écriture artificielle, le vouvoiement systématique et le bannissement total des allégations thérapeutiques contraires à la réglementation européenne.

La direction de Pattes & Papilles conserve l'exclusivité des choix stratégiques : l'approbation du budget d'intervention de 30 000 euros, la validation de chaque geste commercial offert aux abonnés, la renégociation du contrat de transport et la décision industrielle de modifier la recette de croquettes au saumon.

---

## 6. Limites et risques

L'exploitation des résultats doit tenir compte des contraintes intrinsèques aux bases de données consultées et des aléas extérieurs à l'entreprise.

### Limites méthodologiques du jeu de données

Le catalogue officiel des produits mentionne uniquement les prix de vente publics TTC. Aucun coût de revient unitaire ni aucune marge brute réelle n'y figurent, ce qui contraint à poser une hypothèse normative de marge pour évaluer les gains financiers.

Les coûts réels du transporteur, les tarifs unitaires de traitement d'une réclamation au service client et les frais engagés lors d'une réexpédition de colis ne sont pas documentés dans les données transmises.

L'échantillon extrait rassemble 65,14 % d'abonnés, alors que la population active totale n'en comporte que 44,00 %. Les projections financières ont corrigé cette surreprésentation, mais une incertitude subsiste sur le comportement réel des 10 080 clients sans abonnement.

Les variables de comportement d'abonnement, comme les sauts de livraison ou le rythme des expéditions, sont par définition vides pour les acheteurs ponctuels. Ces mentions manquantes ne peuvent être assimilées à une absence de réclamation.

Les avis clients et les tranches de revenus ne couvrent pas l'intégralité de la base : 44,2 % seulement des clients ont laissé une note, et 29,7 % des revenus restent inconnus car issus d'un rapprochement externe estimé.

Le détail qualitatif des motifs de contact au support client demeure inaccessible dans les fichiers chiffrés, en dehors de la mention catégorisée au moment du départ définitif.

### Risques opérationnels d'exécution

Le risque principal concerne la logistique. Si le transporteur actuel ne stabilise pas ses délais sous trente jours dans les départements ruraux, les gestes d'apaisement offerts par le service client perdront toute efficacité.

Le deuxième risque porte sur l'acceptabilité alimentaire des chats. Même avec une bascule vers la recette poulet, certains félins heurtés par le changement de recette de mai peuvent maintenir une néophobie durable et refuser toute la gamme.

Le troisième risque relève de la conformité de contact. Parmi les vingt dossiers sensibles, neuf clients affichent un refus de lettre d'information, dont quatre acheteurs sans abonnement. L'envoi d'un courriel requiert la confirmation juridique expresse de l'absence d'opposition globale à la prospection sur produits similaires.

Le quatrième risque touche à la politique tarifaire. Accorder des compensations ou des remises sans cadrage strict pourrait habituer la clientèle à réclamer pour obtenir des avantages financiers, ce qui éroderait la rentabilité de la marque.

Le contexte économique global présente enfin des facteurs incontrôlables par l'entreprise : l'inflation sur les approvisionnements de viande française et la pression publicitaire des concurrents sur le segment du petfood sur abonnement.
