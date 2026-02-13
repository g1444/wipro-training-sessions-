import pytest,requests

base_url="http://127.0.0.1:5000"


# -------------getting all movies test------------
def test_get_movies():
    r=requests.get(base_url)
    print(r.json())
    assert r.status_code==200
# ------------------------------------------------

# --------------getting movie by id test----------
movie_url=base_url+"/movies/1"
def test_get_movie_by_id():
    r=requests.get(movie_url)
    print(r.json())
    assert r.status_code==200
# ------------------------------------------------
# posting new movie test
post_url=base_url+"/movies"
def test_post_new_movie():
    post_body={
        "movie_name":"your name",
        "language":"japanese",
        "duration":"1 hr 48 m",
        "price":220
               }
    r=requests.post(post_url,json=post_body)
    print(r.json())
    assert r.status_code==201

# booking test
booking_url=base_url+"/bookings"
def test_booking():
    booking_body={
        "movie_id":2,
        "tickets":2,
        "customer":"gowtham"
    }
    r=requests.post(booking_url,json=booking_body)
    print(r.json())
    assert r.status_code==201