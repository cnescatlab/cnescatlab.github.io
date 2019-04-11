# Guide d'utilisation de CAT
Ce guide explique comment installer et utiliser CAT. Pour une compatibilité
maximale il est recommandé d'utiliser un système linux.

## Installation rapide
Vous pouvez vous référer au fichier readme du dépot
[docker-cat](https://github.com/lequal/docker-cat) pour installer et exécuter
CAT rapidement.

## Installation personnalisée
Cette section décrit la procédure d'installation de manière plus complète afin
d'adapter l'installation de CAT vos besoins.

### Prérequis
Avant de pouvoir utiliser CAT vous devez avoir installé docker sur votre machine
et vous devez avoir lancé le démon docker.
De plus votre compte utilisateur doit avoir accès au groupe `docker` de votre
machine ou être `root` sur la machine.

- [Documentation sur l'installation de docker](https://docs.docker.com/install/)
- Pour lancer le démon docker: `sudo service docker start`
- Pour voir si votre compte utilisateur est membre du groupe docker:
  `cat /etc/groups | grep docker` doit indiquer `docker:<gid-docker>:x:<votre-compte>`

### Récupération de l'image

#### Via le Docker-Hub
Depuis n'importe quel dossier, exécutez la commande `docker pull lequal/docker-cat`

#### Refaire un build complet
Si vous le souhaitez vous pouvez réaliser le build vous même à partir des sources.
Pour cela, clonez le dépot GitHub puis exécutez un build.
```
git clone https://github.com/lequal/docker-cat
cd docker-cat
docker build -t <tag> .
```

### Lancement de l'image
#### Identification des droits
L'image docker-cat necessite préalablement d'identifier les fichiers qui doivent
être accessubkes (ou non) par SonarQube. Ainsi il faut identifier:

- Le dossier qui devra être accessible par docker
- Les fichiers accessibles par SonarQube

#### Choix du dossier partagé avec Docker
Le conteneur docker bénificie de droits **root** sur les fichiers qui lui sont
partagés, une fois le conteneur lancé. Il faut donc être précis et privilégier
éventuellement de ne laisser qu'un seul dossier "*Workspace*" pour son
utilisation.

#### Fichiers accessible par SonarQube
La variable `ALLOWED_GROUPS` permet de définir une liste de GID (identifiant de
groupe utilisateur) auquel appartiendra l'utilisateur `sonarqube` sur le
conteneur.

Voici la procédure pour identifier les GID à autoriser:
- Lister les fichiers que SonarQube doit analyser.
- Avec la commande `ls -l` identifier l'appartenance de ces fichiers au niveau
de la colonne groupes
- Pour chaque groupe, identifier le GID correspondant via `cat /etc/groups` ou
`getent <group_name> | cut -d : -f3`

Enfin pour chaque GID identifié ajouter `-e ALLOWED_GROUPS="<GID1>;<GID2>;<...>"`
lors du lancement du conteneur.

#### Lancement du conteneur.
Pour lancer le conteneur il suffit de taper:
```
docker run -v <dossier_partage>:/media/sf_Shared:rw -p 9000:9000 -p 9001:9001 -e ALLOWED_GROUPS="<GID>" lequal/docker-cat:latest
```
Si le lancement du conteneur à fonctionné vous pouvez vous rendre sur
[http://localhost:9000](http://localhost:9000/)

#### Utilisation de SonarQube

**ATTENTION:** La base de donnée par défaut est une base de donnée éphémère.
Pensez à bien exporter vos analyses ou à lier une base de donnée à Docker
(cf *Lier une base de données à Docker*).

Rendez vous sur l'interface web depuis un navigateur via l'url
[http://localhost:9000](http://localhost:9000/) puis connectez-vous.

Par défaut l'utilisateur est `admin` et le mot de passe est `admin`.

Vous avez désormais accès à la page d'analyse via *More -> CNES Analisys*.

Il vous suffit de remplir le formulaire à disposition et de lancer l'analyse via
le bouton en bas de page. Voici quelques précisions sur les champs du formulaire:

- **Project key** doit être unique à chaque projet, si vous analysez un projet
  déjà analysé vous devez utiliser le même **Project key** sinon vous devez le
  changer.
- **Workspace** doit être rempli avec un chemin relatif au dossier partagé avec
  Docker, par exemple si votre projet se trouve dans
  `/home/user/docker/entreprise/projet` et si vous partagez `/home/user/docker`,
  dans ce cas là renseignez `entreprise/projet`
- **Sources** doit être rempli avec un chemin relatif à la racine du **projet**
- **sonar-project.properties** n'a pas besoin d'être modifié sauf pour une
  utilisation spécifique de SonarQube. Dans la plupart des cas la seule
  modification de ce champ sera de dé-commenter la ligne sonar.java.binaries.


Une fois l'analyse faite retournez sur la page d'accueil de SonarQube pour voir
les résultats ou exportez les via *More -> CNES Report*

#### Utilisation type de docker-cat
##### Sur un poste utilisateur
L'image docker-cat peut être utilisé directement sur un poste utilisateur.
C'est principalement pour cette utilisation par les responsables qualités qu'a
été réalisée cette image. Dans ce cas d'utilisation il suffit simplement de
placer les projets  analyserdans le dossier partagé avec Docker.

##### Sur un serveur
Contrairement à **SonarQube**, le CAT n'est pas prévue pour une utilisation en
intégration continue. Par conséquence, dans une chaine d'intégration continue
certains plugins comme cnes-scan ne sont pas exploitables.

Dans le cas de l'utilisation sur un serveur, il faut monter un dossier partagé
(en NFS par exemple) puis ajouter chaque utilisateur autorisé dans la variable
`ALLOWED_GROUPS` au lancement du docker-cat.

#### Lier une base de donnée à Docker
L'image docket-cat inclut nativement une base de donnée nommée *derby*. Il s'agit
d'une petite base de donnée qui ne peut supporter que quelques méga-octets de
charge, de plus, celle-ci est éphémère. A chaque arrêt du docker, la base de
donnée est vidée.

Pour obtenir une persistance des données ou monter en charge il faut joindre une
base de donnée à l'image docker-cat.

Si vous avez déjà une base de donnée il suffit d'ajouter les variables
d'environnement suivantes au lancement du conteneur:

- SONARQUBE_JDBC_USERNAME
- SONARQUBE_JBDC_PASSWORD
- SONARQUBE_JBDC_URL

Si vous n'avez pas de base de données, vous pouvez utiliser le fichier
`docker-compose.yml` du [dépot git](https://github.com/lequal/docker-cat) après
avoir installé docker-compose. Il vous suffira simplement d’exécuter
`docker-compose up` dans le dossier où se trouve `docker-compose.yml`.

Deux conteneur seront lancés, **docker-cat** et un conteneur **pgsql**.


#### Ajouter un plugin
Pour ajouter un plugin vous devez modifier `Dockerfile` et ajouter le
téléchargement de votre plugin vers `/opt/sonarqube/extensions/plugins`.

Dans ce cas là référez vous à la section *Refaire un build complet*
