# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 15:00:37 2019

@author: emtsdmr
"""

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    
    def permutation(sequence, chosen):

        if sequence == "":
            result.append(chosen)
        else:
            for i in range(len(sequence)):

                c = sequence[i]        
                chosen += c
                sequence = sequence[:i] + sequence[i+1:]
                permutation(sequence,chosen)        
                sequence = sequence[:i] + c + sequence[i:]
                chosen = chosen[:-1]        

    result=[]
    permutation(sequence,"")
    return result

if __name__ == '__main__':
    #EXAMPLE
    example_input ='abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    pass #delete this line and replace with your code here


