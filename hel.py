import requests
from flask import Flask, render_template_string, request, redirect, url_for, jsonify
from html_script import script
from utils import for_style, place_style, remove_class_duplicates, compare_replace
from bs4 import BeautifulSoup

url = 'https://stackoverflow.com'
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"}
response = requests.get(url, headers=headers)


if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    all_tags = soup.find_all()
    html_content=(soup)
    print(soup)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

html_content = script(html_content)

app = Flask(__name__)

# Global variable to store HTML content
current_html_content = html_content

@app.route('/')
def index():
    return render_template_string(current_html_content)

@app.route('/right-click', methods=['POST'])
def handle_right_click():
    data = request.get_json()
    tag = data.get('tag')
    print(f"----------{tag}") 
    tag = data.get('class')
    print(f"----------{tag}") 
    return '', 204 

@app.route('/submit-username', methods=['POST'])
def submit_username():
    data = request.get_json()
    style = 'style="'+data.get('username')+'"'
    # print(f'Received username: {style}')
    
    global current_html_content
    data = request.get_json()
    tag = data.get('tag')
    className = data.get('class')
    tex = data.get('text')
    username = data.get('username')
    # if ('highlight' in className):
    #     className=className.replace('highlight','')
    className=className.strip()
    print(f'--{className}---')
    clas=list(className.split(" "))
    alter=soup.find_all(class_=clas)
    if len(clas)!=0 and len(clas)!=1:
        for i in alter:
            l=f'<{str(tag).lower()}'
            # print("====================================")
            # print(f"===={i.text.strip()}=={tex.strip()}===")
            # print(f"{str(i)[:len(l)]}--")
            # print(f'{l}--')
            if i.text.strip()==tex.strip() and str(i)[:len(l)]==l :
                
                final_tag=i
                break
    else:
        hui=soup.find_all(tag.lower())
        l=f'<{tag.lower()}'
        for i in hui:
            print(i)
            if i.text.strip()==tex.strip():
                final_tag=i
                break
    print(f"----={final_tag}")
    # if final_tag:
    #     style=f' style="{username}" '
    #     final=""
    #     for i in str(final_tag):
    #         if i==">" and "style=" not in final:
    #             final+=(style+'>')
    #         else:
    #             final+=i
    if final_tag:
        style=f' style="{username}" '
        final=str(final_tag)
        try:
            # Append to the existing style attribute
            # final_tag=final_tag.replace("!important","")
            final_tag['style'] += (username+" !important;")
        except:
            final_tag['style'] = (username+" !important;")
    print(style)
    if str(final) in current_html_content:
        # print(current_html_content)
        current_html_content = current_html_content.replace(str(final),str(final_tag))
    else:
        print("Nooooooooooooooooooooo")
    # print(final_tag)
    # print(final)           
    
    
    
    return jsonify({'message': 'Username received successfully!'}), 200


if __name__ == '__main__':
    app.run(debug=True)


