FROM python:onbuild
ENV PORT 5000
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]
