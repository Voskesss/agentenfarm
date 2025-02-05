import sys
import os

# Voeg de root directory toe aan Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from agency_swarm import Agency
from agency_swarm.agents.BrowsingAgent import BrowsingAgent

# Maak een BrowsingAgent met default configuratie
browser_agent = BrowsingAgent()

# Voeg extra instructies toe
browser_agent.add_shared_instructions("""
Je bent een agent die gespecialiseerd is in het vinden van informatie over facilitaire bedrijven.
Voor elk bedrijf verzamel je:
- Bedrijfsnaam
- Website
- Locatie hoofdkantoor
- Kerndiensten
- Bedrijfsgrootte
- Oprichtingsjaar

BELANGRIJK: Gebruik altijd Bing.com als zoekmachine in plaats van Google. Begin je zoekopdracht met https://www.bing.com/search?q=
""")

# Maak een agency met alleen de browser agent
agency = Agency([browser_agent])

def main():
    # Start de demo interface
    demo = agency.demo_gradio(height=700)
    demo.launch()

if __name__ == "__main__":
    main()
