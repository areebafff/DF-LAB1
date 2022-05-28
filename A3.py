import argparse 
import re
import os.path   

def check_dir(file, regex):
    if(os.path.isdir(file) == True):
		directory = (os.listdir(file))
		for directories in directory:
			if(regex.search(file)):
				print("File Found, Named = ", file)
                result=re.match(file,regex)
			file += "/" + directories
			check_dir(file, regex)
                return result


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument('-f', help = 'argument for file')
    parser.add_argument('-r', help = 'argument for regex')
    args = parser.parse_args()
    check_dir(args.f, re.compile(args.r))
    print(check_dir(args.f, re.compile(args.r)))
