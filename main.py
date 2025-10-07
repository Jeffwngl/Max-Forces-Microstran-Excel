# 3.12.6
# import CSV file

import pandas as pd

def find_range(filePath, startRow, endRow, caseNumber, isMax):
    try:
        df = pd.read_csv(filePath)
        print("Data loaded")
    except FileNotFoundError:
        print("File not Found")

    print("Shape: " + str(df.shape))

    filter = (df["CaseNo"] == int(caseNumber)) & (df["MemberNo"] >= int(startRow)) & (df["MemberNo"] <= int(endRow))
    filtered = df.loc[filter, "Fxb"]

    print(filtered)

    if isMax == True:
        return filtered.max()
    else:
        return filtered.min()

if __name__ == "__main__":
    filePath = "public/Steels Assignment 2_results.csv"
    startMember = input("Enter member start: ")
    endMember = input("Enter member end: ")
    caseNumber = input("Enter case number: ")
    isMax = True if input("Enter max for maximum or anything else for minimum: ") == "max" else False

    result = find_range(filePath, startMember, endMember, caseNumber, isMax)
    print("The maximum is: " + str(result))