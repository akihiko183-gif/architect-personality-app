import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def research_building(
    building_name,
    extra_info="",
    reference_url=""
):

    prompt = f"""
あなたは建築史家、
建築評論家、
建築ジャーナリストです。

建築作品をできるだけ正確に整理してください。

====================

建築名

{building_name}

====================

追加情報

{extra_info}

====================

参考URL

{reference_url}

====================

以下を整理してください。

# 建築概要

・正式名称
・設計者
・所在地
・竣工年
・用途

# 特徴

・形態
・空間
・構造
・材料
・環境

# 建築史的意義

# 受賞歴

# エピソード

# 一般利用者の印象

重要

・追加情報を積極的に活用する
・不明なら不明
・推測しない
・事実と推測を区別する
"""

    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )

    return response.output_text
