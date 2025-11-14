import streamlit as st
from PIL import Image

st.markdown("---")
st.title(" 👩‍💻👨‍💻 Development Team")

st.markdown("""This is the team of developers who made CLAWRIF-AI possible. 
			If there are any doubts about the development of the app, 
			the deployment of the app to the cloud, or even the app itself, please feel free to reach out to any of them. 
			They will be happy to answer your questions.""")

st.write("")

#Fixing the images
## joy
joy_image = Image.open("assets/samir_image.jpg")
joy_image = samir_image.resize((300, 300))

## antonio
antonio_image = Image.open("assets/alejandro_image.jpg")
antonio_image = alejandro_image.resize((300, 300))

## ruben
ruben_image = Image.open("assets/thomas_image.jpg")
ruben_image = thomas_image.resize((300, 300))

## pablo
pablo_image = Image.open("assets/nour_image.jpg")
pablo_image = nour_image.resize((300, 300))

## andres
andres_image = Image.open("assets/joy_image.jpg")
andres_image = joy_image.resize((300, 300))

#continue here to add pics
col1,col2,col3,col4,col5=st.columns(5)
with col1:
    st.image(joy_image)
    st.markdown('*Joy Zhong*')
    
with col2:
	st.image(antonio_image)
	st.markdown('*Antotnio*')
	
	
with col3:
	st.image(ruben_image)
	st.markdown('*Ruben*')
	
	
with col4:
	st.image(pablo_image)
	st.markdown('*Pablo*')
	
	
with col5:
	st.image(andres_image)
	st.markdown('*Andres*')
	
st.write("")

st.subheader("GitHub Repo")

st.markdown("""This is an OpenSource project. Therefore, the GitHub repository which the includes the code 
			used to carry out this project can be found following this link: 
			https://github.com/thomasrenwickm/Paramo_GPT""")
	




