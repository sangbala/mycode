#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests

URL= "https://opentdb.com/api.php?amount=3&category=23&difficulty=easy&type=boolean"

def main():

    # data will be a python dictionary rendered from your API link's JSON!
    data= requests.get(URL).json()
    #print(data)
    #print()
    
    i=0
    while i<3: 
        print(data['results'][i]['question'])
        print(data['results'][i]['correct_answer'])        
        i+=1


if __name__ == "__main__":
    main()

