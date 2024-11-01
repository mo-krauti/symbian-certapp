# symbian certapp

certapp allows you to create your own CA certificate bundles for symbian.

## build
Because this software is so ancient, it is built and run in ubuntu-6.06 dapper.
```bash
docker build -t symbian-certapp .
```

## run
Copy system certs to input and create human readable cert store:
```bash
cd certs
cp /etc/ssl/certs/*.pem .
python create_cacerts_txt.py
```

Create binary cert store:
```bash
docker run -it --rm -v ./:/wd symbian-certapp --hca=cacerts.txt --out --bca=cacerts.dat
```
`cacerts.dat` is now in the `certs` folder, copy it to `C://private/101f72a6/` on your phone. Backup the original file before!

## tls v1.3
Use [this patch](https://nnp.nnchan.ru/tls/) for tls1.2 / tls 1.3 support

## docs

found them here:  
http://devlib.symbian.slions.net/s3/GUID-6BD23C4F-CBF7-584D-81D9-EB8D14DC3081.html

## source code

found it here:  
https://github.com/SymbianSource/oss.FCL.sf.os.security
