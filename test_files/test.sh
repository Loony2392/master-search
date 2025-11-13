#!/bin/bash
# Test shell script
echo "Running test script"
TEST_VAR="test_value"
if [ "$TEST_VAR" = "test_value" ]; then
    echo "Test passed"
else
    echo "Test failed"
fi