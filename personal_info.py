import csv
import browser_info

existing_subscriptions=[] #default value for now

sites =open('s_sites.csv', 'r+')

sites.seek(0)
reader=csv.reader(sites)
writer=csv.writer(sites)

browsing_choice=browser_info.browser_toggle()
for i in reader:
    existing_subscriptions.append(i)

def update():
    sites.seek(0)
    sites.truncate()
    writer.writerows(existing_subscriptions)

def add_subscription(s_sites, premium_or_no):
    add = [s_sites]
    if premium_or_no:
        add.append("Premium subscription")
    else:
        add.append("Subscription")
    existing_subscriptions.append(add)
    update()
    
def delete_subscription(s_sites):
    j=0
    for i in existing_subscriptions:
        if i[0]==s_sites:
            del existing_subscriptions[j]
            break
        j+=1
    update()

def update_subscription(s_sites, premium_or_no):
    for i in existing_subscriptions:
        if i[0]==s_sites:
            if premium_or_no:
                i[1]="Premium subscription"
            else:
                i[1]="Subscription"
    
    update()

#print(browsing_choice)
#print(existing_subscriptions)
