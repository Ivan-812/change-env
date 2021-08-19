import sys
import getopt


def find_key(line,target):
    if target in line:
        return True
    else:
        return False

def change_value(key, target, path='.env'):

    with open(path, 'r') as file:
        data = file.readlines()
    
    #find that line
    line = -1
    for i in range(len(data)):
        if find_key(data[i],key):
            line = i
    if line != -1:
        data[line] = key + '=' + target + '\n'
    
    #write to file
    with open(path, 'w') as file:
        file.writelines(data)

    file.close()
    print("Changed value of " + key + " to " + target)

def change_key(old, target, path='.env'):

    with open(path, 'r') as file :
        data = file.readlines()

    #find that line
    line = -1
    for i in range(len(data)):
        if find_key(data[i], old):
            line = i
    if line != -1:
        data[line] = data[line].replace(old, target, 1)

    #write to file
    with open(path, 'w') as file:
        file.writelines(data)

    file.close()
    print("Changed key " + old + " into " + target)


def main(argv):

    filepath = ".env"

    # get the arguments
    try:
        opts, args = getopt.getopt(argv,"f:k:v:",["filepath=","key=","value="])
    except getopt.GetoptError:
        print ('change-env.py -f <new_path> -k <old_key>,<new_key> -v <target_key>,<new_value>')
        sys.exit(2)

    # put the arguments into the variable
    for opt, arg in opts:         
        if opt == '-f':
            filepath = arg
        elif opt in ("-k", "--key"):
            argumnets = arg.split(',')
            change_key(argumnets[0], argumnets[1], filepath)
        elif opt in ("-v", "--value"):
            argumnets = arg.split(',')
            change_value(argumnets[0], argumnets[1], filepath)


if __name__ == "__main__":
    main(sys.argv[1:])

