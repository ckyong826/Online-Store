from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt    
from models.usersModel import User, TokenBlocklist
from models.itemsModel import ItemsModel
from Schema import UserSchema, ItemsSchema

admin_bp = Blueprint("admin", __name__)

@admin_bp.get("/allusers")
@jwt_required()
def get_all_users():
    claims = get_jwt()

    if claims.get("is_staff") == True:
        users = User.query.paginate()

        result = UserSchema().dump(users, many=True)

        return (
            jsonify(
                {
                    "users": result,
                }
            ),
            200,
        )

    return jsonify({"message": "You are not authorized to access this"}), 401

@admin_bp.post("/additems")
@jwt_required()
def add_items():
    claims = get_jwt()

    if claims.get("is_staff") == True:
        data = request.get_json()

        new_items = ItemsModel()
        for key in data:
            if data.get(key):
                setattr(new_items, key, data[key])

        new_items.save()

        result = ItemsSchema().dump(new_items)

        return jsonify({"items": result,}),201

@admin_bp.patch("/updateitems/<int:Items_id>")
@jwt_required()
def update_items(Items_id):
    claims = get_jwt()

    if claims.get("is_staff") == True:
        data = request.get_json()

        new_items = ItemsModel.query.filter_by(id=Items_id).first()

        if not new_items:
            return jsonify({"message": "Items does not existed, cannot update..."}), 404

        for key in data:
            if data.get(key):
                setattr(new_items, key, data[key])

        new_items.save()

        result = ItemsSchema().dump(new_items)

        return jsonify({"items": result,}),201

@admin_bp.delete("/deleteitems/<int:Items_id>")
@jwt_required()
def delete_items(Items_id):
    claims = get_jwt()

    if claims.get("is_staff") == True:

        result = ItemsModel.query.filter_by(id=Items_id).first()

        if not result:
            return jsonify({"message": "Items does not existed, cannot delete..."}), 404

        result.delete()

        return jsonify({"message": "Items deleted"}), 201