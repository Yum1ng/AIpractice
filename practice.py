# -*- coding: utf-8 -*-
import collections

############################################################
# Problem 1a

def compute_max_word_length(text):
    """
    Given a string |text|, return the longest word in |text|.  If there are
    ties, choose the word that comes latest in the alphabet.
    A word is wwfined by a maximal sequence of characters without whitespaces.
    You might find max() and list comprehensions handy here.
    """
    # BEGIN_YOUR_CODE (around 1 line of code expected)
    return max(text.split());
    # END_YOUR_CODE

############################################################
# Problem 1b

def manhattan_distance(loc1, loc2):
    """
    Return the Manhattan distance between two locations, where the locations
    are pairs of numbers (e.g., (3, 5)).
    """
    # BEGIN_YOUR_CODE (around 1 line of code expected)
    return (abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1]));
    # END_YOUR_CODE

############################################################
# Problem 1c

def sparse_vector_dot_product(v1, v2):
    """
    Given two sparse vectors |v1| and |v2|, each represented as Counters, return
    their dot product.
    You might find it useful to use sum() and a list comprehension.
    """
    # BEGIN_YOUR_CODE (around 5 lines of code expected)
    product = 0;
    for number in v1:
        product += v1[number]*v2[number];
    return product;
    # END_YOUR_CODE

############################################################
# Problem 1d

def compute_most_frequent_word(text):
    """
    Splits the string |text| by whitespace and returns two things as a pair: 
    the set of words that occur the maximum number of times, and
	their count, i.e. (set of words that occur the most number of times, that maximum number/count)
    You might find it useful to use collections.Counter().
    """
    # BEGIN_YOUR_CODE (around 5 lines of code expected)

    words = text.split();
    c = collections.Counter(words);
    set1 = c.most_common();
    mfset = set();
    i = 1;
    mfset.add(set1[0][0]);
    while(i<len(set1)):
        if(set1[i][1] == set1[i-1][1]):
            mfset.add(set1[i][0]);
            i += 1;
        else: break;
    
    return (mfset,set1[0][1]);
    # END_YOUR_CODE

############################################################
# Problem 1e

def correct_parentheses(expression):
    """
    Checks if a given expression has a correct combination of opening and
    closing parentheses. (a+b)*c returns True, ((a+b) returns False.
    Hint: use stack
    """
    # BEGIN_YOUR_CODE
    k = 0;
    i = 0; 
    while(i < len(expression)):
        if(k < 0): return False;
        if(expression[i] == "("): k += 1;
        if(expression[i] == ")"): k -= 1;
        i += 1;

    if(k == 0): return True;
    else: return False;
    # END_YOUR_CODE
    
############################################################
# Problem 1f

def nested_parentheses(expression):
    """
    Must be done recursively. 
    Given a string, return true if it is a nesting of zero or more pairs of parenthesis, 
    like "(())" or "((()))". Suggestion: check the first and last chars, 
    and then recur on what's inside them. 

    nestedParentheses("(())") → true
    nestedParentheses("((()))") → true
    nestedParentheses("(((x))") → false
    
    Use this link to practice in Java first:
    http://codingbat.com/prob/p183174
    """
    # BEGIN_YOUR_CODE 
    raise Exception("Not implemented yet")
    # END_YOUR_CODE
   
