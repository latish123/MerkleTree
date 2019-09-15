import hashlib
import xlwt 
from xlwt import Workbook  

hasher = hashlib.md5()
with open('verify.txt', 'rb') as afile:
    buf = afile.read()
    hasher.update(buf)
hasher1 = hashlib.md5()
with open('verify1.txt', 'rb') as afile:
    buf1 = afile.read()
    hasher1.update(buf1)
hasher2 = hashlib.md5()
with open('verify2.txt', 'rb') as afile:
    buf2 = afile.read()
    hasher2.update(buf2)
hasher3 = hashlib.md5()
with open('verify3.txt', 'rb') as afile:
    buf3 = afile.read()
    hasher3.update(buf3)



  
  
# Workbook is created 
wb = Workbook() 
  
# add_sheet is used to create sheet. 
sheet1 = wb.add_sheet('Sheet 1')

  

sheet1.write(1,0,hasher.hexdigest())
sheet1.write(2,0,hasher1.hexdigest())
sheet1.write(3,0,hasher2.hexdigest())
sheet1.write(4,0,hasher3.hexdigest())
  
wb.save('latish.csv') 
