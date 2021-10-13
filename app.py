import psycopg2.extras
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from psycopg2 import *

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# Connect to your postgres DB
connection = connect(dbname="contactdb", user="postgres", password="postgress")
connection.autocommit = True


# Open a cursor to perform database operations


@app.route('/users', methods=['GET'])
def users():
    cur = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute('SELECT * FROM contacts')
    return jsonify([dict(row) for row in cur.fetchall()])


@app.route('/add_contact', methods=['POST'])
def add_contact():
    cur = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        post_data = request.get_json(force=True)
        name = post_data['name']
        ser_name = post_data['ser_name']
        second_name = post_data['second_name']
        organisation = post_data['organisation']
        position = post_data['position']
        email = post_data['email']
        tel = post_data['tel']
        cur.execute("""INSERT INTO contacts (name, ser_name, second_name,
         organisation, position, email, tel) VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                    (name, ser_name, second_name, organisation, position, email, tel))
        return jsonify('Contact added!')


@app.route('/edit_contact', methods=['POST'])
def edit_contact():
    cur = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        post_data = request.get_json(force=True)
        contact_id = post_data['id']
        name = post_data['name']
        ser_name = post_data['ser_name']
        second_name = post_data['second_name']
        organisation = post_data['organisation']
        position = post_data['position']
        email = post_data['email']
        tel = post_data['tel']
        cur.execute("""UPDATE contacts
            SET name = %s,
                ser_name = %s,
                second_name = %s,
                organisation = %s,
                position = %s,
                email = %s,
                tel = %s                
            WHERE id = %s""",
                    (name, ser_name, second_name, organisation, position, email, tel, contact_id)
                    )
        return jsonify('Contact edited!')


@app.route('/delete_contact/<contact_id>', methods=['DELETE'])
def delete_user(contact_id):
    cur = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    sql_delete_user = f"DELETE FROM contacts WHERE id={contact_id}"
    cur.execute(sql_delete_user)
    return jsonify('Contact removed!')


class User:
    def __init__(self,
                 id,
                 name,
                 ser_name,
                 second_name,
                 organisation,
                 position,
                 email,
                 tel):
        self.id = id
        self.name = name
        self.ser_name = ser_name
        self.second_name = second_name
        self.organisation = organisation
        self.position = position
        self.email = email
        self.tel = tel


if __name__ == '__main__':
    app.run()
