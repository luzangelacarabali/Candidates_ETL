import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# Construir la URL de conexión
DATABASE_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

def get_engine():
    """Devuelve un objeto SQLAlchemy Engine para la conexión a la base de datos."""
    return create_engine(DATABASE_URL)




