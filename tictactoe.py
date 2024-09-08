import tkinter
import tkinter as tk

i = 0   # X, O
scores = [0, 0]
buttons = []

winningScores = (111, 111000, 111000000, 1001001, 10010010, 100100100, 1010100, 100010001)  # Tuple of winning scores
adderDict = {  # Dictionary for the key of each field
            "1":          1,
            "2":         10,
            "3":        100,
            "4":       1000,
            "5":      10000,
            "6":     100000,
            "7":    1000000,
            "8":   10000000,
            "9":  100000000
}

#-----------------------------------------------------------------------------------------------------------------------

def determinePlayer():  # Flip-flop to the players take turns
    global i
    if i % 2 == 0:
        char = "X"
    else:
        char = "O"
    i += 1
    return char


def calcScores(player, key):
    """Adds the results to scores"""
    if player == "X":  # Determines what player is playing right now
        scores[0] += adderDict[str(key)]  # Adds their score by grabbing the value from the dictionary adderDict
    if player == "O":
        scores[1] += adderDict[str(key)]


def winnerCalc(player):  # Calculates winner score
    winnerDetermined = 0
    n = None

    if player == "X":
        for _ in range(len(winningScores)):  # Sets up for loop in the range of the length of the winningScores
            n = str(scores[0] + winningScores[_])  # Defines n to be the sum of an element in winningScores + score
            if n.count("2") >= 3:  # If sum(n) has more than or equal to 3 2's inside that player has won the game
                winnerDetermined = 1
    if player == "O":
        for _ in range(len(winningScores)):
            n = str(scores[1] + winningScores[_])
            if n.count("2") >= 3:
                winnerDetermined = 2
    return winnerDetermined

def closingRound(input):
    x = False
    winningText = tk.StringVar()

    if input != 0 or (len(buttons) >= 9 and input == 0):  # Disables buttons on tie and win
        button0["state"] = "disabled"
        button1["state"] = "disabled"
        button2["state"] = "disabled"
        button3["state"] = "disabled"
        button4["state"] = "disabled"
        button5["state"] = "disabled"
        button6["state"] = "disabled"
        button7["state"] = "disabled"
        button8["state"] = "disabled"
        x = True

    if len(buttons) >= 9 and input == 0:
        winningText.set("It's a tie! Restart?")
        x = True
    if input == 1:
        winningText.set("X won! Restart?")
        x = True
    if input == 2:
        winningText.set("O won! Restart?")
        x = True

    if x == True:  # Creates the window for the prompt
        prompt = tkinter.Toplevel(root)
        prompt.title("Exit?")
        prompt.geometry("300x125")
        prompt.resizable(False, False)
        prompt.configure(bg="#24273a")

        promptLabel = tk.Label(prompt, textvariable=winningText, font=("Gabarito Regular", 20), borderwidth=0, bg="#24273a", fg="#b8c0e0")
        promptButton = tk.Button(prompt, text="Restart", width=9, font=("Gabarito Regular", 15), borderwidth=0, activebackground="#3c3c4a", activeforeground="#b8c0e0", bg="#363a4f", fg="#b8c0e0", command=lambda: [promptButtonHandling(), prompt.destroy()])
        promptLabel.pack(pady=10)
        promptButton.pack(pady=5)


def promptButtonHandling():  # Resets everything in the game
    global i
    global scores
    global buttons

    i = 0
    scores = [0, 0]
    buttons = []

    button0Var.set("_")
    button1Var.set("_")
    button2Var.set("_")
    button3Var.set("_")
    button4Var.set("_")
    button5Var.set("_")
    button6Var.set("_")
    button7Var.set("_")
    button8Var.set("_")

    button0["state"] = "normal"
    button1["state"] = "normal"
    button2["state"] = "normal"
    button3["state"] = "normal"
    button4["state"] = "normal"
    button5["state"] = "normal"
    button6["state"] = "normal"
    button7["state"] = "normal"
    button8["state"] = "normal"

def game(buttonVar, buttonValue):  # Flow
    global buttons
    if buttonValue not in buttons:
        buttons.append(buttonValue)
        currentPlayer = determinePlayer()
        calcScores(currentPlayer, buttonValue)
        buttonVar.set(currentPlayer)
        calc = winnerCalc(currentPlayer)
        closingRound(calc)

#-----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    root = tk.Tk()  # Creates tkinter object thing
    root.title("Mimi's Tic-Tac-Toe")  # Sets the title of the window
    root.resizable(False, False)  # Forbids the window from changing in size
    root.geometry("600x600")  # Sets the window size
    root.configure(bg="#24273a")  # Sets the background color of the window

    root.rowconfigure((0, 1, 2), weight=1)  # Creates grid for the buttons
    root.columnconfigure((0, 1, 2), weight=1)

#-----------------------------------------------------------------------------------------------------------------------

    button0Var = tk.StringVar(root, "_")  # Creates StringVar which can be used to dynamically change the text
    button0 = tk.Button(root, textvariable=button0Var, font=("Cascadia Mono", 60), borderwidth=0,
                        activebackground="#3c3c4a", activeforeground="#b8c0e0", bg="#363a4f", fg="#b8c0e0",
                        command=lambda: game(button0Var, "1"))  # Attributes of the buttons as well as what function gets called when the button gets pressed
    button0.grid(row=0, column=0, sticky="nsew", pady=5, padx=5)  # Places the button into the grid created above with some other stuff

    button1Var = tk.StringVar(root, "_")
    button1 = tk.Button(root, textvariable=button1Var, font=("Cascadia Mono", 60), borderwidth=0,
                        activebackground="#3c3c4a", activeforeground="#b8c0e0", bg="#363a4f", fg="#b8c0e0",
                        command=lambda: game(button1Var, "2"))
    button1.grid(row=0, column=1, sticky="nsew", pady=5, padx=5)

    button2Var = tk.StringVar(root, "_")
    button2 = tk.Button(root, textvariable=button2Var, font=("Cascadia Mono", 60), borderwidth=0,
                        activebackground="#3c3c4a", activeforeground="#b8c0e0", bg="#363a4f", fg="#b8c0e0",
                        command=lambda: game(button2Var, "3"))
    button2.grid(row=0, column=2, sticky="nsew", pady=5, padx=5)

    button3Var = tk.StringVar(root, "_")
    button3 = tk.Button(root, textvariable=button3Var, font=("Cascadia Mono", 60), borderwidth=0,
                        activebackground="#3c3c4a", activeforeground="#b8c0e0", bg="#363a4f", fg="#b8c0e0",
                        command=lambda: game(button3Var, "4"))
    button3.grid(row=1, column=0, sticky="nsew", pady=5, padx=5)

    button4Var = tk.StringVar(root, "_")
    button4 = tk.Button(root, textvariable=button4Var, font=("Cascadia Mono", 60), borderwidth=0,
                        activebackground="#3c3c4a", activeforeground="#b8c0e0", bg="#363a4f", fg="#b8c0e0",
                        command=lambda: game(button4Var, "5"))
    button4.grid(row=1, column=1, sticky="nsew", pady=5, padx=5)

    button5Var = tk.StringVar(root, "_")
    button5 = tk.Button(root, textvariable=button5Var, font=("Cascadia Mono", 60), borderwidth=0,
                        activebackground="#3c3c4a", activeforeground="#b8c0e0", bg="#363a4f", fg="#b8c0e0",
                        command=lambda: game(button5Var, "6"))
    button5.grid(row=1, column=2, sticky="nsew", pady=5, padx=5)

    button6Var = tk.StringVar(root, "_")
    button6 = tk.Button(root, textvariable=button6Var, font=("Cascadia Mono", 60), borderwidth=0,
                        activebackground="#3c3c4a", activeforeground="#b8c0e0", bg="#363a4f", fg="#b8c0e0",
                        command=lambda: game(button6Var, "7"))
    button6.grid(row=2, column=0, sticky="nsew", pady=5, padx=5)

    button7Var = tk.StringVar(root, "_")
    button7 = tk.Button(root, textvariable=button7Var, font=("Cascadia Mono", 60), borderwidth=0,
                        activebackground="#3c3c4a", activeforeground="#b8c0e0", bg="#363a4f", fg="#b8c0e0",
                        command=lambda: game(button7Var, "8"))
    button7.grid(row=2, column=1, sticky="nsew", pady=5, padx=5)

    button8Var = tk.StringVar(root, "_")
    button8 = tk.Button(root, textvariable=button8Var, font=("Cascadia Mono", 60), borderwidth=0,
                        activebackground="#3c3c4a", activeforeground="#b8c0e0", bg="#363a4f", fg="#b8c0e0",
                        command=lambda: game(button8Var, "9"))
    button8.grid(row=2, column=2, sticky="nsew", pady=5, padx=5)

    root.mainloop()  # Mainloop which is required for this all to work

#-----------------------------------------------------------------------------------------------------------------------