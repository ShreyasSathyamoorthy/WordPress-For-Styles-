def for_style(tagg):
    tagg_spl=list(tagg.split(" "))
    stylee=""
    sty=[]
    sty1=[]
    for i in tagg_spl:
        if "style=" in i:
            i=i.strip()
            i=i.replace('"',"")
            i=i.replace('style=',"")
            if i[-1]!=";":
                i=i+";"
            stylee+=i
            

    all={}
    for i in list(stylee.split(";")):
        try:
            x=list(i.split(":"))
            all[x[0]]=x[1]
        except:
            pass
        
    print(all)
    
    stylee=""
    for key,value in all.items():
        stylee+=(key+":"+value+";")
    
    
    stylee='style="'+stylee+'" '
    tex=""
    for i in tagg_spl:
        if "style=" not in i:
            # print(i)
            tex+=(i+" ")
    tagg=place_style(stylee, tex)
    return (tagg)

    
def place_style(style_text, tags):
    style_text=style_text.strip()
    if style_text[0]!=" ":
        style_text=" "+style_text
    if style_text[-1]!=" ":
        style_text=style_text+" "
    c=0
    tag1=""
    for i in (str(tags)):
        if i == ">" and c==0:
            tag1 += style_text + i
            c=1
        else:
            tag1+=i
    return tag1


def remove_class_duplicates(tag):
    tag_new=""
    tag_spll=list(tag.split(" "))
    for i in tag_spll:
        if "class=" in i:
            i=i.replace('"',"")
        tag_new+=(i+" ")
    return tag_new

def compare_replace(script, alter):
    
    alter=alter.strip()
    while True:
        if "\n" in alter:
            alter=alter.replace("\n","")
        else:
            break
    while True:
        if "\t" in alter:
            alter=alter.replace("\t","")
        else:
            break
    while True:
        if " " in alter:
            alter=alter.replace(" ","")
        else:
            break
    while True:
        if "&amp;" in alter:
            alter=alter.replace("&amp;","&")
        else:
            break
    while True:
        if '"' in alter:
            alter=alter.replace('"',"")
        else:
            break
    while True:
        if "highlight" in alter:
            alter=alter.replace("highlight","")
        else:
            break
    x=""
    # print(script)
    print(alter)
    # print(len(script)-len(alter)+1)
    script1=script
    while True:
        if ' ' in script1:
            script1=script1.replace(' ',"")
        else:
            break
    while True:
        if '\n' in script1:
            script1=script1.replace('\n',"")
        else:
            break
    while True:
        if '"' in script1:
            script1=script1.replace('"',"")
        else:
            break
    print("----------------------------")
    if alter in script1:
        print("yes")
        for i in range(0,len(script)-len(alter)+1):
            x=""
            j=i
            while(len(x)!=len(alter)):
                if j!=len(script):
                    if script[j]!=" " and script[j]!='\n' and script[j]!='"':
                        x+=script[j]
                        j+=1
                    else:
                        j+=1
                else:
                    break
            if x==alter:
                return (i,j)
    else:
        print("noo")
    return None,None
        
        
        
        
# <aclass=gb1href="https://www.google.co.in/imghp?hl=en&tab=wi">Images</a>
# <aclass=gb1href="https://www.google.co.in/imghp?hl=en&amp;tab=wi">Images</a>