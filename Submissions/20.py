sample_dict = {'a': 3, 'b': 1, 'c': 2, 'd': 5, 'e': 4} 

sorted_dict_asc = dict(sorted(sample_dict.items(), key=lambda item: item[1])) 
print("Ascending Order:", sorted_dict_asc) 

sorted_dict_desc = dict(sorted(sample_dict.items(), key=lambda item: item[1], reverse=True)) 
print("Descending Order:", sorted_dict_desc) 
