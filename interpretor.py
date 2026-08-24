import streamlit as st
st.set_page_config(layout="wide", initial_sidebar_state="expanded")

simple=st.sidebar.toggle("Mode résumé",1)
debug=st.sidebar.toggle("debug",0)
dataf=st.sidebar.toggle("Disposition tableau",0)
if 'data' not in st.session_state:
    fichier=open("data.txt","r",encoding="UTF-8")
    data=fichier.read().split("---")[1:]
    fichier.close()
    dic={}
    d=[data[i].split("--") for i in range(len(data))]
    for i in range(len(d)):
        dic[d[i][0]]=d[i][1:]
    # dic.keys
    for i in dic.keys():
        for j in range(len(dic[i])):
            k=dic[i][j].split("||")
            if len(k)<3:
                k+=[k[-1]]
            dic[i][j]=k
    st.session_state['data']=dic
if debug : st.session_state['data']
tabs=st.tabs(list(st.session_state['data'].keys()))

if dataf : 
    for cat in st.session_state['data'].keys():
        tabs[list(st.session_state['data'].keys()).index(cat)].dataframe(st.session_state['data'][cat],column_config={1:"Nom",2:"Explication",3:"résumé"})
else : 
    for cat in st.session_state['data'].keys():
        k=list(st.session_state['data'].keys()).index(cat)
        q=len(st.session_state['data'][cat])//4 +1
        r=len(st.session_state['data'][cat])%4
        if debug : 
            st.dataframe(st.session_state['data'][cat])
            cat
            q,r
        cont=[tabs[list(st.session_state['data'].keys()).index(cat)].container(key=str(i)+"cont"+str(cat)) for i in range(q-int(r==0))]
        cols=[cont[i].columns(4) for i in range(len(cont))]
        for i in range(q-int(r==0)):

            for j in range(4+(r-4)*int(i==q-int(r==0)-1)):
                
                cols[i][j].expander(st.session_state['data'][cat][i*4+j][0]).text(st.session_state['data'][cat][i*4+j][1+int(simple)])
        
    



