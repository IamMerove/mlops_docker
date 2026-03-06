from modules.connect import init_db, SessionLocal
from modules import crud


def test_connection():
    print("--- Tentative d'initialisation de la BDD ---")
    # 1. On crée les tables
    init_db()

    # 2. On ouvre une session
    db = SessionLocal()

    try:
        print("--- Insertion d'une donnée de test ---")
        # 3. On tente d'insérer un calcul fictif
        new_row = crud.create_calculation(
            db=db, operation="test_init", val=10.0, res=100.0
        )
        print(f"Succès ! Donnée insérée avec l'ID : {new_row.id}")

        # 4. On vérifie la lecture
        all_data = crud.get_all_calculations(db)
        print(f"Nombre de lignes en base : {len(all_data)}")

    except Exception as e:
        print(f"Erreur lors du test : {e}")
    finally:
        db.close()


if __name__ == "__main__":
    test_connection()
