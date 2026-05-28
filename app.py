```python
import streamlit as st
import random

# =========================
# 页面基础配置
# =========================
st.set_page_config(
    page_title="생명과학 스마트 학습 시스템",
    page_icon="🧬",
    layout="centered"
)

# =========================
# 题库（韩英双语）
# =========================
questions = [
    {
        "id": 1,
        "question_kr": "병원균과 같은 감염원이 우리 몸 안으로 침입했을 때, 면역계는 이를 어떻게 '비자기(non-self)'로 인식하는가?",
        "question_en": "How does the immune system recognize invading pathogens as 'non-self'?",
        "options": {
            1: {
                "kr": "DNA 서열을 분석한다",
                "en": "By analyzing DNA sequences"
            },
            2: {
                "kr": "세포 수를 계산한다",
                "en": "By counting the number of cells"
            },
            3: {
                "kr": "병원체 관련 분자 패턴(PAMPs)을 탐지한다",
                "en": "By detecting pathogen-associated molecular patterns"
            },
            4: {
                "kr": "체온 변화를 감지한다",
                "en": "By detecting body temperature changes"
            }
        },
        "answer": 3
    },

    {
        "id": 2,
        "question_kr": "아나필락시스(anaphylaxis) 동안 히스타민(histamine)은 어디에서 방출되는가?",
        "question_en": "What is the source of histamine release during anaphylaxis?",
        "options": {
            1: {
                "kr": "간(Liver)",
                "en": "Liver"
            },
            2: {
                "kr": "대식세포(Macrophages)",
                "en": "Macrophages"
            },
            3: {
                "kr": "비만세포의 폭발적 탈과립",
                "en": "Explosive degranulation of mast cells"
            },
            4: {
                "kr": "적혈구(Red blood cells)",
                "en": "Red blood cells"
            }
        },
        "answer": 3
    },

    {
        "id": 3,
        "question_kr": "REM 수면의 특징으로 가장 적절한 것은?",
        "question_en": "Which of the following best describes REM sleep?",
        "options": {
            1: {
                "kr": "깊은 서파 수면",
                "en": "Deep slow-wave sleep"
            },
            2: {
                "kr": "꿈과 기억 공고화가 활발하다",
                "en": "Dreaming and memory consolidation are active"
            },
            3: {
                "kr": "뇌 활동이 거의 없다",
                "en": "Very little brain activity occurs"
            },
            4: {
                "kr": "눈 움직임이 없다",
                "en": "No eye movement occurs"
            }
        },
        "answer": 2
    },

    {
        "id": 4,
        "question_kr": "인슐린(insulin)을 분비하는 기관은?",
        "question_en": "Which organ secretes insulin?",
        "options": {
            1: {
                "kr": "간(Liver)",
                "en": "Liver"
            },
            2: {
                "kr": "췌장(Pancreas)",
                "en": "Pancreas"
            },
            3: {
                "kr": "소장(Small intestine)",
                "en": "Small intestine"
            },
            4: {
                "kr": "신장(Kidney)",
                "en": "Kidney"
            }
        },
        "answer": 2
    },

    {
        "id": 5,
        "question_kr": "세포의 에너지 발전소(powerhouse)라고 불리는 세포 소기관은?",
        "question_en": "Which organelle is known as the powerhouse of the cell?",
        "options": {
            1: {
                "kr": "핵(Nucleus)",
                "en": "Nucleus"
            },
            2: {
                "kr": "리보솜(Ribosome)",
                "en": "Ribosome"
            },
            3: {
                "kr": "미토콘드리아(Mitochondria)",
                "en": "Mitochondria"
            },
            4: {
                "kr": "골지체(Golgi apparatus)",
                "en": "Golgi apparatus"
            }
        },
        "answer": 3
    }
]

# =========================
# Session State 초기화
# =========================
if "current_index" not in st.session_state:
    st.session_state.current_index = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "answered" not in st.session_state:
    st.session_state.answered = False

if "selected" not in st.session_state:
    st.session_state.selected = None

if "wrong_questions" not in st.session_state:
    st.session_state.wrong_questions = []

if "shuffled" not in st.session_state:
    random.shuffle(questions)
    st.session_state.shuffled = True

# =========================
# 标题
# =========================
st.title("🧬 생명과학 스마트 학습 시스템")
st.subheader("Bioscience Smart Learning System")

st.markdown("---")

# =========================
# 当前题目
# =========================
idx = st.session_state.current_index
total_q = len(questions)

if idx < total_q:

    q = questions[idx]

    # 进度条
    progress = (idx + 1) / total_q

    st.progress(
        progress,
        text=f"진행도 Progress : {idx + 1} / {total_q}"
    )

    st.markdown(f"## 📘 문제 {idx + 1}")

    # 韩英双语题目
    st.info(
        f"""
🇰🇷 {q['question_kr']}

🇺🇸 {q['question_en']}
"""
    )

    # =========================
    # 选项显示
    # =========================
    option_map = {}

    for key, value in q["options"].items():

        display_text = (
            f"{key}. "
            f"{value['kr']} "
            f"({value['en']})"
        )

        option_map[display_text] = key

    selected = st.radio(
        "정답을 선택하세요 / Choose your answer:",
        list(option_map.keys()),
        index=None,
        disabled=st.session_state.answered
    )

    st.write("")

    # =========================
    # 提交答案
    # =========================
    if not st.session_state.answered:

        if st.button(
            "💥 정답 제출 Submit",
            type="primary",
            use_container_width=True
        ):

            if selected is None:
                st.warning("⚠️ 보기를 선택하세요! / Please select an option!")
            else:

                st.session_state.selected = selected
                st.session_state.answered = True

                selected_num = option_map[selected]

                if selected_num == q["answer"]:
                    st.session_state.score += 1
                else:
                    st.session_state.wrong_questions.append(q)

                st.rerun()

    # =========================
    # 显示结果
    # =========================
    else:

        selected_num = option_map[st.session_state.selected]

        correct_num = q["answer"]

        correct_option = q["options"][correct_num]

        if selected_num == correct_num:

            st.success(
                "🎯 정답입니다! Correct Answer!"
            )

        else:

            st.error(
                f"""
❌ 오답입니다! Wrong Answer!

정답:
{correct_num}. {correct_option['kr']}
({correct_option['en']})
"""
            )

        st.write("")

        # 下一题
        if st.button(
            "➡️ 다음 문제 Next Question",
            use_container_width=True
        ):

            st.session_state.current_index += 1
            st.session_state.answered = False
            st.session_state.selected = None

            st.rerun()

# =========================
# 全部完成
# =========================
else:

    st.balloons()

    final_score = st.session_state.score
    accuracy = (final_score / total_q) * 100

    st.success("🎉 모든 문제를 완료했습니다!")

    col1, col2 = st.columns(2)

    col1.metric(
        "최종 점수 Final Score",
        f"{final_score} / {total_q}"
    )

    col2.metric(
        "정답률 Accuracy",
        f"{accuracy:.1f}%"
    )

    st.markdown("---")

    # 错题本
    if len(st.session_state.wrong_questions) > 0:

        st.error(
            f"❌ 틀린 문제 수: {len(st.session_state.wrong_questions)}"
        )

        with st.expander("📚 틀린 문제 다시 보기 / Review Wrong Answers"):

            for wq in st.session_state.wrong_questions:

                st.markdown(
                    f"""
### 문제 {wq['id']}

🇰🇷 {wq['question_kr']}

🇺🇸 {wq['question_en']}
"""
                )

                correct = wq["answer"]

                st.success(
                    f"""
정답:
{correct}. {wq['options'][correct]['kr']}

({wq['options'][correct]['en']})
"""
                )

    # 重新开始
    if st.button(
        "🔄 처음부터 다시 시작 Restart",
        use_container_width=True
    ):

        st.session_state.current_index = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.session_state.selected = None
        st.session_state.wrong_questions = []

        random.shuffle(questions)

        st.rerun()
```

