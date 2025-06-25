import requests
import re
import argparse

SERVER_ID = "29566604"
API_URL = "https://api.battlemetrics.com/players"
HEADERS = {
    "Authorization": "Bearer "
}
PAGE_SIZE = 100

def fetch_all_active_players(server_id):
    all_players = []
    url = API_URL
    params = {
        "filter[servers]": server_id,
        "filter[online]": "true",
        "page[size]": PAGE_SIZE,
        "fields[player]": "name"
    }

    while url:
        response = requests.get(url, headers=HEADERS, params=params if "?" not in url else {})
        if response.status_code != 200:
            raise Exception(f"Fehler beim Abrufen der Daten: {response.status_code} - {response.text}")
        data = response.json()
        names = [player['attributes']['name'] for player in data.get('data', [])]
        all_players.extend(names)
        url = data.get('links', {}).get('next')
        params = {}
    return all_players

def filter_by_tag(players, tags):
    return [name for name in players if any(re.search(re.escape(tag), name, re.IGNORECASE) for tag in tags)]

def filter_by_name(players, name_fragment):
    return [name for name in players if name_fragment.lower() in name.lower()]

def main():
    parser = argparse.ArgumentParser(description="BattleMetrics Spieleranzeige mit Pagination")
    parser.add_argument("--tag", nargs="+", help="Liste von Clan-Tags zum Filtern, z. B. --tag [XYZ] [ABC]")
    parser.add_argument("--name", help="Teilname eines Spielers zum Suchen")
    parser.add_argument("--all", action="store_true", help="Zeige alle Spieler")
    args = parser.parse_args()

    try:
        print("Abrufen aktiver Spieler vom Server (mit Pagination)...")
        players = fetch_all_active_players(SERVER_ID)
        print(f"{len(players)} Spieler gefunden.\n")

        if args.tag:
            print(f"Suche nach Tags: {args.tag}")
            matched = filter_by_tag(players, args.tag)
        elif args.name:
            print(f"Suche nach Namen, die '{args.name}' enthalten...")
            matched = filter_by_name(players, args.name)
        elif args.all:
            print("Alle Spieler:")
            matched = players
        else:
            print("⚠️  Bitte gib --tag, --name oder --all an.")
            return

        if not matched:
            print("❌ Keine passenden Spieler gefunden.")
        else:
            for name in matched:
                print(f" - {name}")

    except Exception as e:
        print(f"Fehler: {e}")

if __name__ == "__main__":
    main()