from flask import Flask, render_template, request


# export FLASK_APP=hello.py
# flask run

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
@app.route("/Home")
def index():
    return render_template("index.html")

    

@app.route("/bubble", methods=["GET","POST"])
def bubble():
    if request.method == "GET":
        return render_template("bubble.html")


    elif request.method == "POST":
        listy = request.form["myList"].split(",")
        listy = fixList(listy)
        sortedList, comps = bubbleSort(listy)
 
        return render_template("bubble.html", sortedList=sortedList, comparisons=comps)
 

@app.route("/merge", methods=["GET", "POST"])
def merge():
    if request.method == "GET":
        return render_template("merge.html")


    elif request.method == "POST":
        listy = request.form["myList"].split(",")
        listy = fixList(listy)

        sortedList, comps = mergeSort(listy, 0)
 
        return render_template("merge.html", sortedList=sortedList, comparisons=comps)

@app.route("/linear", methods=["GET", "POST"])
def linear():
    if request.method == "GET":
        return render_template("linear.html")


    elif request.method == "POST":
        listy = request.form["myList"].split(",")
        listy = fixList(listy)
        try:
            searchFor = int(request.form["searchVal"])
            result, comps = linearSearch(listy,searchFor)
        except:
            result = "the search value is not an integer"
            comps = "N/A"
 
        return render_template("linear.html", result=result, comparisons=comps)

@app.route("/binary", methods=["GET", "POST"])
def binary():
    if request.method == "GET":
        return render_template("binary.html")


    elif request.method == "POST":
        listy = request.form["myList"].split(",")
        listy = fixList(listy)
        if checkSorted(listy):
            searchFor = int(request.form["searchVal"])
            result = binarySearch(listy,searchFor)
        else:
            result = "The list was not sorted in ascending order"
 
        return render_template("binary.html", result=result)


# ============================== pythonic funcs ==============================

def fixList(listy):
    fixedList = []
    for i in listy:
        try:
            i = int(i)
            fixedList.append(i)
        except:
            pass

    return fixedList

def checkSorted(listy):
    for i in range(len(listy)-1):
        if listy[i] > listy[i+1]:
            return False
    return True



def bubbleSort(theList):
    comps = 0
    origLen = len(theList)
    swaps = -1
    passes = 0

    while swaps != 0 and passes < origLen:
        comps += 2
        swaps = 0
        for i in range(origLen-passes-1):
            comps += 1
            if theList[i] > theList[i+1]:
                theList[i], theList[i+1] = theList[i+1], theList[i]
                swaps += 1
        passes += 1
    return theList, comps

def mergeSort(listy, comps):
    comps += 1
    if len(listy) > 1:
        mid = len(listy)//2
        right = listy[mid:]
        left = listy[:mid]

        right, comps = mergeSort(right, comps)
        left, comps = mergeSort(left, comps)

        nextList = []
        pointer1 = 0
        pointer2 = 0
        comps += 2
        while pointer1 < len(left) and pointer2 < len(right):
            comps += 1
            if left[pointer1] < right[pointer2]:
                nextList.append(left[pointer1])
                pointer1 += 1
            else:
                nextList.append(right[pointer2])
                pointer2 += 1
        comps += 1
        if pointer1 < len(left):
            for val in left[pointer1:]:
                nextList.append(val)
        else:
            for val in right[pointer2:]:
                nextList.append(val)

        listy = nextList
    return listy, comps


def linearSearch(theList, val):
    comps = 0
    for i in theList:
        comps += 1
        if i == val:
            return "True", comps
        
    return "False ", comps

def binarySearch(theList, val):
    if len(theList) == 1:
        if theList[0] == val:
            return "True"
        else:
            return "False"
    else:
        midpoint = len(theList)//2
        if theList[midpoint] == val:
            return "True"
        elif theList[midpoint] > val:
            return binarySearch(theList[:midpoint], val)
        else:
            return binarySearch(theList[midpoint:], val)


if __name__ == "__main__":
    app.run(debug=True)



