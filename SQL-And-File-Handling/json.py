import json
#python JSON looks very much similar to dictionary in python for example
data = {
    'books': 12,
    'articles': 100,
    'subjects': ['math', 'programming','data science']
}

#We can convert this to a JSON format string in Python by first importing the built-in json module, then using json.dumps()

#import json

json_string = json.dump(data)
print(json_string)

#If you want to convert back to a dictionary, we can do it with json.loads() method

data = json.loads(json_string)
print(data)

