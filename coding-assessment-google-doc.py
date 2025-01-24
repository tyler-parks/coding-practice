from bs4 import BeautifulSoup   # Import BeautifulSoup for HTML Parsing
import requests                 # Import requests for HTML requests

#-----------------------#
#    HELPER FUNCTIONS   #
#-----------------------#

#-----------------------#
# Function: getArrayDimensions
# Params: data
# Use: Fetch the array dimensions
#      needed to create a readable
#      and correctly-sized display for the user.
#-----------------------#
def getArrayDimensions(data):
    # save the x and y coordinate rows, and convert the string numbers into integers
    xCoords = [eval(item[0]) for item in data]
    yCoords = [eval(item[1]) for item in data]

    xCoords.sort()
    yCoords.sort()

    xlargestCoord = xCoords[-1] + 1
    ylargestCoord = yCoords[-1] + 1

    return xlargestCoord, ylargestCoord
#----------END----------#

#-----------------------#
# Function: fetchHTML
# Params: url
# Use: Fetch and parse 
#      the HTML content
#      from the given URL
#-----------------------#
def fetchHTML(url):
    # Fetch the HTML content and store the content inside a "response" variable
    response = requests.get(url)
    html_content = response.content

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Parse the Table by locating the "table" and "tr" HTML tags
    table = soup.find('table')
    rows = table.find_all('tr')

    # Parse the Rows by storing the individual values inside sublists
    data = []
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele]) 

    # remove column labels
    data.pop(0)

    # return the parsed table data
    return data
#----------END----------#

#-----------------------#
# Function: normalizeCoords
# Params: data
# Use: The incoming data
#      displays the desired
#      character in-between
#      the x and y coordinates.
#      We can place the x, y 
#      coords next to one another.
#-----------------------#
def normalizeCoords(data):
    # normalize coordinates by using "temp" variable swapping
    for i in data:
        temp = i[1]
        i[1] = i[2]
        i[2] = temp

    return data
#----------END----------#

#-----------------------#
# Function: populateDisplay
# Params: data, xLarge, yLarge
# Use: Create an NxM large 2D Array (list of lists)
#      using the largest X and Y value found
#      inside the list of coordinates. 
#
#      Then, populate the 2D Array with the
#      corresponding values from "data".
#-----------------------#
def populateDisplay(data, xLarge, yLarge):
    # create a 2D grid of size "largestCoord"
    arr = [[' ']*xLarge for i in range(yLarge)]

    # for each list in "data"
    for i in data:
        # capture the x, y coordinates, along with the corresponding UNICODE character
        x = eval(i[0])
        y = eval(i[1])
        char = i[2]

        # remap the y value.
        #
        # This is so our array's [0,0] coordinate is located at the bottom-left corner
        # of the array.
        remapped_y = yLarge - 1 - y

        # assign the UNICODE character to the array at position arr[y][x],
        # where y has been remapped to align with the correct positioning.
        arr[remapped_y][x] = char

    # Finally, print the secret statement.
    for i in arr:
        print(*i, sep='')
#----------END----------#

def getSecretCode(url):
    # Call Helper Function to fetch the HTML content.
    data = fetchHTML(url)

    # Call Helper Function to normalize coordinates using variable swapping.
    data = normalizeCoords(data)

    # Call Helper Function to find and store the largest dimensions needed for the
    # x and y coordinates.
    xlargestCoord, ylargestCoord = getArrayDimensions(data)

    # Call Helper Function to display the secret code.
    populateDisplay(data, xlargestCoord, ylargestCoord)
#----------END----------#

#-----------------------#
#   MAIN DRIVER CODE    #
#-----------------------#
realURL = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"

# Final Submission with the secondary URL
getSecretCode(realURL)
#----------END----------#
