import httpx as http
from itertools import accumulate
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette, QColor, QImage, QPixmap, QFontDatabase
from PyQt5.QtWidgets import QApplication

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
    team = list(accumulate(p.team for p in players.all_players if p.name == player))
    return team[0] if team else None


def findStatsOfPlayer(player, players):
    stats = list(accumulate(p.stats for p in players.all_players if p.name == player))
    return stats[0] if stats else None


def findAgentOfPlayer(player, players):
    agent = list(accumulate(p.character for p in players.all_players if p.name == player))
    return agent if agent else None
