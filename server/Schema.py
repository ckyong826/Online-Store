from marshmallow import fields, Schema

class UserSchema(Schema):
    id = fields.String()
    username = fields.String()
    email = fields.String()

class ItemsSchema(Schema):
    id = fields.String()
    name = fields.String()
    description = fields.String()
    price = fields.Integer()
    collection = fields.String()
    sizeS=fields.Integer()
    sizeM=fields.Integer()
    sizeL=fields.Integer()
    sizeXL=fields.Integer()
    