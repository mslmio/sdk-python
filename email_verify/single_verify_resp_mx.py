from dataclasses import dataclass


@dataclass
class SingleVerifyRespMx:
    """
    Data class representing Mail Exchange (MX) records in the response of a single email verification.

    Attributes:-
        - host (str): The host or domain name of the mail server.
        - pref (int): The preference value indicating the priority of the mail server.

    Methods:-
        - __str__(self): Returns a string representation of the SingleVerifyRespMx object.
        - get_host(self): Returns the host or domain name of the mail server.
        - get_pref(self): Returns the preference value indicating the priority of the mail server.
    """

    host: str
    pref: int

    def __str__(self):
        """
        Returns a string representation of the SingleVerifyRespMx object.

        Returns:
            - str: A string representation of the SingleVerifyRespMx object.
        """
        return f"SingleVerifyRespMx{{host='{self.host}', pref={self.pref}}}"

    def get_host(self):
        """
        Returns the host or domain name of the mail server.

        Returns:
            - str: The host or domain name of the mail server.
        """
        return self.host

    def get_pref(self):
        """
        Returns the preference value indicating the priority of the mail server.

        Returns:
            - int: The preference value indicating the priority of the mail server.
        """
        return self.pref
