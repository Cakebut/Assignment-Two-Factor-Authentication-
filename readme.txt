Two factor Authentication 

Write two separate programs to simulate two-factor authentication. These 
programs must not communicate through sockets, files, or any other means. 
The implementations should be consistent and capable of operating on 
different computers. 

Requirements: 
• The programs must be written in either Java, C/C++, or Python. 
• Compilation environment instructions will be provided separately. 
• Include a Readme.txt file with detailed instructions on how to compile 
the programs within the specified environment. 


The programs are as follows: 
1. Device: This represents the device which can provide one–time pins 
that need to be used along with a password. 
2. Connect: This represents the device which a user intends to connect to, 
and that the user needs to provide authentication to. 
Device should run as: 
Device username password 
for example, Device Alice 1wdcasFga 
Device does not check that the user or password is valid. It starts 
generating ”one–time” pin values, 6 digit pins. As far as being one–time 
you do not need to check that they haven’t been used before. 
Device: 107283 
Device: 837226 
Device: 012123 
Device: 492833 
Device: 217281 
... 
Each pin should be valid for 15 seconds, although the first pin does not 
need to be displayed for 15 seconds before the next is displayed. Every 15 
seconds, other than for the first pin, a new now-valid pin should appear. 
So, 15 seconds is how long a user must use that pin in attaching to Connect. 
The details of pin generation inside Device are up to you. but it needs to be 
a function of the user and their password in such a way that the Connect 
can check it is correct during the appropriate time window. 


Device should keep running until it is broken by the user, with Ctrl-C for 
example. 
You should include, with your answers to the first part of the assignment, 
an explanation of the relationship you have chosen to use. You should also 
explain why you consider the pin values will not leak information about the 
password despite being a function of the password and username. 
Connect should run as: 
Connect username new 
or 
Connect username password pin 
The first form is for new users. A new user should be prompted to enter a 
password twice for confirmation. There should be basic checks to ensure 
the appropriateness of the password. If the password meets the criteria, it 
should be stored in a file called Passwords.txt, along with the username. 

This file should be in plain text, meaning the contents will be human- 
readable, with the password visible. Although this is not a secure practice 
in real scenarios, it simplifies the assessment. You can decide the file's 
format, but it should allow for easy reading and searching of users within 
the file. 

In the second form, the program should verify the username, password, 
and pin. It should read from the Passwords.txt file to check the consistency 
of the username and password.



****************************************************************************************************************************************
Running both code on Cyberlab terminal

Do change the path if necessary: cd Desktop/<Folder name>


- To start the device which can provide one–time pins every 15 secs, enter the following format in the terminal:

python3 device.py <username> <password>

---------------------------------------------------------------------------------------

- For the Connecting:

Adding a new User, enter the following format in the terminal:
python connect.py <username> new

* Do note Password must be at least 8 characters long, contain letters and numbers

------------------------------------------------------------------------------------------
Connect to the device, enter the following format in the terminal:

python connect.py <username> <password> <OTP>

The otp is obtained from the device.py that should be running
