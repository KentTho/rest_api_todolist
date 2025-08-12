from flask import Flask, request, Response, jsonify, Blueprint
blueprint = Blueprint('todo', __name__, url_prefix="/todo")
from model import Item, toDoList

# ==========================================
#  API lấy toàn bộ danh sách To-Do
# ==========================================
@blueprint.route("/list", methods=["GET"])
def get_all_todos():
    return jsonify(toDoList), 200


# ==========================================
#  API tạo mới một To-Do
# ==========================================
@blueprint.route("/", methods=["POST"])
def create_new_todo():
    data = request.get_json()  # Lấy dữ liệu từ request body
    item = Item(**data)        # Tạo Item từ dict
    toDoList.append(item.to_json())  # Lưu vào danh sách
    return jsonify({"message": "success"}), 201


# ==========================================
#  API lấy To-Do theo ID
# ==========================================
@blueprint.route("/<id>", methods=["GET"])
def find_todo_by_id(id):
    item_found = next((item for item in toDoList if item["id"] == id), None)
    if item_found:
        return jsonify(item_found), 200
    else:
        return jsonify({"message": "item not found"}), 404


# ==========================================
#  API cập nhật To-Do
# ==========================================
@blueprint.route("/", methods=["PUT"])
def update_todo():
    data = request.get_json()
    item = Item(**data)

    is_exist = False
    for i in toDoList:
        if i["id"] == item.id:
            i["title"] = item.title    # sửa từ '==' thành '='
            i["desc"] = item.desc
            is_exist = True
            break

    if is_exist:
        return jsonify({"message": "item updated successfully"}), 200
    else:
        return jsonify({"message": "item not exist"}), 404


# ==========================================
#  API xóa To-Do theo ID
# ==========================================
@blueprint.route("/<id>", methods=["DELETE"])
def delete_todo_by_id(id):
    item_to_delete = next((item for item in toDoList if item["id"] == id), None)

    if item_to_delete:
        toDoList.remove(item_to_delete)
        return jsonify({"message": "item removed successfully"}), 200
    else:
        return jsonify({"message": "item not exist"}), 404


