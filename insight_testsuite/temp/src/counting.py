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

