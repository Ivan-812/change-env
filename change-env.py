import sys
import getopt


def main(argv):

    # get the arguments
    try:
        opts, args1, args2 = getopt.getopt(argv,"f:k::v::",["key=","value="])
    except getopt.GetoptError:
        print ('change-env.py -f <new_path> -k <old_key> <new_key> -v <target_key> <new_value>')
        sys.exit(2)

    # put the arguments into the variable
    for opt, args1, args2 in opts:
        if opt == '-f':
            print()
            # change path
        if opt in ("-k", "--key"):
            change_key(args1, args2)
        elif opt in ("-v", "--value"):
            change_value(args1, args2)

if __name__ == "__main__":
    main(sys.argv[1:])



def change_key(old, target):

    with open('.env', 'r') as file :
        filedata = file.read()

    filedata = filedata.replace(old, target)

    with open('.env', 'w') as file:
        file.write(filedata)
    

def change_value(key, target):

    with open('.env', 'r') as file:
        data = file.readlines()
    
    #find that line
    for i in range(len(data)):
        if find_key(data[i],key):
            line = i
    data[line] = key + '=' + target
    
    #write to file
    with open('.env', 'w') as file:
        file.writelines(data)


def find_key(line,target):
    if target in line:
        return True
    else:
        return False