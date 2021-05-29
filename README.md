# ODBM
odbm api call with python3.

This program will generate ODBMapi output on the commandline console.

API key has to be generated from the website at the first place.

I have imported requests and pprint to get the pretty output on the console.

I have assigned "r" for the API key.

When you successfully execute the program the console output will be the desired moviename details.

Run "python3 odbm.py" to execute the program.


Pre-requsites:
==============

Pithon3 and pip should be installed on the system.

"pip install omdbapi"

"pip install requests pprintpp"

Requests and PPrint is also required which can be installed by pip.


Commandline output of the program is uploaded as a screenshot. (https://github.com/bhargavaE/ODBM/blob/main/Screenshot%20from%202021-05-29%2015-40-35.png)


Docker Image :
==============

Run the command "docker build -t omdb:0.1 ." ..... which will create a docker image with name and tag as omdb and 0.1.

To run the Docker image use the command "docker run -it -p 8000:8000 omdb:0.1"

