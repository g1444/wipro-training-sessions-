from flask import Flask,request,jsonify

app=Flask(__name__)

users=[{"id":1,"name":"gowtham"},{"id": 2,"name":"harsha"}]

@app.route("/",methods=["GET"])

def home():
    return "this is my get method one "
@app.route("/users",methods=["GET"])
def get_users():
    return jsonify(users)
@app.route("/users/<int:user_id>",methods=["GET"])
def get_user_by_id(user_id):
    for user in users:
        if user["id"]==user_id:
            return jsonify(user)
    return jsonify({"message":"user not found"}),404

@app.route("/users",methods=["POST"])
def post_user():
    data=request.json
    new_user={"id":len(users)+1,"name":data.get("name")}
    users.append(new_user)
    return jsonify(new_user),201
@app.route("/users/<int:user_id>", methods=['PUT'])
def put_user(user_id):
    data=request.json
    for user in users:
        if user["id"]==user_id:
            user['name']=data.get("name")
            return jsonify(user),200
    return jsonify({"message": "user not found"}),404
@app.route("/users/<int:user_id>",methods=["PATCH"])
def update_user(user_id):
    data=request.json
    for u in users:
        if u['id']==user_id:
            u.update(data)
            return jsonify(u),200
    return jsonify({"message":"user not found"}),404
@app.route("/users/<int:user_id>",methods=["DELETE"])
def delete_user(user_id):
    for u in users:
        if u["id"]==user_id:
            users.remove(u)
            return jsonify({"message":"user removed"}),201
        
    return jsonify({"message": "user not found"}),404
if __name__=="__main__":
    app.run(port=5000,debug=True)