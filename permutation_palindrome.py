def main():
    mydict = {}
    my_input = raw_input('Enter input:')
    for character in my_input:
        if character in mydict:
            mydict[character] += 1
        else:
            mydict[character] = 1
    flag = 0
    for key, value in mydict.iteritems():
        if value % 2 == 1:
            if flag:
                return False
            flag += 1
    return True

if __name__ == "__main__":
    print main()
