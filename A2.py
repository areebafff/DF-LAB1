
    
#assignment 2
import argparse
import os.path
import os
import filecmp
    			

def CheckDir(dir1, dir2):
    compared = filecmp.dircmp(dir1, dir2)
    if (compared.left_only or compared.right_only or compared.diff_files or compared.funny_files):
        return False
    for subdir in compared.common_dirs:
        if not CheckDir(os.path.join(dir1, subdir), os.path.join(dir2, subdir)):
            return False    
    return True
    
    
    
def CheckFile(file1, file2):
    if file1 != file2:
    	return False
    else:
    	return True
    	


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('D1')
    parser.add_argument('D2')
    args = parser.parse_args()
    Directory1 = args.D1
    Directory2 = args.D2
    if os.path.isfile(Directory1) and os.path.isfile(Directory2):
    	res = CheckFile(Directory1, Directory2)
    elif os.path.isdir(Directory1) and os.path.isdir(Directory2):
    	res = CheckDir(Directory1, Directory2)
    else:
    	if os.path.isfile(Directory1) and os.path.isdir(Directory2):
    		res=0   #both should be directories	
    		 			    	
    if (res):
        print("Match")
    else:
    	print("Mismatch")
    
