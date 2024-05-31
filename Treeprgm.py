#Dictionary 3-trees
Families={
           'Raju':
           {'shethal':{'rahim','merry'},
            'Nexa':{'Rosy'}},
           'Yakub':
           {'Tommy':{'puppy'},
            'Timmy':{'Hamster'},
            'tanny':{'Hamster'}},
           'carles':
           {'Digo':'cat','forest':'fox'}
           }
for parent,children in Families.items():
     print("(parent) has (len(children);kid(s):")
     print(" {',and '.join([str(child) for child in[*children]])}")
               
           