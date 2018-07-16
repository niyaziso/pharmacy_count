# main file 
# 

import sys
inFile = sys.argv[1]
outFile = sys.argv[2]
#pharmcount2 = counting("../insight_testsuite/tests/mytest/input/itcont.txt") #../input/itcont.txt

pharmcount2 = counting(inFile)

output_file = outFile#"../output/top_cost_drug.txt"
with open(output_file, "wb") as out:
    out.write("drug_name,num_prescriber,total_cost\n")
    for i in range(len(pharmcount2)):
        out.write((pharmcount2[i][0])+",")
        out.write(str(pharmcount2[i][1][0])+",")
        out.write(str(int(pharmcount2[i][1][1]))+"\n")
