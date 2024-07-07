import json

import requests
import base64
import cv2 as cv


# opencv 图片
def vehicle_detect(img):
    # print("調用车辆检测")
    # 获取access_token的请求
    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=W2HoHrrI8awgsyqEB9jBQodt&client_secret=Ull2pWTXbTd47Nn54B9pPNdUdc7UO2Ew"
    payload = ""
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    # print(response.text)
    response_dict = json.loads(response.text)  # 将响应文本转换为字典
    access_token = response_dict["access_token"]  # 提取access_token
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/vehicle_detect"
    _, encoded_image = cv.imencode('.jpg', img)
    base64_image = base64.b64encode(encoded_image)
    params = {"image":base64_image}

    # access_token = '24.f75792c48fa7edc89286af0746aab238.2592000.1722478226.282335-89935675'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)

    num = 0
    if response:
        # print("车辆检测成功返回")
        data = response.json()
        num = data['vehicle_num']['car']
        # for item in data['vehicle_info']:
        #     location = item['location']
        #     x1 = location['left']
        #     y1 = location['top']
        #     x2 = x1 + location['width']
        #     y2 = y1 + location['height']
        #     cv.rectangle(img,(x1,y1),(x2,y2),(0,0,255),2)
        # # 定义要绘制的文字
        #     text = item['type']
        #     position = (x1, y1-2)
        #     font = cv.FONT_HERSHEY_SIMPLEX
        #     font_scale = 1
        #     color = (0, 0, 255)  # 红色
        #     thickness = 2
        #     img = cv.putText(img, text, position, font, font_scale, color, thickness, cv.LINE_AA)
            # cv.imshow('Rectangle', img)
            # return img
    return num
    # return img, num
    # return num
    # 等待按键，然后关闭窗口
    cv.waitKey(0)
    cv.destroyAllWindows()

