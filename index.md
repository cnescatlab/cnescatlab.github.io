# Lequal

Le LEQUAL est un laboratoire d'expertise du CNES qui développe un ensemble
d'outils permettant l'analyse d'un code source afin de s'assurer de sa
qualité. L'outil principal est CAT (Code Analisys Tool). Basé sur SONARQUBE et
docker, il permet l'analyse d'un code source et la création de rapports Excel ou
Word pour permettre une analyse plus complète par un humain. Cet outil peut être
complété par les différents développements disponibles sur
[le dépot github](https://github.com/lequal).

CAT est capable de réaliser une analyse de code sur les langages suivants:

- C++
- Java
- Python
- Web (HTML, JavaScript, TypeScript, PHP, etc.)

[En savoir plus sur CAT](cat) -
[Installation / Utilisation de CAT](how-to-use-cat) -
[Guide technique](tech-guide)


# Codes présents sur le dépot
Le tableau ci-dessous shematise les relations entre les codes présents sur le dépot.

Le projet [sonar-cnes-report](https://github.com/lequal/sonar-cnes-report) 
fonctionne de manière indépendante à docker-cat. Même si docker-cat inclut 
cet outil, il est possible de télécharger 
[sonar-cnes-report](https://github.com/lequal/sonar-cnes-report) et de
l'utiliser sans avoir à installer docker-cat sur la machine. Ce projet permet
d'exporter les résultats d'une analyse de code depuis Sonarqube vers un
fichier excel et/ou docx.

Excepté les plugins listés ci-dessous, les plugins sonarqube permettent 
de prendre en charge plus de langages lors des analyses de code, 
referez vous au readme de ces plugins pour en savoir plus.

- [sonar-cnes-scan-plugin](https://github.com/lequal/sonar-cnes-scan-plugin)
permet d'ajouter une interface graphique permettant de lancer une analyse
de code.
- [sonar-cnes-export-plugin](https://github.com/lequal/sonar-cnes-export-plugin)
permet d'exporter les règles utilisées pour l'analyse de code.

<table>
<tr><th colspan='5'><a href="https://github.com/lequal/docker-cat">DOCKER-CAT</a></th></tr>
<tr>
    <td><table>
        <tr><th>Sonarqube</th></tr>
        <tr><td><a href="https://github.com/lequal/sonar-cnes-scan-plugin">sonar-cnes-scan-plugin</a></td></tr>
        <tr><td><a href="https://github.com/lequal/sonar-cnes-export-plugin">sonar-cnes-export-plugin</a></td></tr>
        <tr><td><a href="https://github.com/lequal/sonar-frama-c-plugin">sonar-frama-c-plugin</a></td></tr>
        <tr><td><a href="https://github.com/lequal/sonar-icode-cnes-plugin">sonar-icode-cnes-plugin</a></td></tr>
        <tr><td><a href="https://github.com/lequal/sonar-cnes-python-plugin">sonar-cnes-python-plugin</a></td></tr>
        <tr><td><a href="https://github.com/lequal/sonar-shellcheck-plugin">sonar-shellcheck-plugin</a></td></tr>
        <tr><td><a href="https://github.com/lequal/sonar-cnes-cxx-plugin">sonar-cnes-cxx-plugin</a></td></tr>
    </table></td>
    <td><table>
        <tr><td><a href="https://github.com/lequal/sonar-cnes-report">sonar-cnes-report</a><br><em>Fonctionne aussi sans docker-cat</em></td></tr>
    </table></td>
</tr>
</table>
