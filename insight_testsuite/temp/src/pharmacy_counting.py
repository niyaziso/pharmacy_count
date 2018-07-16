# main file 
# 

import sys
inFile = sys.argv[1]
outFile = sys.argv[2]
#pharmcount2 = counting("../insight_testsuite/tests/mytest/input/itcont.txt") #../input/itcont.txt
def counting(input_file):
    pharmcount1 ={}
    with open(input_file, "rb") as inp:
        for i, line in enumerate(inp):
            if i >0 :
                sepline = line.split(",")
                #print sepline
                if sepline[3] not in pharmcount1:
                    pharmcount1[sepline[3]] = [0, 0]
                if sepline[3] in pharmcount1:
                    pharmcount1[sepline[3]]= [pharmcount1[sepline[3]][0]+1,pharmcount1[sepline[3]][1]+float(sepline[4])]
    pharmcount2 = sorted(pharmcount1.items(), key=lambda kv: kv[1][1], reverse=True)
    return pharmcount2


pharmcount2 = counting(inFile)

output_file = outFile#"../output/top_cost_drug.txt"
with open(output_file, "wb") as out:
    out.write("drug_name,num_prescriber,total_cost\n")
    for i in range(len(pharmcount2)):
        out.write((pharmcount2[i][0])+",")
        out.write(str(pharmcount2[i][1][0])+",")
        out.write(str(int(pharmcount2[i][1][1]))+"\n")
