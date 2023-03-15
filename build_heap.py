# python3
import math

swaps_vals = []


def build_heap(data):
    swaps = []
    n = len(data)

    for i in range(n, (math.floor(n / 2) + 1), -1):

        root_reached = 0

        if n % 2 == 1:
            right_child_index = left_child_index = i - 1
        else:
            right_child_index = i - 1
            left_child_index = i - 2

        left_child = data[left_child_index]
        right_child = data[right_child_index]

        if right_child < left_child:
            target_index = right_child_index
        else:
            target_index = left_child_index

        parent_index = math.ceil(target_index / 2 - 1)

        while root_reached != 1:
            target = data[target_index]
            parent = data[parent_index]

            if parent_index == 0:
                root_reached = 1

            if parent > target:
                swaps.append([parent_index, target_index])
                swaps_vals.append([parent, target])
                data[target_index], data[parent_index] = parent, target
                target_index = parent_index
                parent_index = math.ceil(target_index / 2 - 1)
            else:
                break

    # try to achieve  O(n) and not O(n2)

    return swaps


def main():
    # add another input for I or F
    # first two tests are from keyboard, third test is from a file
    text = input()
    # text = "F"  # Test line
    if "F" in text:
        file_name = input()

        file = open("./tests/" + file_name, "r")
        # file = open("./tests/" + "04", "r")  # Test line
        text = file.read()

        text = text.split('\n')
        n = int(text[0])
        data = list(map(int, text[1].split()))

    elif "I" in text:
        # # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # this number should be less than 4n (less than 4*len(data))

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)
    # print("----")
    # for i, j in swaps_vals:
    #     print(i, j)


if __name__ == "__main__":
    main()
