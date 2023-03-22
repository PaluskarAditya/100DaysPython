import os

def clear(path, format):
    j = 1

    os.chdir(path)
    print(f"current directory: {os.getcwd()}")

    for i in os.listdir():
        if i.endswith(format):
            os.rename(i, str(j)+format)
            j += 1
        else:
            print("File not found")
            break
            
    all_files = os.listdir(path)
    for file in all_files:
        print(file)        

path = '..//temp'
clear(path, '.txt')
