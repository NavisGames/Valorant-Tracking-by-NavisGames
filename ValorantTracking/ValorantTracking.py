# Credits for this program go to NavisGames, selling this program or saying it's yours is not allowed! Read the
# license for more. If you want, please fork this program to share what you changed in this program ^^

import asyncio
import concurrent.futures
import time
import traceback
from pathlib import Path

import requests
import valo_api
from functions import (
    clear_layout,
    current_season,
    display_time,
    find_agent_of_player,
    find_round_player,
    find_stats_of_player,
    find_team_of_player,
    get_image,
    get_image_async,
    ranklist,
)
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QFontDatabase, QImage, QPalette, QPixmap
from PyQt5.QtWidgets import QApplication, QMessageBox


class Ui_ValorantTrackerByNavisGames(object):
    async def setupUi(self, valorant_tracking_by_navisgames):
        try:
            # Creating MainWindow
            self.dark_mode = False
            valorant_tracking_by_navisgames.setObjectName(
                "valorant_tracking_by_navisgames"
            )
            valorant_tracking_by_navisgames.setEnabled(True)
            valorant_tracking_by_navisgames.resize(1049, 890)
            valorant_tracking_by_navisgames.setMaximumSize(
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
            valorant_tracking_by_navisgames.setFont(font)
            valorant_tracking_by_navisgames.setMouseTracking(False)
            valorant_tracking_by_navisgames.setWindowTitle(
                "Valorant Tracking 2.5 By NavisGames"
            )
            icon = QtGui.QIcon()
            iconImage = Path(__file__).parent.joinpath("Images/icon.png")
            icon.addPixmap(
                QtGui.QPixmap(str(iconImage)),
                QtGui.QIcon.Normal,
                QtGui.QIcon.Off,
            )
            valorant_tracking_by_navisgames.setWindowIcon(icon)
            valorant_tracking_by_navisgames.setDockOptions(
                QtWidgets.QMainWindow.AllowTabbedDocks
                | QtWidgets.QMainWindow.AnimatedDocks
            )

            # Create CENTRAL WIDGET
            self.centralwidget = QtWidgets.QWidget(valorant_tracking_by_navisgames)
            self.centralwidget.setObjectName("centralwidget")

            # Create Layout for WIDGET
            self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.centralwidget)
            self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout_7.setSpacing(0)
            self.verticalLayout_7.setObjectName("verticalLayout_7")

            # Creating Tabs
            self.tabs = QtWidgets.QTabWidget(self.centralwidget)
            self.tabs.setEnabled(True)
            self.tabs.setFocusPolicy(QtCore.Qt.NoFocus)
            self.tabs.setLayoutDirection(QtCore.Qt.LeftToRight)
            self.tabs.setTabPosition(QtWidgets.QTabWidget.North)
            self.tabs.setTabShape(QtWidgets.QTabWidget.Rounded)
            self.tabs.setElideMode(QtCore.Qt.ElideNone)
            self.tabs.setUsesScrollButtons(False)
            self.tabs.setDocumentMode(False)
            self.tabs.setTabsClosable(False)
            self.tabs.setMovable(False)
            self.tabs.setTabBarAutoHide(False)
            self.tabs.setObjectName("Tabs")

            # Creating Home Tab
            self.home = QtWidgets.QWidget()
            self.home.setObjectName("Home")
            self.verticalLayout = QtWidgets.QVBoxLayout(self.home)

            # Creating Home Layout
            self.verticalLayout.setObjectName("verticalLayout")

            # Creating player Input Frame
            self.player_input = QtWidgets.QFrame(self.home)
            self.player_input.setEnabled(True)
            self.player_input.setLineWidth(0)
            self.player_input.setObjectName("player_input")

            # Creating player Input Layout
            self.horizontalLayout = QtWidgets.QHBoxLayout(self.player_input)
            self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout.setSpacing(5)
            self.horizontalLayout.setObjectName("horizontalLayout")

            # Light / Dark-mode switcher
            self.mode_switcher = QtWidgets.QPushButton(self.player_input)
            self.mode_switcher.setAutoFillBackground(False)
            self.mode_switcher.setText("")
            icon1 = QtGui.QIcon()
            LightMode = Path(__file__).parent.joinpath("Images/LightMode.webp")
            icon1.addPixmap(
                QtGui.QPixmap(str(LightMode)),
                QtGui.QIcon.Normal,
                QtGui.QIcon.Off,
            )
            self.mode_switcher.setIcon(icon1)
            self.mode_switcher.setIconSize(QtCore.QSize(32, 32))
            self.mode_switcher.setAutoDefault(False)
            self.mode_switcher.setDefault(False)
            self.mode_switcher.setFlat(False)
            self.mode_switcher.setObjectName("mode_switcher")
            self.horizontalLayout.addWidget(self.mode_switcher)

            # Create player Name Input
            self.player_name = QtWidgets.QLineEdit(self.player_input)
            self.player_name.setEnabled(True)
            self.player_name.setToolTipDuration(-7)
            self.player_name.setInputMask("")
            self.player_name.setText("")
            self.player_name.setMaxLength(16)
            self.player_name.setAlignment(QtCore.Qt.AlignCenter)
            self.player_name.setPlaceholderText("PLAYER NAME (16 characters)")
            self.player_name.setObjectName("player_name")
            self.horizontalLayout.addWidget(self.player_name)

            # Create player Tag Input
            self.player_tag = QtWidgets.QLineEdit(self.player_input)
            self.player_tag.setEnabled(True)
            self.player_tag.setInputMask("")
            self.player_tag.setText("")
            self.player_tag.setMaxLength(5)
            self.player_tag.setAlignment(QtCore.Qt.AlignCenter)
            self.player_tag.setPlaceholderText("PLAYER TAG (5 characters)")
            self.player_tag.setObjectName("player_tag")
            self.horizontalLayout.addWidget(self.player_tag)

            # Create player region Input
            self.player_region = QtWidgets.QComboBox(self.player_input)
            self.player_region.setEnabled(True)
            self.player_region.setLayoutDirection(QtCore.Qt.LeftToRight)
            self.player_region.setCurrentText("EU")
            self.player_region.setMaxVisibleItems(6)
            self.player_region.setMaxCount(6)
            self.player_region.setDuplicatesEnabled(False)
            self.player_region.setObjectName("player_region")
            self.player_region.addItem("")
            self.player_region.setItemText(0, "EU")
            self.player_region.addItem("")
            self.player_region.setItemText(1, "NA")
            self.player_region.addItem("")
            self.player_region.setItemText(2, "KR")
            self.player_region.addItem("")
            self.player_region.setItemText(3, "AP")
            self.player_region.addItem("")
            self.player_region.setItemText(4, "LATAM")
            self.player_region.addItem("")
            self.player_region.setItemText(5, "BR")
            self.player_region.setEditable(True)
            self.PlayerRegionEdit = self.player_region.lineEdit()
            self.PlayerRegionEdit.setAlignment(Qt.AlignCenter)
            self.PlayerRegionEdit.setReadOnly(True)
            self.horizontalLayout.addWidget(self.player_region)

            # Create player Gamemode Input
            self.player_gamemode = QtWidgets.QComboBox(self.player_input)
            self.player_gamemode.setEnabled(True)
            self.player_gamemode.setLayoutDirection(QtCore.Qt.LeftToRight)
            self.player_gamemode.setCurrentText("ALL")
            self.player_gamemode.setMaxVisibleItems(6)
            self.player_gamemode.setMaxCount(6)
            self.player_gamemode.setDuplicatesEnabled(False)
            self.player_gamemode.setObjectName("player_gamemode")
            self.player_gamemode.addItem("")
            self.player_gamemode.setItemText(0, "ALL")
            self.player_gamemode.addItem("")
            self.player_gamemode.setItemText(1, "COMPETITIVE")
            self.player_gamemode.addItem("")
            self.player_gamemode.setItemText(2, "UNRATED")
            self.player_gamemode.addItem("")
            self.player_gamemode.setItemText(3, "SPIKERUSH")
            self.player_gamemode.addItem("")
            self.player_gamemode.setItemText(4, "SWIFTPLAY")
            self.player_gamemode.addItem("")
            self.player_gamemode.setItemText(5, "DEATHMATCH")
            self.player_gamemode.setEditable(True)
            self.player_gamemode_edit = self.player_gamemode.lineEdit()
            self.player_gamemode_edit.setAlignment(Qt.AlignCenter)
            self.player_gamemode_edit.setReadOnly(True)
            self.horizontalLayout.addWidget(self.player_gamemode)

            # Create Apply, Reset Buttons
            self.dialog_button = QtWidgets.QDialogButtonBox(self.player_input)
            self.dialog_button.setEnabled(True)
            self.dialog_button.setOrientation(QtCore.Qt.Horizontal)
            self.dialog_button.setCenterButtons(False)
            self.dialog_button.setObjectName("dialog_button")

            # Create Buttons for DialogBox
            self.get_button = QtWidgets.QPushButton("EXECUTE")
            self.get_button.setDefault(True)
            self.reset_button = QtWidgets.QPushButton("RESET")
            self.reset_button.setDefault(True)
            self.dialog_button.addButton(
                self.get_button, QtWidgets.QDialogButtonBox.ActionRole
            )
            self.dialog_button.addButton(
                self.reset_button, QtWidgets.QDialogButtonBox.ActionRole
            )

            # Layers
            self.horizontalLayout.addWidget(self.dialog_button)
            self.horizontalLayout.setStretch(1, 4)
            self.horizontalLayout.setStretch(2, 3)
            self.verticalLayout.addWidget(self.player_input)

            # Create player Output Banner & Data etc. Frame
            self.player_information = QtWidgets.QFrame(self.home)
            self.player_information.setEnabled(True)
            self.player_information.setLineWidth(0)
            self.player_information.setObjectName("player_information")
            self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.player_information)
            self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
            self.horizontalLayout_2.setSpacing(15)
            self.horizontalLayout_2.setObjectName("horizontalLayout_2")

            # Create player Banner PixMap
            example_banner = Path(__file__).parent.joinpath(
                "Images/Example/ExampleWideBanner.png"
            )
            self.player_banner = QtWidgets.QLabel(self.player_information)
            self.player_banner.setEnabled(True)
            self.player_banner.setLineWidth(1)
            self.player_banner.setText("")
            self.player_banner.setPixmap(QtGui.QPixmap(str(example_banner)))
            self.player_banner.setScaledContents(True)
            self.player_banner.setAlignment(QtCore.Qt.AlignCenter)
            self.player_banner.setWordWrap(False)
            self.player_banner.setFrameShape(QtWidgets.QFrame.Box)
            self.player_banner.setLineWidth(0)
            self.player_banner.setObjectName("player_banner")
            self.horizontalLayout_2.addWidget(self.player_banner)

            # Create player Information Frame
            self.player_datas = QtWidgets.QFrame(self.player_information)
            self.player_datas.setObjectName("player_datas")
            self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.player_datas)
            self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout_5.setSpacing(0)
            self.verticalLayout_5.setObjectName("verticalLayout_5")

            # Create player puu-id + region
            self.player_ids = QtWidgets.QLabel(self.player_datas)
            font = QtGui.QFont()
            font.setPointSize(15)
            self.player_ids.setFont(font)
            self.player_ids.setText("puu-ID | EU")
            self.player_ids.setAlignment(
                QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
            )
            self.player_ids.setObjectName("player_ids")
            self.verticalLayout_5.addWidget(self.player_ids)

            # Creating player, Add HTML Text with AccountLevel, player#Tag and rank.
            tier_icon = Path(__file__).parent.joinpath("Images\Example\ExampleRank.png")
            self.player = QtWidgets.QLabel(self.player_datas)
            self.player.setEnabled(True)
            font = QtGui.QFont()
            font.setPointSize(35)
            self.player.setFont(font)
            self.player.setText(
                f'<html><head/><body><p><span style=" font-size:29pt;">player#Tag<p'
                f'>Account Level 0 | Iron 3 </span><img src="{tier_icon}"width="33 '
                f'"height="33"/><span style=" font-size:20pt;"> 0rr</span></p></body></html>'
            )
            self.player.setTextFormat(QtCore.Qt.RichText)
            self.player.setAlignment(
                QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
            )
            self.player.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
            self.player.setObjectName("player")

            # Layer Stuff. IDC
            self.verticalLayout_5.addWidget(self.player)
            self.horizontalLayout_2.addWidget(self.player_datas)
            self.verticalLayout.addWidget(self.player_information)

            # Creating Accuracy & Stats Frame
            self.general_stats = QtWidgets.QFrame(self.home)
            self.general_stats.setObjectName("general_stats")
            self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.general_stats)
            self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout_8.setObjectName("horizontalLayout_8")

            # Creating Stats
            self.StatsFrame = QtWidgets.QFrame(self.general_stats)
            self.StatsFrame.setObjectName("StatsFrame")
            self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.StatsFrame)
            self.verticalLayout_6.setContentsMargins(5, 0, 5, 0)
            self.verticalLayout_6.setSpacing(0)
            self.verticalLayout_6.setObjectName("verticalLayout_6")

            # Creating Stats Title
            self.stats_title = QtWidgets.QLabel(self.StatsFrame)
            font = QtGui.QFont()
            font.setUnderline(False)
            font.setStrikeOut(False)
            self.stats_title.setFont(font)
            self.stats_title.setText(
                '<html><head/><body><p><span style=" font-size:22pt;">General Stats </span><span style=" font-size:18pt; '
                'color:#6a6a6a;">(Last 10 Matches)</span></p></body></html> '
            )
            self.stats_title.setTextFormat(QtCore.Qt.RichText)
            self.stats_title.setAlignment(QtCore.Qt.AlignCenter)
            self.stats_title.setObjectName("stats_title")
            self.verticalLayout_6.addWidget(self.stats_title)

            # Creating Stats for Pixmap and Info's
            self.g_stats = QtWidgets.QFrame(self.StatsFrame)
            self.g_stats.setFrameShape(QtWidgets.QFrame.Box)
            self.g_stats.setFrameShadow(QtWidgets.QFrame.Plain)
            self.g_stats.setLineWidth(0)
            self.g_stats.setObjectName("g_stats")
            self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.g_stats)
            self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout_9.setSpacing(15)
            self.horizontalLayout_9.setObjectName("horizontalLayout_9")

            # Creating Accuracy Pixmap
            Basic = Path(__file__).parent.joinpath("Images/Dummy/Basic.png")
            self.accuracy_logo = QtWidgets.QLabel(self.g_stats)
            self.accuracy_logo.setLayoutDirection(QtCore.Qt.LeftToRight)
            self.accuracy_logo.setText("")
            self.accuracy_logo.setPixmap(QtGui.QPixmap(str(Basic)))
            self.accuracy_logo.setAlignment(QtCore.Qt.AlignCenter)
            self.accuracy_logo.setObjectName("accuracy_logo")
            self.horizontalLayout_9.addWidget(self.accuracy_logo)

            # Creating Accuracy Texts for HS Rate etc.
            self.accuarcy_text = QtWidgets.QLabel(self.g_stats)
            self.accuarcy_text.setLayoutDirection(QtCore.Qt.LeftToRight)
            self.accuarcy_text.setText(
                "Headshots: 0%\n" "Bodyshots: 0%\n" "Legshots: 0%"
            )
            self.accuarcy_text.setAlignment(QtCore.Qt.AlignCenter)
            self.accuarcy_text.setObjectName("accuarcy_text")
            self.horizontalLayout_9.addWidget(self.accuarcy_text)

            # Creating HTML Code with K/D, Win rate and the Title in it
            self.stats_text = QtWidgets.QLabel(self.g_stats)
            self.stats_text.setText(
                "K/D: 0.00\n"
                "Average Combat Score: 0\n"
                "Average Damage per Round: 0\n"
                "Winrate: 0%"
            )
            self.stats_text.setAlignment(QtCore.Qt.AlignCenter)
            self.stats_text.setObjectName("stats_text")
            self.horizontalLayout_9.addWidget(self.stats_text)
            self.verticalLayout_6.addWidget(self.g_stats)

            # Spacer Item
            self.horizontalLayout_8.addWidget(self.StatsFrame)

            # Creating Stats Frame
            self.stats = QtWidgets.QFrame(self.home)
            self.stats.setObjectName("Stats")
            self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.stats)
            self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout_6.setObjectName("horizontalLayout_6")

            # Creating CompetitiveStats Frame for Stats
            self.comp_information = QtWidgets.QFrame(self.stats)
            self.comp_information.setEnabled(True)
            self.comp_information.setObjectName("comp_information")
            self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.comp_information)
            self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout_2.setObjectName("verticalLayout_2")

            # Creating Competitive Title
            self.comp_title = QtWidgets.QLabel(self.comp_information)
            self.comp_title.setEnabled(True)
            self.comp_title.setText("COMPETITIVE STATS")
            self.comp_title.setAlignment(QtCore.Qt.AlignCenter)
            self.comp_title.setObjectName("comp_title")
            self.verticalLayout_2.addWidget(self.comp_title)

            # Creating ScrollArea for the Field of Competitive
            self.comp_scroll_area = QtWidgets.QScrollArea(self.comp_information)
            self.comp_scroll_area.setEnabled(True)
            self.comp_scroll_area.setVerticalScrollBarPolicy(
                QtCore.Qt.ScrollBarAsNeeded
            )
            self.comp_scroll_area.setHorizontalScrollBarPolicy(
                QtCore.Qt.ScrollBarAlwaysOff
            )
            self.comp_scroll_area.setWidgetResizable(True)
            self.comp_scroll_area.setAlignment(QtCore.Qt.AlignCenter)
            self.comp_scroll_area.setObjectName("comp_scroll_area")
            self.comp_scroll_area.setFrameShape(QtWidgets.QFrame.Box)
            self.comp_scroll_area.setFrameShadow(QtWidgets.QFrame.Plain)
            self.comp_scroll_area.setLineWidth(0)
            self.CompScrollLayout = QtWidgets.QWidget()
            self.CompScrollLayout.setGeometry(QtCore.QRect(0, 0, 519, 355))
            self.CompScrollLayout.setObjectName("CompScrollLayout")
            self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.CompScrollLayout)
            self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout_3.setObjectName("horizontalLayout_3")

            # Creating Competitive history
            self.comp_history = QtWidgets.QLabel(self.CompScrollLayout)
            self.comp_history.setEnabled(True)
            font = QtGui.QFont()
            font.setPointSize(14)
            self.comp_history.setFont(font)
            self.comp_history.setLineWidth(1)
            self.comp_history.setWordWrap(True)
            self.comp_history.setText(
                "Matchmaking Ratio \n"
                "Competitive Wins \n"
                "Competitive Games played \n"
                "Previous Ranks \n"
                "rank history\n"
            )
            self.comp_history.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
            self.comp_history.setWordWrap(True)
            self.comp_history.setObjectName("comp_history")
            self.horizontalLayout_3.addWidget(self.comp_history)
            self.comp_scroll_area.setWidget(self.CompScrollLayout)
            self.verticalLayout_2.addWidget(self.comp_scroll_area)
            self.horizontalLayout_6.addWidget(self.comp_information)

            # Creating Match history Frame for Stats
            self.match_history = QtWidgets.QFrame(self.stats)
            self.match_history.setEnabled(True)
            self.match_history.setFrameShape(QtWidgets.QFrame.Box)
            self.match_history.setFrameShadow(QtWidgets.QFrame.Plain)
            self.match_history.setLineWidth(0)
            self.match_history.setObjectName("match_history")
            self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.match_history)
            self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout_4.setObjectName("verticalLayout_4")

            # Creating history Title
            self.history_title = QtWidgets.QLabel(self.match_history)
            self.history_title.setEnabled(True)
            self.history_title.setText("MATCH HISTORY")
            self.history_title.setAlignment(QtCore.Qt.AlignCenter)
            self.history_title.setObjectName("history_title")
            self.verticalLayout_4.addWidget(self.history_title)

            # Creating ScrollArea for the Field of Match history
            self.history_scroll_area = QtWidgets.QScrollArea(self.match_history)
            self.history_scroll_area.setEnabled(True)
            self.history_scroll_area.setLineWidth(1)
            self.history_scroll_area.setHorizontalScrollBarPolicy(
                QtCore.Qt.ScrollBarAlwaysOff
            )
            self.history_scroll_area.setWidgetResizable(True)
            self.history_scroll_area.setObjectName("history_scroll_area")
            self.history_scroll_layout = QtWidgets.QWidget()
            self.history_scroll_layout.setGeometry(QtCore.QRect(0, 0, 519, 355))
            self.history_scroll_layout.setObjectName("history_scroll_layout")
            self.history_scroll_area.setFrameShape(QtWidgets.QFrame.Box)
            self.history_scroll_area.setFrameShadow(QtWidgets.QFrame.Plain)
            self.history_scroll_area.setLineWidth(0)
            self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.history_scroll_layout)
            self.horizontalLayout_4.setObjectName("horizontalLayout_4")

            # Creating match_history Text.
            self.history = QtWidgets.QLabel(self.history_scroll_layout)
            self.history.setEnabled(True)
            font = QtGui.QFont()
            font.setPointSize(14)
            self.history.setFont(font)
            self.history.setWordWrap(True)
            self.history.setText(
                "Day, Date, Time\n"
                "Match ID\n"
                "region - Cluster\n"
                "Map | Gamemode | Agent: Jett\n"
                "0-0 WON\n"
                "Kills Assists Deaths | 0.00 K/D\n"
                "HS%: 0% | ACS: 0 | ADR: 0 | Total Score: 0\n\n"
            )
            self.history.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
            self.history.setObjectName("history")
            self.horizontalLayout_4.addWidget(self.history)
            self.history_scroll_area.setWidget(self.history_scroll_layout)
            self.verticalLayout_4.addWidget(self.history_scroll_area)
            self.horizontalLayout_6.addWidget(self.match_history)

            # Adding Widgets to HOME
            self.verticalLayout.addWidget(self.stats)
            self.verticalLayout.addWidget(self.general_stats)

            # Adding home_error to find Errors better
            self.home_error = QtWidgets.QLabel(self.home)
            font = QtGui.QFont()
            font.setPointSize(12)
            self.home_error.setFont(font)
            self.home_error.setText("")
            self.home_error.setAlignment(
                QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
            )
            self.home_error.setWordWrap(True)
            self.home_error.setObjectName("home_error")
            self.verticalLayout.addWidget(self.home_error)

            # Add HOME Tab to Tabs
            self.tabs.addTab(self.home, "HOME")

            # Creating leaderboard Tab & Layout
            self.leaderboard = QtWidgets.QWidget()
            self.leaderboard.setObjectName("leaderboard")
            self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.leaderboard)
            self.verticalLayout_3.setContentsMargins(0, -1, 0, 0)
            self.verticalLayout_3.setObjectName("verticalLayout_3")

            # Creating leaderboard Input Frame
            self.LeaderBoardInput = QtWidgets.QFrame(self.leaderboard)
            self.LeaderBoardInput.setObjectName("LeaderBoardInput")
            self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.LeaderBoardInput)
            self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout_7.setObjectName("horizontalLayout_7")

            # Creating Combo Box for all Acts
            self.act = QtWidgets.QComboBox(self.LeaderBoardInput)
            self.act.setCurrentText("E6A3")
            self.act.setObjectName("act")
            self.act.addItem("")
            self.act.setItemText(0, "E6A3")
            self.act.addItem("")
            self.act.setItemText(1, "E6A2")
            self.act.addItem("")
            self.act.setItemText(2, "E6A1")
            self.act.addItem("")
            self.act.setItemText(3, "E5A3")
            self.act.addItem("")
            self.act.setItemText(4, "E5A2")
            self.act.addItem("")
            self.act.setItemText(5, "E5A1")
            self.act.addItem("")
            self.act.setItemText(6, "E4A3")
            self.act.addItem("")
            self.act.setItemText(7, "E4A2")
            self.act.addItem("")
            self.act.setItemText(8, "E4A1")
            self.act.addItem("")
            self.act.setItemText(9, "E3A3")
            self.act.addItem("")
            self.act.setItemText(10, "E3A2")
            self.act.addItem("")
            self.act.setItemText(11, "E3A1")
            self.act.addItem("")
            self.act.setItemText(12, "E2A3")
            self.act.addItem("")
            self.act.setItemText(13, "E2A2")
            self.act.addItem("")
            self.act.setItemText(14, "E2A1")
            self.act.setEditable(True)
            self.horizontalLayout_7.addWidget(self.act)
            self.act_edit = self.act.lineEdit()
            self.act_edit.setAlignment(Qt.AlignCenter)
            self.act_edit.setReadOnly(True)

            # Creating leaderboard Regions
            self.leaderboard_region = QtWidgets.QComboBox(self.LeaderBoardInput)
            self.leaderboard_region.setEnabled(True)
            self.leaderboard_region.setLayoutDirection(QtCore.Qt.LeftToRight)
            self.leaderboard_region.setCurrentText("EU")
            self.leaderboard_region.setMaxVisibleItems(6)
            self.leaderboard_region.setMaxCount(6)
            self.leaderboard_region.setDuplicatesEnabled(False)
            self.leaderboard_region.setObjectName("leaderboard_region")
            self.leaderboard_region.addItem("")
            self.leaderboard_region.setItemText(0, "EU")
            self.leaderboard_region.addItem("")
            self.leaderboard_region.setItemText(1, "NA")
            self.leaderboard_region.addItem("")
            self.leaderboard_region.setItemText(2, "KR")
            self.leaderboard_region.addItem("")
            self.leaderboard_region.setItemText(3, "AP")
            self.leaderboard_region.addItem("")
            self.leaderboard_region.setItemText(4, "LATAM")
            self.leaderboard_region.addItem("")
            self.leaderboard_region.setItemText(5, "BR")
            self.leaderboard_region.setEditable(True)
            self.horizontalLayout_7.addWidget(self.leaderboard_region)
            self.leaderboard_edit = self.leaderboard_region.lineEdit()
            self.leaderboard_edit.setAlignment(Qt.AlignCenter)
            self.leaderboard_edit.setReadOnly(True)

            # Create player count Box
            self.player_count = QtWidgets.QSpinBox(self.LeaderBoardInput)
            self.player_count.setWrapping(False)
            self.player_count.setFrame(True)
            self.player_count.setAlignment(QtCore.Qt.AlignCenter)
            self.player_count.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
            self.player_count.setSpecialValueText("")
            self.player_count.setProperty("showGroupSeparator", False)
            self.player_count.setPrefix("Players: ")
            self.player_count.setMinimum(1)
            self.player_count.setMaximum(15000)
            self.player_count.setObjectName("spinBox")
            self.horizontalLayout_7.addWidget(self.player_count)

            # Create Reload Button
            self.reload_button = QtWidgets.QPushButton(self.LeaderBoardInput)
            self.reload_button.setText("Reload")
            self.reload_button.setDefault(False)
            self.reload_button.setFlat(False)
            self.reload_button.setObjectName("Reload")
            self.horizontalLayout_7.addWidget(self.reload_button)
            self.verticalLayout_3.addWidget(self.LeaderBoardInput)

            # Create Players Frame & ScrollArea & Layout
            self.players = QtWidgets.QVBoxLayout()
            self.players.setContentsMargins(0, 0, 0, 0)
            self.players.setObjectName("Players")
            self.player_scroll_area = QtWidgets.QScrollArea(self.leaderboard)
            self.player_scroll_area.setFrameShape(QtWidgets.QFrame.Box)
            self.player_scroll_area.setFrameShadow(QtWidgets.QFrame.Plain)
            self.player_scroll_area.setLineWidth(0)
            self.player_scroll_area.setHorizontalScrollBarPolicy(
                QtCore.Qt.ScrollBarAlwaysOff
            )
            self.player_scroll_area.setSizeAdjustPolicy(
                QtWidgets.QAbstractScrollArea.AdjustIgnored
            )
            self.player_scroll_area.setWidgetResizable(True)
            self.player_scroll_area.setAlignment(QtCore.Qt.AlignCenter)
            self.player_scroll_area.setObjectName("player_scroll_area")
            self.player_scroll_area_layout = QtWidgets.QWidget()
            self.player_scroll_area_layout.setGeometry(QtCore.QRect(0, 0, 486, 145))
            self.player_scroll_area_layout.setObjectName("player_scroll_area_layout")

            self.player_scroll_area.setWidget(self.player_scroll_area_layout)
            self.players.addWidget(self.player_scroll_area)
            self.verticalLayout_3.addLayout(self.players)
            self.tabs.addTab(self.leaderboard, "LEADERBOARD")

            # Create Leader player Stuff for function
            self.leaderboard_player_banner = dict()
            self.leaderboard_player_information = dict()
            self.leaderboard_player = dict()
            self.leaderboard_player_layout = dict()
            self.leaderboard_player_spacer = dict()

            self.verticalLayout_8 = QtWidgets.QVBoxLayout(
                self.player_scroll_area_layout
            )
            self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout_8.setSpacing(5)
            self.verticalLayout_8.setObjectName("verticalLayout_8")

            # Create Dicts with Bundles and use Valorant API to get all current bundles
            current_Bundle = valo_api.get_store_featured_v2()
            self.bundle = dict()

            for i, bundles in enumerate(current_Bundle):
                bundleUuid = current_Bundle[i].bundle_uuid

                # Getting Bundle Banner as PixMap
                bundleJson = requests.get(
                    url=f"https://valorant-api.com/v1/bundles/{bundleUuid}"
                ).json()
                img = await get_image_async(bundleJson["data"]["displayIcon2"])

                # Creating Bundle
                self.bundle[i] = QtWidgets.QWidget()
                self.bundle[i].setObjectName("Bundle")
                self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.bundle[i])
                self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout_10.setSpacing(0)
                self.verticalLayout_10.setObjectName("verticalLayout_10")

                # Creating Bundle MainFrame
                self.bundle_main = QtWidgets.QFrame(self.bundle[i])
                self.bundle_main.setObjectName("BundleMain")
                self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.bundle_main)
                self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout_11.setSpacing(0)
                self.verticalLayout_11.setObjectName("verticalLayout_11")

                # Creating Bundle Banner
                self.bundle_banner = QtWidgets.QLabel(self.bundle_main)
                self.bundle_banner.setMinimumSize(QtCore.QSize(1, 1))
                self.bundle_banner.setMaximumSize(QtCore.QSize(234234, 234234))
                font = QtGui.QFont()
                font.setKerning(True)
                self.bundle_banner.setFont(font)
                self.bundle_banner.setAutoFillBackground(False)
                self.bundle_banner.setText("")
                self.bundle_banner.setPixmap(QtGui.QPixmap(img))
                self.bundle_banner.setScaledContents(True)
                self.bundle_banner.setAlignment(QtCore.Qt.AlignCenter)
                self.bundle_banner.setWordWrap(False)
                self.bundle_banner.setObjectName("BundleBanner")
                self.verticalLayout_11.addWidget(self.bundle_banner)

                # Create Bundle prices
                self.bundle_prices = QtWidgets.QLabel(self.bundle_main)
                self.bundle_prices.setText(
                    "BUNDLE PRICE: 0 VP\n"
                    "Weapon: 0 VP | 0 VP -> Whole Bundle\n"
                    "Weapon: 0 VP | 0 VP -> Whole Bundle\n"
                    "Weapon: 0 VP | 0 VP -> Whole Bundle\n"
                    "2x Buddy: 0 VP | 0 VP -> Whole Bundle\n"
                    "player card: 0 VP | 0 VP -> Whole Bundle\n"
                    "Spray: 0 VP | 0 VP -> Whole Bundle"
                )
                self.bundle_prices.setAlignment(QtCore.Qt.AlignCenter)
                self.bundle_prices.setObjectName("BundlePrices")
                self.verticalLayout_11.addWidget(self.bundle_prices)

                # Create Seconds Remaining in Shop
                self.bundle_last = QtWidgets.QLabel(self.bundle_main)
                font = QtGui.QFont()
                font.setPointSize(15)
                self.bundle_last.setFont(font)
                self.bundle_last.setText("Bundle in Shop until: Weeks : Days : Hours")
                self.bundle_last.setAlignment(QtCore.Qt.AlignCenter)
                self.bundle_last.setObjectName("BundleLast")
                self.verticalLayout_11.addWidget(self.bundle_last)
                self.verticalLayout_10.addWidget(self.bundle_main)

                # Get every item and set a string (before a list!)
                prices = [
                    f"Bundle Price - {current_Bundle[i].bundle_price} Valorant Points\n"
                ]
                for item in current_Bundle[i].items:
                    if item.amount > 1:
                        prices.append(
                            f"{item.amount}x {item.name} - {item.base_price} VP | {item.discounted_price} VP for whole Bundle\n"
                        )
                    else:
                        prices.append(
                            f"{item.name} - {item.base_price} VP | {item.discounted_price} VP for whole Bundle\n"
                        )
                prices = "".join(prices)

                # Set Texts
                self.bundle_prices.setText(prices)
                self.bundle_last.setText(
                    f"Bundle remaining in Shop: {display_time(bundles.seconds_remaining, 3)}"
                )

                # Add Bundles
                self.tabs.addTab(
                    self.bundle[i],
                    f"{bundleJson['data']['displayName'].upper()}",
                )

            # Create match_tracker Widget
            self.match_tracker = QtWidgets.QWidget()
            self.match_tracker.setObjectName("match_tracker")

            # Create Layout
            self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.match_tracker)
            self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
            self.verticalLayout_9.setObjectName("verticalLayout_9")

            # Create MatchInputLayout
            self.match_inputs = QtWidgets.QHBoxLayout()
            self.match_inputs.setObjectName("match_inputs")

            # Create MatchID Input
            spacerItem2 = QtWidgets.QSpacerItem(
                40,
                20,
                QtWidgets.QSizePolicy.Expanding,
                QtWidgets.QSizePolicy.Minimum,
            )
            self.match_inputs.addItem(spacerItem2)
            self.match_id_input = QtWidgets.QLineEdit(self.match_tracker)
            self.match_id_input.setInputMask("")
            self.match_id_input.setText("")
            self.match_id_input.setMaxLength(36)
            self.match_id_input.setAlignment(QtCore.Qt.AlignCenter)
            self.match_id_input.setObjectName("match_id_input")
            self.match_id_input.setPlaceholderText("ENTER MATCH ID (36 characters)")
            self.match_inputs.addWidget(self.match_id_input)

            # Create Execute Button
            self.execute_button = QtWidgets.QPushButton(self.match_tracker)
            self.execute_button.setText("EXECUTE")
            self.execute_button.setObjectName("execute_button")
            self.match_inputs.addWidget(self.execute_button)

            # Spacer
            spacerItem3 = QtWidgets.QSpacerItem(
                40,
                20,
                QtWidgets.QSizePolicy.Expanding,
                QtWidgets.QSizePolicy.Minimum,
            )
            self.match_inputs.addItem(spacerItem3)
            self.verticalLayout_9.addLayout(self.match_inputs)

            # Create Match Informations
            self.MatchInformations = QtWidgets.QLabel(self.match_tracker)
            font = QtGui.QFont()
            font.setPointSize(18)
            self.MatchInformations.setFont(font)
            self.MatchInformations.setText(
                "Match ID\n"
                "Date - Match Duration\n"
                "region - Cluster\n"
                "Gamemode - Map"
            )
            self.MatchInformations.setTextFormat(QtCore.Qt.PlainText)
            self.MatchInformations.setAlignment(QtCore.Qt.AlignCenter)
            self.MatchInformations.setObjectName("MatchInformations")
            self.verticalLayout_9.addWidget(self.MatchInformations)

            # Create Match Results
            self.match_result = QtWidgets.QLabel(self.match_tracker)
            self.match_result.setText(
                '<html><head/><body><p align="center"><span style=" font-size:18pt; color:#00ba82;">TEAM A</span><span style=" font-size:18pt; color:#00ffb3;">⠀</span><span style=" font-size:18pt; color:#000000;">:</span><span style=" font-size:18pt; color:#00ffb3;">⠀</span><span style=" font-size:18pt; color:#ff0000;">TEAM B</span></p><p align="center"><span style=" font-size:18pt; color:#00ba82;">13</span><span style=" font-size:18pt; color:#00ffb3;">⠀</span><span style=" font-size:18pt; color:#000000;">:</span><span style=" font-size:18pt; color:#00ffb3;">⠀</span><span style=" font-size:18pt; color:#ff0000;">5</span></p></body></html>'
            )
            self.match_result.setTextFormat(QtCore.Qt.RichText)
            self.match_result.setAlignment(QtCore.Qt.AlignCenter)
            self.match_result.setObjectName("match_result")
            self.verticalLayout_9.addWidget(self.match_result)

            # Add Widget & Layout stuff
            spacerItem2 = QtWidgets.QSpacerItem(
                20,
                40,
                QtWidgets.QSizePolicy.Minimum,
                QtWidgets.QSizePolicy.Expanding,
            )
            self.verticalLayout_9.addItem(spacerItem2)
            spacerItem4 = QtWidgets.QSpacerItem(
                20,
                40,
                QtWidgets.QSizePolicy.Minimum,
                QtWidgets.QSizePolicy.Expanding,
            )
            self.verticalLayout_9.addItem(spacerItem4)

            # Create Match Error
            self.match_error = QtWidgets.QLabel(self.match_tracker)
            font = QtGui.QFont()
            font.setPointSize(12)
            self.match_error.setFont(font)
            self.match_error.setText("")
            self.match_error.setWordWrap(True)
            self.match_error.setObjectName("match_error")
            self.verticalLayout_9.addWidget(self.match_error)

            # Index, Layout, adding Match Tracker
            self.tabs.addTab(self.match_tracker, "MATCH")
            self.verticalLayout_7.addWidget(self.tabs)
            valorant_tracking_by_navisgames.setCentralWidget(self.centralwidget)
            self.tabs.setCurrentIndex(0)
            self.player_region.setCurrentIndex(0)
            self.leaderboard_region.setCurrentIndex(0)

            # Functions
            self.get_button.clicked.connect(self.get_information)
            self.execute_button.clicked.connect(self.get_match_information)
            self.reset_button.clicked.connect(self.reset_information)
            self.reload_button.clicked.connect(self.get_leaderboard)
            self.mode_switcher.clicked.connect(self.modeSwitch)
            QtCore.QMetaObject.connectSlotsByName(valorant_tracking_by_navisgames)

        except BaseException as error:
            print(traceback.format_exc())
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText(f"{format(error)}")
            msg_box.setWindowTitle("an error occurred")
            msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg_box.exec()

    def get_information(self):
        try:
            # API functions
            Details = valo_api.get_account_details_by_name(
                version="v1",
                name=self.player_name.text(),
                tag=self.player_tag.text(),
            )

            # Get rank, rr and mmr
            RankDetails = valo_api.get_mmr_details_by_name_v2(
                region=self.player_region.currentText(),
                name=self.player_name.text(),
                tag=self.player_tag.text(),
            )

            # Get Match history
            if self.player_gamemode.currentText() != "ALL":
                HistoryDetails = valo_api.get_match_history_by_name(
                    version="v3",
                    region=self.player_region.currentText(),
                    name=self.player_name.text(),
                    tag=self.player_tag.text(),
                    size=10,
                    game_mode=self.player_gamemode.currentText().lower(),
                )
            else:
                HistoryDetails = valo_api.get_match_history_by_name(
                    version="v3",
                    region=self.player_region.currentText(),
                    name=self.player_name.text(),
                    tag=self.player_tag.text(),
                    size=10,
                )

            # Get Recent rank Changes
            MMRDetails = valo_api.get_mmr_history_by_name(
                version="v1",
                region=self.player_region.currentText(),
                name=self.player_name.text(),
                tag=self.player_tag.text(),
            )

            # DETAILS ~ puuid, region, Account Level and the PlayerCard
            # RANK DETAILS ~ rank, rr, mmr
            puuid = Details.puuid
            region = Details.region
            account_level = Details.account_level
            card = str(Details.card.wide)
            rank = RankDetails.current_data.currenttierpatched
            peak_rank = RankDetails.highest_rank.patched_tier
            rr = RankDetails.current_data.ranking_in_tier
            mmr = RankDetails.current_data.elo

            # Sets PUU-ID and region
            self.player_ids.setText(f"{puuid} | {region}")

            # Creates List with mmr, Comp Wins, Comp Games
            previous_ranks = [
                f"Rank: {rank} {rr}rr\n"
                f"Peak Rank: {peak_rank}\n"
                f"Matchmaking Ratio: {mmr}\n\n"
            ]

            # Gets Last rank Adds last Ranks with mmr, Wins, Games to the List | if player didn't play in this act or an
            # API Problem is there, then continue
            act_ranks = RankDetails.by_season
            last_rank = dict(reversed(act_ranks.items()))
            for x in last_rank:
                try:
                    if (
                        last_rank[x].final_rank_patched not in (None, "Unrated")
                        and x != current_season.lower()
                    ):
                        previous_ranks.append(
                            f"{x.upper()}: {last_rank[x].final_rank_patched} | {last_rank[x].wins} Wins - {last_rank[x].number_of_games}Game(s) played\n"
                        )
                    else:
                        continue
                except BaseException as error:
                    print(traceback.format_exc())
                    self.home_error.setText(f"{format(error)}")

            # If there is a rank, add a rank history
            # For every last match in the detail get +rr or -rr and rank / rr
            if rank is not None:
                previous_ranks.append("\n")
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
            previous_ranks = "".join(previous_ranks)
            self.comp_history.setText(previous_ranks)

            # getting an QImage for the player card.
            with concurrent.futures.ThreadPoolExecutor() as executor:
                img = executor.submit(get_image, card)
                img = img.result()
            self.player_banner.setPixmap(QPixmap(img))

            # Get Match history as a List, and gets every current matches
            match_history = []

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

                # Get Stats of player with get_stats function
                get_stats = find_stats_of_player(Details.name, players.all_players)

                # Get Agent of player
                get_agent = find_agent_of_player(Details.name, players.all_players)

                # Some Variables
                kills = get_stats.kills if hasattr(get_stats, "kills") else 0
                deaths = get_stats.deaths if hasattr(get_stats, "deaths") else 0
                assists = get_stats.assists if hasattr(get_stats, "assists") else 0
                total_score = get_stats.score if hasattr(get_stats, "score") else 0
                combat_score = total_score / rounds_played
                damage = 0

                for rounds in x.rounds:
                    player = find_round_player(
                        f"{Details.name}#{Details.tag}", rounds.player_stats
                    )
                    damage += player.damage if hasattr(player, "damage") else 0
                    total_rounds += 1

                # Add Aim rates
                headshots += (
                    get_stats.headshots if hasattr(get_stats, "headshots") else 0
                )
                bodyshots += (
                    get_stats.bodyshots if hasattr(get_stats, "bodyshots") else 0
                )
                legshots += get_stats.legshots if hasattr(get_stats, "legshots") else 0

                # Some Variables
                total_kills += kills
                total_deaths += deaths
                total_combat_score += combat_score
                total_damage += damage

                # Calculate HS% in the Match
                try:
                    headshot_rate = round(
                        get_stats.headshots
                        if hasattr(get_stats, "headshots")
                        else 0
                        / (
                            get_stats.headshots
                            if hasattr(get_stats, "headshots")
                            else 0 + get_stats.bodyshots
                            if hasattr(get_stats, "bodyshots")
                            else 0 + get_stats.legshots
                            if hasattr(get_stats, "legshots")
                            else 0
                        )
                        * 100
                    )
                except ZeroDivisionError:
                    headshot_rate = None

                # Rounds to 0.00 <- 2 Decimals
                try:
                    kd = format(kills / deaths, ".2f")
                except ZeroDivisionError:
                    kd = format(kills, ".2f")

                # Get Team and Team information of player with get_team function
                get_team = find_team_of_player(Details.name, players.all_players)
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

                # Get Match ID, Map, region, Cluster and Mode with Match Metadata
                match_id = match.matchid
                match_map = match.map
                region = match.region.upper()
                cluster = match.cluster
                mode = match.mode

                # If Deathmatch, remove Rounds, Won/Lost and Combat Score
                if mode == "Deathmatch":
                    match_history.append(
                        f"{match.game_start_patched}\n"
                        f"{match_id}\n"
                        f"{region} - {cluster}\n"
                        f"{match_map} | {mode} | Agent: {get_agent}\n"
                        f"{kills} Kills {assists} Assists {deaths} Deaths | {kd} K/D\n"
                        f"Total Score: {total_score}\n\n"
                    )
                else:
                    match_history.append(
                        f"{match.game_start_patched}\n"
                        f"{match_id}\n"
                        f"{region} - {cluster}\n"
                        f"{match_map} | {mode} | Agent: {get_agent}\n"
                        f"{rounds_won}-{rounds_lost} {won}\n"
                        f"{kills} Kills {assists} Assists {deaths} Deaths | {kd} K/D\n"
                        f"HS%: {headshot_rate}% | CS: {round(combat_score)} | ADR: {round(damage / rounds_played)} | Total Score: {total_score}\n\n"
                    )

            # Set Match to Text
            match_history = "".join(match_history)

            # Dummys
            headshot_dummy = Path(__file__).parent.joinpath("Images/Dummy/Headshot.png")
            bodyshot_dummy = Path(__file__).parent.joinpath("Images/Dummy/Bodyshot.png")
            legshot_dummy = Path(__file__).parent.joinpath("Images/Dummy/Legshot.png")
            basic_dummy = Path(__file__).parent.joinpath("Images/Dummy/Basic.png")

            # Set Rates with Math
            if self.player_gamemode.currentText() != "DEATHMATCH":
                try:
                    headshot_rate = round(
                        headshots / (headshots + bodyshots + legshots) * 100
                    )
                    bodyshot_rate = round(
                        bodyshots / (headshots + bodyshots + legshots) * 100
                    )
                    legshot_rate = round(
                        legshots / (headshots + bodyshots + legshots) * 100
                    )
                except ZeroDivisionError:
                    headshot_rate = 0
                    bodyshot_rate = 0
                    legshot_rate = 0

                # Set Dummy Prior

                if headshot_rate > bodyshot_rate and headshot_rate > legshot_rate:
                    self.accuracy_logo.setPixmap(QtGui.QPixmap(str(headshot_dummy)))
                elif bodyshot_rate > headshot_rate and bodyshot_rate > legshot_rate:
                    self.accuracy_logo.setPixmap(QtGui.QPixmap(str(bodyshot_dummy)))
                elif legshot_rate > headshot_rate and legshot_rate > bodyshot_rate:
                    self.accuracy_logo.setPixmap(QtGui.QPixmap(str(legshot_dummy)))
                else:
                    self.accuracy_logo.setPixmap(QtGui.QPixmap(str(basic_dummy)))
            else:
                headshot_rate = "-"
                bodyshot_rate = "-"
                legshot_rate = "-"
                self.accuracy_logo.setPixmap(QtGui.QPixmap(str(basic_dummy)))

            # Gets the current rank AS TIER INDEX (int) and compares it with the index data, to get the RANK IMAGE
            tier_index = RankDetails.current_data.currenttier
            data = requests.get("https://valorant-api.com/v1/competitivetiers").json()
            tiers = data["data"][-1]["tiers"]
            tier = None

            # If it has any rank, get it ELSE say Unranked
            if rank is not None:
                for tier in tiers:
                    if tier["tier"] == tier_index:
                        tier = tier["tierName"]
                        break
            else:
                tier = "UNRANKED"

            # Gets the PNG for the HTML Rich Text
            tier_icon = Path(__file__).parent.joinpath(f"Images/Ranks/{tier}.png")

            # Add Texts
            self.history.setText(match_history)  # <- List which got made to a string
            self.accuarcy_text.setText(
                f"Headshots: {headshot_rate}%\n"
                f"Bodyshots: {bodyshot_rate}%\n"
                f"Legshots: {legshot_rate}%"
            )
            try:
                self.stats_text.setText(
                    f"K/D: {format(total_kills / total_deaths, '.2f')}\n"
                    f"Average Combat Score: {round(total_combat_score / total_matches)}\n"
                    f"Average Damage per Round: {round(total_damage / total_rounds)}\n"
                    f"Winrate: {round(total_wins / total_matches * 100)}%"
                )
            except ZeroDivisionError:
                self.stats_text.setText("")
            self.player.setText(
                f'<html><head/><body><p><span style=" font-size:29pt;">{Details.name}#{Details.tag}<p'
                f'>Account Level {account_level} | {rank} </span><img src="{tier_icon}"width="33 '
                f'"height="33"/><span style=" font-size:20pt;"> {rr}rr</span></p></body></html>'
            )
            self.home_error.setText(f"")
        except BaseException as error:
            print(traceback.format_exc())
            self.home_error.setText(f"{format(error)}")

    def get_leaderboard(self):
        start_time = time.time()
        try:
            # Get Values
            season = self.act.currentText().lower()
            region = self.leaderboard_region.currentText()
            player_limit = int(self.player_count.value())
            player_cards = {}

            try:
                clear_layout(self.verticalLayout_8)
            except AttributeError:
                pass

            # Get API
            leaderboard = valo_api.get_leaderboard(
                version="v2", region=region, season_id=season
            )

            # Set all new leaderboard stuff
            for i, x in enumerate(leaderboard.players):
                if i < player_limit:
                    try:
                        # Setting player
                        self.leaderboard_player[i] = QtWidgets.QFrame(
                            self.player_scroll_area_layout
                        )
                        self.leaderboard_player[i].setEnabled(True)
                        self.leaderboard_player[i].setObjectName("PlayerTemplate")
                        self.leaderboard_player_layout[i] = QtWidgets.QHBoxLayout(
                            self.leaderboard_player[i]
                        )
                        self.leaderboard_player_layout[i].setContentsMargins(0, 0, 0, 0)
                        self.leaderboard_player_layout[i].setObjectName(
                            "PlayerLayoutTemplate"
                        )

                        # Setting Banner
                        example_banner = Path(__file__).parent.joinpath(
                            "Images/Example/example_banner.png"
                        )
                        self.leaderboard_player_banner[i] = QtWidgets.QLabel(
                            self.leaderboard_player[i]
                        )
                        self.leaderboard_player_banner[i].setText("")
                        self.leaderboard_player_banner[i].setPixmap(
                            QtGui.QPixmap(str(example_banner))
                        )
                        self.leaderboard_player_banner[i].setScaledContents(False)
                        self.leaderboard_player_banner[i].setObjectName(
                            "leaderboard_player_banner"
                        )
                        self.leaderboard_player_layout[i].addWidget(
                            self.leaderboard_player_banner[i]
                        )
                        self.leaderboard_player_information[i] = QtWidgets.QLabel(
                            self.leaderboard_player[i]
                        )

                        # Get LeaderboardPlayers rank, watching out if Episode is under 5
                        tier = x.competitiveTier
                        if int(self.act.currentText()[1]) < 5 and tier >= 21:
                            tier += 3
                        rank = ranklist[tier]

                        # If anonymous else stuff
                        if x.IsAnonymized:
                            self.leaderboard_player_information[i].setText(
                                f"#{x.leaderboardRank} | Anonymous player | {rank} {x.rankedRating}rr | {x.numberOfWins} Wins"
                            )
                        else:
                            self.leaderboard_player_information[i].setText(
                                f"#{x.leaderboardRank} | {x.gameName}#{x.tagLine} | {rank} {x.rankedRating}rr | {x.numberOfWins} Wins | {x.puuid}"
                            )

                        # Layouts
                        self.leaderboard_player_information[i].setAlignment(
                            QtCore.Qt.AlignCenter
                        )
                        self.leaderboard_player_information[i].setObjectName(
                            "leaderboard_player_information"
                        )
                        self.leaderboard_player_layout[i].addWidget(
                            self.leaderboard_player_information[i]
                        )

                        self.leaderboard_player_spacer[i] = QtWidgets.QSpacerItem(
                            40,
                            20,
                            QtWidgets.QSizePolicy.Expanding,
                            QtWidgets.QSizePolicy.Minimum,
                        )
                        self.leaderboard_player_layout[i].addItem(
                            self.leaderboard_player_spacer[i]
                        )
                        self.verticalLayout_8.addWidget(self.leaderboard_player[i])

                        # Getting players banner and add it to player_cards
                        player_card = f"https://media.valorant-api.com/playercards/{x.PlayerCardID}/smallart.png"
                        player_cards[i] = player_card

                    except AttributeError:
                        break
                else:
                    break

            self.leaderboard_spacer = QtWidgets.QSpacerItem(
                20,
                40,
                QtWidgets.QSizePolicy.Minimum,
                QtWidgets.QSizePolicy.Expanding,
            )
            self.verticalLayout_8.addItem(self.leaderboard_spacer)

            # Get & Set Banner
            with concurrent.futures.ThreadPoolExecutor() as executor:
                image = executor.map(requests.get, player_cards.values())
                image = tuple(image)

            for _ in player_cards:
                img = QImage()
                img.loadFromData(image[_].content)
                self.leaderboard_player_banner[_].setPixmap(QPixmap(img))

            print(f"LEADERBOARD took --- %s seconds ---" % (time.time() - start_time))

        except BaseException as error:
            print(traceback.format_exc())
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText(f"{format(error)}")
            msg_box.setWindowTitle("an error occurred")
            msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg_box.exec()

    def get_match_information(self):
        try:
            # Get Match Details
            Match = valo_api.get_match_details_v2(match_id=self.match_id_input.text())

            # Variables
            match_id = Match.metadata.matchid
            game_date = Match.metadata.game_start_patched
            game_last = Match.metadata.game_length
            region = Match.metadata.region.upper()
            cluster = Match.metadata.cluster
            gamemode = Match.metadata.mode
            game_map = Match.metadata.map

            self.MatchInformations.setText(
                f"{match_id}\n"
                f"{game_date} - {game_last}\n"
                f"{region} - {cluster}\n"
                f"{gamemode} - {game_map}"
            )
        except BaseException as error:
            print(traceback.format_exc())
            self.match_error.setText(f"{format(error)}")

    def reset_information(self):
        try:
            tier_icon = Path(__file__).parent.joinpath("Images\Example\ExampleRank.png")
            example_banner = Path(__file__).parent.joinpath(
                "Images/Example/ExampleWideBanner.png"
            )
            basic_dummy = Path(__file__).parent.joinpath("Images/Dummy/Basic.png")
            self.player_name.setText("")
            self.player_name.setPlaceholderText("PLAYER NAME (16 characters)")
            self.player_tag.setText("")
            self.player_tag.setPlaceholderText("PLAYER TAG (5 characters)")
            self.player_banner.setPixmap(QtGui.QPixmap(str(example_banner)))
            self.player_ids.setText("puu-ID | EU")
            self.player.setText(
                f'<html><head/><body><p><span style=" font-size:29pt;">player#Tag<p'
                f'>Account Level 0 | Iron 3 </span><img src="{tier_icon}"width="33 '
                f'"height="33"/><span style=" font-size:20pt;"> 0rr</span></p></body></html>'
            )
            self.MatchInformations.setText(
                "Match ID\n"
                "Date - Match Duration\n"
                "region - Cluster\n"
                "Gamemode - Map"
            )
            self.accuarcy_text.setText(
                "Headshots: 0%\n" "Bodyshots: 0%\n" "Legshots: 0%"
            )
            self.accuracy_logo.setPixmap(QtGui.QPixmap(str(basic_dummy)))
            self.stats_text.setText(
                "K/D: 0.00\n"
                "Average Combat Score: 0\n"
                "Average Damage per Round: 0\n"
                "Winrate: 0%"
            )
            self.home_error.setText(f"")
            self.match_error.setText(f"")
            self.comp_history.setText(
                "Matchmaking Ratio \n"
                "Competitive Wins \n"
                "Competitive Games played \n"
                "Previous Ranks \n"
                "rank history\n"
                ""
            )
            self.history.setText(
                "Day, Date, Time\n"
                "Match ID\n"
                "region - Cluster\n"
                "Map | Gamemode | Agent: Jett\n"
                "0-0 WON\n"
                "Kills Assists Deaths | 0.00 K/D\n"
                "HS%: 0% | ACS: 0 | ADR: 0 | Total Score: 0\n"
            )

        except BaseException as error:
            print(traceback.format_exc())

    def modeSwitch(self):
        LightMode = Path(__file__).parent.joinpath("Images/LightMode.webp")
        DarkMode = Path(__file__).parent.joinpath("Images/DarkMode.webp")
        if self.dark_mode:
            self.dark_mode = False
            self.mode_switcher.setIcon(QtGui.QIcon(str(LightMode)))
            QApplication.setPalette(QApplication.style().standardPalette())
        else:
            self.dark_mode = True
            self.mode_switcher.setIcon(QtGui.QIcon(str(DarkMode)))
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
            dark_palette.setColor(QPalette.Active, QPalette.Button, QColor(35, 35, 35))
            dark_palette.setColor(QPalette.Disabled, QPalette.ButtonText, Qt.darkGray)
            dark_palette.setColor(QPalette.Disabled, QPalette.WindowText, Qt.darkGray)
            dark_palette.setColor(QPalette.Disabled, QPalette.Text, Qt.darkGray)
            dark_palette.setColor(QPalette.Disabled, QPalette.Light, QColor(35, 35, 35))
            QApplication.setPalette(dark_palette)


async def main():
    import sys

    app = QtWidgets.QApplication(sys.argv)
    valorant_tracking_by_navisgames = QtWidgets.QMainWindow()
    ui = Ui_ValorantTrackerByNavisGames()
    await ui.setupUi(valorant_tracking_by_navisgames)
    QApplication.setStyle("Fusion")
    valorant_tracking_by_navisgames.show()
    sys.exit(app.exec_())


asyncio.run(main())
