client<llm> EchoModelClient {
  provider openai-generic
  options {
    model "echo-model"
    base_url "http://localhost:8200"
    api_key ""
  }
}
