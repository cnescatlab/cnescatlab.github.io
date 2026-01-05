# Who we are & What we do

The CAT Lab (for *Code Analysis Tools Laboratory*) is a CNES software quality community, that creates tools to analyse code and verify its quality.
All our projects are available on GitHub [here](https://github.com/cnescatlab).

The goal of all these projects is to provide some tools to do code analisys and check the quality of a project, with CNES standards in mind.
Even if it's build on CNES needs, you can use these tools to check all types of project and reconfigure them to fit your own specifications.
Most of the tools are based on SonarQube and designed to work on SonarQube 7.9 LTS, as well as previous LTS versions.
Please check compatibility matrix of each tool for more information.
These matrix are available in the README file of each project.

## Most popular tools :

- An all-in-one solution includes most of our tools: [Docker-CAT](tools/cat). This project provide all the tools already configured in a virtual environment managed by Docker.
  - You can find the Docker Image on DockerHub [here](https://hub.docker.com/r/lequal/docker-cat).
  - The source code to generate it is available [here](https://github.com/cnescatlab/docker-cat).

- The [sonar-cnes-report](https://github.com/cnescatlab/sonar-cnes-report) can generate a quality report from a SonarQube project. Output can be in Docx (Microsoft Word), XLSX (Microsoft Excel), CSV or Markdown. It works as a sonar plugin or as a standalone command line tool.
  - Plugin mode is very simple to use and to install, as being a part of your SonarQube tool.
  - Standalone mode is JAR executable that can be configured with a lot of settings. For instance, you can change report templates, and call any distant SonarQube server, including SonarCloud.

![sonar-cnes-report](img/cnes-report.png)

- [i-CodeCNES](https://github.com/cnescatlab/i-CodeCNES) is an eclipse Plugin that lets you check Fortran 77, Fortran 90 and Shell code.

## Other tools :

* [sonar-icode-cnes-plugin](https://github.com/cnescatlab/sonar-icode-cnes-plugin) : _Let you import i-Code results in SonarQube._
* [polyspace-report2excel](https://github.com/cnescatlab/polyspace-report2excel): _Extract tables from Polyspace report and copy them in excel file._
