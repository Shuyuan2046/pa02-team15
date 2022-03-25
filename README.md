# pa02-team15

Script started on Fri Mar 25 09:30:34 2022
[1m[7m%[27m[1m[0m

[0m[27m[24m[J(base) luhao@MacBook-Pro pa02-team15 % [K[?2004hexitpython transactions.py[?2004l

[1m[7m%[27m[1m[0m

[0m[27m[24m[J(base) luhao@MacBook-Pro pa02-team15 % [K[?2004hppython tracker.py[?2004l

0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu
12. summarize transactions by recent years
13. show db
14. summarize transactions by amount
15. check if the item exits in the database
16. summarize trasactions by month and category
17. summarize transactions by name and year

## 1. show categories

> 1

## id name description

1 seafood shrimp, fish  
2 meat chicken, beef  
3 drink juice, coke  
4 electric phone, computer  
5 clothes dress, pants  
6 furniture home

## 2. add category

> 2
> category name: entertainment
> category description: fun

## 3. modify category

> 3
> modifying category
> rowid: 1
> new category name: seafood
> new category description: shrimp, s fish, crab

## 4. show transactions

> 4

## item # amount category date description

apple 2 food 20220322 grocery  
beef 1 meat 20220317 dinner

## 5. add transaction

> 5
> item of transaction: fish
> amount of transaction: 3
> category of the transaction: seafood
> date of the transaction(yyyymmdd): 20220324
> description of the transaction: seafood

> 4

## item # amount category date description

apple 2 food 20220322 grocery  
beef 1 meat 20220317 dinner  
fish 3 seafood 20220324 seafood

## 6. delete transaction

> 6
> delete transaction
> rowid: 3
> 4

## item # amount category date description

apple 2 food 20220322 grocery  
beef 1 meat 20220317 dinner

## 7. summarize transactions by date

> 7
> enter the date of transaction you want to see: 22

## item # amount category date description

apple 2 food 20220322 grocery

## 8. summarize transactions by month

> 8
> enter the month of transaction you want to see: 3

## item # amount category date description

apple 2 food 20220322 grocery  
beef 1 meat 20220317 dinner

## 9. summarize transactions by year

> 9
> enter the year of transaction you want to see: 2022

## item # amount category date description

apple 2 food 20220322 grocery  
beef 1 meat 20220317 dinner

## 10. summarize transactions by category

> 10
> enter the category of transaction you want to see: fop od

## item # amount category date description

apple 2 food 20220322 grocery

## 11. print this menu

> 11

0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu
12. summarize transactions by recent years
13. show db
14. summarize transactions by amount
15. check if the item exits in the database
16. summarize trasactions by month and category
17. summarize transactions by name and year

## 12. summarize transactions by recent years

> 12
> enter the start year of transaction you want to see: 2022

## item # amount category date description

apple 2 food 20220322 grocery  
beef 1 meat 20220317 dinner

## 13. show db

> 13

## item # amount category date description

apple 2 food 20220322 grocery  
beef 1 meat 20220317 dinner

## 14. summarize transactions by amount

> 14
> enter the amount of items' transaction you want to see: 2

## item # amount category date description

apple 2 food 20220322 grocery

## 15. check if the item exits in the database

> 15
> What item do you want to check: beef

## item # amount category date description

beef 1 meat 20220317 dinner

## 16. summarize trasactions by month and category

> 16
> enter the month of transaction you want to see: 3
> enter the category of transaction you want to see: food

## item # amount category date description

apple 2 food 20220322 grocery

## 17. summarize transactions by name and year

> 17
> enter the item of transaction you want to see: apple
> enter the year of transaction you want to see: 2022

## item # amount category date description

apple 2 food 20220322 grocery

> ^CTraceback (most recent call last):
> File "/Users/luhao/Desktop/pa02-team15/tracker.py", line 194, in <module>

    toplevel()

File "/Users/luhao/Desktop/pa02-team15/tracker.py", line 162, in toplevel
choice = process_choice(choice)
File "/Users/luhao/Desktop/pa02-team15/tracker.py", line 151, in process_choice
choice = input("> ")
KeyboardInterrupt

[1m[7m%[27m[1m[0m

## pylint transactions.py

[0m[27m[24m[J(base) luhao@MacBook-Pro pa02-team15 % [K[?2004hppylint transactions.py[?2004l

******\******* Module transactions
transactions.py:7:0: C0301: Line too long (143/100) (line-too-long)
transactions.py:42:0: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:46:0: C0301: Line too long (108/100) (line-too-long)
transactions.py:65:0: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:74:0: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:83:0: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:101:0: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:115:0: C0301: Line too long (102/100) (line-too-long)
transactions.py:139:0: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:149:0: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:164:0: C0301: Line too long (112/100) (line-too-long)
transactions.py:170:0: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:1:0: C0114: Missing module docstring (missing-module-docstring)
transactions.py:14:0: C0115: Missing class docstring (missing-class-docstring)
transactions.py:34:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:43:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:55:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:66:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:75:32: W0621: Redefining name 'date' from outer scope (line 1) (redefined-outer-name)
transactions.py:75:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:84:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:93:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:102:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:112:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:114:8: C0103: Variable name "c" doesn't conform to snake_case naming style (invalid-name)
transactions.py:121:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:131:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:141:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:151:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:161:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:1:0: W0611: Unused date imported from datetime (unused-import)

---

Your code has been rated at 7.67/10 (previous run: 7.76/10, -0.09)

[0m[1m[7m%[27m[1m[0m

## pylint tracker.py

[0m[27m[24m[J(base) luhao@MacBook-Pro pa02-team15 % [K[?2004hppylint tracker.py[?2004l

******\******* Module tracker
tracker.py:29:61: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:97:0: C0301: Line too long (108/100) (line-too-long)
tracker.py:152:0: C0325: Unnecessary parens after 'return' keyword (superfluous-parens)
tracker.py:179:37: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:195:0: C0305: Trailing newlines (trailing-newlines)
tracker.py:44:0: C0103: Constant name "menu" doesn't conform to UPPER_CASE naming style (invalid-name)
tracker.py:68:0: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:70:4: R1705: Unnecessary "elif" after "return" (no-else-return)
tracker.py:68:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
tracker.py:68:0: R0912: Too many branches (19/12) (too-many-branches)
tracker.py:68:0: R0915: Too many statements (78/50) (too-many-statements)
tracker.py:158:4: W0105: String statement has no effect (pointless-string-statement)
tracker.py:182:0: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:185:0: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:36:0: W0611: Unused import sys (unused-import)
tracker.py:36:0: C0411: standard import "import sys" should be placed before "from transactions import Transaction" (wrong-import-order)

---

Your code has been rated at 8.55/10 (previous run: 8.09/10, +0.46)

[0m[1m[7m%[27m[1m[0m

## pytest test_transactions.py

[0m[27m[24m[J(base) luhao@MacBook-Pro pa02-team15 % [K[?2004httest  t  pytest test_transaction.py   s.py[?2004l

[1m=================================================== test session starts ===================================================[0m
platform darwin -- Python 3.9.7, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: /Users/luhao/Desktop/pa02-team15, configfile: pytest.ini
plugins: anyio-2.2.0
[1mcollecting ... [0m[1m
collected 10 items [0m

test_transactions.py [32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m [100%][0m

[32m=================================================== [32m[1m10 passed[0m[32m in 0.05s[0m[32m ====================================================[0m
[1m[7m%[27m[1m[0m

[0m[27m[24m[J(base) luhao@MacBook-Pro pa02-team15 % [K[?2004heexit[?2004l

Script done on Fri Mar 25 09:35:52 2022
