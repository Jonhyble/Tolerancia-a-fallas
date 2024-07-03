from airflow.decorators import dag, task
from datetime import datetime

@dag(
    dag_id="read_txt",
    schedule=None,
    start_date= datetime(2023, 3, 12),
    tags=["document"]
)

def float_converter():
    @task()
    def read_file(path):
        archivo = open(path, "r")
        return archivo


    @task()
    def separate_lines(r):
        result = [float(line) for line in r]
        return result


    @task()
    def check_results(line):
        for number in line:
            print(number)


    path = "texto.txt"
    r = read_file(path)
    line = separate_lines(r)
    check_results(line)


float_converter()