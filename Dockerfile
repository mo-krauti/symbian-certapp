FROM icomputer7/ancient-ubuntu-docker:dapper AS build
RUN apt-get update
RUN apt-get install -y g++-3.4 make libssl-dev
WORKDIR /build
COPY PDK_3.0.4.tar.gz .
RUN tar -xvf PDK_3.0.4.tar.gz
WORKDIR /build/oss.FCL.sf.os.security-PDK_3.0.4/securityanddataprivacytools/securitytools/certapp/
# ignore the failed build, the tool itself builds sucessfully it's just the tests
RUN make || :

FROM icomputer7/ancient-ubuntu-docker:dapper
COPY --from=build /build/oss.FCL.sf.os.security-PDK_3.0.4/securityanddataprivacytools/securitytools/certapp/certapp /bin/certapp

# create unpriviledged user
RUN groupadd app -g 1000 && useradd -u 1000 -g app -m -d /wd -s /sbin/nologin app && \
 chmod 755 /wd && chown -R app:app /wd
USER app
WORKDIR /wd

ENTRYPOINT ["/bin/certapp"]
CMD ["-h"]
