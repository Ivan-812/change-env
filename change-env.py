import sys
import getopt


def find_key(line,target):
    if target in line and target[0] == line[0]:
        return True
    else:
        return False

def find_line(key, data):
    for i in range(len(data)):
        if find_key(data[i], key):
            return i
    return -1

def change_value(key, target, path='.env'):

    with open(path, 'r') as file:
        data = file.readlines()
    
    #find that line
    line = find_line(key, data)
    if line != -1:
        if line != len(data)-1:
            data[line] = key + '=' + target + '\n'
        else:
            data[line] = key + '=' + target
    
    #write to file
    with open(path, 'w') as file:
        file.writelines(data)

    file.close()
    print("Changed value of " + key + " to " + target)

def change_key(old, target, path='.env'):

    with open(path, 'r') as file :
        data = file.readlines()

    #find that line
    line = find_line(old, data)
    if line != -1:
        data[line] = data[line].replace(old, target, 1)

    #write to file
    with open(path, 'w') as file:
        file.writelines(data)

    file.close()
    print("Changed key " + old + " into " + target)

def append(line, path='.env'):
    file = open(path, "a")
    file.write("\n" + line)

    file.close()

def delete(key, path='.env'):
    with open(path, 'r') as file :
        data = file.readlines()

    #ignore that line and write
    line = find_line(key, data)
    if line != -1:
        with open(path, 'w') as file:
            for i in range(len(data)):
                if i != line:
                    file.write(data[i])
                

    file.close()


def main(argv):

    filepath = ".env"

    # get the arguments
    try:
        opts, args = getopt.getopt(argv,"f:k:v:a:d:",["filepath=","key=","value=","add=","delete="])
    except getopt.GetoptError:
        print ('change-env.py -f <new_path> -k <old_key>,<new_key> -v <target_key>,<new_value> -a <new_field> -d <target_key>')
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
        elif opt in ("-a", "--add"):
            append(arg, filepath)
        elif opt in ("-d", "delete"):
            argumnets = arg.split(',')
            delete(arg, filepath)


if __name__ == "__main__":
    main(sys.argv[1:])

