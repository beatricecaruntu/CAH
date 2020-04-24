group: development do
    gem 'sqlite3'
end

group: production do
    gem 'pg'
    gem "activerecord-postgresql-adapter"
end

development:
    adapter: sqlite3
    database: cards.db

test:
    adapter: sqlite3
    database: cards.db
   
production:
    adapter: postgresql
    database: mission
    username: bia
    password: bia
    host: localhost
    