def add(a, b):
    """Additionne a et b."""
    return a + b


def sub(a, b):
    """Soustrait b de a."""
    return a - b


def square(a):
    """Retourne le carré de a."""
    return a * a


def print_data(df):
    """Affiche le dataframe et retourne le nombre de lignes."""
    print(df)
    return len(df)
