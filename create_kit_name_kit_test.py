import sender_stand_request
import data

def test_track_order():
    response = sender_stand_request.get_track_order()
    assert response.status_code == 200