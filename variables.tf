variable "environment_aws_arn" {
  type = string
  description = "[Required] aws arn for building lambda function"
  default = ""
}

variable "memory_size" {
  type = number
  description = "[Required] memory for the function"
  default = 1024
}