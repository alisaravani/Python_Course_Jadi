import hashlib
import csv

def hash_password_hack(input_file_name, output_file_name):

    with open(input_file_name,'r') as fin:
        reader=csv.reader(fin)
        listName=[]
        listHash=[]
        listDB=[]
        listPass=[]
        counter=0
        
        for row in reader:
            listName.append(row[0])
            listHash.append(row[1])

        for i in range(0000,9999+1):
            hash=hashlib.sha256(str(i).encode())
            listDB.append(hash.hexdigest())
        
        while counter<len(listHash):
            if listHash[counter] in listDB:
                listPass.append(listDB.index(listHash[counter]))
                counter+=1


    with open(output_file_name,'w') as writeFile:
        writer=csv.writer(writeFile)
        for writerow in range(len(listName)):
            writer.writerow([listName[writerow],listPass[writerow]])
    
    fin.close()
    writeFile.close()
