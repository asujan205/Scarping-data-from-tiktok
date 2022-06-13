from TikTokApi import TikTokApi
import pandas as pd
api = TikTokApi()
def userIdInfo():
     userName = input("Enter Username: ")
     userInfo = api.user(userName)
     return userInfo.as_dict
userIdInfo()