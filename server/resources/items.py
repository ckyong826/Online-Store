from models.itemsModel import ItemsModel
from flask import Blueprint, jsonify, request
from Schema import ItemsSchema

items_bp = Blueprint("items", __name__)

#Get All Items
@items_bp.get("/all")
def get_all_items():
    items = ItemsModel.query.paginate()

    result = ItemsSchema().dump(items, many=True)
    return jsonify({"items": result,}),200,

#Get Item by ID
@items_bp.get("/<int:Items_id>")
def get_item(Items_id):
    items = ItemsModel.query.filter_by(id=Items_id).first()
    result = ItemsSchema().dump(items)
    if not result:
        return jsonify({"message": "Items does not existed, cannot load..."}), 404
    return jsonify({"items": result,}),200,


