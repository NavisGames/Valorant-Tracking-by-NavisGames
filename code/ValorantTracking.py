# Credits for this program go to NavisGames, selling this program or saying it's yours is not allowed! Read the
# license for more. If you want, please fork this program to share what you changed in this program ^^
from itertools import accumulate
from PyQt5.QtCore import Qt, QSettings
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication
from PyQt5.QtGui import QPalette, QColor, QImage, QPixmap, QIcon
import valo_api
import requests
from pathlib import Path

import httpx as http
import concurrent.futures
import time

valo_api.set_api_key("HDEV-e6c002ce-3c53-4464-9586-c58c586baf1c")  # HIDE IN GITHUB!

def get_image(url):
    with http.Client() as client:
        r = client.get(url)
    img = QImage()
    img.loadFromData(r.content)
    return img


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        try:
            # Main Window
            MainWindow.setObjectName("Valorant Tracking by NavisGames")
            MainWindow.resize(1095, 755)
            MainWindow.setMinimumSize(QtCore.QSize(1095, 765))
            MainWindow.setMaximumSize(QtCore.QSize(1095, 765))
            font = QtGui.QFont()
            font.setFamily("Open Sans")
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            MainWindow.setFont(font)
            MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
            MainWindow.setAutoFillBackground(False)
            MainWindow.setStyleSheet("")
            MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
            MainWindow.setWindowIcon((QtGui.QIcon('icon.png')))
            self.centralwidget = QtWidgets.QWidget(MainWindow)
            font = QtGui.QFont()
            font.setPointSize(8)
            self.centralwidget.setFont(font)
            self.centralwidget.setAutoFillBackground(False)
            self.centralwidget.setStyleSheet("")
            self.centralwidget.setObjectName("centralwidget")

            self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
            self.gridLayout.setContentsMargins(0, 0, 0, 0)
            self.gridLayout.setSpacing(0)
            self.gridLayout.setObjectName("gridLayout")

            # Creating Tabs
            self.Tabs = QtWidgets.QTabWidget(self.centralwidget)
            self.Tabs.setEnabled(True)

            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.Tabs.sizePolicy().hasHeightForWidth())
            self.Tabs.setSizePolicy(sizePolicy)

            self.Tabs.setMinimumSize(QtCore.QSize(0, 0))
            self.Tabs.setMaximumSize(QtCore.QSize(16777215, 16777215))

            font = QtGui.QFont()
            font.setPointSize(18)
            font.setKerning(True)
            self.Tabs.setFont(font)
            self.Tabs.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
            self.Tabs.setFocusPolicy(QtCore.Qt.TabFocus)
            self.Tabs.setAutoFillBackground(False)
            self.Tabs.setStyleSheet("")
            self.Tabs.setTabPosition(QtWidgets.QTabWidget.North)
            self.Tabs.setTabShape(QtWidgets.QTabWidget.Rounded)
            self.Tabs.setUsesScrollButtons(False)
            self.Tabs.setObjectName("Tabs")

            # Create Home Tab
            self.Home = QtWidgets.QWidget()
            font = QtGui.QFont()
            font.setPointSize(8)
            self.Home.setFont(font)
            self.Home.setAutoFillBackground(False)
            self.Home.setStyleSheet("")
            self.Home.setObjectName("Home")

            # Home Title
            self.Title = QtWidgets.QLabel(self.Home)
            self.Title.setGeometry(QtCore.QRect(0, 0, 1121, 51))
            font = QtGui.QFont()
            font.setPointSize(29)
            self.Title.setFont(font)
            self.Title.setAlignment(QtCore.Qt.AlignCenter)
            self.Title.setObjectName("Title")

            # Enter Name
            self.NameInput = QtWidgets.QLineEdit(self.Home)
            self.NameInput.setGeometry(QtCore.QRect(90, 60, 151, 20))
            self.NameInput.setText("")
            self.NameInput.setAlignment(QtCore.Qt.AlignCenter)
            self.NameInput.setObjectName("NameInput")

            # Enter Hashtag
            self.HashtagInput = QtWidgets.QLineEdit(self.Home)
            self.HashtagInput.setGeometry(QtCore.QRect(320, 60, 151, 20))
            self.HashtagInput.setText("")
            self.HashtagInput.setAlignment(QtCore.Qt.AlignCenter)
            self.HashtagInput.setObjectName("HashtagInput")

            # Enter Region
            self.RegionInput = QtWidgets.QComboBox(self.Home)
            self.RegionInput.setGeometry(QtCore.QRect(560, 60, 151, 20))
            self.RegionInput.setObjectName("RegionInput")
            self.RegionInput.addItem("")
            self.RegionInput.addItem("")
            self.RegionInput.addItem("")
            self.RegionInput.addItem("")
            self.RegionInput.addItem("")
            self.RegionInput.addItem("")

            # Enter Button
            self.GetButton = QtWidgets.QPushButton(self.Home)
            self.GetButton.setGeometry(QtCore.QRect(810, 59, 151, 22))
            font = QtGui.QFont()
            font.setPointSize(8)
            font.setBold(True)
            font.setWeight(75)
            font.setKerning(True)
            self.GetButton.setFont(font)
            self.GetButton.setObjectName("GetButton")

            # The Banner of Player
            self.BannerInformation = QtWidgets.QLabel(self.Home)
            self.BannerInformation.setGeometry(QtCore.QRect(10, 100, 451, 121))
            self.BannerInformation.setText("")
            self.BannerInformation.setTextFormat(QtCore.Qt.RichText)
            self.BannerInformation.setScaledContents(True)
            self.BannerInformation.setAlignment(QtCore.Qt.AlignCenter)
            self.BannerInformation.setObjectName("BannerInformation")

            # The Name of Player
            self.NameInformation = QtWidgets.QLabel(self.Home)
            self.NameInformation.setGeometry(QtCore.QRect(470, 120, 651, 41))
            font = QtGui.QFont()
            font.setPointSize(23)
            self.NameInformation.setFont(font)
            self.NameInformation.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
            self.NameInformation.setTextInteractionFlags(
                QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
            self.NameInformation.setObjectName("NameInformation")

            # Account Level
            self.Informations = QtWidgets.QLabel(self.Home)
            self.Informations.setGeometry(QtCore.QRect(470, 160, 651, 71))
            self.Informations.setTextFormat(QtCore.Qt.RichText)

            font = QtGui.QFont()
            font.setPointSize(8)
            self.Informations.setFont(font)
            self.Informations.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
            self.Informations.setTextInteractionFlags(
                QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
            self.Informations.setObjectName("Informations")

            # PuuID & Region
            self.PuuidRegionInformation = QtWidgets.QLabel(self.Home)
            self.PuuidRegionInformation.setGeometry(QtCore.QRect(470, 100, 651, 31))
            font = QtGui.QFont()
            font.setPointSize(10)
            self.PuuidRegionInformation.setFont(font)
            self.PuuidRegionInformation.setAlignment(
                QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
            self.PuuidRegionInformation.setTextInteractionFlags(
                QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
            self.PuuidRegionInformation.setObjectName("PuuidRegionInformation")

            # Added Leaderboard Tab

            self.Leaderboard = QtWidgets.QWidget()
            self.Leaderboard.setAutoFillBackground(False)
            self.Leaderboard.setObjectName("Leaderboard")
            MainWindow.setCentralWidget(self.centralwidget)
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Information)

            # Title of Leaderboard Tab
            self.LeaderboardTitle = QtWidgets.QLabel(self.Leaderboard)
            self.LeaderboardTitle.setGeometry(QtCore.QRect(0, 0, 1121, 51))
            font = QtGui.QFont()
            font.setPointSize(29)
            self.LeaderboardTitle.setFont(font)
            self.LeaderboardTitle.setFrameShape(QtWidgets.QFrame.NoFrame)
            self.LeaderboardTitle.setAlignment(QtCore.Qt.AlignCenter)
            self.LeaderboardTitle.setObjectName("LeaderboardTitle")

            # The Frame for 5000 players
            self.scrollFrame = QtWidgets.QScrollArea(self.Leaderboard)
            self.scrollFrame.setGeometry(QtCore.QRect(1, 79, 1091, 641))
            self.scrollFrame.setStyleSheet("border: none;\nbackground-color: rgba(72,68,68,0);")
            self.scrollFrame.setFrameShape(QtWidgets.QFrame.Box)
            self.scrollFrame.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
            self.scrollFrame.setWidgetResizable(True)
            self.scrollFrame.setObjectName("scrollFrame")

            # The Area of the Frame
            self.scrollArea = QtWidgets.QWidget()
            self.scrollArea.setGeometry(QtCore.QRect(0, 0, 1087, 637))
            self.scrollArea.setObjectName("scrollArea")
            self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollArea)
            self.verticalLayout.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout.setSpacing(5)
            self.verticalLayout.setObjectName("verticalLayout")

            # Leaderstats Player dicts

            self.Player = dict()
            self.PlayerText = dict()
            self.PlayerBanner = dict()

            # Refresh Button
            self.LeaderboardRefresh = QtWidgets.QPushButton(self.Leaderboard)
            self.LeaderboardRefresh.setGeometry(QtCore.QRect(10, 10, 40, 40))
            font = QtGui.QFont()
            font.setPointSize(16)
            self.LeaderboardRefresh.setFont(font)
            self.LeaderboardRefresh.setObjectName("LeaderboardRefresh")

            # Leaderboard Regions
            self.LeaderboardRegion = QtWidgets.QComboBox(self.Leaderboard)
            self.LeaderboardRegion.setGeometry(QtCore.QRect(440, 55, 85, 30))
            font = QtGui.QFont()
            font.setPointSize(15)
            font.setBold(True)
            font.setWeight(75)
            self.LeaderboardRegion.setFont(font)
            self.LeaderboardRegion.setObjectName("LeaderboardRegion")
            self.LeaderboardRegion.addItem("")
            self.LeaderboardRegion.addItem("")
            self.LeaderboardRegion.addItem("")
            self.LeaderboardRegion.addItem("")
            self.LeaderboardRegion.addItem("")
            self.LeaderboardRegion.addItem("")

            # Leaderboard Seasons / Acts
            self.LeaderboardSeason = QtWidgets.QComboBox(self.Leaderboard)
            self.LeaderboardSeason.setGeometry(QtCore.QRect(560, 55, 85, 30))
            font = QtGui.QFont()
            font.setPointSize(15)
            font.setBold(True)
            font.setWeight(75)
            self.LeaderboardSeason.setFont(font)
            self.LeaderboardSeason.setObjectName("LeaderboardSeason")
            self.LeaderboardSeason.addItem("E5A2")
            self.LeaderboardSeason.addItem("E5A1")
            self.LeaderboardSeason.addItem("E4A3")
            self.LeaderboardSeason.addItem("E4A2")
            self.LeaderboardSeason.addItem("E4A1")
            self.LeaderboardSeason.addItem("E3A3")
            self.LeaderboardSeason.addItem("E3A2")
            self.LeaderboardSeason.addItem("E3A1")
            self.LeaderboardSeason.addItem("E2A3")
            self.LeaderboardSeason.addItem("E2A2")
            self.LeaderboardSeason.addItem("E2A1")

            # Match History
            self.MatchHistory = QtWidgets.QTextEdit(self.Home)
            self.MatchHistory.setGeometry(QtCore.QRect(460, 225, 635, 500))
            font = QtGui.QFont()
            font.setPointSize(5)
            self.MatchHistory.setFont(font)
            self.MatchHistory.setStyleSheet("border: none;\nbackground-color: rgba(72,68,68,0);")
            self.MatchHistory.setFrameShape(QtWidgets.QFrame.Box)
            self.MatchHistory.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            self.MatchHistory.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            self.MatchHistory.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
            self.MatchHistory.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
            self.MatchHistory.setReadOnly(True)
            self.MatchHistory.setObjectName("MatchHistory")
            font = QtGui.QFont()
            font.setFamily("Open Sans")
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.MatchHistory.setFont(font)

            # MMR Changes
            self.CompetitiveInformation = QtWidgets.QTextEdit(self.Home)
            self.CompetitiveInformation.setGeometry(QtCore.QRect(0, 225, 451, 501))
            self.CompetitiveInformation.setStyleSheet("border: none;\nbackground-color: rgba(72,68,68,0);")
            self.CompetitiveInformation.setFrameShape(QtWidgets.QFrame.Box)
            self.CompetitiveInformation.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
            self.CompetitiveInformation.setReadOnly(True)
            self.CompetitiveInformation.setPlaceholderText("")
            self.CompetitiveInformation.setObjectName("CompetitiveInformation")
            font = QtGui.QFont()
            font.setFamily("Open Sans")
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.CompetitiveInformation.setFont(font)

            # Added Bundles Tab
            self.Bundles = dict()
            current_Bundle = valo_api.get_store_featured_v2()

            # Adding Tabs
            self.Tabs.addTab(self.Home, "Home")
            self.Tabs.addTab(self.Leaderboard, "Leaderboard")

            for i, bundles in enumerate(current_Bundle):
                # for i in range(current_Bundle):
                self.Bundles[i] = QtWidgets.QWidget()
                self.Bundles[i].setObjectName("Bundle")

                # Getting Current Bundle
                bundleUuid = current_Bundle[i].bundle_uuid
                # Getting Bundle Banner as PixMap
                bundleJson = requests.get(url=f"https://valorant-api.com/v1/bundles/{bundleUuid}").json()
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    img = executor.submit(get_image, bundleJson["data"]["displayIcon2"])
                    img = img.result()

                # Layouts
                self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Bundles[i])
                self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
                self.verticalLayout_2.setSpacing(5)
                self.verticalLayout_2.setObjectName("verticalLayout_2")

                # Bundle Name
                self.BundleName = QtWidgets.QLabel(self.Bundles[i])
                font = QtGui.QFont()
                font.setFamily("Open Sans")
                font.setPointSize(22)
                font.setBold(True)
                font.setWeight(75)
                self.BundleName.setFont(font)
                self.BundleName.setAlignment(QtCore.Qt.AlignCenter)
                self.BundleName.setObjectName("Name")
                self.verticalLayout_2.addWidget(self.BundleName)

                # Bundle Image
                self.Image = QtWidgets.QLabel(self.Bundles[i])
                self.Image.setText("")
                self.Image.setScaledContents(True)
                self.Image.setIndent(-1)
                self.Image.setObjectName("Image")
                self.verticalLayout_2.addWidget(self.Image)
                self.Image.setPixmap(QtGui.QPixmap(img))

                # Bundle Description
                self.extraDescription = QtWidgets.QLabel(self.Bundles[i])
                font = QtGui.QFont()
                font.setFamily("Open Sans")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.extraDescription.setFont(font)
                self.extraDescription.setScaledContents(False)
                self.extraDescription.setAlignment(QtCore.Qt.AlignCenter)
                self.extraDescription.setWordWrap(True)
                self.extraDescription.setObjectName("extraDescription")

                self.verticalLayout_2.addWidget(self.extraDescription)

                # Bundle Price
                self.Price = QtWidgets.QLabel(self.Bundles[i])
                font = QtGui.QFont()
                font.setFamily("Open Sans")
                font.setPointSize(15)
                font.setBold(True)
                font.setWeight(75)
                self.Price.setFont(font)
                self.Price.setScaledContents(False)
                self.Price.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
                self.Price.setWordWrap(True)
                self.Price.setObjectName("Price")
                self.verticalLayout_2.addWidget(self.Price)

                # Bundle Items
                self.Items = QtWidgets.QLabel(self.Bundles[i])
                font = QtGui.QFont()
                font.setFamily("Open Sans")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.Items.setFont(font)
                self.Items.setScaledContents(False)
                self.Items.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
                self.Items.setWordWrap(True)
                self.Items.setObjectName("Items")
                self.verticalLayout_2.addWidget(self.Items)

                # Get Bundle Items
                Items = []
                for item in current_Bundle[i].items:
                    if item.amount > 1:
                        Items.append(
                            f"{item.amount}x {item.name} - {item.base_price} Valorant Points | {item.discounted_price} -> whole Bundle\n")
                    else:
                        Items.append(
                            f"{item.name} - {item.base_price} Valorant Points | {item.discounted_price} -> whole Bundle\n")

                # Sets the Current Bundle Texts
                self.BundleName.setText(f"{bundleJson['data']['displayName']}")
                if bundleJson['data']['extraDescription'] is None:
                    self.extraDescription.hide()
                else:
                    self.extraDescription.setText(f"{bundleJson['data']['extraDescription']}")
                self.Price.setText(f"Bundle Price - {current_Bundle[i].bundle_price} Valorant Points")
                self.Items.setText("".join(Items))

                self.Tabs.addTab(self.Bundles[i], f"Bundle: {bundleJson['data']['displayName']}")

            # Functions
            self.Tabs.setCurrentIndex(0)

            self.GetButton.clicked.connect(self.get_information)

            self.LeaderboardRefresh.clicked.connect(self.get_leaderboard)

            self.retranslateUi(MainWindow)

            QtCore.QMetaObject.connectSlotsByName(MainWindow)

            self.gridLayout.addWidget(self.Tabs)
        except BaseException as error:
            print('An exception occurred: {}'.format(error))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        # Translate Main
        MainWindow.setWindowTitle(_translate("MainWindow", "Valorant Tracking by NavisGames"))

        # Titles
        self.Title.setText(_translate("MainWindow", "Valorant | Account Details"))
        self.LeaderboardTitle.setText(_translate("ValorantTrackingbyNavisGames", "Valorant | Leaderboard"))

        # Inputs
        self.NameInput.setPlaceholderText(_translate("MainWindow", "Player Name"))
        self.HashtagInput.setPlaceholderText(_translate("MainWindow", "Player Tag"))

        # Buttons
        self.GetButton.setText(_translate("MainWindow", "Get information"))
        self.LeaderboardRefresh.setText(_translate("ValorantTrackingbyNavisGames", "R"))

        # Regions
        self.RegionInput.setItemText(0, _translate("MainWindow", "EU"))
        self.RegionInput.setItemText(1, _translate("MainWindow", "NA"))
        self.RegionInput.setItemText(2, _translate("MainWindow", "KR"))
        self.RegionInput.setItemText(3, _translate("MainWindow", "AP"))
        self.RegionInput.setItemText(4, _translate("MainWindow", "LATAM"))
        self.RegionInput.setItemText(5, _translate("MainWindow", "BR"))

        self.LeaderboardRegion.setCurrentText(_translate("ValorantTrackingbyNavisGames", "EU"))
        self.LeaderboardRegion.setItemText(0, _translate("ValorantTrackingbyNavisGames", "EU"))
        self.LeaderboardRegion.setItemText(1, _translate("ValorantTrackingbyNavisGames", "NA"))
        self.LeaderboardRegion.setItemText(2, _translate("ValorantTrackingbyNavisGames", "KR"))
        self.LeaderboardRegion.setItemText(3, _translate("ValorantTrackingbyNavisGames", "AP"))
        self.LeaderboardRegion.setItemText(4, _translate("ValorantTrackingbyNavisGames", "LATAM"))
        self.LeaderboardRegion.setItemText(5, _translate("ValorantTrackingbyNavisGames", "BR"))

    def get_information(self):
        try:
            start_time = time.time()
            # API funcions
            Details = valo_api.get_account_details_by_name(version="v1", name=self.NameInput.text(),
                                                           tag=self.HashtagInput.text(),
                                                           force_update=True)
            # Puuid, Region, Account Level and the PlayerCard
            Puuid = Details.puuid
            Region = Details.region
            Account_level = Details.account_level
            Card = str(Details.card.wide)

            # Get Rank, RR and MMR
            RankDetails = valo_api.get_mmr_details_by_name_v2(region=self.RegionInput.currentText(),
                                                              name=self.NameInput.text(), tag=self.HashtagInput.text())
            Rank = RankDetails.current_data.currenttierpatched
            RR = RankDetails.current_data.ranking_in_tier
            MMR = RankDetails.current_data.elo

            # Get Match History
            HistoryDetails = valo_api.get_match_history_by_name(version="v3", region=self.RegionInput.currentText(),
                                                                name=self.NameInput.text(),
                                                                tag=self.HashtagInput.text(),
                                                                size=5)

            # Get Recent Rank Changes
            MMRDetails = valo_api.get_mmr_history_by_name(version="v1", region=self.RegionInput.currentText(),
                                                          name=self.NameInput.text(), tag=self.HashtagInput.text())

            # Checks if there any games already played.
            try:
                wins = RankDetails.by_season["e5a2"].wins
                games_played = RankDetails.by_season["e5a2"].number_of_games
            except AttributeError:
                wins = 0
                games_played = 0

            # Gets Last Rank
            lastRank = RankDetails.by_season

            # Creates List with MMR, Comp Wins, Comp Games
            previous_ranks = [f"Matchmaking Ratio: {MMR}\n"
                              f"Competitive Wins: {wins}\n"
                              f"Competitive Games played: {games_played}\n"
                              "\nPrevious Ranks:\n"
                              ]

            # Adds last Ranks with MMR, Wins, Games to the List
            for x in lastRank:
                try:
                    if lastRank[x].final_rank_patched is not None:
                        previous_ranks.append(
                            f"{x.upper()}: {lastRank[x].final_rank_patched} | {lastRank[x].wins} Wins - {lastRank[x].number_of_games}Game(s) played\n")
                    else:
                        # if player didn't play in this act, then say continue
                        continue
                # If API problem (I guess?) then continue
                except BaseException as error:
                    print('An exception occurred: {}'.format(error))

            # If there is an rank, add a rank history (MMR Details)
            if Rank is not None:
                previous_ranks.append(
                    f"\nRank History:\n")
                # For every Last Match in The Detail get +RR or -RR and current rank / rr
                for x in MMRDetails:
                    # If getting + else -
                    if x.mmr_change_to_last_game >= 0:
                        previous_ranks.append(
                            f"{x.date} | {x.currenttierpatched} {x.ranking_in_tier}rr (+{x.mmr_change_to_last_game})\n")
                    else:
                        previous_ranks.append(
                            f"{x.date} | {x.currenttierpatched} {x.ranking_in_tier}rr ({x.mmr_change_to_last_game})\n")

            # Makes List to a String.
            previous_ranks = "".join(previous_ranks)

            # Getting Banner as PixMap
            with concurrent.futures.ThreadPoolExecutor() as executor:
                img = executor.submit(get_image, Card)
                img = img.result()

            # Setting Banner, Name and Region, Puuid, Previous Ranks
            self.BannerInformation.setPixmap(QPixmap(img))
            self.NameInformation.setText(f"{Details.name}#{Details.tag}")
            self.PuuidRegionInformation.setText(f"{Puuid} | {Region.upper()}")
            self.CompetitiveInformation.setText(f"{previous_ranks}")  # <- The List which got made to a string

            # Gets the current Rank AS TIER INDEX (int) and compares it with the index data, to get the RANK IMAGE
            tier_index = RankDetails.current_data.currenttier
            data = requests.get("https://valorant-api.com/v1/competitivetiers").json()
            tiers = data["data"][-1]["tiers"]
            tier = None
            # If it has any Rank, get it ELSE say unranked
            if Rank is not None:
                for tier in tiers:
                    if tier["tier"] == tier_index:
                        tier = tier["tierName"]
                        break
            else:
                tier = "UNRANKED"
            # Gets the PNG for the HTML Rich Text
            tier_icon = Path(__file__).parent.joinpath(f'Ranks/{tier}.png')

            # Sets an HTML Text with the Rank as Texture and a Text also it gets the Current Rank as PNG
            if Rank is not None:
                self.Informations.setText(
                    f"<html><head/><body><p><span style=\" font-size:18pt;\">Account Level: {Account_level}<br>Current Rank: {Rank} </span><img src=\"{tier_icon}\" width=\"29\" height=\"29\"/><span style=\" font-size:18pt;\"> {RR}rr</span></p></body></html>")
            else:
                remaining = RankDetails.current_data.games_needed_for_rating
                self.Informations.setText(
                    f"<html><head/><body><p><span style=\" font-size:18pt;\">Account Level: {Account_level}<br>Current Rank: Unrated </span><img src=\"{tier_icon}\" width=\"29\" height=\"29\"/><span style=\" font-size:18pt;\"> {remaining} games remaining</span></p></body></html>")

            # Get Match History as a List, and gets every current matches
            match_History = []
            for x in HistoryDetails:

                # Match, Team and Players
                match = x.metadata
                teams = x.teams
                players = x.players

                # Functions to get Team, Stats of a player.
                def findTeamOfPlayer(player):
                    team = list(accumulate(p.team for p in players.all_players if p.name == player))
                    return team[0] if team else None

                def findStatsOfPlayer(player):
                    stats = list(accumulate(p.stats for p in players.all_players if p.name == player))
                    return stats[0] if stats else None

                # Get Stats of Player with get_stats function
                get_stats = findStatsOfPlayer(Details.name)
                kills = get_stats.kills
                deaths = get_stats.deaths
                assists = get_stats.assists
                score = get_stats.score
                # Rounds to 0.00 <- 2 Decimals
                KD = format(kills / deaths, '.2f')

                # Get Team and Team information of Player with get_team function
                get_team = findTeamOfPlayer(Details.name)

                # If Team is Blue, Else Red, if nothing do nothing.
                if get_team == "Blue":
                    won = teams.blue.has_won
                    rounds_won = teams.blue.rounds_won
                    rounds_lost = teams.blue.rounds_lost

                elif get_team == "Red":
                    won = teams.red.has_won
                    rounds_won = teams.red.rounds_won
                    rounds_lost = teams.red.rounds_lost

                else:
                    won = ""
                    rounds_won = ""
                    rounds_lost = ""

                # If match lost, make text lost
                if not won:
                    won = "LOST"
                else:
                    won = "WON"

                # Get Match ID, Map, Region, Cluster and Mode with Match Metadata
                match_id = match.matchid
                match_map = match.map
                region = match.region.upper()
                cluster = match.cluster
                mode = match.mode

                # If Deathmatch, remove Rounds and Won/Lost
                if mode == "Deathmatch":
                    match_History.append(
                        f"{match.game_start_patched} | Match {match_id}\n{region} - {cluster}\n{match_map} - {mode}\n {kills} Kills {assists} Assists {deaths} Deaths - {KD} KD | {score} Score\n\n")
                else:
                    match_History.append(
                        f"{match.game_start_patched} | Match {match_id}\n{region} - {cluster}\n{match_map} - {mode}\n{rounds_won}-{rounds_lost} {won}\n{kills} Kills {assists} Assists {deaths} Deaths - {KD} KD | {score} Score\n\n")

            # Makes List to String.
            match_History = "".join(match_History)

            # Set Match History Text
            self.MatchHistory.setText(f"{match_History}")  # <- List which got made to a string
            print("PLAYER took --- %s seconds ---" % (time.time() - start_time))

        except BaseException as error:
            self.Informations.setText("")
            self.NameInformation.setText("")
            self.PuuidRegionInformation.setText("")
            self.MatchHistory.setText("")
            self.BannerInformation.setPixmap(QPixmap(None))
            self.CompetitiveInformation.setText('An exception occurred: {}'.format(error))
            print('An exception occurred: {}'.format(error))

    def get_leaderboard(self):
        PlayerCount = 3000

        try:

            # Valo API get leaderboard with season_id
            if self.LeaderboardSeason.currentText() == "E5A2":
                Details = valo_api.get_leaderboard(version="v2", region=self.LeaderboardRegion.currentText())
            else:
                Details = valo_api.get_leaderboard(version="v2", region=self.LeaderboardRegion.currentText(),
                                                   season_id=self.LeaderboardSeason.currentText())

            # Gets Message Box for Loading Leaderboard
            self.msg.setText(
                f"Loading leaderboard! The program could possibly freeze.\nWait a few seconds to minutes until its done")
            self.msg.setWindowTitle("Valorant Tracking")
            self.msg.exec_()

            # Start Timer
            start_time = time.time()
            Player_Cards = {}

            # For every Player get Ranks, RR, Placing, Number of wins, PlayerCard
            for i in range(PlayerCount):
                try:
                    self.PlayerBanner[i].deleteLater()
                    self.PlayerText[i].deleteLater()
                    self.Player[i].deleteLater()
                    Player_Cards = {}
                except KeyError:
                    continue

            for i, x in enumerate(Details.players):
                if i < PlayerCount:
                    try:
                        # Create "Player Layout"
                        self.Player[i] = QtWidgets.QHBoxLayout()
                        self.Player[i].setObjectName(f"Player{i}")

                        # Create Player Banner
                        self.PlayerBanner[i] = QtWidgets.QLabel(self.scrollArea)
                        self.PlayerBanner[i].setText("")
                        self.PlayerBanner[i].setScaledContents(True)
                        self.PlayerBanner[i].setObjectName(f"Player{i}Banner")

                        # Add Banner to Layout
                        self.Player[i].addWidget(self.PlayerBanner[i])

                        # Create Player Text (For Win Counter etc.)
                        self.PlayerText[i] = QtWidgets.QLabel(self.scrollArea)
                        self.PlayerText[i].setObjectName(f"Player{i}Text")
                        font = QtGui.QFont()
                        font.setPointSize(12)
                        font.setBold(True)
                        self.PlayerText[i].setFont(font)

                        # Add Text to Layout
                        self.Player[i].addWidget(self.PlayerText[i])
                        self.Player[i].setStretch(1, 1)
                        self.verticalLayout.addLayout(self.Player[i])

                        # Needs an Update
                        if self.LeaderboardSeason.currentText() == "E5A1" or "E5A2":
                            if x.competitiveTier == 27:
                                Rank = "Radiant"
                            elif x.competitiveTier == 26:
                                Rank = "Immortal 3"
                            elif x.competitiveTier == 25:
                                Rank = "Immortal 2"
                            elif x.competitiveTier == 24:
                                Rank = "Immortal 1"
                            elif x.competitiveTier == 23:
                                Rank = "Ascendant 3"
                            elif x.competitiveTier == 22:
                                Rank = "Ascendant 2"
                            elif x.competitiveTier == 21:
                                Rank = "Ascendant 1"
                        else:
                            if x.competitiveTier == 24:
                                Rank = "Radiant"
                            elif x.competitiveTier == 23:
                                Rank = "Immortal 3"
                            elif x.competitiveTier == 22:
                                Rank = "Immortal 2"
                            elif x.competitiveTier == 21:
                                Rank = "Immortal 1"

                        if x.IsAnonymized:
                            # Set Anonymous Player from Current Index to Information
                            self.PlayerText[i].setText(
                                f"#{x.leaderboardRank} Anonymous Player | {Rank} {x.rankedRating}rr - {x.numberOfWins} Wins")
                        else:
                            # Set Player from Current Index to Information (Rank, Name, #, RR, Wins, PUUID)
                            self.PlayerText[i].setText(
                                f"#{x.leaderboardRank} {x.gameName}#{x.tagLine} | {Rank} {x.rankedRating}rr - {x.numberOfWins} Wins | {x.puuid}")

                        # Get Playercard for Banner
                        PlayerCard = f"https://media.valorant-api.com/playercards/{x.PlayerCardID}/smallart.png"
                        Player_Cards[i] = PlayerCard
                    except AttributeError:
                        break  # In case if some Players don't load (API problems)
                else:
                    break

            # Get Banner
            with concurrent.futures.ThreadPoolExecutor() as executor:
                image = executor.map(requests.get, Player_Cards.values())
                image = tuple(image)

            # Set Banner
            for _ in Player_Cards:
                img = QImage()
                img.loadFromData(image[_].content)
                self.PlayerBanner[_].setPixmap(QPixmap(img))

            # Spacer for Banner etc
            spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                               QtWidgets.QSizePolicy.Expanding)
            self.verticalLayout.addItem(spacerItem)
            self.scrollFrame.setWidget(self.scrollArea)
            print(f"LEADERBOARD took --- %s seconds ---" % (time.time() - start_time))
        except BaseException as error:
            print('An exception occurred: {}'.format(error))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    Is_DarkMode = True

    if Is_DarkMode is True:
        QApplication.setStyle("Fusion")
        dark_palette = QPalette()
        dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.WindowText, Qt.white)
        dark_palette.setColor(QPalette.Base, QColor(35, 35, 35))
        dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ToolTipBase, QColor(25, 25, 25))
        dark_palette.setColor(QPalette.ToolTipText, Qt.white)
        dark_palette.setColor(QPalette.Text, Qt.white)
        dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ButtonText, Qt.white)
        dark_palette.setColor(QPalette.BrightText, Qt.red)
        dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.HighlightedText, QColor(35, 35, 35))
        dark_palette.setColor(QPalette.Active, QPalette.Button, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.Disabled, QPalette.ButtonText, Qt.darkGray)
        dark_palette.setColor(QPalette.Disabled, QPalette.WindowText, Qt.darkGray)
        dark_palette.setColor(QPalette.Disabled, QPalette.Text, Qt.darkGray)
        dark_palette.setColor(QPalette.Disabled, QPalette.Light, QColor(53, 53, 53))
        QApplication.setPalette(dark_palette)
    else:
        QApplication.setStyle("")
        pass
    MainWindow.show()
    sys.exit(app.exec_())
