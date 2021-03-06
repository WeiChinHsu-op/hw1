# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
total = 0
cwb_filename = 'sample_input.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      total = total+1
      data.append(row)
#total = number of data


#=======================================
# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
''' when we pop out the data, all the data will move
 toward one space, so the index become (i-j) '''
j = 0
for i in range(total):
    if data[i-j]["PRES"]=='-99.000' or data[i-j]["PRES"]=='-999.000' :
        data.pop(i-j)
        j = j+1
        total = total-1
    else:
        i=i

#initialize the sum of pressure & total number
C0A880_PRES = 0
C0F9A0_PRES = 0
C0G640_PRES = 0
C0R190_PRES = 0
C0X260_PRES = 0
C0A880_count = 0
C0F9A0_count = 0
C0G640_count = 0
C0R190_count = 0
C0X260_count = 0

# just add it up
for i in range(total):
    if data[i]["station_id"] == 'C0A880':
        C0A880_PRES = C0A880_PRES+float(data[i]["PRES"])
        C0A880_count = C0A880_count+1
    elif data[i]["station_id"] == 'C0F9A0':
        C0F9A0_PRES = C0F9A0_PRES+float(data[i]["PRES"])
        C0F9A0_count = C0F9A0_count+1
    elif data[i]["station_id"] == 'C0G640':
        C0G640_PRES = C0G640_PRES+float(data[i]["PRES"])
        C0G640_count = C0G640_count+1
    elif data[i]["station_id"] == 'C0R190':
        C0R190_PRES = C0R190_PRES+float(data[i]["PRES"])
        C0R190_count = C0R190_count+1
    elif data[i]["station_id"] == 'C0X260':
        C0X260_PRES = C0X260_PRES+float(data[i]["PRES"])
        C0X260_count = C0X260_count+1
    else:
        i=i
        
# if C0XXXX = 0 , it means all the data had been deleted
if C0A880_PRES==0:
    C0A880_mean = 'None'
else:
    C0A880_mean = C0A880_PRES/C0A880_count

if C0F9A0_PRES==0:
    C0F9A0_mean = 'None'
else:
    C0F9A0_mean = C0F9A0_PRES/C0F9A0_count
    
if C0G640_PRES==0:
    C0G640_mean = 'None'
else:
    C0G640_mean = C0G640_PRES/C0G640_count
    
if C0R190_PRES==0:
    C0R190_mean = 'None'
else:
    C0R190_mean = C0R190_PRES/C0R190_count
    
if C0X260_PRES==0:
    C0X260_mean = 'None'
else:
    C0X260_mean = C0X260_PRES/C0X260_count

#=======================================
# Part. 4
#=======================================
# Print result
C0A880 = []
C0A880.append('C0A880')
C0A880.append(C0A880_mean)

C0F9A0 = []
C0F9A0.append('C0F9A0')
C0F9A0.append(C0F9A0_mean)

C0G640 = []
C0G640.append('C0G640')
C0G640.append(C0G640_mean)

C0R190 = []
C0R190.append('C0R190')
C0R190.append(C0R190_mean)

C0X260 = []
C0X260.append('C0X260')
C0X260.append(C0X260_mean)

# Generate the desired output
Ans = []
Ans.append(C0A880)
Ans.append(C0F9A0)
Ans.append(C0G640)
Ans.append(C0R190)
Ans.append(C0X260)
print(Ans)
#========================================