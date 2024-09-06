FROM apache/airflow:2.6.3

# Troca para o usuário airflow
USER airflow

# Instala o pacote flask-admin
RUN pip install flask-admin
