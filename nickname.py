from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def create_nickname(
    building_name,
    research_text,
    extra_info=""
):

    prompt = f"""
あなたは建築評論家、
コピーライター、
建築オタクです。

建築作品を擬人化してください。

====================

建築名

{building_name}

====================

追加情報

{extra_info}

====================

建築調査結果

{research_text}

====================

重要ルール

・「不明」は無視する
・追加情報を最優先する
・設計者の作風を反映する
・受賞歴を反映する
・建築の特徴を反映する

悪い例

憶測禁止マン
一次資料至上主義くん

↑
これは建築ではなく
調査結果の人格化なので禁止

良い例

風読み研究者
静かな発明家
環境チューナー

↑
建築の特徴を人格化する

====================

出力

# 建築人格

・性格

・長所

・短所

・口癖

・動物に例えると

・職業に例えると

# あだ名

## ゆるキャラ系
3案

## オノマトペ系
3案

## 毒舌系
3案

## 建築オタク系
3案

## 学生が呼びそうなあだ名
3案

## SNSで流行りそうなあだ名
3案

必ず理由を書く。
"""

    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )

    return response.output_text
