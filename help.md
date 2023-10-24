
# 1. package

```shell
python setup.py sdist bdist_wheel
```

2. install twine
```shell
pip install twine
```

3. push
twine upload dist/*

[ref]
https://www.jianshu.com/p/fbb083aebcc1