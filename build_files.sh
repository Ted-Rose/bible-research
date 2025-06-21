python3 -m pip install -r requirements.txt

python3 scripts/vercel_setup.py create_ca_pem create_private_settings_yaml

# Collect static files
python3 manage.py collectstatic --noinput

# Create Vercel-compatible output vercel directory
mkdir -p .vercel/output/static
cp -r /vercel/path1/staticfiles/* .vercel/output/static/

python3 manage.py makemigrations
python3 manage.py migrate