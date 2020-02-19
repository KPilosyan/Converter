from abc import ABC, abstractmethod 

class BinaryBase(ABC):
    """ Abstract class from which others inherit. Takes main user inputs. """
    def __init__(self, val, fr, to):
        self._val = val
        self.fr = fr
        self.to = to

    @abstractmethod
    def keywords(self):
        pass 
    """ Returns tuple of the keywords that user can input to perform the operation.
    It's used to validate user inputs"""

    @abstractmethod
    def validateValue(self):
        pass 
    """ Returns true in case the value input meets the corresponding class requirements. Otherwise false """

    @abstractmethod
    def validateKeywords(self):
        pass 
    """ Returns true if the requirements of a certain class meet are satisfied """   

    @abstractmethod
    def convert(self):
        pass 
    """ Contains the conversion formula. Returns the conversion final result """

    @abstractmethod
    def getInfo(self):
        pass
    """ Requires each class to have its description, to be shown under 'list_of_converters' command"""

