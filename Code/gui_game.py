
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGraphicsScene, QPushButton, QGraphicsView, QLabel
from PyQt5.QtCore import pyqtSignal

from gi_unit import GIUnit
from gi_tile import GITile

class GameWindow(QMainWindow):

    switch_window = pyqtSignal()

    def __init__(self, game):
        super(GameWindow, self).__init__()
        self.game = game
        self.unitgi_list = []

        #self.chosen_mem = None # used to detect chosen tile changes
        
        self.setCentralWidget(QWidget())

        self.layout = QVBoxLayout()
        self.centralWidget().setLayout(self.layout)

        self.init_Scene()
        self.init_GameUI()
        self.init_Signals()

        self.update_turn_data()

        self.setGeometry(0,0,800,600) # Settings change window size


    def init_Scene(self): # populate scene from self.game

        self.scene = QGraphicsScene() # create scene to handle gi in
        
        game_map = self.game.level.map # tile generation

        x = len(game_map[0]) * 64
        y = len(game_map) * 64
        self.scene.setSceneRect(0,0,x,y) #IMPLEMENT SCALING BY MAP!!, this is max size of scene

        for h in range(len(game_map)):
            for w in range(len(game_map[0])):
                obj = GITile(game_map[h][w])
                self.scene.addItem(obj)

        units = self.game.all_units() # unit generation

        for unit in units:
            obj = GIUnit(unit)
            self.scene.addItem(obj)  

        self.update_unitgi_list() #update units to list

        self.view = QGraphicsView(self.scene, self) # crete view and add to layout
        self.view.adjustSize()
        self.view.show()

        self.layout.addWidget(self.view)

    def init_GameUI(self):
        layout_ui = QHBoxLayout()

        self.btn_quit = QPushButton("Quit", self)
        self.btn_quit.clicked.connect(self.quit)
        layout_ui.addWidget(self.btn_quit)

        layout_game_data = QVBoxLayout() # game data 

        self.lbl_turn = QLabel()
        self.lbl_active_player = QLabel()
        self.lbl_gold = QLabel()

        layout_game_data.addWidget( self.lbl_turn )
        layout_game_data.addWidget( self.lbl_active_player )
        layout_game_data.addWidget( self.lbl_gold )

        layout_ui.addLayout(layout_game_data)

        layout_chosen_unit_data = QVBoxLayout() # chosen unit data

        self.lbl_hp = QLabel()
        self.lbl_ap = QLabel()
        self.lbl_arm = QLabel()
        self.lbl_dmg = QLabel()
        self.lbl_rng = QLabel()

        layout_chosen_unit_data.addWidget( self.lbl_hp )
        layout_chosen_unit_data.addWidget( self.lbl_ap )
        layout_chosen_unit_data.addWidget( self.lbl_arm )
        layout_chosen_unit_data.addWidget( self.lbl_dmg )
        layout_chosen_unit_data.addWidget( self.lbl_rng )

        layout_ui.addLayout(layout_chosen_unit_data)

        self.btn_next_turn = QPushButton("Next Turn", self)
        self.btn_next_turn.clicked.connect(self.game.next_turn)
        layout_ui.addWidget(self.btn_next_turn) 

        self.layout.addLayout(layout_ui)

    def init_Signals(self): # init signal from game 
        self.game.chosen_change.connect(self.update_chosen_data)
        self.game.turn_change.connect(self.update_turn_data)
        self.game.gi_update.connect(self.update_gi)

    def update_unitgi_list(self):
        self.unitgi_list = []

        for item in self.scene.items():
            if type(item) is GIUnit:
                self.unitgi_list.append(item)

    def update_gi(self):
        self.update_unitgi_list()

        for unit_gi in self.unitgi_list:

            print(unit_gi.unit.status)

            if unit_gi.unit.status == 'Dead':
                self.scene.removeItem(unit_gi)


            else:
                unit_gi.update()

    def update_chosen_data(self):
        if self.game.chosen_tile is not None:
            unit = self.game.chosen_tile.unit

            if unit is None:
                self.lbl_hp.setText(None)
                self.lbl_ap.setText(None)
                self.lbl_arm.setText(None)
                self.lbl_dmg.setText(None)
                self.lbl_rng.setText(None)
            else:
                self.lbl_hp.setText("hp:"+str(unit.hp))
                self.lbl_ap.setText("ap:"+str(unit.ap))
                self.lbl_arm.setText("armour:"+str(unit.arm))
                self.lbl_dmg.setText("damage:"+str(unit.dmg))
                self.lbl_rng.setText("range:"+str(unit.rng))
        else:
            self.lbl_hp.setText(None)
            self.lbl_ap.setText(None)
            self.lbl_arm.setText(None)
            self.lbl_dmg.setText(None)
            self.lbl_rng.setText(None)

    def update_turn_data(self):
        self.lbl_turn.setText( "Turn number: " + str(self.game.turn_num) )
        self.lbl_active_player.setText( "Active Player: " + self.game.players[self.game.turn_player].name ) 
        self.lbl_gold.setText( "Gold:" + self.game.players[self.game.turn_player].gold )

    def quit(self):
        self.switch_window.emit()