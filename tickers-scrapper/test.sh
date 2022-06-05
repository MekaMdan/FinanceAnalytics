for module in ./src/tests/*.py; do
    module_to_test="$(basename "$module" .py)"
    echo Testing module: $module_to_test
    python -m unittest src.tests."$module_to_test"
    done