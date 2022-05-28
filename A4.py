import argparse 
import re
import os.path   

def check_dir(file, regex):
    if(os.path.exists(file) == True):
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
    parser.add_argument('file', help = 'argument for file')
    parser.add_argument('regex', help = 'argument for regex')
    args = parser.parse_args()
    print(check_dir(args.file, re.compile(args.regex)))
