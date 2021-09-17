import datetime,mysql.connector
from projectapp import db


class dealer(db.Model):
    __tablename__='dealer'
    dealer_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    dealer_fname = db.Column(db.String(45), nullable = False)
    dealer_lname = db.Column(db.String(45), nullable = False)
    dealer_email = db.Column(db.String(75), nullable = False)
    dealer_address = db.Column(db.String(200), nullable = False)
    dealer_pwd = db.Column(db.String(35), nullable = False)
    dealer_signupdate = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    deal = db.relationship('vehicle',backref='vehic')

class orders(db.Model):
    __tablename__ = 'orders'
    order_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    vehicle_id = db.Column(db.Integer(),db.ForeignKey('vehicle.vehicle_id'),nullable = False)
    user_id = db.Column(db.Integer(),db.ForeignKey('user.user_id'),nullable = False)
    payment_id = db.Column(db.Integer(),db.ForeignKey('payment.payment_id'),nullable = False)
    order_date = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    order_status = db.Column(db.String(45), nullable = False)

class payment(db.Model):
    __tablename__ = 'payment'
    payment_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    payment_status = db.Column(db.String(45), nullable = False)
    payment_date = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    user_idpayment = db.Column(db.Integer(), db.ForeignKey('user.user_id') ,nullable=False)
    payment_amt = db.Column(db.BigInteger())
    vehicle_idpayment = db.Column(db.Integer(), db.ForeignKey('vehicle.vehicle_id') ,nullable=False)
    payment_type = db.Column(db.Integer(), db.ForeignKey('pay_type.pay_id') ,nullable=False)
    order = db.relationship('orders',backref='pay')

class pay_type(db.Model):
    __tablename__ = 'pay_type'
    pay_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    pay_mode = db.Column(db.String(45), nullable = False)
    pay = db.relationship('payment', backref='paytype')

class shipment(db.Model):
    __tablename__ = 'shipment'
    shipment_id= db.Column(db.Integer(), primary_key=True, autoincrement=True)
    shipment_status = db.Column(db.String(45), nullable = False)
    shipment_type = db.Column(db.String(45), nullable = False)
    date_shipped = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    departure_port = db.Column(db.String(100), nullable = False)
    arrival_port = db.Column(db.String(100), nullable = False)
    shipmentorder = db.Column(db.Integer())
    shipmentcharge = db.Column(db.BigInteger())

class user(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    user_fname = db.Column(db.String(45), nullable = False)
    user_lname = db.Column(db.String(45), nullable = False)
    user_email = db.Column(db.String(75), nullable = False)
    user_address = db.Column(db.String(200), nullable = False)
    user_password = db.Column(db.String(75), nullable = False)
    user_signup = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    order = db.relationship('orders',backref='user')
    pay = db.relationship('payment', backref='user')




class vehicle(db.Model):
    __tablename__ = 'vehicle'
    vehicle_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    vehicle_name = db.Column(db.String(85), nullable = False)
    vehicle_price = db.Column(db.BigInteger(), nullable = False)
    vehicle_location = db.Column(db.String(85), nullable = False)
    vehicle_type = db.Column(db.String(45), nullable = False)
    vehicle_dealerid = db.Column(db.Integer(), db.ForeignKey('dealer.dealer_id') ,nullable = False)
    vehicle_year = db.Column(db.Integer(), nullable = False)
    vehicle_vin = db.Column(db.Integer(), nullable = False)
    vehicle_mileage = db.Column(db.Integer(), nullable = False)
    vehicle_trans = db.Column(db.String(45), nullable = False)
    vehicle_manufacturer = db.Column(db.String(45), nullable = False)
    vehicle_model = db.Column(db.String(45), nullable = False)
    order = db.relationship('orders',backref='vehicle')
    pay = db.relationship('payment', backref='vehicle')


class vehicle_Pic(db.Model):
    __tablename__ = 'vehicle_pic'
    pic_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    vehicle_pic = db.Column(db.String(85), nullable = False)
    picvehicle_id = db.Column(db.Integer(), db.ForeignKey('vehicle_pic.pic_id') ,nullable = False)

class vehicle_type(db.Model):
    __tablename__ = 'vehicle_type'
    vehicle_type_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    vehicle_type = db.Column(db.String(45), nullable = False)




















   
