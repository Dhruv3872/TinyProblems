A Python project containing tiny problems and their coding solutions.  
It's for the sake of practising Python programming.

### Changes made in this commit:
- Took care of the following test cases for the following problems:
  - 9_remove_duplicate_characters:
      - Output does not follow character sequence of the string  
    given to the function: Rewrote the function using dictionaries  
    instead of sets to resolve this issue.
  - The following programs were initially written using numpy library:
    - 10, 11, 12. I made them work without the use of the library.
  - 13 & 14: While asking for input values from the user, these programs  
  were printing a generalised message. I made it more relevant by  
  including the column number and row number in it.
  - 15: 
    - Renamed it to `create_nxn_matrix` to enable it to be imported into  
    another Python file as files beginning with a digit cannot be  
    imported as per the Python module import rules.
      - This also mandated removal of the line which runs the function as  
      the line made the function run explicitly  when we run a file  
      containing the import.
    - Made arrangements to show the print message in the form of  
    `Enter value for row x column y` at every iteration step.
  - 16: Imported the module `create_nxn_matrix` to use it to obtain values  
  for an nxn matrix from the user as the first step to solve this problem.
  - 17: Removed printing messages showing whether the given lists are  
  eligible matrices and whether the two given matrices are compatible.