from aip import AipFace

""" 你的 APPID AK SK """

APP_ID = '23496008'
API_KEY = '1APyzZ0nRBGuNt26M8psqnD4'
SECRET_KEY = 'ns0Q5LkpDakGCRXIa2vwKttxuvduYtHU'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)


def face_register(image,user_id,image_type='BASE64',group_id='user'):
    res=client.addUser(image,user_id,image_type,group_id)
    print(res)
    if res['error_code']:
        return False
    return True