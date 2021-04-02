# City Names: Write a function called city_country() that takes in the name of a city and its country. This function should
# return a string formatted like this: 'Santiago, Chile'. Call your function with at least three city-country pairs, and
# print the values that are returned.

def city_country(city, country):
    location = f'{city}, {country}'
    return location.title()

enter_location = city_country('paris', 'france')
print(enter_location)

enter_location = city_country('ushuaia', 'argentina')
print(enter_location)

enter_location = city_country('cape town', 'south africa')
print(enter_location)


# Album: Write a function called make_album() that builds a dictionary describing a music album. The function should take
# in an artist name and an album title, and it should return a dictionary containing these pieces of information. Use the 
# function to make three dictionaries representing different albums. Print each return value to show that the dictionaries
# are storing the album information correctly.

# Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. If the 
# calling line includes a value for the number of songs, add that value to the album's dictionary. Make at least one new
# function call that includes the number of songs on an album.

def make_album(artist_name, album_title, number_of_songs=None):
    album = {
        'artist': artist_name,
        'album title': album_title
    }

    if number_of_songs:
        album['album tracks'] = number_of_songs
    return album
  
    
artist_profile = make_album('beyonce', 'lemonade', 12)
print(artist_profile)

artist_profile = make_album('kendrick lamar', 'good kid maad city')
print(artist_profile)

artist_profile = make_album('city girls', 'period')
print(artist_profile)

# REMEMBER THE LAST DICTIONARY ENTRY WILL ALWAYS TAKE PRECEDENT IN A FOR LOOP

for album_features, album_info in artist_profile.items():
    if album_features == 'album tracks':
        print(f'{album_features.title()}: {album_info}')
    else:
        print(f'{album_features.title()}: {album_info.title()}')

    
# User Albums: Start with your program 'Album'. Write a while loop that allows users to enter an album's artist and title.
# Once you have that information, call make_album() with the user's input and print the dictionary that's created. Be sure
# to include a quit value in the while loop.

def make_album2(artist_name, album_title, number_of_songs=None):
    album = {
        'artist': artist_name,
        'album title': album_title
    }

    if number_of_songs:
        album['album tracks'] = number_of_songs
    return album

while True:
    print('Enter your an artist\'s name and album....Enter "quit" to exit')
    
    a_name = input('Please enter the artist... ')
    if a_name == 'quit':
      break

    a_title = input('Please enter album... ')
    if a_title == 'quit':
      break

    num_songs = input('Please enter number of songs in album... ')  
    if num_songs == 'quit':
      break

   
    artist_profile = make_album2(a_name, a_title, num_songs)

for album_features, album_info in artist_profile.items():
    if album_features == 'album tracks':
        print(f'{album_features.title()}: {album_info}')
    else:
        print(f'{album_features.title()}: {album_info.title()}')






    
    


