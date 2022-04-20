# ParkingSystem
## Solution to final proyect (OOP)

## description of the problem

Have you ever been in a parking lot and can’t find a free parking spot? Either because of the clutter on the part of the drivers or the parking lot, or even because of the high traffic inside a parking lot, it is a nuisance to deal with these situations; you lose time and in most cases you despair. This is the problem we seek to combat with our project. 

We will have a vehicle registration system where the basic data of the same are stored, as well as additional data regarding the date and time, in addition, the owner of the vehicle can decide whether to use our services inside the parking (if available), which will be invoiced together with the parking lot on a single invoice. Additional, after entering the vehicle data to our system, you will be assigned a place inside the parking lot (you will take into account if there is a disabled person or not). 

### Functional and non-functional requirements

#### Functional requirements

- The system must allow users to create and log in to an account.
- The system must allow users to input the parking organization system.
- The system must allow users to see and edit any car information.
- The system must allow users to manage the bills

#### Non-functional requirements

- The parking organization will be read from a text file.
- The app shall open the exit door only if the identified plate has no debt.
- The workers have the possibility to have a car that not pay
 
### Similar solutions in literature and the market

Referring about the solution market based on this approach, there are currently many options and solutions, some with more features than others, but the basics are entering and exiting vehicles and how it is readed in the program. Most basic solutions import the data input manually (plate) and the output via a button or option (also manually). The most dedicated solutions already integrate a detection system at the entrance/exit of the vehicles, so the input and output of the data (only from the license plate) is automatic, and the presence of an operator is hardly dispensable. For some additional functions, such as the general data of the parking lot (availability, number of vehicles), this is also done automatically by a detection system based on magnets. Some of these projects are used in shopping’s centers likes the ’Buenavista Shopping Center”. If we specifically refer to the program’s architecture, we can be found many variates solutions in free projects on sites like ”codeprojectz”, ”itsourcecode”, ”morioh” and many others. In order not only to complete our project successfully, but also to support these projects free of some innovations, we will implement the allocation of seats inside the parking lot automatically at the entrance of the parking lot, a feature that will avoid confusion and problems in finding seats vacant, making the car park a place with better mobility. 

### Available technologies 

In order to make our project and its functions, there is enough technology to be able to fulfill all of our functions. From the programmable aspect, we have libraries such as “Pytesseract” or “Folium” for the conception of the board and its data and libraries such as “Numpy” for video processing among the functions that stand out the most.
