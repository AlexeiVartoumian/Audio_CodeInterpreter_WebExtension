# Audio_CodeInterpreter_WebExtension
## <h1> Why I made this </h1>
 There are many variants of this idea that exist already where you can highlight text for example and it would transcribe the input into audio input. I struggled however to find a web-extension that works specifically for code snippets inside text editors and struggled further still to find any that would describe a given code snippet outside of phonetic representation.\

 
 As such this project in this state only workd with Pythontutor.com and with the python language. However, I have tested this with Chatgpt-3 and it works in principle with thier code snippets as well as Udemies.\

 
 As such The project is divided into two folders , Javascript and PYTHON.  The javascript file named Web extension has a singular role: It send Code snippets as JSON and receives message from server as audio. Upon the icon being clicked it would target the specific class 
 where a code snippet lives as HTML, turns it into JSON and then sends it to the the Python web server that will be running listening for any requests made to it. The Second Folder Python Web Server  also has a singular responsibility upon receiving the JSON , would  convert the JSON object into an array of strings separated by spaces. and sends back the audio format of this strings.\

 
 it is here where the the Pyttsx3 library is used (Python text to speech) an machine learning library with an audio voice in that phonetically reads the sounds associated to a given letter and group of letters.\ 

 
 it is in the generator.py file where I am having a bunch of fun chopping and shaving the strings to add extra meaning to them. for example say there is a variabl# isBoolean = True. whilst in this case the phonetic representation is obvious as to what is being described I wanted to add extra meaning,for example the audio output would be  "variable isBoolean is equal to True of type Boolean" stating if the line in question is a variable and if so what data type does it contain.\

 
 furthermore I began implementing a similar use case for variables containing data structures, opting for a stack to read the input of the string and derive meaning from there. further down the road I would like to implement reserved keywords as well and built in functions too :)
