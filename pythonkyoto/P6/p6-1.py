tozai = ["三条", "四条", "五条"]
nanboku = ["堀川", "烏丸", "河原町"]
cross_table = []
for i in range(len(tozai)):
    cross = []
    for j in range(len(nanboku)):
        cross.append(tozai[i] + nanboku[j])
    cross_table.append(cross)
print(*cross_table, sep=", ")
