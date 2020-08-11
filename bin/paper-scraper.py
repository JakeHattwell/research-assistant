#!/usr/bin/env python

import PyPDF2
import os
import warnings

__author__ = "Jake Hattwell"
__copyright__ = "Copyright 2020"
__credits__ = ["Jake Hattwell","Luke Husdell"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Jake Hattwell"
__email__ = "j.hattwell@uq.edu.au"
__status__ = "Production"

CHAR_LIMIT = 64
FORBIDDEN = ['\\','/',':','*','?','"','<','>','|']

if __name__ == '__main__':
	print("=============")
	print("PAPER SCRAPER")
	print("=============")
	print("This utility will attempt to rename all PDFs in a target directory into the format FirstAuthorSurname_Year_Title.")
	print("Depending on the journal, the author field of the PDF usually contains the first or last author.")
	print("I strongly recommended that you back up all files before renaming, as occasionally the results will be worse than the original filename.")
	print("""Due to operating system restrictions, Paper Scraper automatically truncates filenames to 64 characters, including the .pdf extension. 
	In some folder structures, this may be too long. Truncation length can be edited by changing the CHAR_LIMIT parameter at the start of this script.""")
	print("As part of the renaming process, a file called ___renamed_paper_log.log is created. Keep this file to make future renames faster.")
	print("If you manually rename files, add the new filename to the end of the ___renamed_paper_log.log file")
	print("=============")
	directory = input("Please enter the path to the directory, or hit enter to select this directory: ")
	if directory == "":
		directory = os.getcwd()
	if os.path.isdir(directory) == False:
		input("Directory not found. Press return/enter to exit.")
		exit()
	os.chdir(directory)
	change_count = 0

	#check if log exists
	if os.path.isfile("___renamed_paper_log.log"):
		with open("___renamed_paper_log.log","r") as log_file:
			preread = log_file.read()
	else:
		preread = ""

	#stats
	to_change = sum([1 for paper in os.listdir(os.getcwd()) if ".pdf" in paper.lower() and paper not in preread])
	already_changed = sum([1 for paper in os.listdir(os.getcwd()) if ".pdf" in paper.lower() and paper in preread])
	total = to_change+already_changed
	print()
	print(total,"pdfs found")
	print(already_changed,"files already renamed,",to_change,"files to be renamed.")

	#exit if no new files
	if to_change == 0:
		input("No new files to rename. Press return/enter to exit.")
		exit()

	#confirm rename
	action = input('This renaming is irreversible. Would you like to continue [Y/N]: ')
	print()
	if action.upper() == "Y":
		converted = []
		#open log
		with open("___renamed_paper_log.log","a+") as log_file:
			for f in os.listdir(os.getcwd()):
				if ".pdf" in f.lower() and f not in preread:
					try:
						#open the file and read the metadata
						warnings.filterwarnings("ignore") #block pdf reading warnings
						reader = PyPDF2.PdfFileReader(f)
						warnings.filterwarnings("default") #reenable warnings
						title = reader.documentInfo["/Title"]
						date = reader.documentInfo["/CreationDate"]
						author = reader.documentInfo.get("/Author","")
						#process author information
						author = author.split(",")[0]
						for bad in FORBIDDEN:
							author = author.replace(bad, " ")
							title = title.replace(bad, " ")
						author = author.rstrip().split(" ")[-1].title()
						#join author, date, and title
						name = author+"_"+date[2:6]+"_"+title
						name = "_".join(name.split())
						#truncate and attach pdf extension
						if len(name) > CHAR_LIMIT:
							name = name[:CHAR_LIMIT-4]
						name+=".pdf"
						if name in preread or name in converted:
							print(f,"is a duplicate of",name+". Tagged with '__DUPE_' and skipped.")
							name = "__DUPE_"+f
							os.rename(f,name)
							log_file.write(name+"\n")
							converted.append(name)
						else:
							#renaming
							try:
								os.rename(f,name)
								change_count += 1
							except OSError:
								name = "__"+f
								os.rename(f,name)
							log_file.write(name+"\n")
							converted.append(name)
					except:
						#if any metadata was unreadable, rename and skip
						name = "__"+f
						os.rename(f,name)
						log_file.write(name+"\n")
		print()
		print("Complete!",change_count,"files were renamed.\nA single underscore denotes files where authorship could not be determined.\nA leading double underscore denotes any files which were duplicates, unreadable, or contained no metadata.")
		input("Press return/enter to exit.")
		exit()
	else:
		#if no confirmation
		input("Confirmation not received. Aborting renaming process. Press return/enter to exit.")
		exit()