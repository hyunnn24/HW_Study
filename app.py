import streamlit as st

def Abstract():
    st.write("this page works well")
def Autodesek_Fusion():
    st.write("this page works well")
def PCB_Basic():
    st.write("this page works well")
def Projects():
    st.write("this page works well")
def Advanced():
    st.write("this page works well")

#페이지 
page = st.sidebar.selectbox("HW STUDY", ["Abstract","Autodesek Fusion","PCB Basic","Projects (Open Source)", "Advanced (Optional)"])
st.sidebar.text("  made by hyunnn :kr: \n  CERT-IS PKNU \n  2024.09.13")

if page == "Abstract":
    Abstract()
elif page == "Autodesek Fusion":
    Autodesek_Fusion()
elif page == "PCB Basic":
    PCB_Basic()
elif page == "Projects (Open Source)":
    Projects()
elif page == "Advanced (Optional)":
    Advanced()
#elif page == "":

#elif page == "":