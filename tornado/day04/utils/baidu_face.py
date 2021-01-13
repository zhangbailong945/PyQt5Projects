from aip import AipFace

""" 你的 APPID AK SK """

APP_ID = '23496008'
API_KEY = '1APyzZ0nRBGuNt26M8psqnD4'
SECRET_KEY = 'ns0Q5LkpDakGCRXIa2vwKttxuvduYtHU'
import base64

client = AipFace(APP_ID, API_KEY, SECRET_KEY)


def face_register(image,imageType,groupId,userId):
    res=client.addUser(image,imageType,groupId,userId)
    print(res)
    if res['error_code']:
        return False
    return True

def face_search(image,imageType,groupIdList):
    res=client.search(image,imageType,groupIdList)
    if res['error_code']:
        return False
    return True

