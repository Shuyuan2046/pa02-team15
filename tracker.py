#! /opt/miniconda3/bin/python3
'''
tracker is an app that maintains a list of personal
financial transactions.

It uses Object Relational Mappings (ORM)
to abstract out the database operations from the
UI/UX code.

The ORM, Category, will map SQL rows with the schema
  (rowid, category, description)
to Python Dictionaries as follows:

(5,'rent','monthly rent payments') <-->

{rowid:5,
 category:'rent',
 description:'monthly rent payments'
 }

Likewise, the ORM, Transaction will mirror the database with
columns:
amount, category, date (yyyymmdd), description

In place of SQL queries, we will have method calls.

This app will store the data in a SQLite database ~/tracker.db

Note the actual implementation of the ORM is hidden and so it 
could be replaced with PostgreSQL or Pandas or straight python lists

'''

from transactions import Transaction
from category import Category
import sys

transactions = Transaction('tracker.db')
category = Category('tracker.db')


# here is the menu for the tracker app

menu = '''
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
'''




def process_choice(choice):

    if choice=='0':
        return
    elif choice=='1':
        cats = category.select_all()
        print_categories(cats)
    elif choice=='2':
        name = input("category name: ")
        desc = input("category description: ")
        cat = {'name':name, 'desc':desc}
        category.add(cat)
    elif choice=='3':
        print("modifying category")
        rowid = int(input("rowid: "))
        name = input("new category name: ")
        desc = input("new category description: ")
        cat = {'name':name, 'desc':desc}
        category.update(rowid,cat)
    elif choice == '4':
        trans = transactions.select_all()
        print_transactions(trans)
        #print(trans)
    elif choice =='5':
        item = input("item of transaction: ")
        amount = int(input("amount of transaction: "))
        cate = input("category of the transaction: ")
        date = int(input("date of the transaction(yyyymmdd): "))
        description = input("description of the transaction: ")
        trans = {'item': item, 'amount': amount, 'category': cate, 'date': date, 'description': description}
        transactions.add(trans)
    elif choice == '6':
        print("delete transaction")
        rowid = int(input("rowid: "))
        transactions.delete(rowid)
    elif choice == '7':
        asw = int(input("enter the date of transaction you want to see: "))
        trans = transactions.summarize_by_date(asw)
        print_transactions(trans)
    elif choice == '8':
        asw = int(input("enter the month of transaction you want to see: "))
        trans = transactions.summarize_by_month(asw)
        print_transactions(trans)
    elif choice == '9':
        asw = int(input("enter the year of transaction you want to see: "))
        trans = transactions.summarize_by_year(asw)
        print_transactions(trans)
    elif choice == '10':
        asw = input("enter the category of transaction you want to see: ")
        trans = transactions.summarize_by_category(asw)
        print_transactions(trans)
    elif choice == '11':
        print(menu)
    elif choice == '12':
        print("upate transaction")
        rowid = int(input("rowid: "))
        item = input("new item of transaction: ")
        amount = int(input("new amount of transaction: "))
        cat = input("new category of the transaction: ")
        date = int(input("new date of the transaction(yyyymmdd): "))
        description = input("new description of the transaction: ")
        trans = {'item': item, 'amount': amount, 'category': cat, 'date': date, 'description': description}
        transactions.update(trans)
    elif choice=='13':
        year = int(input("enter the start year of transaction you want to see: "))
        trans = transactions.summarize_by_recent_year(year)
        print_transactions(trans)
    elif choice=='14':
        trans = transactions.show_db()
        print_transactions(trans)
    elif choice == '15':
        asw = input("enter the amount of items' transaction you want to see: ")
        trans = transactions.summarize_by_amount(asw)
        print_transactions(trans)
    elif choice == '16':
        asw = input("What item do you want to check: ")
        trans = transactions.check_item(asw)
        print_transactions(trans)
    #Jing Cheng
    elif choice == '17':
        asw = int(input("enter the month of transaction you want to see: "))
        cat = input("enter the category of transaction you want to see: ")
        trans = transactions.summarize_by_month_cat(asw,cat)
        print_transactions(trans)
    else:
        print("choice",choice,"not yet implemented")

    choice = input("> ")
    return(choice)


def toplevel():
    ''' handle the user's choice '''

    ''' read the command args and process them'''
    print(menu)
    choice = input("> ")
    while choice !='0' :
        choice = process_choice(choice)
    print('bye')

#
# here are some helper functions
#

def print_transactions(items):
    ''' print the transactions '''
    if len(items)==0:
        print('no items to print')
        return
    print('\n')
    print("%-10s %-10s %-10s %-10s %-30s"%(
        'item #','amount','category','date','description'))
    print('-'*40)
    for item in items:
        values = tuple(item.values()) 
        print("%-10s %-10s %-10s %-10s %-30s"%values)

def print_category(cat):
    print("%-3d %-10s %-30s"%(cat['rowid'],cat['name'],cat['desc']))

def print_categories(cats):
    print("%-3s %-10s %-30s"%("id","name","description"))
    print('-'*45)
    for cat in cats:
        print_category(cat)


# here is the main call!

toplevel()

