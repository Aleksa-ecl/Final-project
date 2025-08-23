import configuration
import requests
import data


def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body,
                         headers=data.headers)


response = post_new_order(data.create_order_body)
track = response.json()["track"]

def create_order(body):
    #Функция для создания заказа
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                        json=body,
                        headers={"Content-Type":"application/json"})

def get_track_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.TRACK_ORDER, params={"t": track} )
