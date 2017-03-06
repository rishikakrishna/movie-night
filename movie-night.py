"""
Determines which titles are in common between different lists.
Authors: Rishika Krishna

Input: user watchlists (as .txt files right now)
Output: sequence of common items 
"""

import argparse

def watch(p1_file,p2_file):
    """
    Reads a files containing a list of arbitrarily ordered titles
    and prints the output of those that are present in both.
    
    args:
        p1_file: external .txt file containing the people you follow
        p2_file: external .txt file containing your followers
    returns:
        a sequence of titles in common
    """
    p1 = [ ]
    for line in p1_file:
        p1.append(line.strip())

    p2 = [ ]
    for line in p2_file:
        p2.append(line.strip())

    for title in p1:
        if title in p2:
            print(title)

def main( ):
    """
    Interaction if run from the command line.
    Usage: python movie-night.py p1_file.txt p2_file.txt
    """
    parser = argparse.ArgumentParser(description="Compare watchlists")
    parser.add_argument('p1', type=argparse.FileType('r'),
                        help="Text files containing the first person's watchlist")
    parser.add_argument('p2', type=argparse.FileType('r'),
                        help="Text files containing the second person's watchlist")
    args = parser.parse_args()  # gets arguments from command line
    p1_file = args.p1
    p2_file = args.p2
    watch(p1_file,p2_file)
    
    
if __name__ == "__main__":
    main( )