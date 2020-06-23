def get_permutation(lst):
   # For an empty list, there is no permutation
   if len(lst) == 0:
       return []
   # list with one element will have only one
   # permutation
   if len(lst) == 1:
       return [lst]
  # Create an empty list to store permutation
   perms = []
   for i in range(len(lst)):
       # Extract current elemnt from the list.
       current = lst[i]
       # Recursively call permutation for the
       # remaining list
       rem_list = lst[:i] + lst[i+1:]
       rem_perm = get_permutation(rem_list)
       # Generate permutations by adding first element
       for p in rem_perm:
           perms.append([current] + p)
   return perms
# now test the function
data = [1,2,3]
for perm in get_permutation(data):
   print (perm)
