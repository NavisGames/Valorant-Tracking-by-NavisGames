# Credits for this program go to NavisGames, selling this program or saying it's yours is not allowed! Read the
# license for more. If you want, please fork this program to share what you changed in this program ^^

from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette, QColor, QImage, QPixmap, QFontDatabase
from PyQt5.QtWidgets import QApplication
from pathlib import Path
import traceback
import valo_api
import requests
import concurrent.futures
import time
from functions import (
    get_image,
    display_time,
    clearLayout,
    findAgentOfPlayer,
    findStatsOfPlayer,
    findTeamOfPlayer,
    findRoundPlayer,
    current_season,
    get_matches,
)


class Ui_ValorantTrackerByNavisGames(object):
    def setupUi(self, ValorantTrackerByNavisGames):
        try:
            # Creating MainWindow
            self.dark_mode = False
            ValorantTrackerByNavisGames.setObjectName(
                "ValorantTrackerByNavisGames"
            )
            ValorantTrackerByNavisGames.setEnabled(True)
            ValorantTrackerByNavisGames.resize(1124, 922)
            ValorantTrackerByNavisGames.setMaximumSize(
                QtCore.QSize(16777215, 16777215)
            )

            # Creating Font Standards
            QFontDatabase.addApplicationFont("Images/Tungsten-Bold.ttf")
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
            ValorantTrackerByNavisGames.setWindowTitle(
                "Valorant Tracking 2.2 By NavisGames"
            )
            icon = QtGui.QIcon()
            iconImage = Path(__file__).parent.joinpath("Images/icon.png")
            icon.addPixmap(
                QtGui.QPixmap(str(iconImage)),
                QtGui.QIcon.Normal,
                QtGui.QIcon.Off,
            )
            ValorantTrackerByNavisGames.setWindowIcon(icon)
            ValorantTrackerByNavisGames.setDockOptions(
                QtWidgets.QMainWindow.AllowTabbedDocks
                | QtWidgets.QMainWindow.AnimatedDocks
            )

            # Create CENTRAL WIDGET
            self.centralwidget = QtWidgets.QWidget(ValorantTrackerByNavisGames)
            self.centralwidget.setObjectName("centralwidget")

            # Create Layout for WIDGET
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
            self.PlayerInput.setLineWidth(0)
            self.PlayerInput.setObjectName("PlayerInput")

            # Creating Player Input Layout
            self.horizontalLayout = QtWidgets.QHBoxLayout(self.PlayerInput)
            self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout.setSpacing(5)
            self.horizontalLayout.setObjectName("horizontalLayout")

            # Light / Dark-mode switcher
            self.modeSwitcher = QtWidgets.QPushButton(self.PlayerInput)
            self.modeSwitcher.setAutoFillBackground(False)
            self.modeSwitcher.setText("")
            icon1 = QtGui.QIcon()
            LightMode = Path(__file__).parent.joinpath("Images/LightMode.webp")
            icon1.addPixmap(
                QtGui.QPixmap(str(LightMode)),
                QtGui.QIcon.Normal,
                QtGui.QIcon.Off,
            )
            self.modeSwitcher.setIcon(icon1)
            self.modeSwitcher.setIconSize(QtCore.QSize(32, 32))
            self.modeSwitcher.setAutoDefault(False)
            self.modeSwitcher.setDefault(False)
            self.modeSwitcher.setFlat(False)
            self.modeSwitcher.setObjectName("modeSwitcher")
            self.horizontalLayout.addWidget(self.modeSwitcher)

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
            self.PlayerRegion.setEditable(True)
            self.PlayerRegionEdit = self.PlayerRegion.lineEdit()
            self.PlayerRegionEdit.setAlignment(Qt.AlignCenter)
            self.PlayerRegionEdit.setReadOnly(True)
            self.horizontalLayout.addWidget(self.PlayerRegion)

            # Create Player Gamemode Input
            self.PlayerGamemode = QtWidgets.QComboBox(self.PlayerInput)
            self.PlayerGamemode.setEnabled(True)
            self.PlayerGamemode.setLayoutDirection(QtCore.Qt.LeftToRight)
            self.PlayerGamemode.setCurrentText("ALL")
            self.PlayerGamemode.setMaxVisibleItems(6)
            self.PlayerGamemode.setMaxCount(6)
            self.PlayerGamemode.setDuplicatesEnabled(False)
            self.PlayerGamemode.setObjectName("PlayerGamemode")
            self.PlayerGamemode.addItem("")
            self.PlayerGamemode.setItemText(0, "ALL")
            self.PlayerGamemode.addItem("")
            self.PlayerGamemode.setItemText(1, "COMPETITIVE")
            self.PlayerGamemode.addItem("")
            self.PlayerGamemode.setItemText(2, "UNRATED")
            self.PlayerGamemode.addItem("")
            self.PlayerGamemode.setItemText(3, "SPIKERUSH")
            self.PlayerGamemode.addItem("")
            self.PlayerGamemode.setItemText(4, "SWIFTPLAY")
            self.PlayerGamemode.addItem("")
            self.PlayerGamemode.setItemText(5, "DEATHMATCH")
            self.PlayerGamemode.setEditable(True)
            self.PlayerGamemodeEdit = self.PlayerGamemode.lineEdit()
            self.PlayerGamemodeEdit.setAlignment(Qt.AlignCenter)
            self.PlayerGamemodeEdit.setReadOnly(True)
            self.horizontalLayout.addWidget(self.PlayerGamemode)

            # Create Apply, Reset Buttons
            self.DialogButton = QtWidgets.QDialogButtonBox(self.PlayerInput)
            self.DialogButton.setEnabled(True)
            self.DialogButton.setOrientation(QtCore.Qt.Horizontal)
            self.DialogButton.setCenterButtons(False)
            self.DialogButton.setObjectName("DialogButton")

            # Create Buttons for DialogBox
            self.getButton = QtWidgets.QPushButton("EXECUTE")
            self.getButton.setDefault(True)
            self.resetButton = QtWidgets.QPushButton("RESET")
            self.resetButton.setDefault(True)
            self.DialogButton.addButton(
                self.getButton, QtWidgets.QDialogButtonBox.ActionRole
            )
            self.DialogButton.addButton(
                self.resetButton, QtWidgets.QDialogButtonBox.ActionRole
            )

            # Layers
            self.horizontalLayout.addWidget(self.DialogButton)
            self.horizontalLayout.setStretch(1, 7)
            self.horizontalLayout.setStretch(2, 6)
            self.verticalLayout.addWidget(self.PlayerInput)

            # Create Player Output Banner & Data etc. Frame
            self.PlayerInformation = QtWidgets.QFrame(self.Home)
            self.PlayerInformation.setEnabled(True)
            self.PlayerInformation.setLineWidth(0)
            self.PlayerInformation.setObjectName("PlayerInformation")
            self.horizontalLayout_2 = QtWidgets.QHBoxLayout(
                self.PlayerInformation
            )
            self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout_2.setSpacing(5)
            self.horizontalLayout_2.setObjectName("horizontalLayout_2")

            # Create Player Banner PixMap
            ExampleBanner = Path(__file__).parent.joinpath(
                "Images/Example/ExampleWideBanner.png"
            )
            self.PlayerBanner = QtWidgets.QLabel(self.PlayerInformation)
            self.PlayerBanner.setEnabled(True)
            self.PlayerBanner.setLineWidth(1)
            self.PlayerBanner.setText("")
            self.PlayerBanner.setPixmap(QtGui.QPixmap(str(ExampleBanner)))
            self.PlayerBanner.setScaledContents(False)
            self.PlayerBanner.setAlignment(QtCore.Qt.AlignCenter)
            self.PlayerBanner.setWordWrap(False)
            self.PlayerBanner.setObjectName("PlayerBanner")
            self.horizontalLayout_2.addWidget(self.PlayerBanner)

            # Create Player Information Frame
            self.PlayerDatas = QtWidgets.QFrame(self.PlayerInformation)
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
            self.PlayerIDs.setText("puu-ID | EU")
            self.PlayerIDs.setAlignment(
                QtCore.Qt.AlignLeading
                | QtCore.Qt.AlignLeft
                | QtCore.Qt.AlignVCenter
            )
            self.PlayerIDs.setObjectName("PlayerIDs")
            self.verticalLayout_5.addWidget(self.PlayerIDs)

            # Creating Player, Add HTML Text with AccountLevel, Player#Tag and Rank.
            tier_icon = Path(__file__).parent.joinpath(
                "Images\Example\ExampleRank.png"
            )
            self.Player = QtWidgets.QLabel(self.PlayerDatas)
            self.Player.setEnabled(True)
            font = QtGui.QFont()
            font.setPointSize(35)
            self.Player.setFont(font)
            self.Player.setText(
                f'<html><head/><body><p><span style=" font-size:29pt;">Player#Tag<p'
                f'>Account Level 0 | Iron 3 </span><img src="{tier_icon}"width="33 '
                f'"height="33"/><span style=" font-size:20pt;"> 0rr</span></p></body></html>'
            )
            self.Player.setTextFormat(QtCore.Qt.RichText)
            self.Player.setAlignment(
                QtCore.Qt.AlignLeading
                | QtCore.Qt.AlignLeft
                | QtCore.Qt.AlignVCenter
            )
            self.Player.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
            self.Player.setObjectName("Player")

            # Layer Stuff. IDC
            self.verticalLayout_5.addWidget(self.Player)
            self.horizontalLayout_2.addWidget(self.PlayerDatas)
            self.verticalLayout.addWidget(self.PlayerInformation)

            # Creating Accuracy & Stats Frame
            self.GeneralStats = QtWidgets.QFrame(self.Home)
            self.GeneralStats.setLineWidth(1)
            self.GeneralStats.setObjectName("GeneralStats")
            self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.GeneralStats)
            self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout_8.setObjectName("horizontalLayout_8")

            # Spacer Item
            spacerItem1 = QtWidgets.QSpacerItem(
                40,
                20,
                QtWidgets.QSizePolicy.Expanding,
                QtWidgets.QSizePolicy.Minimum,
            )
            self.horizontalLayout_8.addItem(spacerItem1)

            # Creating Accuracy Stats
            self.AccuarcyStats = QtWidgets.QFrame(self.GeneralStats)
            self.AccuarcyStats.setLineWidth(1)
            self.AccuarcyStats.setObjectName("AccuarcyStats")
            self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.AccuarcyStats)
            self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout_6.setSpacing(0)
            self.verticalLayout_6.setObjectName("verticalLayout_6")

            # Creating Accuracy Title
            self.AccuracyTitle = QtWidgets.QLabel(self.AccuarcyStats)
            font = QtGui.QFont()
            font.setUnderline(False)
            font.setStrikeOut(False)
            self.AccuracyTitle.setFont(font)
            self.AccuracyTitle.setText(
                '<html><head/><body><p><span style=" font-size:22pt;">Accuracy </span><span style=" font-size:18pt; '
                'color:#6a6a6a;">(Last 10 Matches)</span></p></body></html> '
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
            Basic = Path(__file__).parent.joinpath("Images/Dummy/Basic.png")
            self.AccuracyLogo = QtWidgets.QLabel(self.Accuracy)
            self.AccuracyLogo.setLayoutDirection(QtCore.Qt.LeftToRight)
            self.AccuracyLogo.setText("")
            self.AccuracyLogo.setPixmap(QtGui.QPixmap(str(Basic)))
            self.AccuracyLogo.setAlignment(QtCore.Qt.AlignCenter)
            self.AccuracyLogo.setObjectName("AccuracyLogo")
            self.horizontalLayout_9.addWidget(self.AccuracyLogo)

            # Creating Accuracy Texts for HS Rate etc.
            self.AccuracyText = QtWidgets.QLabel(self.Accuracy)
            self.AccuracyText.setLayoutDirection(QtCore.Qt.LeftToRight)
            self.AccuracyText.setText(
                "Headshots: 0%\n" "Bodyshots: 0%\n" "Legshots: 0%"
            )
            self.AccuracyText.setAlignment(QtCore.Qt.AlignCenter)
            self.AccuracyText.setObjectName("AccuracyText")
            self.horizontalLayout_9.addWidget(self.AccuracyText)
            self.verticalLayout_6.addWidget(self.Accuracy)
            self.horizontalLayout_8.addWidget(self.AccuarcyStats)

            # Spacer Item
            spacerItem2 = QtWidgets.QSpacerItem(
                40,
                20,
                QtWidgets.QSizePolicy.Expanding,
                QtWidgets.QSizePolicy.Minimum,
            )
            self.horizontalLayout_8.addItem(spacerItem2)

            # Creating K/D & Win rate Frame
            self.OtherStats = QtWidgets.QFrame(self.GeneralStats)
            self.OtherStats.setObjectName("OtherStats")
            self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.OtherStats)
            self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout_9.setObjectName("verticalLayout_9")

            # Creating HTML Code with K/D, Win rate and the Title in it
            self.OtherStatsTexts = QtWidgets.QLabel(self.OtherStats)
            self.OtherStatsTexts.setText(
                '<html><head/><body><p align="center"><span style=" font-size:22pt;">Stats </span><span style=" '
                'font-size:18pt; color:#6a6a6a;">(Last 10 Matches)</span></p><p><span style=" font-size:22pt;">'
                'K/D: 0.00</span></p><p><span style=" font-size:22pt;">Average Combat Score: 0</span></p><p><span style=" font-size:22pt;">Average Damage per Round: 0</span></p><p><span style=" font-size:22pt;">Winrate: 0%</span></p></body></html> '
            )
            self.OtherStatsTexts.setTextFormat(QtCore.Qt.RichText)
            self.OtherStatsTexts.setScaledContents(False)
            self.OtherStatsTexts.setAlignment(
                QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop
            )
            self.OtherStatsTexts.setObjectName("OtherStatsTexts")
            self.verticalLayout_9.addWidget(self.OtherStatsTexts)
            self.horizontalLayout_8.addWidget(self.OtherStats)

            # Spacer Item
            spacerItem3 = QtWidgets.QSpacerItem(
                40,
                20,
                QtWidgets.QSizePolicy.Expanding,
                QtWidgets.QSizePolicy.Minimum,
            )
            self.horizontalLayout_8.addItem(spacerItem3)

            # Creating Stats Frame
            self.Stats = QtWidgets.QFrame(self.Home)
            self.Stats.setObjectName("Stats")
            self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.Stats)
            self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout_6.setObjectName("horizontalLayout_6")

            # Creating CompetitiveStats Frame for Stats
            self.CompInformation = QtWidgets.QFrame(self.Stats)
            self.CompInformation.setEnabled(True)
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
            self.CompScrollArea.setVerticalScrollBarPolicy(
                QtCore.Qt.ScrollBarAsNeeded
            )
            self.CompScrollArea.setHorizontalScrollBarPolicy(
                QtCore.Qt.ScrollBarAlwaysOff
            )
            self.CompScrollArea.setWidgetResizable(True)
            self.CompScrollArea.setAlignment(QtCore.Qt.AlignCenter)
            self.CompScrollArea.setObjectName("CompScrollArea")
            self.CompScrollLayout = QtWidgets.QWidget()
            self.CompScrollLayout.setGeometry(QtCore.QRect(0, 0, 519, 355))
            self.CompScrollLayout.setObjectName("CompScrollLayout")
            self.horizontalLayout_3 = QtWidgets.QHBoxLayout(
                self.CompScrollLayout
            )
            self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout_3.setObjectName("horizontalLayout_3")

            # Creating Competitive History
            self.CompHistory = QtWidgets.QLabel(self.CompScrollLayout)
            self.CompHistory.setEnabled(True)
            font = QtGui.QFont()
            font.setPointSize(14)
            self.CompHistory.setFont(font)
            self.CompHistory.setLineWidth(1)
            self.CompHistory.setWordWrap(True)
            self.CompHistory.setText(
                "Matchmaking Ratio \n"
                "Competitive Wins \n"
                "Competitive Games played \n"
                "Previous Ranks \n"
                "Rank History\n"
                ""
            )
            self.CompHistory.setAlignment(
                QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop
            )
            self.CompHistory.setObjectName("CompHistory")
            self.horizontalLayout_3.addWidget(self.CompHistory)
            self.CompScrollArea.setWidget(self.CompScrollLayout)
            self.verticalLayout_2.addWidget(self.CompScrollArea)
            self.horizontalLayout_6.addWidget(self.CompInformation)

            # Creating Match History Frame for Stats
            self.MatchHistory = QtWidgets.QFrame(self.Stats)
            self.MatchHistory.setEnabled(True)
            self.MatchHistory.setObjectName("MatchHistory")
            self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.MatchHistory)
            self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout_4.setObjectName("verticalLayout_4")

            # Creating History Title
            self.HistoryTitle = QtWidgets.QLabel(self.MatchHistory)
            self.HistoryTitle.setEnabled(True)
            self.HistoryTitle.setText("MATCH HISTORY")
            self.HistoryTitle.setAlignment(QtCore.Qt.AlignCenter)
            self.HistoryTitle.setObjectName("HistoryTitle")
            self.verticalLayout_4.addWidget(self.HistoryTitle)

            # Creating ScrollArea for the Field of Match History
            self.HistoryScrollArea = QtWidgets.QScrollArea(self.MatchHistory)
            self.HistoryScrollArea.setEnabled(True)
            self.HistoryScrollArea.setLineWidth(1)
            self.HistoryScrollArea.setHorizontalScrollBarPolicy(
                QtCore.Qt.ScrollBarAlwaysOff
            )
            self.HistoryScrollArea.setWidgetResizable(True)
            self.HistoryScrollArea.setObjectName("HistoryScrollArea")
            self.HistoryScrollLayout = QtWidgets.QWidget()
            self.HistoryScrollLayout.setGeometry(QtCore.QRect(0, 0, 519, 355))
            self.HistoryScrollLayout.setObjectName("HistoryScrollLayout")
            self.horizontalLayout_4 = QtWidgets.QHBoxLayout(
                self.HistoryScrollLayout
            )
            self.horizontalLayout_4.setObjectName("horizontalLayout_4")

            # Creating MatchHistory Text.
            self.History = QtWidgets.QLabel(self.HistoryScrollLayout)
            self.History.setEnabled(True)
            font = QtGui.QFont()
            font.setPointSize(14)
            self.History.setFont(font)
            self.History.setWordWrap(True)
            self.History.setText(
                "Day, Date, Time\n"
                "Match ID\n"
                "Region - Cluster\n"
                "Map | Gamemode | Agent: Jett\n"
                "0-0 WON\n"
                "Kills Assists Deaths | 0.00 K/D\n"
                "HS%: 0% | ACS: 0 | ADR: 0 | Total Score: 0\n"
            )
            self.History.setAlignment(
                QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop
            )
            self.History.setObjectName("History")
            self.horizontalLayout_4.addWidget(self.History)
            self.HistoryScrollArea.setWidget(self.HistoryScrollLayout)
            self.verticalLayout_4.addWidget(self.HistoryScrollArea)
            self.horizontalLayout_6.addWidget(self.MatchHistory)

            # Adding Widgets to HOME
            self.verticalLayout.addWidget(self.Stats)
            self.verticalLayout.addWidget(self.GeneralStats)

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
            self.LeaderBoardInput.setObjectName("LeaderBoardInput")
            self.horizontalLayout_7 = QtWidgets.QHBoxLayout(
                self.LeaderBoardInput
            )
            self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
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
            self.Act.setEditable(True)
            self.horizontalLayout_7.addWidget(self.Act)
            self.ActEdit = self.Act.lineEdit()
            self.ActEdit.setAlignment(Qt.AlignCenter)
            self.ActEdit.setReadOnly(True)

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
            self.LeaderBoardRegion.setEditable(True)
            self.horizontalLayout_7.addWidget(self.LeaderBoardRegion)
            self.LeaderboardEdit = self.LeaderBoardRegion.lineEdit()
            self.LeaderboardEdit.setAlignment(Qt.AlignCenter)
            self.LeaderboardEdit.setReadOnly(True)

            # Create Player count Box
            self.Playercount = QtWidgets.QSpinBox(self.LeaderBoardInput)
            self.Playercount.setWrapping(False)
            self.Playercount.setFrame(True)
            self.Playercount.setAlignment(QtCore.Qt.AlignCenter)
            self.Playercount.setButtonSymbols(
                QtWidgets.QAbstractSpinBox.UpDownArrows
            )
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
            self.Players.setContentsMargins(0, 0, 0, 0)
            self.Players.setObjectName("Players")
            self.PlayerScrollArea = QtWidgets.QScrollArea(self.Leaderboard)
            self.PlayerScrollArea.setLineWidth(3)
            self.PlayerScrollArea.setHorizontalScrollBarPolicy(
                QtCore.Qt.ScrollBarAlwaysOff
            )
            self.PlayerScrollArea.setSizeAdjustPolicy(
                QtWidgets.QAbstractScrollArea.AdjustIgnored
            )
            self.PlayerScrollArea.setWidgetResizable(True)
            self.PlayerScrollArea.setAlignment(QtCore.Qt.AlignCenter)
            self.PlayerScrollArea.setObjectName("PlayerScrollArea")
            self.PlayerScrollAreaLayout = QtWidgets.QWidget()
            self.PlayerScrollAreaLayout.setGeometry(
                QtCore.QRect(0, 0, 486, 145)
            )
            self.PlayerScrollAreaLayout.setObjectName("PlayerScrollAreaLayout")

            self.PlayerScrollArea.setWidget(self.PlayerScrollAreaLayout)
            self.Players.addWidget(self.PlayerScrollArea)
            self.verticalLayout_3.addLayout(self.Players)
            self.Tabs.addTab(self.Leaderboard, "LEADERBOARD")

            # Create Leader Player Stuff for function
            self.LeaderboardPlayerBanner = dict()
            self.LeaderboardPlayerInformation = dict()
            self.LeaderboardPlayer = dict()
            self.LeaderboardPlayerLayout = dict()
            self.LeaderboardPlayerSpacer = dict()

            self.verticalLayout_8 = QtWidgets.QVBoxLayout(
                self.PlayerScrollAreaLayout
            )
            self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout_8.setSpacing(5)
            self.verticalLayout_8.setObjectName("verticalLayout_8")

            # Create Dicts with Bundles and use Valorant API to get all current bundles
            current_Bundle = valo_api.get_store_featured_v2()
            self.Bundle = dict()

            for i, bundles in enumerate(current_Bundle):
                bundleUuid = current_Bundle[i].bundle_uuid

                # Getting Bundle Banner as PixMap
                bundleJson = requests.get(
                    url=f"https://valorant-api.com/v1/bundles/{bundleUuid}"
                ).json()
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    img = executor.submit(
                        get_image, bundleJson["data"]["displayIcon2"]
                    )
                    img = img.result()

                # Creating Bundle
                self.Bundle[i] = QtWidgets.QWidget()
                self.Bundle[i].setObjectName("Bundle")
                self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.Bundle[i])
                self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout_10.setSpacing(0)
                self.verticalLayout_10.setObjectName("verticalLayout_10")

                # Creating Bundle MainFrame
                self.BundleMain = QtWidgets.QFrame(self.Bundle[i])
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
                    "Spray: 0 VP | 0 VP -> Whole Bundle"
                )
                self.BundlePrices.setAlignment(QtCore.Qt.AlignCenter)
                self.BundlePrices.setObjectName("BundlePrices")
                self.verticalLayout_11.addWidget(self.BundlePrices)

                # Create Seconds Remaining in Shop
                self.BundleLast = QtWidgets.QLabel(self.BundleMain)
                font = QtGui.QFont()
                font.setPointSize(15)
                self.BundleLast.setFont(font)
                self.BundleLast.setText(
                    "Bundle in Shop until: Weeks : Days : Hours"
                )
                self.BundleLast.setAlignment(QtCore.Qt.AlignCenter)
                self.BundleLast.setObjectName("BundleLast")
                self.verticalLayout_11.addWidget(self.BundleLast)
                self.verticalLayout_10.addWidget(self.BundleMain)

                # Get every item and set a string (before a list!)
                Prices = [
                    f"Bundle Price - {current_Bundle[i].bundle_price} Valorant Points\n"
                ]
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
                self.BundleTitle.setText(
                    f"{bundleJson['data']['displayName']}"
                )
                self.BundlePrices.setText(Prices)
                self.BundleLast.setText(
                    f"Bundle remaining in Shop: {display_time(bundles.seconds_remaining, 3)}"
                )

                # Add Bundles
                self.Tabs.addTab(
                    self.Bundle[i],
                    f"{bundleJson['data']['displayName']} Bundle",
                )

            # Index, Layout
            self.verticalLayout_7.addWidget(self.Tabs)
            ValorantTrackerByNavisGames.setCentralWidget(self.centralwidget)
            self.Tabs.setCurrentIndex(0)
            self.PlayerRegion.setCurrentIndex(0)
            self.LeaderBoardRegion.setCurrentIndex(0)

            # Functions
            self.getButton.clicked.connect(self.get_information)
            self.resetButton.clicked.connect(self.reset_information)
            self.Reload.clicked.connect(self.leaderboard)
            self.modeSwitcher.clicked.connect(self.modeSwitch)
            QtCore.QMetaObject.connectSlotsByName(ValorantTrackerByNavisGames)

        except BaseException:
            print(traceback.format_exc())

    def get_information(self):
        try:
            # API functions
            Details = valo_api.get_account_details_by_name(
                version="v1",
                name=self.PlayerName.text(),
                tag=self.PlayerTag.text(),
            )

            # Get Rank, RR and MMR
            RankDetails = valo_api.get_mmr_details_by_name_v2(
                region=self.PlayerRegion.currentText(),
                name=self.PlayerName.text(),
                tag=self.PlayerTag.text(),
            )

            # Get Match History
            if self.PlayerGamemode.currentText() != "ALL":
                HistoryDetails = valo_api.get_match_history_by_name(
                    version="v3",
                    region=self.PlayerRegion.currentText(),
                    name=self.PlayerName.text(),
                    tag=self.PlayerTag.text(),
                    size=10,
                    game_mode=self.PlayerGamemode.currentText().lower(),
                )
            else:
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

            # DETAILS ~ puuid, Region, Account Level and the PlayerCard
            # RANK DETAILS ~ Rank, RR, MMR
            puuid = Details.puuid
            Region = Details.region
            Account_level = Details.account_level
            Card = str(Details.card.wide)
            Rank = RankDetails.current_data.currenttierpatched
            RR = RankDetails.current_data.ranking_in_tier
            MMR = RankDetails.current_data.elo

            # Sets PUU-ID and Region
            self.PlayerIDs.setText(f"{puuid} | {Region}")

            # Wins, Games Played
            try:
                wins = RankDetails.by_season[current_season.lower()].wins
                games_played = RankDetails.by_season[
                    current_season.lower()
                ].number_of_games
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
                    if (
                        lastRank[x].final_rank_patched is not None
                        and x != current_season.lower()
                    ):
                        previous_ranks.append(
                            f"{x.upper()}: {lastRank[x].final_rank_patched} | {lastRank[x].wins} Wins - {lastRank[x].number_of_games}Game(s) played\n "
                        )
                    else:
                        continue
                except BaseException:
                    print(traceback.format_exc())

            # If there is a rank, add a rank history
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

            # Some Variables
            headshots = 0
            bodyshots = 0
            legshots = 0
            total_damage = 0
            total_rounds = 0
            total_combat_score = 0
            total_kills = 0
            total_deaths = 0
            total_wins = 0
            total_matches = 0

            for x in HistoryDetails:
                # Match, Team, Players and Rounds played
                match = x.metadata
                teams = x.teams
                players = x.players
                rounds_played = match.rounds_played

                # Get Stats of Player with get_stats function
                get_stats = findStatsOfPlayer(Details.name, players)

                # Get Agent of Player
                get_agent = findAgentOfPlayer(Details.name, players)

                # Some Variables
                kills = get_stats.kills
                deaths = get_stats.deaths
                assists = get_stats.assists
                total_score = get_stats.score
                combat_score = total_score / rounds_played
                damage = 0

                for rounds in x.rounds:
                    PlayerDamage = findRoundPlayer(
                        f"{Details.name}#{Details.tag}", rounds
                    )
                    damage += PlayerDamage[0]
                    total_rounds += 1

                # Add Aim rates
                headshots += get_stats.headshots
                bodyshots += get_stats.bodyshots
                legshots += get_stats.legshots

                # Some Variables
                total_kills += kills
                total_deaths += deaths
                total_combat_score += combat_score
                total_damage += damage

                # Calculate HS% in the Match
                try:
                    HSR = round(
                        get_stats.headshots
                        / (
                            get_stats.headshots
                            + get_stats.bodyshots
                            + get_stats.legshots
                        )
                        * 100
                    )
                except ZeroDivisionError:
                    HSR = None

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

                # If Deathmatch, remove Rounds, Won/Lost and Combat Score
                if mode == "Deathmatch":
                    match_History.append(
                        f"{match.game_start_patched}\n"
                        f"{match_id}\n"
                        f"{region} - {cluster}\n"
                        f"{match_map} | {mode} | Agent: {get_agent[0]}\n"
                        f"{kills} Kills {assists} Assists {deaths} Deaths | {KD} K/D\n"
                        f"CS: {round(combat_score)} | Total Score: {total_score}\n\n"
                    )
                else:
                    match_History.append(
                        f"{match.game_start_patched}\n"
                        f"{match_id}\n"
                        f"{region} - {cluster}\n"
                        f"{match_map} | {mode} | Agent: {get_agent[0]}\n"
                        f"{rounds_won}-{rounds_lost} {won}\n"
                        f"{kills} Kills {assists} Assists {deaths} Deaths | {KD} K/D\n"
                        f"HS%: {HSR}% | CS: {round(combat_score)} | ADR: {round(damage / rounds_played)} | Total Score: {total_score}\n\n"
                    )

            # Set Match to Text
            match_History = "".join(match_History)

            HeadshotDummy = Path(__file__).parent.joinpath(
                "Images/Dummy/Headshot.png"
            )
            BodyshotDummy = Path(__file__).parent.joinpath(
                "Images/Dummy/Bodyshot.png"
            )
            LegshotDummy = Path(__file__).parent.joinpath(
                "Images/Dummy/Legshot.png"
            )
            BasicDummy = Path(__file__).parent.joinpath(
                "Images/Dummy/Basic.png"
            )

            # Set Rates with Math
            if self.PlayerGamemode.currentText() != "DEATHMATCH":
                headshot_rate = round(
                    headshots / (headshots + bodyshots + legshots) * 100
                )
                bodyshot_rate = round(
                    bodyshots / (headshots + bodyshots + legshots) * 100
                )
                legshot_rate = round(
                    legshots / (headshots + bodyshots + legshots) * 100
                )

                # Set Dummy Prior

                if (
                    headshot_rate > bodyshot_rate
                    and headshot_rate > legshot_rate
                ):
                    self.AccuracyLogo.setPixmap(
                        QtGui.QPixmap(str(HeadshotDummy))
                    )
                elif (
                    bodyshot_rate > headshot_rate
                    and bodyshot_rate > legshot_rate
                ):
                    self.AccuracyLogo.setPixmap(
                        QtGui.QPixmap(str(BodyshotDummy))
                    )
                elif (
                    legshot_rate > headshot_rate
                    and legshot_rate > bodyshot_rate
                ):

                    self.AccuracyLogo.setPixmap(
                        QtGui.QPixmap(str(LegshotDummy))
                    )
            else:
                headshot_rate = "-"
                bodyshot_rate = "-"
                legshot_rate = "-"
                self.AccuracyLogo.setPixmap(QtGui.QPixmap(str(BasicDummy)))

            # Gets the current Rank AS TIER INDEX (int) and compares it with the index data, to get the RANK IMAGE
            tier_index = RankDetails.current_data.currenttier
            data = requests.get(
                "https://valorant-api.com/v1/competitivetiers"
            ).json()
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
            tier_icon = Path(__file__).parent.joinpath(
                f"Images/Ranks/{tier}.png"
            )

            # Add Texts
            self.History.setText(
                match_History
            )  # <- List which got made to a string
            self.AccuracyText.setText(
                f"Headshots: {headshot_rate}%\n"
                f"Bodyshots: {bodyshot_rate}%\n"
                f"Legshots: {legshot_rate}%"
            )
            self.OtherStatsTexts.setText(
                f'<html><head/><body><p align="center"><span style=" font-size:22pt;">Stats </span><span '
                f'style=" font-size:18pt; color:#6a6a6a;">(Last 10 Matches)</span></p><p><span style=" '
                f"font-size:22pt;\">K/D: {format(total_kills / total_deaths, '.2f')}</span></p><p><span "
                f'style=" font-size:22pt; ">Average Combat Score: '
                f"{round(total_combat_score / total_matches)}</span></p>"
                f'<p><span style=" font-size:22pt; ">Average Damage per Round: '
                f"{round(total_damage / total_rounds)}</span></p>"
                f'<p><span style=" font-size:22pt; ">Winrate: '
                f"{round(total_wins / total_matches * 100)}%</span></p></body></html> "
            )
            self.Player.setText(
                f'<html><head/><body><p><span style=" font-size:29pt;">{Details.name}#{Details.tag}<p'
                f'>Account Level {Account_level} | {Rank} </span><img src="{tier_icon}"width="33 '
                f'"height="33"/><span style=" font-size:20pt;"> {RR}rr</span></p></body></html>'
            )

        except BaseException:
            print(traceback.format_exc())

    def leaderboard(self):
        start_time = time.time()
        try:
            # Get Values
            season = self.Act.currentText().lower()
            region = self.LeaderBoardRegion.currentText()
            player_limit = int(self.Playercount.value())
            player_cards = {}

            try:
                clearLayout(self.verticalLayout_8)
            except AttributeError:
                pass

            # Get API
            leaderboard = valo_api.get_leaderboard(
                version="v2", region=region, season_id=season
            )

            # Set all new Leaderboard stuff
            for i, x in enumerate(leaderboard.players):
                if i < player_limit:
                    try:

                        # Setting player
                        self.LeaderboardPlayer[i] = QtWidgets.QFrame(
                            self.PlayerScrollAreaLayout
                        )
                        self.LeaderboardPlayer[i].setEnabled(True)
                        self.LeaderboardPlayer[i].setObjectName(
                            "PlayerTemplate"
                        )
                        self.LeaderboardPlayerLayout[
                            i
                        ] = QtWidgets.QHBoxLayout(self.LeaderboardPlayer[i])
                        self.LeaderboardPlayerLayout[i].setContentsMargins(
                            0, 0, 0, 0
                        )
                        self.LeaderboardPlayerLayout[i].setObjectName(
                            "PlayerLayoutTemplate"
                        )

                        # Setting Banner
                        ExampleBanner = Path(__file__).parent.joinpath(
                            "Images/Example/ExampleBanner.png"
                        )
                        self.LeaderboardPlayerBanner[i] = QtWidgets.QLabel(
                            self.LeaderboardPlayer[i]
                        )
                        self.LeaderboardPlayerBanner[i].setText("")
                        self.LeaderboardPlayerBanner[i].setPixmap(
                            QtGui.QPixmap(str(ExampleBanner))
                        )
                        self.LeaderboardPlayerBanner[i].setScaledContents(
                            False
                        )
                        self.LeaderboardPlayerBanner[i].setObjectName(
                            "LeaderboardPlayerBanner"
                        )
                        self.LeaderboardPlayerLayout[i].addWidget(
                            self.LeaderboardPlayerBanner[i]
                        )
                        self.LeaderboardPlayerInformation[
                            i
                        ] = QtWidgets.QLabel(self.LeaderboardPlayer[i])

                        # Getting changed later
                        if (
                            self.LeaderBoardRegion.currentText() == "E5A1"
                            or "E5A2"
                            or "E5A3"
                        ):
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

                        # Layouts
                        self.LeaderboardPlayerInformation[i].setAlignment(
                            QtCore.Qt.AlignCenter
                        )
                        self.LeaderboardPlayerInformation[i].setObjectName(
                            "LeaderboardPlayerInformation"
                        )
                        self.LeaderboardPlayerLayout[i].addWidget(
                            self.LeaderboardPlayerInformation[i]
                        )

                        self.LeaderboardPlayerSpacer[
                            i
                        ] = QtWidgets.QSpacerItem(
                            40,
                            20,
                            QtWidgets.QSizePolicy.Expanding,
                            QtWidgets.QSizePolicy.Minimum,
                        )
                        self.LeaderboardPlayerLayout[i].addItem(
                            self.LeaderboardPlayerSpacer[i]
                        )
                        self.verticalLayout_8.addWidget(
                            self.LeaderboardPlayer[i]
                        )

                        # Getting players banner and add it to player_cards
                        player_card = f"https://media.valorant-api.com/playercards/{x.PlayerCardID}/smallart.png"
                        player_cards[i] = player_card

                    except AttributeError:
                        break
                else:
                    break

            self.LeaderboardSpacer = QtWidgets.QSpacerItem(
                20,
                40,
                QtWidgets.QSizePolicy.Minimum,
                QtWidgets.QSizePolicy.Expanding,
            )
            self.verticalLayout_8.addItem(self.LeaderboardSpacer)

            # Get & Set Banner
            with concurrent.futures.ThreadPoolExecutor() as executor:
                image = executor.map(requests.get, player_cards.values())
                image = tuple(image)

            for _ in player_cards:
                img = QImage()
                img.loadFromData(image[_].content)
                self.LeaderboardPlayerBanner[_].setPixmap(QPixmap(img))

            print(
                f"LEADERBOARD took --- %s seconds ---"
                % (time.time() - start_time)
            )

        except BaseException:
            print(traceback.format_exc())

    def reset_information(self):
        try:
            tier_icon = Path(__file__).parent.joinpath(
                "Images\Example\ExampleRank.png"
            )
            ExampleBanner = Path(__file__).parent.joinpath(
                "Images/Example/ExampleWideBanner.png"
            )
            BasicDummy = Path(__file__).parent.joinpath(
                "Images/Dummy/Basic.png"
            )
            self.PlayerName.setText("")
            self.PlayerName.setPlaceholderText("PLAYER NAME (16 characters)")
            self.PlayerTag.setText("")
            self.PlayerTag.setPlaceholderText("PLAYER TAG (5 characters)")
            self.PlayerBanner.setPixmap(QtGui.QPixmap(str(ExampleBanner)))
            self.PlayerIDs.setText("puu-ID | EU")
            self.Player.setText(
                f'<html><head/><body><p><span style=" font-size:29pt;">Player#Tag<p'
                f'>Account Level 0 | Iron 3 </span><img src="{tier_icon}"width="33 '
                f'"height="33"/><span style=" font-size:20pt;"> 0rr</span></p></body></html>'
            )
            self.AccuracyText.setText(
                "Headshots: 0%\n" "Bodyshots: 0%\n" "Legshots: 0%"
            )
            self.AccuracyLogo.setPixmap(QtGui.QPixmap(str(BasicDummy)))
            self.OtherStatsTexts.setText(
                '<html><head/><body><p align="center"><span style=" font-size:22pt;">Stats </span><span style=" '
                'font-size:18pt; color:#6a6a6a;">(Last 10 Matches)</span></p><p><span style=" font-size:22pt;">'
                'K/D: 0.00</span></p><p><span style=" font-size:22pt;">Average Combat Score: 0</span></p><p><span style=" font-size:22pt;">Average Damage per Round: 0</span></p><p><span style=" font-size:22pt;">Winrate: 0%</span></p></body></html> '
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
                "Day, Date, Time\n"
                "Match ID\n"
                "Region - Cluster\n"
                "Map | Gamemode | Agent: Jett\n"
                "0-0 WON\n"
                "Kills Assists Deaths | 0.00 K/D\n"
                "HS%: 0% | ACS: 0 | ADR: 0 | Total Score: 0\n"
            )

        except BaseException:
            print(traceback.format_exc())

    def modeSwitch(self):
        LightMode = Path(__file__).parent.joinpath("Images/LightMode.webp")
        DarkMode = Path(__file__).parent.joinpath("Images/DarkMode.webp")
        if self.dark_mode:
            self.dark_mode = False
            self.modeSwitcher.setIcon(QtGui.QIcon(str(LightMode)))
            QApplication.setPalette(QApplication.style().standardPalette())
        else:
            self.dark_mode = True
            self.modeSwitcher.setIcon(QtGui.QIcon(str(DarkMode)))
            dark_palette = QPalette()
            dark_palette.setColor(QPalette.Window, QColor(35, 35, 35))
            dark_palette.setColor(QPalette.WindowText, Qt.white)
            dark_palette.setColor(QPalette.Base, QColor(35, 35, 35))
            dark_palette.setColor(QPalette.AlternateBase, QColor(35, 35, 35))
            dark_palette.setColor(QPalette.ToolTipBase, QColor(35, 35, 35))
            dark_palette.setColor(QPalette.ToolTipText, Qt.white)
            dark_palette.setColor(QPalette.Text, Qt.white)
            dark_palette.setColor(QPalette.Button, QColor(35, 35, 35))
            dark_palette.setColor(QPalette.ButtonText, Qt.white)
            dark_palette.setColor(QPalette.BrightText, Qt.red)
            dark_palette.setColor(QPalette.Link, QColor(35, 35, 35))
            dark_palette.setColor(QPalette.Highlight, QColor(35, 35, 35))
            dark_palette.setColor(QPalette.HighlightedText, QColor(97, 97, 97))
            dark_palette.setColor(
                QPalette.Active, QPalette.Button, QColor(35, 35, 35)
            )
            dark_palette.setColor(
                QPalette.Disabled, QPalette.ButtonText, Qt.darkGray
            )
            dark_palette.setColor(
                QPalette.Disabled, QPalette.WindowText, Qt.darkGray
            )
            dark_palette.setColor(
                QPalette.Disabled, QPalette.Text, Qt.darkGray
            )
            dark_palette.setColor(
                QPalette.Disabled, QPalette.Light, QColor(35, 35, 35)
            )
            QApplication.setPalette(dark_palette)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ValorantTrackerByNavisGames = QtWidgets.QMainWindow()
    ui = Ui_ValorantTrackerByNavisGames()
    ui.setupUi(ValorantTrackerByNavisGames)
    QApplication.setStyle("Fusion")
    ValorantTrackerByNavisGames.show()
    sys.exit(app.exec_())
