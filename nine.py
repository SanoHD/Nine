import sys, os, shlex

#  N     INE
# (NEXT LINE)

var = {}
commentsymbol = ";"
filename = sys.argv[1]

def error(txt):
    global LN, LC
    print("[ERROR]",txt,str(LN)+":"+str(LC))
    sys.exit()

def parser(line):
    global runned
    if line[0] == "~":
        line = line[1:]
        runned.append(line)
    
    for v in var:
        if "$"+v+"$" in line:
            line = line.replace("$"+v+"$",str(var[v]))
    if line[0] == "(" and line[-1] == ")":
        try:
            if line.split("|")[0][1:] == line.split("|")[1][:-1]:
                return "nextline"
        except IndexError:
            try:
                if not int(line.split("%")[0][1:]) % int(line.split("%")[1][:-1]) == 0:
                    return "nextline"
            except:
                if line[1:-1] == "" or line[1:-1] == False or line[1:-1] == None:
                    return "nextline"

    if line[0] == "#":
        try:
            Sline = line.split(".")
            vn = Sline[0][1:]
            vv = Sline[1]
            if vv == "*":
                var[vn] = input()
            else:
                var[vn] = vv.replace("_"," ")
        except:
            try:
                Pline = line.split("+")
                vn = Pline[0][1:]
                vv = Pline[1]
                var[vn] = int(var[vn]) + int(vv)
            except:
                try:
                    Mline = line.split("-")
                    vn = Mline[0][1:]
                    vv = Mline[1]
                    var[vn] = int(var[vn]) - int(vv)
                except:
                    error("Error. Shit.")

    if line[0] == ">":
        line = line.replace("_"," ")
        if line[-1] == "*":
            print(line[1:-1],end="")
        else:
            print(line[1:])

    if line == "!":
        return "nextline"

    if line == "end":
        return "end"

LN = 0
LC = 0

runned = []
run = True
while run:
    file = open(filename)
    for line in file:
        LN += 1
        LC = 0
        line = line.strip()
        if line != "" and line[0] != commentsymbol:
            for L in shlex.split(line):
                LC += 1
                if not L[1:] in runned:
                    ret = parser(L)
                    if ret == "nextline":
                        break
                    elif ret == "end":
                        run = False
            continue
        else:
            continue

print("\n\n"+str(var))
