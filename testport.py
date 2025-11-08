from flask import Flask, jsonify, request, render_template_string
import logging
from typing import Any, TypedDict
from datetime import datetime
import json

logger = logging.getLogger('test')

app = Flask(__name__)

class UserData(TypedDict):
    usrid: str
    pwd: str

class AdminData(TypedDict):
    name: str
    pwd: str
    permission: list[str]

# 使用更具描述性的变量名
user_database: list[UserData] = []
admin_database: list[AdminData] = [
    {
        "name":"admin",
        "pwd":"admin123",
        "permission":["view_all_data","view_count"]
    }
] 

@app.route('/')
def home():
    resp: dict[str, Any] = {
        "msg1": "hello",
        "msg2": 123,
        "msg3": True
    }
    logger.info('Home page accessed')
    return jsonify(resp)

@app.route('/post', methods=['POST'])  # 改为大写
def handle_post():
    if request.is_json:
        data = request.get_json()
    elif request.content_type == 'application/x-www-form-urlencoded':
        data: dict[str, Any] = request.form.to_dict()
    else:
        strdata = request.data.decode()
        return jsonify({
            "data": strdata,
            "timestamp": datetime.now().timestamp()
        })
    data['timestamp'] = datetime.now().timestamp()  # 保持数字类型
    return jsonify(data)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Password Helper</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        h2 { color: #333; }
        h3 { color: #666; }
        .section { margin-bottom: 30px; padding: 20px; border-left: 4px solid #007cba; background: #f5f5f5; }
    </style>
</head>
<body>
    <h1>🔐 Password Management System</h1>
    
    <div class="section">
        <h2>📝 Add User</h2>
        <p>Choose method "add" to create a new user</p>
    </div>
    
    <div class="section">
        <h2>🗑️ Delete User</h2>
        <p>Choose method "del" to remove a user</p>
    </div>
    
    <div class="section">
        <h2>🔑 Login</h2>
        <p>Choose method "log" to authenticate</p>
    </div>
    
    <div class="section">
        <h2>📋 Usage Example</h2>
        <h3>JSON Format:</h3>
        <code>{"method": "log", "pwd": "123456789"}</code>
        <h3>Available Methods:</h3>
        <ul>
            <li><strong>add</strong> - Create new user</li>
            <li><strong>del</strong> - Delete existing user</li>
            <li><strong>log</strong> - User login</li>
        </ul>
    </div>
</body>
</html>
"""

def find_user_index(userid: str) -> int:
    """查找用户索引，找不到返回 -1"""
    for i, user in enumerate(user_database):
        if user['usrid'] == userid:
            return i
    return -1

def find_admin_index(username: str) -> int:
    """查找管理员索引， 找不到返回-1"""
    for i,admin in enumerate(admin_database):
        if admin['name'] == username:
            return i
    return -1

def user_exists(userid: str) -> bool:
    """检查用户是否存在"""
    return find_user_index(userid) != -1

def admin_exists(username: str) -> bool:
    """检查管理员是否存在"""
    return find_admin_index(username) != -1

@app.route("/pwd/<userid>", methods=['GET', 'POST'])
def password_manager(userid: str):
    if request.method == 'GET':
        return render_template_string(HTML)
    
    # POST 请求处理
    if not request.is_json:
        return jsonify({
            "status": "error",
            "message": "Content-Type must be application/json"
        }), 415
    
    data: dict[str, str] = request.get_json()
    method = data.get('method', '').lower()
    password = data.get('pwd', '')
    
    # 输入验证
    if not method:
        return jsonify({
            "status": "error", 
            "message": "Method is required"
        }), 400
    
    if not password:
        return jsonify({
            "status": "error",
            "message": "Password is required"
        }), 400
    
    # 方法路由
    if method == 'log':
        if not user_exists(userid):
            return jsonify({
                "status": "error",
                "message": "User not found"
            }), 404
        
        # 这里应该验证密码，但你代码中没存储密码验证逻辑
        user_index = find_user_index(userid)
        stored_password = user_database[user_index]['pwd']
        
        if password == stored_password:
            return jsonify({
                "status": "success",
                "message": "Login successful"
            }), 200
        else:
            return jsonify({
                "status": "error", 
                "message": "Invalid password"
            }), 401
    
    elif method == 'add':
        if user_exists(userid):
            return jsonify({
                "status": "error",
                "message": "User ID already exists"
            }), 409  # 冲突状态码
        
        new_user: UserData = {
            "usrid": userid,
            "pwd": password
        }
        user_database.append(new_user)
        
        return jsonify({
            "status": "success",
            "message": "User created successfully",
            "userid": userid
        }), 201
    
    elif method == 'del':
        if not user_exists(userid):
            return jsonify({
                "status": "error",
                "message": "User not found"
            }), 404
        
        user_index = find_user_index(userid)
        deleted_user = user_database.pop(user_index)
        
        return jsonify({
            "status": "success",
            "message": "User deleted successfully",
            "deleted_userid": deleted_user['usrid']
        }), 200
    
    else:
        return jsonify({
            "status": "error",
            "message": "Invalid method. Use 'add', 'del', or 'log'",
            "available_methods": ["add", "del", "log"]
        }), 400

@app.route('/admin')
def admin():
    auth = request.authorization
    if not auth:
        return jsonify({
            "status":"error",
            "message":"authorization needed"
        }), 401
    account = auth.username
    pwd = auth.Password
    if account is None or account.strip() == "":
        return jsonify({
            "status":"error",
            "message":"username needed"
        }), 401
    if pwd is None or pwd.strip() == "":
        return jsonify({
            "status":"error",
            "message":"password cant be empty"
        }), 401
    if admin_exists(account):
        index = find_admin_index(account)
        if admin_database[index]['pwd'] == pwd:
            return_data = {"status":"success","timestamp":datetime.now().timestamp()}
            if 'view_all_data' in admin_database[index]['permission']:
                return_data['all_data'] = str(user_database)
            if 'view_count' in admin_database[index]['permission']:
                return_data['count'] = len(user_database)
            return jsonify(return_data),200
        else:
            return jsonify({
                "status":"error",
                "message":"Invalid password"
            }), 401
    else:
        return jsonify({
            "status":"error",
            "message":"Admin no found"
        }), 404


@app.route('/save')
def save():
    with open('user.json','w') as f:
        json.dump(user_database,f,indent=4)
    
    with open('admin.json','w') as f:
        json.dump(admin_database,f,indent=4)

    return '',200

if __name__ == '__main__':
    app.run('localhost', 5000, debug=True)  # 开启调试模式
