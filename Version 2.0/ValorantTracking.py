# Credits for this program go to NavisGames, selling this program or saying it's yours is not allowed! Read the
# license for more. If you want, please fork this program to share what you changed in this program ^^

from itertools import accumulate
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
import traceback
import valo_api
import requests
from pathlib import Path
import httpx as http
import concurrent.futures
import time

valo_api.set_api_key("")
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
    return " | ".join(result[:granularity])


class Ui_ValorantTrackerByNavisGames(object):
    def setupUi(self, ValorantTrackerByNavisGames):
        try:
            # Creating MainWindow
            ValorantTrackerByNavisGames.setObjectName("ValorantTrackerByNavisGames")
            ValorantTrackerByNavisGames.setEnabled(True)
            ValorantTrackerByNavisGames.resize(945, 922)
            ValorantTrackerByNavisGames.setMaximumSize(QtCore.QSize(16777215, 16777215))

            # Creating Font Standards
            font = QtGui.QFont()
            font.setFamily("Tungsten Bold")
            font.setPointSize(20)
            font.setBold(False)
            font.setItalic(False)
            font.setWeight(50)
            font.setKerning(True)

            # Set Font, WindowTitle and Icon
            ValorantTrackerByNavisGames.setFont(font)
            ValorantTrackerByNavisGames.setMouseTracking(False)
            ValorantTrackerByNavisGames.setWindowTitle("Valorant Tracker 2.0 By NavisGames")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            ValorantTrackerByNavisGames.setWindowIcon(icon)
            ValorantTrackerByNavisGames.setDockOptions(
                QtWidgets.QMainWindow.AllowTabbedDocks | QtWidgets.QMainWindow.AnimatedDocks
            )

            # Create CENTRAL WIDGET (What is it? i still dont get it..)
            self.centralwidget = QtWidgets.QWidget(ValorantTrackerByNavisGames)
            self.centralwidget.setObjectName("centralwidget")

            # Create Layout for WIDGET (Why for every widget..  i cant even rename them in QTDesigner..)
            self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.centralwidget)
            self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout_7.setSpacing(0)
            self.verticalLayout_7.setObjectName("verticalLayout_7")

            # Creating Tabs
            self.Tabs = QtWidgets.QTabWidget(self.centralwidget)
            self.Tabs.setEnabled(True)
            self.Tabs.setFocusPolicy(QtCore.Qt.NoFocus)
            self.Tabs.setLayoutDirection(QtCore.Qt.LeftToRight)
            self.Tabs.setTabPosition(QtWidgets.QTabWidget.North)
            self.Tabs.setTabShape(QtWidgets.QTabWidget.Rounded)
            self.Tabs.setElideMode(QtCore.Qt.ElideNone)
            self.Tabs.setUsesScrollButtons(False)
            self.Tabs.setDocumentMode(False)
            self.Tabs.setTabsClosable(False)
            self.Tabs.setMovable(False)
            self.Tabs.setTabBarAutoHide(False)
            self.Tabs.setObjectName("Tabs")

            # Creating Home Tab
            self.Home = QtWidgets.QWidget()
            self.Home.setObjectName("Home")
            self.verticalLayout = QtWidgets.QVBoxLayout(self.Home)

            # Creating Home Layout
            self.verticalLayout.setObjectName("verticalLayout")

            # Creating Player Input Frame
            self.PlayerInput = QtWidgets.QFrame(self.Home)
            self.PlayerInput.setEnabled(True)
            self.PlayerInput.setFrameShape(QtWidgets.QFrame.Box)
            self.PlayerInput.setFrameShadow(QtWidgets.QFrame.Plain)
            self.PlayerInput.setLineWidth(0)
            self.PlayerInput.setObjectName("PlayerInput")

            # Creating Player Input Layout
            self.horizontalLayout = QtWidgets.QHBoxLayout(self.PlayerInput)
            self.horizontalLayout.setContentsMargins(5, 0, 5, 0)
            self.horizontalLayout.setSpacing(5)
            self.horizontalLayout.setObjectName("horizontalLayout")

            # Create Player Name Input
            self.PlayerName = QtWidgets.QLineEdit(self.PlayerInput)
            self.PlayerName.setEnabled(True)
            self.PlayerName.setToolTipDuration(-7)
            self.PlayerName.setInputMask("")
            self.PlayerName.setText("")
            self.PlayerName.setMaxLength(16)
            self.PlayerName.setAlignment(QtCore.Qt.AlignCenter)
            self.PlayerName.setPlaceholderText("PLAYER NAME (16 characters)")
            self.PlayerName.setObjectName("PlayerName")
            self.horizontalLayout.addWidget(self.PlayerName)

            # Create Player Tag Input
            self.PlayerTag = QtWidgets.QLineEdit(self.PlayerInput)
            self.PlayerTag.setEnabled(True)
            self.PlayerTag.setInputMask("")
            self.PlayerTag.setText("")
            self.PlayerTag.setMaxLength(5)
            self.PlayerTag.setAlignment(QtCore.Qt.AlignCenter)
            self.PlayerTag.setPlaceholderText("PLAYER TAG (5 characters)")
            self.PlayerTag.setObjectName("PlayerTag")
            self.horizontalLayout.addWidget(self.PlayerTag)

            # Create Player Region Input
            self.PlayerRegion = QtWidgets.QComboBox(self.PlayerInput)
            self.PlayerRegion.setEnabled(True)
            self.PlayerRegion.setLayoutDirection(QtCore.Qt.LeftToRight)
            self.PlayerRegion.setCurrentText("EU")
            self.PlayerRegion.setMaxVisibleItems(6)
            self.PlayerRegion.setMaxCount(6)
            self.PlayerRegion.setDuplicatesEnabled(False)
            self.PlayerRegion.setObjectName("PlayerRegion")
            self.PlayerRegion.addItem("")
            self.PlayerRegion.setItemText(0, "EU")
            self.PlayerRegion.addItem("")
            self.PlayerRegion.setItemText(1, "NA")
            self.PlayerRegion.addItem("")
            self.PlayerRegion.setItemText(2, "KR")
            self.PlayerRegion.addItem("")
            self.PlayerRegion.setItemText(3, "AP")
            self.PlayerRegion.addItem("")
            self.PlayerRegion.setItemText(4, "LATAM")
            self.PlayerRegion.addItem("")
            self.PlayerRegion.setItemText(5, "BR")
            self.horizontalLayout.addWidget(self.PlayerRegion)

            # Create Apply, Reset Buttons
            self.DialogButton = QtWidgets.QDialogButtonBox(self.PlayerInput)
            self.DialogButton.setEnabled(True)
            self.DialogButton.setOrientation(QtCore.Qt.Horizontal)
            self.DialogButton.setCenterButtons(False)
            self.DialogButton.setObjectName("DialogButton")

            # Create Buttons for DialogBox
            self.getButton = QtWidgets.QPushButton("&Get")
            self.getButton.setDefault(True)
            self.resetButton = QtWidgets.QPushButton("&Reset")
            self.resetButton.setDefault(True)
            self.DialogButton.addButton(self.getButton, QtWidgets.QDialogButtonBox.ActionRole)
            self.DialogButton.addButton(self.resetButton, QtWidgets.QDialogButtonBox.ActionRole)

            # Layer Stuff. IDC
            self.horizontalLayout.addWidget(self.DialogButton)
            self.horizontalLayout.setStretch(0, 2)
            self.horizontalLayout.setStretch(1, 1)
            self.verticalLayout.addWidget(self.PlayerInput)

            # Create Player Output Banner & Data etc. Frame
            self.PlayerInformation = QtWidgets.QFrame(self.Home)
            self.PlayerInformation.setEnabled(True)
            self.PlayerInformation.setFrameShape(QtWidgets.QFrame.Box)
            self.PlayerInformation.setFrameShadow(QtWidgets.QFrame.Plain)
            self.PlayerInformation.setLineWidth(0)
            self.PlayerInformation.setObjectName("PlayerInformation")
            self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.PlayerInformation)
            self.horizontalLayout_2.setContentsMargins(5, 0, 5, 0)
            self.horizontalLayout_2.setSpacing(0)
            self.horizontalLayout_2.setObjectName("horizontalLayout_2")

            # Create Player Banner PixMap
            self.PlayerBanner = QtWidgets.QLabel(self.PlayerInformation)
            self.PlayerBanner.setEnabled(True)
            self.PlayerBanner.setFrameShape(QtWidgets.QFrame.NoFrame)
            self.PlayerBanner.setLineWidth(1)
            self.PlayerBanner.setText("")
            self.PlayerBanner.setPixmap(QtGui.QPixmap("StandardBanner.png"))
            self.PlayerBanner.setScaledContents(False)
            self.PlayerBanner.setAlignment(QtCore.Qt.AlignCenter)
            self.PlayerBanner.setWordWrap(False)
            self.PlayerBanner.setObjectName("PlayerBanner")
            self.horizontalLayout_2.addWidget(self.PlayerBanner)

            # Create Player Information Frame
            self.PlayerDatas = QtWidgets.QFrame(self.PlayerInformation)
            self.PlayerDatas.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.PlayerDatas.setFrameShadow(QtWidgets.QFrame.Raised)
            self.PlayerDatas.setObjectName("PlayerDatas")
            self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.PlayerDatas)
            self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout_5.setSpacing(0)
            self.verticalLayout_5.setObjectName("verticalLayout_5")

            # Create Player puu-id + Region
            self.PlayerIDs = QtWidgets.QLabel(self.PlayerDatas)
            font = QtGui.QFont()
            font.setPointSize(15)
            self.PlayerIDs.setFont(font)
            self.PlayerIDs.setFrameShape(QtWidgets.QFrame.NoFrame)
            self.PlayerIDs.setText("puu-ID | EU")
            self.PlayerIDs.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
            self.PlayerIDs.setObjectName("PlayerIDs")
            self.verticalLayout_5.addWidget(self.PlayerIDs)

            # Creating Player, Add HTML Text wich is bigger than my Dick With AccountLevel, Player#Tag and Rank.
            # Complicate Shit, i cant code HTML
            self.Player = QtWidgets.QLabel(self.PlayerDatas)
            self.Player.setEnabled(True)
            font = QtGui.QFont()
            font.setPointSize(35)
            self.Player.setFont(font)
            self.Player.setFrameShape(QtWidgets.QFrame.NoFrame)
            self.Player.setText(
                '<html><head/><body><p><span style=" font-size:29pt;">Player#Tag<p>Account Level 0 | Rank </span><img src="StandardRank.png"width="33"height="33"/><span style=" font-size:20pt;"> 0rr</span></p></body></html>'
            )
            self.Player.setTextFormat(QtCore.Qt.RichText)
            self.Player.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
            self.Player.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
            self.Player.setObjectName("Player")

            # Layer Stuff. IDC
            self.verticalLayout_5.addWidget(self.Player)
            self.horizontalLayout_2.addWidget(self.PlayerDatas)
            self.verticalLayout.addWidget(self.PlayerInformation)

            # Creating Accuracy & Stats Frame
            self.GeneralStats = QtWidgets.QFrame(self.Home)
            self.GeneralStats.setFrameShape(QtWidgets.QFrame.NoFrame)
            self.GeneralStats.setFrameShadow(QtWidgets.QFrame.Plain)
            self.GeneralStats.setLineWidth(1)
            self.GeneralStats.setObjectName("GeneralStats")
            self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.GeneralStats)
            self.horizontalLayout_8.setContentsMargins(5, 0, 5, 5)
            self.horizontalLayout_8.setObjectName("horizontalLayout_8")

            # Creating Accuracy Stats
            self.AccuarcyStats = QtWidgets.QFrame(self.GeneralStats)
            self.AccuarcyStats.setFrameShape(QtWidgets.QFrame.Box)
            self.AccuarcyStats.setFrameShadow(QtWidgets.QFrame.Plain)
            self.AccuarcyStats.setLineWidth(1)
            self.AccuarcyStats.setObjectName("AccuarcyStats")
            self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.AccuarcyStats)
            self.verticalLayout_6.setContentsMargins(5, 0, 5, 0)
            self.verticalLayout_6.setSpacing(0)
            self.verticalLayout_6.setObjectName("verticalLayout_6")

            # Creating Accuracy Title
            self.AccuracyTitle = QtWidgets.QLabel(self.AccuarcyStats)
            font = QtGui.QFont()
            font.setUnderline(False)
            font.setStrikeOut(False)
            self.AccuracyTitle.setFont(font)
            self.AccuracyTitle.setText(
                '<html><head/><body><p><span style=" font-size:22pt;">Accuracy </span><span style=" font-size:18pt; color:#6a6a6a;">(Last 10 Matches)</span></p></body></html>'
            )
            self.AccuracyTitle.setTextFormat(QtCore.Qt.RichText)
            self.AccuracyTitle.setAlignment(QtCore.Qt.AlignCenter)
            self.AccuracyTitle.setObjectName("AccuracyTitle")
            self.verticalLayout_6.addWidget(self.AccuracyTitle)

            # Creating Accuracy Frame for Pixmap and Info's
            self.Accuracy = QtWidgets.QFrame(self.AccuarcyStats)
            self.Accuracy.setFrameShape(QtWidgets.QFrame.NoFrame)
            self.Accuracy.setFrameShadow(QtWidgets.QFrame.Plain)
            self.Accuracy.setLineWidth(5)
            self.Accuracy.setObjectName("Accuracy")
            self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.Accuracy)
            self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout_9.setSpacing(0)
            self.horizontalLayout_9.setStretch(0, 3)
            self.horizontalLayout_9.setObjectName("horizontalLayout_9")

            # Creating Accuracy Pixmap
            self.AccuracyLogo = QtWidgets.QLabel(self.Accuracy)
            self.AccuracyLogo.setLayoutDirection(QtCore.Qt.LeftToRight)
            self.AccuracyLogo.setText("")
            self.AccuracyLogo.setPixmap(QtGui.QPixmap("Basic.png"))
            self.AccuracyLogo.setAlignment(QtCore.Qt.AlignCenter)
            self.AccuracyLogo.setObjectName("AccuracyLogo")
            self.horizontalLayout_9.addWidget(self.AccuracyLogo)

            # Creating Accuracy Texts for HS Rate etc.
            self.AccuracyText = QtWidgets.QLabel(self.Accuracy)
            self.AccuracyText.setLayoutDirection(QtCore.Qt.LeftToRight)
            self.AccuracyText.setText("Headshots: 0%\n" "Bodyshots: 0%\n" "Legshots: 0%")
            self.AccuracyText.setAlignment(QtCore.Qt.AlignCenter)
            self.AccuracyText.setObjectName("AccuracyText")
            self.horizontalLayout_9.addWidget(self.AccuracyText)
            self.verticalLayout_6.addWidget(self.Accuracy)
            self.horizontalLayout_8.addWidget(self.AccuarcyStats)

            # Creating Average KD & Winrate Frame
            self.OtherStats = QtWidgets.QFrame(self.GeneralStats)
            self.OtherStats.setFrameShape(QtWidgets.QFrame.Box)
            self.OtherStats.setFrameShadow(QtWidgets.QFrame.Plain)
            self.OtherStats.setObjectName("OtherStats")
            self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.OtherStats)
            self.verticalLayout_9.setContentsMargins(5, 0, 5, 0)
            self.verticalLayout_9.setObjectName("verticalLayout_9")

            # Creating ANOTHER complicated HTML Code with Average KD, Winrate and the Title in it (URGH)
            self.OtherStatsTexts = QtWidgets.QLabel(self.OtherStats)
            self.OtherStatsTexts.setText(
                '<html><head/><body><p align="center"><span style=" font-size:22pt;">Other Stats </span><span style=" font-size:18pt; color:#6a6a6a;">(Last 10 Matches)</span></p><p><span style=" font-size:22pt;">Average KD: 0.00</span></p><p><span style=" font-size:22pt; color:#000000;">Winrate: 0%</span></p></body></html>'
            )
            self.OtherStatsTexts.setTextFormat(QtCore.Qt.RichText)
            self.OtherStatsTexts.setScaledContents(False)
            self.OtherStatsTexts.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
            self.OtherStatsTexts.setObjectName("OtherStatsTexts")
            self.verticalLayout_9.addWidget(self.OtherStatsTexts)
            self.horizontalLayout_8.addWidget(self.OtherStats)
            self.verticalLayout.addWidget(self.GeneralStats)

            # Creating Stats Frame
            self.Stats = QtWidgets.QFrame(self.Home)
            self.Stats.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.Stats.setFrameShadow(QtWidgets.QFrame.Raised)
            self.Stats.setObjectName("Stats")
            self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.Stats)
            self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
            self.horizontalLayout_6.setObjectName("horizontalLayout_6")

            # Creating CompetitiveStats Frame for Stats
            self.CompInformation = QtWidgets.QFrame(self.Stats)
            self.CompInformation.setEnabled(True)
            self.CompInformation.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.CompInformation.setFrameShadow(QtWidgets.QFrame.Raised)
            self.CompInformation.setObjectName("CompInformation")
            self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.CompInformation)
            self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout_2.setObjectName("verticalLayout_2")

            # Creating Competitive Title
            self.CompTitle = QtWidgets.QLabel(self.CompInformation)
            self.CompTitle.setEnabled(True)
            self.CompTitle.setText("COMPETITIVE STATS")
            self.CompTitle.setAlignment(QtCore.Qt.AlignCenter)
            self.CompTitle.setObjectName("CompTitle")
            self.verticalLayout_2.addWidget(self.CompTitle)

            # Creating ScrollArea for the Field of Competitive
            self.CompScrollArea = QtWidgets.QScrollArea(self.CompInformation)
            self.CompScrollArea.setEnabled(True)
            self.CompScrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
            self.CompScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            self.CompScrollArea.setWidgetResizable(True)
            self.CompScrollArea.setAlignment(QtCore.Qt.AlignCenter)
            self.CompScrollArea.setObjectName("CompScrollArea")
            self.CompScrollLayout = QtWidgets.QWidget()
            self.CompScrollLayout.setGeometry(QtCore.QRect(0, 0, 519, 355))
            self.CompScrollLayout.setObjectName("CompScrollLayout")
            self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.CompScrollLayout)
            self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout_3.setObjectName("horizontalLayout_3")

            # Creating Competititve History
            self.CompHistory = QtWidgets.QLabel(self.CompScrollLayout)
            self.CompHistory.setEnabled(True)
            font = QtGui.QFont()
            font.setPointSize(14)
            self.CompHistory.setFont(font)
            self.CompHistory.setFrameShape(QtWidgets.QFrame.Box)
            self.CompHistory.setLineWidth(1)
            self.CompHistory.setText(
                "Matchmaking Ratio \n"
                "Competitive Wins \n"
                "Competitive Games played \n"
                "Previous Ranks \n"
                "Rank History\n"
                ""
            )
            self.CompHistory.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
            self.CompHistory.setObjectName("CompHistory")
            self.horizontalLayout_3.addWidget(self.CompHistory)
            self.CompScrollArea.setWidget(self.CompScrollLayout)
            self.verticalLayout_2.addWidget(self.CompScrollArea)
            self.horizontalLayout_6.addWidget(self.CompInformation)

            # Creating Match History Frame for Stats
            self.MatchHistory = QtWidgets.QFrame(self.Stats)
            self.MatchHistory.setEnabled(True)
            self.MatchHistory.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.MatchHistory.setFrameShadow(QtWidgets.QFrame.Raised)
            self.MatchHistory.setObjectName("MatchHistory")
            self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.MatchHistory)
            self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout_4.setObjectName("verticalLayout_4")

            # Craeting History Title
            self.HistoryTitle = QtWidgets.QLabel(self.MatchHistory)
            self.HistoryTitle.setEnabled(True)
            self.HistoryTitle.setText("MATCH HISTORY")
            self.HistoryTitle.setAlignment(QtCore.Qt.AlignCenter)
            self.HistoryTitle.setObjectName("HistoryTitle")
            self.verticalLayout_4.addWidget(self.HistoryTitle)

            # Creating ScrollArea for the Field of Match History
            self.HistoryScrollArea = QtWidgets.QScrollArea(self.MatchHistory)
            self.HistoryScrollArea.setEnabled(True)
            self.HistoryScrollArea.setFrameShape(QtWidgets.QFrame.Box)
            self.HistoryScrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
            self.HistoryScrollArea.setLineWidth(1)
            self.HistoryScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            self.HistoryScrollArea.setWidgetResizable(True)
            self.HistoryScrollArea.setObjectName("HistoryScrollArea")
            self.HistoryScrollLayout = QtWidgets.QWidget()
            self.HistoryScrollLayout.setGeometry(QtCore.QRect(0, 0, 519, 355))
            self.HistoryScrollLayout.setObjectName("HistoryScrollLayout")
            self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.HistoryScrollLayout)
            self.horizontalLayout_4.setObjectName("horizontalLayout_4")

            # Creating MatchHistory Text.
            self.History = QtWidgets.QLabel(self.HistoryScrollLayout)
            self.History.setEnabled(True)
            font = QtGui.QFont()
            font.setPointSize(14)
            self.History.setFont(font)
            self.History.setText(
                "Day, Date, Time | Match ID\n"
                "REGION - CLUSTER\n"
                " Map - Gamemode - Agent Played: Jett\n"
                "0-0 \n"
                "Kills Assists Deaths - KD |  Score"
            )
            self.History.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
            self.History.setObjectName("History")
            self.horizontalLayout_4.addWidget(self.History)
            self.HistoryScrollArea.setWidget(self.HistoryScrollLayout)
            self.verticalLayout_4.addWidget(self.HistoryScrollArea)
            self.horizontalLayout_6.addWidget(self.MatchHistory)
            self.verticalLayout.addWidget(self.Stats)

            # Add HOME Tab to Tabs
            self.Tabs.addTab(self.Home, "HOME")

            # Creating Leaderboard Tab & Layout
            self.Leaderboard = QtWidgets.QWidget()
            self.Leaderboard.setObjectName("Leaderboard")
            self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Leaderboard)
            self.verticalLayout_3.setContentsMargins(0, -1, 0, 0)
            self.verticalLayout_3.setObjectName("verticalLayout_3")

            # Creating Leaderboard Input Frame
            self.LeaderBoardInput = QtWidgets.QFrame(self.Leaderboard)
            self.LeaderBoardInput.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.LeaderBoardInput.setFrameShadow(QtWidgets.QFrame.Raised)
            self.LeaderBoardInput.setObjectName("LeaderBoardInput")
            self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.LeaderBoardInput)
            self.horizontalLayout_7.setContentsMargins(5, 0, 5, 0)
            self.horizontalLayout_7.setObjectName("horizontalLayout_7")

            # Creating Combo Box for all Acts
            self.Act = QtWidgets.QComboBox(self.LeaderBoardInput)
            self.Act.setCurrentText("E5A3")
            self.Act.setObjectName("Act")
            self.Act.addItem("")
            self.Act.setItemText(0, "E5A3")
            self.Act.addItem("")
            self.Act.setItemText(1, "E5A2")
            self.Act.addItem("")
            self.Act.setItemText(2, "E5A1")
            self.Act.addItem("")
            self.Act.setItemText(3, "E4A3")
            self.Act.addItem("")
            self.Act.setItemText(4, "E4A2")
            self.Act.addItem("")
            self.Act.setItemText(5, "E4A1")
            self.Act.addItem("")
            self.Act.setItemText(6, "E3A3")
            self.Act.addItem("")
            self.Act.setItemText(7, "E3A2")
            self.Act.addItem("")
            self.Act.setItemText(8, "E3A1")
            self.Act.addItem("")
            self.Act.setItemText(9, "E2A3")
            self.Act.addItem("")
            self.Act.setItemText(10, "E2A2")
            self.Act.addItem("")
            self.Act.setItemText(11, "E2A2")
            self.horizontalLayout_7.addWidget(self.Act)

            # Creating Leaderboard Regions
            self.LeaderBoardRegion = QtWidgets.QComboBox(self.LeaderBoardInput)
            self.LeaderBoardRegion.setEnabled(True)
            self.LeaderBoardRegion.setLayoutDirection(QtCore.Qt.LeftToRight)
            self.LeaderBoardRegion.setCurrentText("EU")
            self.LeaderBoardRegion.setMaxVisibleItems(6)
            self.LeaderBoardRegion.setMaxCount(6)
            self.LeaderBoardRegion.setDuplicatesEnabled(False)
            self.LeaderBoardRegion.setObjectName("LeaderBoardRegion")
            self.LeaderBoardRegion.addItem("")
            self.LeaderBoardRegion.setItemText(0, "EU")
            self.LeaderBoardRegion.addItem("")
            self.LeaderBoardRegion.setItemText(1, "NA")
            self.LeaderBoardRegion.addItem("")
            self.LeaderBoardRegion.setItemText(2, "KR")
            self.LeaderBoardRegion.addItem("")
            self.LeaderBoardRegion.setItemText(3, "AP")
            self.LeaderBoardRegion.addItem("")
            self.LeaderBoardRegion.setItemText(4, "LATAM")
            self.LeaderBoardRegion.addItem("")
            self.LeaderBoardRegion.setItemText(5, "BR")
            self.horizontalLayout_7.addWidget(self.LeaderBoardRegion)

            # Create Playercount Box
            self.Playercount = QtWidgets.QSpinBox(self.LeaderBoardInput)
            self.Playercount.setWrapping(False)
            self.Playercount.setFrame(True)
            self.Playercount.setAlignment(QtCore.Qt.AlignCenter)
            self.Playercount.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
            self.Playercount.setSpecialValueText("")
            self.Playercount.setProperty("showGroupSeparator", False)
            self.Playercount.setPrefix("Players: ")
            self.Playercount.setMinimum(1)
            self.Playercount.setMaximum(15000)
            self.Playercount.setObjectName("spinBox")
            self.horizontalLayout_7.addWidget(self.Playercount)

            # Create Reload Button
            self.Reload = QtWidgets.QPushButton(self.LeaderBoardInput)
            self.Reload.setText("Reload")
            self.Reload.setDefault(False)
            self.Reload.setFlat(False)
            self.Reload.setObjectName("Reload")
            self.horizontalLayout_7.addWidget(self.Reload)
            self.verticalLayout_3.addWidget(self.LeaderBoardInput)

            # Create Players Frame & ScrollArea & Layout
            self.Players = QtWidgets.QVBoxLayout()
            self.Players.setContentsMargins(5, 5, 5, 5)
            self.Players.setObjectName("Players")
            self.PlayerScrollArea = QtWidgets.QScrollArea(self.Leaderboard)
            self.PlayerScrollArea.setFrameShape(QtWidgets.QFrame.Box)
            self.PlayerScrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
            self.PlayerScrollArea.setLineWidth(3)
            self.PlayerScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            self.PlayerScrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
            self.PlayerScrollArea.setWidgetResizable(True)
            self.PlayerScrollArea.setAlignment(QtCore.Qt.AlignCenter)
            self.PlayerScrollArea.setObjectName("PlayerScrollArea")
            self.PlayerScrollAreaLayout = QtWidgets.QWidget()
            self.PlayerScrollAreaLayout.setGeometry(QtCore.QRect(0, 0, 486, 145))
            self.PlayerScrollAreaLayout.setObjectName("PlayerScrollAreaLayout")
            self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.PlayerScrollAreaLayout)
            self.verticalLayout_8.setContentsMargins(5, 5, 5, 5)
            self.verticalLayout_8.setSpacing(5)
            self.verticalLayout_8.setObjectName("verticalLayout_8")

            # Create Leader Player Stuff for function
            self.LeaderboardPlayerBanner = dict()
            self.LeaderboardPlayerInformation = dict()
            self.LeaderboardPlayer = dict()
            self.LeaderboardPlayerLayout = dict()
            self.LeaderboardSpacer = dict()

            # Player Template
            self.LeaderboardPlayerTemplate = QtWidgets.QFrame(self.PlayerScrollAreaLayout)
            self.LeaderboardPlayerTemplate.setEnabled(True)
            self.LeaderboardPlayerTemplate.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.LeaderboardPlayerTemplate.setFrameShadow(QtWidgets.QFrame.Raised)
            self.LeaderboardPlayerTemplate.setObjectName("PlayerTemplate")
            self.PlayerLayoutTemplate = QtWidgets.QHBoxLayout(self.LeaderboardPlayerTemplate)
            self.PlayerLayoutTemplate.setContentsMargins(0, 0, 0, 0)
            self.PlayerLayoutTemplate.setObjectName("PlayerLayoutTemplate")

            # Player Banner Template
            self.LeaderboardPlayerBannerTemplate = QtWidgets.QLabel(self.LeaderboardPlayerTemplate)
            self.LeaderboardPlayerBannerTemplate.setText("")
            self.LeaderboardPlayerBannerTemplate.setPixmap(QtGui.QPixmap("ExampleBanner.png"))
            self.LeaderboardPlayerBannerTemplate.setScaledContents(False)
            self.LeaderboardPlayerBannerTemplate.setObjectName("LeaderboardPlayerBannerTemplate")
            self.PlayerLayoutTemplate.addWidget(self.LeaderboardPlayerBannerTemplate)
            self.LeaderboardPlayerInformationTemplate = QtWidgets.QLabel(self.LeaderboardPlayerTemplate)

            # Stats Template
            self.LeaderboardPlayerInformationTemplate.setText("#1 Player#Tag | Radiant 0rr | 0 Wins | puuid")
            self.LeaderboardPlayerInformationTemplate.setAlignment(QtCore.Qt.AlignCenter)
            self.LeaderboardPlayerInformationTemplate.setObjectName("LeaderboardPlayerInformationTemplate")

            # Layout Shit and Scroll area Shit. Also adding the Tab Leaderboard to Tabs
            self.PlayerLayoutTemplate.addWidget(self.LeaderboardPlayerInformationTemplate)
            LeaderboardSpacerTemplate = QtWidgets.QSpacerItem(
                40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
            )
            self.PlayerLayoutTemplate.addItem(LeaderboardSpacerTemplate)

            self.verticalLayout_8.addWidget(self.LeaderboardPlayerTemplate)
            spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            self.verticalLayout_8.addItem(spacerItem1)
            self.PlayerScrollArea.setWidget(self.PlayerScrollAreaLayout)
            self.Players.addWidget(self.PlayerScrollArea)
            self.verticalLayout_3.addLayout(self.Players)
            self.Tabs.addTab(self.Leaderboard, "LEADERBOARD")

            # Create Dicts with Bundles and use Valorant API to get all current bundles
            current_Bundle = valo_api.get_store_featured_v2()
            self.Bundle = dict()

            for i, bundles in enumerate(current_Bundle):
                # Getting Current Bundle

                bundleUuid = current_Bundle[i].bundle_uuid

                # Getting Bundle Banner as PixMap
                bundleJson = requests.get(url=f"https://valorant-api.com/v1/bundles/{bundleUuid}").json()
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    img = executor.submit(get_image, bundleJson["data"]["displayIcon2"])
                    img = img.result()

                # Creating Bundle
                self.Bundle[i] = QtWidgets.QWidget()
                self.Bundle[i].setObjectName("Bundle")
                self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.Bundle[i])
                self.verticalLayout_10.setContentsMargins(5, 5, 5, 5)
                self.verticalLayout_10.setSpacing(0)
                self.verticalLayout_10.setObjectName("verticalLayout_10")

                # Creating Bundle MainFrame
                self.BundleMain = QtWidgets.QFrame(self.Bundle[i])
                self.BundleMain.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.BundleMain.setFrameShadow(QtWidgets.QFrame.Raised)
                self.BundleMain.setObjectName("BundleMain")
                self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.BundleMain)
                self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout_11.setSpacing(0)
                self.verticalLayout_11.setObjectName("verticalLayout_11")

                # Creating Bundle Title
                self.BundleTitle = QtWidgets.QLabel(self.BundleMain)
                font = QtGui.QFont()
                font.setPointSize(35)
                self.BundleTitle.setFont(font)
                self.BundleTitle.setText("BUNDLE NAME")
                self.BundleTitle.setAlignment(QtCore.Qt.AlignCenter)
                self.BundleTitle.setObjectName("BundleTitle")
                self.verticalLayout_11.addWidget(self.BundleTitle)

                # Creating Bundle Banner
                self.BundleBanner = QtWidgets.QLabel(self.BundleMain)
                self.BundleBanner.setMinimumSize(QtCore.QSize(1, 1))
                self.BundleBanner.setMaximumSize(QtCore.QSize(234234, 234234))
                font = QtGui.QFont()
                font.setKerning(True)
                self.BundleBanner.setFont(font)
                self.BundleBanner.setAutoFillBackground(False)
                self.BundleBanner.setText("")
                self.BundleBanner.setPixmap(QtGui.QPixmap(img))
                self.BundleBanner.setScaledContents(True)
                self.BundleBanner.setAlignment(QtCore.Qt.AlignCenter)
                self.BundleBanner.setWordWrap(False)
                self.BundleBanner.setObjectName("BundleBanner")
                self.verticalLayout_11.addWidget(self.BundleBanner)

                # Create Bundle Prices
                self.BundlePrices = QtWidgets.QLabel(self.BundleMain)
                self.BundlePrices.setText(
                    "BUNDLE PRICE: 0 VP\n"
                    "Weapon: 0 VP | 0 VP -> Whole Bundle\n"
                    "Weapon: 0 VP | 0 VP -> Whole Bundle\n"
                    "Weapon: 0 VP | 0 VP -> Whole Bundle\n"
                    "2x Buddy: 0 VP | 0 VP -> Whole Bundle\n"
                    "Player Card: 0 VP | 0 VP -> Whole Bundle\n"
                    " Spray: 0 VP | 0 VP -> Whole Bundle"
                )
                self.BundlePrices.setAlignment(QtCore.Qt.AlignCenter)
                self.BundlePrices.setObjectName("BundlePrices")
                self.verticalLayout_11.addWidget(self.BundlePrices)

                # Create Seconds Remaining in Shop
                self.BundleLast = QtWidgets.QLabel(self.BundleMain)
                font = QtGui.QFont()
                font.setPointSize(15)
                self.BundleLast.setFont(font)
                self.BundleLast.setText("Bundle in Shop until: Weeks : Days : Hours")
                self.BundleLast.setAlignment(QtCore.Qt.AlignCenter)
                self.BundleLast.setObjectName("BundleLast")
                self.verticalLayout_11.addWidget(self.BundleLast)
                self.verticalLayout_10.addWidget(self.BundleMain)

                # Get Every Item and Set A String (before a List!)
                Prices = [f"Bundle Price - {current_Bundle[i].bundle_price} Valorant Points\n"]
                for item in current_Bundle[i].items:
                    if item.amount > 1:
                        Prices.append(
                            f"{item.amount}x {item.name} - {item.base_price} VP | {item.discounted_price} VP -> whole Bundle\n"
                        )
                    else:
                        Prices.append(
                            f"{item.name} - {item.base_price} VP | {item.discounted_price} VP -> whole Bundle\n"
                        )
                Prices = "".join(Prices)

                # Set Texts
                self.BundleTitle.setText(f"{bundleJson['data']['displayName']}")
                self.BundlePrices.setText(Prices)
                self.BundleLast.setText(f"Bundle remaining in Shop: {display_time(bundles.seconds_remaining, 3)}s")

                # Add Bundles
                self.Tabs.addTab(self.Bundle[i], f"{bundleJson['data']['displayName']} Bundle")

            # Index, Layout shit. blah blah you get it.
            self.verticalLayout_7.addWidget(self.Tabs)
            ValorantTrackerByNavisGames.setCentralWidget(self.centralwidget)
            self.Tabs.setCurrentIndex(0)
            self.PlayerRegion.setCurrentIndex(0)
            self.LeaderBoardRegion.setCurrentIndex(0)

            # Functions
            self.getButton.clicked.connect(self.get_information)
            self.resetButton.clicked.connect(self.reset_information)
            self.Reload.clicked.connect(self.leaderboard)
            QtCore.QMetaObject.connectSlotsByName(ValorantTrackerByNavisGames)

        except BaseException:
            print(traceback.format_exc())

    def get_information(self):
        try:
            # Functions
            def findTeamOfPlayer(player, players):
                team = list(accumulate(p.team for p in players.all_players if p.name == player))
                return team[0] if team else None

            def findStatsOfPlayer(player, players):
                stats = list(accumulate(p.stats for p in players.all_players if p.name == player))
                return stats[0] if stats else None

            def findAgentOfPlayer(player, players):
                agent = list(accumulate(p.character for p in players.all_players if p.name == player))
                return agent if agent else None

            # API functions
            Details = valo_api.get_account_details_by_name(
                version="v1", name=self.PlayerName.text(), tag=self.PlayerTag.text()
            )

            # Get Rank, RR and MMR
            RankDetails = valo_api.get_mmr_details_by_name_v2(
                region=self.PlayerRegion.currentText(),
                name=self.PlayerName.text(),
                tag=self.PlayerTag.text(),
            )

            # Get Match History
            HistoryDetails = valo_api.get_match_history_by_name(
                version="v3",
                region=self.PlayerRegion.currentText(),
                name=self.PlayerName.text(),
                tag=self.PlayerTag.text(),
                size=10,
            )

            # Get Recent Rank Changes
            MMRDetails = valo_api.get_mmr_history_by_name(
                version="v1",
                region=self.PlayerRegion.currentText(),
                name=self.PlayerName.text(),
                tag=self.PlayerTag.text(),
            )

            # DETAILS ~ Puuid, Region, Account Level and the PlayerCard
            # RANKDETAILS ~ Rank, RR, MMR
            Puuid = Details.puuid
            Region = Details.region
            Account_level = Details.account_level
            Card = str(Details.card.wide)
            Rank = RankDetails.current_data.currenttierpatched
            RR = RankDetails.current_data.ranking_in_tier
            MMR = RankDetails.current_data.elo

            # Sets PUU-ID and Region
            self.PlayerIDs.setText(f"{Puuid} | {Region}")

            # Wins, Games Played
            try:
                wins = RankDetails.by_season[current_season.lower()].wins
                games_played = RankDetails.by_season[current_season.lower()].number_of_games
            except AttributeError:
                wins = 0
                games_played = 0

            # Creates List with MMR, Comp Wins, Comp Games
            previous_ranks = [
                f"Matchmaking Ratio: {MMR}\n"
                f"Competitive Wins: {wins}\n"
                f"Competitive Games played: {games_played}\n"
                "\nPrevious Ranks:\n"
            ]

            # Gets Last Rank Adds last Ranks with MMR, Wins, Games to the List | if player didn't play in this act or an
            # API Problem is there, then continue
            lastRank = RankDetails.by_season
            for x in lastRank:
                try:
                    if lastRank[x].final_rank_patched is not None and x != current_season.lower():
                        previous_ranks.append(
                            f"{x.upper()}: {lastRank[x].final_rank_patched} | {lastRank[x].wins} Wins - {lastRank[x].number_of_games}Game(s) played\n"
                        )
                    else:
                        continue
                except BaseException:
                    print(traceback.format_exc())

            # If there is a rank, add a rank history)
            # For every last match in the detail get +RR or -RR and rank / rr
            # And if getting + add a + symbol else -
            if Rank is not None:
                previous_ranks.append(f"\nRank History:\n")
                for x in MMRDetails:
                    if x.mmr_change_to_last_game >= 0:
                        previous_ranks.append(
                            f"{x.date} | {x.currenttierpatched} {x.ranking_in_tier}rr (+{x.mmr_change_to_last_game})\n"
                        )
                    else:
                        previous_ranks.append(
                            f"{x.date} | {x.currenttierpatched} {x.ranking_in_tier}rr ({x.mmr_change_to_last_game})\n"
                        )

            # Makes Ranks to str and makes it to Text
            # Sets CompHistory to Ranks
            previous_ranks = "".join(previous_ranks)
            self.CompHistory.setText(previous_ranks)

            # Makes a ThreadPool for getting an QImage for the Player Card.
            # Sets Banner
            with concurrent.futures.ThreadPoolExecutor() as executor:
                img = executor.submit(get_image, Card)
                img = img.result()
            self.PlayerBanner.setPixmap(QPixmap(img))

            # Get Match History as a List, and gets every current matches
            match_History = []

            headshots = 0
            bodyshots = 0
            legshots = 0
            total_kills = 0
            total_deaths = 0
            total_wins = 0
            total_matches = 0

            for x in HistoryDetails:

                # Match, Team and Players
                match = x.metadata
                teams = x.teams
                players = x.players

                # Get Stats of Player with get_stats function
                get_stats = findStatsOfPlayer(Details.name, players)
                kills = get_stats.kills
                deaths = get_stats.deaths
                assists = get_stats.assists
                score = get_stats.score

                total_kills += kills
                total_deaths += deaths

                # Get Agent of Player
                get_agent = findAgentOfPlayer(Details.name, players)

                # Add Aim rates
                headshots += get_stats.headshots
                bodyshots += get_stats.bodyshots
                legshots += get_stats.legshots

                # Rounds to 0.00 <- 2 Decimals
                try:
                    KD = format(kills / deaths, ".2f")
                except ZeroDivisionError:
                    KD = format(kills, ".2f")

                # Get Team and Team information of Player with get_team function
                get_team = findTeamOfPlayer(Details.name, players)
                if get_team == "Blue":
                    get_team = teams.blue
                else:
                    get_team = teams.red

                # Set when Won, Rounds Won, Lost.
                won = get_team.has_won
                rounds_won = get_team.rounds_won
                rounds_lost = get_team.rounds_lost
                total_matches += 1

                # If match lost, make text lost
                if won:
                    total_wins += 1
                    won = "WON"
                else:
                    won = "LOST"

                # Get Match ID, Map, Region, Cluster and Mode with Match Metadata
                match_id = match.matchid
                match_map = match.map
                region = match.region.upper()
                cluster = match.cluster
                mode = match.mode

                # If Deathmatch, remove Rounds and Won/Lost
                if mode == "Deathmatch":
                    match_History.append(
                        f"{match.game_start_patched} | Match {match_id}\n{region} - {cluster}\n{match_map} - {mode} - Agent played: {get_agent[0]}\n{kills} Kills {assists} Assists {deaths} Deaths - {KD} KD | {score} Score\n\n"
                    )
                else:
                    match_History.append(
                        f"{match.game_start_patched} | Match {match_id}\n{region} - {cluster}\n{match_map} - {mode} - Agent played: {get_agent[0]}\n{rounds_won}-{rounds_lost} {won}\n{kills} Kills {assists} Assists {deaths} Deaths - {KD} KD | {score} Score\n\n"
                    )
            # Set Match to Text
            match_History = "".join(match_History)

            # Set Rates with Math
            headshot_rate = round(headshots / (headshots + bodyshots + legshots) * 100)
            bodyshot_rate = round(bodyshots / (headshots + bodyshots + legshots) * 100)
            legshot_rate = round(legshots / (headshots + bodyshots + legshots) * 100)

            # Set Dummy Prior
            if headshot_rate > bodyshot_rate and headshot_rate > legshot_rate:
                self.AccuracyLogo.setPixmap(QtGui.QPixmap("Headshot.png"))
            elif bodyshot_rate > headshot_rate and bodyshot_rate > legshot_rate:
                self.AccuracyLogo.setPixmap(QtGui.QPixmap("Bodyshot.png"))
            elif legshot_rate > headshot_rate and legshot_rate > bodyshot_rate:
                self.AccuracyLogo.setPixmap(QtGui.QPixmap("Legshot.png"))

            # Gets the current Rank AS TIER INDEX (int) and compares it with the index data, to get the RANK IMAGE
            tier_index = RankDetails.current_data.currenttier
            data = requests.get("https://valorant-api.com/v1/competitivetiers").json()
            tiers = data["data"][-1]["tiers"]
            tier = None

            # If it has any Rank, get it ELSE say Unranked
            if Rank is not None:
                for tier in tiers:
                    if tier["tier"] == tier_index:
                        tier = tier["tierName"]
                        break
            else:
                tier = "UNRANKED"

            # Gets the PNG for the HTML Rich Text
            tier_icon = Path(__file__).parent.joinpath(f"Ranks/{tier}.png")

            # Add Texts
            self.History.setText(match_History)  # <- List which got made to a string
            self.AccuracyText.setText(
                f"Headshots: {headshot_rate}%\n" f"Bodyshots: {bodyshot_rate}%\n" f"Legshots: {legshot_rate}%"
            )
            self.OtherStatsTexts.setText(
                f"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">Other Stats </span><span style=\" font-size:18pt; color:#6a6a6a;\">(Last 10 Matches)</span></p><p><span style=\" font-size:22pt;\">Average KD: {format(total_kills / total_deaths, '.2f')}</span></p><p><span style=\" font-size:22pt; color:#000000;\">Winrate: {round(total_wins / total_matches * 100)}%</span></p></body></html>"
            )
            self.Player.setText(
                f'<html><head/><body><p><span style=" font-size:29pt;">{Details.name}#{Details.tag}<p>Account Level {Account_level} | {Rank} </span><img src="{tier_icon}"width="33"height="33"/><span style=" font-size:20pt;"> {RR}rr</span></p></body></html>'
            )

        except BaseException:
            print(traceback.format_exc())

    def leaderboard(self):
        start_time = time.time()
        try:
            # Get Values
            season = self.Act.currentText()
            region = self.LeaderBoardRegion.currentText()
            player_limit = int(self.Playercount.value())
            player_cards = {}

            # Get API
            if season == current_season:
                leaderboard = valo_api.get_leaderboard(version="v2", region=region)
            else:
                leaderboard = valo_api.get_leaderboard(version="v2", region=region, season_id=season)

            try:
                self.LeaderboardPlayerTemplate.deleteLater()
                self.LeaderboardPlayerBannerTemplate.deleteLater()
                self.LeaderboardPlayerInformationTemplate.deleteLater()
                self.PlayerLayoutTemplate.deleteLater()
            except RuntimeError:
                pass

            # Delete all old Leaderboard stuff
            for i, x in enumerate(self.LeaderboardPlayer):
                try:
                    self.LeaderboardPlayerBanner[i].deleteLater()
                    self.LeaderboardPlayerInformation[i].deleteLater()
                    self.LeaderboardPlayer[i].deleteLater()
                    self.LeaderboardPlayerLayout[i].deleteLater()

                    player_cards = {}
                except KeyError:
                    continue
                except RuntimeError:
                    continue

            # Set all new Leaderboard stuff
            for i, x in enumerate(leaderboard.players):
                if i < player_limit:
                    try:

                        # Setting player
                        self.LeaderboardPlayer[i] = QtWidgets.QFrame(self.PlayerScrollAreaLayout)
                        self.LeaderboardPlayer[i].setEnabled(True)
                        self.LeaderboardPlayer[i].setFrameShape(QtWidgets.QFrame.StyledPanel)
                        self.LeaderboardPlayer[i].setFrameShadow(QtWidgets.QFrame.Raised)
                        self.LeaderboardPlayer[i].setObjectName("PlayerTemplate")
                        self.LeaderboardPlayerLayout[i] = QtWidgets.QHBoxLayout(self.LeaderboardPlayer[i])
                        self.LeaderboardPlayerLayout[i].setContentsMargins(0, 0, 0, 0)
                        self.LeaderboardPlayerLayout[i].setObjectName("PlayerLayoutTemplate")

                        # Setting Banner
                        self.LeaderboardPlayerBanner[i] = QtWidgets.QLabel(self.LeaderboardPlayer[i])
                        self.LeaderboardPlayerBanner[i].setText("")
                        self.LeaderboardPlayerBanner[i].setPixmap(QtGui.QPixmap("ExampleBanner.png"))
                        self.LeaderboardPlayerBanner[i].setScaledContents(False)
                        self.LeaderboardPlayerBanner[i].setObjectName("LeaderboardPlayerBanner")
                        self.LeaderboardPlayerLayout[i].addWidget(self.LeaderboardPlayerBanner[i])
                        self.LeaderboardPlayerInformation[i] = QtWidgets.QLabel(self.LeaderboardPlayer[i])

                        # Getting changed later
                        if self.LeaderBoardRegion.currentText() == "E5A1" or "E5A2" or "E5A3":
                            if x.competitiveTier == 27:
                                rank = "Radiant"
                            elif x.competitiveTier == 26:
                                rank = "Immortal 3"
                            elif x.competitiveTier == 25:
                                rank = "Immortal 2"
                            elif x.competitiveTier == 24:
                                rank = "Immortal 1"
                            elif x.competitiveTier == 23:
                                rank = "Ascendant 3"
                            elif x.competitiveTier == 22:
                                rank = "Ascendant 2"
                            elif x.competitiveTier == 21:
                                rank = "Ascendant 1"
                        else:
                            if x.competitiveTier == 24:
                                rank = "Radiant"
                            elif x.competitiveTier == 23:
                                rank = "Immortal 3"
                            elif x.competitiveTier == 22:
                                rank = "Immortal 2"
                            elif x.competitiveTier == 21:
                                rank = "Immortal 1"

                        # If anonymous else stuff
                        if x.IsAnonymized:
                            self.LeaderboardPlayerInformation[i].setText(
                                f"#{x.leaderboardRank} | Anonymous Player | {rank} {x.rankedRating}rr | {x.numberOfWins} Wins"
                            )
                        else:
                            self.LeaderboardPlayerInformation[i].setText(
                                f"#{x.leaderboardRank} | {x.gameName}#{x.tagLine} | {rank} {x.rankedRating}rr | {x.numberOfWins} Wins | {x.puuid}"
                            )

                        # blah blah layouts..
                        self.LeaderboardPlayerInformation[i].setAlignment(QtCore.Qt.AlignCenter)
                        self.LeaderboardPlayerInformation[i].setObjectName("LeaderboardPlayerInformation")
                        self.LeaderboardPlayerLayout[i].addWidget(self.LeaderboardPlayerInformation[i])
                        self.LeaderboardSpacer[i] = QtWidgets.QSpacerItem(
                            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
                        )
                        self.LeaderboardPlayerLayout[i].addItem(self.LeaderboardSpacer[i])
                        self.verticalLayout_8.addWidget(self.LeaderboardPlayer[i])

                        # Getting players banner and add it to player_cards
                        player_card = f"https://media.valorant-api.com/playercards/{x.PlayerCardID}/smallart.png"
                        player_cards[i] = player_card

                    except AttributeError:
                        break
                else:
                    break

            # Get & Set Banner
            with concurrent.futures.ThreadPoolExecutor() as executor:
                image = executor.map(requests.get, player_cards.values())
                image = tuple(image)

            for _ in player_cards:
                img = QImage()
                img.loadFromData(image[_].content)
                self.LeaderboardPlayerBanner[_].setPixmap(QPixmap(img))

            print(f"LEADERBOARD took --- %s seconds ---" % (time.time() - start_time))

        except BaseException:
            print(traceback.format_exc())

    def reset_information(self):
        self.PlayerName.setText("")
        self.PlayerName.setPlaceholderText("PLAYER NAME (16 characters)")
        self.PlayerTag.setText("")
        self.PlayerTag.setPlaceholderText("PLAYER TAG (5 characters)")
        self.PlayerBanner.setPixmap(QtGui.QPixmap("StandardBanner.png"))
        self.PlayerIDs.setText("puu-ID | EU")
        self.Player.setText(
            '<html><head/><body><p><span style=" font-size:29pt;">Player#Tag<p>Account Level 0 | Rank </span><img src="StandardRank.png"width="33"height="33"/><span style=" font-size:20pt;"> 0rr</span></p></body></html>'
        )
        self.AccuracyText.setText("Headshots: 0%\n" "Bodyshots: 0%\n" "Legshots: 0%")
        self.AccuracyLogo.setPixmap(QtGui.QPixmap("Basic.png"))
        self.OtherStatsTexts.setText(
            '<html><head/><body><p align="center"><span style=" font-size:22pt;">Other Stats </span><span style=" font-size:18pt; color:#6a6a6a;">(Last 10 Matches)</span></p><p><span style=" font-size:22pt;">Average KD: 0.00</span></p><p><span style=" font-size:22pt; color:#000000;">Winrate: 0%</span></p></body></html>'
        )
        self.CompHistory.setText(
            "Matchmaking Ratio \n"
            "Competitive Wins \n"
            "Competitive Games played \n"
            "Previous Ranks \n"
            "Rank History\n"
            ""
        )
        self.History.setText(
            "Day, Date, Time | Match ID\n"
            "REGION - CLUSTER\n"
            " Map - Gamemode - Agent Played: Jett\n"
            "0-0 \n"
            "Kills Assists Deaths - KD |  Score"
        )


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ValorantTrackerByNavisGames = QtWidgets.QMainWindow()
    ui = Ui_ValorantTrackerByNavisGames()
    ui.setupUi(ValorantTrackerByNavisGames)
    ValorantTrackerByNavisGames.show()
    sys.exit(app.exec_())
