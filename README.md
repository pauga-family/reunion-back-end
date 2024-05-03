# Pauga Reunion Back End
This is the source code for the Pauga Family Reunion back end service. This project uses Flask and is written in python. This README will guide you through setting up your development environment.

## Prequesites

- You must have Python 3 installed on your machine. You can install it via:
    - All Platforms
        - [Official Python website](https://www.python.org/downloads/)
    - Mac
        - Homebrew: `brew install python`

## Setting Up Your Local Dev Environment
### Clone the project
First, clone the repository by running the following command in your terminal:
```
git clone git@github.com:pauga-family/reunion-back-end.git
cd reunion-back-end
```

## Setting Up Your Virtual Environment
### Mac OS
#### Run the following commands in your terminal
```
# Create a new virtual environment
python3 -m venv venv

# Activate the virtual environment (Do this every time you start a new terminal session)
source venv/bin/activate
```

#### Install Dependencies
```
pip install -r requirements.txt
```

## Setup DB
If this is your first time pulling the project run
```
flask db upgrade
```
to setup the database on your local machine

## Running the Application
In your terminal, navigate to the project directory and enter:
```
flask run
```
The application should now be running at `http://localhost:8000`
