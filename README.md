## Stream API pre-Alpha
| Method |          Url          |     Accept     |               Returns               |
|:------:|:---------------------:|:--------------:|:-----------------------------------:|
|   PUT  |    /api/add_stream/   |   Stream json  |         Redis command result        |
|   GET  |    /api/get_stream/   | Stream id json |  Stream json / Redis command result |
|   GET  | /api/get_all_streams/ |       -        | Streams json / Redis command result |
| DELETE |  /api/delete_stream/  | Stream id json |         Redis command result        |
|  POST  |  /api/update_stream/  |   Stream json  |         Redis command result        |
|   GET  |   /api/dump_streams/  |       -        |         Redis command result        |
