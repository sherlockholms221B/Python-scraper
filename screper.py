import pandas as pd
url = 'https://mobiletvshows.net/subfolder-Arrow.htm'
data_frame = pd.read_html('https://en.wikipedia.org/wiki/List_of_Arrow_episodes')
print(data_frame[2])
''