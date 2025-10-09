# 3.12.6
# import CSV file

import pandas as pd

def find_range(filePath, startRow, endRow, caseNumber, isMax):
    try:
        df = pd.read_csv(filePath)
        # print("Data loaded")
    except FileNotFoundError:
        print("File not Found")

    # print("Shape: " + str(df.shape))

    filter = (df["CaseNo"] == int(caseNumber)) & (df["MemberNo"] >= int(startRow)) & (df["MemberNo"] <= int(endRow))
    filtered = df.loc[filter, "Fxb"]

    # print(filtered)

    if isMax == True:
        return filtered.max()
    else:
        return filtered.min()

if __name__ == "__main__":
    filePath = "public/Steels Assignment 2_results.csv" # Change to your file format: public/filename
    # Prolly should've used a loop lol
    # Change beam numbers to your numbers in Microstran
    startMemberSeg11 = 201
    endMemberSeg11 = 206
    startMemberSeg12 = 207
    endMemberSeg12 = 214
    startMemberSeg13 = 215
    endMemberSeg13 = 220

    startMemberSeg21 = 102
    endMemberSeg21 = 106
    startMemberSeg22 = 107
    endMemberSeg22 = 115
    startMemberSeg23 = 116
    endMemberSeg23 = 120

    startMemberSeg31 = 401
    endMemberSeg31 = 412
    startMemberSeg32 = 413
    endMemberSeg32 = 428
    startMemberSeg33 = 429
    endMemberSeg33 = 440
    # Don't change below this line.

    # Case 5
    result1case5 = find_range(filePath, startMemberSeg11, endMemberSeg11, 5, True) # Top Chord
    result2case5 = find_range(filePath, startMemberSeg12, endMemberSeg12, 5, True)
    result3case5 = find_range(filePath, startMemberSeg13, endMemberSeg13, 5, True)

    result4case5 = find_range(filePath, startMemberSeg21, endMemberSeg21, 5, False) # Bottom Chord
    result5case5 = find_range(filePath, startMemberSeg22, endMemberSeg22, 5, False)
    result6case5 = find_range(filePath, startMemberSeg23, endMemberSeg23, 5, False)

    result7case5 = find_range(filePath, startMemberSeg31, endMemberSeg31, 5, True) # Middle Chord
    result8case5 = find_range(filePath, startMemberSeg32, endMemberSeg32, 5, True)
    result9case5 = find_range(filePath, startMemberSeg33, endMemberSeg33, 5, True)

    # Case 6
    result1case6 = find_range(filePath, startMemberSeg11, endMemberSeg11, 6, False)
    result2case6 = find_range(filePath, startMemberSeg12, endMemberSeg12, 6, False)
    result3case6 = find_range(filePath, startMemberSeg13, endMemberSeg13, 6, False)

    result4case6 = find_range(filePath, startMemberSeg21, endMemberSeg21, 6, True)
    result5case6 = find_range(filePath, startMemberSeg22, endMemberSeg22, 6, True)
    result6case6 = find_range(filePath, startMemberSeg23, endMemberSeg23, 6, True)

    result7case6 = find_range(filePath, startMemberSeg31, endMemberSeg31, 6, True)
    result8case6 = find_range(filePath, startMemberSeg32, endMemberSeg32, 6, True)
    result9case6 = find_range(filePath, startMemberSeg33, endMemberSeg33, 6, True)

    # Case 7
    result1case7 = find_range(filePath, startMemberSeg11, endMemberSeg11, 7, True)
    result2case7 = find_range(filePath, startMemberSeg12, endMemberSeg12, 7, True)
    result3case7 = find_range(filePath, startMemberSeg13, endMemberSeg13, 7, True)

    result4case7 = find_range(filePath, startMemberSeg21, endMemberSeg21, 7, False)
    result5case7 = find_range(filePath, startMemberSeg22, endMemberSeg22, 7, False)
    result6case7 = find_range(filePath, startMemberSeg23, endMemberSeg23, 7, False)

    result7case7 = find_range(filePath, startMemberSeg31, endMemberSeg31, 7, True)
    result8case7 = find_range(filePath, startMemberSeg32, endMemberSeg32, 7, True)
    result9case7 = find_range(filePath, startMemberSeg33, endMemberSeg33, 7, True)

    # Top Chord
    print("The value for case 5 for segment 1 Top Chord is : " + str(result1case5))
    print("The value for case 5 for segment 2 Top Chord is : " + str(result2case5))
    print("The value for case 5 for segment 3 Top Chord is : " + str(result3case5))

    print("The value for case 6 for segment 1 Top Chord is : " + str(result1case6))
    print("The value for case 6 for segment 2 Top Chord is : " + str(result2case6))
    print("The value for case 6 for segment 3 Top Chord is : " + str(result3case6))

    print("The value for case 7 for segment 1 Top Chord is : " + str(result1case7))
    print("The value for case 7 for segment 2 Top Chord is : " + str(result2case7))
    print("The value for case 7 for segment 3 Top Chord is : " + str(result3case7))

    print("\n")

    # Bottom Chord
    print("The value for case 5 for segment 1 Bottom Chord is : " + str(result4case5))
    print("The value for case 5 for segment 2 Bottom Chord is : " + str(result5case5))
    print("The value for case 5 for segment 3 Bottom Chord is : " + str(result6case5))

    print("The value for case 6 for segment 1 Bottom Chord is : " + str(result4case6))
    print("The value for case 6 for segment 2 Bottom Chord is : " + str(result5case6))
    print("The value for case 6 for segment 3 Bottom Chord is : " + str(result6case6))

    print("The value for case 7 for segment 1 Bottom Chord is : " + str(result4case7))
    print("The value for case 7 for segment 2 Bottom Chord is : " + str(result5case7))
    print("The value for case 7 for segment 3 Bottom Chord is : " + str(result6case7))

    print("\n")

    # Diagonals
    print("The value for case 5 for segment 1 Diagonal Chord is : " + str(result7case5))
    print("The value for case 5 for segment 2 Diagonal Chord is : " + str(result8case5))
    print("The value for case 5 for segment 3 Diagonal Chord is : " + str(result9case5))

    print("The value for case 6 for segment 1 Diagonal Chord is : " + str(result7case6))
    print("The value for case 6 for segment 2 Diagonal Chord is : " + str(result8case6))
    print("The value for case 6 for segment 3 Diagonal Chord is : " + str(result9case6))

    print("The value for case 7 for segment 1 Diagonal Chord is : " + str(result7case7))
    print("The value for case 7 for segment 2 Diagonal Chord is : " + str(result8case7))
    print("The value for case 7 for segment 3 Diagonal Chord is : " + str(result9case7))