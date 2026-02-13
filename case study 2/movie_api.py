from flask import Flask,request,jsonify
app=Flask(__name__)

movies = [
    {
        "id": 1,
        "movie_name": "Interstellar",
        "language": "English",
        "duration": "2h 49m",
        "price": 250
    },
    {
        "id": 2,
        "movie_name": "Jailer",
        "language": "Tamil",
        "duration": "2h 35m",
        "price": 200
    }]

bookings=[]

# getting all movies
@app.route("/",methods=['GET'])
def get_movies():
    return jsonify(movies)

# getting movie by id
@app.route("/movies/<int:movie_id>",methods=['GET'])
def get_movie_by_id(movie_id):
    for movie in movies:
        if movie["id"]==movie_id:
            return jsonify(movie)
    return jsonify({"message":"movie not found"}),404
    
# posting the movie 
@app.route("/movies",methods=["POST"])
def post_new_movie():
    data=request.json
    if any(m["movie_name"] == data.get("movie_name") for m in movies):
        return jsonify({"message":"the movie already exists in our data"}),409
    new_movie={"id":len(movies)+1,"movie_name":data.get("movie_name"),"language":data.get("language"),"duration":data.get("duration"),"price":data.get("price")}
    movies.append(new_movie)
    return jsonify(new_movie),201
    
# put(edit existing movie details)
@app.route("/movies/<int:movie_id>",methods=['PUT'])
def edit_movie_details(movie_id):
    data=request.json
    for movie in movies:
        if movie["id"]==movie_id:
            movie["movie_name"]=data.get("movie_name")
            movie["language"]=data.get("language")
            movie["duration"]=data.get("duration")
            movie["price"]=data.get("price")
            return jsonify(movie),200
    return  jsonify({"message":"movie not found"}),404

# patch(can add new fields or replace existing fields)
@app.route("/movies/<int:movie_id>",methods=['PATCH'])
def add_new_details(movie_id):
    data=request.json
    for movie in movies:
        if movie["id"]==movie_id:
            movie.update(data)
            return jsonify(movie),200
    return  jsonify({"message":"movie not found"}),404
@app.route("/movies/<int:movie_id>",methods=["DELETE"])
def remove_movie(movie_id):
    for movie in movies:
        if movie["id"]==movie_id:
            movies.remove(movie)
            return jsonify({"message":"movie removed"}),200
    return jsonify({"message":"movie not found"}),404

@app.route("/bookings",methods=["POST"])
def book_tickets():
    data=request.json

    new_booking={"movie_id":data.get("movie_id"),"tickets":data.get("tickets"),"customer":data.get("customer")}
    for movie in movies:
        if movie["id"]==int(new_booking["movie_id"]):
        
            bookings.append(new_booking)
            return jsonify({"status":"Booking successful","booking":new_booking,"price":int(movie["price"]*new_booking["tickets"])}),201
    return jsonify({"message":"movie not found"}),404
if __name__=="__main__":
    app.run(port=5000,debug=True)