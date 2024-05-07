def subsequence(source, target):
    """
    :type source, target: str
    :rtype: bool
    """
    count = 0  
    i = 0  
    while i < len(target):
        subseq_pos = 0  
        matched = False  
        while i < len(target) and subseq_pos < len(source):
            if target[i] == source[subseq_pos]:  
                i += 1  
                matched = True  
            subseq_pos += 1  
        if not matched:  
            return -1
        count += 1  
    return count

# test
print(subsequence("abc", "abcbc"))  
print(subsequence("abc", "acdbc"))  
print(subsequence("xyz", "xzyxz"))  
