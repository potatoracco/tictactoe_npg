from abc import ABC, abstractmethod
import curses


class ProgramState(ABC):
    @abstractmethod
    def loop(self, scr):
        """
        Funkcja powinna zawierać pętle przyjmującą dane wejściowe od użytkownika
        i wyświetlającą odpowiednią zawartość na ekranie.

        Wartością zwracaną ma być kolejny stan programu wraz z odpowiednimi parametrami
        np. z ekranu ustalania zasad gry przechodzimy do samej gry

        return /stan/, /agrumenty/, /argumenty nazwane/
        return 'game', (3), {Player1: p1, Player2: p2}
        """
        pass

    def tui_template(self, scr):
        curses.curs_set(0)
        scr.nodelay(True)