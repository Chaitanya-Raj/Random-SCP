import webbrowser
import random

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
