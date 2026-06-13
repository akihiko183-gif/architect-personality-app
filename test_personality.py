from research import research_building
from nickname import create_nickname

name = "ROKI Global Innovation Center"

research = research_building(name)

print("=" * 80)
print("建築調査")
print("=" * 80)

print(research)

print("=" * 80)
print("人格分析")
print("=" * 80)

result = create_nickname(
    name,
    research
)

print(result)
