from prefect import Flow, task, Parameter

@task
def read_file(path):
    archivo = open(path, "r")
    return archivo


@task
def separate_lines(r):
    result = [float(line) for line in r]
    return result


@task
def check_results(line):
    for number in line:
        print(number)


def build_flow():
    with Flow("first_flow") as f:
        path = Parameter(name="path", required=True)
        r = read_file(path)
        line = separate_lines(r)
        check_results(line)

    return f


if __name__ == "__main__":
    flow = build_flow()
    flow.run(parameters= {
        "path" : "texto.txt"
    })