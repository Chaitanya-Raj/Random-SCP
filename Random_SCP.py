import webbrowser
import random


''' Can open any scp article in the range 1 - 4999
    Just click on the file.
    It will run the code in the background
    and open a new tab with a random scp article in your default browser.
'''


x = random.randint(1, 5000)
if x < 10:
    url = f"http://www.scp-wiki.net/scp-00{str(x)}"
elif x >= 10 and x < 100:
    url = f"http://www.scp-wiki.net/scp-0{str(x)}"
elif x >= 100 and x < 1000:
    url = f"http://www.scp-wiki.net/scp-{str(x)}"
elif x >= 1000:
    url = f"http://www.scp-wiki.net/scp-{str(x)}"


webbrowser.open_new_tab(url)
