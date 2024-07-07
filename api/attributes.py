import requests
import base64
import cv2 as cv


# opencv 图片
def car_att(img):
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/car"
    # 车型识别
    _, encoded_image = cv.imencode('.jpg', img)
    base64_image = base64.b64encode(encoded_image)
    params = {"image":base64_image}
    access_token = '24.f75792c48fa7edc89286af0746aab238.2592000.1722478226.282335-89935675'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)

    num = 0
    if response:
        # print("车辆属性识别成功返回")
        data = response.json()
        first_result = data['result'][0]['name']
        # print(first_result)
    return first_result
    # # 等待按键，然后关闭窗口
    cv.waitKey(0)
    cv.destroyAllWindows()
