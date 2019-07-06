import webbrowser
import random

x = random.randint(1, 5000)
if x < 10:
    url = "http://www.scp-wiki.net/scp-00%s" % str(x)
elif x >= 10 < 100:
    url = "http://www.scp-wiki.net/scp-0%s" % str(x)
elif x >= 100 < 1000:
    url = "http://www.scp-wiki.net/scp-%s" % str(x)
elif x >= 1000:
    url = "http://www.scp-wiki.net/scp-%s" % str(x)

webbrowser.open_new_tab(url)
