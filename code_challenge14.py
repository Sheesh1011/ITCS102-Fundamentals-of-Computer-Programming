list_anime = [ ]

while True:
    title = input("Enter the title of an anime (type 'exit' to exit): " )
    
    if title == "exit": 
        print("Exiting the program.")
        break
    else:
         list_anime.append(title)
         print(f"> {title} < has been added to your lists")
        
print("Your anime lists: ")
for anime in list_anime:
       print(f"> {anime}")


