SIMPLE_STYLISH = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

SIMPLE_PLAIN = """Property 'follow' was removed
Property 'proxy' was removed
Property 'timeout' was updated. From '50' to '20'
Property 'verbose' was added with value: true"""

RECURSIVE_STYLISH = """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}"""

RECURSIVE_PLAIN = """Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]"""

SIMPLE_JSON = """[{"name": "follow", "status": 2, "children": null, "value": false, "old_value": null, "new_value": null}, {"name": "host", "status": 5, "children": null, "value": "hexlet.io", "old_value": null, "new_value": null}, {"name": "proxy", "status": 2, "children": null, "value": "123.234.53.22", "old_value": null, "new_value": null}, {"name": "timeout", "status": 4, "children": null, "value": null, "old_value": 50, "new_value": 20}, {"name": "verbose", "status": 1, "children": null, "value": true, "old_value": null, "new_value": null}]"""

RECURSIVE_JSON = """[{"name": "common", "status": 3, "children": [{"name": "follow", "status": 1, "children": null, "value": false, "old_value": null, "new_value": null}, {"name": "setting1", "status": 5, "children": null, "value": "Value 1", "old_value": null, "new_value": null}, {"name": "setting2", "status": 2, "children": null, "value": 200, "old_value": null, "new_value": null}, {"name": "setting3", "status": 4, "children": null, "value": null, "old_value": true, "new_value": null}, {"name": "setting4", "status": 1, "children": null, "value": "blah blah", "old_value": null, "new_value": null}, {"name": "setting5", "status": 1, "children": null, "value": {"key5": "value5"}, "old_value": null, "new_value": null}, {"name": "setting6", "status": 3, "children": [{"name": "doge", "status": 3, "children": [{"name": "wow", "status": 4, "children": null, "value": null, "old_value": "", "new_value": "so much"}], "value": null, "old_value": null, "new_value": null}, {"name": "key", "status": 5, "children": null, "value": "value", "old_value": null, "new_value": null}, {"name": "ops", "status": 1, "children": null, "value": "vops", "old_value": null, "new_value": null}], "value": null, "old_value": null, "new_value": null}], "value": null, "old_value": null, "new_value": null}, {"name": "group1", "status": 3, "children": [{"name": "baz", "status": 4, "children": null, "value": null, "old_value": "bas", "new_value": "bars"}, {"name": "foo", "status": 5, "children": null, "value": "bar", "old_value": null, "new_value": null}, {"name": "nest", "status": 4, "children": null, "value": null, "old_value": {"key": "value"}, "new_value": "str"}], "value": null, "old_value": null, "new_value": null}, {"name": "group2", "status": 2, "children": null, "value": {"abc": 12345, "deep": {"id": 45}}, "old_value": null, "new_value": null}, {"name": "group3", "status": 1, "children": null, "value": {"deep": {"id": {"number": 45}}, "fee": 100500}, "old_value": null, "new_value": null}]"""
