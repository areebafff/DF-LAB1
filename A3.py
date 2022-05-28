#assignment 3
import argparse 
import os   
import yara

def dir_search(file, rule):
    if(os.path.isdir(file)):
		    directory = os.listdir(file)
		    for directories in directory:
			    dir_search(file+"/"+directories, rule)
	else:
		    if(rule.match(file)):
		        print("Rule Matched = "+ file)


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('path',help='target')
    parser.add_argument('-r',help='yara rules defined')
    arg = parser.parse_args()
    direc = arg.path
    rules=yara.compile(filepath=arg.r)
    if(os.isfile(direc)):
        print("enter directory name")
    else:    
        search(direc, rules)
