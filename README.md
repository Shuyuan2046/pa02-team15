# pa02-team15

pylint: No problems have been detected in the workplace.

#Lingyu Liu: 
transactions.py : show_db: show the datas in db
                  summarize_by_recent_year: summarize from starting year
                  summarize_by_name_year: summarize by input name and year

test_transactions.py: test_summarize_by_name_year, test_showdb, test_summarize_by_recent_year

Script started on Fri Mar 25 00:22:34 2022
[1m[7m%[27m[1m[0m                                                                               
 
]7;file://liulingyus-MacBook-Pro.local/Users/ll/desktop/103/pa2/pa2
[0m[27m[24m[J(base) ll@liulingyus-MacBook-Pro pa2 % [K[?2004hppyt lint transactions.py[?2004l

************* Module transactions
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

-----------------------------------
Your code has been rated at 7.67/10

[0m[1m[7m%[27m[1m[0m                                                                               
 
]7;file://liulingyus-MacBook-Pro.local/Users/ll/desktop/103/pa2/pa2
[0m[27m[24m[J(base) ll@liulingyus-MacBook-Pro pa2 % [K[?2004hppytest test_tan  ransactions.py[?2004l

[1m============================= test session starts ==============================[0m
platform darwin -- Python 3.9.7, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: /Users/ll/Desktop/103/pa2/pa2, configfile: pytest.ini
plugins: anyio-2.2.0
[1mcollecting ... [0m[1m
collected 10 items                                                             [0m

test_transactions.py [32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m                                          [100%][0m

[32m============================== [32m[1m10 passed[0m[32m in 0.06s[0m[32m ==============================[0m
[1m[7m%[27m[1m[0m                                                                               
 
]7;file://liulingyus-MacBook-Pro.local/Users/ll/desktop/103/pa2/pa2
[0m[27m[24m[J(base) ll@liulingyus-MacBook-Pro pa2 % [K[?2004hppython traa cek  ker.py[?2004l


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
12. upate transaction
13. summarize transactions by recent years
14. show db
15. summarize transactions by amount
16. check if the item exits in the database
17. summarize trasactions by month and category
18. summarize transactions by name and year

> 14


item #     amount     category   date       description                   
----------------------------------------
banana     1          food       20220318   lunch                         
apple      1          food       20220317   dinner                        
> 13
enter the start year of transaction you want to see: 2022


item #     amount     category   date       description                   
----------------------------------------
banana     1          food       20220318   lunch                         
apple      1          food       20220317   dinner                        
> 18
enter the item of transaction you want to see: apple
enter the year of transaction you want to see: 2022


item #     amount     category   date       description                   
----------------------------------------
apple      1          food       20220317   dinner                        
> exit
choice exit not yet implemented
> 0
bye
[1m[7m%[27m[1m[0m                                                                               
 
]7;file://liulingyus-MacBook-Pro.local/Users/ll/desktop/103/pa2/pa2
[0m[27m[24m[J(base) ll@liulingyus-MacBook-Pro pa2 % [K[?2004heexit[?2004l

Saving session...
...copying shared history...
...saving history...truncating history files...
...completed.
Deleting expired sessions...      52 completed.

Script done on Fri Mar 25 00:23:38 2022