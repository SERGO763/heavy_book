import weakref
class MyList(list):
    """Подкласс list, на экземпляр которого можно создать слабую ссылку"""

a_list = MyList(range(10))
wref_to_a_list = weakref.ref(a_list)