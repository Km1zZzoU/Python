import wcwidth

def format_table(benchmarks, algos, results):
    
    if len(benchmarks)==len(results):
        for i in range(len(benchmarks)):
            if len(results[i])!=len(algos):
                return "error format table"

    firstelalgos = ["Benchmarks"]
    algos = firstelalgos+algos
    
    lenstr1 = 9 #len 'Benchmarks'
    for i in range(len(benchmarks)):
        lenstr1 = max(lenstr1, len(benchmarks[i]))
    
    
    maxlenstr = 0 
    for i in range(1, len(algos)):
        for j in range(len(benchmarks)+1):
            if j == 0:
                lenstr = len(algos[i])
            else:
                lenstr = max(lenstr, len(str(results[j-1][i-1])))
        maxlenstr=max(maxlenstr, lenstr)

    retStr= "| " + "Benchmark".ljust(lenstr1) + " |"
    for i in range(1, len(algos)):
        retStr += " " + algos[i].center(maxlenstr) + " |"
    fix = retStr
    retStr += "\n|" + "-" * (wcwidth.wcswidth(fix)-2) + "|"

    for i in range(len(benchmarks)):
        retStr += "\n| " + benchmarks[i].ljust(lenstr1) + " |"
        for j in range(len(results)+1):
            retStr += " " + str(results[i][j]).center(maxlenstr) + " |"
    
    return retStr    
    
print(format_table(["best case", "the worst case"],["quick sort", "merge sort", "bubble sort"],[[1.23, 1.56, 2.0], [3.3, 2.9, 3.9]]))
        
        
    
    
