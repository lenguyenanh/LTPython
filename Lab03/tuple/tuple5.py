# Python2 program to remove empty tuples
# from a list of tuples function to remove
# empty tuples using filter
def remove(tuples):
    for i in tuples:
        if len(i) == 0:
            tuples.remove(i)
    print(tuples)
    
tuples = [(), ('ram', '15', '8'), (), ('laxman', 'sita'),
          ('krishna', 'akbar', '45'), ('', ''), ()]
remove(tuples)
