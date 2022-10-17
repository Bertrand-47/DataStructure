class MyHashSet(object):

    def __init__(self):
        
        self.list1 =[]
        

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if(not self.contains(key)):
            self.list1.append(key)
        
    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if(self.contains(key)):
            key = self.list1.index(key)
            self.list1.pop(key)
    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        for i in self.list1:
            if i == key:
                return True
        return False