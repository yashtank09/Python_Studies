import csv

fields = ['id', 'songname', 'singername', 'duration', 'catagory', 'language']
rows = [[1, 'Vaishnav Jan', 'Narsinh Mehta', 4, 'Bhajan', 'Gujarati'],
        [2, 'Hanuman Chalisa', 'Gulshan Kumar', 8, 'Bhajan', 'Hindi'],
        [3, 'See You Again', 'Wiz Khalifa', 4, 'POP', 'English'],
        [4, 'Lift Karade', 'Adnan Sami', 5, 'Hindi POP', 'Hindi'],
        [5, 'Behti Hava Sath avo', 'Shan', 3, 'Mild', 'Hindi']
       ]

filename = 'songs.csv'

with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)