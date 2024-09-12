import streamlit as st

def Intro():
    st.write("1. 하드웨어 설계 기초 및 기초 회로 이론 스터디
이 스터디는 오토데스크 Fusion 360의 3D 모델링 및 전자 설계 기능을 활용하여 하드웨어 설계의 기초부터 기초 회로 이론까지 학습하는 과정입니다. 3D 모델링을 통한 제품 설계, 기초 전자 회로 설계, 그리고 이를 기반으로 한 실제 프로토타입 제작을 경험할 수 있습니다. 이론과 실습을 결합하여 전자 기기 설계의 기본을 익히고, 간단한 프로젝트를 통해 학습 성과를 직접 확인할 수 있습니다.

2. PCB 제작 및 하드웨어 수리 실습 스터디
이 스터디는 PCB 제작과 만능기판을 이용한 회로 제작, 납땜 및 SMD 솔더링 기술을 배우고 실습하는 과정입니다. 더 나아가 히팅건을 사용한 메모리 또는 AP(애플리케이션 프로세서) 스왑과 같은 고급 하드웨어 수리 기술도 실습합니다. 이 과정을 통해 참가자는 실제 하드웨어 제작과 수리 경험을 쌓고, 이를 통해 전자 기기 수리와 유지보수의 기본을 확실히 다질 수 있습니다.

")
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
page = st.sidebar.selectbox("HW STUDY", ["Introduction","Abstract","Autodesek Fusion","PCB Basic","Projects (Open Source)", "Advanced (Optional)"])
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
elif page == "Introduction":
    Intro()

#elif page == "":