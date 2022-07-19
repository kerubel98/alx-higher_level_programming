#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    resalt = []
    while i < list_length:
        resf = 0
        try:
            resf = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        finally:
            resalt.append(resf)
            i += 1
    return resalt
