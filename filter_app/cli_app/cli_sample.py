class a:
    @staticmethod
    def func():
        print('func a1')


class b:
    @staticmethod
    def func():
        print('func b1')


class c:
    @staticmethod
    def func():
        print('func a1')


class A:
    """

    """
    array = [a, b, c]

    @classmethod
    def func(cls):
        pass


class ImageEditor:
    array = []

    def _rollback(self):
        pass

    def create_chain(self):
        pass

    def filtering(self):
        while True:
            nav = input('Enter filter group please: ')
            if 'Face Detect' in nav:
                filter_specific = input(f'enter filter you want to use {A.array}: ')
                for i in A.array:
                    if str(i).endswith(filter_specific + "'>"):
                        i.func()
            elif 'Rollback' in nav:
                self._rollback()


if __name__ == '__main__':
    editor = ImageEditor()
    editor.filtering()
