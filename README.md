# event-server

Backend that provides a thirdparty to report events.

Currently an event is defined as:
Event
  - title
  - description
  - created (date of creation)
  - updated (date of last update)
  - Category
    - title
    - description
    - created (date of creation)
    - updated (date of last update)
    
The REST api is exposed through:
remotely: https://events-rep.herokuapp.com/v1/
locally: http://localhost:8000/v1/

