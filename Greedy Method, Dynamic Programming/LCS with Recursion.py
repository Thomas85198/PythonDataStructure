def simpleLCS(str1, str2):
    if len(str1) == 0 or len(str2) == 0:
        return 0
    else:
        if str1[-1] == str2[-1]:
            return 1 + simpleLCS(str1[0:-1], str2[0:-1])
        else:
            return max(simpleLCS(str1[0:-1], str2),
                       simpleLCS(str1, str2[0:-1]))


print(simpleLCS("ATAACGCGCTGCTCGGGT", "TCAATCAGGATCCGCTGA"))  # 11
