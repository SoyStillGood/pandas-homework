import argparse
import pandas as pd
import matplotlib.pyplot as plt
import os

def load_file():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", dest="file", help="input data file")

    args = parser.parse_args()
    file = args.file

    diabetes = pd.read_csv(filepath_or_buffer=file, sep=' ', header=0)
    print(diabetes)

def make_DF():
    diabetes = pd.read_csv(filepath_or_buffer=file, sep=' ', header=0)
    print(diabetes)
    return pd.DataFrame(data=diabetes)

def plotting(diabetes_df):
    plt.plot(diabetes_df['age'])
    plt.title('age deviation by index')
    plt.xlabel('index')
    plt.ylabel('age deviation')
    plt.show()



def main():
    load_file()
    diabetes_df = make_DF()
    plotting(diabetes_df)


if __name__ == "__main__":
    main()

