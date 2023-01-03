
def sortList():
    """sorts lists"""

    items = [5, 1, 3, 2, 4]
    items.sort()
    print(items)  # [1, 2, 3, 4, 5]

    items = ['xx', 'xxx', 'xxxxx', 'xxxx']
    sorted_items = sorted(items, key=len)
    print(sorted_items)  # ['xx', 'xxx', 'xxxx', 'xxxx']

    items = [5, 1, 3, 2, 4]
    sorted_items = sorted(items, reverse=True)
    print(sorted_items)  # [5, 4, 3, 2, 1]

sortList()