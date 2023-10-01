import os
import shutil

def is_venv_related(path):
    """
    Check if the given path is related to a virtual environment (venv).
    """
    return "venv" in path or "virtualenv" in path

def remove_migrations_and_pycache(root_dir):
    """
    Recursively remove migration directories and __pycache__ directories,
    avoiding venv directory.
    """
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=True):
        # Skip virtual environment directories
        if is_venv_related(dirpath):
            continue
        
        # Remove migration directories
        migration_dirs = [d for d in dirnames if d == "migrations"]
        for migration_dir in migration_dirs:
            full_migration_dir = os.path.join(dirpath, migration_dir)
            print(f"Removing: {full_migration_dir}")
            shutil.rmtree(full_migration_dir)
            dirnames.remove(migration_dir)
        
        # Remove __pycache__ directories
        pycache_dirs = [d for d in dirnames if d == "__pycache__"]
        for pycache_dir in pycache_dirs:
            full_pycache_dir = os.path.join(dirpath, pycache_dir)
            print(f"Removing: {full_pycache_dir}")
            shutil.rmtree(full_pycache_dir)
            dirnames.remove(pycache_dir)

if __name__ == "__main__":
    script_directory = os.path.dirname(os.path.abspath(__file__))
    target_directory = script_directory
    
    remove_migrations_and_pycache(target_directory)
    print("Cleanup completed.")
