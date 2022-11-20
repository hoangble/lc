def dna_match_topdown(DNA1, DNA2):
    """    Recursive function that determines the longest common sequence    
    :param DNA1: String 1    
    :param DNA2: String 2    
    :return: Integer which represents the longest common sequence    """    
    # Length of each DNA    
    index1 = len(DNA1)
    index2 = len(DNA2)
    cache = [[0 for x in range(index2 + 1)] for x in range(index1 + 1)]
    dna_topdown_helper(DNA1, DNA2, index1, index2, cache)
    print(cache)

def dna_topdown_helper (DNA1, DNA2, i, j, cache):
    # Base case    
    if i == 0 or j == 0:
        return 0    # Check if there is a value in the cache already    
    elif cache[i][j] != 0:
        return cache[i][j]
    # If there is a match    
    elif DNA1[i - 1] == DNA2[j - 1]:
        cache[i][j] = 1 + dna_topdown_helper(DNA1, DNA2, i - 1, j - 1, cache)
    # No Match    
    else:
        value1 = dna_topdown_helper(DNA1, DNA2, i - 1, j, cache)
        value2 = dna_topdown_helper(DNA1, DNA2, i, j - 1, cache)
        cache[i][j] = max(value1, value2)
