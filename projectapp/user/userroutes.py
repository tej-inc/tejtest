from flask import render_template,make_response,abort,request,redirect,flash,session,url_for
from werkzeug.security import generate_password_hash,check_password_hash
from . import userobj

from projectapp.forms import login,register,adminlog,dealerregister,dealerlog









@userobj.route('/')
def mainpage():
    from projectapp import mymodels  ,db
    #t = db.session.execute(f"SELECT * FROM vehicle_type")
    #model = db.session.execute(f"SELECT * FROM make")
    #manu = db.session.execute(f"SELECT * FROM make")
    session.get('user')
    return render_template('uindex.html')

@userobj.route('/explore')
def explore():
    session.get('user')
    return render_template('upage1.html')

@userobj.route('/shipping')
def ship():
    loggedin=session.get('user') 
    if loggedin !=None:
        return render_template('upage2.html')
    else:
        return redirect('/login')




@userobj.route('/ulogin',methods=['POST','GET'])
def ulogs():
    from projectapp import db
    from projectapp.mymodels import user
    from projectapp.forms import login
    
    if request.method=='GET':
        return render_template('userlogin.html')
    else:
        mymail = request.form.get('themail')
        mypwd = request.form.get('thepassword')
        v = db.session.execute(f"SELECT * FROM user WHERE user_email='{mymail}' AND user_password='{mypwd}'")
        g = v.fetchone()
        if g !=None:
            flash("logged in successfully")
            return redirect("/explore")
        else:
            flash("Incorrect Details")
            return redirect("/ulogin")
                  
                  
            
            

@userobj.route('/register',methods=['POST','GET'])
def ureg():
    loggedin=session.get('user')

    reg = register()
    from projectapp import db
    from projectapp.mymodels import user
    if request.method=='GET':
        return render_template('userregister.html',reg=reg)
    else:
        fname= request.form.get('fname')
        lname= request.form.get('lname')
        mail = request.form.get('email')
        add = request.form.get('address')
        pwd = request.form.get('password')
        pwd2 = request.form.get('password2')
        if pwd == pwd2:
            coded= generate_password_hash(pwd)
            u = user(user_fname=fname,user_lname=lname,user_email=mail,user_address=add,user_password=coded)
            db.session.add(u)
            db.session.commit()
            session['user'] = u.user_fname
            flash('You have successfully signed up!')
            return redirect('/explore')
        else:
            flash ('Sorry your passwords do not match')
            return redirect('/register')


@userobj.route('/submitit', methods=['POST', 'GET'])
def submitam():
    #user = request.args['username'] or request.args.get('username')
    #val = request.values['username']
    head = request.headers
    data = request.form.getlist('media')
    
    for i in data:
        mid=open('media.txt','a')
        data.write(i+'\n')
        mid.close()
        
    return render_template('clwfrm.html')    
    #return f'form will be submitted here{val} {user}'
    





@userobj.route('/signout')
def signout():
    if session.get('user')!=None:
        session.pop('user')
        return render_template('upage1.html')
   

@userobj.errorhandler(404)
def fatalerror(error):
    return (render_template('error.html',error=error),404)



@userobj.route('/about/')
def about():
    return render_template('about.html')




@userobj.route('/adminlogin',methods=['POST','GET'])
def adminlogin():
    
    ad = adminlog()
    if request.method=='GET':
        return render_template('adminlog.html',ad=ad)
    else:
        auth1 = 'tejadmin'
        auth2 = '55531'
        mail = ad.email.data
        pwd = ad.password.data
        if mail==auth1 and pwd ==auth2:
            return redirect('/adminhome')
        else:
            return redirect('/adminlogin')
        

    
@userobj.route('/dealerlogin',methods=['POST','GET'])
def dealerlogin():
    dl = dealerlog()
    from projectapp import db
    from projectapp.mymodels import dealer
    
    if request.method=='GET':
        return render_template('dealerlogin.html',dl=dl)
    else:
        dl= dealerlog()
        mail = dl.email.data
        pwd = dl.password.data
        check = db.session.query(dealer).filter(dealer.dealer_email==f'{mail}', dealer.dealer_pwd==f'{pwd}').all()
        if check != None :
            session['dealer'] = mail
            
            return redirect('/dealerhome')
        else:
            return redirect('/dealerlogin')






@userobj.route('/adminhome')
def adminhome():
    return render_template('adminhome.html')

@userobj.route('/dealerhome')
def dealerhome():
    return render_template('dealerhome.html')


@userobj.route('/dealerreg', methods=['POST','GET'])
def dealereg():
    deal = dealerregister()
    from projectapp import db,mymodels
    if request.method=='GET':
        return render_template('dealerreg.html',deal=deal)
    else:
        fname= request.form.get('fname')
        lname= request.form.get('lname')
        mail = request.form.get('email')
        add = request.form.get('address')
        pwd = request.form.get('password')
        pwd2 = request.form.get('password2')
        if pwd == pwd2:
            coded= generate_password_hash(pwd2)
            db.session.execute(f"INSERT INTO dealer SET dealer_fname='{fname}',dealer_lname='{lname}',dealer_email='{mail}',dealer_address='{add}', dealer_pwd='{coded}'")
            db.session.commit()
            return redirect('/dealerhome')
        else:
            flash ('Sorry your passwords do not match')
            return redirect('/dealerreg')


    

