from flask import Flask, render_template, request

# export FLASK_APP=hello.py
# flask run

app = Flask(__name__)

posts = [1,2,3,4]

@app.route('/', methods=["GET","POST"])
@app.route("/Home")
def index():
    return render_template("index.html")

    

@app.route("/bubble", methods=["GET","POST"])
def bubble():
    if request.method == "GET":
        return render_template("bubble.html")


    elif request.method == "POST":
        listy = request.form["mylist"].split(",")
        listy = [int(x) for x in listy]
        sortedList = bubbleSort(listy)
 
        return render_template("bubble.html", sortedList=sortedList)
 

@app.route("/merge", methods=["GET", "POST"])
def merge():
    if request.method == "GET":
        return render_template("merge.html")


    elif request.method == "POST":
        listy = request.form["myList"].split(",")
        listy = [int(x) for x in listy]
        sortedList = mergeSort(listy)
 
        return render_template("merge.html", sortedList=sortedList)

@app.route("/linear", methods=["GET", "POST"])
def linear():
    if request.method == "GET":
        return render_template("linear.html")


    elif request.method == "POST":
        listy = request.form["myList"].split(",")
        listy = [int(x) for x in listy]
        searchFor = int(request.form["searchVal"])
        result = linearSearch(listy,searchFor)
 
        return render_template("linear.html", result=result)

@app.route("/binary", methods=["GET", "POST"])
def binary():
    if request.method == "GET":
        return render_template("binary.html")


    elif request.method == "POST":
        listy = request.form["myList"].split(",")
        listy = [int(x) for x in listy]
        searchFor = int(request.form["searchVal"])
        result = binarySearch(listy,searchFor)
 
        return render_template("binary.html", result=result)


# ============================== pythonic funcs ==============================


def bubbleSort(theList):
    origLen = len(theList)
    swaps = -1
    passes = 0

    while swaps != 0 and passes < origLen:
        swaps = 0
        for i in range(origLen-passes-1):
            if theList[i] > theList[i+1]:
                theList[i], theList[i+1] = theList[i+1], theList[i]
                swaps += 1
        passes += 1
    return theList

def mergeSorted(list1,list2):
    nextList = []
    pointer1 = 0
    pointer2 = 0
    while pointer1 < len(list1) and pointer2 < len(list2):
        
        if list1[pointer1] < list2[pointer2]:
            nextList.append(list1[pointer1])
            pointer1 += 1
        else:
            nextList.append(list2[pointer2])
            pointer2 += 1

    if pointer1 < len(list1):
        for val in list1[pointer1:]:
            nextList.append(val)
    else:
        for val in list2[pointer2:]:
            nextList.append(val)

    return nextList

def mergeSort(theList):
    if len(theList) == 1:
        return theList

    else:
        mid = len(theList)//2
        return mergeSorted(mergeSort(theList[:mid]), mergeSort(theList[mid:]))


def linearSearch(theList, val):
    for i in theList:
        if i == val:
            return "The item was found in the list"
        
    return "The item was not found in the list"

def binarySearch(theList, val):
    if len(theList) == 1:
        if theList[0] == val:
            return "The item was found in the list"
        else:
            return "The item was not found in the list"
    else:
        midpoint = len(theList)//2
        if theList[midpoint] == val:
            return "The item was found in the list"
        elif theList[midpoint] > val:
            return binarySearch(theList[:midpoint], val)
        else:
            return binarySearch(theList[midpoint:], val)


if __name__ == "__main__":
    app.run(debug=True)



