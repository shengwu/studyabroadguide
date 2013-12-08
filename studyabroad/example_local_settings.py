import dj_database_url
DATABASES = {'default': dj_database_url.parse('postgres://username:password@localhost/database')}
