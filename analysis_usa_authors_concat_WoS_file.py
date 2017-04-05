# analysis usa-authors

filepath = r'\\campus.eur.nl\shared\departments\ESE-FD-BB-ONDERZOEK\Pieter_Vreeburg\1_Project_support\Research_morning_2016\WoS_concat_source_usa_authors.txt'
file = open(filepath).read().splitlines()

total_pub = 0
total_usa = 0
total_usa_oth = 0
total_oth = 0

for line in file:
    cnt_usa = 0
    cnt_oth = 0
    total_pub += 1
    auths = line.split('\t')[22].lower().split('; [')
    for auth in auths:
        if 'usa' in auth:
            cnt_usa += 1
        else:
            cnt_oth += 1
    if cnt_usa >= 1 and cnt_oth == 0:
        total_usa += 1
    elif cnt_usa >= 1 and cnt_oth >= 1:
        total_usa_oth += 1
    else:
        total_oth += 1
    
print 'Total publ:', total_pub
print '# publ with only USA authors:', total_usa
print '% publ with only USA authors:', round(float(total_usa)/float(total_pub)*100,2)
print '# publ with at least 1 USA author:', total_usa_oth
print '# publ with no USA authors:', total_oth



    
