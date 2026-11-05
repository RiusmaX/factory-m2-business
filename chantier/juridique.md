# Contrôle juridique des messages aux abonnés

Le fichier `chantier/livrables/messages-abonnes.md` est introuvable au moment de cet audit. Le répertoire `chantier/livrables/` ne contient que le marqueur `.gitkeep`, car les étapes de stratégie et de rédaction n'ont pas encore produit leurs livrables.

Sans texte soumis à relecture, la conformité RGPD et prospection électronique des 20 courriels attendus pour les 20 profils de `donnees/abonnes_support.csv` (comptage des 20 lignes hors en-tête, lignes 2 à 21) ne peut pas être validée. Le jalon est bloqué.

## Liste des problèmes relevés

| Numéro du message | Citation exacte | Point enfreint |
|---|---|---|
| Messages 1 à 20 (`PP-019048` à `PP-018012`) | `[Fichier chantier/livrables/messages-abonnes.md absent]` | Points 1 à 6 de `agents/juriste.md` invérifiables faute de livrable (destinataire unique, absence de donnée de profilage, encadrement de la prospection sur les achats ponctuels, mention de désinscription, traitement des situations sensibles, absence de fausse urgence). |

## Balises juridiques issues des données sources pour la rédaction

L'examen préalable de `donnees/abonnes_support.csv`, `donnees/customers.csv`, `donnees/orders.csv` et `donnees/products.csv` met en évidence cinq contraintes impératives que le rédacteur devra respecter pour obtenir la levée du blocage lors de la prochaine passe.

Plusieurs homonymies exposent au croisement de données personnelles entre clients (point 1). Le fichier `donnees/abonnes_support.csv` compte 2 clientes prénommées Caroline sur 20 lignes (comptage par valeur de `first_name` : message 8, `PP-017626`, chat Mimi ; message 9, `PP-021977`, chien Praline) ainsi que 3 prénoms d'animaux portés chacun par 2 foyers distincts (comptage par valeur de `pet_name` : Chouquette aux messages 2 et 6, Mimi aux messages 4 et 8, Tofu aux messages 16 et 17). Les avis publics de `corpus/avis-clients-2025-2026.md` citent aussi d'autres foyers homonymes étrangers à cette liste, comme Laurent G. dont le chien Gaston est décédé (ligne 238) alors que le message 18 vise Laurent (`PP-015094`) et son chat Opale. Aucun détail issu d'un homonyme ne doit glisser d'un courriel à l'autre.

Toute trace de profilage ou de classification interne est proscrite dans le corps comme dans l'objet des courriels (point 2). Le client ne doit jamais lire son identifiant `PP-...`, son score `churn_risk_pct` compris entre 58 % et 99 % (`donnees/abonnes_support.csv`, minimum ligne 21 et maximum ligne 2) ni son intitulé de `segment` (`En sommeil`, `Nouveaux ou occasionnels récents`, `À risque (bons clients qui s'éloignent)`, `Champions`, `Fidèles`). Les formulations brutes de `main_signal` (`4 contacts au service client en 12 mois`, `aucune commande depuis 176 jours` ou `ouvre peu les e-mails (18 %)`) restent tout aussi confidentielles. Même interdiction pour la tranche de revenu `household_income_band` estimée par un courtier dans `donnees/customers.csv`.

La moitié de la cible relève du régime de la prospection commerciale et non du suivi d'abonnement (points 3 et 4). On dénombre 10 clients en `achat ponctuel` sur les 20 lignes de `donnees/abonnes_support.csv` (filtrage sur la colonne `plan`, messages 1, 2, 3, 4, 5, 6, 10, 11, 13 et 14), contre 10 en `abonnement`. En application de l'article L. 34-5 du Code des postes et des communications électroniques, la sollicitation adressée à chacun de ces 10 acheteurs ponctuels doit porter sur des produits analogues à ceux déjà facturés à ce même client dans `donnees/orders.csv` (croisé avec `donnees/products.csv`). Or la jointure sur `customer_id` avec `donnees/customers.csv` montre que 9 clients sur 20 affichent `newsletter_optin` à `no` (comptage sur les 20 profils), dont 4 acheteurs ponctuels (`PP-019048` au message 1, `PP-021712` au message 6, `PP-021842` au message 10 et `PP-017578` au message 13) et 5 abonnés (`PP-017626`, `PP-021977`, `PP-015069`, `PP-015094`, `PP-018012`). La déléguée à la protection des données Lucie Prigent devra confirmer avant expédition que `newsletter_optin` à `no` ne traduit pas une opposition générale à la prospection sur produits analogues. Chacun des 20 messages se terminera par un moyen simple et immédiat de désinscription.

Trois dossiers appellent une retenue stricte sur l'état de l'animal (point 5). Aucun des 20 profils n'est marqué résilié ni associé au motif `pet_deceased` ou `moved_to_vet_diet` dans `donnees/customers.csv` (0 cas sur 20 avec `churned` à 1, colonne `churn_reason` vide sur les 20 lignes). Trois fiches déclarent en revanche une sensibilité dans `donnees/abonnes_support.csv` (comptage des valeurs distinctes de `aucune` dans `sensitivity`) : `peau` aux messages 11 (`PP-021311`, Chloé et Lola) et 12 (`PP-012566`, Paul et Milo), et `surpoids` au message 13 (`PP-017578`, Elsa et Tonka). Aucun argument vétérinaire ou curatif ne peut leur être adressé (règlement CE 767/2009, article 13). Si l'historique SAV de Chloé (4 tickets sur 12 mois dans `donnees/customers.csv`, ligne `PP-021311`) fait état d'une maladie diagnostiquée, toute offre commerciale devra être écartée du message 11.

Aucune fausse urgence ni remise non écrite par la cliente ne sera admise (point 6). Toute offre tarifaire ou commerciale mentionnée devra porter le marqueur `À VALIDER` destiné à l'équipe de Pattes & Papilles.

VERDICT : A CORRIGER
