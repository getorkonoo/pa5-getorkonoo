# Name:  Genevieve Torkornoo
# Date:  Novmber 12th 2021
# Problem Summary:
# Inputs:
# Outputs:
import math
DURATION_START = 2
DURATION_END = 3
DISTANCE = 4
COST = 5
PAYMENTS = 6
LATITUDE_START = 8
LONGITUDE_START = 9
LATITUDE_END = 10
LONGITUDE_END = 11

def readFile( filename ):
    allData = []
    try:
        file = open(filename, "r")
        for line in file:
            line = line.strip()
            temp = line.split(",")
            if (len(temp) == 12):
                try:
                    #temp[DURATION_START] = int(temp[DURATION_START])
                    #temp[DURATION_END] = int(temp[DURATION_END])
                    temp[DISTANCE] = float(temp[DISTANCE])
                    temp[COST] = float(temp[COST])

                    temp[LATITUDE_START] = float(temp[LATITUDE_START])
                    temp[LONGITUDE_START] = float(temp[LONGITUDE_START])
                    temp[LATITUDE_END] = float(temp[LATITUDE_END])
                    temp[LONGITUDE_END] = float(temp[LONGITUDE_END])
                    allData.append(temp)
                except ValueError:
                    print(line, "Bad data in line .. skipping")
            else:
                print(line, "Wrong amount of data in line .. skipping")
    except FileNotFoundError:
        return []
    return allData

def distance(lat1_deg, lon1_deg, lat2_deg, lon2_deg):
        lat1 = math.radians(lat1_deg)
        lon1 = math.radians(lon1_deg)
        lat2 = math.radians(lat2_deg)
        lon2 = math.radians(lon2_deg)
        return math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2)) * 3959

def averageCostCash(listofdata):
    #find the amount of ones that use cash
    count = 0
    sum = 0
    for temp in listofdata:
        if temp[PAYMENTS] == "Cash":
            sum += temp[COST]
            count += 1
    return sum/count

    # if it is under cash caculate the adverage ( sum/number of cash users)

def averageCostCredit(listofdata):
# find the amount of those who used card
    count = 0
    sum = 0
    for temp in listofdata:
        if temp[PAYMENTS] == "Credit Card":
            sum += temp[COST]
            count += 1
    return sum/count
# take the sum/number of card users



def onedaytrip (listofdata,givendate):
    count = 0
    for temp in listofdata:
        startDate = temp[DURATION_START].split(" ")
        #print(startDate[0])
        endDate = temp[DURATION_END].split(" ")
        if startDate[0] == givendate or endDate[0] == givendate:
            print(temp)
            count += 1

    return count

def givendistance(listOfData, newfile, lon, lat, dist):
    file = open(newfile,"w")
    #open file for writing user inputs file name
    #loop throught list of list and look at each long and lad in the list
    #call distance funtion ( user input lat1, lon1) long2 and lat2 come from the file.
    #compare if the distance calcuated is == or less then the distance provided by the user
    for temp in listOfData:
        distance1 = distance(temp[LATITUDE_START], temp[LONGITUDE_START] , lat, lon)
        distance2 = distance(temp[LATITUDE_END], temp[LONGITUDE_END], lat, lon)
        if distance1 <= dist or distance2 <= dist:






# user inputs filename
# user gives longtituide, ladituide, distance

#calcuate the distance between two points
def main():
    data = readFile("testinput.csv")
    # print( data )
    print("# of records =", len(data))
    #distance_baltimore_dc = distance(39.2904, -76.6122, 38.9072, -77.0369)
    #print("The distance between Baltimore and Washington is", distance_baltimore_dc, "miles")
    print("The average number of money people who used cash paid is", "%.2f" % averageCostCash(data) )
    print("The average number of money people who used credit paid is", "%.2f" % averageCostCredit(data))
    givenDate = input("Enter the date you started or ended then trip > ")
    onedaytrip(data, givenDate)
    longitude = float(input("Please input a longitude >"))
    latitude = float(input("please input a latitude >"))
    distance = float(input("Please input the distance > "))
    newFile = input("please type the name of the file you would like to open >")
    givendistance(data,newFile,longitude,latitude, distance)


main()