#--------------------------------------------------------------
#
# marks new media file renaming program
# filenames2.py
#
#	Needs to remove extra dots (and double dots)
#	replace lowercase with uppercase first letter
#	possibly, to remove certain strings - like 720 HD 
#	
#	To remove special characters - []()@#$%^&! etc.
#	How to remove double dots?
#
#
#      write filelist before and after
#
#
#
#
#--------------------------------------------------------------


import os
import os.path
import sys

# import subprocess

# would use this if we did nolt already have a directory
# 	mkdir /media/NASDrive
# might need this to assign nas to drive works at OS level
# 	mount -t cifs -o user=admin,password=Bulkd1sh //192.168.1.102/multimedia/Video/Sci-Fi /media/NASDrive



#finish
def finish(sometext, fo2):                  
   fo2.write(sometext+chr(13))
   fo2.close()
   quit()	

def wfiles(filelist,fo,dp):
   for fn in filelist:
       fo.write(dp+'/'+fn+chr(13))

# write filelist
def writefilelist(filob,filepath):
   file_path = ''
   fn = ''   
   try:
      for (dirpath, dirnames, filenames) in os.walk(filepath, topdown=True, onerror=None, followlinks=False):
        wfiles(filenames,filob,dirpath)
   except:
      e = sys.exc_info()[0]
      finish(str(e),filob)

def replow(fns,dp,filob,fc):
   for filename in fns:
      fextn = os.path.splitext(filename)[1].split('.')[1]
      print(fextn)
      new_filename = ''
      # check for lowercase first character & correct
      if (filename[0].islower()):
         print('is lower')
         if (fextn in ['avi','mkv','ts','mp4','vob','m4v','mpg']):
            print('extn')
            fc += 1		
            new_filename = filename[0].upper()+filename[1:]
            print(new_filename)
         # when we are sure
#            os.rename(dp+'/'+filename, dp+'/'+new_filename)
            print(str(fc)+'   ' +new_filename)
            filob.write(str(fc)+': ' +new_filename+chr(13))
   return fc
#--------------------------------------------------------------
# Processes
# first pass replaces lowercase ist character with upercase
def lowerreplace(fo,filepath):
   file_counter = 0
   try:
      for (dirpath, dirnames, filenames) in os.walk(filepath):
         print(str(file_counter))
         file_counter = replow(filenames,dirpath,fo,file_counter)
      if file_counter == 0:
         print('No lowercase first letters to change!')
   except:
      e = sys.exc_info()[0]
      finish(str(e),fo)


# second pass replaces any double dots and other special characters
def chrsreplace(fo,filepath):
   file_counter = 0
   replace = 0
   new_filename = ''
   file_path = ''   

   try:
      for (dirpath, dirnames, filenames) in os.walk(filepath):
         for directory in dirnames:
            for filename in filenames:
               new_filename = filename[0:]
               file_path = dirpath+'/'
               # check for double dots
               if ".." in filename:
                   new_filename = new_filename.replace("..", ".")
                   replace = replace + 1;
               if " ." in filename:
                   new_filename = new_filename.replace(" .", ".")
                   replace = replace + 1;
               if "(" in filename:
                   new_filename = new_filename.replace("(", " ")
                   replace = replace + 1;
               if ")" in filename:
                   new_filename = new_filename.replace(")", " ")
                   replace = replace + 1;
               if "[" in filename:
                   new_filename = new_filename.replace("[", " ")
                   replace = replace + 1;
               if "]" in filename:
                   new_filename = new_filename.replace("]", " ")
                   replace = replace + 1;
               if "}" in filename:
                   new_filename = new_filename.replace("}", " ")
                   replace = replace + 1;
               if "{" in filename:
                   new_filename = new_filename.replace("{", " ")
                   replace = replace + 1;
               if "%" in filename:
                   new_filename = new_filename.replace("%", " ")
                   replace = replace + 1;
               if "@" in filename:
                   new_filename = new_filename.replace("@", " ")
                   replace = replace + 1;
               if "#" in filename:
                   new_filename = new_filename.replace("#", " ")
                   replace = replace + 1;
               if "$" in filename:
                   new_filename = new_filename.replace("$", " ")
                   replace = replace + 1;
               if "^" in filename:
                   new_filename = new_filename.replace("^", " ")
                   replace = replace + 1;
               if "&" in filename:
                   new_filename = new_filename.replace("&", " ")
                   replace = replace + 1;
               if "*" in filename:
                   new_filename = new_filename.replace("*", " ")
                   replace = replace + 1;
               if "_" in filename:
                   new_filename = new_filename.replace("_", " ")
                   replace = replace + 1;
               if "-" in filename:
                   new_filename = new_filename.replace("-", " ")
                   replace = replace + 1;
               # replace double spaces with single
               if "  " in filename:
                   new_filename = new_filename.replace("  ", " ")
                   replace = replace + 1;

               if replace > 0: 
                  file_counter = file_counter + 1		
                  print('Before: '+file_path+filename)
                  print('After:  '+file_path+new_filename)
                  raw_input('Hit Enter Key to process')
                  os.rename(file_path+filename, file_path+new_filename)
                  fo.write(str(file_counter)+ ' ' + str(replace) +' : ' + new_filename+chr(13))
                  replace = 0

      if file_counter == 0:
         print('No specoial characters to change!')

   except:
      e = sys.exc_info()[0]
      finish(str(e),fo)


def dotsreplace(fo,filepath):
   # code to replace filenames split with dots
   filecounter = 0
   files_with_dots = 0
   split_file = []
   new_filename = ''
   file_path = ''   

   try:
      for (dirpath, dirnames, filenames) in os.walk(filepath):
         for directory in dirnames:
            for filename in filenames:
               new_filename = ''
               file_path = dirpath+'/'
               split_file = os.path.splitext(filename)[0].split('.')
               if len(split_file) > 1:
                  files_with_dots = files_with_dots + 1		
                  for element in split_file:
                     new_filename = new_filename + element + ' '
                  # remove last space and add extension
                  new_filename = new_filename[:(len(new_filename)-1)]+'.'+os.path.splitext(filename)[1].split('.')[1]
                  if raw_input('Hit y, to rename DOTS, return key to continue.  ') == 'y':
                     print('Before: '+filename)
                     print('After:  '+new_filename)
                     raw_input('Hit Enter Key to process')
                     # rename oldfilename with new_filename
                     os.rename(file_path+filename, file_path+new_filename)
                     fo.write(str(file_counter)+': ' + new_filename+chr(13))
      if files_with_dots == 0:
         print('No files with dots to change!')
   except:
      e = sys.exc_info()[0]
      finish(str(e),fo)



def main(argv):
   
   #--------------------------------------------------------------
   # Declare Program Variables
  
   # strings
   output_file_name = "MJFFileRename.log"
   fp = r'/media/NASDrive'

   #objects
   fileobject = open(output_file_name,"w")

   # My code here
   print ('This procedure trawls media files to remove some naming conventions') 
   print(fp + '  1')
   fileobject.write('Start'+chr(13))
   writefilelist(fileobject,fp)

   print(fp + '  2')
   fileobject.write('Start Lowercase'+chr(13))
   lowerreplace(fileobject,fp)

   if raw_input('Lowercase check complete, Hit x to Finish, Enter to continue.  ') == 'x':
      finish('Lowercase check complete',fileobject)

   # temp stop here
   quit()	

    
   fileobject.write('Start Special Characters'+chr(13))
   chrsreplace(fileobject,fp)

   if raw_input('Character check complete, Hit x to Finish, Enter to continue.  ') == 'x':
      finish('Character check complete',fileobject)

   fileobject.write('Start Dots'+chr(13))
   dotsreplace(fileobject,fp)

   if raw_input('Dots check complete, Hit x to Finish, Enter to continue.  ') == 'x':
      finish('Dots check complete',fileobject)

   fileobject.write('Final File Check'+chr(13))
   writefilelist(fileobject,fp)

   pass

if __name__ == "__main__":
    main(sys.argv)



      








#			extension = os.path.splitext(filename)[1].split('.')
# 			print(extension)
#			if extension[1] not in extension_list :
#				# put second element into array
#				extension_list.append(extension[1]) 
#				print("Hit a key.")
#				raw_input()




