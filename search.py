#Import os module 
import os 

# Ask the user to enter string to search
path = input("Enter directory path to search : ") 
extension_input = input("Enter the extension of the file type you'll like to narrow the search to (e.g. html, txt, py.). If you want to cover all file extensions, just ignore this prompt and hit the ENTER key. ")
file_type = "." + extension_input
search_str = input("Enter the search string : ")

# Append a directory separator if not already present
if not (path.endswith("/") or path.endswith("\\") ):
	path = path + "/"

# If path does not exist, set search path to current directory 
if not os.path.exists(path):
	path ="." 

# Repeat for each file in the directory
for root, directories, files in os.walk(path, topdown=True):
	for fname in files:
		# Apply file type filter
		if (file_type=="." or fname.endswith(file_type)):
			# Open file for reading
			fo = open(path + fname)
			
			# Read the first line from the file
			line = fo.readline()
			
			# Initialize counter for line number
			line_no = 1
		
			# Loop until EOF
			while line != '' :
				# Search for string in line
				index = line.find(search_str)
				if ( index != -1) :
					print(os.path.join(root, fname), "[", line_no, ",", index, "] ", line, sep="")
			
				# Read next line
				line = fo.readline()
			
				# Increment line counter
				line_no += 1
			# Close the files
			fo.close()