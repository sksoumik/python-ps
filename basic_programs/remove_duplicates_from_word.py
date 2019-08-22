from collections import OrderedDict


def remove_duplicate_without_order(str):
    return "".join(set(str))


def remove_duplicate_with_order(str):
    return "".join(OrderedDict.fromkeys(str))


# Driver program
if __name__ == "__main__":
    str = "pythonjavacppjs"
    print(remove_duplicate_without_order(str))
    print(remove_duplicate_with_order(str))
