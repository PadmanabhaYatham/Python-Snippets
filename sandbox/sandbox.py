import datetime
from typing import Optional


class CustomisedError(Exception):
    """
    Customised exception for SavedSnippets.
    """


class SavedSnippets:
    def __init__(self):
        self.today: Optional[datetime.datetime] = datetime.datetime.today()
        self.count: Optional[int] = None
        self.sum: Optional[int] = None

    # region properties
    @property
    def count(self) -> int:
        """
        Gets the count value.
        """
        if self.count is None:
            raise CustomisedError("count is not intitialized")
        return self.count

    @count.setter
    def count(self, value: int) -> None:
        self.count = value

    @property
    def sum(self) -> int:
        """
        Gets the sum value.
        """
        if self.sum is None:
            raise CustomisedError("sum is not intitialized")
        return self.sum

    @sum.setter
    def sum(self, value: int) -> None:
        self.sum = value

    # endregion

    # region code snippets
    def check_given_number_is_armstorng(self, num: int) -> bool:
        """
        Verifies the given number is a valid armstrong number or not.

        Args:
            num (int): input number value

        Returns:
            bool: status of the number is armstrong or not.
        """
        temp_num = num
        self.sum = 0

        while temp_num > 0:
            c = temp_num % 10
            self.sum += c**3
            temp_num //= 10

        return self.sum == num

    # endregion


if __name__ == "__main__":
    snippets = SavedSnippets()
    snippets.check_given_number_is_armstorng(65325)
