# Bilan de clôture de la mission anti-churn de Pattes & Papilles

L'équipe de l'agence a achevé l'ensemble des productions demandées par Nadia Ferrand dans sa feuille de route de fin d'année. Les cinq livrables attendus sont disponibles dans le répertoire de travail partagé. Tous ont obtenu la validation conjointe du relecteur éditorial et du contrôleur des chiffres après une phase de corrections ciblées.

## Livrables achevés et chemins d'accès

Le dispositif livre cinq outils opérationnels prêts pour le comité de direction :

- Diagnostic quantitatif du churn : `chantier/livrables/dossier.md` (sections 1 et 2). Ce document analyse les 1 985 clients uniques de l'échantillon dédoublonné, détaille la rupture consécutive aux hausses tarifaires et logistiques de mars 2026, et identifie les signaux précurseurs d'attrition.
- Tableau de bord exécutif pour navigateur : `chantier/livrables/tableau-de-bord.html`. Cette page web autonome intègre les indicateurs clés et six graphiques au format PNG encodés directement pour une consultation sans dépendance externe.
- Messages personnalisés pour les vingt clients à risque : `chantier/livrables/messages-abonnes.md`. Le recueil rassemble vingt courriels conformes à la charte de marque. Chaque texte vouvoie le destinataire, cite l'animal par son prénom et formule une solution pratique unique.
- Modèle économique et business case : `chantier/livrables/dossier.md` (section 4). La modélisation chiffre les trajectoires financière et opérationnelle sur le portefeuille global de 18 000 clients actifs. Elle sépare une variante prudente et une variante centrale.
- Support de présentation pour le comité : `chantier/livrables/presentation.html`. Ce diaporama interactif de dix écrans plein écran est conçu selon les codes graphiques de la marque, avec une limite stricte de moins de trente mots par diapositive hors éléments visuels.

Ces livrables s'appuient sur un ensemble de documents méthodologiques et techniques vérifiables :

- Script d'extraction et calculs consolidés : `chantier/analyse/analyse.py` et `chantier/analyse/chiffres.md`
- Graphiques de synthèse sous charte graphique : `chantier/livrables/assets/`
- Cadrage stratégique et fiches d'arbitrage unitaire : `chantier/strategie.md` et `chantier/recommandations.md`
- Script et rapport d'audit arithmétique : `chantier/controle/controle.py` et `chantier/controle.md`
- Rapports de validation juridique et stylistique : `chantier/juridique.md` et `chantier/relecture.md`

## Refus exprimés lors des audits et corrections apportées

Le premier cycle de vérification s'est conclu sur deux avis négatifs bloquants. Le relecteur éditorial et le contrôleur arithmétique ont identifié plusieurs écarts incompatibles avec les engagements de qualité.

Le rapport de relecture a relevé sept anomalies majeures :

1. Remise commerciale inventée dans le message 4. Le projet initial accordait un bon d'achat de 5 euros absent du catalogue officiel d'automne 2026. Le rédacteur a remplacé ce bon par un sachet de friandises Cœurs fondants au poulet de 60 grammes (référence P036, valeur 5,90 euros TTC) assorti de la mention de réserve réglementaire.
2. Produit inexistant dans le message 13. Le texte proposait un coffret dégustation non référencé dans les données de l'entreprise. La proposition a été réorientée vers un pack officiel de mousse pour chat au thon de douze boîtes de 85 grammes (référence P035, valeur 15,90 euros TTC).
3. Tarif abonné non autorisé dans le message 19. Le courriel appliquait la remise de 10 % (9,81 euros) sur un tube de pâte au malt de 100 grammes (référence P038). Ce produit d'hygiène et de confort n'est pas éligible au tarif réduit, réservé aux aliments complets. L'offre a été requalifiée en attention commerciale gracieuse soumise à arbitrage.
4. Fausse imputation logistique dans le message 11 adressé à Chloé. Le premier jet invoquait des retards de livraison passés, alors que le dossier de la cliente enregistre zéro incident de transport dans la base customers.csv. Le texte s'appuie désormais sur le motif authentique consigné au service client, à savoir les rougeurs cutanées de sa chienne Lola.
5. Discordance numérique dans la présentation. La diapositive 7 mentionnait un taux d'attrition de 43,4 % pour les foyers ayant bénéficié d'une remise initiale de 30 %. Les données sources de customers.csv établissent ce taux à 49,15 %. Le designer a corrigé l'écran pour afficher 49,2 %.
6. Conditionnements unitaires non répertoriés dans les messages 2 et 20. Les offres prévoyaient des échantillons et des sachets vendus isolément. Elles intègrent désormais des références complètes du catalogue, à savoir le pack de douze sachets fraîcheur de volaille (référence P033) et le pot d'herbe à chat à faire pousser (référence P037).
7. Monotonie de la cadence d'écriture dans les messages 1, 12 et 17. Ces courriels enchaînaient plusieurs phrases d'une longueur moyenne constante. L'insertion de propositions courtes de trois à cinq mots a brisé cette régularité artificielle.

Le contrôleur arithmétique a rejeté la première version du diaporama devant l'écart de 11,7 % constaté sur la diapositive 7. Cette marge dépassait le plafond toléré de 2 %. Le contrôleur a également demandé le réalignement de la sous-population des retards d'expédition dans le dossier stratégique. Ce groupe s'appuie désormais sur les 100 abonnés réels comptabilisant deux retards (taux d'attrition de 21,00 %) et sur les 127 abonnés cumulant au moins deux retards.

Les corrections effectuées par le rédacteur et le designer ont permis de lever l'intégralité des réserves. Les deux rapports d'audit se concluent sur un accord formel sans réserve.

## Décisions et arbitrages réservés à l'équipe cliente

L'application du plan requiert plusieurs arbitrages humains de la part de la direction de Pattes & Papilles avant diffusion externe.

La conformité juridique et réglementaire exige un contrôle de Lucie Prigent, déléguée à la protection des données. Neuf des vingt personnes répertoriées dans le fichier de suivi présentent la variable newsletter_optin à la valeur non. Ce groupe comprend quatre acheteurs sans abonnement (Damien, Kevin, Julie et Elsa) et cinq abonnés actifs. La responsable juridique doit confirmer si cette mention traduit un simple refus de lettre promotionnelle ou une opposition générale à la prospection sur produits analogues, au titre de l'article L. 34-5 du code des postes et des communications électroniques. Une bascule vers un appel téléphonique d'accompagnement reste recommandée pour les clients dont le taux d'ouverture des courriels est inférieur à 20 %.

Le service client doit vérifier la fiche d'assistance de Chloé avant expédition du message 11. Cette cliente a sollicité quatre fois l'assistance pour une sensibilité de peau de sa chienne Lola. Si ces échanges signalent une prescription médicale stricte, toute suggestion d'alimentation au saumon doit être suspendue pour laisser la priorité au praticien traitant.

La direction marketing doit valider les offres commerciales. Chacune des vingt mesures de compensation ou de bienvenue inscrites dans les courriels porte la mention À VALIDER. Nadia Ferrand doit approuver ces attributions de stock.

Le comité de direction doit statuer sur le financement opérationnel. Le budget requis s'élève à 30 000 euros. Il finance la cellule d'assistance téléphonique (8 000 euros), les dédommagements sur les sacs au saumon contestés (10 000 euros), le développement des alertes sur les sauts de livraison (7 000 euros) et les guides de transition alimentaire (5 000 euros). L'enveloppe de 150 000 euros votée en septembre 2026 concerne le programme technologique de 2027. Elle ne couvre pas ce plan d'urgence.

La rentabilité financière dépend de la validation du taux de marge brute. Faute de coûts de revient unitaires dans le fichier des articles, le modèle retient une marge de référence de 60 %. La direction financière devra confirmer cette estimation pour figer le gain net, estimé à 65 442,83 euros dans la variante prudente et à 145 684,59 euros dans la variante centrale.

La politique d'acquisition commande un recadrage rapide. Les recrutements issus des partenariats d'influenceurs coûtent 100,27 euros par nouveau foyer pour un taux de départ de 45,60 %. La remise de 30 % accordée au premier achat provoque 49,2 % d'attrition. La direction doit décider du plafonnement de cette remise au profit du parrainage, dont l'attrition se limite à 20,06 % pour un coût d'acquisition de 30,81 euros.

## Trois leçons méthodologiques pour les missions futures

Les anomalies rencontrées durant la fabrication dictent trois évolutions des modes opératoires de l'atelier.

La première règle s'applique à la fiche de rôle du rédacteur (agents/redacteur.md). Tout geste commercial, cadeau ou tarif mentionné dans un texte client doit comporter la référence exacte du catalogue officiel (champ product_id). La proposition d'un bon d'achat chiffré, d'un échantillon ou d'un conditionnement non indexé dans la nomenclature officielle entraîne le rejet automatique du document dès le premier contrôle.

La deuxième règle s'impose à l'ensemble de l'équipe dans le document général (AGENTS.md). Toute valeur statistique ou financière intégrée dans un support visuel ou une note de synthèse doit obligatoirement désigner la ligne précise du tableau de référence chantier/analyse/chiffres.md dont elle découle. Aucun arrondi manuel ni aucune adaptation graphique n'est tolérée sans réconciliation immédiate avec le script de calculs.

La troisième règle concerne la fiche de rôle de l'analyste (agents/analyste.md). En cas d'absence de données économiques structurelles dans les tables du commanditaire, notamment les coûts de revient industriels ou les coûts de traitement du service client, l'analyste doit formaliser une grille d'hypothèses de gestion dès le dépôt du premier état chiffré. Cette grille devient la référence unique obligatoire pour les modélisations financières du stratège et les audits du contrôleur.
