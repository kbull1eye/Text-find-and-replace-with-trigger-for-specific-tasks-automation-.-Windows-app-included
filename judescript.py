import os
texttofinde = 'NUME'
texttoreplace = input("NUME:\n")
texttofinde1 = 'SERIE'
texttoreplace1 = input("SERIE:\n")
texttofinde2 = 'NR'
texttoreplace2 = input("NR:\n")

sourcepath = os.listdir('C:/Users/kbull/PycharmProjects/judetest/input')
for file in sourcepath:
    inputfile = 'C:/Users/kbull/PycharmProjects/judetest/input/'+ file
    print('Se prelucreaza documentul:' +inputfile)
    with open(inputfile,'r') as inputfile:
        filedata = inputfile.read()
        freq = 0
        freq = filedata.count(texttofinde)
    destinationpath = 'C:/Users/kbull/PycharmProjects/judetest/output/' + file
    filedata = filedata.replace(texttofinde,texttoreplace)
    filedata = filedata.replace(texttofinde1,texttoreplace1)
    filedata = filedata.replace(texttofinde2,texttoreplace2)
    with open(destinationpath,'w') as file:
        file.write(filedata)
    print ('Total %d Record Replaced' %freq)
