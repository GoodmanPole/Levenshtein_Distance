#Implementation of the Levenshtein Distance Algorithm
#The main part of the algorithm is using Dynamic Programming(DP)

def levenshteinDistance(s1,s2):
    m=[[0 for i in range(len(s2))] for j in range(len(s1))]


    for i in range(0,len(s1)):
        m[i][0]=i

    for j in range(0, len(s2)):
        m[0][j]=j

    print("Matrix before filling with Dynamic Programming (DP):")
    print(m,"\n")


    for i in range(1,len(s1)):
        for j in range(1,len(s2)):
            if s1[i]==s2[j]:
                m[i][j]=min(m[i-1][j]+1,m[i][j-1]+1,m[i-1][j-1])
            else:
                m[i][j] = min(m[i - 1][j] + 1, m[i][j - 1] + 1, m[i - 1][j - 1]+1)


    print("Matrix after it filled with Dynamic Programing (DP):")
    print(m,"\n")

    return m[len(s1)-1][len(s2)-1]


def test_bench():
    s1=input("Enter the original word: ")
    s2=input("Enter the goal word:")
    print("\n","This is the given word:",s1," ","This is goal word:",s2)
    print()
    print("The Levenshtein Distance(Edit Distance) of the given words is:",levenshteinDistance(s1,s2))


test_bench()