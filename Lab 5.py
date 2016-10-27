import os

extensionsToCheck = ['.txt']#Checks if extension is .txt
dict1 = {}; frontier = []; words = []#For storing file words

for folderName, subfolders, filenames in os.walk('C:\\'): #Walking entire directory from C
    dir1 = folderName[-1] 
    if not dict1.has_key(dir1):
        dict1.update({dir1:[]});
        dict1[dir1].append(folderName);
    else:
        dict1[dir1].append(folderName);
    for subfolder in subfolders:
        if not dict1.has_key(subfolder):
            dict1.update({subfolder:[]});
            dict1[subfolder].append(folderName);
        else:
            dict1[subfolder].append(folderName);
    for filename in filenames: #Transeversing files
        if not dict1.has_key(filename): #If not key, create new dictionary entry
                dict1.update({filename:[]});
                dict1[filename].append(folderName);
        if any(ext in filename for ext in extensionsToCheck):#Else don't, if name has a valid extension
          if os.path.isfile(folderName+'\\'+filename) and "$" not in filename:  
              with open(folderName+'\\'+filename) as f:
                   words = f.read().split()
              for wor in words:
                    if not dict1.has_key(wor):
                       dict1.update({wor:[]});
                       dict1[wor].append(folderName + '\\' + filename);#Appending entire path
                    else:
                       dict1[wor].append(folderName + '\\' + filename);
while(1):
    var = raw_input("Please enter something you wish to search: ");#Taking user input
    if not dict1.has_key(var):
        print "Could not find file!\n";
    else:
        print dict1[var];#prints dict1 directory for that file

              
                
