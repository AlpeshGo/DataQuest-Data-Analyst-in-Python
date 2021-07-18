## 1. Functions ##

a_list = [4444, 8897, 6340, 9896, 4835, 4324, 10, 6445,
          661, 1246, 1000, 7429, 1376, 8121, 647, 1280,
          3993, 4881, 9500, 6701, 1199, 6251, 4432, 37]
sum_manual = 0
for element in a_list:
    sum_manual += element
    
print(sum_manual)
print(sum(a_list))

#Output:
###
103945
103945
###

## 2. Built-in Functions ##

ratings = ['4+', '4+', '4+', '9+', '12+', '12+', '17+', '17+']

content_ratings = {}

for rating in ratings:
    if rating in content_ratings:
        content_ratings[rating] += 1
        
    else:
        content_ratings[rating] = 1
        
print(content_ratings)        
    
#Output:
###
{'4+': 3, '9+': 1, '12+': 2, '17+': 2}
###
    

## 3. Creating Our Own Functions ##

def square(a_number):
    squared_number = a_number * a_number
    return squared_number

squared_10 = square(a_number = 10)
squared_16 = square(a_number = 16)

#Output:
###
100
256
###

## 4. The Structure of a Function ##

def add_10(number):
    addition = number + 10
    return addition

add_30 = add_10(number = 30)
add_90 = add_10(number = 90)

print(add_30)
print(add_90)
    
#Output:
###
40
100
###

## 5. Parameters and Arguments ##

def square(a):
    return a * a

squared_6 = square(6)
squared_11 = square(11)

#Output:
###
36
121
###

## 6. Extract Values from Any Column ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(index):
    column = []
    for row in apps_data[1:]:
        value = row[index]
        column.append(value)
        
    return column

genres = extract(11)

#Output:
###
['Social Networking', 'Photo & Video', 'Games', 'Games', 'Music', 'Social Networking', 'Reference', 'Games', 'Music', 'Games', 'Games', 'Games', 'Games', 'Games', 'Games', 'Games', 'Games', 'Games', 'Games', 'Games', 'Health & Fitness', 'Games', 'Weather', 'Games', 'Utilities', 'Games', 'Games', 'Travel', 'Games', 'Games', 'Shopping', 'Games', 'Games', 'Games', 'Games', 'Music', 'Games', 'Games', 'Games', 'Games', 'Games', 'Games', 'Health & Fitness', 'Social Networking', 'Games', 'Games', 'Games', 'News', 'Social Networking', 'Navigation']
###

## 7. Creating Frequency Tables ##

# CODE FROM THE PREVIOUS SCREEN
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(index):
    column = []    
    for row in apps_data[1:]:
        value = row[index]
        column.append(value)    
    return column

genres = extract(11)

def freq_table(column):
    frequency_table = {}
    for value in column:
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1
    return frequency_table

genres_ft = freq_table(genres)

#Output:
###
{'Book': 112, 'Business': 57, 'Catalogs': 10, 'Education': 453, 'Entertainment': 535, 'Finance': 104, 'Food & Drink': 63, 'Games': 3862, 'Health & Fitness': 180, 'Lifestyle': 144, 'Medical': 23, 'Music': 138, 'Navigation': 46, 'News': 75, 'Photo & Video': 349, 'Productivity': 178, 'Reference': 64, 'Shopping': 122, 'Social Networking': 167, 'Sports': 114, 'Travel': 81, 'Utilities': 248, 'Weather': 72}
###

## 8. Writing a Single Function ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def freq_table(index):
    frequency_table = {}
    
    for row in apps_data[1:]:
        value = row[index]
        if value in frequency_table:
            frequency_table[value] += 1
            
        else:
            frequency_table[value] = 1
    return frequency_table

ratings_ft = freq_table(7)
#Output:
###
{'0.0': 929, '1.0': 44, '1.5': 56, '2.0': 106, '2.5': 196, '3.0': 383, '3.5': 702, '4.0': 1626, '4.5': 2663, '5.0': 492}
###

## 9. Reusability and Multiple Parameters ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

# INITIAL FUNCTION
def freq_table(data_set, index):
    frequency_table = {}
    
    for row in apps_data[1:]:
        value = row[index]
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1
            
    return frequency_table
ratings_ft = freq_table(data_set=apps_data, index=7)

#Output:
###
{'0.0': 929, '1.0': 44, '1.5': 56, '2.0': 106, '2.5': 196, '3.0': 383, '3.5': 702, '4.0': 1626, '4.5': 2663, '5.0': 492}
###


## 10. Keyword and Positional Arguments ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def freq_table(data_set, index):
    frequency_table = {}
    
    for row in data_set[1:]:
        value = row[index]
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1
        
    return frequency_table

content_ratings_ft = freq_table(apps_data, 10)
ratings_ft = freq_table(apps_data, 7)
genres_ft = freq_table(apps_data, 11)

#Output:
###
{'12+': 1155, '17+': 622, '4+': 4433, '9+': 987}
{'0.0': 929, '1.0': 44, '1.5': 56, '2.0': 106, '2.5': 196, '3.0': 383, '3.5': 702, '4.0': 1626, '4.5': 2663, '5.0': 492}
{'Book': 112, 'Business': 57, 'Catalogs': 10, 'Education': 453, 'Entertainment': 535, 'Finance': 104, 'Food & Drink': 63, 'Games': 3862, 'Health & Fitness': 180, 'Lifestyle': 144, 'Medical': 23, 'Music': 138, 'Navigation': 46, 'News': 75, 'Photo & Video': 349, 'Productivity': 178, 'Reference': 64, 'Shopping': 122, 'Social Networking': 167, 'Sports': 114, 'Travel': 81, 'Utilities': 248, 'Weather': 72}
###


## 11. Combining Functions ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(data_set, index):
    column = []    
    for row in data_set[1:]:
        value = row[index]
        column.append(value)    
    return column

def find_sum(a_list):
    a_sum = 0
    for element in a_list:
        a_sum += float(element)
    return a_sum

def find_length(a_list):
    length = 0
    for element in a_list:
        length += 1
    return length

def mean(data_set, index):
    column = extract(data_set, index)
    return find_sum(column)/find_length(column)

avg_price = mean(apps_data, 4)

#Output:
###
1.7262178685562666
###

## 12. Debugging Functions ##

def extract(data_set, index):
    column = []
    
    for row in data_set[1:]:
        value = row[index]
        column.append(value)
    
    return column

def find_sum(a_list):
    a_sum = 0
    for element in a_list:
        a_sum += float(element)
    return a_sum

def find_length(a_list):
    length = 0
    for element in a_list:
        length += 1
    return length

def mean(data_set, index):
    column = extract(data_set, index)
    return find_sum(column) / find_length(column)

avg_price = mean(apps_data, 4)
avg_rating = mean(apps_data, 7)

#Output:
###
1.7262178685562666
3.526955675976101
###
