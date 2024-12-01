import subprocess

def main():
    """
    Starts the Jupyter Notebook server and opens the specified notebook file.
    """
    subprocess.run(["jupyter", "notebook", "experiment/puzzle8_experiment.ipynb"])

if __name__ == "__main__":
    main()
