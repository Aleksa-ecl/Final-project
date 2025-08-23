# Молдован Александра, 33-я когорта — Финальный проект. Инженер по тестированию расширенный 
import sender_stand_request
import data


def test_track_order():
    # Запрос на создание заказа
    create_order_response = sender_stand_request.create_order(data.create_order_body)
    
    # Проверка, что заказ создался успешно
    assert create_order_response.status_code == 201
    
    # Сохранить номер трека заказа
    track_number = create_order_response.json()["track"]
    
    # Запрос на получение заказа по треку заказа
    get_order_response = sender_stand_request.get_track_order(track_number)
    
    # Проверка, что код ответа равен 200
    assert get_order_response.status_code == 200
