# Who we are & What we do

The LEQUAL (for *Laboratoire d'Expertise QUAlité Logiciel*) is a CNES software quality expertise lab, that creates tools to analyse code and verify its quality.
All our projects are available on GitHub [here](https://github.com/lequal).

The goal of all these projects is to provide some tools to do code analisys and check the quality of a project, with CNES standards in mind.
Even if it's build on CNES needs, you can use these tools to check all types of project and reconfigure them to fit your own specifications.
Most of the tools are based on SonarQube and designed to work on SonarQube 7.9 LTS, as well as previous LTS versions.
Please check compatibility matrix of each tool for more information.
These matrix are available in the README file of each project.

## Most popular tools :

- An all-in-one solution includes most of our tools: [Docker-CAT](tools/cat). This project provide all the tools already configured in a virtual environment managed by Docker.
  - You can find the Docker Image on DockerHub [here](https://hub.docker.com/r/lequal/docker-cat).
  - The source code to generate it is available [here](https://github.com/lequal/docker-cat).

- The [sonar-cnes-report](https://github.com/lequal/sonar-cnes-report) can generate a quality report from a SonarQube project. Output can be in Docx (Microsoft Word), XLSX (Microsoft Excel), CSV or Markdown. It works as a sonar plugin or as a standalone command line tool.
  - Plugin mode is very simple to use and to install, as being a part of your SonarQube tool.
  - Standalone mode is JAR executable that can be configured with a lot of settings. For instance, you can change report templates, and call any distant SonarQube server, including SonarCloud.

![sonar-cnes-report](img/cnes-report.png)

- [i-CodeCNES](https://github.com/lequal/i-CodeCNES) is an eclipse Plugin that lets you check Fortran 77, Fortran 90 and Shell code.

## Other tools :

* [sonar-icode-cnes-plugin](https://github.com/lequal/sonar-icode-cnes-plugin) : _Let you import i-Code results in SonarQube._
* [sonar-cnes-scan-plugin](https://github.com/lequal/sonar-cnes-scan-plugin) : _Provide an HIM to start an analysis directly from the web interface of SonarQube._
* [sonar-cnes-export-plugin](https://github.com/lequal/sonar-cnes-export-plugin) : _Add ability to export the rules of a given quality profile directly from the web interface._
* [cnes-pylint-extension](https://github.com/lequal/cnes-pylint-extension) : _Add more checkers to Pylint with CNES guidelines._
* [sonar-frama-c-plugin](https://github.com/lequal/sonar-frama-c-plugin) : _Let you import Frama-C results in SonarQube._
* [sonar-shellcheck-plugin](https://github.com/lequal/sonar-shellcheck-plugin) : _Let you import ShellCheck results in SonarQube._
* [sonar-cnes-cxx-plugin](https://github.com/lequal/sonar-cnes-cxx-plugin) : _Execute C/C++ analysis tools (CppCheck, Rats, Vera++) and import results in SonarQube._
* [polyspace-report2excel](https://github.com/lequal/polyspace-report2excel): _Extract tables from Polyspace report and copy them in excel file._
