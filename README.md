# Flipkart E2E Test

This project contains an end-to-end test for Flipkart using Selenium and Pytest.

## Prerequisites

- Python 3.x installed
- Google Chrome browser installed
- Install dependencies:
  ```
  pip install selenium
  pip install pytest
  ```

## Running the Test

To run the Flipkart E2E test with the `e2e_flipkart` marker, use the following command in your terminal:

```
pytest -m e2e_flipkart -v -s
```

- `-m e2e_flipkart` runs only tests marked with `@pytest.mark.e2e_flipkart`
- `-v` enables verbose output
- `-s` allows print statements and `input()` to show in the terminal

## OTP Input

During the test run, you will be prompted to enter the test mobile number and OTP sent to your registered mobile number.  
**Please monitor the terminal and enter the registered Mobile number and OTP when prompted.**

## Notes

- The test will pause and wait for Flipkart test account phone number.
- The test will pause and wait for OTP input.
- Do not close the terminal until the test completes.
