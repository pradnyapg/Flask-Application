
from flask import Flask,render_template, redirect, url_for, request,jsonify
from pprint import pprint
import pymysql
app = Flask(__name__)

# Open database connection
db = pymysql.connect("127.0.0.1","root","","inventory")
# prepare a cursor object using cursor() method
cursor = db.cursor()

@app.route('/')
def home():

   sql = "SELECT * FROM product" 
   cursor.execute(sql)
   rows = cursor.fetchall()
  
   return render_template('home.html',rows = rows,var = "product")

@app.route('/productAddPage',methods = ['POST', 'GET'])
def productAddPage():

    productname = request.form['productname']
    productquantity = request.form['productquantity']
    productmrp = request.form['productmrp']
    
    sql = "INSERT INTO product (product_name, product_qty, product_mrp) VALUES (%s,%s,%s)"   
    cursor.execute(sql,(productname,productquantity,productmrp))
    #pymysql.connection.commit()
    db.commit()
    return jsonify({'abc': 'registration unsuccessful'})
    #return redirect(url_for('home'))

@app.route('/productEditPage',methods = ['GET', 'POST'])
def productEditPage():

    product_id = request.form['productid']
    productname = request.form['updateproductname']
    productquantity = request.form['updateproductquantity']
    productmrp = request.form['updateproductmrp']
    
    sql = "UPDATE product SET product_name =%s,product_qty=%s,product_mrp=%s where product_id = %s"   
    input = (productname,productquantity,productmrp,product_id)
    cursor.execute(sql,input)
    #pymysql.connection.commit()
    db.commit()
    #return jsonify({'Product': 'Product Added successful','productid':product_id,'productname':productname})
    return home()
	
@app.route('/locationAddPage',methods = ['POST', 'GET'])	
def locationAddPage():

    locationname = request.form['locationname']
    
    sql = "INSERT INTO location (location_name) VALUES (%s)"   
    cursor.execute(sql,(locationname))
    #pymysql.connection.commit()
    db.commit()
    return jsonify({'Location': 'Location Added successful'})
    #return redirect(url_for('home'))
    
@app.route('/locationDetails')
def locationDetails():

   sql = "SELECT * FROM location" 
   cursor.execute(sql)
   result = cursor.fetchall()
   
   return render_template('home.html',result = result,var = 'location')

@app.route('/locationUpdatePage',methods = ['POST','GET'])
def locationUpdatePage():

    location_id = request.form['location_id']
    locationname = request.form['locationname']
    locationaddress = request.form['locationaddress']
    sql = "UPDATE location SET location_address =%s where location_id = %s"   
    input = (locationaddress,location_id)
    cursor.execute(sql,input)
    #pymysql.connection.commit()
    db.commit()
    #return jsonify({'Location': 'Location Updated successful','locationid':location_id,'locationaddress':locationaddress})
    return locationDetails()
    
@app.route('/productMovementDetails')
def productMovementDetails():

   sql = "SELECT product_movement.movement_id,p.product_id,l.location_id,a.location_id,p.product_name,l.location_name,a.location_name as to_name,product_movement.qty,product_movement.timestamp FROM product_movement Inner Join product p ON product_movement.product_id = p.product_id Inner Join location l ON product_movement.from_location = l.location_id Inner Join location a ON product_movement.to_location = a.location_id order by product_movement.movement_id" 
   cursor.execute(sql)
   res = cursor.fetchall()

   sql = "SELECT * FROM product where product_id NOT IN(select product_id from product_movement)" 
   cursor.execute(sql)
   rows = cursor.fetchall()
    
   sql = "SELECT product_id,product_name FROM PRODUCT"
   cursor.execute(sql)
   productdata = cursor.fetchall()   
   
   sql = "SELECT * FROM location" 
   cursor.execute(sql)
   result = cursor.fetchall()
    
   return render_template('home.html',res = res,productresult = rows,locationresult= result,allproducts=productdata,var = 'product_movement')


@app.route('/ProductMovementAddPage',methods = ['POST', 'GET'])
def ProductMovementAddPage():

    product_id = request.form['productname']
    from_location_id = request.form['from_locationname']
    to_location_id = request.form['to_locationname']
	
    #sql = "SELECT product_id FROM product where product_name ='productname' " 
    #cursor.execute(sql)
    #rows = cursor.fetchone()
	
    sql = "INSERT INTO product_movement (product_id,from_location,to_location) VALUES (%s,%s,%s)"   
    cursor.execute(sql,(product_id,from_location_id,to_location_id))
    #pymysql.connection.commit()
    db.commit()
    #return jsonify({'abc': 'registration unsuccessful'})
    return productMovementDetails()
	 
@app.route('/updateProductMovement',methods=['POST','GET'])
def updateProductMovement():
    
    product_id = request.form['productname']    
    from_location_id = request.form['from_locationname']    
    to_location_id = request.form['to_locationname']    
    
    sql = "INSERT INTO product_movement (product_id,from_location,to_location) VALUES (%s,%s,%s)"   
    cursor.execute(sql,(product_id,from_location_id,to_location_id))
    db.commit()
    return jsonify({'abc': 'registration unsuccessful'})
	
if __name__ == '__main__':
   app.run(debug = True)