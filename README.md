# Bibseq

Break sequences into subsequences,
Where each subsequence begins with its leading, smallest element.

For example, the list

`[ 31, 41, 59, 26, 53, 58, 97, 93, 23, 84, 62, 64, 33 ]`

becomes the lists

`[31, 41, 59] [26, 53, 58, 97, 93] [23, 84, 62, 64, 33]`

Note that the leading elements are strictly monotonically decreasing, 
and decomposition is both complete and unique.
Every element is in a subsequence, 
subsequences do not overlap, 
and a sequence can only be decomposed one way.
