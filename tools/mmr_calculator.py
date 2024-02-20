class MMRGameCalculator:
    def __init__(
        self,
        mmr_per_division: int | float,
        current_mmr: int | float,
        divisions: int,
        win_mmr: int | float,
        loss_mmr: int | float,
    ) -> None:
        """
        Initialises a MMRGameCalculator Instance.
        The MMRGameCalculator Object is able to calculate game related statistics

        Parameters
        ----------
        mmr_per_division : int | float
            The MMR gained per division.
        current_mmr : int | float
            The current MMR of the player.
        divisions : int
            The number of divisions to climb.
        win_mmr : int | float
            The MMR gained per win.
        loss_mmr : int | float
            The MMR lost per loss.

        Returns
        -------
        None
        """
        self.__mmr_per_division = mmr_per_division
        self.__current_mmr = current_mmr
        self.__divisions = divisions
        self.__win_mmr = win_mmr
        self.__loss_mmr = loss_mmr

        total_mmr_needed = (
            self.__divisions * self.__mmr_per_division - self.__current_mmr
        )
        self.__total_mmr_needed = total_mmr_needed

        print(f"MMR GAME CALCULATOR IS NOW RUNNING.")

    def calculate_winrate_required(self, total_games: int) -> None:
        """
        Calculates and prints the winrate required to climb the specified number of divisions
        within the given total number of games.

        Parameters
        ----------
        total_games : int
            The total number of games you're willing to play.

        Returns
        -------
        None
        """
        # Input validity checks
        if not isinstance(total_games, int):
            raise ValueError(
                f"total_games must be of type int, {type(total_games)} was given instead."
            )

        winrate_required = (self.__total_mmr_needed / total_games - self.__loss_mmr) / (
            self.__win_mmr - self.__loss_mmr
        )
        if winrate_required > 1:
            raise ValueError(
                f"{total_games} of games is not enough to climb out the division even when at 100% winrate."
            )
        print(f"WINRATE REQUIRED IS: {winrate_required:.1%}")

    def calculate_games_required(self, winrate: float) -> None:
        """
        Calculate and print the number of games needed to climb the specified number of divisions
        with the given winrate.

        Parameters
        ----------
        winrate : float
            The winrate achieved in games (0.0 to 1.0).
        
        Returns
        -------
        None
        """
        # Input validity checks
        if not isinstance(winrate, (int, float)):
            raise ValueError(
                f"winrate must be of type int or float, {type(winrate)} was given instead."
            )
        if winrate < 0 or winrate > 1:
            raise ValueError(
                f"winrate can only be of values between 0.0 to 1.0. winrate is currently set at {winrate}"
            )

        games_required = self.__total_mmr_needed / (
            winrate * self.__win_mmr + (1 - winrate) * self.__loss_mmr
        )
        print(
            f"GAMES REQUIRED TO CLIMB {self.__divisions} DIVISIONS IS: {games_required:.1f}"
        )
