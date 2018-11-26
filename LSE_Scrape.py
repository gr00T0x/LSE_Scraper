import urllib.request
import re
# Import both libraries needed. re for regular expression and urllib.request for requesting and opening the url.

url = 'http://www.londonstockexchange.com/exchange/prices-and-markets/stocks/indices/summary/summary-indices.html?index=UKX'
# create a variable called url which contains the website I need to request data from.
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
# this piece of code elimates the http 403 error or any other errors by tricking the website into thinking I am requesting access to there page from Mozilla Firefox.

def main():
#We define the code. This makes it easier to seperate the tasks so it looks cleaner and does not cause the two codes to mix or cause crashes
    resp = urllib.request.urlopen(req)
    # create the variable resp (response) which opens and loads the website to python
    respData = resp.read()
    # create a variable that reads all the data on the website
    headings = re.findall('abbr="(.*?)">',str(respData))
    figures = re.findall('(?:<td>|<td class="red">|<td class="green">|<td class="black">)(.*?)(?:<.td>|<)',str(respData))
    # Create regex functions for all the headings and figures in the table and then convert to a string so we can print it without getting erros
    table = headings[0:6], figures
    #create a variable (table) that includes both regex functions and slice first regex to prevent excess data being printed
    print('FTSE 100 SUMMARY')
    # prints above second print to get desired output stated in the brief
    col_width = max(len(word) for row in table for word in row) + 2  # padding
    for row in table:
        print("".join(word.ljust(col_width) for word in row))
    # These 3 lines format the regex functions and all the data inside of them into a table removing all the commas and apostrophes after each word
main()

#NOTE - When  inputting your desired indices please be aware it is case and space sensitive. 

#To avoid getting an error message, keep the input name the same as it is on the LSE website.
lse = 'http://www.londonstockexchange.com/exchange/prices-and-markets/stocks/indices/ftse-indices.html'
# create a variable called lse which contains the website with all the indices which I need to request data from.
req1 = urllib.request.Request(lse, headers={'User-Agent': 'Mozilla/5.0'})
# this piece of code elimates the http 403 error or any other errors by tricking the website into thinking I am requesting access to there page from Mozilla Firefox.
def indices():
#We define the code. This is important when writing if statements as it limits errors and keeps all your code together so you can call back to previous variables
    resp = urllib.request.urlopen(req1)
    respData = resp.read()
    headings2 = re.findall('<th scope="col"(.*?)<.th>',str(respData))
    figures2 =  re.findall('(?:<td>|<td class="red">|<td class="green">|<td class="black">)(.*?)(?:<.td>|<)',str(respData))
# create two regex functions which find every single index heading and figure

    
    ftse100 = headings2[1:7], figures2[0:6]
    #create a variable which combines the two regex functions and slice them so it only displays the first tables data
    col_width = max(len(word) for row in ftse100 for word in row) + 2  # padding
    for row in ftse100:
        ftse100 = ("".join(word.ljust(col_width) for word in row))
    # These 3 lines format the regex functions and all the data inside of them into a table removing all the commas and apostrophes after each word   

    ftse250 = headings2[1:7], figures2[6:12]
    col_width = max(len(word) for row in ftse250 for word in row) + 2  # padding
    for row in ftse250:
        ftse250 = ("".join(word.ljust(col_width) for word in row))
        

    ftse350 = headings2[1:7], figures2[12:18]
    col_width = max(len(word) for row in ftse350 for word in row) + 2  # padding
    for row in ftse350:
        ftse350 = ("".join(word.ljust(col_width) for word in row))
   
    ftseallshare = headings2[1:7], figures2[18:24]
    col_width = max(len(word) for row in ftseallshare for word in row) + 2  # padding
    for row in ftseallshare:
        ftseallshare = ("".join(word.ljust(col_width) for word in row))
   
    ftse50 = headings2[1:7], figures2[24:30]
    col_width = max(len(word) for row in ftse50 for word in row) + 2  # padding
    for row in ftse50:
        ftse50 = ("".join(word.ljust(col_width) for word in row))

    ftseaim100 = headings2[1:7], figures2[30:36]
    col_width = max(len(word) for row in ftseaim100 for word in row) + 2  # padding
    for row in ftseaim100:
        ftseaim100 = ("".join(word.ljust(col_width) for word in row))

    ftseaimallshare = headings2[1:7], figures2[36:42]
    col_width = max(len(word) for row in ftseaimallshare for word in row) + 2  # padding
    for row in ftseaimallshare:
        ftseaimallshare= ("".join(word.ljust(col_width) for word in row))
        
    ftsemid250 = headings2[9:13], figures2[42:46]
    col_width = max(len(word) for row in ftsemid250 for word in row) + 2  # padding
    for row in ftsemid250:
        ftsemid250 = ("".join(word.ljust(col_width) for word in row))
        
    ftse350highyield = headings2[9:13], figures2[46:50]
    col_width = max(len(word) for row in ftse350highyield for word in row) + 2  # padding
    for row in ftse350highyield:
        ftse350highyield = ("".join(word.ljust(col_width) for word in row))

    ftse350lowyield = headings2[9:13], figures2[50:54]
    col_width = max(len(word) for row in ftse350lowyield for word in row) + 2  # padding
    for row in ftse350lowyield:
        ftse350lowyield = ("".join(word.ljust(col_width) for word in row))

    ftse350exit = headings2[9:13], figures2[54:58]
    col_width = max(len(word) for row in ftse350exit for word in row) + 2  # padding
    for row in ftse350exit:
        ftse350exit = ("".join(word.ljust(col_width) for word in row))

    ftseallshareexit = headings2[9:13], figures2[58:62]
    col_width = max(len(word) for row in ftseallshareexit for word in row) + 2  # padding
    for row in ftseallshareexit:
        ftseallshareexit = ("".join(word.ljust(col_width) for word in row))
        
    ftsefocus = headings2[9:13], figures2[62:66]
    col_width = max(len(word) for row in ftsefocus for word in row) + 2  # padding
    for row in ftsefocus:
        ftsefocus = ("".join(word.ljust(col_width) for word in row))

    ftsemediscience = headings2[9:13], figures2[66:70]
    col_width = max(len(word) for row in ftsemediscience for word in row) + 2  # padding
    for row in ftsemediscience:
        ftsemediscience = ("".join(word.ljust(col_width) for word in row))

    ftsetechshare = headings2[9:13], figures2[70:74]
    col_width = max(len(word) for row in ftsetechshare for word in row) + 2  # padding
    for row in ftsetechshare:
        ftsetechshare = ("".join(word.ljust(col_width) for word in row))

    ftsesmallcap = headings2[9:13], figures2[74:78]
    col_width = max(len(word) for row in ftsesmallcap for word in row) + 2  # padding
    for row in ftsesmallcap:
        ftsesmallcap = ("".join(word.ljust(col_width) for word in row))
        
    ftseeurotop = headings2[9:13], figures2[78:82]
    col_width = max(len(word) for row in ftseeurotop for word in row) + 2  # padding
    for row in ftseeurotop:
        ftseeurotop = ("".join(word.ljust(col_width) for word in row))
        
    ftseorbindex = headings2[9:13], figures2[82:86]
    col_width = max(len(word) for row in ftseorbindex for word in row) + 2  # padding
    for row in ftseorbindex:
        ftseorbindex = ("".join(word.ljust(col_width) for word in row))
        
    ftseorbfinancial = headings2[9:13], figures2[86:90]
    col_width = max(len(word) for row in ftseorbfinancial for word in row) + 2  # padding
    for row in ftseorbfinancial:
        ftseorbfinancial = ("".join(word.ljust(col_width) for word in row))
        
    ftseorbnonfinancial = headings2[9:13], figures2[90:94]
    col_width = max(len(word) for row in ftseorbnonfinancial for word in row) + 2  # padding
    for row in ftseorbnonfinancial:
        ftseorbnonfinancial = ("".join(word.ljust(col_width) for word in row))
        
    ftseorbunder = headings2[9:13], figures2[94:98]
    col_width = max(len(word) for row in ftseorbunder for word in row) + 2  # padding
    for row in ftseorbunder:
        ftseorbunder = ("".join(word.ljust(col_width) for word in row))
        
    ftseorbover = headings2[9:13], figures2[98:102]
    col_width = max(len(word) for row in ftseorbover for word in row) + 2  # padding
    for row in ftseorbover:
        ftseorbover = ("".join(word.ljust(col_width) for word in row))
        
    ftseenv = headings2[1:7], figures2[102:108]
    col_width = max(len(word) for row in ftseenv for word in row) + 2  # padding
    for row in ftseenv:
        ftseenv = ("".join(word.ljust(col_width) for word in row))
        
    ftseeu = headings2[1:7], figures2[108:114]
    col_width = max(len(word) for row in ftseeu for word in row) + 2  # padding
    for row in ftseeu:
        ftseeu = ("".join(word.ljust(col_width) for word in row))
        
    ftseglobal = headings2[1:7], figures2[114:120]
    col_width = max(len(word) for row in ftseglobal for word in row) + 2  # padding
    for row in ftseglobal:
        ftseglobal = ("".join(word.ljust(col_width) for word in row))
        
    ftseusa = headings2[1:7], figures2[120:126]
    col_width = max(len(word) for row in ftseusa for word in row) + 2  # padding
    for row in ftseusa:
        ftseusa = ("".join(word.ljust(col_width) for word in row))
        
    ftseuk = headings2[1:7], figures2[126:132]
    col_width = max(len(word) for row in ftseuk for word in row) + 2  # padding
    for row in ftseuk:
        ftseuk = ("".join(word.ljust(col_width) for word in row))


    user = input('Enter an index:')
    # create an input function which briefs the user to enter an index
    if user in ('FTSE100', 'FTSE 100' ):
        print ('FTSE 100 SUMMARY')
        print ('Value         +/-         %+/-         High         Low          Prev Close  ')
        print (ftse100)
    # IF statement which says if a user enters ftse 100 in either format to print the strings and regexes
        
    elif user in ('FTSE250', 'FTSE 250'):
    #elif function allows us to have another option (index) for users to input 
        print ('FTSE 250 SUMMARY')
        print ('Value         +/-         %+/-         High         Low          Prev Close  ')
        print (ftse250)
        
    elif user in ('FTSE350', 'FTSE 350'):
        print ('FTSE 350 SUMMARY')
        print ('Value         +/-         %+/-         High         Low          Prev Close  ')
        print (ftse350)
        
    elif user in ('FTSE All-Share', 'FTSEAll-Share', 'FTSE All Share'):
        print ('FTSE ALL-SHARE SUMMARY')
        print ('Value         +/-         %+/-         High         Low          Prev Close  ')
        print (ftseallshare)
        
    elif user in ('FTSE AIM UK 50', 'FTSEAIMUK50'):
        print ('FTSE AIM UK 50 SUMMARY')
        print ('Value         +/-         %+/-         High         Low          Prev Close  ')
        print (ftse50)
        
    elif user in ('FTSEAIM100', 'FTSE AIM 100'):
        print ('FTSE AIM 100 SUMMARY')
        print ('Value         +/-         %+/-         High         Low          Prev Close  ')
        print (ftseaim100)
        
    elif user in ('FTSE AIM All-Share', 'FTSEAIMAll-Share', 'FTSE AIM All Share'):
        print ('FTSE AIM ALL-SHARE SUMMARY')
        print ('Value         +/-         %+/-         High         Low          Prev Close  ')
        print (ftseaimallshare)
        
    elif user in ('FTSEMID250', 'FTSE MID 250', 'FTSEMID250(ex IT)', 'FTSE MID 250 (ex IT)'):
        print ('FTSE MID 250 (exIT) SUMMARY')
        print ('Prev Close   Value         +/-         %+/-    ')
        print (ftsemid250)
        
    elif user in ('FTSE 350 High Yield', 'FTSE350HighYield'):
        print ('FTSE 350 High Yield SUMMARY')
        print ('Prev Close   Value         +/-         %+/-    ')
        print (ftse350highyield)
        
    elif user in ('FTSE 350 Low Yield', 'FTSE350LowYield'):
        print ('FTSE 350 Low Yield SUMMARY')
        print ('Prev Close   Value         +/-         %+/-    ')
        print (ftse350lowyield)
        
    elif user in ('FTSE350EXIT', 'FTSE 350 EX IT', 'FTSE 350 (ex IT)', 'FTSE350(ex IT)'):
        print ('FTSE 350 (ex IT) SUMMARY')
        print ('Prev Close   Value         +/-         %+/-    ')
        print (ftse350exit)
        
    elif user in ('FTSEALLSHAREEXIT', 'FTSE ALL SHARE EX IT', 'FTSE All-Share (ex IT)', 'FTSEAll-Share(ex IT)' ):
        print ('FTSE All-Share (ex IT) SUMMARY')
        print ('Prev Close   Value         +/-         %+/-    ')
        print (ftseallshareexit)
        
    elif user in ('FTSETECHMARKFOCUS',  'FTSE TECH MARK FOCUS', 'FTSE techMARK Focus', 'FTSEtechMARKFocus'):
        print ('FTSE techMARK Focus SUMMARY')
        print ('Value         +/-          %+/-        Prev Close    ')
        print (ftsefocus)
        
    elif user in ('FTSETECHMARKMEDISCIENCE', 'FTSE TECH MARK MEDISCIENCE', 'FTSE techMARK mediscience', 'FTSEtechMARKmediscience'):
        print ('FTSE techMARK mediscience SUMMARY')
        print ('Value         +/-          %+/-        Prev Close    ')
        print (ftsemediscience)
        
    elif user in ('FTSEtechMARKAll-Share', 'FTSE techMARK All-Share'):
        print ('FTSE techMARK All-Share SUMMARY')
        print ('Value         +/-          %+/-        Prev Close    ')
        print (ftsetechshare)
        
    elif user in ('FTSESmallCap', 'FTSE SmallCap'):
        print ('FTSE SmallCap SUMMARY')
        print ('Value         +/-          %+/-        Prev Close    ')
        print (ftsesmallcap)
        
    elif user in ('FTSEEurotop300', 'FTSE Eurotop 300'):
        print ('FTSE Eurotop 300 SUMMARY')
        print ('Value         +/-          %+/-        Prev Close    ')
        print (ftseeurotop)
        
    elif user in ('FTSEORBIndex', 'FTSE ORB Index'):
        print ('FTSE ORB Index SUMMARY')
        print ('Value         +/-          %+/-        Prev Close    ')
        print (ftseorbindex)
        
    elif user in ('FTSEORBFinancialsIndex', 'FTSE ORB Financials Index'):
        print ('FTSE ORB Financials Index SUMMARY')
        print ('Value         +/-          %+/-        Prev Close    ')
        print (ftseorbfinancial)
        
    elif user in ('FTSEORBNon-FinancialsIndex', 'FTSE ORB Non-Financials Index'):
        print ('FTSE ORB Non-Financials Index SUMMARY')
        print ('Value         +/-          %+/-        Prev Close    ')
        print (ftseorbnonfinancial)
        
    elif user in ('FTSEORBunder5yuntilmaturityIndex', 'FTSE ORB under 5y until maturity Index', 'FTSEORBUNDER', 'FTSE ORB UNDER'):
        print ('FTSE ORB under 5y until maturity Index SUMMARY')
        print ('Value         +/-          %+/-        Prev Close    ')
        print (ftseorbunder)
        
    elif user in ('FTSEORBover5yuntilmaturityIndex', 'FTSE ORB over 5y until maturity Index', 'FTSEORBOVER', 'FTSE ORB OVER'):
        print ('FTSE ORB over 5y until maturity Index SUMMARY')
        print ('Value         +/-          %+/-        Prev Close    ')
        print (ftseorbover)
        
    elif user in ('FTSE4Good Env.Lead.Euro40', 'FTSE4GoodEnv.Lead.Euro40', 'FTSE4Good EnvLeadEuro40', 'FTSE4Good Env Lead Euro40'):
        print ('FTSE4Good Env.Lead.Euro40 SUMMARY')
        print ('Value         +/-         %+/-         High         Low          Prev Close  ')
        print (ftseenv)
        
    elif user in ('FTSE4Good Europe', 'FTSE4GoodEurope'):
        print ('FTSE4Good Europe SUMMARY')
        print ('Value         +/-         %+/-         High         Low          Prev Close  ')
        print (ftseeu)
        
    elif user in ('FTSE4Good Global', 'FTSE4GoodGlobal'):
        print ('FTSE4Good Global SUMMARY')
        print ('Value         +/-         %+/-         High         Low          Prev Close  ')
        print (ftseglobal)
        
    elif user in ('FTSE4Good USA', 'FTSE4GoodUSA'):
        print ('FTSE4Good USA SUMMARY')
        print ('Value         +/-         %+/-         High         Low          Prev Close  ')
        print (ftseusa)
        
    elif user in ('FTSE4Good UK', 'FTSE4GoodUK'):
        print ('FTSE4Good UK SUMMARY')
        print ('Value         +/-         %+/-         High         Low          Prev Close  ')
        print (ftseuk)
        
    else :
        print ('ERROR. You have selected an index that does not exist. Please restart the program and try again.')
# The else function is used to alert users if they type anything that is not part of the strings above with the elif functions it will print an error explaining why.
indices()
