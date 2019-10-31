import argparse
import pandas as pd

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", dest="file", help="input data file")

    args = parser.parse_args()
    file = args.file

    diabetes = pd.read_csv(filepath_or_buffer=file, sep=' ', header=0)
    diabetes_df = pd.DataFrame(data=diabetes)
    print(diabetes_df)


if __name__ == "__main__":
    main()