"""Entry point for the OpenBB Python interface build script."""

# pylint: disable=import-outside-toplevel,unused-import
# flake8: noqa

def main():
    """Build the OpenBB Python interface."""

    import sys
    import subprocess
    try:
        import openbb
    except ImportError:
        print("\nThe OpenBB Python interface build script was not found, installing it now...\n")
        subprocess.run([sys.executable, "-m", "pip", "install", "openbb", "--no-deps"])  # noqa

    print("\nBuilding the OpenBB Python interface...\n")

    subprocess.run([sys.executable, "-c", "import openbb;openbb.build()"])

    print("\nThe build was completed!\n")

if __name__ == "__main__":
    main()
