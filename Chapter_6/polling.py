favorite_language = {
    "Jen": "Python",
    "Sarah": "C",
    "Edward": "Ruby",
    "Phil": "Python",
}

expected_voters = ["Jen", "Sarah","Will", "Edward", "Phil", "Mike", "Sadie"]


for voter in expected_voters:
    if (voter in favorite_language.keys()):
        print(f"Thank you {voter} for taking part in the poll!")
    else:
        print(f"Hello {voter}! Please take the poll at a time of your convenience!")