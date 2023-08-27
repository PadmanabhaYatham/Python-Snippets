import datetime
from typing import Optional, Any


class CustomisedError(Exception):
    """
    Customised exception for SavedSnippets.
    """


class SavedSnippets:
    def __init__(self):
        # Builtin attributes
        self.today: Optional[datetime.datetime] = datetime.datetime.today()

        # runtime attributes
        self._count: Optional[int] = None
        self._sum: Optional[int] = None
        self._idx: Optional[int] = None
        self._result: Optional[Any] = None

    # region properties
    @property
    def count(self) -> int:
        """
        Gets the count value.
        """
        if self._count is None:
            raise CustomisedError("count is not initialized")
        return self._count

    @count.setter
    def count(self, value: int) -> None:
        self._count = value

    @property
    def sum(self) -> int:
        """
        Gets the sum value.
        """
        if self._sum is None:
            raise CustomisedError("sum is not initialized")
        return self._sum

    @sum.setter
    def sum(self, value: int) -> None:
        self._sum = value

    @property
    def idx(self) -> int:
        """
        Gets the index value for our UC.
        """
        if self._idx is None:
            raise CustomisedError("count is not initialized")
        return self._idx

    @idx.setter
    def idx(self, value: int) -> None:
        self._idx = value

    @property
    def result(self) -> Any:
        """
        Gets the result value for our UC.
        """
        if self._result is None:
            raise CustomisedError("count is not initialized")
        return self._result

    @result.setter
    def result(self, value: int) -> None:
        self._result = value

    # endregion

    # region Helpers
    def _get_char_number(self, letter) -> int | Any:
        letters = [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
        ]

        self.result = ""
        self.idx = 0
        for char in letter:
            if not char.isalpha():
                self.result += char

            elif self.idx == 0:
                num = letters.index(char.lower())
                self.result += str(num + 1)

            else:
                num = letters.index(char.lower())
                self.result += "-" + str(num + 1)

            self.idx += 1

        return self.result

    # endregion

    # region practice snippets
    def verify_is_armstrong_number(self, num: int) -> None:
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

        if self.sum == num:
            print("The given number is 'armstrong number'.")

        else:
            print("The given number is 'not a armstrong number'.")

    @staticmethod
    def print_given_matrix_anti_diagonals() -> None:
        """
        Prints the anti-diagonals of given matrix.
        """
        # collect user input
        row_count, column_count = map(
            int,
            input(
                "Enter length of matrix (if it is MxN matrix then your input will be M N) separated by space: "
            ).split(),
        )

        mtx = []
        for i in range(row_count):

            def take_row_values():
                inp = input(
                    f"Enter row {column_count} values separated by space: "
                ).split()
                if len(inp) == column_count:
                    mtx.append(inp)

                else:
                    print(f"Pls enter {column_count} number of values")
                    take_row_values()

        # perform printing anti-diagonals steps
        rm = []
        for i in range(row_count + column_count + 1):
            r = []
            for j in range(row_count):
                for k in range(column_count):
                    if j + k == i:
                        r.append(mtx[j][k])

            if r:
                rm.append(r)

        for i in rm:
            print(" ".join(i))

    def encrypt_message_by_nums(self, inp_msg: Any) -> None:
        """
        Encrypts the input message by replacing the characters by numbers.

        Args:
            inp_msg (Str): input string value.
        """
        res = ""
        for char in inp_msg.split():
            res += str(self._get_char_number(char)) + " "

        print(res)

    # endregion


if __name__ == "__main__":
    operations = SavedSnippets()
    # operations.verify_is_armstrong_number(153)
    operations.encrypt_message_by_nums("Hello yatham")
