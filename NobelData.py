import json
class NobelData:
    def __init__(self, file_name = 'nobels.json'):
        with open(file_name) as nobel_file:
            self.nobel_data = json.load(nobel_file)

    def search_nobel(self, year, category):
        winners = []
        for entry in self.nobel_data:
            if entry['year'] == year and entry['category'] == category:
                winners.append(entry['laureates'][0]['surname'])
        return sorted(winners)

nd = NobelData()
print(nd.search_nobel("2001", "economics"))

'''
Output should be:

['Akerlof', 'Mackey', 'Spence']
import json

class NobelData():
    def __init__(self):
        with open('nobels.json') as json_file:
            self.nobels = json.load(json_file)

    def search_nobel(self, year, category):
        winners = []
        for nobel in self.nobels:
            if nobel['year'] == year and nobel['category'] == category:
                winners.append(nobel['laureates'][0]['surname'])
        return sorted(winners)



if __name__ == '__main__':
    nd = NobelData()
    print(nd.search_nobel("2001", "economics"))
    print(nd.search_nobel("1975", "literature"))
    print(nd.search_nobel("1945", "peace"))
    print(nd.search_nobel("1968", "physics"))
    print(nd.search_nobel("1998", "medicine"))
    print(nd.search_nobel("1903", "chemistry"))


The init method should read the json file and save the data into a private data member of the class.

The search_nobel method should take as parameters a year and a category, and return the surname of the winner (or winners, in the case of a shared prize) for that category for that year.

The year parameter to search_nobel will be a string (e.g. "1975"), not a number.

You can assume that the categories are: "chemistry", "economics", "literature", "peace", "physics", and "medicine".

You can assume that the only possible values for the category parameter are those six strings.

You can assume that the only possible values for the year parameter are years for which there is data in the JSON file (i.e. 1901 through 2016).

You can assume that there is at most one winner for each category in each year (i.e. there will never be two or more people sharing the same prize in a single year).

You can assume that the name of each winner will be in the format "Firstname Lastname".

nd = NobelData()
print(nd.search_nobel("1975", "peace"))
print(nd.search_nobel("2001", "economics"))
print(nd.search_nobel("1982", "medicine"))
print(nd.search_nobel("1984", "literature"))
print(nd.search_nobel("1975", "chemistry"))
print(nd.search_nobel("1926", "physics"))
print(nd.search_nobel("1955", "physics"))
print(nd.search_nobel("1930", "economics"))