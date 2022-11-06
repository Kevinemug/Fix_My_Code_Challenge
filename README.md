# Fix_My_Code_Challenge


## Requirements
### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be compiled on Ubuntu 20.04 LTS
- All your files should end with a new line
- A `README.md` file, at the root of the folder of the project is mandatory
## Background Context

Fix a code is a new type of project, where we will jump into an existing code base and fix it.

Sometimes you will know the language, sometimes you won't.

Download the [0x00-Fix_My_Code_Challenge](https://github.com/holbertonschool/0x00-Fix_My_Code_Challenge) repository and use it as starter files for all fixes.

An important part of this project is that you don't have to recode everything, just fix it!

## Files

### 0-fizzbuzz.py
Please take a look at my implementation of FizzBuzz in Python: [source code](https://github.com/holbertonschool/Fix-my-code-0/blob/master/0-fizzbuzz.py)

Something is going wrong….

`15` should print `FizzBuzz` not Fizz
```Python
$ ./0-fizzbuzz.py 50
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 Fizz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 Fizz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44 Fizz 46 47 Fizz 49 Buzz
$
```

### 1-print_square.js
Please take a look at my implementation of printing a square in Javascript: [source code](https://intranet.hbtn.io/rltoken/1HbXCw-nF028p5VlBAfedQ)

Something is going wrong….

./1-print_square.js 10 should print a square of size 10…
```JavaScript
$ ./1-print_square.js 4
####
####
####
####
$ ./1-print_square.js 10
################
################
################
################
################
################
################
################
################
################
################
################
################
################
################
################
$
```

### 2-sort.rb
Please find here my implementation of sorting arguments in Ruby: [source code](https://intranet.hbtn.io/rltoken/5E7Rrq_70OutipYULjh6Gw)

Something is going wrong….
```Ruby
$ ruby 2-sort.rb 12 41 2 C 9 -9 31 fun -1 32
31
32
12
41
2
9
-9
-1
$
```

### 3-user.py
Please find here my implementation of a User class in Python: [source code](https://github.com/holbertonschool/Fix-my-code-0/blob/master/3-user.py)

Something is going wrong….
```Python
$ ./3-user.py 
Test User
is_valid_password should return True if it's the right password
$
```

## Double linked list / directory 4-delete_dnodeint
### add_dnodeint_end.c / delete_dnodeint_at_index.c / free_dlistint.c / lists.h / main.c / print_dlistint.c

Please find here my implementation of a Double linked list in C: source code

Something is going wrong…. It doesn’t look right…
```C
$ gcc -Wall -pedantic -Werror -Wextra -std=gnu89 main.c free_dlistint.c print_dlistint.c add_dnodeint_end.c delete_dnodeint_at_index.c -o delete_dnodeint
$ ./delete_dnodeint 
0
1
2
3
4
98
402
1024
-----------------
0
1
2
3
4
0
402
1024
-----------------
1
2
3
4
0
402
1024
-----------------
2
3
4
0
402
1024
-----------------
3
4
0
402
1024
-----------------
4
0
402
1024
-----------------
0
402
1024
-----------------
402
1024
-----------------
-----------------
-----------------
-----------------
-----------------
-----------------
-----------------
-----------------
-----------------
-----------------
$
```