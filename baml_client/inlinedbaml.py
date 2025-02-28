###############################################################################
#
#  Welcome to Baml! To use this generated code, please run the following:
#
#  $ pip install baml-py
#
###############################################################################

# This file was generated by BAML: please do not edit it. Instead, edit the
# BAML files and re-generate this code.
#
# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

file_map = {
    
    "clients.baml": "client<llm> EchoModelClient {\n  provider openai-generic\n  options {\n    model \"echo-model\"\n    base_url \"http://localhost:8200\"\n    api_key env.OPENAI_API_KEY\n  }\n}\n",
    "generators.baml": "// This helps use auto generate libraries you can use in the language of\n// your choice. You can have multiple generators if you use multiple languages.\n// Just ensure that the output_dir is different for each generator.\ngenerator target {\n    // Valid values: \"python/pydantic\", \"typescript\", \"ruby/sorbet\", \"rest/openapi\"\n    output_type \"python/pydantic\"\n\n    // Where the generated code will be saved (relative to baml_src/)\n    output_dir \"../\"\n\n    // The version of the BAML package you have installed (e.g. same version as your baml-py or @boundaryml/baml).\n    // The BAML VSCode extension version should also match this version.\n    version \"0.77.0\"\n\n    // Valid values: \"sync\", \"async\"\n    // This controls what `b.FunctionName()` will be (sync or async).\n    default_client_mode sync\n}\n",
    "parse.baml": "class Result {\n  @@dynamic\n}\n\nfunction ParseCompletion(completion: string) -> Result {\n  client EchoModelClient\n  prompt #\"{{ completion }}\"#\n}\n",
    "parse_food.baml": "class Food {\n  count int\n  items string[]\n}\n\nfunction ParseFood(completion: string) -> Food {\n  client EchoModelClient\n  prompt #\"{{ completion }}\"#\n}\n\ntest test_parse_food {\n  functions [ParseFood]\n  args {\n    completion #\"\n      Of course, I can help you with that. Here is a list of fruits:\n      {\n        count: 3,\n        items: [\n          apple, \n          banana, \n          cherry\n        ]\n      }\n      Let me know if you need anything else!\n    \"#\n  }\n}\n",
}

def get_baml_files():
    return file_map