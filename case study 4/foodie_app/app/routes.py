from flask import request,jsonify

restaurants={}

next_id=1

def register_routes(app):
    
    @app.route("/api/v1/restaurants",methods=["POST"])
    def add_restaurant():
        global next_id
    
        data=request.get_json(force=True)

        if not data or "name" not in data:
            return jsonify({"message":"invalid data"})
        restaurant={
            "id":next_id,
            "name":data["name"],
            "category":data.get("category"),
            "location":data.get("location")
        }
        restaurants[next_id]=restaurant
        next_id+=1
        return jsonify(restaurant),201
    
    @app.route("/api/v1/restaurants",methods=["GET"])
    def show_all_restaurants():
        return jsonify(list(restaurants.values())),200
    
    @app.route("/api/v1/restaurants/<int:r_id>",methods=['GET'])
    def get_restaurant(r_id):
        restaurant=restaurants.get(r_id)
        if not restaurant:
            return jsonify({"error":"restaurant not found"}),404
        return jsonify(restaurant),200
    
    @app.route("/api/v1/restaurants/<int:r_id>",methods=["PUT"])
    def update_restaurant(r_id):
        restaurant=restaurants.get(r_id)
        if not restaurant:
            return jsonify({"error":"restaurant not found"}),404
        data=request.get_json(force=True)
        if not data:
            return jsonify({"error": "Request must be JSON"}), 415
        
        restaurant["name"]=data.get("name",restaurant["name"])
        restaurant["category"]=data.get("category",restaurant.get("category"))#this is a bit confusing but it jsut takes both new and old values if new value exists replace if not jsut continue with old value
        restaurant["location"]=data.get("location",restaurant.get("location"))

        return jsonify(restaurant),200
    