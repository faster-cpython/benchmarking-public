| benchmark | collect-stats | darwin-arm64 | linux-aarch64 | linux-x86_64 | windows-x86 | windows-x86_64 |
| --- | --- | --- | --- | --- | --- | --- |
| chameleon | [[pystats run]](#chameleon-on-collect-stats-pystats) | [[default run]](#chameleon-on-darwin-arm64-default) | [[default run]](#chameleon-on-linux-aarch64-default) | [[default run]](#chameleon-on-linux-x86_64-default) | [[default run]](#chameleon-on-windows-x86-default) | [[default run]](#chameleon-on-windows-x86_64-default) |
| dask |  | [[default run]](#dask-on-darwin-arm64-default) |  |  |  |  |
| djangocms | [[pystats build]](#djangocms-on-collect-stats-pystats) | [[default build]](#djangocms-on-darwin-arm64-default) | [[nogil build]](#djangocms-on-linux-aarch64-nogil) | [[nogil build]](#djangocms-on-linux-x86_64-nogil) | [[default build]](#djangocms-on-windows-x86-default) | [[default build]](#djangocms-on-windows-x86_64-default) |
| flaskblogging | [[pystats run]](#flaskblogging-on-collect-stats-pystats) | [[default run]](#flaskblogging-on-darwin-arm64-default) | [[default run]](#flaskblogging-on-linux-aarch64-default) | [[default run]](#flaskblogging-on-linux-x86_64-default) | [[default run]](#flaskblogging-on-windows-x86-default) | [[default run]](#flaskblogging-on-windows-x86_64-default) |
| gevent_hub | [[pystats run]](#gevent_hub-on-collect-stats-pystats) | [[default run]](#gevent_hub-on-darwin-arm64-default) | [[default run]](#gevent_hub-on-linux-aarch64-default) | [[default run]](#gevent_hub-on-linux-x86_64-default) | [[default build]](#gevent_hub-on-windows-x86-default) | [[default build]](#gevent_hub-on-windows-x86_64-default) |
| gunicorn | [[pystats run]](#gunicorn-on-collect-stats-pystats) | [[default run]](#gunicorn-on-darwin-arm64-default) | [[default run]](#gunicorn-on-linux-aarch64-default) | [[default run]](#gunicorn-on-linux-x86_64-default) | [[default run]](#gunicorn-on-windows-x86-default) | [[default run]](#gunicorn-on-windows-x86_64-default) |
| kinto | [[pystats run]](#kinto-on-collect-stats-pystats) | [[default build]](#kinto-on-darwin-arm64-default) | [[default build]](#kinto-on-linux-aarch64-default) | [[default build]](#kinto-on-linux-x86_64-default) | [[default build]](#kinto-on-windows-x86-default) | [[default build]](#kinto-on-windows-x86_64-default) |
| pytorch_alexnet_inference | [[pystats build]](#pytorch_alexnet_inference-on-collect-stats-pystats) | [[default build]](#pytorch_alexnet_inference-on-darwin-arm64-default) | [[default build]](#pytorch_alexnet_inference-on-linux-aarch64-default) | [[default build]](#pytorch_alexnet_inference-on-linux-x86_64-default) | [[default build]](#pytorch_alexnet_inference-on-windows-x86-default) | [[default build]](#pytorch_alexnet_inference-on-windows-x86_64-default) |
| sqlalchemy_declarative |  |  |  |  | [[default build]](#sqlalchemy_declarative-on-windows-x86-default) | [[default build]](#sqlalchemy_declarative-on-windows-x86_64-default) |
| sqlalchemy_imperative |  |  |  |  | [[default build]](#sqlalchemy_imperative-on-windows-x86-default) | [[default build]](#sqlalchemy_imperative-on-windows-x86_64-default) |
| tornado_http | [[pystats run]](#tornado_http-on-collect-stats-pystats) | [[default run]](#tornado_http-on-darwin-arm64-default) | [[default run]](#tornado_http-on-linux-aarch64-default) | [[default run]](#tornado_http-on-linux-x86_64-default) | [[default run]](#tornado_http-on-windows-x86-default) | [[default run]](#tornado_http-on-windows-x86_64-default) |
## chameleon on darwin-arm64 default

<details>
<summary>Log for chameleon on darwin-arm64 default</summary>

```
# /Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688/bin/python -u /Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.12/site-packages/pyperformance/data-files/benchmarks/bm_chameleon/run_benchmark.py --inherit-environ PYPERFORMANCE_RUNID,PYTHON_JIT --output /tmp/tmp5t18_u0o
Traceback (most recent call last):
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.12/site-packages/pyperformance/data-files/benchmarks/bm_chameleon/run_benchmark.py", line 5, in <module>
    from chameleon import PageTemplate
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/__init__.py", line 1, in <module>
    from .zpt.template import PageTemplate
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/zpt/template.py", line 6, in <module>
    from ..tales import PythonExpr
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/tales.py", line 27, in <module>
    from .compiler import Interpolator
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/compiler.py", line 34, in <module>
    from .tal import ErrorInfo
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/tal.py", line 26, in <module>
    from chameleon import interfaces
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/interfaces.py", line 1, in <module>
    from zope.interface import Interface
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/__init__.py", line 58, in <module>
    _wire()
    ~~~~~^^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 1154, in _wire
    from zope.interface.interfaces import IElement
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interfaces.py", line 56, in <module>
    class IElement(Interface):
    ...<93 lines>...
            """
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 794, in __init__
    self.__attrs = self.__compute_attrs(attrs)
                   ~~~~~~~~~~~~~~~~~~~~^^^^^^^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 813, in __compute_attrs
    aname: update_value(aname, aval)
           ~~~~~~~~~~~~^^^^^^^^^^^^^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 809, in update_value
    raise InvalidInterface("Concrete attribute, " + aname)
zope.interface.exceptions.InvalidInterface: Concrete attribute, __classdictcell__
Traceback (most recent call last):
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.12/site-packages/pyperformance/run.py", line 170, in run_benchmarks
    result = bench.run(
             ^^^^^^^^^^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.12/site-packages/pyperformance/_benchmark.py", line 189, in run
    bench = _run_perf_script(
            ^^^^^^^^^^^^^^^^^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.12/site-packages/pyperformance/_benchmark.py", line 240, in _run_perf_script
    raise RuntimeError("Benchmark died")
RuntimeError: Benchmark died
Command failed with exit code 1
```

</details>

## chameleon on linux-aarch64 default

<details>
<summary>Log for chameleon on linux-aarch64 default</summary>

```
# /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-6e18c82301b6-compat-cb6a104a6688/bin/python -u /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/data-files/benchmarks/bm_chameleon/run_benchmark.py --inherit-environ PYPERFORMANCE_RUNID,PYTHON_JIT --output /tmp/tmpllaggtgp
Traceback (most recent call last):
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/data-files/benchmarks/bm_chameleon/run_benchmark.py", line 5, in <module>
    from chameleon import PageTemplate
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-6e18c82301b6-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/__init__.py", line 1, in <module>
    from .zpt.template import PageTemplate
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-6e18c82301b6-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/zpt/template.py", line 6, in <module>
    from ..tales import PythonExpr
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-6e18c82301b6-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/tales.py", line 27, in <module>
    from .compiler import Interpolator
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-6e18c82301b6-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/compiler.py", line 34, in <module>
    from .tal import ErrorInfo
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-6e18c82301b6-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/tal.py", line 26, in <module>
    from chameleon import interfaces
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-6e18c82301b6-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/interfaces.py", line 1, in <module>
    from zope.interface import Interface
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-6e18c82301b6-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/__init__.py", line 58, in <module>
    _wire()
    ~~~~~^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-6e18c82301b6-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 1154, in _wire
    from zope.interface.interfaces import IElement
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-6e18c82301b6-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interfaces.py", line 56, in <module>
    class IElement(Interface):
    ...<93 lines>...
            """
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-6e18c82301b6-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 794, in __init__
    self.__attrs = self.__compute_attrs(attrs)
                   ~~~~~~~~~~~~~~~~~~~~^^^^^^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-6e18c82301b6-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 813, in __compute_attrs
    aname: update_value(aname, aval)
           ~~~~~~~~~~~~^^^^^^^^^^^^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-6e18c82301b6-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 809, in update_value
    raise InvalidInterface("Concrete attribute, " + aname)
zope.interface.exceptions.InvalidInterface: Concrete attribute, __classdictcell__
Traceback (most recent call last):
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/run.py", line 170, in run_benchmarks
    result = bench.run(
             ^^^^^^^^^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/_benchmark.py", line 189, in run
    bench = _run_perf_script(
            ^^^^^^^^^^^^^^^^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/_benchmark.py", line 240, in _run_perf_script
    raise RuntimeError("Benchmark died")
RuntimeError: Benchmark died
Command failed with exit code 1
```

</details>

## chameleon on collect-stats pystats

<details>
<summary>Log for chameleon on collect-stats pystats</summary>

```
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-7c12bab99a20-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/template.py", line 137, in __init__
    self.write(body)
    ~~~~~~~~~~^^^^^^
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-7c12bab99a20-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/template.py", line 235, in write
    self.cook(body)
    ~~~~~~~~~^^^^^^
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-7c12bab99a20-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/template.py", line 167, in cook
    program = self._cook(body, digest, names)
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-7c12bab99a20-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/template.py", line 245, in _cook
    source = self._compile(body, builtins)
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-7c12bab99a20-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/template.py", line 276, in _compile
    program = self.parse(body)
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-7c12bab99a20-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/zpt/template.py", line 227, in parse
    return MacroProgram(
        body, self.mode, self.filename,
    ...<9 lines>...
        tokenizer=self.tokenizer
    )
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-7c12bab99a20-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/zpt/program.py", line 174, in __init__
    super(MacroProgram, self).__init__(*args, **kwargs)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-7c12bab99a20-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/program.py", line 35, in __init__
    node = self.visit(kind, args)
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-7c12bab99a20-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/program.py", line 41, in visit
    return visitor(*args)
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-7c12bab99a20-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/zpt/program.py", line 320, in visit_element
    ATTRIBUTES = self._create_attributes_nodes(
        prepared, I18N_ATTRIBUTES, STATIC_ATTRIBUTES,
    )
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-7c12bab99a20-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/zpt/program.py", line 794, in _create_attributes_nodes
    default = ast.Str(s=text) if text is not None else None
              ^^^^^^^
AttributeError: module 'ast' has no attribute 'Str'
Traceback (most recent call last):
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/run.py", line 170, in run_benchmarks
    result = bench.run(
             ^^^^^^^^^^
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/_benchmark.py", line 189, in run
    bench = _run_perf_script(
            ^^^^^^^^^^^^^^^^^
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/_benchmark.py", line 240, in _run_perf_script
    raise RuntimeError("Benchmark died")
RuntimeError: Benchmark died
Command failed with exit code 1

ERROR: No benchmark was run
Python benchmark suite 1.11.0


==================================================
```

</details>

## chameleon on linux-x86_64 default

<details>
<summary>Log for chameleon on linux-x86_64 default</summary>

```
# /home/ddfun/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0e992284450f-compat-cb6a104a6688/bin/python -u /home/ddfun/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/data-files/benchmarks/bm_chameleon/run_benchmark.py --inherit-environ PYTHON_JIT,PYPERFORMANCE_RUNID --output /tmp/tmp14dktb35
Traceback (most recent call last):
  File "/home/ddfun/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/data-files/benchmarks/bm_chameleon/run_benchmark.py", line 5, in <module>
    from chameleon import PageTemplate
  File "/home/ddfun/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0e992284450f-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/__init__.py", line 1, in <module>
    from .zpt.template import PageTemplate
  File "/home/ddfun/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0e992284450f-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/zpt/template.py", line 6, in <module>
    from ..tales import PythonExpr
  File "/home/ddfun/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0e992284450f-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/tales.py", line 27, in <module>
    from .compiler import Interpolator
  File "/home/ddfun/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0e992284450f-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/compiler.py", line 34, in <module>
    from .tal import ErrorInfo
  File "/home/ddfun/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0e992284450f-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/tal.py", line 26, in <module>
    from chameleon import interfaces
  File "/home/ddfun/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0e992284450f-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/interfaces.py", line 1, in <module>
    from zope.interface import Interface
  File "/home/ddfun/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0e992284450f-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/__init__.py", line 58, in <module>
    _wire()
    ~~~~~^^
  File "/home/ddfun/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0e992284450f-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 1154, in _wire
    from zope.interface.interfaces import IElement
  File "/home/ddfun/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0e992284450f-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interfaces.py", line 56, in <module>
    class IElement(Interface):
    ...<93 lines>...
            """
  File "/home/ddfun/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0e992284450f-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 794, in __init__
    self.__attrs = self.__compute_attrs(attrs)
                   ~~~~~~~~~~~~~~~~~~~~^^^^^^^
  File "/home/ddfun/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0e992284450f-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 813, in __compute_attrs
    aname: update_value(aname, aval)
           ~~~~~~~~~~~~^^^^^^^^^^^^^
  File "/home/ddfun/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0e992284450f-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 809, in update_value
    raise InvalidInterface("Concrete attribute, " + aname)
zope.interface.exceptions.InvalidInterface: Concrete attribute, __classdictcell__
Traceback (most recent call last):
  File "/home/ddfun/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/run.py", line 170, in run_benchmarks
    result = bench.run(
             ^^^^^^^^^^
  File "/home/ddfun/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/_benchmark.py", line 189, in run
    bench = _run_perf_script(
            ^^^^^^^^^^^^^^^^^
  File "/home/ddfun/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/_benchmark.py", line 240, in _run_perf_script
    raise RuntimeError("Benchmark died")
RuntimeError: Benchmark died
Command failed with exit code 1
```

</details>

## chameleon on windows-x86_64 default

<details>
<summary>Log for chameleon on windows-x86_64 default</summary>

```
    ~~~~^^
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\Lib\site-packages\pyperformance\data-files\benchmarks\bm_chameleon\run_benchmark.py", line 25, in main
    tmpl = PageTemplate(BIGTABLE_ZPT)
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-0db56efbb5b3-compat-cb6a104a6688\Lib\site-packages\chameleon\zpt\template.py", line 205, in __init__
    super(PageTemplate, self).__init__(body, **config)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-0db56efbb5b3-compat-cb6a104a6688\Lib\site-packages\chameleon\template.py", line 137, in __init__
    self.write(body)
    ~~~~~~~~~~^^^^^^
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-0db56efbb5b3-compat-cb6a104a6688\Lib\site-packages\chameleon\template.py", line 235, in write
    self.cook(body)
    ~~~~~~~~~^^^^^^
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-0db56efbb5b3-compat-cb6a104a6688\Lib\site-packages\chameleon\template.py", line 167, in cook
    program = self._cook(body, digest, names)
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-0db56efbb5b3-compat-cb6a104a6688\Lib\site-packages\chameleon\template.py", line 245, in _cook
    source = self._compile(body, builtins)
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-0db56efbb5b3-compat-cb6a104a6688\Lib\site-packages\chameleon\template.py", line 276, in _compile
    program = self.parse(body)
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-0db56efbb5b3-compat-cb6a104a6688\Lib\site-packages\chameleon\zpt\template.py", line 227, in parse
    return MacroProgram(
        body, self.mode, self.filename,
    ...<9 lines>...
        tokenizer=self.tokenizer
    )
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-0db56efbb5b3-compat-cb6a104a6688\Lib\site-packages\chameleon\zpt\program.py", line 174, in __init__
    super(MacroProgram, self).__init__(*args, **kwargs)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-0db56efbb5b3-compat-cb6a104a6688\Lib\site-packages\chameleon\program.py", line 35, in __init__
    node = self.visit(kind, args)
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-0db56efbb5b3-compat-cb6a104a6688\Lib\site-packages\chameleon\program.py", line 41, in visit
    return visitor(*args)
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-0db56efbb5b3-compat-cb6a104a6688\Lib\site-packages\chameleon\zpt\program.py", line 320, in visit_element
    ATTRIBUTES = self._create_attributes_nodes(
        prepared, I18N_ATTRIBUTES, STATIC_ATTRIBUTES,
    )
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-0db56efbb5b3-compat-cb6a104a6688\Lib\site-packages\chameleon\zpt\program.py", line 794, in _create_attributes_nodes
    default = ast.Str(s=text) if text is not None else None
              ^^^^^^^
AttributeError: module 'ast' has no attribute 'Str'
Traceback (most recent call last):
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\Lib\site-packages\pyperformance\run.py", line 170, in run_benchmarks
    result = bench.run(
             ^^^^^^^^^^
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\Lib\site-packages\pyperformance\_benchmark.py", line 189, in run
    bench = _run_perf_script(
            ^^^^^^^^^^^^^^^^^
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\Lib\site-packages\pyperformance\_benchmark.py", line 240, in _run_perf_script
    raise RuntimeError("Benchmark died")
RuntimeError: Benchmark died
Command failed with exit code 1
```

</details>

## chameleon on windows-x86 default

<details>
<summary>Log for chameleon on windows-x86 default</summary>

```
    ~~~~^^
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\Lib\site-packages\pyperformance\data-files\benchmarks\bm_chameleon\run_benchmark.py", line 25, in main
    tmpl = PageTemplate(BIGTABLE_ZPT)
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-1d2c37c6a427-compat-cb6a104a6688\Lib\site-packages\chameleon\zpt\template.py", line 205, in __init__
    super(PageTemplate, self).__init__(body, **config)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-1d2c37c6a427-compat-cb6a104a6688\Lib\site-packages\chameleon\template.py", line 137, in __init__
    self.write(body)
    ~~~~~~~~~~^^^^^^
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-1d2c37c6a427-compat-cb6a104a6688\Lib\site-packages\chameleon\template.py", line 235, in write
    self.cook(body)
    ~~~~~~~~~^^^^^^
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-1d2c37c6a427-compat-cb6a104a6688\Lib\site-packages\chameleon\template.py", line 167, in cook
    program = self._cook(body, digest, names)
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-1d2c37c6a427-compat-cb6a104a6688\Lib\site-packages\chameleon\template.py", line 245, in _cook
    source = self._compile(body, builtins)
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-1d2c37c6a427-compat-cb6a104a6688\Lib\site-packages\chameleon\template.py", line 276, in _compile
    program = self.parse(body)
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-1d2c37c6a427-compat-cb6a104a6688\Lib\site-packages\chameleon\zpt\template.py", line 227, in parse
    return MacroProgram(
        body, self.mode, self.filename,
    ...<9 lines>...
        tokenizer=self.tokenizer
    )
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-1d2c37c6a427-compat-cb6a104a6688\Lib\site-packages\chameleon\zpt\program.py", line 174, in __init__
    super(MacroProgram, self).__init__(*args, **kwargs)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-1d2c37c6a427-compat-cb6a104a6688\Lib\site-packages\chameleon\program.py", line 35, in __init__
    node = self.visit(kind, args)
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-1d2c37c6a427-compat-cb6a104a6688\Lib\site-packages\chameleon\program.py", line 41, in visit
    return visitor(*args)
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-1d2c37c6a427-compat-cb6a104a6688\Lib\site-packages\chameleon\zpt\program.py", line 320, in visit_element
    ATTRIBUTES = self._create_attributes_nodes(
        prepared, I18N_ATTRIBUTES, STATIC_ATTRIBUTES,
    )
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-1d2c37c6a427-compat-cb6a104a6688\Lib\site-packages\chameleon\zpt\program.py", line 794, in _create_attributes_nodes
    default = ast.Str(s=text) if text is not None else None
              ^^^^^^^
AttributeError: module 'ast' has no attribute 'Str'
Traceback (most recent call last):
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\Lib\site-packages\pyperformance\run.py", line 170, in run_benchmarks
    result = bench.run(
             ^^^^^^^^^^
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\Lib\site-packages\pyperformance\_benchmark.py", line 189, in run
    bench = _run_perf_script(
            ^^^^^^^^^^^^^^^^^
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\Lib\site-packages\pyperformance\_benchmark.py", line 240, in _run_perf_script
    raise RuntimeError("Benchmark died")
RuntimeError: Benchmark died
Command failed with exit code 1
```

</details>

## dask on darwin-arm64 default

<details>
<summary>Log for dask on darwin-arm64 default</summary>

```
    return future.result()
           ~~~~~~~~~~~~~^^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_runner.py", line 586, in main
    await local_func()
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.12/site-packages/pyperformance/data-files/benchmarks/bm_dask/run_benchmark.py", line 22, in benchmark
    futures = client.map(inc, range(100))
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688/lib/python3.14/site-packages/distributed/client.py", line 2341, in map
    futures = self._graph_to_futures(
        dsk,
    ...<9 lines>...
        span_metadata=SpanMetadata(collections=[{"type": "Future"}]),
    )
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688/lib/python3.14/site-packages/distributed/client.py", line 3355, in _graph_to_futures
    header, frames = serialize(ToPickle(dsk), on_error="raise")
                     ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688/lib/python3.14/site-packages/distributed/protocol/serialize.py", line 392, in serialize
    raise TypeError(msg, str_x) from exc
TypeError: ('Could not serialize object of type HighLevelGraph', '<ToPickle: HighLevelGraph with 1 layers.\n<dask.highlevelgraph.HighLevelGraph object at 0x102d66e40>\n 0. 4342574320\n>')
Traceback (most recent call last):
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.12/site-packages/pyperformance/data-files/benchmarks/bm_dask/run_benchmark.py", line 32, in <module>
    runner.bench_async_func('dask', benchmark)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_runner.py", line 610, in bench_async_func
    result = self._main(task)
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_runner.py", line 465, in _main
    bench = self._manager()
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_runner.py", line 678, in _manager
    bench = Manager(self).create_bench()
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_manager.py", line 243, in create_bench
    worker_bench, run = self.create_worker_bench()
                        ~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_manager.py", line 142, in create_worker_bench
    suite = self.create_suite()
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_manager.py", line 132, in create_suite
    suite = self.spawn_worker(self.calibrate_loops, 0)
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_manager.py", line 118, in spawn_worker
    raise RuntimeError("%s failed with exit code %s"
                       % (cmd[0], exitcode))
RuntimeError: /Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688/bin/python failed with exit code 1
Traceback (most recent call last):
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.12/site-packages/pyperformance/run.py", line 170, in run_benchmarks
    result = bench.run(
             ^^^^^^^^^^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.12/site-packages/pyperformance/_benchmark.py", line 189, in run
    bench = _run_perf_script(
            ^^^^^^^^^^^^^^^^^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.12/site-packages/pyperformance/_benchmark.py", line 240, in _run_perf_script
    raise RuntimeError("Benchmark died")
RuntimeError: Benchmark died
Command failed with exit code 1
```

</details>

## djangocms on darwin-arm64 default

<details>
<summary>Log for djangocms on darwin-arm64 default</summary>

```
                                   ~~~~^^^^^^^^^^^^^^^^^^^^^^^^
        File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688-bm-djangocms/lib/python3.14/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 251, in build_wheel
          return _build_backend().build_wheel(wheel_directory, config_settings,
                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                                              metadata_directory)
                                              ^^^^^^^^^^^^^^^^^^^
        File "/private/tmp/pip-install-5tc_m67j/pillow_15edd857b8d44e5993b1043f3bb1eb6c/_custom_build/backend.py", line 26, in build_wheel
          return super().build_wheel(wheel_directory, config_settings, metadata_directory)
                 ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "/private/tmp/pip-build-env-3ukpfcjn/overlay/lib/python3.14/site-packages/setuptools/build_meta.py", line 438, in build_wheel
          return _build(['bdist_wheel', '--dist-info-dir', str(metadata_directory)])
        File "/private/tmp/pip-build-env-3ukpfcjn/overlay/lib/python3.14/site-packages/setuptools/build_meta.py", line 426, in _build
          return self._build_with_temp_dir(
                 ~~~~~~~~~~~~~~~~~~~~~~~~~^
              cmd,
              ^^^^
          ...<3 lines>...
              self._arbitrary_args(config_settings),
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          )
          ^
        File "/private/tmp/pip-build-env-3ukpfcjn/overlay/lib/python3.14/site-packages/setuptools/build_meta.py", line 407, in _build_with_temp_dir
          self.run_setup()
          ~~~~~~~~~~~~~~^^
        File "/private/tmp/pip-install-5tc_m67j/pillow_15edd857b8d44e5993b1043f3bb1eb6c/_custom_build/backend.py", line 20, in run_setup
          return super().run_setup(setup_script)
                 ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^
        File "/private/tmp/pip-build-env-3ukpfcjn/overlay/lib/python3.14/site-packages/setuptools/build_meta.py", line 320, in run_setup
          exec(code, locals())
          ~~~~^^^^^^^^^^^^^^^^
        File "<string>", line 1042, in <module>
      RequiredDependencyException:
      
      The headers or library files could not be found for jpeg,
      a required dependency when compiling Pillow from source.
      
      Please see the install instructions at:
         https://pillow.readthedocs.io/en/latest/installation/basic-installation.html
      
      
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for pillow
Failed to build pillow
ERROR: ERROR: Failed to build installable wheels for some pyproject.toml based projects (pillow)
Command failed with exit code 1


==================================================
```

</details>

## djangocms on collect-stats pystats

<details>
<summary>Log for djangocms on collect-stats pystats</summary>

```
Collecting django-sekizai==4.1.0
  Using cached django_sekizai-4.1.0-py3-none-any.whl.metadata (4.6 kB)
Collecting django-treebeard==4.7.1
  Using cached django_treebeard-4.7.1-py3-none-any.whl.metadata (2.7 kB)
Collecting djangocms-admin-style==3.3.1
  Using cached djangocms_admin_style-3.3.1-py3-none-any.whl.metadata (10 kB)
Collecting djangocms-alias==2.0.1
  Using cached djangocms_alias-2.0.1-py3-none-any.whl.metadata (3.7 kB)
Collecting djangocms-attributes-field==3.0.0
  Using cached djangocms_attributes_field-3.0.0-py3-none-any.whl.metadata (7.7 kB)
Collecting djangocms-frontend==1.3.4
  Using cached djangocms_frontend-1.3.4-py3-none-any.whl.metadata (9.3 kB)
Collecting djangocms-text-ckeditor==5.1.6
  Using cached djangocms_text_ckeditor-5.1.6-py3-none-any.whl.metadata (21 kB)
Collecting djangocms-versioning==2.0.2
  Using cached djangocms_versioning-2.0.2-py3-none-any.whl.metadata (4.1 kB)
Collecting easy-thumbnails==2.10
  Using cached easy_thumbnails-2.10-py3-none-any.whl.metadata (15 kB)
Collecting html5lib==1.1
  Using cached html5lib-1.1-py2.py3-none-any.whl.metadata (16 kB)
Collecting idna==3.10
  Using cached idna-3.10-py3-none-any.whl.metadata (10 kB)
Collecting lxml==5.3.0
  Using cached lxml-5.3.0.tar.gz (3.7 MB)
  Installing build dependencies: started
  Installing build dependencies: finished with status 'done'
  Getting requirements to build wheel: started
  Getting requirements to build wheel: finished with status 'error'
  error: subprocess-exited-with-error
  
  × Getting requirements to build wheel did not run successfully.
  │ exit code: 1
  ╰─> [4 lines of output]
      <string>:67: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
      Building lxml version 5.3.0.
      Building without Cython.
      Error: Please make sure the libxml2 and libxslt development packages are installed.
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
error: subprocess-exited-with-error

× Getting requirements to build wheel did not run successfully.
│ exit code: 1
╰─> See above for output.

note: This error originates from a subprocess, and is likely not a problem with pip.
Command failed with exit code 1


```

</details>

## djangocms on windows-x86_64 default

<details>
<summary>Log for djangocms on windows-x86_64 default</summary>

```
    File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-0db56efbb5b3-compat-cb6a104a6688-bm-djangocms\Lib\site-packages\pip\_vendor\pyproject_hooks\_in_process\_in_process.py", line 251, in build_wheel
      return _build_backend().build_wheel(wheel_directory, config_settings,
             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                                          metadata_directory)
                                          ^^^^^^^^^^^^^^^^^^^
    File "C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\pip-install-7ifcfgty\pillow_5b44722dab9e4f3089a803b80cecd982\_custom_build\backend.py", line 26, in build_wheel
      return super().build_wheel(wheel_directory, config_settings, metadata_directory)
             ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\pip-build-env-9wlxfayr\overlay\Lib\site-packages\setuptools\build_meta.py", line 438, in build_wheel
      return _build(['bdist_wheel', '--dist-info-dir', str(metadata_directory)])
    File "C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\pip-build-env-9wlxfayr\overlay\Lib\site-packages\setuptools\build_meta.py", line 426, in _build
      return self._build_with_temp_dir(
             ~~~~~~~~~~~~~~~~~~~~~~~~~^
          cmd,
          ^^^^
      ...<3 lines>...
          self._arbitrary_args(config_settings),
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      )
      ^
    File "C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\pip-build-env-9wlxfayr\overlay\Lib\site-packages\setuptools\build_meta.py", line 407, in _build_with_temp_dir
      self.run_setup()
      ~~~~~~~~~~~~~~^^
    File "C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\pip-install-7ifcfgty\pillow_5b44722dab9e4f3089a803b80cecd982\_custom_build\backend.py", line 20, in run_setup
      return super().run_setup(setup_script)
             ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^
    File "C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\pip-build-env-9wlxfayr\overlay\Lib\site-packages\setuptools\build_meta.py", line 320, in run_setup
      exec(code, locals())
      ~~~~^^^^^^^^^^^^^^^^
    File "<string>", line 1042, in <module>
  RequiredDependencyException:
  
  The headers or library files could not be found for zlib,
  a required dependency when compiling Pillow from source.
  
  Please see the install instructions at:
     https://pillow.readthedocs.io/en/latest/installation/basic-installation.html
  
  
  <string>:52: RuntimeWarning: Pillow 11.0.0 does not support Python 3.14 and does not provide prebuilt Windows binaries. We do not recommend building from source on Windows.
  [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for pillow
Failed to build lxml pillow
ERROR: ERROR: Failed to build installable wheels for some pyproject.toml based projects (lxml, pillow)
Command failed with exit code 1


==================================================
```

</details>

## djangocms on windows-x86 default

<details>
<summary>Log for djangocms on windows-x86 default</summary>

```
    File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-1d2c37c6a427-compat-cb6a104a6688-bm-djangocms\Lib\site-packages\pip\_vendor\pyproject_hooks\_in_process\_in_process.py", line 251, in build_wheel
      return _build_backend().build_wheel(wheel_directory, config_settings,
             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                                          metadata_directory)
                                          ^^^^^^^^^^^^^^^^^^^
    File "C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\pip-install-5se7imyb\pillow_93cf65ab80b845b99faa584e57c676b9\_custom_build\backend.py", line 26, in build_wheel
      return super().build_wheel(wheel_directory, config_settings, metadata_directory)
             ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\pip-build-env-fsf6khl0\overlay\Lib\site-packages\setuptools\build_meta.py", line 438, in build_wheel
      return _build(['bdist_wheel', '--dist-info-dir', str(metadata_directory)])
    File "C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\pip-build-env-fsf6khl0\overlay\Lib\site-packages\setuptools\build_meta.py", line 426, in _build
      return self._build_with_temp_dir(
             ~~~~~~~~~~~~~~~~~~~~~~~~~^
          cmd,
          ^^^^
      ...<3 lines>...
          self._arbitrary_args(config_settings),
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      )
      ^
    File "C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\pip-build-env-fsf6khl0\overlay\Lib\site-packages\setuptools\build_meta.py", line 407, in _build_with_temp_dir
      self.run_setup()
      ~~~~~~~~~~~~~~^^
    File "C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\pip-install-5se7imyb\pillow_93cf65ab80b845b99faa584e57c676b9\_custom_build\backend.py", line 20, in run_setup
      return super().run_setup(setup_script)
             ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^
    File "C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\pip-build-env-fsf6khl0\overlay\Lib\site-packages\setuptools\build_meta.py", line 320, in run_setup
      exec(code, locals())
      ~~~~^^^^^^^^^^^^^^^^
    File "<string>", line 1042, in <module>
  RequiredDependencyException:
  
  The headers or library files could not be found for zlib,
  a required dependency when compiling Pillow from source.
  
  Please see the install instructions at:
     https://pillow.readthedocs.io/en/latest/installation/basic-installation.html
  
  
  <string>:52: RuntimeWarning: Pillow 11.0.0 does not support Python 3.14 and does not provide prebuilt Windows binaries. We do not recommend building from source on Windows.
  [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for pillow
Failed to build lxml pillow
ERROR: ERROR: Failed to build installable wheels for some pyproject.toml based projects (lxml, pillow)
Command failed with exit code 1


==================================================
```

</details>

## djangocms on linux-aarch64 nogil

<details>
<summary>Log for djangocms on linux-aarch64 nogil</summary>

```
      copying src/lxml/includes/etree_defs.h -> build/lib.linux-aarch64-cpython-314t/lxml/includes
      copying src/lxml/includes/lxml-version.h -> build/lib.linux-aarch64-cpython-314t/lxml/includes
      creating build/lib.linux-aarch64-cpython-314t/lxml/isoschematron/resources/rng
      copying src/lxml/isoschematron/resources/rng/iso-schematron.rng -> build/lib.linux-aarch64-cpython-314t/lxml/isoschematron/resources/rng
      creating build/lib.linux-aarch64-cpython-314t/lxml/isoschematron/resources/xsl
      copying src/lxml/isoschematron/resources/xsl/XSD2Schtrn.xsl -> build/lib.linux-aarch64-cpython-314t/lxml/isoschematron/resources/xsl
      copying src/lxml/isoschematron/resources/xsl/RNG2Schtrn.xsl -> build/lib.linux-aarch64-cpython-314t/lxml/isoschematron/resources/xsl
      creating build/lib.linux-aarch64-cpython-314t/lxml/isoschematron/resources/xsl/iso-schematron-xslt1
      copying src/lxml/isoschematron/resources/xsl/iso-schematron-xslt1/iso_abstract_expand.xsl -> build/lib.linux-aarch64-cpython-314t/lxml/isoschematron/resources/xsl/iso-schematron-xslt1
      copying src/lxml/isoschematron/resources/xsl/iso-schematron-xslt1/iso_schematron_message.xsl -> build/lib.linux-aarch64-cpython-314t/lxml/isoschematron/resources/xsl/iso-schematron-xslt1
      copying src/lxml/isoschematron/resources/xsl/iso-schematron-xslt1/iso_dsdl_include.xsl -> build/lib.linux-aarch64-cpython-314t/lxml/isoschematron/resources/xsl/iso-schematron-xslt1
      copying src/lxml/isoschematron/resources/xsl/iso-schematron-xslt1/iso_svrl_for_xslt1.xsl -> build/lib.linux-aarch64-cpython-314t/lxml/isoschematron/resources/xsl/iso-schematron-xslt1
      copying src/lxml/isoschematron/resources/xsl/iso-schematron-xslt1/iso_schematron_skeleton_for_xslt1.xsl -> build/lib.linux-aarch64-cpython-314t/lxml/isoschematron/resources/xsl/iso-schematron-xslt1
      copying src/lxml/isoschematron/resources/xsl/iso-schematron-xslt1/readme.txt -> build/lib.linux-aarch64-cpython-314t/lxml/isoschematron/resources/xsl/iso-schematron-xslt1
      running build_ext
      building 'lxml.etree' extension
      creating build/temp.linux-aarch64-cpython-314t/src/lxml
      gcc -fno-strict-overflow -Wsign-compare -DNDEBUG -g -O3 -Wall -fPIC -DCYTHON_CLINE_IN_TRACEBACK=0 -I/usr/include/libxml2 -Isrc -Isrc/lxml/includes -I/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-d2066009c166-compat-cb6a104a6688-bm-djangocms/include -I/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/cpython/Include -I/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/cpython -c src/lxml/etree.c -o build/temp.linux-aarch64-cpython-314t/src/lxml/etree.o -w
      src/lxml/etree.c:7210:80: error: unknown type name ‘__pyx_vectorcallfunc’; did you mean ‘vectorcallfunc’?
       7210 | static CYTHON_INLINE PyObject *__Pyx_PyVectorcall_FastCallDict(PyObject *func, __pyx_vectorcallfunc vc, PyObject *const *args, size_t nargs, PyObject *kw);
            |                                                                                ^~~~~~~~~~~~~~~~~~~~
            |                                                                                vectorcallfunc
      src/lxml/etree.c:299050:69: error: unknown type name ‘__pyx_vectorcallfunc’; did you mean ‘vectorcallfunc’?
      299050 | static PyObject *__Pyx_PyVectorcall_FastCallDict_kw(PyObject *func, __pyx_vectorcallfunc vc, PyObject *const *args, size_t nargs, PyObject *kw)
             |                                                                     ^~~~~~~~~~~~~~~~~~~~
             |                                                                     vectorcallfunc
      src/lxml/etree.c:299095:80: error: unknown type name ‘__pyx_vectorcallfunc’; did you mean ‘vectorcallfunc’?
      299095 | static CYTHON_INLINE PyObject *__Pyx_PyVectorcall_FastCallDict(PyObject *func, __pyx_vectorcallfunc vc, PyObject *const *args, size_t nargs, PyObject *kw)
             |                                                                                ^~~~~~~~~~~~~~~~~~~~
             |                                                                                vectorcallfunc
      src/lxml/etree.c: In function ‘__Pyx_CyFunction_CallAsMethod’:
      src/lxml/etree.c:299784:6: error: unknown type name ‘__pyx_vectorcallfunc’; did you mean ‘vectorcallfunc’?
      299784 |      __pyx_vectorcallfunc vc = __Pyx_CyFunction_func_vectorcall(cyfunc);
             |      ^~~~~~~~~~~~~~~~~~~~
             |      vectorcallfunc
      Compile failed: command '/usr/bin/gcc' failed with exit code 1
      creating tmp
      cc -I/usr/include/libxml2 -I/usr/include/libxml2 -c /tmp/xmlXPathInitp2ofgffv.c -o tmp/xmlXPathInitp2ofgffv.o
      cc tmp/xmlXPathInitp2ofgffv.o -lxml2 -o a.out
      error: command '/usr/bin/gcc' failed with exit code 1
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for lxml
Failed to build lxml
ERROR: ERROR: Failed to build installable wheels for some pyproject.toml based projects (lxml)
Command failed with exit code 1


==================================================
```

</details>

## djangocms on linux-x86_64 nogil

<details>
<summary>Log for djangocms on linux-x86_64 nogil</summary>

```
      copying src/lxml/includes/etree_defs.h -> build/lib.linux-x86_64-cpython-314t/lxml/includes
      copying src/lxml/includes/lxml-version.h -> build/lib.linux-x86_64-cpython-314t/lxml/includes
      creating build/lib.linux-x86_64-cpython-314t/lxml/isoschematron/resources/rng
      copying src/lxml/isoschematron/resources/rng/iso-schematron.rng -> build/lib.linux-x86_64-cpython-314t/lxml/isoschematron/resources/rng
      creating build/lib.linux-x86_64-cpython-314t/lxml/isoschematron/resources/xsl
      copying src/lxml/isoschematron/resources/xsl/RNG2Schtrn.xsl -> build/lib.linux-x86_64-cpython-314t/lxml/isoschematron/resources/xsl
      copying src/lxml/isoschematron/resources/xsl/XSD2Schtrn.xsl -> build/lib.linux-x86_64-cpython-314t/lxml/isoschematron/resources/xsl
      creating build/lib.linux-x86_64-cpython-314t/lxml/isoschematron/resources/xsl/iso-schematron-xslt1
      copying src/lxml/isoschematron/resources/xsl/iso-schematron-xslt1/iso_dsdl_include.xsl -> build/lib.linux-x86_64-cpython-314t/lxml/isoschematron/resources/xsl/iso-schematron-xslt1
      copying src/lxml/isoschematron/resources/xsl/iso-schematron-xslt1/iso_schematron_skeleton_for_xslt1.xsl -> build/lib.linux-x86_64-cpython-314t/lxml/isoschematron/resources/xsl/iso-schematron-xslt1
      copying src/lxml/isoschematron/resources/xsl/iso-schematron-xslt1/iso_schematron_message.xsl -> build/lib.linux-x86_64-cpython-314t/lxml/isoschematron/resources/xsl/iso-schematron-xslt1
      copying src/lxml/isoschematron/resources/xsl/iso-schematron-xslt1/iso_svrl_for_xslt1.xsl -> build/lib.linux-x86_64-cpython-314t/lxml/isoschematron/resources/xsl/iso-schematron-xslt1
      copying src/lxml/isoschematron/resources/xsl/iso-schematron-xslt1/iso_abstract_expand.xsl -> build/lib.linux-x86_64-cpython-314t/lxml/isoschematron/resources/xsl/iso-schematron-xslt1
      copying src/lxml/isoschematron/resources/xsl/iso-schematron-xslt1/readme.txt -> build/lib.linux-x86_64-cpython-314t/lxml/isoschematron/resources/xsl/iso-schematron-xslt1
      running build_ext
      building 'lxml.etree' extension
      creating build/temp.linux-x86_64-cpython-314t/src/lxml
      gcc -fno-strict-overflow -Wsign-compare -DNDEBUG -g -O3 -Wall -fPIC -DCYTHON_CLINE_IN_TRACEBACK=0 -I/usr/include/libxml2 -Isrc -Isrc/lxml/includes -I/home/ddfun/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-92cb9f5c0683-compat-cb6a104a6688-bm-djangocms/include -I/home/ddfun/actions-runner/_work/benchmarking/benchmarking/cpython/Include -I/home/ddfun/actions-runner/_work/benchmarking/benchmarking/cpython -c src/lxml/etree.c -o build/temp.linux-x86_64-cpython-314t/src/lxml/etree.o -w
      src/lxml/etree.c:7210:80: error: unknown type name ‘__pyx_vectorcallfunc’; did you mean ‘vectorcallfunc’?
       7210 | static CYTHON_INLINE PyObject *__Pyx_PyVectorcall_FastCallDict(PyObject *func, __pyx_vectorcallfunc vc, PyObject *const *args, size_t nargs, PyObject *kw);
            |                                                                                ^~~~~~~~~~~~~~~~~~~~
            |                                                                                vectorcallfunc
      src/lxml/etree.c:299050:69: error: unknown type name ‘__pyx_vectorcallfunc’; did you mean ‘vectorcallfunc’?
      299050 | static PyObject *__Pyx_PyVectorcall_FastCallDict_kw(PyObject *func, __pyx_vectorcallfunc vc, PyObject *const *args, size_t nargs, PyObject *kw)
             |                                                                     ^~~~~~~~~~~~~~~~~~~~
             |                                                                     vectorcallfunc
      src/lxml/etree.c:299095:80: error: unknown type name ‘__pyx_vectorcallfunc’; did you mean ‘vectorcallfunc’?
      299095 | static CYTHON_INLINE PyObject *__Pyx_PyVectorcall_FastCallDict(PyObject *func, __pyx_vectorcallfunc vc, PyObject *const *args, size_t nargs, PyObject *kw)
             |                                                                                ^~~~~~~~~~~~~~~~~~~~
             |                                                                                vectorcallfunc
      src/lxml/etree.c: In function ‘__Pyx_CyFunction_CallAsMethod’:
      src/lxml/etree.c:299784:6: error: unknown type name ‘__pyx_vectorcallfunc’; did you mean ‘vectorcallfunc’?
      299784 |      __pyx_vectorcallfunc vc = __Pyx_CyFunction_func_vectorcall(cyfunc);
             |      ^~~~~~~~~~~~~~~~~~~~
             |      vectorcallfunc
      Compile failed: command '/usr/bin/gcc' failed with exit code 1
      creating tmp
      cc -I/usr/include/libxml2 -I/usr/include/libxml2 -c /tmp/xmlXPathInitfzqraqzj.c -o tmp/xmlXPathInitfzqraqzj.o
      cc tmp/xmlXPathInitfzqraqzj.o -lxml2 -o a.out
      error: command '/usr/bin/gcc' failed with exit code 1
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for lxml
Failed to build lxml
ERROR: ERROR: Failed to build installable wheels for some pyproject.toml based projects (lxml)
Command failed with exit code 1


==================================================
```

</details>

## flaskblogging on darwin-arm64 default

<details>
<summary>Log for flaskblogging on darwin-arm64 default</summary>

```
# /Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688/bin/python -u /Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_flaskblogging/run_benchmark.py --inherit-environ PYPERFORMANCE_RUNID,PYTHON_JIT --output /tmp/tmp33zhuwd5
Traceback (most recent call last):
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_flaskblogging/run_benchmark.py", line 76, in <module>
    with context:
         ^^^^^^^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/cpython/Lib/contextlib.py", line 141, in __enter__
    return next(self.gen)
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_flaskblogging/netutils.py", line 36, in serving
    waitUntilUp(addr)
    ~~~~~~~~~~~^^^^^^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_flaskblogging/netutils.py", line 66, in waitUntilUp
    raise Exception('Timeout reached when trying to connect')
Exception: Timeout reached when trying to connect
Traceback (most recent call last):
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.12/site-packages/pyperformance/run.py", line 170, in run_benchmarks
    result = bench.run(
             ^^^^^^^^^^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.12/site-packages/pyperformance/_benchmark.py", line 189, in run
    bench = _run_perf_script(
            ^^^^^^^^^^^^^^^^^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.12/site-packages/pyperformance/_benchmark.py", line 240, in _run_perf_script
    raise RuntimeError("Benchmark died")
RuntimeError: Benchmark died
Command failed with exit code 1
```

</details>

## flaskblogging on linux-aarch64 default

<details>
<summary>Log for flaskblogging on linux-aarch64 default</summary>

```
# /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-6e18c82301b6-compat-cb6a104a6688/bin/python -u /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_flaskblogging/run_benchmark.py --inherit-environ PYPERFORMANCE_RUNID,PYTHON_JIT --output /tmp/tmpwc0yif73
Traceback (most recent call last):
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_flaskblogging/run_benchmark.py", line 76, in <module>
    with context:
         ^^^^^^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/cpython/Lib/contextlib.py", line 141, in __enter__
    return next(self.gen)
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_flaskblogging/netutils.py", line 36, in serving
    waitUntilUp(addr)
    ~~~~~~~~~~~^^^^^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_flaskblogging/netutils.py", line 66, in waitUntilUp
    raise Exception('Timeout reached when trying to connect')
Exception: Timeout reached when trying to connect
Traceback (most recent call last):
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/run.py", line 170, in run_benchmarks
    result = bench.run(
             ^^^^^^^^^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/_benchmark.py", line 189, in run
    bench = _run_perf_script(
            ^^^^^^^^^^^^^^^^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/_benchmark.py", line 240, in _run_perf_script
    raise RuntimeError("Benchmark died")
RuntimeError: Benchmark died
Command failed with exit code 1
```

</details>

## flaskblogging on collect-stats pystats

<details>
<summary>Log for flaskblogging on collect-stats pystats</summary>

```
##[error]    raise Exception('Timeout reached when trying to connect')
Exception: Timeout reached when trying to connect
Traceback (most recent call last):
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/run.py", line 170, in run_benchmarks
    result = bench.run(
             ^^^^^^^^^^
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/_benchmark.py", line 189, in run
    bench = _run_perf_script(
            ^^^^^^^^^^^^^^^^^
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/_benchmark.py", line 240, in _run_perf_script
    raise RuntimeError("Benchmark died")
RuntimeError: Benchmark died
Command failed with exit code 1

ERROR: No benchmark was run
Environment variables:
PYTHON_JIT=<unset>
RUNNING: /home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/bin/python -m pyperformance run -o benchmark.json --manifest benchmarks.manifest --benchmarks 2to3 --python cpython/python --inherit-environ PYTHON_JIT --same-loops loops.json --hook pystats
RUNNING: /home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/bin/python -m pyperformance run -o benchmark.json --manifest benchmarks.manifest --benchmarks argparse --python cpython/python --inherit-environ PYTHON_JIT --same-loops loops.json --hook pystats
RUNNING: /home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/bin/python -m pyperformance run -o benchmark.json --manifest benchmarks.manifest --benchmarks argparse_subparsers --python cpython/python --inherit-environ PYTHON_JIT --same-loops loops.json --hook pystats
RUNNING: /home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/bin/python -m pyperformance run -o benchmark.json --manifest benchmarks.manifest --benchmarks async_generators --python cpython/python --inherit-environ PYTHON_JIT --same-loops loops.json --hook pystats
RUNNING: /home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/bin/python -m pyperformance run -o benchmark.json --manifest benchmarks.manifest --benchmarks async_tree --python cpython/python --inherit-environ PYTHON_JIT --same-loops loops.json --hook pystats
RUNNING: /home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/bin/python -m pyperformance run -o benchmark.json --manifest benchmarks.manifest --benchmarks async_tree_cpu_io_mixed --python cpython/python --inherit-environ PYTHON_JIT --same-loops loops.json --hook pystats
RUNNING: /home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/bin/python -m pyperformance run -o benchmark.json --manifest benchmarks.manifest --benchmarks async_tree_cpu_io_mixed_tg --python cpython/python --inherit-environ PYTHON_JIT --same-loops loops.json --hook pystats
RUNNING: /home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/bin/python -m pyperformance run -o benchmark.json --manifest benchmarks.manifest --benchmarks async_tree_io --python cpython/python --inherit-environ PYTHON_JIT --same-loops loops.json --hook pystats
RUNNING: /home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/bin/python -m pyperformance run -o benchmark.json --manifest benchmarks.manifest --benchmarks async_tree_io_tg --python cpython/python --inherit-environ PYTHON_JIT --same-loops loops.json --hook pystats
RUNNING: /home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/bin/python -m pyperformance run -o benchmark.json --manifest benchmarks.manifest --benchmarks async_tree_memoization --python cpython/python --inherit-environ PYTHON_JIT --same-loops loops.json --hook pystats
RUNNING: /home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/bin/python -m pyperformance run -o benchmark.json --manifest benchmarks.manifest --benchmarks async_tree_memoization_tg --python cpython/python --inherit-environ PYTHON_JIT --same-loops loops.json --hook pystats
RUNNING: /home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/bin/python -m pyperformance run -o benchmark.json --manifest benchmarks.manifest --benchmarks async_tree_tg --python cpython/python --inherit-environ PYTHON_JIT --same-loops loops.json --hook pystats
RUNNING: /home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/bin/python -m pyperformance run -o benchmark.json --manifest benchmarks.manifest --benchmarks asyncio_websockets --python cpython/python --inherit-environ PYTHON_JIT --same-loops loops.json --hook pystats
RUNNING: /home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/bin/python -m pyperformance run -o benchmark.json --manifest benchmarks.manifest --benchmarks bpe_tokeniser --python cpython/python --inherit-environ PYTHON_JIT --same-loops loops.json --hook pystats
RUNNING: /home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/bin/python -m pyperformance run -o benchmark.json --manifest benchmarks.manifest --benchmarks chameleon --python cpython/python --inherit-environ PYTHON_JIT --same-loops loops.json --hook pystats
RUNNING: /home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/bin/python -m pyperformance run -o benchmark.json --manifest benchmarks.manifest --benchmarks chaos --python cpython/python --inherit-environ PYTHON_JIT --same-loops loops.json --hook pystats
RUNNING: /home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/bin/python -m pyperformance run -o benchmark.json --manifest benchmarks.manifest --benchmarks comprehensions --python cpython/python --inherit-environ PYTHON_JIT --same-loops loops.json --hook pystats
RUNNING: /home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/bin/python -m pyperformance run -o benchmark.json --manifest benchmarks.manifest --benchmarks concurrent_imap --python cpython/python --inherit-environ PYTHON_JIT --same-loops loops.json --hook pystats
RUNNING: /home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/bin/python -m pyperformance run -o benchmark.json --manifest benchmarks.manifest --benchmarks coroutines --python cpython/python --inherit-environ PYTHON_JIT --same-loops loops.json --hook pystats
RUNNING: /home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/bin/python -m pyperformance run -o benchmark.json --manifest benchmarks.manifest --benchmarks coverage --python cpython/python --inherit-environ PYTHON_JIT --same-loops loops.json --hook pystats
RUNNING: /home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/bin/python -m pyperformance run -o benchmark.json --manifest benchmarks.manifest --benchmarks crypto_pyaes --python cpython/python --inherit-environ PYTHON_JIT --same-loops loops.json --hook pystats
RUNNING: /home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/bin/python -m pyperformance run -o benchmark.json --manifest benchmarks.manifest --benchmarks deepcopy --python cpython/python --inherit-environ PYTHON_JIT --same-loops loops.json --hook pystats
RUNNING: /home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/bin/python -m pyperformance run -o benchmark.json --manifest benchmarks.manifest --benchmarks deltablue --python cpython/python --inherit-environ PYTHON_JIT --same-loops loops.json --hook pystats
RUNNING: /home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/bin/python -m pyperformance run -o benchmark.json --manifest benchmarks.manifest --benchmarks django_template --python cpython/python --inherit-environ PYTHON_JIT --same-loops loops.json --hook pystats
RUNNING: /home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/bin/python -m pyperformance run -o benchmark.json --manifest benchmarks.manifest --benchmarks djangocms --python cpython/python --inherit-environ PYTHON_JIT --same-loops loops.json --hook pystats
RUNNING: /home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/bin/python -m pyperformance run -o benchmark.json --manifest benchmarks.manifest --benchmarks docutils --python cpython/python --inherit-environ PYTHON_JIT --same-loops loops.json --hook pystats
RUNNING: /home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/bin/python -m pyperformance run -o benchmark.json --manifest benchmarks.manifest --benchmarks dulwich_log --python cpython/python --inherit-environ PYTHON_JIT --same-loops loops.json --hook pystats
RUNNING: /home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/bin/python -m pyperformance run -o benchmark.json --manifest benchmarks.manifest --benchmarks fannkuch --python cpython/python --inherit-environ PYTHON_JIT --same-loops loops.json --hook pystats
RUNNING: /home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/bin/python -m pyperformance run -o benchmark.json --manifest benchmarks.manifest --benchmarks flaskblogging --python cpython/python --inherit-environ PYTHON_JIT --same-loops loops.json --hook pystats
Python benchmark suite 1.11.0


==================================================
```

</details>

## flaskblogging on linux-x86_64 default

<details>
<summary>Log for flaskblogging on linux-x86_64 default</summary>

```
# /home/ddfun/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0e992284450f-compat-cb6a104a6688/bin/python -u /home/ddfun/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_flaskblogging/run_benchmark.py --inherit-environ PYTHON_JIT,PYPERFORMANCE_RUNID --output /tmp/tmpdi_e6rep
Traceback (most recent call last):
  File "/home/ddfun/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_flaskblogging/run_benchmark.py", line 76, in <module>
    with context:
         ^^^^^^^
  File "/home/ddfun/actions-runner/_work/benchmarking/benchmarking/cpython/Lib/contextlib.py", line 141, in __enter__
    return next(self.gen)
  File "/home/ddfun/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_flaskblogging/netutils.py", line 36, in serving
    waitUntilUp(addr)
    ~~~~~~~~~~~^^^^^^
  File "/home/ddfun/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_flaskblogging/netutils.py", line 66, in waitUntilUp
##[error]    raise Exception('Timeout reached when trying to connect')
Exception: Timeout reached when trying to connect
Traceback (most recent call last):
  File "/home/ddfun/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/run.py", line 170, in run_benchmarks
    result = bench.run(
             ^^^^^^^^^^
  File "/home/ddfun/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/_benchmark.py", line 189, in run
    bench = _run_perf_script(
            ^^^^^^^^^^^^^^^^^
  File "/home/ddfun/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/_benchmark.py", line 240, in _run_perf_script
    raise RuntimeError("Benchmark died")
RuntimeError: Benchmark died
Command failed with exit code 1
```

</details>

## flaskblogging on windows-x86_64 default

<details>
<summary>Log for flaskblogging on windows-x86_64 default</summary>

```
# 'C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-0db56efbb5b3-compat-cb6a104a6688\Scripts\python.exe' -u 'C:\actions-runner\_work\benchmarking\benchmarking\pyston-benchmarks\benchmarks\bm_flaskblogging\run_benchmark.py' --inherit-environ PYPERFORMANCE_RUNID,PYTHON_JIT --output 'C:\WINDOWS\SERVIC~1\NETWOR~1\AppData\Local\Temp\tmp0ew728iq'
Traceback (most recent call last):
Command failed with exit code 1
  File "C:\actions-runner\_work\benchmarking\benchmarking\pyston-benchmarks\benchmarks\bm_flaskblogging\run_benchmark.py", line 76, in <module>
```

</details>

## flaskblogging on windows-x86 default

<details>
<summary>Log for flaskblogging on windows-x86 default</summary>

```
# 'C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-1d2c37c6a427-compat-cb6a104a6688\Scripts\python.exe' -u 'C:\actions-runner\_work\benchmarking\benchmarking\pyston-benchmarks\benchmarks\bm_flaskblogging\run_benchmark.py' --inherit-environ PYTHON_JIT,PYPERFORMANCE_RUNID --output 'C:\WINDOWS\SERVIC~1\NETWOR~1\AppData\Local\Temp\tmpv2d1y8_i'
Traceback (most recent call last):
  File "C:\actions-runner\_work\benchmarking\benchmarking\pyston-benchmarks\benchmarks\bm_flaskblogging\run_benchmark.py", line 76, in <module>
    with context:
         ^^^^^^^
  File "C:\actions-runner\_work\benchmarking\benchmarking\cpython\Lib\contextlib.py", line 141, in __enter__
    return next(self.gen)
  File "C:\actions-runner\_work\benchmarking\benchmarking\pyston-benchmarks\benchmarks\bm_flaskblogging\netutils.py", line 36, in serving
    waitUntilUp(addr)
    ~~~~~~~~~~~^^^^^^
  File "C:\actions-runner\_work\benchmarking\benchmarking\pyston-benchmarks\benchmarks\bm_flaskblogging\netutils.py", line 66, in waitUntilUp
    raise Exception('Timeout reached when trying to connect')
Exception: Timeout reached when trying to connect
Traceback (most recent call last):
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\Lib\site-packages\pyperformance\run.py", line 170, in run_benchmarks
    result = bench.run(
             ^^^^^^^^^^
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\Lib\site-packages\pyperformance\_benchmark.py", line 189, in run
    bench = _run_perf_script(
            ^^^^^^^^^^^^^^^^^
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\Lib\site-packages\pyperformance\_benchmark.py", line 240, in _run_perf_script
    raise RuntimeError("Benchmark died")
RuntimeError: Benchmark died
Command failed with exit code 1
```

</details>

## gevent_hub on darwin-arm64 default

<details>
<summary>Log for gevent_hub on darwin-arm64 default</summary>

```
    import gevent
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688/lib/python3.14/site-packages/gevent/__init__.py", line 71, in <module>
    from gevent._config import config
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688/lib/python3.14/site-packages/gevent/_config.py", line 730, in <module>
    Loop().get()
    ~~~~~~~~~~^^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688/lib/python3.14/site-packages/gevent/_config.py", line 151, in get
    self.value = self.validate(self._default())
                 ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688/lib/python3.14/site-packages/gevent/_config.py", line 259, in validate
    return self._import_one_of([self.shortname_map.get(x, x) for x in value])
           ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688/lib/python3.14/site-packages/gevent/_config.py", line 230, in _import_one_of
    return self._import_one(item)
           ~~~~~~~~~~~~~~~~^^^^^^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688/lib/python3.14/site-packages/gevent/_config.py", line 248, in _import_one
    module = importlib.import_module(module)
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/cpython/Lib/importlib/__init__.py", line 88, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "src/gevent/libev/corecext.pyx", line 819, in init gevent.libev.corecext
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/__init__.py", line 58, in <module>
    _wire()
    ~~~~~^^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 1154, in _wire
    from zope.interface.interfaces import IElement
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interfaces.py", line 56, in <module>
    class IElement(Interface):
    ...<93 lines>...
            """
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 794, in __init__
    self.__attrs = self.__compute_attrs(attrs)
                   ~~~~~~~~~~~~~~~~~~~~^^^^^^^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 813, in __compute_attrs
    aname: update_value(aname, aval)
           ~~~~~~~~~~~~^^^^^^^^^^^^^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 809, in update_value
    raise InvalidInterface("Concrete attribute, " + aname)
zope.interface.exceptions.InvalidInterface: Concrete attribute, __classdictcell__
Traceback (most recent call last):
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.12/site-packages/pyperformance/run.py", line 170, in run_benchmarks
    result = bench.run(
             ^^^^^^^^^^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.12/site-packages/pyperformance/_benchmark.py", line 189, in run
    bench = _run_perf_script(
            ^^^^^^^^^^^^^^^^^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.12/site-packages/pyperformance/_benchmark.py", line 240, in _run_perf_script
    raise RuntimeError("Benchmark died")
RuntimeError: Benchmark died
Command failed with exit code 1
```

</details>

## gevent_hub on linux-aarch64 default

<details>
<summary>Log for gevent_hub on linux-aarch64 default</summary>

```
    import gevent
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-6e18c82301b6-compat-cb6a104a6688/lib/python3.14/site-packages/gevent/__init__.py", line 71, in <module>
    from gevent._config import config
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-6e18c82301b6-compat-cb6a104a6688/lib/python3.14/site-packages/gevent/_config.py", line 730, in <module>
    Loop().get()
    ~~~~~~~~~~^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-6e18c82301b6-compat-cb6a104a6688/lib/python3.14/site-packages/gevent/_config.py", line 151, in get
    self.value = self.validate(self._default())
                 ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-6e18c82301b6-compat-cb6a104a6688/lib/python3.14/site-packages/gevent/_config.py", line 259, in validate
    return self._import_one_of([self.shortname_map.get(x, x) for x in value])
           ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-6e18c82301b6-compat-cb6a104a6688/lib/python3.14/site-packages/gevent/_config.py", line 230, in _import_one_of
    return self._import_one(item)
           ~~~~~~~~~~~~~~~~^^^^^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-6e18c82301b6-compat-cb6a104a6688/lib/python3.14/site-packages/gevent/_config.py", line 248, in _import_one
    module = importlib.import_module(module)
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/cpython/Lib/importlib/__init__.py", line 88, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "src/gevent/libev/corecext.pyx", line 819, in init gevent.libev.corecext
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-6e18c82301b6-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/__init__.py", line 58, in <module>
    _wire()
    ~~~~~^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-6e18c82301b6-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 1154, in _wire
    from zope.interface.interfaces import IElement
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-6e18c82301b6-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interfaces.py", line 56, in <module>
    class IElement(Interface):
    ...<93 lines>...
            """
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-6e18c82301b6-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 794, in __init__
    self.__attrs = self.__compute_attrs(attrs)
                   ~~~~~~~~~~~~~~~~~~~~^^^^^^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-6e18c82301b6-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 813, in __compute_attrs
    aname: update_value(aname, aval)
           ~~~~~~~~~~~~^^^^^^^^^^^^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-6e18c82301b6-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 809, in update_value
    raise InvalidInterface("Concrete attribute, " + aname)
zope.interface.exceptions.InvalidInterface: Concrete attribute, __classdictcell__
Traceback (most recent call last):
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/run.py", line 170, in run_benchmarks
    result = bench.run(
             ^^^^^^^^^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/_benchmark.py", line 189, in run
    bench = _run_perf_script(
            ^^^^^^^^^^^^^^^^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/_benchmark.py", line 240, in _run_perf_script
    raise RuntimeError("Benchmark died")
RuntimeError: Benchmark died
Command failed with exit code 1
```

</details>

## gevent_hub on collect-stats pystats

<details>
<summary>Log for gevent_hub on collect-stats pystats</summary>

```
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-7c12bab99a20-compat-cb6a104a6688/lib/python3.14/site-packages/gevent/_config.py", line 151, in get
    self.value = self.validate(self._default())
                 ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-7c12bab99a20-compat-cb6a104a6688/lib/python3.14/site-packages/gevent/_config.py", line 259, in validate
    return self._import_one_of([self.shortname_map.get(x, x) for x in value])
           ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-7c12bab99a20-compat-cb6a104a6688/lib/python3.14/site-packages/gevent/_config.py", line 230, in _import_one_of
    return self._import_one(item)
           ~~~~~~~~~~~~~~~~^^^^^^
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-7c12bab99a20-compat-cb6a104a6688/lib/python3.14/site-packages/gevent/_config.py", line 248, in _import_one
    module = importlib.import_module(module)
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/cpython/Lib/importlib/__init__.py", line 88, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "src/gevent/libev/corecext.pyx", line 819, in init gevent.libev.corecext
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-7c12bab99a20-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/__init__.py", line 58, in <module>
    _wire()
    ~~~~~^^
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-7c12bab99a20-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 1154, in _wire
    from zope.interface.interfaces import IElement
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-7c12bab99a20-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interfaces.py", line 56, in <module>
    class IElement(Interface):
    ...<93 lines>...
            """
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-7c12bab99a20-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 794, in __init__
    self.__attrs = self.__compute_attrs(attrs)
                   ~~~~~~~~~~~~~~~~~~~~^^^^^^^
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-7c12bab99a20-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 813, in __compute_attrs
    aname: update_value(aname, aval)
           ~~~~~~~~~~~~^^^^^^^^^^^^^
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-7c12bab99a20-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 809, in update_value
    raise InvalidInterface("Concrete attribute, " + aname)
zope.interface.exceptions.InvalidInterface: Concrete attribute, __classdictcell__
Traceback (most recent call last):
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/run.py", line 170, in run_benchmarks
    result = bench.run(
             ^^^^^^^^^^
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/_benchmark.py", line 189, in run
    bench = _run_perf_script(
            ^^^^^^^^^^^^^^^^^
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/_benchmark.py", line 240, in _run_perf_script
    raise RuntimeError("Benchmark died")
RuntimeError: Benchmark died
Command failed with exit code 1

ERROR: No benchmark was run
Python benchmark suite 1.11.0


==================================================
```

</details>

## gevent_hub on linux-x86_64 default

<details>
<summary>Log for gevent_hub on linux-x86_64 default</summary>

```
# /home/ddfun/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0e992284450f-compat-cb6a104a6688/bin/python -u /home/ddfun/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_gevent_hub/run_benchmark.py --inherit-environ PYTHON_JIT,PYPERFORMANCE_RUNID --output /tmp/tmp2mqyyte2
Traceback (most recent call last):
  File "/home/ddfun/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_gevent_hub/run_benchmark.py", line 11, in <module>
    import gevent
  File "/home/ddfun/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0e992284450f-compat-cb6a104a6688/lib/python3.14/site-packages/gevent/__init__.py", line 71, in <module>
    from gevent._config import config
Command failed with exit code 1
  File "/home/ddfun/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0e992284450f-compat-cb6a104a6688/lib/python3.14/site-packages/gevent/_config.py", line 730, in <module>
    Loop().get()
    ~~~~~~~~~~^^
  File "/home/ddfun/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0e992284450f-compat-cb6a104a6688/lib/python3.14/site-packages/gevent/_config.py", line 151, in get
    self.value = self.validate(self._default())
                 ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/ddfun/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0e992284450f-compat-cb6a104a6688/lib/python3.14/site-packages/gevent/_config.py", line 259, in validate
    return self._import_one_of([self.shortname_map.get(x, x) for x in value])
           ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ddfun/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0e992284450f-compat-cb6a104a6688/lib/python3.14/site-packages/gevent/_config.py", line 230, in _import_one_of
    return self._import_one(item)
           ~~~~~~~~~~~~~~~~^^^^^^
  File "/home/ddfun/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0e992284450f-compat-cb6a104a6688/lib/python3.14/site-packages/gevent/_config.py", line 248, in _import_one
    module = importlib.import_module(module)
  File "/home/ddfun/actions-runner/_work/benchmarking/benchmarking/cpython/Lib/importlib/__init__.py", line 88, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "src/gevent/libev/corecext.pyx", line 819, in init gevent.libev.corecext
  File "/home/ddfun/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0e992284450f-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/__init__.py", line 58, in <module>
    _wire()
    ~~~~~^^
  File "/home/ddfun/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0e992284450f-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 1154, in _wire
    from zope.interface.interfaces import IElement
  File "/home/ddfun/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0e992284450f-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interfaces.py", line 56, in <module>
    class IElement(Interface):
    ...<93 lines>...
            """
  File "/home/ddfun/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0e992284450f-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 794, in __init__
    self.__attrs = self.__compute_attrs(attrs)
                   ~~~~~~~~~~~~~~~~~~~~^^^^^^^
  File "/home/ddfun/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0e992284450f-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 813, in __compute_attrs
    aname: update_value(aname, aval)
           ~~~~~~~~~~~~^^^^^^^^^^^^^
```

</details>

## gevent_hub on windows-x86_64 default

<details>
<summary>Log for gevent_hub on windows-x86_64 default</summary>

```
    copying src\greenlet\platform\switch_m68k_gcc.h -> build\lib.win-amd64-cpython-314\greenlet\platform
    copying src\greenlet\platform\switch_mips_unix.h -> build\lib.win-amd64-cpython-314\greenlet\platform
    copying src\greenlet\platform\switch_ppc64_aix.h -> build\lib.win-amd64-cpython-314\greenlet\platform
    copying src\greenlet\platform\switch_ppc64_linux.h -> build\lib.win-amd64-cpython-314\greenlet\platform
    copying src\greenlet\platform\switch_ppc_aix.h -> build\lib.win-amd64-cpython-314\greenlet\platform
    copying src\greenlet\platform\switch_ppc_linux.h -> build\lib.win-amd64-cpython-314\greenlet\platform
    copying src\greenlet\platform\switch_ppc_macosx.h -> build\lib.win-amd64-cpython-314\greenlet\platform
    copying src\greenlet\platform\switch_ppc_unix.h -> build\lib.win-amd64-cpython-314\greenlet\platform
    copying src\greenlet\platform\switch_riscv_unix.h -> build\lib.win-amd64-cpython-314\greenlet\platform
    copying src\greenlet\platform\switch_s390_unix.h -> build\lib.win-amd64-cpython-314\greenlet\platform
    copying src\greenlet\platform\switch_sh_gcc.h -> build\lib.win-amd64-cpython-314\greenlet\platform
    copying src\greenlet\platform\switch_sparc_sun_gcc.h -> build\lib.win-amd64-cpython-314\greenlet\platform
    copying src\greenlet\platform\switch_x32_unix.h -> build\lib.win-amd64-cpython-314\greenlet\platform
    copying src\greenlet\platform\switch_x64_masm.asm -> build\lib.win-amd64-cpython-314\greenlet\platform
    copying src\greenlet\platform\switch_x64_masm.obj -> build\lib.win-amd64-cpython-314\greenlet\platform
    copying src\greenlet\platform\switch_x64_msvc.h -> build\lib.win-amd64-cpython-314\greenlet\platform
    copying src\greenlet\platform\switch_x86_msvc.h -> build\lib.win-amd64-cpython-314\greenlet\platform
    copying src\greenlet\platform\switch_x86_unix.h -> build\lib.win-amd64-cpython-314\greenlet\platform
    copying src\greenlet\tests\_test_extension.c -> build\lib.win-amd64-cpython-314\greenlet\tests
    copying src\greenlet\tests\_test_extension_cpp.cpp -> build\lib.win-amd64-cpython-314\greenlet\tests
    running build_ext
    building 'greenlet._greenlet' extension
    creating build\temp.win-amd64-cpython-314\Release\src\greenlet
    "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.41.34120\bin\HostX86\x64\cl.exe" /c /nologo /O2 /W3 /GL /DNDEBUG /MD -DWIN32=1 -IC:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-0db56efbb5b3-compat-cb6a104a6688-bm-gevent_hub\include -IC:\actions-runner\_work\benchmarking\benchmarking\cpython\include -IC:\actions-runner\_work\benchmarking\benchmarking\cpython\PCBuild\amd64 -IC:\actions-runner\_work\benchmarking\benchmarking\cpython\PCBuild\amd64 "-IC:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.41.34120\include" "-IC:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\VS\include" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.22621.0\ucrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\um" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\shared" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\winrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\cppwinrt" /EHsc /Tpsrc/greenlet/greenlet.cpp /Fobuild\temp.win-amd64-cpython-314\Release\src/greenlet/greenlet.obj /EHsr /GT /std:c++20
    greenlet.cpp
    C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(196): error C4576: a parenthesized type followed by an initializer list is a non-standard explicit type conversion syntax
    C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(378): error C4576: a parenthesized type followed by an initializer list is a non-standard explicit type conversion syntax
    C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(379): error C4576: a parenthesized type followed by an initializer list is a non-standard explicit type conversion syntax
    error: command 'C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\VC\\Tools\\MSVC\\14.41.34120\\bin\\HostX86\\x64\\cl.exe' failed with exit code 2
    [end of output]
  
    note: This error originates from a subprocess, and is likely not a problem with pip.
    ERROR: Failed building wheel for greenlet
  Failed to build greenlet
  ERROR: ERROR: Failed to build installable wheels for some pyproject.toml based projects (greenlet)
  [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
error: subprocess-exited-with-error

pip subprocess to install build dependencies did not run successfully.
exit code: 1

See above for output.

note: This error originates from a subprocess, and is likely not a problem with pip.
Command failed with exit code 1


==================================================
```

</details>

## gevent_hub on windows-x86 default

<details>
<summary>Log for gevent_hub on windows-x86 default</summary>

```
    copying src\greenlet\platform\switch_m68k_gcc.h -> build\lib.win32-cpython-314\greenlet\platform
    copying src\greenlet\platform\switch_mips_unix.h -> build\lib.win32-cpython-314\greenlet\platform
    copying src\greenlet\platform\switch_ppc64_aix.h -> build\lib.win32-cpython-314\greenlet\platform
    copying src\greenlet\platform\switch_ppc64_linux.h -> build\lib.win32-cpython-314\greenlet\platform
    copying src\greenlet\platform\switch_ppc_aix.h -> build\lib.win32-cpython-314\greenlet\platform
    copying src\greenlet\platform\switch_ppc_linux.h -> build\lib.win32-cpython-314\greenlet\platform
    copying src\greenlet\platform\switch_ppc_macosx.h -> build\lib.win32-cpython-314\greenlet\platform
    copying src\greenlet\platform\switch_ppc_unix.h -> build\lib.win32-cpython-314\greenlet\platform
    copying src\greenlet\platform\switch_riscv_unix.h -> build\lib.win32-cpython-314\greenlet\platform
    copying src\greenlet\platform\switch_s390_unix.h -> build\lib.win32-cpython-314\greenlet\platform
    copying src\greenlet\platform\switch_sh_gcc.h -> build\lib.win32-cpython-314\greenlet\platform
    copying src\greenlet\platform\switch_sparc_sun_gcc.h -> build\lib.win32-cpython-314\greenlet\platform
    copying src\greenlet\platform\switch_x32_unix.h -> build\lib.win32-cpython-314\greenlet\platform
    copying src\greenlet\platform\switch_x64_masm.asm -> build\lib.win32-cpython-314\greenlet\platform
    copying src\greenlet\platform\switch_x64_masm.obj -> build\lib.win32-cpython-314\greenlet\platform
    copying src\greenlet\platform\switch_x64_msvc.h -> build\lib.win32-cpython-314\greenlet\platform
    copying src\greenlet\platform\switch_x86_msvc.h -> build\lib.win32-cpython-314\greenlet\platform
    copying src\greenlet\platform\switch_x86_unix.h -> build\lib.win32-cpython-314\greenlet\platform
    copying src\greenlet\tests\_test_extension.c -> build\lib.win32-cpython-314\greenlet\tests
    copying src\greenlet\tests\_test_extension_cpp.cpp -> build\lib.win32-cpython-314\greenlet\tests
    running build_ext
    building 'greenlet._greenlet' extension
    creating build\temp.win32-cpython-314\Release\src\greenlet
    "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.41.34120\bin\HostX86\x86\cl.exe" /c /nologo /O2 /W3 /GL /DNDEBUG /MD -DWIN32=1 -IC:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-1d2c37c6a427-compat-cb6a104a6688-bm-gevent_hub\include -IC:\actions-runner\_work\benchmarking\benchmarking\cpython\include -IC:\actions-runner\_work\benchmarking\benchmarking\cpython\PCBuild\win32 -IC:\actions-runner\_work\benchmarking\benchmarking\cpython\PCBuild\win32 "-IC:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.41.34120\include" "-IC:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\VS\include" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.22621.0\ucrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\um" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\shared" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\winrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\cppwinrt" /EHsc /Tpsrc/greenlet/greenlet.cpp /Fobuild\temp.win32-cpython-314\Release\src/greenlet/greenlet.obj /EHsr /GT /std:c++20
    greenlet.cpp
    C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(196): error C4576: a parenthesized type followed by an initializer list is a non-standard explicit type conversion syntax
    C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(378): error C4576: a parenthesized type followed by an initializer list is a non-standard explicit type conversion syntax
    C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(379): error C4576: a parenthesized type followed by an initializer list is a non-standard explicit type conversion syntax
    error: command 'C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\VC\\Tools\\MSVC\\14.41.34120\\bin\\HostX86\\x86\\cl.exe' failed with exit code 2
    [end of output]
  
    note: This error originates from a subprocess, and is likely not a problem with pip.
    ERROR: Failed building wheel for greenlet
  Failed to build greenlet
  ERROR: ERROR: Failed to build installable wheels for some pyproject.toml based projects (greenlet)
  [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
error: subprocess-exited-with-error

pip subprocess to install build dependencies did not run successfully.
exit code: 1

See above for output.

note: This error originates from a subprocess, and is likely not a problem with pip.
Command failed with exit code 1


==================================================
```

</details>

## gunicorn on darwin-arm64 default

<details>
<summary>Log for gunicorn on darwin-arm64 default</summary>

```
# /Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688/bin/python -u /Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_gunicorn/run_benchmark.py --inherit-environ PYPERFORMANCE_RUNID,PYTHON_JIT --output /tmp/tmpetjbih9x
Traceback (most recent call last):
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_gunicorn/run_benchmark.py", line 84, in <module>
    with context:
         ^^^^^^^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/cpython/Lib/contextlib.py", line 141, in __enter__
    return next(self.gen)
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_gunicorn/netutils.py", line 36, in serving
    waitUntilUp(addr)
    ~~~~~~~~~~~^^^^^^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_gunicorn/netutils.py", line 66, in waitUntilUp
    raise Exception('Timeout reached when trying to connect')
Exception: Timeout reached when trying to connect
Traceback (most recent call last):
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.12/site-packages/pyperformance/run.py", line 170, in run_benchmarks
    result = bench.run(
             ^^^^^^^^^^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.12/site-packages/pyperformance/_benchmark.py", line 189, in run
    bench = _run_perf_script(
            ^^^^^^^^^^^^^^^^^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.12/site-packages/pyperformance/_benchmark.py", line 240, in _run_perf_script
    raise RuntimeError("Benchmark died")
RuntimeError: Benchmark died
Command failed with exit code 1
```

</details>

## gunicorn on linux-aarch64 default

<details>
<summary>Log for gunicorn on linux-aarch64 default</summary>

```
# /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-6e18c82301b6-compat-cb6a104a6688/bin/python -u /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_gunicorn/run_benchmark.py --inherit-environ PYPERFORMANCE_RUNID,PYTHON_JIT --output /tmp/tmpa6a7ke3f
Traceback (most recent call last):
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_gunicorn/run_benchmark.py", line 84, in <module>
    with context:
         ^^^^^^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/cpython/Lib/contextlib.py", line 141, in __enter__
    return next(self.gen)
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_gunicorn/netutils.py", line 36, in serving
    waitUntilUp(addr)
    ~~~~~~~~~~~^^^^^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_gunicorn/netutils.py", line 66, in waitUntilUp
    raise Exception('Timeout reached when trying to connect')
Exception: Timeout reached when trying to connect
Traceback (most recent call last):
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/run.py", line 170, in run_benchmarks
    result = bench.run(
             ^^^^^^^^^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/_benchmark.py", line 189, in run
    bench = _run_perf_script(
            ^^^^^^^^^^^^^^^^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/_benchmark.py", line 240, in _run_perf_script
    raise RuntimeError("Benchmark died")
RuntimeError: Benchmark died
Command failed with exit code 1
```

</details>

## gunicorn on collect-stats pystats

<details>
<summary>Log for gunicorn on collect-stats pystats</summary>

```
# /home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-7c12bab99a20-compat-cb6a104a6688/bin/python -u /home/mdboom/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_gunicorn/run_benchmark.py --inherit-environ PYTHON_JIT,PYPERFORMANCE_RUNID --hook=pystats --loops=128 --output /tmp/tmp580mzhmw
Traceback (most recent call last):
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_gunicorn/run_benchmark.py", line 84, in <module>
    with context:
         ^^^^^^^
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/cpython/Lib/contextlib.py", line 141, in __enter__
    return next(self.gen)
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_gunicorn/netutils.py", line 36, in serving
    waitUntilUp(addr)
Command failed with exit code 1
    ~~~~~~~~~~~^^^^^^
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_gunicorn/netutils.py", line 66, in waitUntilUp

##[error]    raise Exception('Timeout reached when trying to connect')
ERROR: No benchmark was run
Exception: Timeout reached when trying to connect
Traceback (most recent call last):
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/run.py", line 170, in run_benchmarks
    result = bench.run(
             ^^^^^^^^^^
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/_benchmark.py", line 189, in run
    bench = _run_perf_script(
            ^^^^^^^^^^^^^^^^^
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/_benchmark.py", line 240, in _run_perf_script
    raise RuntimeError("Benchmark died")
RuntimeError: Benchmark died
Python benchmark suite 1.11.0


==================================================
```

</details>

## gunicorn on linux-x86_64 default

<details>
<summary>Log for gunicorn on linux-x86_64 default</summary>

```
# /home/ddfun/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0e992284450f-compat-cb6a104a6688/bin/python -u /home/ddfun/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_gunicorn/run_benchmark.py --inherit-environ PYTHON_JIT,PYPERFORMANCE_RUNID --output /tmp/tmpybiyz_ak
Traceback (most recent call last):
  File "/home/ddfun/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_gunicorn/run_benchmark.py", line 84, in <module>
    with context:
         ^^^^^^^
  File "/home/ddfun/actions-runner/_work/benchmarking/benchmarking/cpython/Lib/contextlib.py", line 141, in __enter__
    return next(self.gen)
  File "/home/ddfun/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_gunicorn/netutils.py", line 36, in serving
    waitUntilUp(addr)
    ~~~~~~~~~~~^^^^^^
  File "/home/ddfun/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_gunicorn/netutils.py", line 66, in waitUntilUp
##[error]    raise Exception('Timeout reached when trying to connect')
Exception: Timeout reached when trying to connect
Traceback (most recent call last):
  File "/home/ddfun/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/run.py", line 170, in run_benchmarks
    result = bench.run(
             ^^^^^^^^^^
  File "/home/ddfun/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/_benchmark.py", line 189, in run
    bench = _run_perf_script(
            ^^^^^^^^^^^^^^^^^
  File "/home/ddfun/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/_benchmark.py", line 240, in _run_perf_script
    raise RuntimeError("Benchmark died")
RuntimeError: Benchmark died
Command failed with exit code 1
```

</details>

## gunicorn on windows-x86_64 default

<details>
<summary>Log for gunicorn on windows-x86_64 default</summary>

```
# 'C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-0db56efbb5b3-compat-cb6a104a6688\Scripts\python.exe' -u 'C:\actions-runner\_work\benchmarking\benchmarking\pyston-benchmarks\benchmarks\bm_gunicorn\run_benchmark.py' --inherit-environ PYPERFORMANCE_RUNID,PYTHON_JIT --output 'C:\WINDOWS\SERVIC~1\NETWOR~1\AppData\Local\Temp\tmpmuhu_70n'
Traceback (most recent call last):
  File "C:\actions-runner\_work\benchmarking\benchmarking\pyston-benchmarks\benchmarks\bm_gunicorn\run_benchmark.py", line 84, in <module>
    with context:
Command failed with exit code 1
         ^^^^^^^
  File "C:\actions-runner\_work\benchmarking\benchmarking\cpython\Lib\contextlib.py", line 141, in __enter__
    return next(self.gen)
  File "C:\actions-runner\_work\benchmarking\benchmarking\pyston-benchmarks\benchmarks\bm_gunicorn\netutils.py", line 36, in serving
    waitUntilUp(addr)
    ~~~~~~~~~~~^^^^^^
  File "C:\actions-runner\_work\benchmarking\benchmarking\pyston-benchmarks\benchmarks\bm_gunicorn\netutils.py", line 66, in waitUntilUp
    raise Exception('Timeout reached when trying to connect')
Exception: Timeout reached when trying to connect
Traceback (most recent call last):
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\Lib\site-packages\pyperformance\run.py", line 170, in run_benchmarks
    result = bench.run(
             ^^^^^^^^^^
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\Lib\site-packages\pyperformance\_benchmark.py", line 189, in run
    bench = _run_perf_script(
            ^^^^^^^^^^^^^^^^^
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\Lib\site-packages\pyperformance\_benchmark.py", line 240, in _run_perf_script
    raise RuntimeError("Benchmark died")
RuntimeError: Benchmark died
```

</details>

## gunicorn on windows-x86 default

<details>
<summary>Log for gunicorn on windows-x86 default</summary>

```
# 'C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-1d2c37c6a427-compat-cb6a104a6688\Scripts\python.exe' -u 'C:\actions-runner\_work\benchmarking\benchmarking\pyston-benchmarks\benchmarks\bm_gunicorn\run_benchmark.py' --inherit-environ PYTHON_JIT,PYPERFORMANCE_RUNID --output 'C:\WINDOWS\SERVIC~1\NETWOR~1\AppData\Local\Temp\tmpbplgfd0y'
Traceback (most recent call last):
  File "C:\actions-runner\_work\benchmarking\benchmarking\pyston-benchmarks\benchmarks\bm_gunicorn\run_benchmark.py", line 84, in <module>
    with context:
         ^^^^^^^
  File "C:\actions-runner\_work\benchmarking\benchmarking\cpython\Lib\contextlib.py", line 141, in __enter__
    return next(self.gen)
  File "C:\actions-runner\_work\benchmarking\benchmarking\pyston-benchmarks\benchmarks\bm_gunicorn\netutils.py", line 36, in serving
    waitUntilUp(addr)
    ~~~~~~~~~~~^^^^^^
  File "C:\actions-runner\_work\benchmarking\benchmarking\pyston-benchmarks\benchmarks\bm_gunicorn\netutils.py", line 66, in waitUntilUp
    raise Exception('Timeout reached when trying to connect')
Exception: Timeout reached when trying to connect
Traceback (most recent call last):
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\Lib\site-packages\pyperformance\run.py", line 170, in run_benchmarks
    result = bench.run(
             ^^^^^^^^^^
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\Lib\site-packages\pyperformance\_benchmark.py", line 189, in run
    bench = _run_perf_script(
            ^^^^^^^^^^^^^^^^^
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\Lib\site-packages\pyperformance\_benchmark.py", line 240, in _run_perf_script
    raise RuntimeError("Benchmark died")
RuntimeError: Benchmark died
Command failed with exit code 1
```

</details>

## kinto on darwin-arm64 default

<details>
<summary>Log for kinto on darwin-arm64 default</summary>

```
      [thread 5][clang] plugins/http/https.o
      [thread 2][clang] plugins/http/spdy3.o
      [thread 5][clang] plugins/signal/signal_plugin.o
      [thread 3][clang] plugins/syslog/syslog_plugin.o
      [thread 1][clang] plugins/rsyslog/rsyslog_plugin.o
      [thread 7][clang] plugins/logsocket/logsocket_plugin.o
      [thread 2][clang] plugins/router_uwsgi/router_uwsgi.o
      [thread 0][clang] plugins/router_redirect/router_redirect.o
      [thread 4][clang] plugins/router_basicauth/router_basicauth.o
      [thread 6][clang] plugins/zergpool/zergpool.o
      [thread 5][clang] plugins/redislog/redislog_plugin.o
      [thread 2][clang] plugins/mongodblog/mongodblog_plugin.o
      [thread 3][clang] plugins/router_rewrite/router_rewrite.o
      [thread 7][clang] plugins/router_http/router_http.o
      [thread 1][clang] plugins/logfile/logfile.o
      [thread 0][clang] plugins/router_cache/router_cache.o
      [thread 4][clang] plugins/rawrouter/rawrouter.o
      [thread 6][clang] plugins/router_static/router_static.o
      [thread 2][clang] plugins/sslrouter/sslrouter.o
      [thread 3][clang] plugins/spooler/spooler_plugin.o
      [thread 5][clang] plugins/cheaper_busyness/cheaper_busyness.o
      [thread 7][clang] plugins/symcall/symcall_plugin.o
      [thread 1][clang] plugins/transformation_tofile/tofile.o
      [thread 0][clang] plugins/transformation_gzip/gzip.o
      [thread 4][clang] plugins/transformation_chunked/chunked.o
      [thread 6][clang] plugins/transformation_offload/offload.o
      [thread 2][clang] plugins/router_memcached/router_memcached.o
      [thread 3][clang] plugins/router_redis/router_redis.o
      [thread 5][clang] plugins/router_hash/router_hash.o
      [thread 0][clang] plugins/router_expires/expires.o
      [thread 1][clang] plugins/router_metrics/plugin.o
      [thread 7][clang] plugins/transformation_template/tt.o
      [thread 4][clang] plugins/stats_pusher_socket/plugin.o
      *** uWSGI linking ***
      clang -o build/bdist.macosx-15.1-arm64/wheel/uWSGI-2.0.28.data/scripts/uwsgi -L/usr/local/lib -Wl,-rpath,/usr/local/lib core/utils.o core/protocol.o core/socket.o core/logging.o core/master.o core/master_utils.o core/emperor.o core/notify.o core/mule.o core/subscription.o core/stats.o core/sendfile.o core/async.o core/master_checks.o core/fifo.o core/offload.o core/io.o core/static.o core/websockets.o core/spooler.o core/snmp.o core/exceptions.o core/config.o core/setup_utils.o core/clock.o core/init.o core/buffer.o core/reader.o core/writer.o core/alarm.o core/cron.o core/hooks.o core/plugins.o core/lock.o core/cache.o core/daemons.o core/errors.o core/hash.o core/master_events.o core/chunked.o core/queue.o core/event.o core/signal.o core/strings.o core/progress.o core/timebomb.o core/ini.o core/fsmon.o core/mount.o core/metrics.o core/plugins_builder.o core/sharedarea.o core/rpc.o core/gateway.o core/loop.o core/cookie.o core/querystring.o core/rb_timers.o core/transformations.o core/uwsgi.o proto/base.o proto/uwsgi.o proto/http.o proto/fastcgi.o proto/scgi.o proto/puwsgi.o core/zlib.o core/yaml.o core/xmlconf.o core/dot_h.o core/config_py.o plugins/python/python_plugin.o plugins/python/pyutils.o plugins/python/pyloader.o plugins/python/wsgi_handlers.o plugins/python/wsgi_headers.o plugins/python/wsgi_subhandler.o plugins/python/web3_subhandler.o plugins/python/pump_subhandler.o plugins/python/gil.o plugins/python/uwsgi_pymodule.o plugins/python/profiler.o plugins/python/symimporter.o plugins/python/tracebacker.o plugins/python/raw.o plugins/gevent/gevent.o plugins/gevent/hooks.o plugins/ping/ping_plugin.o plugins/cache/cache.o plugins/nagios/nagios.o plugins/rrdtool/rrdtool.o plugins/carbon/carbon.o plugins/rpc/rpc_plugin.o plugins/corerouter/cr_common.o plugins/corerouter/cr_map.o plugins/corerouter/corerouter.o plugins/fastrouter/fastrouter.o plugins/http/http.o plugins/http/keepalive.o plugins/http/https.o plugins/http/spdy3.o plugins/signal/signal_plugin.o plugins/syslog/syslog_plugin.o plugins/rsyslog/rsyslog_plugin.o plugins/logsocket/logsocket_plugin.o plugins/router_uwsgi/router_uwsgi.o plugins/router_redirect/router_redirect.o plugins/router_basicauth/router_basicauth.o plugins/zergpool/zergpool.o plugins/redislog/redislog_plugin.o plugins/mongodblog/mongodblog_plugin.o plugins/router_rewrite/router_rewrite.o plugins/router_http/router_http.o plugins/logfile/logfile.o plugins/router_cache/router_cache.o plugins/rawrouter/rawrouter.o plugins/router_static/router_static.o plugins/sslrouter/sslrouter.o plugins/spooler/spooler_plugin.o plugins/cheaper_busyness/cheaper_busyness.o plugins/symcall/symcall_plugin.o plugins/transformation_tofile/tofile.o plugins/transformation_gzip/gzip.o plugins/transformation_chunked/chunked.o plugins/transformation_offload/offload.o plugins/router_memcached/router_memcached.o plugins/router_redis/router_redis.o plugins/router_hash/router_hash.o plugins/router_expires/expires.o plugins/router_metrics/plugin.o plugins/transformation_template/tt.o plugins/stats_pusher_socket/plugin.o -lpthread -lm -lz -lexpat -ldl -framework CoreFoundation -lpython3.14
      ld: library 'python3.14' not found
      clang: error: linker command failed with exit code 1 (use -v to see invocation)
      *** error linking uWSGI ***
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for uWSGI
  Running setup.py clean for uWSGI
Successfully built kinto
Failed to build uWSGI
ERROR: ERROR: Failed to build installable wheels for some pyproject.toml based projects (uWSGI)
Command failed with exit code 1


==================================================
```

</details>

## kinto on linux-aarch64 default

<details>
<summary>Log for kinto on linux-aarch64 default</summary>

```
                       from plugins/python/uwsgi_python.h:4,
                       from plugins/python/python_plugin.c:1:
      /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/cpython/Include/pylifecycle.h:40:38: note: declared here
         40 | Py_DEPRECATED(3.11) PyAPI_FUNC(void) Py_SetPythonHome(const wchar_t *);
            |                                      ^~~~~~~~~~~~~~~~
      [thread 62][gcc] plugins/transformation_tofile/tofile.o
      plugins/python/python_plugin.c:278:9: warning: ‘Py_SetProgramName’ is deprecated [-Wdeprecated-declarations]
        278 |         Py_SetProgramName(pname);
            |         ^~~~~~~~~~~~~~~~~
      In file included from /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/cpython/Include/Python.h:125,
                       from plugins/python/uwsgi_python.h:4,
                       from plugins/python/python_plugin.c:1:
      /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/cpython/Include/pylifecycle.h:37:38: note: declared here
         37 | Py_DEPRECATED(3.11) PyAPI_FUNC(void) Py_SetProgramName(const wchar_t *);
            |                                      ^~~~~~~~~~~~~~~~~
      plugins/python/python_plugin.c:287:9: warning: ‘Py_OptimizeFlag’ is deprecated [-Wdeprecated-declarations]
        287 |         Py_OptimizeFlag = up.optimize;
            |         ^~~~~~~~~~~~~~~
      In file included from /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/cpython/Include/Python.h:78,
                       from plugins/python/uwsgi_python.h:4,
                       from plugins/python/python_plugin.c:1:
      /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/cpython/Include/cpython/pydebug.h:13:37: note: declared here
         13 | Py_DEPRECATED(3.12) PyAPI_DATA(int) Py_OptimizeFlag;
            |                                     ^~~~~~~~~~~~~~~
      [thread 44][gcc] plugins/transformation_gzip/gzip.o
      [thread 12][gcc] plugins/transformation_chunked/chunked.o
      [thread 43][gcc] plugins/transformation_offload/offload.o
      [thread 14][gcc] plugins/router_memcached/router_memcached.o
      [thread 15][gcc] plugins/router_redis/router_redis.o
      [thread 23][gcc] plugins/router_hash/router_hash.o
      [thread 37][gcc] plugins/router_expires/expires.o
      [thread 74][gcc] plugins/router_metrics/plugin.o
      [thread 69][gcc] plugins/transformation_template/tt.o
      [thread 76][gcc] plugins/stats_pusher_socket/plugin.o
      *** uWSGI linking ***
      gcc -o build/bdist.linux-aarch64/wheel/uWSGI-2.0.28.data/scripts/uwsgi -L/usr/local/lib -Wl,-rpath,/usr/local/lib core/utils.o core/protocol.o core/socket.o core/logging.o core/master.o core/master_utils.o core/emperor.o core/notify.o core/mule.o core/subscription.o core/stats.o core/sendfile.o core/async.o core/master_checks.o core/fifo.o core/offload.o core/io.o core/static.o core/websockets.o core/spooler.o core/snmp.o core/exceptions.o core/config.o core/setup_utils.o core/clock.o core/init.o core/buffer.o core/reader.o core/writer.o core/alarm.o core/cron.o core/hooks.o core/plugins.o core/lock.o core/cache.o core/daemons.o core/errors.o core/hash.o core/master_events.o core/chunked.o core/queue.o core/event.o core/signal.o core/strings.o core/progress.o core/timebomb.o core/ini.o core/fsmon.o core/mount.o core/metrics.o core/plugins_builder.o core/sharedarea.o core/rpc.o core/gateway.o core/loop.o core/cookie.o core/querystring.o core/rb_timers.o core/transformations.o core/uwsgi.o proto/base.o proto/uwsgi.o proto/http.o proto/fastcgi.o proto/scgi.o proto/puwsgi.o lib/linux_ns.o core/zlib.o core/yaml.o core/ssl.o core/legion.o core/xmlconf.o core/dot_h.o core/config_py.o plugins/python/python_plugin.o plugins/python/pyutils.o plugins/python/pyloader.o plugins/python/wsgi_handlers.o plugins/python/wsgi_headers.o plugins/python/wsgi_subhandler.o plugins/python/web3_subhandler.o plugins/python/pump_subhandler.o plugins/python/gil.o plugins/python/uwsgi_pymodule.o plugins/python/profiler.o plugins/python/symimporter.o plugins/python/tracebacker.o plugins/python/raw.o plugins/gevent/gevent.o plugins/gevent/hooks.o plugins/ping/ping_plugin.o plugins/cache/cache.o plugins/nagios/nagios.o plugins/rrdtool/rrdtool.o plugins/carbon/carbon.o plugins/rpc/rpc_plugin.o plugins/corerouter/cr_common.o plugins/corerouter/cr_map.o plugins/corerouter/corerouter.o plugins/fastrouter/fastrouter.o plugins/http/http.o plugins/http/keepalive.o plugins/http/https.o plugins/http/spdy3.o plugins/ugreen/ugreen.o plugins/signal/signal_plugin.o plugins/syslog/syslog_plugin.o plugins/rsyslog/rsyslog_plugin.o plugins/logsocket/logsocket_plugin.o plugins/router_uwsgi/router_uwsgi.o plugins/router_redirect/router_redirect.o plugins/router_basicauth/router_basicauth.o plugins/zergpool/zergpool.o plugins/redislog/redislog_plugin.o plugins/mongodblog/mongodblog_plugin.o plugins/router_rewrite/router_rewrite.o plugins/router_http/router_http.o plugins/logfile/logfile.o plugins/router_cache/router_cache.o plugins/rawrouter/rawrouter.o plugins/router_static/router_static.o plugins/sslrouter/sslrouter.o plugins/spooler/spooler_plugin.o plugins/cheaper_busyness/cheaper_busyness.o plugins/symcall/symcall_plugin.o plugins/transformation_tofile/tofile.o plugins/transformation_gzip/gzip.o plugins/transformation_chunked/chunked.o plugins/transformation_offload/offload.o plugins/router_memcached/router_memcached.o plugins/router_redis/router_redis.o plugins/router_hash/router_hash.o plugins/router_expires/expires.o plugins/router_metrics/plugin.o plugins/transformation_template/tt.o plugins/stats_pusher_socket/plugin.o -lpthread -lm -rdynamic -ldl -lz -luuid -lssl -lcrypto -lxml2 -ldl -lm -lpython3.14 -lcrypt
      /usr/bin/ld: cannot find -lpython3.14: No such file or directory
      collect2: error: ld returned 1 exit status
      *** error linking uWSGI ***
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for uWSGI
Successfully built kinto
Failed to build uWSGI
ERROR: ERROR: Failed to build installable wheels for some pyproject.toml based projects (uWSGI)
Command failed with exit code 1


==================================================
```

</details>

## kinto on collect-stats pystats

<details>
<summary>Log for kinto on collect-stats pystats</summary>

```
# /home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-7c12bab99a20-compat-cb6a104a6688/bin/python -u /home/mdboom/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_kinto/run_benchmark.py --inherit-environ PYTHON_JIT,PYPERFORMANCE_RUNID --hook=pystats --output /tmp/tmpc6u4j489
Traceback (most recent call last):
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_kinto/run_benchmark.py", line 73, in <module>
    raise Exception("nginx is not installed")
Exception: nginx is not installed
Traceback (most recent call last):
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/run.py", line 170, in run_benchmarks
    result = bench.run(
             ^^^^^^^^^^
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/_benchmark.py", line 189, in run
    bench = _run_perf_script(
            ^^^^^^^^^^^^^^^^^
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/_benchmark.py", line 240, in _run_perf_script
    raise RuntimeError("Benchmark died")
RuntimeError: Benchmark died
Command failed with exit code 1

ERROR: No benchmark was run
Python benchmark suite 1.11.0


==================================================
```

</details>

## kinto on linux-x86_64 default

<details>
<summary>Log for kinto on linux-x86_64 default</summary>

```
      [thread 11][gcc] plugins/http/spdy3.o
      [thread 17][gcc] plugins/ugreen/ugreen.o
      [thread 20][gcc] plugins/signal/signal_plugin.o
      [thread 4][gcc] plugins/syslog/syslog_plugin.o
      [thread 22][gcc] plugins/rsyslog/rsyslog_plugin.o
      [thread 3][gcc] plugins/logsocket/logsocket_plugin.o
      [thread 5][gcc] plugins/router_uwsgi/router_uwsgi.o
      [thread 10][gcc] plugins/router_redirect/router_redirect.o
      [thread 15][gcc] plugins/router_basicauth/router_basicauth.o
      [thread 23][gcc] plugins/zergpool/zergpool.o
      [thread 9][gcc] plugins/redislog/redislog_plugin.o
      [thread 18][gcc] plugins/mongodblog/mongodblog_plugin.o
      [thread 8][gcc] plugins/router_rewrite/router_rewrite.o
      [thread 13][gcc] plugins/router_http/router_http.o
      [thread 20][gcc] plugins/logfile/logfile.o
      [thread 1][gcc] plugins/router_cache/router_cache.o
      [thread 19][gcc] plugins/rawrouter/rawrouter.o
      [thread 17][gcc] plugins/router_static/router_static.o
      [thread 12][gcc] plugins/sslrouter/sslrouter.o
      [thread 4][gcc] plugins/spooler/spooler_plugin.o
      [thread 5][gcc] plugins/cheaper_busyness/cheaper_busyness.o
      [thread 3][gcc] plugins/symcall/symcall_plugin.o
      [thread 22][gcc] plugins/transformation_tofile/tofile.o
      [thread 15][gcc] plugins/transformation_gzip/gzip.o
      [thread 10][gcc] plugins/transformation_chunked/chunked.o
      [thread 2][gcc] plugins/transformation_offload/offload.o
      [thread 6][gcc] plugins/router_memcached/router_memcached.o
      [thread 14][gcc] plugins/router_redis/router_redis.o
      [thread 9][gcc] plugins/router_hash/router_hash.o
      [thread 18][gcc] plugins/router_expires/expires.o
      [thread 23][gcc] plugins/router_metrics/plugin.o
      [thread 8][gcc] plugins/transformation_template/tt.o
      [thread 13][gcc] plugins/stats_pusher_socket/plugin.o
      *** uWSGI linking ***
      gcc -o build/bdist.linux-x86_64/wheel/uWSGI-2.0.28.data/scripts/uwsgi -L/usr/local/lib -Wl,-rpath,/usr/local/lib core/utils.o core/protocol.o core/socket.o core/logging.o core/master.o core/master_utils.o core/emperor.o core/notify.o core/mule.o core/subscription.o core/stats.o core/sendfile.o core/async.o core/master_checks.o core/fifo.o core/offload.o core/io.o core/static.o core/websockets.o core/spooler.o core/snmp.o core/exceptions.o core/config.o core/setup_utils.o core/clock.o core/init.o core/buffer.o core/reader.o core/writer.o core/alarm.o core/cron.o core/hooks.o core/plugins.o core/lock.o core/cache.o core/daemons.o core/errors.o core/hash.o core/master_events.o core/chunked.o core/queue.o core/event.o core/signal.o core/strings.o core/progress.o core/timebomb.o core/ini.o core/fsmon.o core/mount.o core/metrics.o core/plugins_builder.o core/sharedarea.o core/rpc.o core/gateway.o core/loop.o core/cookie.o core/querystring.o core/rb_timers.o core/transformations.o core/uwsgi.o proto/base.o proto/uwsgi.o proto/http.o proto/fastcgi.o proto/scgi.o proto/puwsgi.o lib/linux_ns.o core/zlib.o core/yaml.o core/ssl.o core/legion.o core/xmlconf.o core/dot_h.o core/config_py.o plugins/python/python_plugin.o plugins/python/pyutils.o plugins/python/pyloader.o plugins/python/wsgi_handlers.o plugins/python/wsgi_headers.o plugins/python/wsgi_subhandler.o plugins/python/web3_subhandler.o plugins/python/pump_subhandler.o plugins/python/gil.o plugins/python/uwsgi_pymodule.o plugins/python/profiler.o plugins/python/symimporter.o plugins/python/tracebacker.o plugins/python/raw.o plugins/gevent/gevent.o plugins/gevent/hooks.o plugins/ping/ping_plugin.o plugins/cache/cache.o plugins/nagios/nagios.o plugins/rrdtool/rrdtool.o plugins/carbon/carbon.o plugins/rpc/rpc_plugin.o plugins/corerouter/cr_common.o plugins/corerouter/cr_map.o plugins/corerouter/corerouter.o plugins/fastrouter/fastrouter.o plugins/http/http.o plugins/http/keepalive.o plugins/http/https.o plugins/http/spdy3.o plugins/ugreen/ugreen.o plugins/signal/signal_plugin.o plugins/syslog/syslog_plugin.o plugins/rsyslog/rsyslog_plugin.o plugins/logsocket/logsocket_plugin.o plugins/router_uwsgi/router_uwsgi.o plugins/router_redirect/router_redirect.o plugins/router_basicauth/router_basicauth.o plugins/zergpool/zergpool.o plugins/redislog/redislog_plugin.o plugins/mongodblog/mongodblog_plugin.o plugins/router_rewrite/router_rewrite.o plugins/router_http/router_http.o plugins/logfile/logfile.o plugins/router_cache/router_cache.o plugins/rawrouter/rawrouter.o plugins/router_static/router_static.o plugins/sslrouter/sslrouter.o plugins/spooler/spooler_plugin.o plugins/cheaper_busyness/cheaper_busyness.o plugins/symcall/symcall_plugin.o plugins/transformation_tofile/tofile.o plugins/transformation_gzip/gzip.o plugins/transformation_chunked/chunked.o plugins/transformation_offload/offload.o plugins/router_memcached/router_memcached.o plugins/router_redis/router_redis.o plugins/router_hash/router_hash.o plugins/router_expires/expires.o plugins/router_metrics/plugin.o plugins/transformation_template/tt.o plugins/stats_pusher_socket/plugin.o -lpthread -lm -rdynamic -ldl -lz -luuid -lssl -lcrypto -lxml2 -ldl -lm -lpython3.14 -lcrypt
      /usr/bin/ld: cannot find -lpython3.14: No such file or directory
      collect2: error: ld returned 1 exit status
      *** error linking uWSGI ***
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for uWSGI
  Running setup.py clean for uWSGI
Successfully built kinto
Failed to build uWSGI
ERROR: ERROR: Failed to build installable wheels for some pyproject.toml based projects (uWSGI)
Command failed with exit code 1


==================================================
```

</details>

## kinto on windows-x86_64 default

<details>
<summary>Log for kinto on windows-x86_64 default</summary>

```
  Installing build dependencies: finished with status 'done'
  Getting requirements to build wheel: started
  Getting requirements to build wheel: finished with status 'done'
  Preparing metadata (pyproject.toml): started
  Preparing metadata (pyproject.toml): finished with status 'done'
Collecting urllib3==2.0.2
  Using cached urllib3-2.0.2-py3-none-any.whl.metadata (6.6 kB)
Collecting uWSGI==2.0.28
  Using cached uwsgi-2.0.28.tar.gz (816 kB)
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'error'
  error: subprocess-exited-with-error
  
  python setup.py egg_info did not run successfully.
  exit code: 1
  
  [18 lines of output]
  Traceback (most recent call last):
    File "<string>", line 2, in <module>
      exec(compile('''
      ~~~~^^^^^^^^^^^^
      # This is <pip-setuptools-caller> -- a caller that pip uses to run setup.py
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      ...<31 lines>...
      exec(compile(setup_py_code, filename, "exec"))
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      ''' % ('C:\\Windows\\ServiceProfiles\\NetworkService\\AppData\\Local\\Temp\\pip-install-lkf2i94y\\uwsgi_bd4180d2692c49479dff3f16a2f6983c\\setup.py',), "<pip-setuptools-caller>", "exec"))
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "<pip-setuptools-caller>", line 34, in <module>
    File "C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\pip-install-lkf2i94y\uwsgi_bd4180d2692c49479dff3f16a2f6983c\setup.py", line 3, in <module>
      import uwsgiconfig as uc
    File "C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\pip-install-lkf2i94y\uwsgi_bd4180d2692c49479dff3f16a2f6983c\uwsgiconfig.py", line 8, in <module>
      uwsgi_os = os.uname()[0]
                 ^^^^^^^^
  AttributeError: module 'os' has no attribute 'uname'. Did you mean: 'name'?
  [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
error: metadata-generation-failed

Encountered error while generating package metadata.

See above for output.

note: This is an issue with the package mentioned above, not pip.
hint: See above for details.
Command failed with exit code 1


==================================================
```

</details>

## kinto on windows-x86 default

<details>
<summary>Log for kinto on windows-x86 default</summary>

```
  Installing build dependencies: finished with status 'done'
  Getting requirements to build wheel: started
  Getting requirements to build wheel: finished with status 'done'
  Preparing metadata (pyproject.toml): started
  Preparing metadata (pyproject.toml): finished with status 'done'
Collecting urllib3==2.0.2
  Using cached urllib3-2.0.2-py3-none-any.whl.metadata (6.6 kB)
Collecting uWSGI==2.0.28
  Using cached uwsgi-2.0.28.tar.gz (816 kB)
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'error'
  error: subprocess-exited-with-error
  
  python setup.py egg_info did not run successfully.
  exit code: 1
  
  [18 lines of output]
  Traceback (most recent call last):
    File "<string>", line 2, in <module>
      exec(compile('''
      ~~~~^^^^^^^^^^^^
      # This is <pip-setuptools-caller> -- a caller that pip uses to run setup.py
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      ...<31 lines>...
      exec(compile(setup_py_code, filename, "exec"))
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      ''' % ('C:\\Windows\\ServiceProfiles\\NetworkService\\AppData\\Local\\Temp\\pip-install-i4czrt8q\\uwsgi_efef84aba0bb4a88b7969851bd9e5751\\setup.py',), "<pip-setuptools-caller>", "exec"))
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "<pip-setuptools-caller>", line 34, in <module>
    File "C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\pip-install-i4czrt8q\uwsgi_efef84aba0bb4a88b7969851bd9e5751\setup.py", line 3, in <module>
      import uwsgiconfig as uc
    File "C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\pip-install-i4czrt8q\uwsgi_efef84aba0bb4a88b7969851bd9e5751\uwsgiconfig.py", line 8, in <module>
      uwsgi_os = os.uname()[0]
                 ^^^^^^^^
  AttributeError: module 'os' has no attribute 'uname'. Did you mean: 'name'?
  [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
error: metadata-generation-failed

Encountered error while generating package metadata.

See above for output.

note: This is an issue with the package mentioned above, not pip.
hint: See above for details.
Command failed with exit code 1


==================================================
```

</details>

## pytorch_alexnet_inference on darwin-arm64 default

<details>
<summary>Log for pytorch_alexnet_inference on darwin-arm64 default</summary>

```
  error: subprocess-exited-with-error
  
  × Preparing metadata (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> [31 lines of output]
      Running from numpy source directory.
      <string>:460: UserWarning: Unrecognized setuptools command, proceeding with generating Cython sources and expanding templates
      Traceback (most recent call last):
        File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688-bm-pytorch_alexnet_inference/lib/python3.14/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 353, in <module>
          main()
          ~~~~^^
        File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688-bm-pytorch_alexnet_inference/lib/python3.14/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 335, in main
          json_out['return_val'] = hook(**hook_input['kwargs'])
                                   ~~~~^^^^^^^^^^^^^^^^^^^^^^^^
        File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688-bm-pytorch_alexnet_inference/lib/python3.14/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 149, in prepare_metadata_for_build_wheel
          return hook(metadata_directory, config_settings)
        File "/private/tmp/pip-build-env-mck14oc1/overlay/lib/python3.14/site-packages/setuptools/build_meta.py", line 377, in prepare_metadata_for_build_wheel
          self.run_setup()
          ~~~~~~~~~~~~~~^^
        File "/private/tmp/pip-build-env-mck14oc1/overlay/lib/python3.14/site-packages/setuptools/build_meta.py", line 522, in run_setup
          super().run_setup(setup_script=setup_script)
          ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "/private/tmp/pip-build-env-mck14oc1/overlay/lib/python3.14/site-packages/setuptools/build_meta.py", line 320, in run_setup
          exec(code, locals())
          ~~~~^^^^^^^^^^^^^^^^
        File "<string>", line 489, in <module>
        File "<string>", line 465, in setup_package
        File "/private/tmp/pip-install-ta5lpyef/numpy_1a31f4a0254c43d99333789ada3133ec/numpy/distutils/core.py", line 24, in <module>
          from numpy.distutils.command import config, config_compiler, \
          ...<2 lines>...
               install_clib
        File "/private/tmp/pip-install-ta5lpyef/numpy_1a31f4a0254c43d99333789ada3133ec/numpy/distutils/command/config.py", line 19, in <module>
          from numpy.distutils.mingw32ccompiler import generate_manifest
        File "/private/tmp/pip-install-ta5lpyef/numpy_1a31f4a0254c43d99333789ada3133ec/numpy/distutils/mingw32ccompiler.py", line 28, in <module>
          from distutils.msvccompiler import get_build_version as get_build_msvc_version
      ModuleNotFoundError: No module named 'distutils.msvccompiler'
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
error: metadata-generation-failed

× Encountered error while generating package metadata.
╰─> See above for output.

note: This is an issue with the package mentioned above, not pip.
hint: See above for details.
Command failed with exit code 1


==================================================
```

</details>

## pytorch_alexnet_inference on linux-aarch64 default

<details>
<summary>Log for pytorch_alexnet_inference on linux-aarch64 default</summary>

```
  error: subprocess-exited-with-error
  
  × Preparing metadata (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> [31 lines of output]
      Running from numpy source directory.
      <string>:460: UserWarning: Unrecognized setuptools command, proceeding with generating Cython sources and expanding templates
      Traceback (most recent call last):
        File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-6e18c82301b6-compat-cb6a104a6688-bm-pytorch_alexnet_inference/lib/python3.14/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 353, in <module>
          main()
          ~~~~^^
        File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-6e18c82301b6-compat-cb6a104a6688-bm-pytorch_alexnet_inference/lib/python3.14/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 335, in main
          json_out['return_val'] = hook(**hook_input['kwargs'])
                                   ~~~~^^^^^^^^^^^^^^^^^^^^^^^^
        File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-6e18c82301b6-compat-cb6a104a6688-bm-pytorch_alexnet_inference/lib/python3.14/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 149, in prepare_metadata_for_build_wheel
          return hook(metadata_directory, config_settings)
        File "/tmp/pip-build-env-9xcy0661/overlay/lib/python3.14/site-packages/setuptools/build_meta.py", line 377, in prepare_metadata_for_build_wheel
          self.run_setup()
          ~~~~~~~~~~~~~~^^
        File "/tmp/pip-build-env-9xcy0661/overlay/lib/python3.14/site-packages/setuptools/build_meta.py", line 522, in run_setup
          super().run_setup(setup_script=setup_script)
          ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "/tmp/pip-build-env-9xcy0661/overlay/lib/python3.14/site-packages/setuptools/build_meta.py", line 320, in run_setup
          exec(code, locals())
          ~~~~^^^^^^^^^^^^^^^^
        File "<string>", line 489, in <module>
        File "<string>", line 465, in setup_package
        File "/tmp/pip-install-8e93n6a0/numpy_eb6072e4b00a40a0874c255d6359f02c/numpy/distutils/core.py", line 24, in <module>
          from numpy.distutils.command import config, config_compiler, \
          ...<2 lines>...
               install_clib
        File "/tmp/pip-install-8e93n6a0/numpy_eb6072e4b00a40a0874c255d6359f02c/numpy/distutils/command/config.py", line 19, in <module>
          from numpy.distutils.mingw32ccompiler import generate_manifest
        File "/tmp/pip-install-8e93n6a0/numpy_eb6072e4b00a40a0874c255d6359f02c/numpy/distutils/mingw32ccompiler.py", line 28, in <module>
          from distutils.msvccompiler import get_build_version as get_build_msvc_version
      ModuleNotFoundError: No module named 'distutils.msvccompiler'
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
error: metadata-generation-failed

× Encountered error while generating package metadata.
╰─> See above for output.

note: This is an issue with the package mentioned above, not pip.
hint: See above for details.
Command failed with exit code 1


==================================================
```

</details>

## pytorch_alexnet_inference on collect-stats pystats

<details>
<summary>Log for pytorch_alexnet_inference on collect-stats pystats</summary>

```
  Preparing metadata (pyproject.toml): finished with status 'error'
  error: subprocess-exited-with-error
  
  × Preparing metadata (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> [31 lines of output]
      Running from numpy source directory.
      <string>:460: UserWarning: Unrecognized setuptools command, proceeding with generating Cython sources and expanding templates
      Traceback (most recent call last):
        File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-7c12bab99a20-compat-cb6a104a6688-bm-pytorch_alexnet_inference/lib/python3.14/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 353, in <module>
          main()
          ~~~~^^
        File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-7c12bab99a20-compat-cb6a104a6688-bm-pytorch_alexnet_inference/lib/python3.14/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 335, in main
          json_out['return_val'] = hook(**hook_input['kwargs'])
                                   ~~~~^^^^^^^^^^^^^^^^^^^^^^^^
        File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-7c12bab99a20-compat-cb6a104a6688-bm-pytorch_alexnet_inference/lib/python3.14/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 149, in prepare_metadata_for_build_wheel
          return hook(metadata_directory, config_settings)
        File "/tmp/pip-build-env-fjl2ohae/overlay/lib/python3.14/site-packages/setuptools/build_meta.py", line 377, in prepare_metadata_for_build_wheel
          self.run_setup()
          ~~~~~~~~~~~~~~^^
        File "/tmp/pip-build-env-fjl2ohae/overlay/lib/python3.14/site-packages/setuptools/build_meta.py", line 522, in run_setup
          super().run_setup(setup_script=setup_script)
          ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "/tmp/pip-build-env-fjl2ohae/overlay/lib/python3.14/site-packages/setuptools/build_meta.py", line 320, in run_setup
          exec(code, locals())
          ~~~~^^^^^^^^^^^^^^^^
        File "<string>", line 489, in <module>
        File "<string>", line 465, in setup_package
        File "/tmp/pip-install-y37jrtrz/numpy_b1b14bd05b1a4347986b1c34c526f694/numpy/distutils/core.py", line 24, in <module>
          from numpy.distutils.command import config, config_compiler, \
          ...<2 lines>...
               install_clib
        File "/tmp/pip-install-y37jrtrz/numpy_b1b14bd05b1a4347986b1c34c526f694/numpy/distutils/command/config.py", line 19, in <module>
          from numpy.distutils.mingw32ccompiler import generate_manifest
        File "/tmp/pip-install-y37jrtrz/numpy_b1b14bd05b1a4347986b1c34c526f694/numpy/distutils/mingw32ccompiler.py", line 28, in <module>
          from distutils.msvccompiler import get_build_version as get_build_msvc_version
      ModuleNotFoundError: No module named 'distutils.msvccompiler'
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
error: metadata-generation-failed

× Encountered error while generating package metadata.
╰─> See above for output.

note: This is an issue with the package mentioned above, not pip.
hint: See above for details.
Command failed with exit code 1


```

</details>

## pytorch_alexnet_inference on linux-x86_64 default

<details>
<summary>Log for pytorch_alexnet_inference on linux-x86_64 default</summary>

```
  error: subprocess-exited-with-error
  
  × Preparing metadata (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> [31 lines of output]
      Running from numpy source directory.
      <string>:460: UserWarning: Unrecognized setuptools command, proceeding with generating Cython sources and expanding templates
      Traceback (most recent call last):
        File "/home/ddfun/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0e992284450f-compat-cb6a104a6688-bm-pytorch_alexnet_inference/lib/python3.14/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 353, in <module>
          main()
          ~~~~^^
        File "/home/ddfun/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0e992284450f-compat-cb6a104a6688-bm-pytorch_alexnet_inference/lib/python3.14/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 335, in main
          json_out['return_val'] = hook(**hook_input['kwargs'])
                                   ~~~~^^^^^^^^^^^^^^^^^^^^^^^^
        File "/home/ddfun/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0e992284450f-compat-cb6a104a6688-bm-pytorch_alexnet_inference/lib/python3.14/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 149, in prepare_metadata_for_build_wheel
          return hook(metadata_directory, config_settings)
        File "/tmp/pip-build-env-m5692y4l/overlay/lib/python3.14/site-packages/setuptools/build_meta.py", line 377, in prepare_metadata_for_build_wheel
          self.run_setup()
          ~~~~~~~~~~~~~~^^
        File "/tmp/pip-build-env-m5692y4l/overlay/lib/python3.14/site-packages/setuptools/build_meta.py", line 522, in run_setup
          super().run_setup(setup_script=setup_script)
          ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "/tmp/pip-build-env-m5692y4l/overlay/lib/python3.14/site-packages/setuptools/build_meta.py", line 320, in run_setup
          exec(code, locals())
          ~~~~^^^^^^^^^^^^^^^^
        File "<string>", line 489, in <module>
        File "<string>", line 465, in setup_package
        File "/tmp/pip-install-_plbf50m/numpy_ae26352a70c74c2ea80199dd615504bd/numpy/distutils/core.py", line 24, in <module>
          from numpy.distutils.command import config, config_compiler, \
          ...<2 lines>...
               install_clib
        File "/tmp/pip-install-_plbf50m/numpy_ae26352a70c74c2ea80199dd615504bd/numpy/distutils/command/config.py", line 19, in <module>
          from numpy.distutils.mingw32ccompiler import generate_manifest
        File "/tmp/pip-install-_plbf50m/numpy_ae26352a70c74c2ea80199dd615504bd/numpy/distutils/mingw32ccompiler.py", line 28, in <module>
          from distutils.msvccompiler import get_build_version as get_build_msvc_version
      ModuleNotFoundError: No module named 'distutils.msvccompiler'
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
error: metadata-generation-failed

× Encountered error while generating package metadata.
╰─> See above for output.

note: This is an issue with the package mentioned above, not pip.
hint: See above for details.
Command failed with exit code 1


==================================================
```

</details>

## pytorch_alexnet_inference on windows-x86_64 default

<details>
<summary>Log for pytorch_alexnet_inference on windows-x86_64 default</summary>

```
      exec(code, locals())
      ~~~~^^^^^^^^^^^^^^^^
    File "<string>", line 489, in <module>
    File "<string>", line 465, in setup_package
    File "C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\pip-install-5qvvxqzi\numpy_3d4d3169d76d473ea83604f7ea60c579\numpy\distutils\core.py", line 24, in <module>
      from numpy.distutils.command import config, config_compiler, \
      ...<2 lines>...
           install_clib
    File "C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\pip-install-5qvvxqzi\numpy_3d4d3169d76d473ea83604f7ea60c579\numpy\distutils\command\config.py", line 19, in <module>
      from numpy.distutils.mingw32ccompiler import generate_manifest
    File "C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\pip-install-5qvvxqzi\numpy_3d4d3169d76d473ea83604f7ea60c579\numpy\distutils\mingw32ccompiler.py", line 28, in <module>
      from distutils.msvccompiler import get_build_version as get_build_msvc_version
  ModuleNotFoundError: No module named 'distutils.msvccompiler'
  [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
  Preparing metadata (pyproject.toml): finished with status 'error'
error: metadata-generation-failed

Encountered error while generating package metadata.

See above for output.

note: This is an issue with the package mentioned above, not pip.
hint: See above for details.
Command failed with exit code 1
(falling back to unique venv)
Creating the virtual environment C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-0db56efbb5b3-compat-cb6a104a6688-bm-pytorch_alexnet_inference
# 'C:\actions-runner\_work\benchmarking\benchmarking\cpython\PCBuild\amd64\python.exe' -m venv --without-pip 'C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-0db56efbb5b3-compat-cb6a104a6688-bm-pytorch_alexnet_inference'
# 'C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-0db56efbb5b3-compat-cb6a104a6688-bm-pytorch_alexnet_inference\Scripts\python.exe' -m ensurepip -v -U
Using pip 24.3.1 from C:\WINDOWS\SERVIC~1\NETWOR~1\AppData\Local\Temp\tmpy98f82fx\pip-24.3.1-py3-none-any.whl\pip (python 3.14)
Looking in links: c:\WINDOWS\SERVIC~1\NETWOR~1\AppData\Local\Temp\tmpy98f82fx
Processing c:\windows\servic~1\networ~1\appdata\local\temp\tmpy98f82fx\pip-24.3.1-py3-none-any.whl
Installing collected packages: pip
Successfully installed pip-24.3.1
# 'C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-0db56efbb5b3-compat-cb6a104a6688-bm-pytorch_alexnet_inference\Scripts\python.exe' -m pip install -U 'setuptools>=18.5' wheel
Collecting setuptools>=18.5
  Using cached setuptools-75.6.0-py3-none-any.whl.metadata (6.7 kB)
Collecting wheel
  Using cached wheel-0.45.1-py3-none-any.whl.metadata (2.3 kB)
Using cached setuptools-75.6.0-py3-none-any.whl (1.2 MB)
Using cached wheel-0.45.1-py3-none-any.whl (72 kB)
Installing collected packages: wheel, setuptools
ERROR: Could not install packages due to an OSError: [Errno 2] No such file or directory: 'C:\\actions-runner\\_work\\benchmarking\\benchmarking\\venv\\cpython3.14-0db56efbb5b3-compat-cb6a104a6688-bm-pytorch_alexnet_inference\\Lib\\site-packages\\pkg_resources\\tests\\data\\my-test-package_unpacked-egg\\my_test_package-1.0-py3.7.egg\\EGG-INFO\\dependency_links.txt'

Command failed with exit code 1
Remove directory C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-0db56efbb5b3-compat-cb6a104a6688-bm-pytorch_alexnet_inference


==================================================
```

</details>

## pytorch_alexnet_inference on windows-x86 default

<details>
<summary>Log for pytorch_alexnet_inference on windows-x86 default</summary>

```
    File "C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\pip-build-env-56r7ptpw\overlay\Lib\site-packages\setuptools\build_meta.py", line 320, in run_setup
      exec(code, locals())
      ~~~~^^^^^^^^^^^^^^^^
    File "<string>", line 489, in <module>
    File "<string>", line 465, in setup_package
    File "C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\pip-install-qlhzvpgl\numpy_45fa0275b0fe4a1f976dd64637068845\numpy\distutils\core.py", line 24, in <module>
      from numpy.distutils.command import config, config_compiler, \
      ...<2 lines>...
           install_clib
    File "C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\pip-install-qlhzvpgl\numpy_45fa0275b0fe4a1f976dd64637068845\numpy\distutils\command\config.py", line 19, in <module>
      from numpy.distutils.mingw32ccompiler import generate_manifest
    File "C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\pip-install-qlhzvpgl\numpy_45fa0275b0fe4a1f976dd64637068845\numpy\distutils\mingw32ccompiler.py", line 28, in <module>
      from distutils.msvccompiler import get_build_version as get_build_msvc_version
  ModuleNotFoundError: No module named 'distutils.msvccompiler'
  [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
error: metadata-generation-failed

Encountered error while generating package metadata.

See above for output.

note: This is an issue with the package mentioned above, not pip.
hint: See above for details.
Command failed with exit code 1
(falling back to unique venv)
Creating the virtual environment C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-1d2c37c6a427-compat-cb6a104a6688-bm-pytorch_alexnet_inference
# 'C:\actions-runner\_work\benchmarking\benchmarking\cpython\PCBuild\win32\python.exe' -m venv --without-pip 'C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-1d2c37c6a427-compat-cb6a104a6688-bm-pytorch_alexnet_inference'
# 'C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-1d2c37c6a427-compat-cb6a104a6688-bm-pytorch_alexnet_inference\Scripts\python.exe' -m ensurepip -v -U
Using pip 24.3.1 from C:\WINDOWS\SERVIC~1\NETWOR~1\AppData\Local\Temp\tmp2qfmubkj\pip-24.3.1-py3-none-any.whl\pip (python 3.14)
Looking in links: c:\WINDOWS\SERVIC~1\NETWOR~1\AppData\Local\Temp\tmp2qfmubkj
Processing c:\windows\servic~1\networ~1\appdata\local\temp\tmp2qfmubkj\pip-24.3.1-py3-none-any.whl
Installing collected packages: pip
Successfully installed pip-24.3.1
# 'C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-1d2c37c6a427-compat-cb6a104a6688-bm-pytorch_alexnet_inference\Scripts\python.exe' -m pip install -U 'setuptools>=18.5' wheel
Collecting setuptools>=18.5
  Using cached setuptools-75.6.0-py3-none-any.whl.metadata (6.7 kB)
Collecting wheel
  Using cached wheel-0.45.1-py3-none-any.whl.metadata (2.3 kB)
Using cached setuptools-75.6.0-py3-none-any.whl (1.2 MB)
Using cached wheel-0.45.1-py3-none-any.whl (72 kB)
Installing collected packages: wheel, setuptools
ERROR: Could not install packages due to an OSError: [Errno 2] No such file or directory: 'C:\\actions-runner\\_work\\benchmarking\\benchmarking\\venv\\cpython3.14-1d2c37c6a427-compat-cb6a104a6688-bm-pytorch_alexnet_inference\\Lib\\site-packages\\pkg_resources\\tests\\data\\my-test-package_unpacked-egg\\my_test_package-1.0-py3.7.egg\\EGG-INFO\\dependency_links.txt'

Command failed with exit code 1
Remove directory C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-1d2c37c6a427-compat-cb6a104a6688-bm-pytorch_alexnet_inference


==================================================
```

</details>

## sqlalchemy_declarative on windows-x86_64 default

<details>
<summary>Log for sqlalchemy_declarative on windows-x86_64 default</summary>

```
  copying src\greenlet\platform\switch_arm32_ios.h -> build\lib.win-amd64-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_arm64_masm.asm -> build\lib.win-amd64-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_arm64_masm.obj -> build\lib.win-amd64-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_arm64_msvc.h -> build\lib.win-amd64-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_csky_gcc.h -> build\lib.win-amd64-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_loongarch64_linux.h -> build\lib.win-amd64-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_m68k_gcc.h -> build\lib.win-amd64-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_mips_unix.h -> build\lib.win-amd64-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_ppc64_aix.h -> build\lib.win-amd64-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_ppc64_linux.h -> build\lib.win-amd64-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_ppc_aix.h -> build\lib.win-amd64-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_ppc_linux.h -> build\lib.win-amd64-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_ppc_macosx.h -> build\lib.win-amd64-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_ppc_unix.h -> build\lib.win-amd64-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_riscv_unix.h -> build\lib.win-amd64-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_s390_unix.h -> build\lib.win-amd64-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_sh_gcc.h -> build\lib.win-amd64-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_sparc_sun_gcc.h -> build\lib.win-amd64-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_x32_unix.h -> build\lib.win-amd64-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_x64_masm.asm -> build\lib.win-amd64-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_x64_masm.obj -> build\lib.win-amd64-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_x64_msvc.h -> build\lib.win-amd64-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_x86_msvc.h -> build\lib.win-amd64-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_x86_unix.h -> build\lib.win-amd64-cpython-314\greenlet\platform
  copying src\greenlet\tests\_test_extension.c -> build\lib.win-amd64-cpython-314\greenlet\tests
  copying src\greenlet\tests\_test_extension_cpp.cpp -> build\lib.win-amd64-cpython-314\greenlet\tests
  running build_ext
  building 'greenlet._greenlet' extension
  creating build\temp.win-amd64-cpython-314\Release\src\greenlet
  "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.41.34120\bin\HostX86\x64\cl.exe" /c /nologo /O2 /W3 /GL /DNDEBUG /MD -DWIN32=1 -IC:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-0db56efbb5b3-compat-cb6a104a6688-bm-sqlalchemy_declarative\include -IC:\actions-runner\_work\benchmarking\benchmarking\cpython\include -IC:\actions-runner\_work\benchmarking\benchmarking\cpython\PCBuild\amd64 -IC:\actions-runner\_work\benchmarking\benchmarking\cpython\PCBuild\amd64 "-IC:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.41.34120\include" "-IC:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\VS\include" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.22621.0\ucrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\um" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\shared" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\winrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\cppwinrt" /EHsc /Tpsrc/greenlet/greenlet.cpp /Fobuild\temp.win-amd64-cpython-314\Release\src/greenlet/greenlet.obj /EHsr /GT
  greenlet.cpp
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal\pycore_stackref.h(168): error C7555: use of designated initializers requires at least '/std:c++20'
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal\pycore_stackref.h(168): error C2737: 'PyStackRef_NULL': const object must be initialized
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(196): error C7555: use of designated initializers requires at least '/std:c++20'
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(196): error C4576: a parenthesized type followed by an initializer list is a non-standard explicit type conversion syntax
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(378): error C7555: use of designated initializers requires at least '/std:c++20'
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(378): error C4576: a parenthesized type followed by an initializer list is a non-standard explicit type conversion syntax
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(379): error C7555: use of designated initializers requires at least '/std:c++20'
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(379): error C4576: a parenthesized type followed by an initializer list is a non-standard explicit type conversion syntax
  error: command 'C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\VC\\Tools\\MSVC\\14.41.34120\\bin\\HostX86\\x64\\cl.exe' failed with exit code 2
  [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for greenlet
Failed to build greenlet
ERROR: ERROR: Failed to build installable wheels for some pyproject.toml based projects (greenlet)
Command failed with exit code 1


==================================================
```

</details>

## sqlalchemy_declarative on windows-x86 default

<details>
<summary>Log for sqlalchemy_declarative on windows-x86 default</summary>

```
  copying src\greenlet\platform\switch_arm32_ios.h -> build\lib.win32-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_arm64_masm.asm -> build\lib.win32-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_arm64_masm.obj -> build\lib.win32-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_arm64_msvc.h -> build\lib.win32-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_csky_gcc.h -> build\lib.win32-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_loongarch64_linux.h -> build\lib.win32-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_m68k_gcc.h -> build\lib.win32-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_mips_unix.h -> build\lib.win32-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_ppc64_aix.h -> build\lib.win32-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_ppc64_linux.h -> build\lib.win32-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_ppc_aix.h -> build\lib.win32-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_ppc_linux.h -> build\lib.win32-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_ppc_macosx.h -> build\lib.win32-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_ppc_unix.h -> build\lib.win32-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_riscv_unix.h -> build\lib.win32-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_s390_unix.h -> build\lib.win32-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_sh_gcc.h -> build\lib.win32-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_sparc_sun_gcc.h -> build\lib.win32-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_x32_unix.h -> build\lib.win32-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_x64_masm.asm -> build\lib.win32-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_x64_masm.obj -> build\lib.win32-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_x64_msvc.h -> build\lib.win32-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_x86_msvc.h -> build\lib.win32-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_x86_unix.h -> build\lib.win32-cpython-314\greenlet\platform
  copying src\greenlet\tests\_test_extension.c -> build\lib.win32-cpython-314\greenlet\tests
  copying src\greenlet\tests\_test_extension_cpp.cpp -> build\lib.win32-cpython-314\greenlet\tests
  running build_ext
  building 'greenlet._greenlet' extension
  creating build\temp.win32-cpython-314\Release\src\greenlet
  "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.41.34120\bin\HostX86\x86\cl.exe" /c /nologo /O2 /W3 /GL /DNDEBUG /MD -DWIN32=1 -IC:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-1d2c37c6a427-compat-cb6a104a6688-bm-sqlalchemy_declarative\include -IC:\actions-runner\_work\benchmarking\benchmarking\cpython\include -IC:\actions-runner\_work\benchmarking\benchmarking\cpython\PCBuild\win32 -IC:\actions-runner\_work\benchmarking\benchmarking\cpython\PCBuild\win32 "-IC:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.41.34120\include" "-IC:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\VS\include" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.22621.0\ucrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\um" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\shared" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\winrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\cppwinrt" /EHsc /Tpsrc/greenlet/greenlet.cpp /Fobuild\temp.win32-cpython-314\Release\src/greenlet/greenlet.obj /EHsr /GT
  greenlet.cpp
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal\pycore_stackref.h(168): error C7555: use of designated initializers requires at least '/std:c++20'
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal\pycore_stackref.h(168): error C2737: 'PyStackRef_NULL': const object must be initialized
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(196): error C7555: use of designated initializers requires at least '/std:c++20'
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(196): error C4576: a parenthesized type followed by an initializer list is a non-standard explicit type conversion syntax
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(378): error C7555: use of designated initializers requires at least '/std:c++20'
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(378): error C4576: a parenthesized type followed by an initializer list is a non-standard explicit type conversion syntax
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(379): error C7555: use of designated initializers requires at least '/std:c++20'
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(379): error C4576: a parenthesized type followed by an initializer list is a non-standard explicit type conversion syntax
  error: command 'C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\VC\\Tools\\MSVC\\14.41.34120\\bin\\HostX86\\x86\\cl.exe' failed with exit code 2
  [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for greenlet
Failed to build greenlet
ERROR: ERROR: Failed to build installable wheels for some pyproject.toml based projects (greenlet)
Command failed with exit code 1


==================================================
```

</details>

## sqlalchemy_imperative on windows-x86_64 default

<details>
<summary>Log for sqlalchemy_imperative on windows-x86_64 default</summary>

```
  copying src\greenlet\platform\switch_arm32_ios.h -> build\lib.win-amd64-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_arm64_masm.asm -> build\lib.win-amd64-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_arm64_masm.obj -> build\lib.win-amd64-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_arm64_msvc.h -> build\lib.win-amd64-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_csky_gcc.h -> build\lib.win-amd64-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_loongarch64_linux.h -> build\lib.win-amd64-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_m68k_gcc.h -> build\lib.win-amd64-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_mips_unix.h -> build\lib.win-amd64-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_ppc64_aix.h -> build\lib.win-amd64-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_ppc64_linux.h -> build\lib.win-amd64-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_ppc_aix.h -> build\lib.win-amd64-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_ppc_linux.h -> build\lib.win-amd64-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_ppc_macosx.h -> build\lib.win-amd64-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_ppc_unix.h -> build\lib.win-amd64-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_riscv_unix.h -> build\lib.win-amd64-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_s390_unix.h -> build\lib.win-amd64-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_sh_gcc.h -> build\lib.win-amd64-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_sparc_sun_gcc.h -> build\lib.win-amd64-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_x32_unix.h -> build\lib.win-amd64-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_x64_masm.asm -> build\lib.win-amd64-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_x64_masm.obj -> build\lib.win-amd64-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_x64_msvc.h -> build\lib.win-amd64-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_x86_msvc.h -> build\lib.win-amd64-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_x86_unix.h -> build\lib.win-amd64-cpython-314\greenlet\platform
  copying src\greenlet\tests\_test_extension.c -> build\lib.win-amd64-cpython-314\greenlet\tests
  copying src\greenlet\tests\_test_extension_cpp.cpp -> build\lib.win-amd64-cpython-314\greenlet\tests
  running build_ext
  building 'greenlet._greenlet' extension
  creating build\temp.win-amd64-cpython-314\Release\src\greenlet
  "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.41.34120\bin\HostX86\x64\cl.exe" /c /nologo /O2 /W3 /GL /DNDEBUG /MD -DWIN32=1 -IC:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-0db56efbb5b3-compat-cb6a104a6688-bm-sqlalchemy_imperative\include -IC:\actions-runner\_work\benchmarking\benchmarking\cpython\include -IC:\actions-runner\_work\benchmarking\benchmarking\cpython\PCBuild\amd64 -IC:\actions-runner\_work\benchmarking\benchmarking\cpython\PCBuild\amd64 "-IC:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.41.34120\include" "-IC:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\VS\include" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.22621.0\ucrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\um" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\shared" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\winrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\cppwinrt" /EHsc /Tpsrc/greenlet/greenlet.cpp /Fobuild\temp.win-amd64-cpython-314\Release\src/greenlet/greenlet.obj /EHsr /GT
  greenlet.cpp
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal\pycore_stackref.h(168): error C7555: use of designated initializers requires at least '/std:c++20'
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal\pycore_stackref.h(168): error C2737: 'PyStackRef_NULL': const object must be initialized
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(196): error C7555: use of designated initializers requires at least '/std:c++20'
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(196): error C4576: a parenthesized type followed by an initializer list is a non-standard explicit type conversion syntax
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(378): error C7555: use of designated initializers requires at least '/std:c++20'
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(378): error C4576: a parenthesized type followed by an initializer list is a non-standard explicit type conversion syntax
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(379): error C7555: use of designated initializers requires at least '/std:c++20'
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(379): error C4576: a parenthesized type followed by an initializer list is a non-standard explicit type conversion syntax
  error: command 'C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\VC\\Tools\\MSVC\\14.41.34120\\bin\\HostX86\\x64\\cl.exe' failed with exit code 2
  [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for greenlet
Failed to build greenlet
ERROR: ERROR: Failed to build installable wheels for some pyproject.toml based projects (greenlet)
Command failed with exit code 1


==================================================
```

</details>

## sqlalchemy_imperative on windows-x86 default

<details>
<summary>Log for sqlalchemy_imperative on windows-x86 default</summary>

```
  copying src\greenlet\platform\switch_arm32_ios.h -> build\lib.win32-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_arm64_masm.asm -> build\lib.win32-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_arm64_masm.obj -> build\lib.win32-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_arm64_msvc.h -> build\lib.win32-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_csky_gcc.h -> build\lib.win32-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_loongarch64_linux.h -> build\lib.win32-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_m68k_gcc.h -> build\lib.win32-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_mips_unix.h -> build\lib.win32-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_ppc64_aix.h -> build\lib.win32-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_ppc64_linux.h -> build\lib.win32-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_ppc_aix.h -> build\lib.win32-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_ppc_linux.h -> build\lib.win32-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_ppc_macosx.h -> build\lib.win32-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_ppc_unix.h -> build\lib.win32-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_riscv_unix.h -> build\lib.win32-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_s390_unix.h -> build\lib.win32-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_sh_gcc.h -> build\lib.win32-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_sparc_sun_gcc.h -> build\lib.win32-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_x32_unix.h -> build\lib.win32-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_x64_masm.asm -> build\lib.win32-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_x64_masm.obj -> build\lib.win32-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_x64_msvc.h -> build\lib.win32-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_x86_msvc.h -> build\lib.win32-cpython-314\greenlet\platform
  copying src\greenlet\platform\switch_x86_unix.h -> build\lib.win32-cpython-314\greenlet\platform
  copying src\greenlet\tests\_test_extension.c -> build\lib.win32-cpython-314\greenlet\tests
  copying src\greenlet\tests\_test_extension_cpp.cpp -> build\lib.win32-cpython-314\greenlet\tests
  running build_ext
  building 'greenlet._greenlet' extension
  creating build\temp.win32-cpython-314\Release\src\greenlet
  "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.41.34120\bin\HostX86\x86\cl.exe" /c /nologo /O2 /W3 /GL /DNDEBUG /MD -DWIN32=1 -IC:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-1d2c37c6a427-compat-cb6a104a6688-bm-sqlalchemy_imperative\include -IC:\actions-runner\_work\benchmarking\benchmarking\cpython\include -IC:\actions-runner\_work\benchmarking\benchmarking\cpython\PCBuild\win32 -IC:\actions-runner\_work\benchmarking\benchmarking\cpython\PCBuild\win32 "-IC:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.41.34120\include" "-IC:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\VS\include" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.22621.0\ucrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\um" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\shared" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\winrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\cppwinrt" /EHsc /Tpsrc/greenlet/greenlet.cpp /Fobuild\temp.win32-cpython-314\Release\src/greenlet/greenlet.obj /EHsr /GT
  greenlet.cpp
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal\pycore_stackref.h(168): error C7555: use of designated initializers requires at least '/std:c++20'
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal\pycore_stackref.h(168): error C2737: 'PyStackRef_NULL': const object must be initialized
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(196): error C7555: use of designated initializers requires at least '/std:c++20'
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(196): error C4576: a parenthesized type followed by an initializer list is a non-standard explicit type conversion syntax
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(378): error C7555: use of designated initializers requires at least '/std:c++20'
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(378): error C4576: a parenthesized type followed by an initializer list is a non-standard explicit type conversion syntax
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(379): error C7555: use of designated initializers requires at least '/std:c++20'
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(379): error C4576: a parenthesized type followed by an initializer list is a non-standard explicit type conversion syntax
  error: command 'C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\VC\\Tools\\MSVC\\14.41.34120\\bin\\HostX86\\x86\\cl.exe' failed with exit code 2
  [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for greenlet
Failed to build greenlet
ERROR: ERROR: Failed to build installable wheels for some pyproject.toml based projects (greenlet)
Command failed with exit code 1


==================================================
```

</details>

## tornado_http on darwin-arm64 default

<details>
<summary>Log for tornado_http on darwin-arm64 default</summary>

```
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.12/site-packages/pyperformance/data-files/benchmarks/bm_tornado_http/run_benchmark.py", line 54, in make_http_server
    server.add_sockets(sockets)
    ~~~~~~~~~~~~~~~~~~^^^^^^^^^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688/lib/python3.14/site-packages/tornado/tcpserver.py", line 204, in add_sockets
    self._handlers[sock.fileno()] = add_accept_handler(
                                    ~~~~~~~~~~~~~~~~~~^
        sock, self._handle_connection
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688/lib/python3.14/site-packages/tornado/netutil.py", line 247, in add_accept_handler
    io_loop = IOLoop.current()
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688/lib/python3.14/site-packages/tornado/ioloop.py", line 265, in current
    loop = asyncio.get_event_loop()
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/cpython/Lib/asyncio/events.py", line 681, in get_event_loop
    raise RuntimeError('There is no current event loop in thread %r.'
                       % threading.current_thread().name)
RuntimeError: There is no current event loop in thread 'MainThread'.
Traceback (most recent call last):
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.12/site-packages/pyperformance/data-files/benchmarks/bm_tornado_http/run_benchmark.py", line 102, in <module>
    runner.bench_time_func('tornado_http', bench_tornado)
    ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_runner.py", line 499, in bench_time_func
    result = self._main(task)
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_runner.py", line 465, in _main
    bench = self._manager()
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_runner.py", line 678, in _manager
    bench = Manager(self).create_bench()
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_manager.py", line 243, in create_bench
    worker_bench, run = self.create_worker_bench()
                        ~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_manager.py", line 142, in create_worker_bench
    suite = self.create_suite()
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_manager.py", line 132, in create_suite
    suite = self.spawn_worker(self.calibrate_loops, 0)
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_manager.py", line 118, in spawn_worker
    raise RuntimeError("%s failed with exit code %s"
                       % (cmd[0], exitcode))
RuntimeError: /Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b1ea5acca20e-compat-cb6a104a6688/bin/python failed with exit code 1
Traceback (most recent call last):
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.12/site-packages/pyperformance/run.py", line 170, in run_benchmarks
    result = bench.run(
             ^^^^^^^^^^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.12/site-packages/pyperformance/_benchmark.py", line 189, in run
    bench = _run_perf_script(
            ^^^^^^^^^^^^^^^^^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.12/site-packages/pyperformance/_benchmark.py", line 240, in _run_perf_script
    raise RuntimeError("Benchmark died")
RuntimeError: Benchmark died
Command failed with exit code 1
```

</details>

## tornado_http on linux-aarch64 default

<details>
<summary>Log for tornado_http on linux-aarch64 default</summary>

```
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/data-files/benchmarks/bm_tornado_http/run_benchmark.py", line 54, in make_http_server
    server.add_sockets(sockets)
    ~~~~~~~~~~~~~~~~~~^^^^^^^^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-6e18c82301b6-compat-cb6a104a6688/lib/python3.14/site-packages/tornado/tcpserver.py", line 204, in add_sockets
    self._handlers[sock.fileno()] = add_accept_handler(
                                    ~~~~~~~~~~~~~~~~~~^
        sock, self._handle_connection
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-6e18c82301b6-compat-cb6a104a6688/lib/python3.14/site-packages/tornado/netutil.py", line 247, in add_accept_handler
    io_loop = IOLoop.current()
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-6e18c82301b6-compat-cb6a104a6688/lib/python3.14/site-packages/tornado/ioloop.py", line 265, in current
    loop = asyncio.get_event_loop()
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/cpython/Lib/asyncio/events.py", line 681, in get_event_loop
    raise RuntimeError('There is no current event loop in thread %r.'
                       % threading.current_thread().name)
RuntimeError: There is no current event loop in thread 'MainThread'.
Traceback (most recent call last):
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/data-files/benchmarks/bm_tornado_http/run_benchmark.py", line 102, in <module>
    runner.bench_time_func('tornado_http', bench_tornado)
    ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-6e18c82301b6-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_runner.py", line 499, in bench_time_func
    result = self._main(task)
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-6e18c82301b6-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_runner.py", line 465, in _main
    bench = self._manager()
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-6e18c82301b6-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_runner.py", line 678, in _manager
    bench = Manager(self).create_bench()
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-6e18c82301b6-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_manager.py", line 243, in create_bench
    worker_bench, run = self.create_worker_bench()
                        ~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-6e18c82301b6-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_manager.py", line 142, in create_worker_bench
    suite = self.create_suite()
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-6e18c82301b6-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_manager.py", line 132, in create_suite
    suite = self.spawn_worker(self.calibrate_loops, 0)
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-6e18c82301b6-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_manager.py", line 118, in spawn_worker
    raise RuntimeError("%s failed with exit code %s"
                       % (cmd[0], exitcode))
RuntimeError: /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-6e18c82301b6-compat-cb6a104a6688/bin/python failed with exit code 1
Traceback (most recent call last):
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/run.py", line 170, in run_benchmarks
    result = bench.run(
             ^^^^^^^^^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/_benchmark.py", line 189, in run
    bench = _run_perf_script(
            ^^^^^^^^^^^^^^^^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/_benchmark.py", line 240, in _run_perf_script
    raise RuntimeError("Benchmark died")
RuntimeError: Benchmark died
Command failed with exit code 1
```

</details>

## tornado_http on collect-stats pystats

<details>
<summary>Log for tornado_http on collect-stats pystats</summary>

```
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-7c12bab99a20-compat-cb6a104a6688/lib/python3.14/site-packages/tornado/tcpserver.py", line 204, in add_sockets
    self._handlers[sock.fileno()] = add_accept_handler(
                                    ~~~~~~~~~~~~~~~~~~^
        sock, self._handle_connection
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-7c12bab99a20-compat-cb6a104a6688/lib/python3.14/site-packages/tornado/netutil.py", line 247, in add_accept_handler
    io_loop = IOLoop.current()
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-7c12bab99a20-compat-cb6a104a6688/lib/python3.14/site-packages/tornado/ioloop.py", line 265, in current
    loop = asyncio.get_event_loop()
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/cpython/Lib/asyncio/events.py", line 681, in get_event_loop
    raise RuntimeError('There is no current event loop in thread %r.'
                       % threading.current_thread().name)
RuntimeError: There is no current event loop in thread 'MainThread'.
Traceback (most recent call last):
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/data-files/benchmarks/bm_tornado_http/run_benchmark.py", line 102, in <module>
    runner.bench_time_func('tornado_http', bench_tornado)
    ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-7c12bab99a20-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_runner.py", line 499, in bench_time_func
    result = self._main(task)
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-7c12bab99a20-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_runner.py", line 465, in _main
    bench = self._manager()
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-7c12bab99a20-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_runner.py", line 678, in _manager
    bench = Manager(self).create_bench()
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-7c12bab99a20-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_manager.py", line 243, in create_bench
    worker_bench, run = self.create_worker_bench()
                        ~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-7c12bab99a20-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_manager.py", line 142, in create_worker_bench
    suite = self.create_suite()
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-7c12bab99a20-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_manager.py", line 136, in create_suite
    suite = self.spawn_worker(0, 0)
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-7c12bab99a20-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_manager.py", line 118, in spawn_worker
    raise RuntimeError("%s failed with exit code %s"
                       % (cmd[0], exitcode))
RuntimeError: /home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-7c12bab99a20-compat-cb6a104a6688/bin/python failed with exit code 1
Traceback (most recent call last):
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/run.py", line 170, in run_benchmarks
    result = bench.run(
             ^^^^^^^^^^
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/_benchmark.py", line 189, in run
    bench = _run_perf_script(
            ^^^^^^^^^^^^^^^^^
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/_benchmark.py", line 240, in _run_perf_script
    raise RuntimeError("Benchmark died")
RuntimeError: Benchmark died
Python benchmark suite 1.11.0


==================================================
```

</details>

## tornado_http on linux-x86_64 default

<details>
<summary>Log for tornado_http on linux-x86_64 default</summary>

```
# /home/ddfun/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0e992284450f-compat-cb6a104a6688/bin/python -u /home/ddfun/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/data-files/benchmarks/bm_tornado_http/run_benchmark.py --inherit-environ PYTHON_JIT,PYPERFORMANCE_RUNID --output /tmp/tmpsz_s8117
Traceback (most recent call last):
  File "/home/ddfun/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/data-files/benchmarks/bm_tornado_http/run_benchmark.py", line 102, in <module>
    runner.bench_time_func('tornado_http', bench_tornado)
Command failed with exit code 1
```

</details>

## tornado_http on windows-x86_64 default

<details>
<summary>Log for tornado_http on windows-x86_64 default</summary>

```
# 'C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-0db56efbb5b3-compat-cb6a104a6688\Scripts\python.exe' -u 'C:\actions-runner\_work\benchmarking\benchmarking\venv\Lib\site-packages\pyperformance\data-files\benchmarks\bm_tornado_http\run_benchmark.py' --inherit-environ PYPERFORMANCE_RUNID,PYTHON_JIT --output 'C:\WINDOWS\SERVIC~1\NETWOR~1\AppData\Local\Temp\tmp7cy0hdx8'
Traceback (most recent call last):
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\Lib\site-packages\pyperformance\data-files\benchmarks\bm_tornado_http\run_benchmark.py", line 102, in <module>
    runner.bench_time_func('tornado_http', bench_tornado)
Command failed with exit code 1
```

</details>

## tornado_http on windows-x86 default

<details>
<summary>Log for tornado_http on windows-x86 default</summary>

```
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\Lib\site-packages\pyperformance\data-files\benchmarks\bm_tornado_http\run_benchmark.py", line 54, in make_http_server
    server.add_sockets(sockets)
    ~~~~~~~~~~~~~~~~~~^^^^^^^^^
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-1d2c37c6a427-compat-cb6a104a6688\Lib\site-packages\tornado\tcpserver.py", line 204, in add_sockets
    self._handlers[sock.fileno()] = add_accept_handler(
                                    ~~~~~~~~~~~~~~~~~~^
        sock, self._handle_connection
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-1d2c37c6a427-compat-cb6a104a6688\Lib\site-packages\tornado\netutil.py", line 247, in add_accept_handler
    io_loop = IOLoop.current()
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-1d2c37c6a427-compat-cb6a104a6688\Lib\site-packages\tornado\ioloop.py", line 265, in current
    loop = asyncio.get_event_loop()
  File "C:\actions-runner\_work\benchmarking\benchmarking\cpython\Lib\asyncio\events.py", line 681, in get_event_loop
    raise RuntimeError('There is no current event loop in thread %r.'
                       % threading.current_thread().name)
RuntimeError: There is no current event loop in thread 'MainThread'.
Traceback (most recent call last):
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\Lib\site-packages\pyperformance\data-files\benchmarks\bm_tornado_http\run_benchmark.py", line 102, in <module>
    runner.bench_time_func('tornado_http', bench_tornado)
    ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-1d2c37c6a427-compat-cb6a104a6688\Lib\site-packages\pyperf\_runner.py", line 499, in bench_time_func
    result = self._main(task)
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-1d2c37c6a427-compat-cb6a104a6688\Lib\site-packages\pyperf\_runner.py", line 465, in _main
    bench = self._manager()
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-1d2c37c6a427-compat-cb6a104a6688\Lib\site-packages\pyperf\_runner.py", line 678, in _manager
    bench = Manager(self).create_bench()
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-1d2c37c6a427-compat-cb6a104a6688\Lib\site-packages\pyperf\_manager.py", line 243, in create_bench
    worker_bench, run = self.create_worker_bench()
                        ~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-1d2c37c6a427-compat-cb6a104a6688\Lib\site-packages\pyperf\_manager.py", line 142, in create_worker_bench
    suite = self.create_suite()
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-1d2c37c6a427-compat-cb6a104a6688\Lib\site-packages\pyperf\_manager.py", line 132, in create_suite
    suite = self.spawn_worker(self.calibrate_loops, 0)
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-1d2c37c6a427-compat-cb6a104a6688\Lib\site-packages\pyperf\_manager.py", line 118, in spawn_worker
    raise RuntimeError("%s failed with exit code %s"
                       % (cmd[0], exitcode))
RuntimeError: C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-1d2c37c6a427-compat-cb6a104a6688\Scripts\python.exe failed with exit code 1
Traceback (most recent call last):
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\Lib\site-packages\pyperformance\run.py", line 170, in run_benchmarks
    result = bench.run(
             ^^^^^^^^^^
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\Lib\site-packages\pyperformance\_benchmark.py", line 189, in run
    bench = _run_perf_script(
            ^^^^^^^^^^^^^^^^^
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\Lib\site-packages\pyperformance\_benchmark.py", line 240, in _run_perf_script
    raise RuntimeError("Benchmark died")
RuntimeError: Benchmark died
Command failed with exit code 1
```

</details>

