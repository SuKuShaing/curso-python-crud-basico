import random


def binary_search(data, target, low, high):

    print('')
    print('*' * 50)

    iterador = low
    while iterador < high:
        print(data[iterador], end=' ')
        iterador += 1

    if low > high:
        return False

    mid = (low + high) // 2

    if target == data[mid]:
        return True
    elif target < data[mid]:
        return binary_search(data, target, low, mid - 1)
    else:
        return binary_search(data, target, mid + 1, high)


if __name__ == '__main__':
    data = [random.randint(0, 100) for i in range(30)]

    data.sort() # este método modifica la lista original
    # sorted_data = sorted(data) # este método no modifica la lista original, crea otra

    print(data)

    target = int(input('What number would you like to find?: '))
    found = binary_search(data, target, 0, len(data) - 1)

    print(found)
