#program to represent the match case by using the python
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case 500 | 501 |502 |503:
            return "Server error"
        case _:
            return "Unknown error"

c=http_error(78)

def animal_sound(sound):
    match sound:
        case "cat":
            return "meow"
        case "dog":
            return "bark"
        case "sheep":
            return "baa"
        case _:
            return "unknown sound"

print(animal_sound("cat"))
print(animal_sound("dog"))
print(animal_sound("elephant"))

#some of the things do with "match statements"
#1.Basic value matching
def day_type(day):
    match day:
        case "Monday"| "Tuesday" | "Wednesday" | "Thursday" | "Friday" :
            return "Weekday"
        case "Saturday" | "Sunday":
            return "Weekend"
        case _:
            return "Invalid day "

print(day_type("Monday"))
print(day_type("Sunday"))
print(day_type("j"))

#Multiple Conditions in a Single Case
def weather_advice(weather):
    match weather:
        case "rainy"| "snowy" :
            return "Take an umbrella"
        case "sunny ":
            return "Wear sunglases"
        case _:
            return "Be prepared for anything"

print(weather_advice("sunny"))

#Desturcturing and unpacking

"note- You can match and unpack complex data structures such as tuples, lists, and dictionaries."

def process_point(point):
    match point:
        case (0,0):
            return "Origin"
        case (x,0):
            return f"X-axis at {x}"
        case (0,y):
            return f"Y-axis at {y} "
        case (x,y):
            return f"Point at ({x},{y})"
        case _:
            return "not a point "

print(process_point((0,0)))
print(process_point((3,0)))
print(process_point((0,4)))
print(process_point((2,5)))

#Type Matching
def describe_value(values):
    result = []
    for value in values:
        match value:
            case int():
                result.append("Integer")
            case str():
                result.append("String")
            case list():
                result.append("List")
            case _:
                result.append("Unknown type")
    global permanent
    permanent = tuple(result)

type1= [42,"hello",[1,2,3]]
print(describe_value(type1))
print(permanent)

#Guard Clauses 
""" Note - You can use guard clauses 
to add additional conditions to patterns."""

def process_number(*numbers):
    result=[]
    for number  in numbers:
        match number:
            case x if x<0:
                result.append("Negative")
            case x if x>0:
                result.append("Positive")
            case x if x==0:
                result.append("Zero")
    return result
print(process_number(0,8,-1))


