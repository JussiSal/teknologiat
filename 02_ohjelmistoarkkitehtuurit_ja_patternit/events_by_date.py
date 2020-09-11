import json
import urllib.request

def sortteri(array):
    for i in range(1, len(array)):
        itemi = array[i]
        j = i-1

        while j >=0 and str(itemi['event_dates']['starting_day']) < str(array[j]['event_dates']['starting_day']):
            array[j+1]=array[j]
            j = j-1
        array[j+1] = itemi

def haku():
    with urllib.request.urlopen('http://open-api.myhelsinki.fi/v1/events/') as response:
        return json.loads(response.read())

def main():
    tapahtumiendata = haku()
    array = tapahtumiendata['data']
    sortteri(array)
    for i in array:
        print(str(i['event_dates']['starting_day']) + " " + str(i['name']['fi']))

if __name__ == "__main__":
    main()