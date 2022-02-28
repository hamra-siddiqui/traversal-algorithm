# Graph Traversing #
from tkinter import *
import time

global mode, startNode, goalNode, goalCity, ovalLabel
mode = False
startNode = 0
goalNode = 0
goalCity = ""
ovalLabel = {}


class GraphTraversal:
    def clicked(self, *args):
        global startNode, goalNode
        event = args[0]
        startBtnStatus = self.start_btn.cget("relief")
        goalBtnStatus = self.goal_btn.cget("relief")
        # print(event
        # print(f"wow you're at index: {event.__dict__}, {event.y}")
        print('lol nub:', event)
        if startBtnStatus == "sunken":
            print()
            startNode = (event.widget.find_closest(event.x, event.y))[0]
            print(event.widget.find_closest(event.x, event.y))
            self.make_canvas.itemconfig(startNode, fill="red")
            self.total_cities[startNode - 1].config(bg="red")
            # self.make_canvas.itemconfig(self.total_cities[startNode-1]._name, bg="red")
            # self.make_canvas.itemcget(self.total_cities[startNode-1]._name,"text")
            print(self.total_cities[startNode - 1]._name)
            self.start_btn.config(bg="black", fg="white", relief=RAISED)
            print('startNode: ', startNode)
            print('goalNode: ', goalNode)
        if goalBtnStatus == "sunken":
            goalNode = (event.widget.find_closest(event.x, event.y))[0]
            self.make_canvas.itemconfig(goalNode, fill="green")
            self.total_cities[goalNode - 1].config(bg="green")
            self.goal_btn.config(bg="black", fg="white", relief=RAISED)
            print('startNode: ', startNode)
            print('goalNode: ', goalNode)

    def __init__(self, root):
        self.window = root
        self.make_canvas = Canvas(self.window, bg="gray", relief=RAISED, bd=7, width=800, height=768)
        self.make_canvas.pack()
        # Status label initialization
        self.status = None
        self.start_btn = None
        self.goal_btn = None
        self.dropdown = None
        # Some list initialization bt default
        self.cities = ['Select goal',
                       'Arad',
                       'Zerind',
                       'Sibiu',
                       'Temisora',
                       'Oradea',
                       'Rimnicu',
                       'Fagaras',
                       'Lugoj',
                       'Craiova',
                       'Pitesti',
                       'Bucharest',
                       'Mehadia',
                       'Dobreta'
                       ]
        self.vertex_connections = []
        self.total_nodes = []
        self.queue_bfs = []
        self.stack_dfs = []
        self.total_cities = []

        # Some default function call
        self.basic_set_up()
        self.initialize_vertex()

    def basic_set_up(self):
        heading = Label(self.make_canvas, text="Traversal Visualization", bg="gray", fg="black",
                        font=("Arial", 20, "bold", "italic"))
        heading.place(x=260, y=10)

        bfs_btn = Button(self.window, text="BFS", font=("Arial", 15, "bold"), bg="black", fg="white", relief=RAISED,
                         bd=8, command=self.bfs)
        bfs_btn.place(x=455, y=640)

        dfs_btn = Button(self.window, text="DFS", font=("Arial", 15, "bold"), bg="black", fg="white", relief=RAISED,
                         bd=8, command=self.dfs)
        dfs_btn.place(x=545, y=640)

        Reset_btn = Button(self.window, text="Reset", font=("Arial", 15, "bold"), bg="white", fg="black", relief=RAISED,
                           bd=8, command=self.reset)
        Reset_btn.place(x=675, y=640)

        self.start_btn = Button(self.window, text="START", font=("Arial", 15, "bold"), bg="black", fg="white",
                                relief=RAISED,
                                bd=8, command=self.mode_start)
        self.start_btn.place(x=20, y=640)

        self.goal_btn = Button(self.window, text="GOAL", font=("Arial", 15, "bold"), bg="black", fg="white",
                               relief=RAISED,
                               bd=8, command=self.mode_goal)
        self.goal_btn.place(x=135, y=640)

        self.status = Label(self.make_canvas, text="Not Visited", bg="gray", fg="black",
                            font=("Arial", 20, "bold", "italic"))
        self.status.place(x=20, y=590)

        # setting variable for Integers
        self.variable = StringVar()
        self.variable.set(self.cities[0])

        # creating widget
        self.dropdown = OptionMenu(
            self.make_canvas,
            self.variable,
            *self.cities,
            command=self.display_selected
        )
        self.dropdown.config(bg="black", fg="white", bd=8, highlightthickness=0, width=10, font=("Arial", 19, "bold"))
        self.dropdown.place(x=240, y=640)

    def display_selected(self, choice):
        global goalCity
        goalCity = self.variable.get()

    def reset(self):
        global startNode, goalNode, goalCity, mode
        startNode = 0
        goalNode = 0
        goalCity = ""
        mode = False
        self.status['text'] = 'Not Visited'
        self.variable.set(self.cities[0])
        self.reset_colors()

    def reset_colors(self):
        ovals = self.make_canvas.find_withtag("nodeBtn")
        for oval in ovals:
            self.make_canvas.itemconfig(oval, fill="gray")
        for label, widget in self.make_canvas.children.items():
            if label[1] == 'l':
                widget.config(bg="gray")

    def initialize_vertex(self):  # Vertex with connection make
        for i in range(31):
            self.total_nodes.append(i)
            self.total_cities.append(i)

            # LEVEL 0

        self.total_nodes[0] = self.make_canvas.create_oval(40, 330, 110, 370, width=3, tags=("nodeBtn",))  # Arad
        print(self.make_canvas.itemcget(self.total_nodes[0], "tags"))
        self.make_canvas.tag_bind("nodeBtn", "<Button-1>", self.clicked)

        self.total_cities[0] = Label(self.make_canvas, text="Arad", bg="gray", fg="white",
                                     font=("Arial", 8, "italic"))
        # self.total_cities[0].bind("<Button-1>", clicked)

        self.total_cities[0].place(x=60, y=340)
        # LEVEL 1

        self.total_nodes[1] = self.make_canvas.create_oval(120, 260, 190, 300, width=3, tags=("nodeBtn",))  # Zerind
        self.total_cities[1] = Label(self.make_canvas, text="Zerind", bg="gray", fg="white",
                                     font=("Arial", 8, "italic"))
        self.total_cities[1].place(x=135, y=270)
        lbl = StringVar()
        lbl.set(".!canvas.!label3")
        # print('city1: ', lbl.cget("bg"))

        self.total_nodes[2] = self.make_canvas.create_oval(120, 330, 190, 370, width=3, tags=("nodeBtn",))  # Sibiu
        self.total_cities[2] = Label(self.make_canvas, text="Sibiu", bg="gray", fg="white", font=("Arial", 8, "italic"))
        self.total_cities[2].place(x=138, y=340)

        self.total_nodes[3] = self.make_canvas.create_oval(120, 400, 190, 440, width=3,
                                                           tags=("nodeBtn",))  # Temisora
        # self.make_canvas.tag_bind("temisoraBtn", "<Button-1>", self.clicked)
        self.total_cities[3] = Label(self.make_canvas, text="Temisora", bg="gray", fg="white",
                                     font=("Arial", 8, "italic"))
        self.total_cities[3].place(x=130, y=410)

        # LEVEL 2

        self.total_nodes[4] = self.make_canvas.create_oval(200, 210, 270, 250, width=3,
                                                           tags=("nodeBtn",))  # Zerind -> Oradia
        self.total_cities[4] = Label(self.make_canvas, text="Oradea", bg="gray", fg="white",
                                     font=("Arial", 8, "italic"))
        self.total_cities[4].place(x=215, y=220)

        self.total_nodes[5] = self.make_canvas.create_oval(200, 290, 270, 330, width=3,
                                                           tags=("nodeBtn",))  # Sibiu -> Rimnicu
        self.total_cities[5] = Label(self.make_canvas, text="Rimnicu", bg="gray", fg="white",
                                     font=("Arial", 8, "italic"))
        self.total_cities[5].place(x=210, y=300)

        self.total_nodes[6] = self.make_canvas.create_oval(200, 370, 270, 410, width=3,
                                                           tags=("nodeBtn",))  # Sibiu -> Fagaras
        self.total_cities[6] = Label(self.make_canvas, text="Fagaras", bg="gray", fg="white",
                                     font=("Arial", 8, "italic"))
        self.total_cities[6].place(x=210, y=380)

        self.total_nodes[7] = self.make_canvas.create_oval(200, 450, 270, 490, width=3,
                                                           tags=("nodeBtn",))  # Temisora -> Lugoj
        self.total_cities[7] = Label(self.make_canvas, text="Lugoj", bg="gray", fg="white", font=("Arial", 8, "italic"))
        self.total_cities[7].place(x=215, y=460)
        # LEVEL 3

        self.total_nodes[8] = self.make_canvas.create_oval(280, 160, 350, 200, width=3,
                                                           tags=("nodeBtn",))  # Oradia -> Sibiu
        self.total_cities[8] = Label(self.make_canvas, text="Sibiu", bg="gray", fg="white", font=("Arial", 8, "italic"))
        self.total_cities[8].place(x=300, y=170)

        self.total_nodes[9] = self.make_canvas.create_oval(280, 260, 350, 300, width=3,
                                                           tags=("nodeBtn",))  # Rimnicu -> Craiova
        self.total_cities[9] = Label(self.make_canvas, text="Craiova", bg="gray", fg="white",
                                     font=("Arial", 8, "italic"))
        self.total_cities[9].place(x=293, y=270)

        self.total_nodes[10] = self.make_canvas.create_oval(280, 330, 350, 370, width=3,
                                                            tags=("nodeBtn",))  # Rimnicu -> Pitesti
        self.total_cities[10] = Label(self.make_canvas, text="Pitesti", bg="gray", fg="white",
                                      font=("Arial", 8, "italic"))
        self.total_cities[10].place(x=295, y=340)

        self.total_nodes[11] = self.make_canvas.create_oval(280, 400, 350, 440, width=3,
                                                            tags=("nodeBtn",))  # Fagaras -> Bucharest***
        self.total_cities[11] = Label(self.make_canvas, text="Bucharest", bg="gray", fg="white",
                                      font=("Arial", 8, "italic"))
        self.total_cities[11].place(x=288, y=410)

        self.total_nodes[12] = self.make_canvas.create_oval(280, 500, 350, 540, width=3,
                                                            tags=("nodeBtn",))  # Lugoj -> Mehadia
        self.total_cities[12] = Label(self.make_canvas, text="Mehadia", bg="gray", fg="white",
                                      font=("Arial", 8, "italic"))
        self.total_cities[12].place(x=290, y=510)

        # LEVEL 4

        self.total_nodes[13] = self.make_canvas.create_oval(360, 120, 430, 160, width=3,
                                                            tags=("nodeBtn",))  # Sibiu -> Fagaras
        self.total_cities[13] = Label(self.make_canvas, text="Fagaras", bg="gray", fg="white",
                                      font=("Arial", 8, "italic"))
        self.total_cities[13].place(x=372, y=130)

        self.total_nodes[14] = self.make_canvas.create_oval(360, 190, 430, 230, width=3,
                                                            tags=("nodeBtn",))  # sibiu -> Rimnicu
        self.total_cities[14] = Label(self.make_canvas, text="Rimnicu", bg="gray", fg="white",
                                      font=("Arial", 8, "italic"))
        self.total_cities[14].place(x=372, y=200)

        self.total_nodes[15] = self.make_canvas.create_oval(360, 260, 430, 300, width=3,
                                                            tags=("nodeBtn",))  # Craiova -> Pitesti
        self.total_cities[15] = Label(self.make_canvas, text="Pitesti", bg="gray", fg="white",
                                      font=("Arial", 8, "italic"))
        self.total_cities[15].place(x=375, y=270)

        self.total_nodes[16] = self.make_canvas.create_oval(360, 330, 430, 370, width=3,
                                                            tags=("nodeBtn",))  # Pitesti -> Bucharest***
        self.total_cities[16] = Label(self.make_canvas, text="Bucharest", bg="gray", fg="white",
                                      font=("Arial", 8, "italic"))
        self.total_cities[16].place(x=367, y=340)

        self.total_nodes[17] = self.make_canvas.create_oval(360, 500, 430, 540, width=3,
                                                            tags=("nodeBtn",))  # Mehadia -> Dobreta
        self.total_cities[17] = Label(self.make_canvas, text="Dobreta", bg="gray", fg="white",
                                      font=("Arial", 8, "italic"))
        self.total_cities[17].place(x=370, y=510)

        # LEVEL 5

        self.total_nodes[18] = self.make_canvas.create_oval(440, 80, 510, 120, width=3,
                                                            tags=("nodeBtn",))  # Fagaras -> Bucharest***
        self.total_cities[18] = Label(self.make_canvas, text="Bucharest", bg="gray", fg="white",
                                      font=("Arial", 8, "italic"))
        self.total_cities[18].place(x=447, y=90)

        self.total_nodes[19] = self.make_canvas.create_oval(440, 150, 510, 190, width=3,
                                                            tags=("nodeBtn",))  # Rimnicu -> Craiova
        self.total_cities[19] = Label(self.make_canvas, text="Craiova", bg="gray", fg="white",
                                      font=("Arial", 8, "italic"))
        self.total_cities[19].place(x=453, y=160)

        self.total_nodes[20] = self.make_canvas.create_oval(440, 210, 510, 250, width=3,
                                                            tags=("nodeBtn",))  # Rimnicu -> Pitesti
        self.total_cities[20] = Label(self.make_canvas, text="Pitesti", bg="gray", fg="white",
                                      font=("Arial", 8, "italic"))
        self.total_cities[20].place(x=455, y=220)

        self.total_nodes[21] = self.make_canvas.create_oval(440, 280, 510, 320, width=3,
                                                            tags=("nodeBtn",))  # Pitesti -> Bucharest***
        self.total_cities[21] = Label(self.make_canvas, text="Bucharest", bg="gray", fg="white",
                                      font=("Arial", 8, "italic"))
        self.total_cities[21].place(x=447, y=290)

        self.total_nodes[22] = self.make_canvas.create_oval(440, 500, 510, 540, width=3,
                                                            tags=("nodeBtn",))  # Dobreta -> Craiova
        self.total_cities[22] = Label(self.make_canvas, text="Craiova", bg="gray", fg="white",
                                      font=("Arial", 8, "italic"))
        self.total_cities[22].place(x=450, y=510)

        # LEVEL 6

        self.total_nodes[23] = self.make_canvas.create_oval(520, 150, 590, 190, width=3,
                                                            tags=("nodeBtn",))  # Craiova -> Pitesti
        self.total_cities[23] = Label(self.make_canvas, text="Pitesti", bg="gray", fg="white",
                                      font=("Arial", 8, "italic"))
        self.total_cities[23].place(x=535, y=160)

        self.total_nodes[24] = self.make_canvas.create_oval(520, 210, 590, 250, width=3,
                                                            tags=("nodeBtn",))  # Pitesti -> Bucharest***
        self.total_cities[24] = Label(self.make_canvas, text="Bucharest", bg="gray", fg="white",
                                      font=("Arial", 8, "italic"))
        self.total_cities[24].place(x=527, y=220)

        self.total_nodes[25] = self.make_canvas.create_oval(520, 440, 590, 480, width=3,
                                                            tags=("nodeBtn",))  # Craiova -> Rimnicu
        self.total_cities[25] = Label(self.make_canvas, text="Rimnicu", bg="gray", fg="white",
                                      font=("Arial", 8, "italic"))
        self.total_cities[25].place(x=530, y=450)

        self.total_nodes[26] = self.make_canvas.create_oval(520, 500, 590, 540, width=3,
                                                            tags=("nodeBtn",))  # Craiova -> Pitesti
        self.total_cities[26] = Label(self.make_canvas, text="Pitesti", bg="gray", fg="white",
                                      font=("Arial", 8, "italic"))
        self.total_cities[26].place(x=535, y=510)

        # LEVEL 7

        self.total_nodes[27] = self.make_canvas.create_oval(600, 150, 670, 190, width=3,
                                                            tags=("nodeBtn",))  # Pitesti -> Bucharest***
        self.total_cities[27] = Label(self.make_canvas, text="Bucharest", bg="gray", fg="white",
                                      font=("Arial", 8, "italic"))
        self.total_cities[27].place(x=607, y=160)

        self.total_nodes[28] = self.make_canvas.create_oval(600, 440, 670, 480, width=3,
                                                            tags=("nodeBtn",))  # Rimnicu -> Pitesti
        self.total_cities[28] = Label(self.make_canvas, text="Pitesti", bg="gray", fg="white",
                                      font=("Arial", 8, "italic"))
        self.total_cities[28].place(x=615, y=450)

        self.total_nodes[29] = self.make_canvas.create_oval(600, 500, 670, 540, width=3,
                                                            tags=("nodeBtn",))  # Pitesti -> Bucharest***
        self.total_cities[29] = Label(self.make_canvas, text="Bucharest", bg="gray", fg="white",
                                      font=("Arial", 8, "italic"))
        self.total_cities[29].place(x=607, y=510)

        # LEVEL 8

        self.total_nodes[30] = self.make_canvas.create_oval(680, 440, 750, 480, width=3,
                                                            tags=("nodeBtn",))  # Pitesti -> Bucharest***
        self.total_cities[30] = Label(self.make_canvas, text="Bucharest", bg="gray", fg="white",
                                      font=("Arial", 8, "italic"))
        self.total_cities[30].place(x=688, y=450)

        ############################################################################################
        # LEVEL 1
        self.draw_connector(0, 1)
        self.draw_connector(0, 2)
        self.draw_connector(0, 3)
        self.connect_connector(0, 1, 2, 3)

        # LEVEL 2
        self.draw_connector(1, 4)
        self.connect_connector(1, 4)

        self.draw_connector(2, 5)
        self.draw_connector(2, 6)
        self.connect_connector(2, 5, 6)

        self.draw_connector(3, 7)
        self.connect_connector(3, 7)

        # LEVEL 3
        self.draw_connector(4, 8)
        self.draw_connector(5, 9)
        self.draw_connector(5, 10)
        self.draw_connector(6, 11)
        self.draw_connector(7, 12)

        self.connect_connector(4, 8)
        self.connect_connector(5, 9, 10)
        self.connect_connector(6, 11)
        self.connect_connector(7, 12)

        # LEVEL 4
        self.draw_connector(8, 13)
        self.draw_connector(8, 14)
        self.draw_connector(9, 15)
        self.draw_connector(10, 16)
        self.draw_connector(12, 17)

        self.connect_connector(8, 13, 14)
        self.connect_connector(9, 15)
        self.connect_connector(10, 16)
        self.connect_connector(12, 17)

        # LEVEL 5
        self.draw_connector(13, 18)
        self.draw_connector(14, 19)
        self.draw_connector(14, 20)
        self.draw_connector(15, 21)
        self.draw_connector(17, 22)

        self.connect_connector(13, 18)
        self.connect_connector(14, 19, 20)
        self.connect_connector(15, 21)
        self.connect_connector(17, 22)

        # LEVEL 6
        self.draw_connector(19, 23)
        self.draw_connector(20, 24)
        self.draw_connector(22, 25)
        self.draw_connector(22, 26)

        self.connect_connector(19, 23)
        self.connect_connector(20, 24)
        self.connect_connector(22, 25, 26)

        # LEVEL 7
        self.draw_connector(23, 27)
        self.draw_connector(25, 28)
        self.draw_connector(26, 29)

        self.connect_connector(23, 27)
        self.connect_connector(25, 28)
        self.connect_connector(26, 29)

        # LEVEL 8
        self.draw_connector(28, 30)
        self.connect_connector(28, 30)

        print(self.vertex_connections)

    def draw_connector(self, index1, index2):  # Down node connection make
        coord1 = self.make_canvas.coords(self.total_nodes[index1])  # Source node coordinates
        coord2 = self.make_canvas.coords(self.total_nodes[index2])  # Destination node coordinates
        x_start = (coord1[0] + coord1[2]) / 2  # Connector line start_x
        end_x = (coord2[0] + coord2[2]) / 2  # Connector line end_x
        y_start = (coord1[1] + coord1[3]) / 2  # Connector line start_y
        y_end = (coord2[1] + coord2[3]) / 2  # Connector line end_y
        self.make_canvas.create_line(x_start + 34, y_start + 5, end_x - 34, y_end - 5, width=3)

    def connect_connector(self, source, connector1=None, connector2=None,
                          connector3=None):  # All about node data collect and store
        temp = []
        temp.append(self.total_nodes[source])

        if connector1:
            temp.append(self.total_nodes[connector1])
        else:
            temp.append(None)

        if connector2:
            temp.append(self.total_nodes[connector2])
        else:
            temp.append(None)

        if connector3:
            #   print('abc', self.total_circle[connector3])
            temp.append(self.total_nodes[connector3])
        else:
            temp.append(None)
        if source == 22:
            print('temp', temp)
        self.vertex_connections.append(temp)

    def mode_start(self):
        global mode
        mode = True
        self.goal_btn.config(relief=RAISED, bg="black", fg="white")
        self.start_btn.config(relief=SUNKEN, bg="white", fg="black")

    def mode_goal(self):
        global mode
        mode = False
        self.start_btn.config(relief=RAISED, bg="black", fg="white")
        self.goal_btn.config(relief=SUNKEN, bg="white", fg="black")

    def binary_search(self, start, end, find):  # Binary search algorithm use here
        while start <= end:
            mid = int((start + end) / 2)
            if self.vertex_connections[mid][0] == find:
                return self.vertex_connections[mid]
            elif self.vertex_connections[mid][0] < find:
                start = mid + 1
            else:
                end = mid - 1
        return -1

    def bfs(self):
        self.queue_bfs.clear()
        #self.reset_colors()
        global startNode, goalNode, goalCity
        print('startNode: ', startNode, 'GoalNode: ', goalNode)
        start = startNode
        goal = goalNode
        try:
            for i in range(23):
                if self.vertex_connections[i][0] == startNode:
                    start = i
                    break
            print('start: ', start)
            print('bfs vector store val: ', self.vertex_connections[start][0])
            self.queue_bfs.append(self.vertex_connections[start][0])
            while self.queue_bfs:
                temp = self.binary_search(0, 22, self.queue_bfs[0])
                # print('temp: ', temp)
                if temp != -1:
                    if temp[1]:
                        self.queue_bfs.append(temp[1])
                    if temp[2]:
                        self.queue_bfs.append(temp[2])
                    if temp[3]:
                        self.queue_bfs.append(temp[3])
                take_vertex = self.queue_bfs.pop(0)
                self.status['text'] = f"Current City: {self.total_cities[take_vertex - 1].cget('text')}"
                print(self.total_nodes[take_vertex - 1], self.total_cities[take_vertex - 1].cget('text'))
                self.total_cities[take_vertex - 1].config(bg="purple")
                self.make_canvas.itemconfig(take_vertex, fill="purple")
                self.window.update()
                time.sleep(0.3)
                if take_vertex == goal:
                    self.status['text'] = "Goal Reached"
                    break
                #print('goalCity: ', goalCity)
                if self.total_cities[take_vertex - 1].cget("text") == goalCity:
                    self.status['text'] = "Goal Reached"
                    break
            if self.status['text'] != "Goal Reached":
                self.status['text'] = "All node Visited"
        except:
            print("Force stop error")

    def dfs(self):
        #self.reset_colors()
        self.stack_dfs.clear()
        global startNode, goalNode, goalCity
        start = startNode
        goal = goalNode
        try:
            for i in range(23):
                if self.vertex_connections[i][0] == startNode:
                    start = i
                    break
            print('start: ', start, ' goal: ', goal)
            print(f'self.vertex_store[start][0]: {self.vertex_connections[start][0]}')
            self.stack_dfs.append(self.vertex_connections[start][0])
            while self.stack_dfs:
                take_vertex = self.stack_dfs.pop()
                print(f"take_vertex: {take_vertex}")
                self.status['text'] = f"Current City: {self.total_cities[take_vertex - 1].cget('text')}"
                print(self.total_cities[take_vertex - 1].cget("text"))
                self.total_cities[take_vertex - 1].config(bg="blue")
                self.make_canvas.itemconfig(take_vertex, fill="blue")
                self.window.update()
                time.sleep(0.3)
                temp = self.binary_search(0, 22, take_vertex)
                if temp != -1:
                    if temp[1]:
                        self.stack_dfs.append(temp[1])
                    if temp[2]:
                        self.stack_dfs.append(temp[2])
                    if temp[3]:
                        self.stack_dfs.append(temp[3])
                if take_vertex == goal:
                    print(f"take_vertex:{take_vertex}, goal:{goal}")
                    self.status['text'] = "Goal Reached"
                    break
                if self.total_cities[take_vertex - 1].cget("text") == goalCity:
                    self.status['text'] = "Goal Reached"
                    break
            if self.status['text'] != "Goal Reached":
                self.status['text'] = "All node Visited"
        except:
            print("Force stop error")


if __name__ == '__main__':
    window = Tk()
    window.title("Graph Traversal Visualizer")
    window.geometry("400x900")
    window.maxsize(800, 900)
    window.minsize(800, 900)
    window.config(bg="chocolate")
    window.wm_attributes('-transparentcolor', window['bg'])
    GraphTraversal(window)
    window.mainloop()