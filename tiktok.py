import requests, json, os
from TikTokAPI import TikTokAPI

user_name = 'foryou'  # username without the @
c = 1  # number of videos to download

api = TikTokAPI()
current_directory = os.getcwd()
final_directory = os.path.join(current_directory, r'{}'.format(user_name))
if not os.path.exists(final_directory):
   os.makedirs(final_directory)
user_obj = api.getVideosByUserName(user_name, count=c)
jsons = json.dumps(user_obj)
var = json.loads(jsons)
for i in range(c):
    print('{}-{}-{}'.format(i, var['items'][i]['id'], var['items'][i]['video']['downloadAddr']))
    url = var['items'][i]['video']['downloadAddr']
    r = requests.get(url, allow_redirects=True)
    name = '{}\\{}-{}.mp4'.format(user_name, user_name, i)
    open(name, 'wb').write(r.content)
