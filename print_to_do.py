#!/usr/bin/env python3
import os
DIV = "=" * 50
f_name = 'to_do_functions.txt'
with open(f_name) as file:
	#funcs = file.read().splitlines()
	funcs = [line.strip() for line in file]
prefix = 'ft_'
total_to_do_funcs = [prefix + word + ".c" for word in funcs]
total_funcs = len(total_to_do_funcs)
print(f"All functions to do {len(funcs)}:\n{', '.join(funcs)}")
files_lst = os.listdir('.')
to_do_funcs = [func for func in total_to_do_funcs if func not in files_lst]
done = [file for file in files_lst if file in total_to_do_funcs]
print(DIV)
print(f"Left to do {len(to_do_funcs)}:\n{', '.join(to_do_funcs)}")
print(DIV)
print(f"Done {len(done)}/{total_funcs}:\n{', '.join(done)}")
print(DIV)
print("Check suspicios files:")
print(f"{', '.join([file for file in files_lst if file not in total_to_do_funcs])}")