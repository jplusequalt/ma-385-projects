## MA-385 projects
This repo essentially exists to show my "scratch work" for the homework problems assigned in my MA-385 class, and how I created any charts used in my homework submissions.

-----

## Prerequisites
You need git and docker installed to run the application with Docker. If you are on Windows you most likely need to install Windows Subsystem for Linux (WSL) as well.

Alternatively you could install the dependencies yourself and ignore using docker, but you need to download Python instead. This project has only been tested using Python 3.11.2.

-----

## How to run the examples with Docker

To run with docker:
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

## How to run examples manually

To run manually:
1. Pull the repo with ```git clone```
2. Navigate to the specific project you wish to run
3. Create a new virtual environment using ```python -m <venv-name> .venv```
4. Based on your OS, start the virtual environment using one of the following commands:
  - Windows 10:
    ```.venv\Scripts\activate.bat```
  - Linux/macOS
    ```source .venv/bin/activate```
5. Install the necessary Python dependencies with ```python install -r requirements.txt```
6. Run the application with ```python main.py```
