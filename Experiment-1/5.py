num_list = [1, 7, -9, 21, 11, 0, -22, 5, -4, -1, 8]

positive_list = list(filter(lambda x: x>0, num_list))
negative_list = list(filter(lambda x: x<0, num_list))

print(f"Positive numbers: {positive_list}")
print(f"Negative numbers: {negative_list}")