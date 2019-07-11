import os

from flask import Flask

from flask import request





def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that list my todos

    def todo_view(todos):

        the_view='list of my todos' +'<br/>'

        for todo in todos:
            the_view+=(todo + '<br/>')
        the_view+= '-----Ends here-----'

        return the_view


    def get_todos_by_name(name):

        if name=='depo':
           my_todos=['go for run','play cricket']
        elif name=='raj':
            my_todos=['go for run','play cricket']
        elif name=='shivang':
            my_todos=['go for run','play cricket']
        else:
            my_todos=[]

        return my_todos


    @app.route('/todos')
    def todos():

        name=request.args.get('name')
        print(name)

        person_todo_list = get_todos_by_name(name)

        return todo_view(person_todo_list)


    @app.route('/raj')
    def raj():


        my_todos=['Drink coffee','play cricket']
        return todo_view(my_todos)



    @app.route('/depo')
    def depo():


        my_todos=['go for run','play cricket']
        return todo_view(my_todos)



    @app.route('/shivang')
    def shivang():

        my_todos=['go for run','play cricket']
        return todo_view(my_todos)

    @app.route('/sanket')
    def sanket():

        my_todos=['go for run','play cricket']
        return todo_view(my_todos)



    return app

