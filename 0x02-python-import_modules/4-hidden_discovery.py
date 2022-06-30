if __name__ == "__main__":
    import Hidden_4

    for o in dir(Hidden_4):
        if not o.startswith('_'):
            print(o)
