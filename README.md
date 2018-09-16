## Stream API Alpha
| Method |          Url          |     Accept     |               Returns                |
|:------:|:---------------------:|:--------------:|:-----------------------------------: |
|   PUT  |   `/api/add_stream`   |   Stream json  |       Elastic command result         |
|   GET  |    `/api/get_stream`  | Stream id json |Stream json / Elastic command result  |
|   GET  | `/api/get_all_streams`|       -        |Streams json / Elastic command result |
| DELETE |  `/api/delete_stream` | Stream id json |       Elastic command result         |
|  POST  |  `/api/update_stream` |   Stream json  |       Elastic command result         |
|  GET   | `/api/import_streams` |   Stream json  |       Elastic command result         |
|  GET   | `/api/export_streams` |       -        |       Elastic command result         |

### Important: all requests to the API must contain "Content-Type: application/json" header.
