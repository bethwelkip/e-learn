export MAIL_PASSWORD=2

# # #
# python3.7 manage.py db migrate -m "add column \"seen\" "
# python3.7 manage.py db upgrade 

python3.7 manage.py server
#env LDFLAGS="-I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib" pip install psycopg2