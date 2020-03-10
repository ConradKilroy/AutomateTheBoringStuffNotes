# -*- coding: utf-8 -*-
"""
Demonstrates venn sets logic
"""

Ravin_visited = set("""United States of America

Madagascar

Canada

Japan

Brunei

Hong Kong

Russia

Azerbaijan

Bahrain""".split("\n"))





Polina_visited = set("""Russia

United States of America

Germany

France

United Kingdom

Austria

Canada

Azerbaijan

Ukraine

Japan""".split("\n"))



#remember to venn diagram this as a set!!!





print("Both Visited:", Ravin_visited & Polina_visited)

print("Either or visited:", Ravin_visited | Polina_visited)

print("Just One visited:", Ravin_visited ^ Polina_visited)

print("Just Ravin:", Ravin_visited - Polina_visited)

print("Just Polina:", Polina_visited - Ravin_visited)
