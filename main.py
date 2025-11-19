import math


def isprime(p: int) -> bool:
    """
    Vérifie si un nombre entier (p) est un nombre premier.

    Args:
        p: L'entier à tester.

    Returns:
        True si p est premier, False sinon.
    """

    # 1. Un nombre premier est un entier naturel > 1.
    # Les nombres <= 1 ne sont pas premiers.
    if p <= 1:
        return False

    # 2. Le cas spécial de 2, qui est le seul nombre premier pair.
    if p == 2:
        return True

    # 3. Tous les autres nombres pairs ne sont pas premiers.
    # On peut les exclure pour optimiser la boucle.
    if p % 2 == 0:
        return False

    # 4. On vérifie les diviseurs impairs.
    # Il suffit de tester jusqu'à la racine carrée de p.
    # Si p a un diviseur > sqrt(p), il en a forcément un < sqrt(p).
    # math.isqrt(p) calcule la racine carrée entière (plus efficace).
    max_divisor = math.isqrt(p)

    # On boucle de 3 jusqu'à max_divisor (inclus), en avançant de 2 en 2
    # (on ignore les diviseurs pairs, déjà gérés).
    for i in range(3, max_divisor + 1, 2):
        if p % i == 0:
            # p est divisible par i, il n'est donc pas premier.
            return False

    # 5. Si la boucle se termine sans trouver de diviseur,
    # c'est que p est premier.
    return True


def main():
    """
    Fonction principale pour tester la fonction secondaire isprime().
    """
    print("--- Tests de la fonction isprime ---")

    # Cas de base
    print(f"isprime(-5) : {isprime(-5)}")  # Attendu: False
    print(f"isprime(0) : {isprime(0)}")  # Attendu: False
    print(f"isprime(1) : {isprime(1)}")  # Attendu: False

    # Premiers
    print(f"isprime(2) : {isprime(2)}")  # Attendu: True
    print(f"isprime(3) : {isprime(3)}")  # Attendu: True
    print(f"isprime(17) : {isprime(17)}")  # Attendu: True
    print(f"isprime(97) : {isprime(97)}")  # Attendu: True

    # Non premiers
    print(f"isprime(4) : {isprime(4)}")  # Attendu: False (2*2)
    print(f"isprime(9) : {isprime(9)}")  # Attendu: False (3*3)
    print(f"isprime(15) : {isprime(15)}")  # Attendu: False (3*5)
    print(f"isprime(100) : {isprime(100)}")  # Attendu: False (10*10)


if __name__ == "__main__":
    main()
