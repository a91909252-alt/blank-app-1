import streamlit as st
import random
import time

# ==========================================
# 맞춤법 교정 및 역사적 사실에 맞게 수정된 문제 목록
# ==========================================
questions = [
    {"question": "제1차 세계 대전은 식민지를 둘러싼 제국주의 열강의 경쟁과 갈등이 심화되어 일어났다.", "answer": "O"},
    {"question": "삼국 동맹 소속이었던 이탈리아는 전쟁이 시작된 후 이탈하여 협상국 측에 가담하였다.", "answer": "O"},
    {"question": "제1차 세계 대전이 끝날 무렵 독일에서는 공화국이 수립되었다.", "answer": "O"},
    {"question": "제1차 세계 대전 중 레닌이 이끈 볼셰비키의 무장 봉기가 일어나 러시아 차르 체제가 무너졌다.", "answer": "X"},
    {"question": "에도 막부는 미국이 페리 함대를 보내 개항을 요구하자 이를 수용하고 개항하였다.", "answer": "O"},
    {"question": "일본 제국 헌법의 제정으로 천황의 권한이 제한되었고 자유 민권 운동의 요구가 적극적으로 수용되었다.", "answer": "X"},
    {"question": "아편 전쟁에서 패한 청은 개항하고 영국에 홍콩 할양, 공행 폐지 등을 규정한 불평등 조약을 맺었다.", "answer": "O"},
    {"question": "청은 난징 조약을 체결하여 크리스트교 선교를 허용하였다.", "answer": "X"},
    {"question": "서양 열강은 식민지를 확보하기 위해 군사력과 경제력을 앞세워 대외 팽창 정책을 추진하였는데 이를 제국주의라고 한다.", "answer": "O"},
    {"question": "영국은 횡단 정책을, 프랑스는 종단 정책을 추진하여 아프리카 분할을 주도하였다.", "answer": "X"},
    {"question": "서구 열강의 침략에서 벗어나기 위해 아프리카에서는 파쇼다 사건, 모로코 사건 등이 일어났다.", "answer": "X"},
    {"question": "산업 혁명은 영국에서 가장 먼저 시작되었다.", "answer": "O"},
    {"question": "산업화의 양상은 각국의 상황에 따라 다르게 나타났다.", "answer": "O"},
    {"question": "독일에서는 중공업이 발달하여 대규모 자본이 필요하였기 때문에 국가 주도로 산업화가 진행되었다.", "answer": "O"},
    {"question": "산업 사회가 형성되면서 자본가와 노동자 간의 빈부 격차가 줄어들었다.", "answer": "X"},
    {"question": "마르크스와 엥겔스는 노동자의 단결과 계급 투쟁을 주장하였다.", "answer": "O"},
    {"question": "빈 체제에서 유럽 각국의 자유주의와 민족주의 운동은 탄압받았다.", "answer": "O"},
    {"question": "차티스트 운동의 결과 영국에서 여성들이 선거권을 갖게 되었다.", "answer": "X"},
    {"question": "삼부회에서 표결 방식을 두고 제1, 2신분은 머릿수 표결 방식을, 제3신분은 신분별 표결 방식을 요구하면서 대립하였다.", "answer": "X"},
    {"question": "프랑스 혁명은 시민 사회를 형성하고 자본주의 발전의 토대를 마련하였다.", "original_idx": 21, "answer": "O"},
    {"question": "나폴레옹은 《나폴레옹 법전》을 편찬하여 법 앞에서의 평등과 재산 소유권을 보장하였다.", "answer": "O"},
    {"question": "18세기 초 영국의 북아메리카 동부 지역 13개 식민지는 독자적인 의회를 설치하여 실질적인 자치를 누렸다.", "answer": "O"},
    {"question": "보스턴 차 사건을 계기로 영국의 북아메리카 식민지는 독립 전쟁을 시작하였다.", "answer": "O"},
    {"question": "미국 혁명은 프랑스 혁명의 영향을 받았고 라틴아메리카의 독립에 자극을 주었다.", "answer": "X"},
    {"question": "르네상스 이후 천문학의 발전은 유럽인의 의식을 크게 변화시켰다.", "answer": "O"},
    {"question": "갈릴레이는 《천체의 회전에 관하여》라는 책에서 천동설을 대체하는 지동설을 주장하였다.", "answer": "X"},
    {"question": "계몽사상은 인간의 이성을 바탕으로 낡은 관습과 미신을 타파함으로써 사회가 진보할 수 있다는 사상이다.", "answer": "O"},
    {"question": "로크는 인간의 자연 상태를 만인에 대한 만인의 투쟁으로 파악하고 사회 혼란을 막기 위해 개인이 정치적 권리를 군주에게 양도해야 한다고 보았다.", "answer": "X"}
]

# 1. 세션 상태 초기화 (처음 실행할 때 딱 한 번만 작동)
if 'quiz_list' not in st.session_state:
    st.session_state.quiz_list = random.sample(questions, len(questions)) # 문제 랜덤 셔플
    st.session_state.current_idx = 0
    st.session_state.score = 0

# 앱 제목 설정
st.title("🌍 세계사 수행평가 O/X 퀴즈")
st.markdown("---")

total_q = len(st.session_state.quiz_list)
current_idx = st.session_state.current_idx

# 모든 문제를 다 푼 경우
if current_idx >= total_q:
    st.balloons() # 축하 효과
    st.success(f"🎉 모든 문제를 완료했습니다! 당신의 점수는 **{st.session_state.score} / {total_q}** 입니다.")
    
    if st.button("처음부터 다시 도전하기"):
        # 세션 초기화 후 재실행
        st.session_state.quiz_list = random.sample(questions, len(questions))
        st.session_state.current_idx = 0
        st.session_state.score = 0
        st.columns(1) # 화면 갱신용 dummy
        st.rerun()

# 문제가 남아있는 경우
else:
    # 상단 진행률 표시 바
    progress_val = current_idx / total_q
    st.progress(progress_val)
    st.write(f"현재 진행도: {current_idx + 1} / {total_q} 문제")
    
    # 문제 출제
    current_q = st.session_state.quiz_list[current_idx]
    st.info(f"**Q. {current_q['question']}**")
    
    st.write("") # 간격 띄우기
    
    # O, X 버튼 배치
    col1, col2 = st.columns(2)
    user_choice = None
    
    with col1:
        if st.button("⭕ O", use_container_width=True, type="primary"):
            user_choice = "O"
    with col2:
        if st.button("❌ X", use_container_width=True, type="secondary"):
            user_choice = "X"
            
    # 사용자가 버튼을 눌렀을 때의 판정 로직
    if user_choice is not None:
        correct_answer = current_q['answer']
        
        if user_choice == correct_answer:
            # 맞았을 때 피드백
            st.success("## ⭕ 정답입니다!")
            st.session_state.score += 1
            time.sleep(1.2) # 1.2초 대기 후 다음 문제로
            st.session_state.current_idx += 1
            st.rerun()
        else:
            # 틀렸을 때 피드백 및 정답 노출
            st.error(f"## ❌ 틀렸습니다! \n\n 이 문제의 정답은 **[{correct_answer}]** 입니다.")
            time.sleep(3.0) # 답을 읽을 수 있게 3초 대기 후 다음 문제로
            st.session_state.current_idx += 1
            st.rerun()

