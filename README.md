# Workshop #1: Data Engineering

## By Luz Ángela Carabalí Mulato (@luzangelacarabli)

---

## ✨ Overview

In this workshop, we worked with  candidate data stored in a CSV file. The objective was to load, clean, and transform the data to extract meaningful insights using Python, Jupyter Notebook, PostgreSQL, and Power BI.

---

## 🛠 Tools Used

- **Python 3.12** ➜ [Download](https://www.python.org/downloads/)
- **Jupyter Notebook** ➜ [VS Code extension for notebooks](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)
- **PostgreSQL** ➜ [Download](https://www.postgresql.org/download/)
- **Power BI (Desktop version)** ➜ [Download](https://powerbi.microsoft.com/en-us/downloads/)

---

## 📦 Required Python Libraries

These libraries are included in the Poetry project configuration file (`pyproject.toml`):

- `pandas`
- `matplotlib`
- `seaborn`
- `sqlalchemy`
- `dotenv`
- `numpy`
- `scikit-learn`
- `psycopg2`

The step-by-step installation process will be described later.

---

## 📊 Dataset Information

The dataset (`candidates.csv`) contains **50,000 rows** and **10 columns**, each describing a candidate in the recruitment process. After transformations, the dataset is optimized for Power BI visualization.

### **Dataset Structure**

| Column Name               | Data Type | Description                                  |
|---------------------------|-----------|----------------------------------------------|
| `first_name`             | Object    | Candidate's first name                      |
| `last_name`              | Object    | Candidate's last name                       |
| `email`                  | Object    | Candidate's email                           |
| `country`                | Object    | Candidate's country of residence           |
| `application_date`       | Object    | Date of application submission             |
| `yoe` (Years of Experience) | Integer | Candidate's total years of experience      |
| `seniority`              | Object    | Candidate’s seniority level                |
| `technology`             | Object    | Technology the candidate specializes in    |
| `code_challenge_score`   | Integer   | Score obtained in the coding challenge     |
| `technical_interview_score` | Integer | Score obtained in the technical interview |

---

## 🚀 Running the Project

### 1️⃣ Clone the Repository

```sh
git clone  https://github.com/luzangelacarabali/Candidates_ETL.git
cd Candidates_ETL
```

### 2️⃣ Install Dependencies with Poetry


To install Poetry, follow [this link](https://hickory-advantage-9e8.notion.site/installation-poetry-1aa6979ac44380848b2cf0f3f4a423ca?pvs=4).

### 4️⃣ Configure the Database Connection

To establish the database connection, we use the `connection_db.py` module. This script loads environment variables from a configuration file. Follow these steps to set it up:

1. Create an `.env` file inside a new `env/` directory in the cloned repository.
2. Add the following environment variables (without quotes):

```sh
PG_HOST=DB_HOST
PG_PORT=DB_PORT
PG_USER=<your_postgresql_user>
PG_PASSWORD=<your_password>
PG_DRIVER=postgresql+psycopg2
PG_DATABASE=<your_database_name>

```

### 5️⃣ Create the Database

Ensure that your PostgreSQL database name matches the one in the `.env` file before proceeding.

---

## 📝 Data Processing and Notebook Execution

### **Executing the Notebooks**

We use Jupyter Notebook to process and transform the dataset. Execute the notebooks in the following order:

| Notebook                  | Purpose                                      |
|---------------------------|----------------------------------------------|
| `001_extrac.ipynb`   | Loads raw data into PostgreSQL              |
| `002_candidatosEDA.ipynb` | Performs exploratory data analysis (EDA)    |
| `003_cleanDataLoad.ipynb` | Cleans and transforms the dataset           |

📌 **Important:** During data cleaning, we verified that the `is_hire` column was included to track hiring status.

> **Reminder:** Select the correct Python kernel when running the notebook and install `ipykernel` to support Jupyter notebooks in VS Code.

---

## 🔗 Connect the Database with Power BI

1. Open **Power BI Desktop** and create a new dashboard.
2. Select the option **Get Data** and choose **PostgreSQL Database**.
3. Insert the **PostgreSQL server name** and **database name**.
4. Fill in your **credentials**.
5. If the connection is successful, the following tables will appear:

🎯 **Select the `cleaned_candidates` table and start creating your visualizations!**

---
Thank you! 😊

