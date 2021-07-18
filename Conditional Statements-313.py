## 1. If Statements ##

# INITIAL CODE
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

free_apps_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    
    price = float(row[4])
    if price == 0.0:
        free_apps_ratings.append(rating)
        
avg_rating_free = sum(free_apps_ratings)/len(free_apps_ratings)        

#Output:
###
3.3767258382642997
###
        
        

## 2. Booleans ##

a_price = 0
if a_price == 0:
    print("This is free")

if a_price == 1:
    print("This is not free")

#Output:
###
This is free    
###    

## 3. The Average Rating of Non-free Apps ##

# INITIAL CODE
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

non_free_apps_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])   
    if price != 0.0:
        non_free_apps_ratings.append(rating)
    
avg_rating_non_free = sum(non_free_apps_ratings) / len(non_free_apps_ratings)

#Output:
###
3.720948742438714
###

## 4. The Average Rating of Gaming Apps ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

non_games_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]
    
    if genre != 'Games':
        non_games_ratings.append(rating)
 
avg_rating_non_games = sum(non_games_ratings) / len(non_games_ratings)
print(avg_rating_non_games)
    
#Output:
###
3.343928035982009
###

## 5. Multiple Conditions ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

free_games_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])
    genre = row[11]
    # Complete code from here
    if price == 0.0 and genre == 'Games':
        free_games_ratings.append(rating)
        
avg_rating_free_games = sum(free_games_ratings)/len(free_games_ratings)
print(avg_rating_free_games)

#Output:
###
3.5285777580859548
###

## 6. The or Operator ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

games_social_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]
    # Complete code from here
    if genre == 'Social Networking' or genre == 'Games':
        games_social_ratings.append(rating)
        
avg_games_social = sum(games_social_ratings) / len(games_social_ratings)
print(avg_games_social)

#Output:
###
3.655994043186895
###
        

## 7. Combining Logical Operators ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

nonfree_games_social_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]
    price = float(row[4])
    
    if (genre == 'Social Networking' or genre == 'Games') and price != 0:
        nonfree_games_social_ratings.append(rating)
        
avg_non_free = sum(nonfree_games_social_ratings) / len(nonfree_games_social_ratings)

# Non-free apps (average)
print(avg_non_free)

#Output:
###
3.8904235727440146
###

## 8. Comparison Operators ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])
    
    if price > 9:
        ratings.append(rating)

avg_rating = sum(ratings)/len(ratings)
n_apps_more_9 = len(ratings)
n_apps_less_9 = len(apps_data[1:]) - len(ratings)

#Output:
###
7019
###

## 9. The else Clause ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

for app in apps_data[1:]:
    price = float(app[4])
    # Complete code from here
    if price == 0.0:
        app.append('free')
    else:
        app.append('non-free')
        
apps_data[0].append('free_or_not')
print(apps_data[:6])

#Output:
###
[['id', 'track_name', 'size_bytes', 'currency', 'price', 'rating_count_tot', 'rating_count_ver', 'user_rating', 'user_rating_ver', 'ver', 'cont_rating', 'prime_genre', 'sup_devices.num', 'ipadSc_urls.num', 'lang.num', 'vpp_lic', 'free_or_not'], ['284882215', 'Facebook', '389879808', 'USD', '0.0', '2974676', '212', '3.5', '3.5', '95.0', '4+', 'Social Networking', '37', '1', '29', '1', 'free'], ['389801252', 'Instagram', '113954816', 'USD', '0.0', '2161558', '1289', '4.5', '4.0', '10.23', '12+', 'Photo & Video', '37', '0', '29', '1', 'free'], ['529479190', 'Clash of Clans', '116476928', 'USD', '0.0', '2130805', '579', '4.5', '4.5', '9.24.12', '9+', 'Games', '38', '5', '18', '1', 'free'], ['420009108', 'Temple Run', '65921024', 'USD', '0.0', '1724546', '3842', '4.5', '4.0', '1.6.2', '9+', 'Games', '40', '5', '1', '1', 'free'], ['284035177', 'Pandora - Music & Radio', '130242560', 'USD', '0.0', '1126879', '3594', '4.0', '4.5', '8.4.1', '12+', 'Music', '37', '4', '1', '1', 'free']]
###

## 10. The elif Clause ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

for app in apps_data[1:]:
    price = float(app[4])
    # Complete code from here
    if price == 0:
        app.append('free')

    elif price > 0 and price < 20:
        app.append('affordable')
        
    elif price >= 20 and price < 50:
        app.append('expensive')
        
    elif price >= 50:
        app.append('very expensive')

apps_data[0].append('price_label')
print(apps_data[:6])

#Output:
###
['id', 'track_name', 'size_bytes', 'currency', 'price', 'rating_count_tot', 'rating_count_ver', 'user_rating', 'user_rating_ver', 'ver', 'cont_rating', 'prime_genre', 'sup_devices.num', 'ipadSc_urls.num', 'lang.num', 'vpp_lic', 'price_label'], ['284882215', 'Facebook', '389879808', 'USD', '0.0', '2974676', '212', '3.5', '3.5', '95.0', '4+', 'Social Networking', '37', '1', '29', '1', 'free'], ['389801252', 'Instagram', '113954816', 'USD', '0.0', '2161558', '1289', '4.5', '4.0', '10.23', '12+', 'Photo & Video', '37', '0', '29', '1', 'free'], ['529479190', 'Clash of Clans', '116476928', 'USD', '0.0', '2130805', '579', '4.5', '4.5', '9.24.12', '9+', 'Games', '38', '5', '18', '1', 'free'], ['420009108', 'Temple Run', '65921024', 'USD', '0.0', '1724546', '3842', '4.5', '4.0', '1.6.2', '9+', 'Games', '40', '5', '1', '1', 'free'], ['284035177', 'Pandora - Music & Radio', '130242560', 'USD', '0.0', '1126879', '3594', '4.0', '4.5', '8.4.1', '12+', 'Music', '37', '4', '1', '1', 'free']]
###
