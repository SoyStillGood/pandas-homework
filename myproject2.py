import argparse
import pandas as pd
import matplotlib.pyplot as plt
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", dest="file", help="input data file")

    args = parser.parse_args()
    file = args.file

    diabetes = pd.read_csv(filepath_or_buffer=file, sep=' ', header=0)
    print(diabetes)
    diabetes_df = pd.DataFrame(data=diabetes)


    plt.plot(diabetes_df['age'])
    plt.title('age deviation by index')
    plt.xlabel('index')
    plt.ylabel('age deviation')
    plt.show()






if __name__ == "__main__":
    main()