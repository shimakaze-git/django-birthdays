from jeraconv import jeraconv


class JpEra:
    def __init__(self, *args, **kwargs):
        self.j2w = jeraconv.J2W()

    def __convert_to_jp_era(self, year: int, month: int, day: int) -> dict:
        """[summary]

        Args:
            year (int): [description]
            month (int): [description]
            day (int): [description]

        Returns:
            dict: [description]
        """
        pass

    def convert(self, arg: str, limit_check=True):
        """[summary]

        Args:
            str_arg ([type]): [description]
            limit_check (bool, optional): [description]. Defaults to True.
        """
        str_arg = str(arg)
        # str_arg = self.__pre_process(str_arg)

    def __pre_process(self, str_arg):
        """[summary]

        Args:
            str_arg ([type]): [description]
        """
        pass

    def __is_correct_format(self, str_arg):
        """[summary]

        Args:
            str_arg ([type]): [description]
        """
        pass

    def __is_correct_era(self, str_arg):
        """[summary]

        Args:
            str_arg ([type]): [description]
        """
        pass
