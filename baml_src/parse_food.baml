class Food {
  count int
  items string[]
}

function ParseFood(completion: string) -> Food {
  client EchoModelClient
  prompt #"{{ completion }}"#
}

test test_parse_food {
  functions [ParseFood]
  args {
    completion #"
      Of course, I can help you with that. Here is a list of fruits:
      {
        count: 3,
        items: [
          apple, 
          banana, 
          cherry
        ]
      }
      Let me know if you need anything else!
    "#
  }
}
