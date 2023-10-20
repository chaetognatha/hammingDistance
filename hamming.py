import pandas as pd
import itertools
import sys


def getHam(str1,str2):
    count = 0
    for i , _ in enumerate(str1):
        if str1[i] != str2[i]:
            count += 1
    return count

def make_list(df, col1, col2):
    """
    There will be two columns in a dataframe with
    strings that need to be combined
    then all combined strings will be returned as list
    """
    
    alist = []
    for _ , row in df.iterrows():
        alist.append(row[col1] + row[col2])
    return alist


def compare_all(alist):
    """
    Will compare all strings against every other string in a list
    and return the strings that have > 3 in hamming distance
    """
    for a, b in itertools.combinations(alist, 2):
        if getHam(a,b) < 6:
            print(a,b)

def main():
    # take a file path as a parameter and read it into a dataframe
    df = pd.read_csv(sys.argv[1])
    # drop rows with null values
    df.dropna(subset=['INDEX1', 'INDEX2'], inplace=True)    
    # make a list of all the strings (INDEX1 + INDEX2)
    alist = make_list(df, 'INDEX1', 'INDEX2')
    # compare all strings in the list and print the ones that have < 6 combined
    compare_all(alist)
    """
    TODO: We have already printed when INDEX1 + INDEX2 have a bad (< 3 + 3)
    hamming distance. Now we need to make functions that treat the sets of indexes
    separately and finds poor hamming distance within the set.

    So instead of doing INDEX1 + INDEX2, we will do all INDEX1 vs all INDEX1 and same for INDEX2
    """


if __name__ == '__main__':
    main()