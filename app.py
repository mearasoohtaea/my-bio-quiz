import streamlit as st

# 页面基础配置
st.set_page_config(page_title="生命科学智能刷题网页版", page_icon="🧬", layout="centered")

# 已人工精密修复：完美融合原35道题与新题库，无误删，共45道核心题
questions = [
  {
    "id": 1,
    "question": "1. 병원균과 같은 감염원이 우리 몸 안으로 침입했을 때, 우리 몸의 면역 체계는 이러한 감염원이 이물질이고 “비자기(non-self)”인지 어떤 방식으로 결정하는가?\n(When pathogens, such as infectious agents, invade our body, how does the immune system determine that these invaders are foreign and \"non-self\"?)",
    "options": {"1": "DNA 서열을 분석함으로써 (By analyzing DNA sequences)", "2": "세포 수를 계산하여 (By counting the number of cells)", "3": "감염원과 관련된 분자 패턴을 탐지함으로써 (By detecting molecular patterns associated with infectious agents)", "4": "체온을 평가하여 (By assessing body temperature)"},
    "answer": "3"
  },
  {
    "id": 2,
    "question": "2. 알레르기 항원 (allergen)이 혈액을 떠돌며 전신의 면역 체계를 활성화할 경우 여러 과정을 거쳐 히스타민 (histamine)이 방출되어 아나필락시스를 유발할 수 있다. 아나필락시스 동안 히스타민 방출의 원인은 무엇인가?\n(What is the source of histamine release during anaphylaxis?)",
    "options": {"1": "에피네프린 주사 (Epinephrine injection)", "2": "대식세포 (Macrophages)", "3": "비만세포의 폭발적인 탈과립화 (Explosive degranulation of mast cells)", "4": "간에서 생산 (Production by the liver)"},
    "answer": "3"
  },
  {
    "id": 3,
    "question": "3. 항온동물은 체온을 일정하게 유지함으로써 진화적 이점을 얻었다. 항온동물은 변온동물과 비교할 때, 에너지 소비와 생존 능력에 있어 어떤 환경에서 어떤 진화적 이점을 가지게 되었는가?\n(Endotherms have gained an evolutionary advantage by maintaining a constant body temperature.)",
    "options": {"1": "항온동물은 변온동물보다 더 많이 먹어야 한다.", "2": "항온동물은 오랫동안 먹지 않고도 살 수 있다.", "3": "항온동물은 더 추운 기후에서 살 수 있다. (Endotherms can live in colder climate.)", "4": "항온동물은 변온동물보다 작아질 수 있다.", "5": "항온동물은 낮에 변온동물과 더 잘 먹기 위해 경쟁할 수 있다."},
    "answer": "3"
  },
  {
    "id": 4,
    "question": "4. 사람이 ‘나는 이 일을 하도 오랫동안 해 와서 눈 감고도 할 수 있어.’ 라고 말했다면 이 사람은 어떤 일을 하는 건 아마도 굳이 눈으로 보지 않고도 내 팔과 다리가 어느 위치에 어떤 상태인지 알 수 있기 때문일 것이다. 이것은 어떤 감각에 해당하는가?\n(What is this sensation called?)",
    "options": {"1": "시각 (Vision)", "2": "후각 (Olfaction)", "3": "촉각 (Tactile sensation)", "4": "고유감각 (Proprioception)", "5": "내수용감각 (Interoception)"},
    "answer": "4"
  },
  {
    "id": 5,
    "question": "5. 수면의 여러 단계 중 하나로, 이 단계에서는 눈이 빠르게 움직이고 뇌파 활동이 활발하며 기억의 공고화에 중요한 역할을 한다고 알려져 있다. 또한 이 단계에서는 꿈이 활발하게 일어나고 비교적 잘 기억할 수 있다. 이 단계의 수면을 무엇이라고 하는가?\n(What is this stage of sleep called?)",
    "options": {"1": "서파 수면 (Slow-wave sleep)", "2": "얕은 수면 (light sleep)", "3": "비렘 수면 (Non-REM sleep)", "4": "렘 수면 (REM sleep)"},
    "answer": "4"
  },
  {
    "id": 6,
    "question": "6. 인플루엔자 바이러스가 갖고 있는 단백질 중 하나로, 숙주 세포의 표면에 붙어서 바이러스가 세포 안으로 들어가도록 돕는 것은 무엇인가?\n(Which protein found in the influenza virus helps the virus attach to the surface of host cells?)",
    "options": {"1": "헤마글루티닌 (Hemagglutinin)", "2": "뉴라민분해효소 (Neuraminidase)", "3": "복제효소 (Polymerase)", "4": "캡시드 단백질 (Nucleocapsid)"},
    "answer": "1"
  },
  {
    "id": 7,
    "question": "7. SARS-CoV-2 (COVID-19) 는 주로 호흡을 통해 다른 사람에게 전파되기 때문에, 2019년 말에 시작된 팬데믹 이후로 정부에서 마스크 착용을 의무화하였다. 이것은 바이러스의 어떠한 감염 방식인가?\n(What type of infection method does this represent?)",
    "options": {"1": "비말감염 (droplet infection)", "2": "곤충 매개 감염 (insect-mediated infection)", "3": "혈액 감염 (blood infection)", "4": "성적 접촉 (sexual contact)"},
    "answer": "1"
  },
  {
    "id": 8,
    "question": "8. 특정 질병의 다양한 변종 또는 여러 관련 질병에 대해 폭넓은 면역 보호를 제공하는 백신인 범용백신 (universal vaccine)에 대한 설명으로 옳지 않은 것은 무엇인가?\n(Which of the following is incorrect regarding the universal vaccine?)",
    "options": {"1": "범용백신은 특정 질병에 대해 장기적인 면역을 제공하기 위해 개발된다.", "2": "범용백신 is 여러 바이러스의 변종에 대해 동시에 면역을 생성할 수 있도록 설계된다.", "3": "범용백신은 한 가지 백신으로 모든 질병을 예방할 수 있도록 개발된다.", "4": "범용백신은 기존 백신보다 면역 반응을 보다 넓은 범위에서 유도하도록 목표로 한다."},
    "answer": "1"
  },
  {
    "id": 9,
    "question": "9. 혈액에서 혈구 (적혈구, 백혈구, 혈소판)와 혈장을 제거하고 남은 투명한 액체로... 호르몬 검사를 하거나 질병을 진단할 때 중요한 역할을 하는 이 물질은 무엇인가요?\n(What is the substance that remains as a clear liquid after removing blood cells?)",
    "options": {"1": "혈구 (hemocyte)", "2": "혈장 (plasma)", "3": "혈청 (serum)", "4": "림프 (lymph)"},
    "answer": "3"
  },
  {
    "id": 10,
    "question": "10. 다음 설명에 알맞은 용어를 고르시오.\n[생물체 내에서 산화스트레스를 받아서 생성되는 산소의 화합물로, 생체 조직을 공격하고 세포를 손상시키며 노화를 일으키는 산화력이 강한 산소.]",
    "options": {"1": "과산화(peroxidation)", "2": "항산화제(antioxidant)", "3": "활성산소(reactive oxygen species)", "4": "산화환원반응(redox)"},
    "answer": "3"
  },
  {
    "id": 11,
    "question": "11. 다음 중 잠이 가지는 기능으로 보기 어려운 것은? (Which of the following is least likely to be considered a function of sleep?)",
    "options": {"1": "성장호르몬 분비를 통한 성장 촉진", "2": "면역 기능의 항진", "3": "주간에 얻은 정보의 처리", "4": "뇌의 노폐물 제거", "5": "뇌세포의 분화 (Differentiation of brain cells)"},
    "answer": "5"
  },
  {
    "id": 12,
    "question": "12. 세포를 둘러싸고 있는 얇은 막으로 세포의 기능과 생명 유지에 중요한 역할을 하는 세포막에 대한 설명 중 틀린 것은?",
    "options": {"1": "细胞膜由脂质双层组成并具有流动性", "2": "细胞膜是划分细胞内外的界限", "3": "细胞膜上存在发挥多种功能的蛋白质", "4": "세포막의 안쪽 면과 바깥쪽 면의 구성은 동일하다. (The inner and outer layers have the same composition.)"},
    "answer": "4"
  },
  {
    "id": 13,
    "question": "13. 인슐린은 인체에서 중요한 호르몬으로 체내 혈당 수치를 조절하는 역할을 한다... 이런 인슐린이 분비되는 기관은?\n(In which organ is insulin secreted?)",
    "options": {"1": "간 (Liver)", "2": "뇌 (Brain)", "3": "췌장 (Pancreas)", "4": "소장 (Small intestine)"},
    "answer": "3"
  },
  {
    "id": 14,
    "question": "14. 체세포에서 일어나는 일반적인 분열과 다르게 생식세포에서는 두 번의 분열로 4개의 반수체가 생성되는 분열 방식의 명칭은?\n(What is this division process in gamete cells called?)",
    "options": {"1": "반수분열 (haploid division)", "2": "유사분열 (mitosis)", "3": "감수분열 (meiosis)", "4": "세포질분열 (cytokinesis)"},
    "answer": "3"
  },
  {
    "id": 15,
    "question": "15. 찰스 다윈은 일부 특성은 생존과 번식 성공을 촉진할 가능성이 더 높으며, 따라서 이러한 특성이 다음 세대로 전달됨을 주장하였는데, 이를 뜻하는 명칭은?\n(What is this concept?)",
    "options": {"1": "우성 법칙", "2": "혼합 유전", "3": "적응 선택", "4": "자연 선택 (natural selection)"},
    "answer": "4"
  },
  {
    "id": 16,
    "question": "16. 우리 신체의 면역 체계를 활용하여 암과 싸우는 일종의 암 치료법의 이름은?\n(What is the name of the therapy that harnesses the body's immune system to fight cancer?)",
    "options": {"1": "호르몬 치료", "2": "줄기세포 이식", "3": "면역치료 (Immunotherapy)", "4": "수술"},
    "answer": "3"
  },
  {
    "id": 17,
    "question": "17. \"건강수명(Healthspan)\" 용어에 알맞은 설명을 고르시오.",
    "options": {"1": "오래 사는 것은 항상 좋은 것이다.", "2": "역노화 연구 분야의 중점은 질병에 시간을 적게 보내면서 오래 사는 방법을 찾는 것이다. (Focus on spending less time in disease.)", "3": "실제로 100세까지 살아가는 사람들은 질병을 겪는 시간이 길다.", "4": "기대수명과 건강수명은 의미가 같다."},
    "answer": "2"
  },
  {
    "id": 18,
    "question": "18. 다음 중 오른손잡이에서 왼쪽 뇌가 손상되었을 때 주로 나타날 수 있는 증상이 아닌 것은?",
    "options": {"1": "말의 유창성이 떨어진다.", "2": "이름 말하기를 못하게 된다.", "3": "실행증이 나타나게 된다.", "4": "옷 입기 능력이 떨어지게 된다. (Decreased ability to dress)", "5": "계산 능력이 떨어지게 된다."},
    "answer": "4"
  },
  {
    "id": 19,
    "question": "19. 생명공학이 적용되는 특정 분야 중 식물생명공학을 대표하는 색깔은 무엇입니까?\n(Which color represents plant biotechnology?)",
    "options": {"1": "레드 바이오테크놀로지", "2": "그린 바이오테크놀로지 (green biotechnology)", "3": "화이트/그레이 바이오테크놀로지", "4": "옐로우 바이오테크놀로지"},
    "answer": "2"
  },
  {
    "id": 20,
    "question": "20. 뇌의 기저핵에서 분비되며 보상, 동기 부여, 감정 조절에 관여하고 '행복 호르몬'이라 불리는 물질 A는 무엇인가?\n(Often called a 'happiness hormone,' involved in reward and motivation. What is substance A?)",
    "options": {"1": "아드레날린", "2": "도파민 (Dopamine)", "3": "옥시토신", "4": "엔도르핀", "5": "멜라토닌"},
    "answer": "2"
  },
  {
    "id": 21,
    "question": "21. 다음 중 프리바이오틱스(Prebiotics)에 대한 설명 중 틀린 것을 고르시오.",
    "options": {"1": "장내 세균에 의해 분해되면 SCFAs가 생성된다.", "2": "사람의 소화효소에 의해 분해되지 않는다.", "3": "과일, 채소 등에 존재하는 식이섬유를 일컫는다.", "4": "최대한의 효과를 위해서 프로바이오틱스와 함께 섭취하는 것이 권장된다."},
    "answer": "4"
  },
  {
    "id": 22,
    "question": "22. 다음 설명에 알맞은 용어를 고르시오.\n[ CRISPR-Cas9 시스템의 Cas9 단백질을 특정 DNA 서열로 안내하는 RNA 분자 ]",
    "options": {"1": "가이드 RNA (gRNA)", "2": "테라토마", "3": "오가노이드", "4": "분화 완료 세포"},
    "answer": "1"
  },
  {
    "id": 23,
    "question": "23. 인체와 오랜 기간 공동 진화를 거쳐온 미생물 집단으로, 면역 기능 조절 및 소화를 돕는 이것은 무엇인가?\n(Collection of microorganisms part of human body over long period of co-evolution...?)",
    "options": {"1": "세균", "2": "전생명체", "3": "프로바이오틱스", "4": "인간 마이크로바이옴(Human microbiome)"},
    "answer": "4"
  },
  {
    "id": 24,
    "question": "24. 관상동맥의 동맥경화반(Atherosclerotic plaque)은 주로 어떤 물질로 이루어져 있는지 고르시오.\n(What materials are the main compositions of this atherosclerotic plaque?)",
    "options": {"1": "칼슘과 인", "2": "지질과 콜레스테롤 (lipid and cholesterol)", "3": "당류와 단백질", "4": "철분과 마그네슘"},
    "answer": "2"
  },
  {
    "id": 25,
    "question": "25. 조직 배양 기술을 통해 어떤 부분을 잘라내도 전체 식물을 재생할 수 있는 식물의 특징은 무엇인가?\n(Regeneration of an entire plant from any part. What is this characteristic?)",
    "options": {"1": "식물의 전능성 (totipotency of plants)", "2": "식물의 다양성", "3": "광합성", "4": "식물 호르몬"},
    "answer": "1"
  },
  {
    "id": 26,
    "question": "26. 뇌를 좌우 반구로 구분하였을 때, 각 영역에서 담당하는 기능에 대해 잘못 연결된 것을 고르시오.",
    "options": {"1": "좌뇌 - 언어", "2": "좌뇌 - 집중력 (Attention)", "3": "좌뇌 - 계산 능력", "4": "우뇌 - 길 찾기", "5": "우뇌 - 감정"},
    "answer": "2"
  },
  {
    "id": 27,
    "question": "27. 염색체 끝에 있는 반복적인 DNA 염기서열 영역으로 염색체 끝이 닳지 않도록 보호하는 ( A )는?\n(Repetitive DNA sequences protecting the ends of chromosomes.)",
    "options": {"1": "올리고뉴클레오타이드", "2": "텔로미어(Telomere)", "3": "텔로미어레이즈", "4": "셀터린 복합체"},
    "answer": "2"
  },
  {
    "id": 28,
    "question": "28. 다음 중 식물의 방어 기작 중 화학적 방어에 해당하지 않는 것은 무엇인가?\n(Which of the following is not an example of a chemical defense?)",
    "options": {"1": "독소", "2": "왁스층 (wax layer)", "3": "글루코시놀레이트", "4": "알칼로이드"},
    "answer": "2"
  },
  {
    "id": 29,
    "question": "29. 특정 유전자를 완전히 제거하거나 비활성화하여 표현형의 변화를 관찰하는 기술은?\n(Disabling a gene to observe the effects on an organism's phenotype.)",
    "options": {"1": "유전자 삽입", "2": "세포 재프로그래밍", "3": "유전자 노크아웃 (gene knock-out)", "4": "유전자 치료"},
    "answer": "3"
  },
  {
    "id": 30,
    "question": "30. 다음 중 SARS-CoV-2 mRNA 백신에 대한 explanation으로 틀린 것은 무엇일까요?\n(Which of the following statements about the mRNA vaccine is incorrect?)",
    "options": {"1": "일반적으로 예방접종 후 면역을 획득하기까지 24시간 이내의 시간이 소요된다. (Takes less than 24h)", "2": "mRNA 는 스파이크 단백질을 합성하도록 설계할 수 있다", "3": "mRNA 는 lipid nanoparticle 에 포장되어 전달된다", "4": "근육세포는 단백질 항원 제시를 통해 면역세포를 자극한다."},
    "answer": "1"
  },
  {
    "id": 31,
    "question": "31. 시각 정보가 처리되어 사물, 색깔 등을 인지하는 what pathway와 위치, 방향을 판단하는 where pathway가 시작되는 뇌 영역은?",
    "options": {"1": "전두엽", "2": "측두엽", "3": "두정엽", "4": "후두엽 (Occipital Lobe)", "5": "소뇌"},
    "answer": "4"
  },
  {
    "id": 32,
    "question": "32. 알츠하이머병 환자가 기억 상실, 길 잃음 등의 증상을 보일 때 주로 손상된 뇌 영역은?\n(What is the brain area primarily associated with memory loss in Alzheimer's?)",
    "options": {"1": "해마 (Hippocampus)", "2": "편도체", "3": "시상하부", "4": "후각망울", "5": "띠이랑"},
    "answer": "1"
  },
  {
    "id": 33,
    "question": "33. 자가 복제와 분화 두 가지 능력을 갖춘 미분화된 세포는 무엇인가?\n(Undifferentiated cells with the ability to proliferate and differentiate.)",
    "options": {"1": "체세포", "2": "줄기 세포 (stem cell)", "3": "전분포능 세포", "4": "유망 세포"},
    "answer": "2"
  },
  {
    "id": 34,
    "question": "34. 다음 중 유도만능줄기세포(iPSC) 기술로 인해 해결된 문제가 아닌 것은?\n(Which of the following is not an issue resolved by the advent of iPSC technology?)",
    "options": {"1": "면역거부", "2": "인간 난자의 사용", "3": "배아의 파괴", "4": "이식 후 종양 발생(Formation of tumor after transplantation)"},
    "answer": "4"
  },
  {
    "id": 35,
    "question": "35. 다음 중 세 가지 주요 식물 2차 대사산물(Secondary metabolites)에 속하지 않는 것은 무엇인가?",
    "options": {"1": "진세노사이드 (Ginsenosides)", "2": "페놀릭류 (Phenolics)", "3": "테르펜류 (Terpenes)", "4": "알칼로이드 (Alkaloids)"},
    "answer": "1"
  },
  
  # === 🚨 【完美复活】原35题里的第34题（新生血管题），排在第36题 ===
  {
    "id": 36,
    "question": "36. 암세포가 계속 자라나기 위해서는 산소와 영양분을 공급받아야 하므로 새로운 혈관을 만들어내야 한다. 이러한 과정을 무엇이라 하는가?\n(In order for cancer cells to continue growing, they must receive oxygen and nutrients, so they must create new blood vessels. What is this process called?)",
    "options": {
      "1": "① 新生血管 (종양 혈관신생 / Tumor angiogenesis)", 
      "2": "② 세포 사멸 (세포 자살 / Apoptosis)", 
      "3": "③ 면역 회피 (Immune evasion)", 
      "4": "④ 대사 변화 (Metabolic alteration)"
    },
    "answer": "1"
  },

  # === 以下为高级核心题库归位 (题号 37-45) ===
  {
    "id": 37,
    "question": "37. 다음 용어에 알맞은 설명을 고르시오. Choose the appropriate description for the following terminology.\n[ RNA virus (알엔에이 바이러스) / RNA病毒 ]",
    "options": {
      "1": "유전 물질로 아르엔에이를 가지고 있는 바이러스. (A virus in which the genetic information is stored in the form of RNA (as opposed to DNA).) / 遗传信息以RNA形式存储的病毒(与DNA相反)",
      "2": "유전 물질로 디엔에이를 가지고 있는 바이러스. (A virus in which the genetic information is stored in the form of DNA.)",
      "3": "단백질 껍질이 없는 바이러스. (A virus without a protein coat.)"
    },
    "answer": "1"
  },
  {
    "id": 38,
    "question": "38. 다음 용어에 알맞은 설명을 고르시오. Choose the appropriate description for the following terminology.\n[ 촉진 확산 (facilitated diffusion) / 促进扩散 ]",
    "options": {
      "1": "에너지를 소모하여 물질을 농도 경사에 역행하여 수송하는 현상. (Active transport utilizing ATP.)",
      "2": "이동은 물질과 막에 포함된 채널 또는 단백질 사이의 결합에 의존한다. (The transport relies on binding between the matter and the membrane-embedded channel or carrier protein.) / 运输依赖于物质与膜内包含的通道或载体蛋白的结合作用。",
      "3": "세포막이 인지질 2중층을 통해 물질이 직접 확산되는 현상. (Simple diffusion directly through lipid bilayer.)"
    },
    "answer": "2"
  },
  {
    "id": 39,
    "question": "39. 암세포가 전이하기 위하여 상피세포의 특징을 잃고 중간엽세포의 특징을 얻는 과정은 무엇인가?\n(What is the process that cancer cells do for metastasis by changing from an epithelial cell into a mesenchymal cell?) / 癌细胞在转移前会失去上皮细胞的特性并获得间充质细胞的特征,这一过程是什么?",
    "options": {
      "1": "EMT (epithelial-mesenchymal transition) / 上皮-间充质转化(EMT)",
      "2": "Apoptosis / 细胞凋亡",
      "3": "Angiogenesis / 血管生成",
      "4": "Endocytosis / 胞吞作用"
    },
    "answer": "1"
  },
  {
    "id": 40,
    "question": "40. 다음 설명에 알맞은 용어를 고르시오. Choose the appropriate term for the following description.\n[ 진핵세포에 존재하는 대형의 구상 내지는 타원형의 구조, 세포의 여러 가지 활동을 규정하는 유전자를 내부에 포함한다. 적혈구를 제외하고 거의 모든 세포에 존재하는 세포 소기관. ] / 真核细胞中存在的大型球形或椭圆形结构,包含调节各种细胞活动的基因,几乎存在于除红细胞外的所有细胞中",
    "options": {
      "1": "미토콘드리아 (mitochondria) / 线粒体",
      "2": "리보솜 (ribosome) / 核糖体",
      "3": "핵 (nucleus) / 细胞核",
      "4": "골지체 (Golgi apparatus) / 高尔基体"
    },
    "answer": "3"
  },
  {
    "id": 41,
    "question": "41. 세포막에 대한 설명 중 틀린 것은? (Which of the following statements concerning the cell membrane is false?) / 下列关于细胞膜的叙述错误的是?",
    "options": {
      "1": "세포막은 지질 2중층으로 구성되어 있다. (Cell membrane consists of a lipid bilayer.)",
      "2": "어떤 물질도 세포막을 통과할 수 없다. (No substance can pass through the cell membrane.) / 没有物质可以通过细胞膜",
      "3": "세포막에는 다양한 단백질이 존재한다. (Various proteins are embedded in the membrane.)"
    },
    "answer": "2"
  },
  {
    "id": 42,
    "question": "42. 다음 중 이차 능동수송에 대한 설명은? (Which of the following explanations is secondary active transport?) / 下列哪一项是关于次级主动运输的描述?",
    "options": {
      "1": "분자가 농도 경사를 따라 이동할 때, 다른 분자는 농도경사를 거슬러 이동한다. (A molecule is moved down its concentration gradient as another is moved up its concentration gradient.) / 分子沿着浓度阶梯移动,而其他分子则逆着浓度阶梯移动",
      "2": "ATP를 직접 소모하여 물질을 수송한다. (Directly utilizes ATP for transport.)",
      "3": "단백질 통로 없이 직접 세포막을 통과한다. (Passes through membrane without proteins.)"
    },
    "answer": "1"
  },
  {
    "id": 43,
    "question": "43. 다음 중 모든 생명체의 기본 구성요소는? (Which of the following examples is the basic building block of all living things?) / 下列哪一项是所有生命体的基本组成部分?",
    "options": {
      "1": "조직 (tissue) / 组织",
      "2": "기관 (organ) / 器官",
      "3": "세포 (cell) / 细胞",
      "4": "원자 (atom) / 原子"
    },
    "answer": "3"
  },
  {
    "id": 44,
    "question": "44. 다음 중 사회적 감정으로 간주될 수 있는 것은? (Which of the following can be regarded as social emotion?) / 下列哪一项可以被视为社会感情?",
    "options": {
      "1": "공포 (Fear) / 恐惧",
      "2": "분노 (Anger) / 愤怒",
      "3": "죄책감 (Guilt) / 内疚感",
      "4": "기쁨 (Joy) / 喜悦"
    },
    "answer": "3"
  },
  {
    "id": 45,
    "question": "45. 다음 중 화학적 발암물질이 아닌 것은? (Which of the following is not a chemical carcinogen?) / 下列哪一项不是化学致癌物质?",
    "options": {
      "1": "벤젠 (Benzene)",
      "2": "방사선 (ionizing radiation) / 辐射",
      "3": "담배 연기 (Tobacco smoke)",
      "4": "포름알데히드 (Formaldehyde)"
    },
    "answer": "2"
  }
]

# 网页前端渲染逻辑
st.title("🧬 生命科学的世界 (The World of Bioscience)")
st.subheader("生命科学原题刷题系统 (全题库高能去重版)")
st.markdown("---")

if 'current_index' not in st.session_state:
    st.session_state.current_index = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'is_answered' not in st.session_state:
    st.session_state.is_answered = False
if 'selected_option' not in st.session_state:
    st.session_state.selected_option = None

idx = st.session_state.current_index
total_q = len(questions)

if idx < total_q:
    q_data = questions[idx]
    
    st.progress(idx / total_q, text=f"当前复习进度: {idx}/{total_q} 题")
    st.write(f"### **第 {idx + 1} 题**")
    st.info(q_data['question'])
    
    options_list = [f"{key}. {value}" for key, value in q_data['options'].items()]
    
    user_choice = st.radio(
        "请选择你的答案：", 
        options_list, 
        index=None if st.session_state.selected_option is None else options_list.index(st.session_state.selected_option),
        disabled=st.session_state.is_answered,
        key=f"radio_q_{idx}"
    )
    
    st.write("")
    
    if not st.session_state.is_answered:
        if st.button("💥 提交答案", type="primary", use_container_width=True):
            if user_choice is None:
                st.warning("⚠️ 请先勾选一个选项后再提交！")
            else:
                st.session_state.selected_option = user_choice
                st.session_state.is_answered = True
                user_ans_num = user_choice.split(".")[0]
                if user_ans_num == q_data['answer']:
                    st.session_state.score += 1
                st.rerun()
    else:
        user_ans_num = st.session_state.selected_option.split(".")[0]
        if user_ans_num == q_data['answer']:
            st.success("🎯 回答正确！做得太棒了！")
        else:
            st.error(f"❌ 回答错误。这一题的正确答案是 **【 {q_data['answer']} 】**。")
        
        st.write("")
        if st.button("下一题 ➡️", use_container_width=True):
            st.session_state.current_index += 1
            st.session_state.is_answered = False
            st.session_state.selected_option = None
            st.rerun()
else:
    st.balloons()
    st.success("🎉 恭喜你！全套 45 道生命科学考试题已全部复习完毕！")
    final_score = st.session_state.score
    accuracy = (final_score / total_q) * 100
    
    col1, col2 = st.columns(2)
    col1.metric(label="最终得分", value=f"{final_score} / {total_q}")
    col2.metric(label="答题正确率", value=f"{accuracy:.1f}%")
    
    st.markdown("---")
    if st.button("🔄 重新开始练习", use_container_width=True):
        st.session_state.current_index = 0
        st.session_state.score = 0
        st.session_state.is_answered = False
        st.session_state.selected_option = None
        st.rerun()
