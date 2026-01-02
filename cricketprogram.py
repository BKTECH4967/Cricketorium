from tkinter import *
from tkinter.ttk import Combobox, Style
from tkinter import ttk
from tkinter import messagebox as mb

# Variables
balls_list = []
fontname = "Times New Roman"
wides = 1
balls = 0
overs = 0
over_limit = 5

over_balls = 6
total_balls = 0
over_runs = 0
total_runs = 0

batsman = "" # Current Batsman
batsman_playing_list = []
batsman1 = ""
batsman1_score = 0
batsman2 = ""
batsman2_score = 0

bowler = ""
bowler_score = 0
bowler_names = [
    "Bharathi Kannan",
    "Madavan",
    "Balan",
    "S.N. Bala",
    "Chandru",
    "Ramesh",
    "Subbu Ram",
    "Vijay",
    "Mahanth"
]

def MainWindow( para : str ):
    global root, overs, wides, bowler_lbl, batsman1, batsman2, bat1_radio, bat2_radio, bat1var, bat2var
    global batsman1_score, batsman2_score

    if para == "first":
        app = Tk()
        app.title( "Cricketorium - Cricket Over Counter" )
        
        # Centering the Window
        w = 773
        h = 450

        ww = app.winfo_screenwidth()
        hh = app.winfo_screenheight()

        x = ( ww // 2 ) - ( w // 2 )
        y = ( hh // 2 ) - ( h // 2 )

        app.geometry( f"{w}x{h}+{x}+{y}" )

        # 0-1, 1-2, 2-3, 3-4, 4-5, 5-6
        #--------------------------------- Functions ---------------------------------#
        def Wicket( type : str ):
            mb.showinfo( "Cricketorium", f"{batsman.capitalize()} is out by {type}!\n" )
            Submit( "Wk" )
            EntryWindow( "wicket" )

        def Submit( value : str | int ):
            global balls, total_runs, balls_list, overs, over_runs, over_balls, total_balls, wides, batsman1_score, batsman2_score

            if overs <= over_limit:
                if value != "Wd" and value != "Nb":
                    if str( value ).isdigit():
                        if value == 1 or value == 3:
                            if batvar.get() == ( batsman_playing_list.index( batsman1 ) + 1 ):
                                batvar.set( 2 )
                                batsman1_score += value
                                change_batsman()
                            
                            else:
                                batvar.set( 1 )
                                batsman2_score += value
                                change_batsman()
                        
                        if batvar.get() == ( batsman_playing_list.index( batsman1 ) + 1 ):
                            batsman1_score += value
                        
                        else:
                            batsman2_score += value
                        
                        total_runs += value
                        over_runs += value
                    
                    print( batsman1_score )
                    print( batsman2_score )
                    
                    balls_list[balls]["text"] = value
                    balls += 1

                    if balls >= over_balls:
                        balls = 0
                        overs += 1
                        mb.showinfo( "Cricketorium", f"Over {overs} was completed!\nOver Runs : {over_runs}\nTotal Runs : {total_runs}" )
                        print( batsman_playing_list )
                        for ball in balls_list:
                            ball.destroy()
                        
                        balls_list = []
                        for i in range( 6 ):
                            ball1_lbl = Label( master=runs_f, text="0", font=( fontname, 18 ) )
                            ball1_lbl.grid( row=0, column=i, padx=35, pady=15 )
                            total_runs = i
                            balls_list.append( ball1_lbl )
                        
                        over_runs = 0
                        if batvar.get() == ( batsman_playing_list.index( batsman1 ) + 1 ):
                            batvar.set( 2 )
                            change_batsman()
                        
                        else:
                            batvar.set( 1 )
                            change_batsman()
                        
                        EntryWindow( "over_complete" )
                        
                elif value == "Wd" or value == "Nb":
                    balls_list[balls]["text"] = value
                    ball1_lbl = Label( master=runs_f, text="0", font=( fontname, 18 ) )
                    ball1_lbl.grid( row=0, column=total_balls+wides, padx=35, pady=15 )
                    balls_list.append( ball1_lbl )
                    balls += 1
                    total_runs += 1
                    over_runs += 1
                    over_balls += 1
                    wides += 1

        def change_batsman():
            global batsman
            batsman = batsman_playing_list[batvar.get()-1]
        
        def set_batsman1():
            global batsman1
            batsman1 = bat1var.get()
            bat1_radio.config( text=batsman1 )
            batsman_playing_list.append( batsman1 )
        
        def set_batsman2():
            global batsman2
            batsman2 = bat2var.get()
            bat2_radio.config( text=batsman2 )
            batsman_playing_list.append( batsman2 )
        
        def change_bowler():
            s = Style( app )
            s.theme_use( "clam" )
            
            def register():
                global bowler
                bowler = ddl.get()
                bowler_lbl.config( text=bowler )
                ddl.destroy()

            ddlvar = StringVar()
            ddlvar.set( bowler )
            
            ddl = Combobox( master=batball_f, state="r", width=10, values=bowler_names, textvariable=ddlvar, font=( fontname, 13 ) )
            ddl.grid( row=1, column=3, padx=15, pady=( 0, 15 ) )
            balltitle_lbl.bind( "<1>", lambda e: register() )
        
        #--------------------------------- Widgets ---------------------------------#
        # Batsman Selecting Frame
        batball_f = Frame( app )
        batball_f.pack( side=TOP, fill=X )

        s = Style( app )
        s.theme_use( "clam" )

        # Widgets
        battitle_lbl = Label( master=batball_f, text="Batsmans", font=( fontname, 15 ) )
        battitle_lbl.grid( row=0, column=0, columnspan=2, padx=15, pady=(15, 0) )

        batvar = IntVar()
        batvar.set( 1 )
        
        bat1_radio = Radiobutton( master=batball_f, text=batsman1, indicatoron=False, value=1, variable=batvar, font=( fontname, 15 ), command=change_batsman )
        bat1_radio.grid( row=1, column=0, padx=15, pady=(0, 15) )
        
        bat2_radio = Radiobutton( master=batball_f, text=batsman2, indicatoron=False, value=2, variable=batvar, font=( fontname, 15 ), command=change_batsman )
        bat2_radio.grid( row=1, column=1, padx=15, pady=(0, 15) )

        chum = Label( master=batball_f, text="      ", fg="SystemButtonFace", font=( fontname, 15 ) )
        chum.grid( row=0, column=2, padx=15, pady=(15, 0) )

        balltitle_lbl = Label( master=batball_f, text="Bowler", font=( fontname, 15 ) )
        balltitle_lbl.grid( row=0, column=3, padx=15, pady=(15, 0) )

        bowler_lbl = Label( master=batball_f, text=bowler, font=( fontname, 15 ) )
        bowler_lbl.grid( row=1, column=3, padx=15, pady=(0, 15) )
        bowler_lbl.bind( "<Double-1>", lambda e: change_bowler() )

        bat1var = StringVar()
        bat1var.set( batsman1 )

        batsman1_ddl = Combobox( master=batball_f, state="r", width=15, textvariable=bat1var, values=bowler_names, font=( fontname, 15 ) )
        batsman1_ddl.grid( row=0, column=4, padx=15, pady=15 )
        batsman1_ddl.bind( "<<ComboboxSelected>>", lambda e: set_batsman1() )

        bat2var = StringVar()
        bat2var.set( batsman2 )

        batsman2_ddl = Combobox( master=batball_f, state="r", width=15, textvariable=bat2var, values=bowler_names, font=( fontname, 15 ) )
        batsman2_ddl.grid( row=1, column=4, padx=15, pady=15 )
        batsman2_ddl.bind( "<<ComboboxSelected>>", lambda e: set_batsman2() )

        # Runs Frame
        runs_f = Frame( app )
        runs_f.pack( side=TOP, fill=X )
        
        # Widgets
        for i in range( 6 ):
            global total_balls
            ball1_lbl = Label( master=runs_f, text="0", font=( fontname, 18 ) )
            ball1_lbl.grid( row=0, column=i, padx=35, pady=15 )
            total_balls = i
            balls_list.append( ball1_lbl )
        
        # Extras Frame
        extras_f = Frame( app )
        extras_f.pack( side=BOTTOM, fill=X )

        # Wicket LabelFrame
        wicket_lb = LabelFrame( master=extras_f, text="Wicket", relief="ridge" )
        wicket_lb.grid( row=0, column=0, columnspan=8 )

        # Widgets of Wicket LabelFrame
        bowled_btn = Button( master=wicket_lb, text="Bowled", font=( fontname, 18 ), command=lambda : Wicket( "Bowled" ) )
        bowled_btn.grid( row=0, column=0, padx=15, pady=15 )

        lbw_btn = Button( master=wicket_lb, text="LBW", font=( fontname, 18 ), command=lambda : Wicket( "LBW" ) )
        lbw_btn.grid( row=0, column=1, padx=15, pady=15 )

        stumped_btn = Button( master=wicket_lb, text="Stumped", font=( fontname, 18 ), command=lambda : Wicket( "Stumped" ) )
        stumped_btn.grid( row=0, column=2, padx=15, pady=15 )

        runout_btn = Button( master=wicket_lb, text="Run Out", font=( fontname, 18 ), command=lambda : Wicket( "Run Out" ) )
        runout_btn.grid( row=0, column=3, padx=15, pady=15 )

        catch_btn = Button( master=wicket_lb, text="Catch", font=( fontname, 18 ), command=lambda : Wicket( "Catch" ) )
        catch_btn.grid( row=0, column=4, padx=15, pady=15 )

        retired_btn = Button( master=wicket_lb, text="Retired", font=( fontname, 18 ), command=lambda : Wicket( "Catch" ) )
        retired_btn.grid( row=0, column=5, padx=15, pady=15 )

        # Widgets of Common
        w1 = 2

        run0_btn = Button( master=extras_f, text="0", width=w1, font=( fontname, 18 ), command=lambda : Submit( 0 ) )
        run0_btn.grid( row=1, column=0, padx=15, pady=15 )

        run1_btn = Button( master=extras_f, text="1", width=w1, font=( fontname, 18 ), command=lambda : Submit( 1 ) )
        run1_btn.grid( row=1, column=1, padx=15, pady=15 )

        run2_btn = Button( master=extras_f, text="2", width=w1, font=( fontname, 18 ), command=lambda : Submit( 2 ) )
        run2_btn.grid( row=1, column=2, padx=15, pady=15 )

        run3_btn = Button( master=extras_f, text="3", width=w1, font=( fontname, 18 ), command=lambda : Submit( 3 ) )
        run3_btn.grid( row=1, column=3, padx=15, pady=15 )

        run4_btn = Button( master=extras_f, text="4", width=w1, font=( fontname, 18 ), command=lambda : Submit( 4 ) )
        run4_btn.grid( row=1, column=4, padx=15, pady=15 )

        run5_btn = Button( master=extras_f, text="5", width=w1, font=( fontname, 18 ), command=lambda : Submit( 5 ) )
        run5_btn.grid( row=1, column=5, padx=15, pady=15 )

        run6_btn = Button( master=extras_f, text="6", width=w1, font=( fontname, 18 ), command=lambda : Submit( 6 ) )
        run6_btn.grid( row=1, column=6, padx=15, pady=15 )

        run7_btn = Button( master=extras_f, text="7", width=w1, font=( fontname, 18 ), command=lambda : Submit( 7 ) )
        run7_btn.grid( row=1, column=7, padx=15, pady=15 )

        #---------------------------------#
        wide_btn = Button( master=extras_f, text="Wide", font=( fontname, 18 ), command=lambda : Submit( "Wd" ) )
        wide_btn.grid( row=2, column=0, columnspan=4, padx=15, pady=15 )

        noball_btn = Button( master=extras_f, text="No ball", font=( fontname, 18 ), command=lambda : Submit( "Nb" ) )
        noball_btn.grid( row=2, column=4, columnspan=4, padx=15, pady=15 )
        change_bowler()
        
        app.mainloop()

# Window for choosing the batsman
def EntryWindow( string : str ):
    global root, batsman1_name_ddl, bowler_lbl, bat1_radio, bat2_radio

    root = Tk()
    root.title( "Cricketorium" )
    root.attributes( "-toolwindow", True )

    # Centering the Window
    w = 323
    if string == "nothing":
        h = 260
    
    else:
        h = 200

    ww = root.winfo_screenwidth()
    hh = root.winfo_screenheight()

    x = ( ww // 2 ) - ( w // 2 )
    y = ( hh // 2 ) - ( h // 2 )

    root.geometry( f"{w}x{h}+{x}+{y}" )
    
    def Chumma():
        global batsman1, batsman2, bowler, batsman_playing_list
        batsman_playing_list = []
        batsman1 = batsman1_name_ddl.get()
        # batsman2 = batsman2_name_ddl.get()
        batsman_playing_list.append( batsman1 )
        batsman_playing_list.append( batsman2 )

        bowler = bowler_name_ddl.get()
        root.destroy()
        if string == "nothing":
            MainWindow( "first" )
        
        else:
            if string == "wicket":
                # if batsman == batsman1:
                #     bat1_radio.config( text=batsman1 )
                
                # else:
                #     bat2_radio.config( text=batsman2 )
                bat1_radio.config( text=batsman1 )# if batsman == batsman1 else bat2_radio.config( text=batsman2 )
                bat1var.set( batsman1 )# if batsman == batsman1 else bat2var.set( batsman2 )
                
                print( batsman1 )
                print( batsman2 )
                print( bowler )
            
            if string == "over_complete":
                bowler_lbl.config( text=bowler )
            
            MainWindow( "second" )
    
    # Variables
    s = Style( root )
    s.theme_use( "clam" )

    # Lists
    batsman_names = [
        "Bharathi Kannan",
        "Madavan",
        "Balan",
        "Chandru",
        "S.N. Bala",
        "Ramesh",
        "Subbu Ram",
        "Vijay",
        "Mahanth"
    ]
    bowler_names = [
        "Bharathi Kannan",
        "Madavan",
        "Balan",
        "S.N. Bala",
        "Ramesh",
        "Subbu Ram",
        "Vijay",
        "Mahanth"
    ]

    # Vars
    batsman1_var = StringVar()
    batsman1_var.set( "Batsman1" )
    
    batsman2_var = StringVar()
    batsman2_var.set( "Batsman2" )

    bowler_var = StringVar()
    bowler_var.set( bowler )

    # Widgets
    batsman1_name_ddl = Combobox( master=root, state="r", values=batsman_names, textvariable=batsman1_var, font=( fontname, 18 ) )
    batsman1_name_ddl.grid( row=0, column=0, padx=15, pady=15 )
    
    # batsman2_name_ddl = Combobox( master=root, state="r", values=batsman_names, textvariable=batsman2_var, font=( fontname, 18 ) )
    
    bowler_name_ddl = Combobox( master=root, state="r", values=bowler_names, textvariable=bowler_var, font=( fontname, 18 ) )
    bowler_name_ddl.grid( row=2, column=0, padx=15, pady=15 )

    confirm_btn = Button( master=root, text="Confirm", font=( fontname, 15 ), command=Chumma )
    confirm_btn.grid( row=3, column=0, padx=15, pady=15 )
    confirm_btn.bind( "<Return>", lambda e: Chumma() )

    if string == "wicket":
        if not balls >= over_balls:
            bowler_name_ddl["state"] = DISABLED
            batsman1_name_ddl["state"] = "r"
            # batsman2_name_ddl["state"] = "r"
        
        else:
            bowler_name_ddl["state"] = "r"
            batsman1_name_ddl["state"] = "r"
            # batsman2_name_ddl["state"] = "r"
    
    elif string == "over_complete":
        bowler_name_ddl["state"] = "r"
        batsman1_name_ddl["state"] = DISABLED
        # batsman2_name_ddl["state"] = DISABLED
    
    elif string == "nothing":
        # batsman2_name_ddl.grid( row=1, column=0, padx=15, pady=15 )
        bowler_name_ddl["state"] = "r"
        batsman1_name_ddl["state"] = "r"
        # batsman2_name_ddl["state"] = "r"

    root.mainloop()

# EntryWindow( "nothing" )
MainWindow( "first" )