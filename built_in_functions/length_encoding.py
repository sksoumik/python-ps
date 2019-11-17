from collections import OrderedDict


def length_encoding(input_data):
    dic = OrderedDict.fromkeys(input_data, 0)

    for ch in input_data:
        dic[ch] += 1
    output = ''
    for key, values in dic.items():
        output = output + key + str(values)
    return output


if __name__ == '__main__':
    input_sample = 'wwwAAWWxx'
    print("Input: {} ".format(input_sample))
    print("Output: {}".format(length_encoding(input_sample)))
