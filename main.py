import operator as op
from search import *
from personal_info import *

def common_member(streaming, existing):
    result = []
    for i in streaming:
        for j in existing:
            if i[0]==j[0]:
                if i[1]=="Subscription":
                    result.append(i)
                elif i[1]==j[1]:
                    result.append(i)

    return result

media_name = input("Enter name of movie or show: ")
if media_name!="":
    sites=find(media_name)

if sites==[]:
    print("\nNo such movie/show found. Check the spelling once more")
else:
    print("\nThe subscriptions available to watch are:")

    j = common_member(sites,existing_subscriptions)
    k = sites
    if len(j)>0:
        for i in j:
            print("\t",i[0])
            k.remove(i)
    else:
        print("No such subscription")

    if k!=[]:
        print("\nRemaining sites are:")
        for i in k:
            print("\t",i[0],"\t\t\t",i[1])