# analysis citations

filepath = r'\\campus.eur.nl\shared\departments\ESE-FD-BB-ONDERZOEK\Pieter_Vreeburg\1_Project_support\Research_morning_2016\WoS_concat_source_citations.txt'
file = open(filepath).read().splitlines()

cites = [int(line.split('\t')[31]) for line in file]
cites.sort(reverse = True)
total_cites = sum(cites)
total_publ = len(cites)
rtotal_cites = 0
rtotal_publ = 0
for cite in cites:
    rtotal_publ += 1
    rtotal_cites = rtotal_cites + cite
    if rtotal_cites > total_cites/2:
        break

print 'Total publications', total_publ
print 'Total cites:', total_cites
print '# publ for 50% of citations:', rtotal_publ