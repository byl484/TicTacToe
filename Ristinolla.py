# TIE-02100 Johdatus ohjelmointiin
# 13.10 Graafisen käyttöliittymän suunnitteleminen ja toteuttaminen
# Ohjelma, joka tekee graafisen käyttöliittymän Ristinolla-pelille

from tkinter import *


class TicTacToe:
    def __init__(self):
        """
        Rakentaja-metodi tekee quit- ja reset-buttonit, sekä kutsuu
        create_board-metodia, joka tekee tyhjän pelilaudan.
        """
        self.__main_window = Tk()
        self.__main_window.title("Tic-Tac-Toe")

        self.__turn_count = 1
        self.__column = []
        self.__row = []

        self.create_board()

        self.__result_text = Label(self.__main_window, text="")
        self.__result_text.grid(row=0, column=4)

        self.__result_text.config(width=30)

        self.__reset = Button(self.__main_window, text="Reset",
                              command=self.reset_game,
                              background="lemon chiffon")
        self.__reset.grid(row=1, column=4)
        self.__reset.config(width=15)

        self.__quit = Button(self.__main_window, text="Quit",
                             command=self.stop, background="indian red")
        self.__quit.grid(row=2, column=4)
        self.__quit.config(width=15)

    def create_board(self):
        """
        Metodi tekee tyhjän pelilaudan
        tekemällä 3 buttonia, jotka ovat tallennettuta listan
        self.__column alkioihin. Lista, johon buttonit on
        tallennettu edelleen toiseen listaan(self.__row).
        Pelilaudan buttonin command on toteutettu lambda-funktion avulla,
        jotta commandille saa parametrit helposti. Funktiossa (ja koko
        ohjelmassa) x tai i kirjaimet tarkoittavat pelilaudan vaakarivin
        koordinaattia ja pelilaudan vaakarivia kuvaavan listan indeksiä.
        j tai y kirjaimet taas tarkoittavat pystyriviä.
        """
        for i in range(3):
            for j in range(3):
                self.__column.append(Button(self.__main_window, text="",
                                            command=lambda x=i, y=j:
                                            [self.button_press(x, y)]))
                self.__column[j].grid(row=i, column=j)
                self.__column[j].config(height=2, width=6)
            self.__row.append(self.__column)
            self.__column = []

    def reset_game(self):
        """
        Poistaa pelilaudan buttonit,
        tyhjentää listan, johon edellisen pelin merkit oli tallennettu.
        kutsuu metodia, joka tekee uuden tyhjän pelilaudan.
        """
        for i in range(3):
            for j in range(3):
                self.__row[i][j].destroy()
        self.__row = []
        self.create_board()
        self.__turn_count = 1
        self.__result_text.config(text="")

    def mark(self):
        """
        :return: Palauttaa seuraavaksi palautettavan merkin vuorolukeman
        parillisuuden perusteella.
        """

        if self.__turn_count/2 == self.__turn_count//2:
            return "X"
        else:
            return "O"

    def button_press(self, x, y):
        """
        Metodi vaihtaa painetun merkin tekstin tyhjästä X:n tai O:n.
        Riippuen vuorosta, lisää vuorolukemaan yhden ja kutsuu metodia,
        joka tarkastaa, toteutuuko voiton tai tasapelin ehdot.
        :param  x: monesko pelilaudan ruutu vaakasuorassa.
        :param  y: monesko pelilaudan ruutu pystysuorassa.
        """
        self.__turn_count += 1
        self.__row[x][y].configure(text=self.mark(), relief="ridge",
                                   state=DISABLED)

        self.winner(x, y)

    def winner(self, i, j):
        """
        Metodi tarkastaa, toteutuuko voiton tai tasapelin ehdot.
        Jos voiton ehdot toteutuu, metodi kutsuu metodia, joka
        lopettaa pelin pelaamisen ja tulostaa voitto-tekstin.
        :param  i: monesko pelilaudan ruutu vaakasuorassa.
        :param  j: monesko pelilaudan ruutu pystysuorassa.
        """
        mark = self.__row[i][j].cget("text")
        row = self.__row
        if mark == row[i][0].cget("text") == row[i][1].cget("text") ==\
                row[i][2].cget("text") \
                or mark == row[0][j].cget("text") == row[1][j].cget("text") ==\
                row[2][j].cget("text"):

            self.game_is_over(mark)

        elif row[0][0].cget("text") == row[1][1].cget("text") == \
                row[2][2].cget("text") and row[1][1].cget("text") == mark \
                or row[2][0].cget("text") == row[1][1].cget("text") \
                == row[0][2].cget("text") and row[1][1].cget("text") == mark:

            self.game_is_over(mark)

        elif self.__turn_count == 10:
            self.__result_text.configure(text="Tie!")

    def game_is_over(self, mark):
        """
        Tulostaa, kumpi voitti ja lopettaa pelin.
        :param  mark: Voittaneen pelaaja pelimerkki.
        """
        self.__result_text.\
            configure(text="The game ended, the winner is " + mark + "!")
        for k in range(3):
            for i in range(3):
                self.__row[k][i].configure(state=DISABLED, relief="ridge")

    def stop(self):
        self.__main_window.destroy()

    def start(self):
        self.__main_window.mainloop()


def main():
    ui = TicTacToe()
    ui.start()


main()
