# MTCars Flask API

This is an example of running a program off of a Flask API. Everything required to make this happen (the Python environment, the code, the model) is created locally through the use of Docker. 

In order to run this API, you will need to have PYthon 3.7 and Docker both installed on your computer. 

After cloning the repository, navigate to the file named "docker" in your choice of command prompt program (I recommend Powershell for Windows users.)

Once there, run the following command:

`docker-compose up`

This will set up the Python environment and download any necessary requirements to run the model. 
This step may take some time, if your system needs to download any required components. 



If this step is successful, you will not get your input prompt back. To confirm that the localhost server is up and running, you can do one of either two options:

1. Open up a web browser and navigate to http://localhost:5000/

2. Open up a new terminal or command prompt and navigate back to the docker folder. Run the following curl command to get a response from the server.

`curl http://localhost:5000/`

In either step, you should see the following response from the server: "Server is up and running! Nice work!"

Note that if you are running a Windows computer, you will need to replace localhost with your computer's ip address being used for Docker. 


Now that the server is up and running, we can send it requests to make predictions off of the mtcars dataset. 


The model looks at the following variables to predict a car's miles per gallon:

- cyl
- disp
- hp
- drat
- wt
- qsec


Here is an example command:

`curl -H "Content-Type: application/json" -X POST -d '{"cyl": 8, "disp": 472, "hp": 205, "drat": 2.93, "wt": 5.25, "qsec": 17.98}' "http://localhost:5000/predict_mpg"`


If you are running on Windows, you will need to use the escape character on all of the quotes in the json request. For example:

`curl -H "Content-Type: application/json" -X POST -d '{\"cyl\": 8, \"disp\": 472, \"hp\": 205, \"drat\": 2.93, \"wt\": 5.25, \"qsec\": 17.98}' "http://localhost:5000/predict_mpg"`


The resulting prediction should be about 11.4 mpg. 


To stop the server running the API, press `ctrl-C`. 
You can confirm that the docker container has closed with the command `docker container ls`. If it is still running, you can kill it with `docker container kill <container name>`

