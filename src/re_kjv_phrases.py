#!/usr/bin/env python3
# Author: Boaty McBoatface bmcboatface@wesmont.edu

import re


def main():
    # Open up the KJV Bible and get its entire content
    # into a sing string variable named `kjv_bible`.
    # Ideally, we'd use nltk to do this, but I'm going to have you
    # use the static file for this one for autograding purposes.
    with open('../data/bible-kjv.txt', 'r') as file:
        kjv_bible = file.read().replace("\n", " ")
    
    # Put together a regular expression (regex) pattern to match
    # any sentence that has "I said" anywhere within the sentence.
    pattern_i_said = re.compile(r"(I said[^\.!?]*[\.!?])")
    
    
    """''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    TODO: Using the example above, modify the regex and replace the
          "WRITE THIS REGEX YOURSELF!" in the statements below.
          
          `pattern_god_is` should be a pattern to match any sentence
              that has "God is" anywhere within the sentence.
              
          `pattern_jesus_is` should be a pattern to match any sentence
              that has "Jesus" anywhere within the sentence.  
              
          `pattern_mine` should be a pattern of your own creation
              to see if you can find any other interesting matches.
              
        !!! DELETE THIS BLOCK COMMENT ONCE YOU COMPLETE THIS TASK !!!
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""
    pattern_god_is = re.compile(r"WRITE THIS REGEX YOURSELF!")
    pattern_jesus = re.compile(r"WRITE THIS REGEX YOURSELF!")
    pattern_mine = re.compile(r"WRITE THIS REGEX YOURSELF!")
    
    
    # Uses `re.findall` to find all matches within the `kjv_bible`.
    # Return type of `re.findall` is a list (of all matched substrings).
    matches_i_said = re.findall(pattern_i_said, kjv_bible)
    matches_god_is = re.findall(pattern_god_is, kjv_bible)
    matches_jesus = re.findall(pattern_jesus, kjv_bible)
    matches_mine = re.findall(pattern_mine, kjv_bible)
    
    
    """''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    TODO: If you are curious as to what kind of matches we are getting here,
          uncomment the line below and pass in different `matches_*` variable
          in to the `print_matches` function. Once you're done experimenting,
          be sure to comment this back out or delete it alltogether before 
          submitting your code (i.e., git push)!

        !!! DELETE THIS BLOCK COMMENT ONCE YOU COMPLETE THIS TASK !!!
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""
    # print_matches(matches_i_said)
    
    
    # DO NOT MODIFY THIS STATEMENT; THIS IS USED FOR AUTOGRADING.
    # Print out how many matches we got for each pattern we defined.
    print(("\n" + "{:>20} {:7d}\n"*4).format(
        "I said ...", len(matches_i_said),
        "God is ...", len(matches_god_is),
        "Jesus ...", len(matches_jesus),
        "My Pattern ...", len(matches_mine)
    ))
    

def print_matches(matches):
    print("\n--> ".join(matches))


if __name__ == '__main__':
    main()