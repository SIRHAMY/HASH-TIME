
import photohash

class HashProcessor():
    def __init__(self):
        print("HashProcessor running...")

    def getHash(self, imgLocation):
        hash = photohash.average_hash(imgLocation, 16)
        return hash

    def getHashDistance(self, hashOne, hashTwo):
        return photohash.hash_distance(hashOne, hashTwo)

    def getHashValue(self, imgHash):

        totalHashValue = 0

        for char in imgHash:
            value = ord(char)

            if value >= 48 and value <= 57:
                value-=48
            elif value >= 97 and value <= 122:
                value -= 87
            else:
                print "Unsupported char value"
            
            totalHashValue += value

        return totalHashValue