from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import render_template,redirect,session,request,flash
from flask_app.models import models_user
from flask_app.models.models_user import User
from flask_app.models.models_recipe import Recipe


@app.route('/recipes/show')
def showrecipesandusers():
    if 'user_id' not in session:
        flash('must sign in first')
        return redirect ('/')
    recipesandusers = Recipe.get_all()
    return render_template ('showallrecipes.html' , recipesandusers = recipesandusers )

@app.route('/recipes/new')
def createrecipe():
    if 'user_id' not in session:
        flash('must sign in first')
        return redirect ('/')
    return render_template ('addrecipe.html'  )

@app.route('/addrecipes' , methods = ['post'])
def showallrecipes():
    data = {'name':request.form['name'],
            'description':request.form['description'],
            'instructions':request.form['instructions'],
            'user_id':request.form['user_id']
            }
    Recipe.create(data)
    return redirect ('/recipes/show')

@app.route('/recipes/<int:id>')
def showonerecipe(id):
    if 'user_id' not in session:
        flash('must sign in first')
        return redirect ('/')
    data = {'id':id}
    recipe = Recipe.get_one(data )
    return render_template('showone.html' , recipe = recipe)

@app.route('/recipes/edit/<int:id>')
def edit(id):
    if 'user_id' not in session:
        flash('must sign in first')
        return redirect ('/')
    data = {'id':id}
    recipe = Recipe.get_one(data)
    return render_template ('edit.html' , recipe = recipe)

@app.route('/recipes/update/<int:id>' , methods = ['post'])
def update(id):
    data = {'name':request.form['name'] , 'description':request.form['description'] , 'instructions':request.form['instructions']  , 'id':request.form['id']}
    print (data)
    Recipe.update(data)
    return redirect (f'/recipes/{request.form["id"]}')

@app.route('/recipes/delete/<int:id>')
def delete(id):
    data = {'id':id}
    Recipe.delete(data)
    return redirect('/recipes/show')

