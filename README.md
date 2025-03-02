Workshop #1: Data Engineering

By Luz Angela Carabali Mulato (@luzangelacarabli)

Overview ✨

In this workshop, we worked with randomly generated candidate data stored in a CSV file. The objective was to load, clean, and transform the data to extract meaningful insights using Python, Jupyter Notebook, PostgreSQL, and Power BI.

Tools Used

Python 3.12 ➜ Download

Jupyter Notebook ➜ VS Code extension for notebooks

PostgreSQL ➜ Download

Power BI (Desktop version) ➜ Download

Required Python Libraries

These libraries are included in the Poetry project configuration file (pyproject.toml):

pandas

matplotlib

seaborn

sqlalchemy

dotenv

numpy

scikit-learn

psycopg2

These libraries are included in the Poetry project config file (pyproject.toml). The step-by-step installation will be described later.

Dataset Information 📊

The dataset (candidates.csv) contains 50,000 rows and 10 columns, each describing a candidate in the recruitment process. After transformations, the dataset is optimized for Power BI visualization.
Dataset Structure

Column Name

Data Type

Description

first_name

Object

Candidate's first name

last_name

Object

Candidate's last name

email

Object

Candidate's email

country

Object

Candidate's country of residence

application_date

Object

Date of application submission

yoe (Years of Experience)

Integer

Candidate's total years of experience

seniority

Object

Candidate’s seniority level

technology

Object

Technology the candidate specializes in

code_challenge_score

Integer

Score obtained in the coding challenge

technical_interview_score

Integer

Score obtained in the technical interview


Running the Project 🚀
1️⃣ Clone the Repository

git clone <repository_url>
cd <project_directory>

Instalación de las dependencias con Poetry
Para instalar Poetry siga este enlace .


Una vez creado el entorno virtual, ejecutar poetry installpara instalar las dependencias. En caso de error con el archivo .lockpoetry lock , simplemente ejecutar para solucionarlo.

¡Ahora puedes ejecutar los cuadernos!

2️⃣ Set Up a Virtual Environment

poetry install
poetry shell

3️⃣ Configure the Database Connection

To establish the database connection, we use the connection_db.py module. This script loads environment variables from a configuration file. Follow these steps to set it up:

Create an .env file inside a new env/ directory in the cloned repository.

Add the following environment variables without quotes:

PG_HOST=localhost
PG_PORT=5432
PG_USER=<your_postgresql_user>
PG_PASSWORD=<your_password>
PG_DRIVER=postgresql+psycopg2
PG_DATABASE=<your_database_name>
WORK_PATH=<your_project_directory>

4️⃣ Create the Database

Ensure that your PostgreSQL database name matches the one in the .env file before proceeding.

Data Processing and Notebook Execution 📝

Executing the Notebooks

We use Jupyter Notebook to process and transform the dataset. Execute the notebooks in the following order:

Notebook

Purpose

001_rawDataLoad.ipynb

Loads raw data into PostgreSQL

002_candidatosEDA.ipynb

Performs exploratory data analysis (EDA)

003_cleanDataLoad.ipynb

Cleans and transforms the dataset

📌 Important: During data cleaning, we verified that the is_hire column was included to track hiring status.
Recuerde elegir el kernel de Python correcto al momento de ejecutar el notebook e instalar ipykernel para soportar notebooks Jupyter en VS Code.

Conectar la base de datos con Power BI

Abra Power BI Desktop y cree un nuevo panel. Seleccione la opción Obtener datos ; asegúrese de elegir la opción "Base de datos PostgreSQL".
Inserte el nombre del servidor PostgreSQL y de la base de datos.
Llene los siguientes campos con sus credenciales.
Si logras conectarte a la base de datos aparecerán las siguientes tablas:
¡Elige la tabla candidates_hired y empieza a hacer tus propias visualizaciones!
