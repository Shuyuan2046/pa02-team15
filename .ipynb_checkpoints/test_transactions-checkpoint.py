import pytest
from transactions import Transaction, to_trans_dict

@pytest.fixture
def dbfile(tmpdir):
    ''' create a database file in a temporary file system '''
    return tmpdir.join('test_tracker.db')

@pytest.fixture
def empty_db(dbfile):
    ''' create an empty database '''
    db = Transaction(dbfile)
    yield db

@pytest.fixture
def small_db(empty_db):
    ''' create a small database, and tear it down later'''
    cat1 = {'item': 'banana', 'amount':1, 'category':'food', 'date': 20220318, 'description': 'lunch'}
    cat2 = {'item': 'apple', 'amount':1, 'category':'food', 'date': 20220317, 'description': 'dinner'}
    cat3 = {'item': 'ipad', 'amount':1, 'category':'electric', 'date': 20220316, 'description': 'study'}
    id1=empty_db.add(cat1)
    id2=empty_db.add(cat2)
    id3=empty_db.add(cat3)
    yield empty_db
    empty_db.delete(id3)
    empty_db.delete(id2)
    empty_db.delete(id1)

@pytest.mark.simple
def test_to_trans_dict():
    ''' teting the to_trans_dict function '''
    a = to_trans_dict(('testItem',1,'testCategory',20220318,'testDesc'))
    assert a['item']=='testItem'
    assert a['amount']==1
    assert a['category']=='testCategory'
    assert a['date']==20220318
    assert a['description']=='testDesc'
    assert len(a.keys())==5

@pytest.mark.add
def test_add(small_db):
    ''' add a category to db, the select it, then delete it'''

    cat0 = {'item':'testing_item',
            'amount': 1,
            'category': 'testing_category',
            'date': 20220000,
            'description':'see if it works',
            }
    cats0 = small_db.select_all()
    rowid = small_db.add(cat0)
    cats1 = small_db.select_all()
    assert len(cats1) == len(cats0) + 1
    cat1 = small_db.select_one(rowid)
    assert cat1['item']==cat0['item']
    assert cat1['item']==cat0['item']
    assert cat1['amount']==cat0['amount']
    assert cat1['category']==cat0['category']
    assert cat1['date']==cat0['date']
    assert cat1['description']==cat0['description']

@pytest.mark.delete
def test_delete(small_db):
    ''' add a category to db, delete it, and see that the size changes'''
    # first we get the initial table
    cats0 = small_db.select_all()

    cat0 = {'item':'testing_item',
            'amount': 1,
            'category':'testing_category',
            'date':20220318,
            'description':'see if it works',
            }
    rowid = small_db.add(cat0)
    cats1 = small_db.select_all()

    small_db.delete(rowid)
    cats2 = small_db.select_all()

    assert len(cats0)==len(cats2)
    assert len(cats2) == len(cats1)-1  

@pytest.mark.showdb
def test_showdb():
    ''' teting the to_trans_dict function '''
    a = to_trans_dict(('testItem',1,'testCategory',20220318,'testDesc'))
    assert a['item']=='testItem'
    assert a['amount']==1
    assert a['category']=='testCategory'
    assert a['date']==20220318
    assert a['description']=='testDesc'

#Jing Cheng
@pytest.mark.summarize_by_month_cat
def test_summarize_by_month_cat(small_db):
    ''' teting the summarize_by_month_cat function '''
    ans = small_db.summarize_by_month_cat(3, 'food')
    assert len(ans) == 2

#Jing Cheng
@pytest.mark.summarize_by_month
def test_summarize_by_month(small_db):
    ''' teting the summarize_by_month_cat function '''
    ans = small_db.summarize_by_month(3)
    assert len(ans) == 3

#Jing Cheng
@pytest.mark.summarize_by_category
def test_summarize_by_category(small_db):
    ''' teting the summarize_by_month_cat function '''
    ans = small_db.summarize_by_category('food')
    assert len(ans) == 2
    

#Lu Hao
@pytest.mark.summarize_by_amount
def test_summarize_by_category(small_db):
    ''' teting the summarize_by_amount function '''
    ans = small_db.summarize_by_amount('1')
    assert len(ans) == 3
    
#Lu Hao
@pytest.mark.check_item
def test_check_item(small_db):
    ''' teting the summarize_by_amount function '''
    ans = small_db.check_item('apple')
    assert len(ans) == 1