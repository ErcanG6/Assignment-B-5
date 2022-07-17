import json


#Implementation of NobelData class

class NobelData:

    #Implementation of init

    def __init__(self):

        #responseObject = requests.get("http://api.nobelprize.org/v1/prize.json")

        #load json format data

        with open("nobels.json","r") as read_file:
            self.data = json.load(read_file)

    #Implementation of search_nobel method

    def search_nobel(self,year,category):

        #Declare n and store the length of self.data['prizes']

        lengthofPrizes= len(self.data['prizes'])

        #Declare winners as type of list

        winners=[]

        #Declare surnamesofthewinners as type of list

        surnamesofthewinners=[]

        #Iterate loop

        for each in range(0,lengthofPrizes):

            #check self.data['prizes'][each]['year'] is equal to year

            #and check self.data['prizes'][each]['category'] is equal to category

            if(self.data['prizes'][each]['year']==year and self.data['prizes'][each]['category']==category):

                #assign self.data['prizes'][each]['laureates'] to winners

                winners=self.data['prizes'][each]['laureates']

                break

        #caclulate the length of winners and store in lengthofWinners

        lengthofWinners=len(winners)

        #Iterate the loop

        for each in range(0,lengthofWinners):

            #append the winners[each]['surname'] to surnamesofthewinners

            surnamesofthewinners.append(winners[each]['surname'])

        #sort the surnamesofthewinners

        surnamesofthewinners.sort()

        return surnamesofthewinners

#Declare an object for NobelData

nd = NobelData()

#call serach_nobel method

nd.search_nobel("2001", "economics")

#Display statement

print(nd.search_nobel("2001", "economics"))