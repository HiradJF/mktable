-Fix bugs
-complete unittest
-Test and fix those bugs too
-commit and push to github
-Build :
    ```bash
        flit Build
    ```
-Publish to test PyPi :
    ```bash
        flit Publish --repository testpypi
    ```
-Test that :
    ```bash
        pip install -i https://test.pypi.org/simple/ mktable
    ```
-Fix those bugs if any occur
-Rebuild (if changed):
    ```bash
        flit Build
    ```
-Publish to real PyPi:
    ```bash
        flit publish
    ```

