The `main.py` is the main function in lambda, with the entry point is `lambda_handler`
Requirement.txt is list of packages for function (in this exercise, we don't really need any, but I just still add them into). Everything will be locally install to the `package` folder with `python3 -m pip install --only-binary :all: --platform manylinux1-x86_64 --target ./package -r requirements.txt` as the platform in case using arm architechture like I did.

then zip everything `package + main.py` into `function-package.zip` before making it available for terraform to pick up.