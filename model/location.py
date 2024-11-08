class Location:
    def __init__(self, x: int, y: int) -> None:
        self.__x = x
        self.__y = y

    def get_x(self) -> int:
        return self.__x
    
    def get_y(self) -> int:
        return self.get_y
    
    def set_x(self, new_x: int) -> None:
        self.__x = new_x

    def set_y(self, new_y: int) -> None:
        self.__y = new_y
    
        