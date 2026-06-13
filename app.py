import streamlit as st

from alias import normalize_building_name
from research import research_building
from nickname import create_nickname

st.set_page_config(
    page_title="建築人格アプリ",
    page_icon="🏛️",
    layout="wide"
)

st.title("🏛️ 建築人格アプリ")

st.caption(
    "建築作品を人格分析し、特徴やエピソードをもとにあだ名を生成します。"
)

st.markdown("---")

building_name = st.text_input(
    "建築作品名",
    placeholder="例：ROGIC、都庁、サヴォア"
)

extra_info = st.text_area(
    "追加情報（任意）",
    height=150,
    placeholder="""
例：

日本建築学会賞受賞
小堀哲夫設計
風と光を活かした研究施設
"""
)

reference_url = st.text_input(
    "参考URL（任意）",
    placeholder="https://example.com"
)

st.markdown("---")

if st.button(
    "人格分析・あだ名生成",
    type="primary"
):

    if not building_name.strip():

        st.warning("建築作品名を入力してください。")

    else:

        official_name = normalize_building_name(
            building_name
        )

        st.success(
            f"正式名称：{official_name}"
        )

        with st.spinner(
            "建築情報を整理中..."
        ):

            research_text = research_building(
                official_name,
                extra_info,
                reference_url
            )

        st.subheader(
            "📚 建築リサーチ結果"
        )

        st.markdown(
            research_text
        )

        with st.spinner(
            "人格分析中..."
        ):



            nickname_text = create_nickname(
                official_name,
                research_text,
                extra_info
            )


        st.subheader(
            "🎭 建築人格・あだ名"
        )

        st.markdown(
            nickname_text
        )
