import  difflib

string1 ="goodboy"
string2 = "boigood"

def substringg(string1,string2):
    seq = difflib.SequenceMatcher(None, string1, string2)
    mat = seq.find_longest_match(0, len(string1),0,len(string2))
    if (mat.size!=0):
        return (string1[mat.a : mat.a+mat.size])
    else:
        return 0

substringg(string1,string2)
