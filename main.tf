module "lambda_function_existing_package_local" {
  source = "terraform-aws-modules/lambda/aws"

  function_name = "test-iot-lambda"
  description   = "Test function to read and decode iot bytes to data"
  handler       = "main.lambda_handler"
  runtime       = "python3.9"

  create_package         = false
  local_existing_package = "../function-packge.zip"
  attach_cloudwatch_logs_policy = true
  memory_size = 1024
  
}


resource "aws_lambda_function_url" "test_latest" {
  function_name      = aws_lambda_function.lambda.test-iot-lambda
  authorization_type = "NONE"
}

resource "aws_lambda_function_url" "test_live" {
  function_name      = aws_lambda_function.lambda.function_name
  qualifier          = "public_test"
  authorization_type = "NONE"

  cors {
    allow_credentials = false
    allow_origins     = ["*"]
    allow_methods     = ["*"]
    allow_headers     = ["date", "keep-alive"]
    expose_headers    = ["keep-alive", "date"]
    max_age           = 86400
  }
}