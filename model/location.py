class Location:
    # Class Takes X and Y. Used as coordinates for Grid
    def __init__(self, x: int, y: int) -> None:
        self.__x = x
        self.__y = y

    # Returns X
    def get_x(self) -> int:
        return self.__x

    # Returns Y
    def get_y(self) -> int:
        return self.__y

    # Sets new X
    def set_x(self, new_x: int) -> None:
        self.__x = new_x

    # Sets new Y
    def set_y(self, new_y: int) -> None:
        self.__y = new_y
    
        