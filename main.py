import subprocess


def main():
    # Start Jupyter Notebook and open the specific notebook file
    subprocess.run(["jupyter", "notebook", "experiment/puzzle8_experiment.ipynb"])


if __name__ == "__main__":
    main()
