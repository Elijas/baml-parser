class Result {
  @@dynamic
}

function ParseCompletion(completion: string) -> Result {
  client EchoModelClient
  prompt #"{{ completion }}"#
}
