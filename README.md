libfta_script
To check progress and files on Libfta library project for '42 cursus'
Lists 1) the mandotory functions, 2) what functions are left to be done. 3) "suspicios" files that probablly should not be there.
##How to use:
Clone/download and the executable permission to the 'print_to_do.py' and then run 'print_to_do.py'. 
Alternatively run without the executable permission like: 'python3 ./print_to_do.py'

by Alex Artamonov

Sample output:

All functions to do 23:
isalpha, isdigit, isalnum, isascii, isprint, strlen, memset, bzero, memcpy, memmove, strlcpy, strlcat, toupper, tolower, strchr, strrchr, strncmp, memchr, memcmp, strnstr, atoi, calloc, strdup
==================================================
Left to do 14:
ft_memset.c, ft_bzero.c, ft_memcpy.c, ft_memmove.c, ft_strlcpy.c, ft_strlcat.c, ft_strchr.c, ft_strrchr.c, ft_strncmp.c, ft_memchr.c, ft_memcmp.c, ft_strnstr.c, ft_calloc.c, ft_strdup.c
==================================================
Done 9/23:
ft_atoi.c, ft_isalnum.c, ft_isalpha.c, ft_isascii.c, ft_isdigit.c, ft_isprint.c, ft_strlen.c, ft_tolower.c, ft_toupper.c
==================================================
Check suspicios files:
.git, .gitignore, .Makefile.swp, a.out, libft.h, libft.o, Makefile, print_to_do.py, tests.c, to_do_functions.txt
