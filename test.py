if __name__ == '__main__':
    def recur(a):
        b = 1
        for i in range(a):
            b = b * (i + 1)
        return b
    print(recur(4))
