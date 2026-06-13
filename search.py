import re
from duckduckgo_search import DDGS


def normalize_name(name):
    name = name.strip()
    name = name.replace("　", " ")
    name = " ".join(name.split())

    replacements = {
        "東京 都庁": "東京都庁舎",
        "東京都庁": "東京都庁舎",
        "都庁": "東京都庁舎",
        "仙台メディアテーク": "せんだいメディアテーク",
    }

    return replacements.get(name, name)


def build_queries(name):

    return [
        f'"{name}"',
        f'"{name}" 建築',
        f'"{name}" 建築家',
        f'"{name}" 設計者',
        f'"{name}" architect',
        f'"{name}" 日本建築学会賞',
        f'"{name}" JIA',
        f'"{name}" BCS賞',
        f'"{name}" グッドデザイン賞',
        f'"{name}" site:aij.or.jp',
        f'"{name}" site:architecturephoto.net',
        f'"{name}" site:japan-architects.com',
        f'"{name}" site:archdaily.com',
        f'"{name}" site:mag.tecture.jp',
        f'"{name}" site:shinkenchiku.online',
        f'"{name}" 評価',
        f'"{name}" エピソード',
        f'"{name}" 特徴',
        f'"{name}" コンセプト',
        f'"{name}" 受賞',
    ]


def clean_text(text):

    if not text:
        return ""

    text = re.sub(r"\s+", " ", text)

    return text.strip()


def search_building(name, max_results_per_query=5):

    name = normalize_name(name)

    queries = build_queries(name)

    results = []
    seen_urls = set()

    with DDGS() as ddgs:

        for query in queries:

            try:

                search_results = ddgs.text(
                    query,
                    max_results=max_results_per_query
                )

                for r in search_results:

                    url = r.get("href", "")

                    if not url:
                        continue

                    if url in seen_urls:
                        continue

                    seen_urls.add(url)

                    results.append(
                        {
                            "title": clean_text(
                                r.get("title", "")
                            ),
                            "body": clean_text(
                                r.get("body", "")
                            ),
                            "url": url,
                            "query": query
                        }
                    )

            except Exception:
                continue

    return results
