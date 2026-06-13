from search import search_building

results = search_building(
    "ROKI Global Innovation Center"
)

print("件数:", len(results))

for r in results[:10]:

    print("-" * 50)

    print("タイトル")
    print(r["title"])

    print()

    print("概要")
    print(r["body"])

    print()

    print("URL")
    print(r["url"])
