# Django Application that store the User BookMarks

- This app stores users and their bookmarks
- Use '/api/create' endpoint to create BookMarks through POST Call.
- Use '/api/browse' endpoint to browse Bookmarks trough GET call with the below query parameters
      Parameters for /api/browse
          - start_date
          - lat
          - long
          - end_date
          - title_contains
          - source_name
          - sort_by

#### Please use the below command to start the server
```
python manage.py runserver
```
