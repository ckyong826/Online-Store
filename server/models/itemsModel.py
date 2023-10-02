from data import db

class ItemsModel(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    description = db.Column(db.String(100),nullable=False)
    price = db.Column(db.Integer,nullable=False)
    collection = db.Column(db.String(100),nullable=False)
    sizeS=db.Column(db.Integer,nullable=False)
    sizeM=db.Column(db.Integer,nullable=False)
    sizeL=db.Column(db.Integer,nullable=False)
    sizeXL=db.Column(db.Integer,nullable=False)

    def __repr__(self):
        return f"Items(id={self.id},name = {self.name},description = {self.description},price = {self.price},collection = {self.collection},sizeS = {self.sizeS},sizeM = {self.sizeM},sizeL = {self.sizeL},sizeXL = {self.sizeXL})"
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()