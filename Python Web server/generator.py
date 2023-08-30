import pyttsx3
import re
#import pdb
"""
the whole point of this program is that it accepts  code snippets as  strings from a given web page where the code snippet is from. consider the first variable var 2  which represents this. the outpout will return " isBoolean  is equal to True of type Boolean " and the general movement of this program was to annotate everything such as data structures as well as functions and built in keywords and annotate them. as of now i currently have data structures being worked . built in key words yet to be done as well as functions.
"""
var2 = "isBoolean = True "
keywords ={
    "and": "and",
    "as" : "create as",
    "assert": "assert test case",
    "break" : "break out of loop",
    "class" : "class",
    "continue": "continue to next iteration of loop",
    "def": "define function",
    "del": "delete",
    "elif": "else if",
    "else" : "else",
    "except": "except triggered",
    "False": "Boolean value False",
    "finally": "finally this will be executed regardless of exception",
    "for":"for",
    "from": "from",
    "global": "declare global variable",
    "if": "if",
    "import": "import",
    "in": "in",
    "is": "is equal to",
    "lambda": "lambda",
    "None" : "Null value",
    "nonlocal" : "nonlocal",
    "not": "not",
    "or" : "or",
    "pass" : "pass",
    "raise": "raise exception has been triggered",
    "return": "return",
    "True": "Boolean Value True",
    "try": "try",
    "while": "while",
    "with": "with",
    "yield": "yield"
 }
def describe_array(arr):
    result = ""
    stack = []
    last_item = None

    for item in arr:
        if item == "[":
            stack.append("open list")
            result += "open list. "
        elif item == "{":
            stack.append("open dictionary")
            result += "open dictionary "
        elif item == "]":
            stack.pop()
            result += "close list. "
        elif item == "}":
            stack.pop()
            result += "close dictionary. "
        elif item.isdigit():
            if last_item == ":":
                
                #result = result[:-len("of type integer, ")]  # Remove the last description
                result += f"with value {item} of type integer "
            else:
                result += f"{item} of type integer "
        elif item.startswith('"') and item.endswith('"'):
            result += f"{item[1:-1]} of type string "
        elif item == ":":
            
            key = arr[arr.index(last_item) ]
            result = result.replace(f"{key} of type integer", f"with key {key} of type integer", 1)
            last_item = item
            continue  # Skip appending ":" as a description
        elif item == ",":
            continue
        
        last_item = item

    return result.strip()
def floatorinteger(value):
    #helper function for evaluateAssignment Value
    try:
        print(int(value))
        return " of type integer"
    except ValueError:
        try: 
            print(float(value))
            return " of type float"
        except ValueError:
            return None


def evaluateAssignmentValue(value):
    # this function is for when we know the given line is definitely a variable. its ony role is to determine primitive data type.
    returnval = None
    switchCaseReplacementForDataPrimitives= {
        '"' : " of type String",
        "'" : " of type String",
        "True": " of type Boolean",
        "False": " of type Boolean",
        "None":" of type   None"
    }
    for i ,x in switchCaseReplacementForDataPrimitives.items():
        if value[0] == i:
            returnval =x
            break
        elif value == i:
            returnval = x
    if not returnval:
        returnval = floatorinteger(value)
    if not returnval:
        if value in existingvariables: # check if current assignment is a reference to existing variable
            returnval = f" variable {value}"
        else:
            return " variable . SYSTEM WARNING!SYSTEM WARNING! ASSIGNING CURRENT VARIABLE TO NON-EXISTENT VARIABLE." 

    return returnval

existingvariables = set() # I want this because I dont know yet might come in handy. in the first case want to see if a variables being assigned to a non existing one




num = 1j

print(type(num),"hello")







formatstringset = { "=" , "[" , "]","{","}","(",")", ":" }


test2 = var2.split(" ")



def formatstring(curline):
    # handle user not delineatating their code with even spaces. I need this to happen because I want to parse the strings without using eval
    # and furthermore will be using the split function on the string so i can then interpret the meaning of the array. this will also work with functions ,parenthesis and anywhere where the special sequence of characters convey a unique meaning
    output = ""
    curline = curline.replace(","," ")
    print(curline, "before")
    
    for i in range(len(curline)-1):
        output+=curline[i]
        curletter = curline[i]
        if curline[i] in formatstringset:
            output=output[0:len(output)-1]+ " "
            output+= curline[i]
            output+=" "
    if output[-1] != curline[-1]:
            output+= " "
            output+=curline[-1]
    cleanstring = re.sub(r'\s+', ' ', output)    
    return cleanstring.strip()
var3 = formatstring(var2)
print(var3,"haha")
test3 = var3.split(" ")
print(test3)
#var4 = "theobject={1:0,2:1,3:2}"
#var4 = "[{1:0},2,3,[5,6,7]]"
#var4 = "x = [{1:0,2:[[1,2,3],{1:0}]},2,3,[5,6,7]]" # this was me messing around with some nested data structures
#var4 = formatstring(var4)
#test4 = var4.split(" ")
#print(test4)

string = ""
structures = {"{": ["set","dictionary"],"(":"tuple","[":"list" ,"set":"set"}
types = {"<class 'int'>": " class integer","<class 'str'>": "class string"}
test = test3

if test[0] not in keywords: # if first word is not a special keyword IT HASTO BE  A VARIABLE inside this block handles if data structure or primitive
    #pdb.set_trace() 
    string+=" variable " + " " + test[0] + " "
    isstructure = False
    isdatatype = False
    for i in range(1,len(test)-1):
        #if istructure is true : break
        if isstructure:
            break
        if test[i] == "=" and test[i+1] in structures :
            isstructure= True #we need this to exit out of the loop, in the simple case varaible being assigned will only have a single data strcuture , but we might encounter a nested data structure , should have special function to handle this and exit the loop.
            if test[i+1] == "set":
                string+=" is equal to data structure of type set"
            else:
                rest = []
                rest = test[i::]
                print(rest , "here now")
                string += " is equal to data structure "
                string += describe_array(rest)
        else: # if assignment is not a strucutre then barring any unforseen incidents it has to be a primitive data type.
            string+=" is equal to "
            string+= test[i+1]
            #string += " of type "
            string += evaluateAssignmentValue(test[i+1])
else:
    #here we handle the case where we are defining a function for the first time and we need to consider the following
    """
    at the first case : define function  with name trailingzeroes. 
    if it has parameters specify if parameters have type if not then type any, list each parameter.
    inside the function the determine the cases where:
    a variable is being described which we handled above
    a special keyword is being used eg a loop
    determine if a operation is being performed eg *= is times equals
    """
    print(test[0])
    for i in range(len(test)):
        string+= test[i]



engine = pyttsx3.init()
print(string)
engine.setProperty("rate",145) 
engine.say(string)
engine.runAndWait()

