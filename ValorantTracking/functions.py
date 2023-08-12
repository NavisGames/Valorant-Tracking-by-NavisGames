import aiohttp
import httpx as http
from PyQt5.QtGui import QImage

current_season = "e7a1"

intervals = (
    ("Weeks", 604800),  # 60 * 60 * 24 * 7
    ("Days", 86400),  # 60 * 60 * 24
    ("Hours", 3600),  # 60 * 60
    ("Minutes", 60),
    ("Seconds", 1),
)

ranklist = [
    "Unranked",
    "Unused 1",
    "Unused 2",
    "Iron 1",
    "Iron 2",
    "Iron 3",
    "Bronze 1",
    "Bronze 2",
    "Bronze 3",
    "Silver 1",
    "Silver 2",
    "Silver 3",
    "Gold 1",
    "Gold 2",
    "Gold 3",
    "Platinum 1",
    "Platinum 2",
    "Platinum 3",
    "Diamond 1",
    "Diamond 2",
    "Diamond 3",
    "Ascendant 1",
    "Ascendant 2",
    "Ascendant 3",
    "Immortal 1",
    "Immortal 2",
    "Immortal 3",
    "Radiant",
]


def get_image(url: str):
    with http.Client() as client:
        r = client.get(url)
    img = QImage()
    img.loadFromData(r.content)
    return img


async def get_image_async(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            img_data = await response.read()
            return QImage.fromData(img_data)


def display_time(seconds: int, granularity=2):
    result = []

    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip("s")
            result.append("{} {}".format(value, name))
    return " ".join(result[:granularity])


def clear_layout(layout):
    if layout is not None:
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            elif child.layout() is not None:
                clear_layout(child.layout())


def find_team_of_player(player: str, players: list):
    return {p.name: p.team for p in players}.get(player)


def find_stats_of_player(player: str, players: list):
    return {p.name: p.stats for p in players}.get(player)


def find_round_player(player: str, player_stats: list):
    return {p.player_display_name: p for p in player_stats}.get(player)


def find_agent_of_player(player: str, players: list):
    return {p.name: p.character for p in players}.get(player)
