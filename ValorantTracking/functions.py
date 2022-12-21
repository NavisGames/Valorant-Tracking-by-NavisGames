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
    team = list(
        accumulate(p.team for p in players.all_players if p.name == player)
    )
    return team[0] if team else None


def findStatsOfPlayer(player, players):
    stats = list(
        accumulate(p.stats for p in players.all_players if p.name == player)
    )
    return stats[0] if stats else None


def findRoundPlayer(player, rounds):
    player = list(
        accumulate(
            pl.damage
            for pl in rounds.player_stats
            if pl.player_display_name == player
        )
    )
    return player if player else None


def findAgentOfPlayer(player, players):
    agent = list(
        accumulate(
            p.character for p in players.all_players if p.name == player
        )
    )
    return agent if agent else None


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
