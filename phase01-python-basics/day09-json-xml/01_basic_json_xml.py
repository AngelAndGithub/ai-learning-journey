#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 9: JSON/XML解析

本文件包含Python JSON和XML解析的练习代码
"""

import json
import xml.etree.ElementTree as ET
import os

# 1. JSON基本操作
print("=== JSON基本操作 ===")

# 1.1 Python对象转JSON
print("\n1.1 Python对象转JSON")
data = {
    "name": "Alice",
    "age": 30,
    "is_student": False,
    "courses": ["Math", "Science", "English"],
    "address": {
        "city": "New York",
        "zipcode": "10001"
    }
}

# 转换为JSON字符串
json_string = json.dumps(data, indent=2, ensure_ascii=False)
print(f"JSON字符串:\n{json_string}")

# 1.2 JSON字符串转Python对象
print("\n1.2 JSON字符串转Python对象")
json_str = '{"name": "Bob", "age": 25, "is_student": true, "courses": ["Physics", "Chemistry"]}'
parsed_data = json.loads(json_str)
print(f"解析后的数据类型: {type(parsed_data)}")
print(f"Name: {parsed_data['name']}")
print(f"Age: {parsed_data['age']}")
print(f"Courses: {parsed_data['courses']}")

# 1.3 读写JSON文件
print("\n1.3 读写JSON文件")

# 写入JSON文件
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print("JSON文件写入成功")

# 读取JSON文件
with open("data.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)
print("JSON文件读取成功")
print(f"Loaded data: {loaded_data}")

# 2. XML基本操作
print("\n=== XML基本操作 ===")

# 2.1 创建XML
print("\n2.1 创建XML")
root = ET.Element("students")

# 创建学生1
student1 = ET.SubElement(root, "student")
ET.SubElement(student1, "name").text = "Alice"
ET.SubElement(student1, "age").text = "30"
ET.SubElement(student1, "course").text = "Math"

# 创建学生2
student2 = ET.SubElement(root, "student")
ET.SubElement(student2, "name").text = "Bob"
ET.SubElement(student2, "age").text = "25"
ET.SubElement(student2, "course").text = "Science"

# 转换为字符串
xml_string = ET.tostring(root, encoding="utf-8").decode("utf-8")
print(f"XML字符串:\n{xml_string}")

# 2.2 解析XML
print("\n2.2 解析XML")
# 从字符串解析
root_element = ET.fromstring(xml_string)

# 遍历XML
for student in root_element.findall("student"):
    name = student.find("name").text
    age = student.find("age").text
    course = student.find("course").text
    print(f"Student: {name}, Age: {age}, Course: {course}")

# 2.3 读写XML文件
print("\n2.3 读写XML文件")

# 写入XML文件
tree = ET.ElementTree(root)
tree.write("students.xml", encoding="utf-8", xml_declaration=True)
print("XML文件写入成功")

# 读取XML文件
tree = ET.parse("students.xml")
root = tree.getroot()
print("XML文件读取成功")

for student in root.findall("student"):
    name = student.find("name").text
    age = student.find("age").text
    course = student.find("course").text
    print(f"Student: {name}, Age: {age}, Course: {course}")

# 3. JSON与XML的相互转换
print("\n=== JSON与XML的相互转换 ===")

# 3.1 JSON转XML
def json_to_xml(json_data, root_name="root"):
    """将JSON转换为XML"""
    root = ET.Element(root_name)
    
    def convert(data, parent):
        """递归转换"""
        if isinstance(data, dict):
            for key, value in data.items():
                element = ET.SubElement(parent, key)
                convert(value, element)
        elif isinstance(data, list):
            for item in data:
                element = ET.SubElement(parent, "item")
                convert(item, element)
        else:
            parent.text = str(data)
    
    convert(json_data, root)
    return root

# 测试JSON转XML
xml_root = json_to_xml(data, "data")
xml_str = ET.tostring(xml_root, encoding="utf-8").decode("utf-8")
print(f"JSON转XML结果:\n{xml_str}")

# 3.2 XML转JSON
def xml_to_json(element):
    """将XML转换为JSON"""
    result = {}
    
    # 处理子元素
    children = list(element)
    if children:
        for child in children:
            child_data = xml_to_json(child)
            if child.tag in result:
                if not isinstance(result[child.tag], list):
                    result[child.tag] = [result[child.tag]]
                result[child.tag].append(child_data)
            else:
                result[child.tag] = child_data
    # 处理文本内容
    elif element.text and element.text.strip():
        result = element.text.strip()
    
    return result

# 测试XML转JSON
json_data = xml_to_json(root)
print(f"XML转JSON结果:\n{json.dumps(json_data, indent=2, ensure_ascii=False)}")

# 4. 实际应用场景
print("\n=== 实际应用场景 ===")

# 4.1 配置文件处理
print("\n4.1 配置文件处理")

# JSON配置文件
config = {
    "database": {
        "host": "localhost",
        "port": 3306,
        "username": "root",
        "password": "password",
        "database": "mydb"
    },
    "server": {
        "port": 8080,
        "debug": True,
        "timeout": 30
    }
}

# 写入配置文件
with open("config.json", "w", encoding="utf-8") as f:
    json.dump(config, f, indent=2, ensure_ascii=False)
print("配置文件写入成功")

# 读取配置文件
with open("config.json", "r", encoding="utf-8") as f:
    loaded_config = json.load(f)
print("配置文件读取成功")
print(f"Database host: {loaded_config['database']['host']}")
print(f"Server port: {loaded_config['server']['port']}")

# 4.2 API响应处理
print("\n4.2 API响应处理")

# 模拟API响应
api_response = '''
{
    "status": "success",
    "data": {
        "users": [
            {
                "id": 1,
                "name": "Alice",
                "email": "alice@example.com"
            },
            {
                "id": 2,
                "name": "Bob",
                "email": "bob@example.com"
            }
        ],
        "total": 2
    },
    "message": "Users retrieved successfully"
}
'''

# 解析API响应
response_data = json.loads(api_response)
print(f"Status: {response_data['status']}")
print(f"Message: {response_data['message']}")
print(f"Total users: {response_data['data']['total']}")
print("Users:")
for user in response_data['data']['users']:
    print(f"  - {user['name']} ({user['email']})")

# 4.3 XML数据处理
print("\n4.3 XML数据处理")

# 模拟XML数据
xml_data = '''
<library>
    <book>
        <title>Python Programming</title>
        <author>John Doe</author>
        <year>2023</year>
        <price>29.99</price>
    </book>
    <book>
        <title>Data Science</title>
        <author>Jane Smith</author>
        <year>2024</year>
        <price>39.99</price>
    </book>
</library>
'''

# 解析XML数据
root = ET.fromstring(xml_data)
print("Books in library:")
for book in root.findall("book"):
    title = book.find("title").text
    author = book.find("author").text
    year = book.find("year").text
    price = book.find("price").text
    print(f"  - {title} by {author} ({year}): ${price}")

# 5. 错误处理
print("\n=== 错误处理 ===")

# 5.1 JSON错误处理
try:
    invalid_json = '{"name": "Alice", "age": }'
    data = json.loads(invalid_json)
except json.JSONDecodeError as e:
    print(f"JSON解析错误: {e}")

# 5.2 XML错误处理
try:
    invalid_xml = '<root><child>text</root>'  # 缺少结束标签
    root = ET.fromstring(invalid_xml)
except ET.ParseError as e:
    print(f"XML解析错误: {e}")

# 清理测试文件
print("\n清理测试文件")
test_files = ["data.json", "students.xml", "config.json"]
for file in test_files:
    if os.path.exists(file):
        os.remove(file)
        print(f"Deleted {file}")

print("\nJSON/XML解析练习完成！")
