from db import db
from flask_login import UserMixin
from datetime import datetime

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    supplier_eco_certified = db.Column(db.Boolean, default=False, nullable=False)

class Part(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    supplier_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  
    supplier = db.relationship('User', backref=db.backref('parts', lazy=True, cascade="all, delete-orphan"))
    price = db.Column(db.Float, nullable=False)
    availability = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    delivery = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(200), nullable=True)
    description = db.Column(db.Text, nullable=False)
    manufacturer = db.Column(db.String(100), nullable=False)  
    model = db.Column(db.String(100), nullable=False)
    purchases = db.relationship('Purchase', back_populates='part', lazy=True)

    def update_availability(self):
        self.availability = 'Out of Stock' if self.quantity <= 0 else 'In Stock'

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('orders', lazy=True))
    order_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    total_amount = db.Column(db.Float, nullable=False)
    payment_status = db.Column(db.String(20), nullable=False, default='pending')
    payment_reference = db.Column(db.String(100), nullable=True)
    payment_date = db.Column(db.DateTime, nullable=True)
    purchases = db.relationship('Purchase', back_populates='order', lazy=True)

    def update_payment_status(self, status):
        self.payment_status = status
        if status == 'paid':
            self.payment_date = datetime.utcnow()

class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    order = db.relationship('Order', back_populates='purchases', lazy=True)
    part_id = db.Column(db.Integer, db.ForeignKey('part.id'), nullable=False)
    part = db.relationship('Part', back_populates='purchases', lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('purchases', lazy=True))
    quantity = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    purchase_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)