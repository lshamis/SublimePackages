# SublimePackages

Random SublimeText3 packages I wrote that might be useful to others.

## replace_with_python_result

Replaces all highlighted regions with the Python interpretation.
A variable `i` is automatically defined to the region index.

Example:
  `40 + 2` -> `42`

  Before:
 
    10 + i
    10 + i
  After:
  
    10
    11

## replace_with_shell_result

Replaces all highlighted regions with the Shell interpretation.

  `pwd: *pwd*` -> `*~/code/project*`

## natural_sort

Sorts a selected list of lines in a "natural way". Numeric segments of a string are compared by value, rather of lexicographically.

  Before:

    file1.txt
    file10.txt
    file2.txt
    file20.txt
  After:
  
    file1.txt
    file2.txt
    file10.txt
    file20.txt
