#create 5 variables using different naming conventions

#STUDENTNAME="navya"
#studentname="navya"
#Studentname="navya"
#studentName="navya"
#student_name="navya"
#student-name="navya"

#create inavlid variable names and observe the error

#1a=5
#print(1a)       #cannot start with a number

#$=8
#print($)        #cannot start with special character lik @

#if a=5
#print(a)       #cannot use keywords like if,e else etc

#a=5
#print(id(A))    #it is case sensitive even though same variable but differnt meanings

#create one variable of each data types

#a=5
#print(type(a),id(a))

#b=5.0
#print(type(b),id(b))

#c="hello"
#print(type(c),id(c))

#d=True
#print(type(d),id(d))

#list
#players= ["Rohit", "Virat", "Gill", "Dhoni"]
#players[2]="surya"
#players.append("jadeja")
#print(players)
#print(len(players))
#print(players[-2])

#tuples
#laptop_info = ("HP", "16GB", "512GB SSD", 2024, True) 
#laptop_info["HP"]="dell"
#print(laptop_info) #there is an error due to tuples are immutable
#print((laptop_info[-2]))
#print((laptop_info[-1]))                  


#sets
#s = {"India", "USA", "India", "Canada", "UK", "USA"} 
#print(s)
#s.remove("UK")
#s.add("germany")
#print(s)

#frozenset
#frozen_marks = frozenset([90, 85, 75, 85]) 
#frozen_marks.add(95)
#frozen_marks.remove(75)
#print(frozen_marks) #it would be error because these are immutable it means frozen
#print(type(frozen_marks))

#Dictionaries
#car_info = { "brand": "Tesla", 
             #"model": "Model S", 
             #"price": "1.5Cr", 
             #"features": ["Autopilot", "Electric", "Sunroof"] }
#car_info["color"]="white"
#print(car_info)
#car_info["price"]="1.7cr"
#print(car_info)
#car_info["insurance"]={"provider": "HDFC", "valid_till": "2026"}
#print(car_info)

#books = [ 
#{"title": "Atomic Habits", "author": "James Clear"}, 
#{"title": "Ikigai", "author": "Héctor García"}, 
#{"title": "Zero to One", "author": "Peter Thiel"}]
#books.append({"title":"Good Omens","author":"Neil Gaiman"})
#print(books)

#laptop = { 
#"brand": "Apple", 
#"specs": {"ram": "16GB", "storage": "1TB SSD", "chip": "M2"}, 
#"price": "2L"  
#}
#print(laptop["specs"]["chip"])
#print("Apple laptop comes with M2 chip and costs 2l")

#a=5
#b=5
#print(id(a))
#print(id(b))

