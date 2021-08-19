import sys
import getopt


def find_key(line,target):
    if target in line:
        return True
    else:
        return False

def change_value(key, target):

    with open('.env', 'r') as file:
        data = file.readlines()
    
    #find that line
    line = -1
    for i in range(len(data)):
        if find_key(data[i],key):
            line = i
    if line != -1:
        data[line] = key + '=' + target + '\n'
    
    #write to file
    with open('.env', 'w') as file:
        file.writelines(data)

    print("Changed value of " + key + " to " + target)

def change_key(old, target):

    with open('.env', 'r') as file :
        data = file.readlines()

    #find that line
    line = -1
    for i in range(len(data)):
        if find_key(data[i], old):
            line = i
    if line != -1:
        data[line] = data[line].replace(old, target, 1)

    #write to file
    with open('.env', 'w') as file:
        file.writelines(data)

    print("Changed key " + old + " into " + target)



def main(argv):

    print ('Argument List:', str(sys.argv))

    # get the arguments
    try:
        opts, args = getopt.getopt(argv,"f:k:v:",["filepath=","key=","value="])
    except getopt.GetoptError:
        print ('change-env.py -f <new_path> -k <old_key> <new_key> -v <target_key> <new_value>')
        sys.exit(2)

    # put the arguments into the variable
    #print(opts)
    #print(args)

    for opt, arg in opts:         
        if opt == '-f':
            print()
            # change path

        if opt in ("-k", "--key"):
            change_key(arg, args[0])

        if opt in ("-v", "--value"):
            change_value(arg, args[0])

if __name__ == "__main__":
    main(sys.argv[1:])

