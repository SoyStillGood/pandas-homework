import argparse
import pandas as pd

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", dest="file", help="input data file")

    args = parser.parse_args()
    file = args.file

    insurance = pd.read_csv(filepath_or_buffer=file, header=0)
    insurance_df = pd.DataFrame(data=insurance)
    #print(insurance_df)
    print(insurance_df['age'])
    print(insurance_df[['age', 'children', 'charges']])
    print(insurance_df.loc[[1, 2, 3, 4, 5], ['age', 'children', 'charges']])
    print(insurance_df['charges'].describe())
    print(insurance_df.info('charges'))
    print(insurance_df[(insurance_df['charges'] == 10797.3362)])
    print(insurance_df[(insurance_df['charges'] == 63770.428010)])
    print(insurance_df['region'].value_counts)
    print(insurance_df.groupby('region').nunique())
    #print(insurance_df[insurance_df['age'] < 18])
    print(insurance_df['children'].value_counts())
    print(insurance_df.corr(method='pearson'))






if __name__ == "__main__":
    main()