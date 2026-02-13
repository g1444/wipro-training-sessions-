from flask import Flask, request, jsonify

app = Flask(__name__)

restaurants = {}
dishes = {}
users = {}
orders = {}
ratings = {}

next_restaurant_id = 1
next_dish_id = 1
next_user_id = 1
next_order_id = 1
next_rating_id = 1


# ---------------- RESTAURANT MODULE ----------------

@app.route("/api/v1/restaurants", methods=["POST"])
def register_restaurant():
    global next_restaurant_id

    data = request.json
    if not data or "name" not in data:
        return jsonify({"error": "Invalid data"}), 400

    for r in restaurants.values():
        if r["name"] == data["name"]:
            return jsonify({"error": "Restaurant already exists"}), 409

    restaurant = {
        "id": next_restaurant_id,
        "name": data["name"],
        "category": data.get("category"),
        "location": data.get("location"),
        "images": data.get("images"),
        "contact": data.get("contact"),
        "enabled": True,
        "approved": False
    }

    restaurants[next_restaurant_id] = restaurant
    next_restaurant_id += 1

    return jsonify(restaurant), 201


@app.route("/api/v1/restaurants/<int:r_id>", methods=["PUT"])
def update_restaurant(r_id):
    restaurant = restaurants.get(r_id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    data = request.json
    restaurant["name"] = data.get("name", restaurant["name"])
    restaurant["category"] = data.get("category", restaurant.get("category"))
    restaurant["location"] = data.get("location", restaurant.get("location"))

    return jsonify(restaurant), 200


@app.route("/api/v1/restaurants/<int:r_id>/disable", methods=["PUT"])
def disable_restaurant(r_id):
    restaurant = restaurants.get(r_id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    restaurant["enabled"] = False
    return jsonify({"message": "Restaurant disabled"}), 200


@app.route("/api/v1/restaurants/<int:r_id>", methods=["GET"])
def view_restaurant(r_id):
    restaurant = restaurants.get(r_id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404
    return jsonify(restaurant), 200


# ---------------- DISH MODULE ----------------

@app.route("/api/v1/restaurants/<int:r_id>/dishes", methods=["POST"])
def add_dish(r_id):
    global next_dish_id

    if r_id not in restaurants:
        return jsonify({"error": "Restaurant not found"}), 404

    data = request.json
    if not data or "name" not in data or "price" not in data:
        return jsonify({"error": "Invalid dish data"}), 400

    dish = {
        "id": next_dish_id,
        "restaurant_id": r_id,
        "name": data["name"],
        "type": data.get("type"),
        "price": data["price"],
        "enabled": True
    }

    dishes[next_dish_id] = dish
    next_dish_id += 1

    return jsonify(dish), 201


@app.route("/api/v1/dishes/<int:d_id>", methods=["PUT"])
def update_dish(d_id):
    dish = dishes.get(d_id)
    if not dish:
        return jsonify({"error": "Dish not found"}), 404

    data = request.json
    dish["name"] = data.get("name", dish["name"])
    dish["price"] = data.get("price", dish["price"])

    return jsonify(dish), 200


@app.route("/api/v1/dishes/<int:d_id>/status", methods=["PUT"])
def dish_status(d_id):
    dish = dishes.get(d_id)
    if not dish:
        return jsonify({"error": "Dish not found"}), 404

    data = request.json
    dish["enabled"] = data.get("enabled", True)

    return jsonify({"message": "Dish status updated"}), 200


@app.route("/api/v1/dishes/<int:d_id>", methods=["DELETE"])
def delete_dish(d_id):
    if d_id not in dishes:
        return jsonify({"error": "Dish not found"}), 404

    del dishes[d_id]
    return jsonify({"message": "Dish deleted"}), 200


# ---------------- ADMIN MODULE ----------------

@app.route("/api/v1/admin/restaurants/<int:r_id>/approve", methods=["PUT"])
def approve_restaurant(r_id):
    restaurant = restaurants.get(r_id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    restaurant["approved"] = True
    return jsonify({"message": "Restaurant approved"}), 200


@app.route("/api/v1/admin/restaurants/<int:r_id>/disable", methods=["PUT"])
def admin_disable_restaurant(r_id):
    restaurant = restaurants.get(r_id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    restaurant["enabled"] = False
    return jsonify({"message": "Restaurant disabled by admin"}), 200


@app.route("/api/v1/admin/feedback", methods=["GET"])
def view_feedback():
    return jsonify(list(ratings.values())), 200


@app.route("/api/v1/admin/orders", methods=["GET"])
def view_all_orders():
    return jsonify(list(orders.values())), 200


# ---------------- USER MODULE ----------------

@app.route("/api/v1/users/register", methods=["POST"])
def register_user():
    global next_user_id

    data = request.json
    if not data or "email" not in data:
        return jsonify({"error": "Invalid user"}), 400

    for u in users.values():
        if u["email"] == data["email"]:
            return jsonify({"error": "User exists"}), 409

    user = {
        "id": next_user_id,
        "name": data.get("name"),
        "email": data["email"]
    }

    users[next_user_id] = user
    next_user_id += 1

    return jsonify(user), 201


# ---------------- SEARCH ----------------

@app.route("/api/v1/restaurants/search", methods=["GET"])
def search_restaurants():
    name = request.args.get("name")
    location = request.args.get("location")

    results = []
    for r in restaurants.values():
        if name and name.lower() not in r["name"].lower():
            continue
        if location and location.lower() not in (r.get("location") or "").lower():
            continue
        results.append(r)

    return jsonify(results), 200


# ---------------- ORDER MODULE ----------------

@app.route("/api/v1/orders", methods=["POST"])
def place_order():
    global next_order_id

    data = request.json
    if not data:
        return jsonify({"error": "Invalid order"}), 400

    order = {
        "id": next_order_id,
        "user_id": data.get("user_id"),
        "restaurant_id": data.get("restaurant_id"),
        "dishes": data.get("dishes", []),
        "status": "PLACED"
    }

    orders[next_order_id] = order
    next_order_id += 1

    return jsonify(order), 201


@app.route("/api/v1/restaurants/<int:r_id>/orders", methods=["GET"])
def orders_by_restaurant(r_id):
    result = [o for o in orders.values() if o["restaurant_id"] == r_id]
    return jsonify(result), 200


@app.route("/api/v1/users/<int:u_id>/orders", methods=["GET"])
def orders_by_user(u_id):
    result = [o for o in orders.values() if o["user_id"] == u_id]
    return jsonify(result), 200


# ---------------- RATINGS ----------------

@app.route("/api/v1/ratings", methods=["POST"])
def give_rating():
    global next_rating_id

    data = request.json
    if not data or "order_id" not in data:
        return jsonify({"error": "Invalid rating"}), 400

    rating = {
        "id": next_rating_id,
        "order_id": data["order_id"],
        "rating": data.get("rating"),
        "comment": data.get("comment")
    }

    ratings[next_rating_id] = rating
    next_rating_id += 1

    return jsonify(rating), 201


if __name__ == "__main__":
    app.run(debug=True)