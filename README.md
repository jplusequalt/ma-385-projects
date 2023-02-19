## MA-385 projects
This repo essentially exists to show my "scratch work" for the homework problems assigned in my MA-385 class, and how I created any charts used in my homework submissions.

-----

## Prerequisites
You need git and docker installed to run the application. If you are on Windows you most likely need to install Windows Subsystem for Linux (WSL) as well.

Alternatively you could install the dependencies yourself and ignore using docker, but it's faster to just use the listed steps.

-----

## How to run the examples

To run:
1. Pull the repo with ```git clone```
2. Navigate to the specific project you wish to run
3. Build the container using ```docker build --tag <container-name> .```
4. Based on your OS, run the corresponding command:
  - Windows 10:

    ```docker run -v %cd%/outputs:/outputs <container-name>```
  - Linux/macOS:

    ```docker run -v $(pwd)/outputs:/outputs <container-name>```

## How to clean up containers
To delete the containers using Docker Desktop:
1. Open Docker Desktop
2. Navigate to Containers
3. Select the containers that you created while running these examples
4. Click 'Delete'
