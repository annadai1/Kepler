# Python script to create app.py

content = '''from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
'''

# Define the path to the file
file_path = 'app.py'

# Write the content to the file
with open(file_path, 'w') as file:
    file.write(content)

print(f"File {file_path} created successfully.")

