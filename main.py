import os
import csv
voterID = []
county = []
candidate = []
votes_total = 0
stockham = 0
degette = 0
doane = 0
jefferson = 0
denver = 0
arap = 0

csvpath = os.path.join("Resources", "election_results.csv")

#open file to data
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ",")
    #test open
    print(csvreader)
    csv_header = next(csvreader)
    #test print header
    print(csv_header)

    for row in csvreader:
        #populate lists 
        voterID.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
        
        if row[1] == "Jefferson":
            jefferson = jefferson +1
        elif row[1] == "Denver":
            denver = denver +1
        elif row[1] == "Arapahoe":
            arap = arap +1
        
        if row[2] == "Charles Casper Stockham":
            stockham = stockham +1
        elif row[2] == "Diana DeGette":
            degette = degette +1
        elif row[2] == "Raymon Anthony Doane":
            doane = doane +1

        
        
      
    votes_total = len(voterID)
    stockham_percent = ((stockham/votes_total)*100)
    degette_percent = ((degette/votes_total)*100)
    doane_percent = ((doane/votes_total)*100)
    jefferson_percent = ((jefferson/votes_total)*100)
    denver_percent = ((denver/votes_total)*100)
    arap_percent = ((arap/votes_total)*100)

    candidates = {"Charles Casper Stockham": stockham, "Diana DeGette": degette, "Raymon Anthony Doane": doane}
    countyvotes = {"Jefferson": jefferson, "Denver": denver, "Arapahoe": arap}
    winner = max(candidates, key=candidates.get)
    winningvotes = candidates.values()
    winnervotes = max(winningvotes)
    winnerpercent = ((max(winningvotes)/votes_total)*100)
    countymax = max(countyvotes, key=countyvotes.get)
print(f"Election Results")
print(f"--------------------------")
print(f"Total Votes: ", votes_total)
print(f"--------------------------") 
print(f"County Votes:")
print(f"Jefferson: ", '{:.1f}%'.format(jefferson_percent), jefferson) 
print(f"Denver: ", '{:.1f}%'.format(denver_percent), denver) 
print(f"Arapahoe: "'{:.1f}%'.format(arap_percent), arap)
print(f"--------------------------")
print(f"Largest County Turnout: ", countymax)
print(f"--------------------------")
print(f"Charles Casper Stockham: ", '{:.1f}%'.format(stockham_percent), stockham)
print(f"Diana DeGette:  ", '{:.1f}%'.format(degette_percent), degette)
print(f"Raymon Anthony Doane:  ", '{:.1f}%'.format(doane_percent), doane)
print(f"--------------------------")
print(f"Winner:  ", winner)
print(f"Winning Vote Count: ", winnervotes)
print(f"Winning Percentage: ", '{:.1f}%'.format(winnerpercent))

output_path = os.path.join("Analysis", "PyPoll_Analysis.txt")

with open(output_path, "w") as text_file:
    print(f"Election Results", file = text_file)
    print(f"--------------------------", file = text_file)
    print(f"Total Votes: ", votes_total, file = text_file)
    print(f"--------------------------", file = text_file) 
    print(f"County Votes:", file = text_file)
    print(f"Jefferson: ", '{:.1f}%'.format(jefferson_percent), jefferson, file = text_file) 
    print(f"Denver: ", '{:.1f}%'.format(denver_percent), denver, file = text_file) 
    print(f"Arapahoe: "'{:.1f}%'.format(arap_percent), arap, file = text_file)
    print(f"--------------------------", file = text_file)
    print(f"Largest County Turnout: ", countymax, file = text_file)
    print(f"--------------------------", file = text_file)
    print(f"Charles Casper Stockham: ", '{:.1f}%'.format(stockham_percent), stockham, file = text_file)
    print(f"Diana DeGette:  ", '{:.1f}%'.format(degette_percent), degette, file = text_file)
    print(f"Raymon Anthony Doane:  ", '{:.1f}%'.format(doane_percent), doane, file = text_file)
    print(f"--------------------------", file = text_file)
    print(f"Winner:  ", winner, file = text_file)
    print(f"Winning Vote Count: ", winnervotes, file = text_file)
    print(f"Winning Percentage: ", '{:.1f}%'.format(winnerpercent), file = text_file)
