from flask import Flask, request
from CustomeQuery import helloquery

app = Flask(__name__)

@app.route('/')
def root_route():
    return 'Hello World'

@app.route('/hello')
def hello_world():
    my_query = """
        {
            hello ( name: "Lukas" )
            amazing
        }
    """
    
    #Execute
    result = helloquery.helloSchema.execute(my_query)
    
    #Returning the data
    return {
        "data": result.data
    }
    
@app.route('/hello/<name>')
def hello_world_name(name):
    my_query = """
        {
            hello ( name : "%s" )
        }
    """%(name)
  
    #Execute
    result = helloquery.helloSchema.execute(my_query)
    
    #Returning the data
    return {
        "data": result.data
    }

#https://stackoverflow.com/questions/15182696/multiple-parameters-in-flask-approute
#One possible way for multiple params --> It is done via flusk
@app.route('/hello/<name>/<age>')
def hello_world_params_in_rout(name, age):
    print(age)
    my_query = """
        {
            hello ( name : "%s" )
        }
    """%(name)
  
    #Execute
    result = helloquery.helloSchema.execute(my_query)
    
    #Returning the data
    return {
        "data": result.data
    }
    
#Another possible way for multiple params --> It is done via flusk
@app.route('/hello/params')
def hello_world_name_request():
    name = request.args.get('name', None)
    age  = request.args.get('age', None)
    print("The name is: " + name + " and the age is: " + age)
    
    return {
        "test": "test"
    }

if __name__ == '__main__':
    app.run(debug=True)