from typing import List
import httpx as http
from itertools import accumulate
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette, QColor, QImage, QPixmap, QFontDatabase
from PyQt5.QtWidgets import QApplication
import valo_api
from valo_api.endpoints.raw import EndpointType
from valo_api.responses.match_history import MatchHistoryPointV3

current_season = "E5A3"

intervals = (
    ("Weeks", 604800),  # 60 * 60 * 24 * 7
    ("Days", 86400),  # 60 * 60 * 24
    ("Hours", 3600),  # 60 * 60
    ("Minutes", 60),
    ("Seconds", 1),
)

ranklist = [
    "UNRANKED",
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


def get_image(url):
    with http.Client() as client:
        r = client.get(url)
    img = QImage()
    img.loadFromData(r.content)
    return img


def display_time(seconds, granularity=2):
    result = []

    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip("s")
            result.append("{} {}".format(value, name))
    return " ".join(result[:granularity])


def clearLayout(layout):
    if layout is not None:
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            elif child.layout() is not None:
                clearLayout(child.layout())


def findTeamOfPlayer(player, players):
    return {p.name: p.team for p in players}.get(player)


def findStatsOfPlayer(player, players):
    return {p.name: p.stats for p in players}.get(player)


def findRoundPlayer(player, player_stats):
    return {p.player_display_name: p for p in player_stats}.get(player)


def findAgentOfPlayer(player, players):
    return {p.name: p.character for p in players}.get(player)


def get_matches(region: str, puuid: str) -> List[MatchHistoryPointV3]:
    step_size = 20  # maximum is 20

    match_ids = set()
    query_args = {
        "startIndex": 0,
        "endIndex": step_size,
    }
    while True:
        match_history = valo_api.get_raw_data_v1(
            EndpointType.MATCH_HISTORY,
            region=region,
            value=puuid,
            queries=query_args,
        )
        for match in match_history.History:
            match_ids.add(match.MatchID)

        if query_args["endIndex"] >= match_history.Total:
            # All matches processed
            break
        # Update query args. Do the next pagination step.
        query_args["startIndex"] = query_args["endIndex"] + 1
        query_args["endIndex"] = min(
            query_args["endIndex"] + step_size, match_history.Total
        )

    return [
        valo_api.get_match_details_v2(match_id=match_id)
        for match_id in match_ids
    ]
