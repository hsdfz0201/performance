from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import json
import time

#f1 = open("performance.txt", "wb")
#f2 = open("performance_entries.txt","wb")
print "Start : %s" % time.ctime()
display = Display(visible=0, size=(800, 600))
display.start()
browser = webdriver.Firefox() # Get local session of firefox
print("http://www.taobao.com")
while True:
    browser.get("http://www.taobao.com") # Load page
    time.sleep( 5 )
    x = browser.execute_script("return window.performance.timing")
    y = browser.execute_script("return window.performance.getEntries()") 
    t = time.ctime()
    pageloadtime = x["loadEventStart"] - x["navigationStart"]  
    dns = x["domainLookupEnd"] - x["domainLookupStart"]  
    tcp = x["connectEnd"] - x["connectStart"]  
    ttfb = x["responseStart"] - x["navigationStart"]
    print('\n')
    print("time : %s" % t)
    print("pageloadtime = %2f ms"%(pageloadtime))
    print("dns = %2f ms"%(dns))
    print("tcp = %2f ms"%(tcp))
    print("ttfb = %2f ms"%(ttfb))  
    
    for i in y:
        print y.index(i)
        print i["name"]
        print i["duration"]
        
    #f1.write(str(t))
    #f1.write(str(x))
 
    #f2.write(str(t))
    #f2.write(str(y))

#f1.close()
#f2.close()
browser.quit()
