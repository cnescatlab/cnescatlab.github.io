# [DRAFT]
*This documentation is not finished yet. There is some incomplete pages and some pages are still in french.*

# Lequal

The LEQUAL (for *Laboratoire d'Expertise QUAlité Logiciel*) is a CNES laboratory that 
create some tools to analyse code and verify its quality. All the projects are available
in their [repo](https://github.com/lequal).


## Docker CAT - Code Analysis Tools
![Docker-CAT](img/docker-cat.png)
The main tool of this repo is Docker-CAT (Code Analysis Tool). Docker-CAT is the docker version of
CAT, a tool used at CNES.

Docker-CAT is based on SonarQube and upgraded with some tools of this repo so you 
can do some code analysis and verify the quality of your code. Docker-CAT also include
[sonar-cnes-report](https://github.com/lequal/sonar-cnes-report) so you can export
all results in docx, excel, markdown or csv.

Docker cat can analyse
- C++
- Java
- Python
- Web languages (HTML, JavaScript, TypeScript, PHP, etc.)


### Tools included in Docker-CAT

<table><tr><th colspan='2'>DOCKER-CAT</th></tr>
        <tr><td>Sonarqube 6.7.4 (LTS)</td>
        <td><a href="https://github.com/lequal/sonar-cnes-scan-plugin">sonar-cnes-scan-plugin</a><br>
        <em>Add a new UI in sonar to start code Analysis with CNES guidelines.</em></td></tr>
        <tr><td><a href="https://github.com/lequal/sonar-cnes-export-plugin">sonar-cnes-export-plugin</a><br>
        <em>Let you export rules checked by sonar-cnes-scan-plugin.</em></td>
        <td><a href="https://github.com/lequal/sonar-cnes-python-plugin">sonar-cnes-python-plugin</a><br />
        <em>Add possibility to analyse Python code.</em></td></tr>
        <tr><td><a href="https://github.com/lequal/sonar-cnes-report">sonar-cnes-report</a>
        <br><em>Let you generate some reports. <br> Can be used as sonar-plugin or in command line.</em></td>
        <td><a href="https://github.com/lequal/sonar-cnes-python-plugin">sonar-cnes-cxx-plugin</a><br>
        <em>Let you analyse C/C++ code.</em></td></tr>
        <tr><td colspan="2">And other tools...<br />
        <em>There is also some other tools, but not from lequal. You can get complete list  <a href="https://github.com/lequal/docker-cat">here</a>.</em></td></tr>
</table>

## Other tools available in the repo

### i-CodeCNES and icode-cnes-plugin
i-CodeCNES is an eclipse Plugin that let you check Fortran 77, Fortran 90 and shell code. It can be combined with
icode-cnes-plugin to export issues in SonarQube.

Download and documentation: 
[i-CodeCNES](https://github.com/lequal/i-CodeCNES) -
[sonar-icode-cnes-plugin](https://github.com/lequal/sonar-icode-cnes-plugin)

### SonarQube Plugins
* sonar-cnes-scan-plugin
* sonar-frama-c-plugin
* sonar-cnes-python-plugin
* sonar-icode-cnes-plugin
* sonar-cnes-python-plugin
* sonar-shellcheck-plugin
* sonar-cnes-export-plugin
* sonar-cnes-cxx-plugin
* sonar-cnes-report

### Other tools
* polyspace-report2excel
* cnes-pylint-extension
