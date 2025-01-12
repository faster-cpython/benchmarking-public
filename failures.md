| benchmark | collect-stats | darwin-arm64 | linux-aarch64 | linux-x86_64 | windows-x86 | windows-x86_64 |
| --- | --- | --- | --- | --- | --- | --- |
| aiohttp |  | [[default run]](#aiohttp-on-darwin-arm64-default) | [[default run]](#aiohttp-on-linux-aarch64-default) | [[default run]](#aiohttp-on-linux-x86_64-default) | [[default run]](#aiohttp-on-windows-x86-default) | [[default run]](#aiohttp-on-windows-x86_64-default) |
| chameleon | [[pystats run]](#chameleon-on-collect-stats-pystats) | [[default run]](#chameleon-on-darwin-arm64-default) | [[default run]](#chameleon-on-linux-aarch64-default) | [[default run]](#chameleon-on-linux-x86_64-default) | [[default run]](#chameleon-on-windows-x86-default) | [[default run]](#chameleon-on-windows-x86_64-default) |
| dask |  | [[default run]](#dask-on-darwin-arm64-default) |  |  |  |  |
| djangocms | [[pystats build]](#djangocms-on-collect-stats-pystats) | [[default build]](#djangocms-on-darwin-arm64-default) | [[default run]](#djangocms-on-linux-aarch64-default) | [[default run]](#djangocms-on-linux-x86_64-default) | [[default build]](#djangocms-on-windows-x86-default) | [[default build]](#djangocms-on-windows-x86_64-default) |
| flaskblogging | [[pystats run]](#flaskblogging-on-collect-stats-pystats) | [[default run]](#flaskblogging-on-darwin-arm64-default) | [[default run]](#flaskblogging-on-linux-aarch64-default) | [[default run]](#flaskblogging-on-linux-x86_64-default) | [[default run]](#flaskblogging-on-windows-x86-default) | [[default run]](#flaskblogging-on-windows-x86_64-default) |
| gevent_hub | [[pystats run]](#gevent_hub-on-collect-stats-pystats) | [[default run]](#gevent_hub-on-darwin-arm64-default) | [[default run]](#gevent_hub-on-linux-aarch64-default) | [[default run]](#gevent_hub-on-linux-x86_64-default) | [[default build]](#gevent_hub-on-windows-x86-default) | [[default build]](#gevent_hub-on-windows-x86_64-default) |
| gunicorn | [[pystats run]](#gunicorn-on-collect-stats-pystats) | [[default run]](#gunicorn-on-darwin-arm64-default) | [[default run]](#gunicorn-on-linux-aarch64-default) | [[default run]](#gunicorn-on-linux-x86_64-default) | [[default run]](#gunicorn-on-windows-x86-default) | [[default run]](#gunicorn-on-windows-x86_64-default) |
| kinto | [[pystats run]](#kinto-on-collect-stats-pystats) | [[default build]](#kinto-on-darwin-arm64-default) | [[default build]](#kinto-on-linux-aarch64-default) | [[default build]](#kinto-on-linux-x86_64-default) | [[default build]](#kinto-on-windows-x86-default) | [[default build]](#kinto-on-windows-x86_64-default) |
| mypy2 | [[pystats build]](#mypy2-on-collect-stats-pystats) | [[default build]](#mypy2-on-darwin-arm64-default) | [[default build]](#mypy2-on-linux-aarch64-default) | [[default build]](#mypy2-on-linux-x86_64-default) | [[default build]](#mypy2-on-windows-x86-default) | [[default build]](#mypy2-on-windows-x86_64-default) |
| pytorch_alexnet_inference | [[pystats build]](#pytorch_alexnet_inference-on-collect-stats-pystats) | [[default build]](#pytorch_alexnet_inference-on-darwin-arm64-default) | [[default build]](#pytorch_alexnet_inference-on-linux-aarch64-default) | [[default build]](#pytorch_alexnet_inference-on-linux-x86_64-default) | [[default build]](#pytorch_alexnet_inference-on-windows-x86-default) | [[default build]](#pytorch_alexnet_inference-on-windows-x86_64-default) |
| sqlalchemy_declarative |  |  |  |  | [[default build]](#sqlalchemy_declarative-on-windows-x86-default) | [[default build]](#sqlalchemy_declarative-on-windows-x86_64-default) |
| sqlalchemy_imperative |  |  |  |  | [[default build]](#sqlalchemy_imperative-on-windows-x86-default) | [[default build]](#sqlalchemy_imperative-on-windows-x86_64-default) |
| tornado_http | [[pystats run]](#tornado_http-on-collect-stats-pystats) | [[default run]](#tornado_http-on-darwin-arm64-default) | [[default run]](#tornado_http-on-linux-aarch64-default) | [[default run]](#tornado_http-on-linux-x86_64-default) | [[default run]](#tornado_http-on-windows-x86-default) | [[default run]](#tornado_http-on-windows-x86_64-default) |
## aiohttp on linux-aarch64 default

<details>
<summary>Log for aiohttp on linux-aarch64 default</summary>

```
# /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688/bin/python -u /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_aiohttp/run_benchmark.py --inherit-environ PYPERFORMANCE_RUNID,PYTHON_JIT --output /tmp/tmp01dh5hah
Traceback (most recent call last):
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_aiohttp/run_benchmark.py", line 69, in <module>
    with context:
         ^^^^^^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/cpython/Lib/contextlib.py", line 141, in __enter__
    return next(self.gen)
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_aiohttp/netutils.py", line 36, in serving
    waitUntilUp(addr)
    ~~~~~~~~~~~^^^^^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_aiohttp/netutils.py", line 66, in waitUntilUp
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

## aiohttp on darwin-arm64 default

<details>
<summary>Log for aiohttp on darwin-arm64 default</summary>

```
# /Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688/bin/python -u /Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_aiohttp/run_benchmark.py --inherit-environ PYPERFORMANCE_RUNID,PYTHON_JIT --output /tmp/tmp3qmrkwni
Traceback (most recent call last):
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_aiohttp/run_benchmark.py", line 69, in <module>
    with context:
         ^^^^^^^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/cpython/Lib/contextlib.py", line 141, in __enter__
    return next(self.gen)
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_aiohttp/netutils.py", line 36, in serving
    waitUntilUp(addr)
    ~~~~~~~~~~~^^^^^^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_aiohttp/netutils.py", line 66, in waitUntilUp
    raise Exception('Timeout reached when trying to connect')
Exception: Timeout reached when trying to connect
Traceback (most recent call last):
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.13/site-packages/pyperformance/run.py", line 170, in run_benchmarks
    result = bench.run(
        bench_venv.python,
    ...<3 lines>...
        verbose=options.verbose,
    )
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.13/site-packages/pyperformance/_benchmark.py", line 189, in run
    bench = _run_perf_script(
        python,
    ...<4 lines>...
        verbose=verbose,
    )
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.13/site-packages/pyperformance/_benchmark.py", line 240, in _run_perf_script
    raise RuntimeError("Benchmark died")
RuntimeError: Benchmark died
Command failed with exit code 1
```

</details>

## aiohttp on windows-x86_64 default

<details>
<summary>Log for aiohttp on windows-x86_64 default</summary>

```
# 'C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-81fae27ee7dd-compat-cb6a104a6688\Scripts\python.exe' -u 'C:\actions-runner\_work\benchmarking\benchmarking\pyston-benchmarks\benchmarks\bm_aiohttp\run_benchmark.py' --inherit-environ PYPERFORMANCE_RUNID,PYTHON_JIT --output 'C:\WINDOWS\SERVIC~1\NETWOR~1\AppData\Local\Temp\tmpanf8b2ti'
Traceback (most recent call last):
  File "C:\actions-runner\_work\benchmarking\benchmarking\pyston-benchmarks\benchmarks\bm_aiohttp\run_benchmark.py", line 69, in <module>
    with context:
         ^^^^^^^
  File "C:\actions-runner\_work\benchmarking\benchmarking\cpython\Lib\contextlib.py", line 141, in __enter__
    return next(self.gen)
  File "C:\actions-runner\_work\benchmarking\benchmarking\pyston-benchmarks\benchmarks\bm_aiohttp\netutils.py", line 36, in serving
    waitUntilUp(addr)
    ~~~~~~~~~~~^^^^^^
  File "C:\actions-runner\_work\benchmarking\benchmarking\pyston-benchmarks\benchmarks\bm_aiohttp\netutils.py", line 66, in waitUntilUp
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

## aiohttp on linux-x86_64 default

<details>
<summary>Log for aiohttp on linux-x86_64 default</summary>

```
# /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688/bin/python -u /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_aiohttp/run_benchmark.py --inherit-environ PYPERFORMANCE_RUNID,PYTHON_JIT --output /tmp/tmp6wz83u91
Traceback (most recent call last):
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_aiohttp/run_benchmark.py", line 69, in <module>
    with context:
         ^^^^^^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/cpython/Lib/contextlib.py", line 141, in __enter__
    return next(self.gen)
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_aiohttp/netutils.py", line 36, in serving
    waitUntilUp(addr)
    ~~~~~~~~~~~^^^^^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_aiohttp/netutils.py", line 66, in waitUntilUp
##[error]    raise Exception('Timeout reached when trying to connect')
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

## aiohttp on windows-x86 default

<details>
<summary>Log for aiohttp on windows-x86 default</summary>

```
# 'C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-89a32d3d62d8-compat-cb6a104a6688\Scripts\python.exe' -u 'C:\actions-runner\_work\benchmarking\benchmarking\pyston-benchmarks\benchmarks\bm_aiohttp\run_benchmark.py' --inherit-environ PYTHON_JIT,PYPERFORMANCE_RUNID --output 'C:\WINDOWS\SERVIC~1\NETWOR~1\AppData\Local\Temp\tmppdi8rzz2'
Traceback (most recent call last):
  File "C:\actions-runner\_work\benchmarking\benchmarking\pyston-benchmarks\benchmarks\bm_aiohttp\run_benchmark.py", line 69, in <module>
    with context:
         ^^^^^^^
  File "C:\actions-runner\_work\benchmarking\benchmarking\cpython\Lib\contextlib.py", line 141, in __enter__
    return next(self.gen)
  File "C:\actions-runner\_work\benchmarking\benchmarking\pyston-benchmarks\benchmarks\bm_aiohttp\netutils.py", line 36, in serving
    waitUntilUp(addr)
    ~~~~~~~~~~~^^^^^^
  File "C:\actions-runner\_work\benchmarking\benchmarking\pyston-benchmarks\benchmarks\bm_aiohttp\netutils.py", line 66, in waitUntilUp
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

## chameleon on collect-stats pystats

<details>
<summary>Log for chameleon on collect-stats pystats</summary>

```
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0d57dd0c23e2-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/zpt/template.py", line 205, in __init__
    super(PageTemplate, self).__init__(body, **config)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0d57dd0c23e2-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/template.py", line 137, in __init__
    self.write(body)
    ~~~~~~~~~~^^^^^^
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0d57dd0c23e2-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/template.py", line 235, in write
    self.cook(body)
    ~~~~~~~~~^^^^^^
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0d57dd0c23e2-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/template.py", line 167, in cook
    program = self._cook(body, digest, names)
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0d57dd0c23e2-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/template.py", line 245, in _cook
    source = self._compile(body, builtins)
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0d57dd0c23e2-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/template.py", line 276, in _compile
    program = self.parse(body)
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0d57dd0c23e2-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/zpt/template.py", line 227, in parse
    return MacroProgram(
        body, self.mode, self.filename,
    ...<9 lines>...
        tokenizer=self.tokenizer
    )
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0d57dd0c23e2-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/zpt/program.py", line 174, in __init__
    super(MacroProgram, self).__init__(*args, **kwargs)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0d57dd0c23e2-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/program.py", line 35, in __init__
    node = self.visit(kind, args)
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0d57dd0c23e2-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/program.py", line 41, in visit
    return visitor(*args)
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0d57dd0c23e2-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/zpt/program.py", line 320, in visit_element
    ATTRIBUTES = self._create_attributes_nodes(
        prepared, I18N_ATTRIBUTES, STATIC_ATTRIBUTES,
    )
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0d57dd0c23e2-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/zpt/program.py", line 794, in _create_attributes_nodes
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
Python benchmark suite 1.11.0


==================================================
```

</details>

## chameleon on linux-aarch64 default

<details>
<summary>Log for chameleon on linux-aarch64 default</summary>

```
# /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688/bin/python -u /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/data-files/benchmarks/bm_chameleon/run_benchmark.py --inherit-environ PYPERFORMANCE_RUNID,PYTHON_JIT --output /tmp/tmppafx60xk
Traceback (most recent call last):
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/data-files/benchmarks/bm_chameleon/run_benchmark.py", line 5, in <module>
    from chameleon import PageTemplate
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/__init__.py", line 1, in <module>
    from .zpt.template import PageTemplate
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/zpt/template.py", line 6, in <module>
    from ..tales import PythonExpr
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/tales.py", line 27, in <module>
    from .compiler import Interpolator
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/compiler.py", line 34, in <module>
    from .tal import ErrorInfo
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/tal.py", line 26, in <module>
    from chameleon import interfaces
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/interfaces.py", line 1, in <module>
    from zope.interface import Interface
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/__init__.py", line 58, in <module>
    _wire()
    ~~~~~^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 1154, in _wire
    from zope.interface.interfaces import IElement
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interfaces.py", line 56, in <module>
    class IElement(Interface):
    ...<93 lines>...
            """
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 794, in __init__
    self.__attrs = self.__compute_attrs(attrs)
                   ~~~~~~~~~~~~~~~~~~~~^^^^^^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 813, in __compute_attrs
    aname: update_value(aname, aval)
           ~~~~~~~~~~~~^^^^^^^^^^^^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 809, in update_value
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

## chameleon on darwin-arm64 default

<details>
<summary>Log for chameleon on darwin-arm64 default</summary>

```
Traceback (most recent call last):
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.13/site-packages/pyperformance/data-files/benchmarks/bm_chameleon/run_benchmark.py", line 5, in <module>
    from chameleon import PageTemplate
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/__init__.py", line 1, in <module>
    from .zpt.template import PageTemplate
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/zpt/template.py", line 6, in <module>
    from ..tales import PythonExpr
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/tales.py", line 27, in <module>
    from .compiler import Interpolator
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/compiler.py", line 34, in <module>
    from .tal import ErrorInfo
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/tal.py", line 26, in <module>
    from chameleon import interfaces
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/interfaces.py", line 1, in <module>
    from zope.interface import Interface
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/__init__.py", line 58, in <module>
    _wire()
    ~~~~~^^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 1154, in _wire
    from zope.interface.interfaces import IElement
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interfaces.py", line 56, in <module>
    class IElement(Interface):
    ...<93 lines>...
            """
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 794, in __init__
    self.__attrs = self.__compute_attrs(attrs)
                   ~~~~~~~~~~~~~~~~~~~~^^^^^^^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 813, in __compute_attrs
    aname: update_value(aname, aval)
           ~~~~~~~~~~~~^^^^^^^^^^^^^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 809, in update_value
    raise InvalidInterface("Concrete attribute, " + aname)
zope.interface.exceptions.InvalidInterface: Concrete attribute, __classdictcell__
Traceback (most recent call last):
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.13/site-packages/pyperformance/run.py", line 170, in run_benchmarks
    result = bench.run(
        bench_venv.python,
    ...<3 lines>...
        verbose=options.verbose,
    )
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.13/site-packages/pyperformance/_benchmark.py", line 189, in run
    bench = _run_perf_script(
        python,
    ...<4 lines>...
        verbose=verbose,
    )
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.13/site-packages/pyperformance/_benchmark.py", line 240, in _run_perf_script
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
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-81fae27ee7dd-compat-cb6a104a6688\Lib\site-packages\chameleon\zpt\template.py", line 205, in __init__
    super(PageTemplate, self).__init__(body, **config)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-81fae27ee7dd-compat-cb6a104a6688\Lib\site-packages\chameleon\template.py", line 137, in __init__
    self.write(body)
    ~~~~~~~~~~^^^^^^
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-81fae27ee7dd-compat-cb6a104a6688\Lib\site-packages\chameleon\template.py", line 235, in write
    self.cook(body)
    ~~~~~~~~~^^^^^^
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-81fae27ee7dd-compat-cb6a104a6688\Lib\site-packages\chameleon\template.py", line 167, in cook
    program = self._cook(body, digest, names)
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-81fae27ee7dd-compat-cb6a104a6688\Lib\site-packages\chameleon\template.py", line 245, in _cook
    source = self._compile(body, builtins)
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-81fae27ee7dd-compat-cb6a104a6688\Lib\site-packages\chameleon\template.py", line 276, in _compile
    program = self.parse(body)
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-81fae27ee7dd-compat-cb6a104a6688\Lib\site-packages\chameleon\zpt\template.py", line 227, in parse
    return MacroProgram(
        body, self.mode, self.filename,
    ...<9 lines>...
        tokenizer=self.tokenizer
    )
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-81fae27ee7dd-compat-cb6a104a6688\Lib\site-packages\chameleon\zpt\program.py", line 174, in __init__
    super(MacroProgram, self).__init__(*args, **kwargs)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-81fae27ee7dd-compat-cb6a104a6688\Lib\site-packages\chameleon\program.py", line 35, in __init__
    node = self.visit(kind, args)
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-81fae27ee7dd-compat-cb6a104a6688\Lib\site-packages\chameleon\program.py", line 41, in visit
    return visitor(*args)
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-81fae27ee7dd-compat-cb6a104a6688\Lib\site-packages\chameleon\zpt\program.py", line 320, in visit_element
    ATTRIBUTES = self._create_attributes_nodes(
        prepared, I18N_ATTRIBUTES, STATIC_ATTRIBUTES,
    )
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-81fae27ee7dd-compat-cb6a104a6688\Lib\site-packages\chameleon\zpt\program.py", line 794, in _create_attributes_nodes
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

## chameleon on linux-x86_64 default

<details>
<summary>Log for chameleon on linux-x86_64 default</summary>

```
# /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688/bin/python -u /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/data-files/benchmarks/bm_chameleon/run_benchmark.py --inherit-environ PYPERFORMANCE_RUNID,PYTHON_JIT --output /tmp/tmpr0t6i834
Traceback (most recent call last):
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/data-files/benchmarks/bm_chameleon/run_benchmark.py", line 5, in <module>
    from chameleon import PageTemplate
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/__init__.py", line 1, in <module>
    from .zpt.template import PageTemplate
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/zpt/template.py", line 6, in <module>
    from ..tales import PythonExpr
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/tales.py", line 27, in <module>
    from .compiler import Interpolator
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/compiler.py", line 34, in <module>
    from .tal import ErrorInfo
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/tal.py", line 26, in <module>
    from chameleon import interfaces
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688/lib/python3.14/site-packages/chameleon/interfaces.py", line 1, in <module>
    from zope.interface import Interface
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/__init__.py", line 58, in <module>
    _wire()
    ~~~~~^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 1154, in _wire
    from zope.interface.interfaces import IElement
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interfaces.py", line 56, in <module>
    class IElement(Interface):
    ...<93 lines>...
            """
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 794, in __init__
    self.__attrs = self.__compute_attrs(attrs)
                   ~~~~~~~~~~~~~~~~~~~~^^^^^^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 813, in __compute_attrs
    aname: update_value(aname, aval)
           ~~~~~~~~~~~~^^^^^^^^^^^^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 809, in update_value
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

## chameleon on windows-x86 default

<details>
<summary>Log for chameleon on windows-x86 default</summary>

```
    ~~~~^^
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\Lib\site-packages\pyperformance\data-files\benchmarks\bm_chameleon\run_benchmark.py", line 25, in main
    tmpl = PageTemplate(BIGTABLE_ZPT)
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-89a32d3d62d8-compat-cb6a104a6688\Lib\site-packages\chameleon\zpt\template.py", line 205, in __init__
    super(PageTemplate, self).__init__(body, **config)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-89a32d3d62d8-compat-cb6a104a6688\Lib\site-packages\chameleon\template.py", line 137, in __init__
    self.write(body)
    ~~~~~~~~~~^^^^^^
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-89a32d3d62d8-compat-cb6a104a6688\Lib\site-packages\chameleon\template.py", line 235, in write
    self.cook(body)
    ~~~~~~~~~^^^^^^
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-89a32d3d62d8-compat-cb6a104a6688\Lib\site-packages\chameleon\template.py", line 167, in cook
    program = self._cook(body, digest, names)
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-89a32d3d62d8-compat-cb6a104a6688\Lib\site-packages\chameleon\template.py", line 245, in _cook
    source = self._compile(body, builtins)
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-89a32d3d62d8-compat-cb6a104a6688\Lib\site-packages\chameleon\template.py", line 276, in _compile
    program = self.parse(body)
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-89a32d3d62d8-compat-cb6a104a6688\Lib\site-packages\chameleon\zpt\template.py", line 227, in parse
    return MacroProgram(
        body, self.mode, self.filename,
    ...<9 lines>...
        tokenizer=self.tokenizer
    )
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-89a32d3d62d8-compat-cb6a104a6688\Lib\site-packages\chameleon\zpt\program.py", line 174, in __init__
    super(MacroProgram, self).__init__(*args, **kwargs)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-89a32d3d62d8-compat-cb6a104a6688\Lib\site-packages\chameleon\program.py", line 35, in __init__
    node = self.visit(kind, args)
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-89a32d3d62d8-compat-cb6a104a6688\Lib\site-packages\chameleon\program.py", line 41, in visit
    return visitor(*args)
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-89a32d3d62d8-compat-cb6a104a6688\Lib\site-packages\chameleon\zpt\program.py", line 320, in visit_element
    ATTRIBUTES = self._create_attributes_nodes(
        prepared, I18N_ATTRIBUTES, STATIC_ATTRIBUTES,
    )
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-89a32d3d62d8-compat-cb6a104a6688\Lib\site-packages\chameleon\zpt\program.py", line 794, in _create_attributes_nodes
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
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688/lib/python3.14/site-packages/distributed/client.py", line 2341, in map
    futures = self._graph_to_futures(
        dsk,
    ...<9 lines>...
        span_metadata=SpanMetadata(collections=[{"type": "Future"}]),
    )
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688/lib/python3.14/site-packages/distributed/client.py", line 3355, in _graph_to_futures
    header, frames = serialize(ToPickle(dsk), on_error="raise")
                     ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688/lib/python3.14/site-packages/distributed/protocol/serialize.py", line 392, in serialize
    raise TypeError(msg, str_x) from exc
TypeError: ('Could not serialize object of type HighLevelGraph', '<ToPickle: HighLevelGraph with 1 layers.\n<dask.highlevelgraph.HighLevelGraph object at 0x1054ffb60>\n 0. 4384094736\n>')
Traceback (most recent call last):
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.13/site-packages/pyperformance/data-files/benchmarks/bm_dask/run_benchmark.py", line 32, in <module>
    runner.bench_async_func('dask', benchmark)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_runner.py", line 610, in bench_async_func
    result = self._main(task)
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_runner.py", line 465, in _main
    bench = self._manager()
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_runner.py", line 678, in _manager
    bench = Manager(self).create_bench()
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_manager.py", line 243, in create_bench
    worker_bench, run = self.create_worker_bench()
                        ~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_manager.py", line 142, in create_worker_bench
    suite = self.create_suite()
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_manager.py", line 132, in create_suite
    suite = self.spawn_worker(self.calibrate_loops, 0)
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_manager.py", line 118, in spawn_worker
    raise RuntimeError("%s failed with exit code %s"
                       % (cmd[0], exitcode))
RuntimeError: /Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688/bin/python failed with exit code 1
Traceback (most recent call last):
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.13/site-packages/pyperformance/run.py", line 170, in run_benchmarks
    result = bench.run(
        bench_venv.python,
    ...<3 lines>...
        verbose=options.verbose,
    )
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.13/site-packages/pyperformance/_benchmark.py", line 189, in run
    bench = _run_perf_script(
        python,
    ...<4 lines>...
        verbose=verbose,
    )
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.13/site-packages/pyperformance/_benchmark.py", line 240, in _run_perf_script
    raise RuntimeError("Benchmark died")
RuntimeError: Benchmark died
Command failed with exit code 1
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

## djangocms on linux-aarch64 default

<details>
<summary>Log for djangocms on linux-aarch64 default</summary>

```
# /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688/bin/python -u /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_djangocms/run_benchmark.py --inherit-environ PYPERFORMANCE_RUNID,PYTHON_JIT --output /tmp/tmp3qr681m4

Clone template using django-admin

Install requirements in /tmp/djangocms_bench_93vwyo05/testsite/requirements.in

Run migrations
django-admin startproject "testsite" --template https://github.com/django-cms/cms-template/archive/4.1.tar.gz
cd "/tmp/djangocms_bench_93vwyo05/testsite"
python -m pip install -r "/tmp/djangocms_bench_93vwyo05/testsite/requirements.in"
python -m manage migrate

CommandError: /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688/bin/python -m manage migrate failed.
Traceback (most recent call last):
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_djangocms/run_benchmark.py", line 234, in <module>
    sitedir, elapsed = setup(datadir)
                       ~~~~~^^^^^^^^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_djangocms/run_benchmark.py", line 75, in setup
    subprocess.check_call(ARGV_CREATE, cwd=rootdir)
    ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/cpython/Lib/subprocess.py", line 419, in check_call
    raise CalledProcessError(retcode, cmd)
subprocess.CalledProcessError: Command '['/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688/bin/djangocms', 'testsite', '--no-input']' returned non-zero exit status 1.
Command failed with exit code 1
Traceback (most recent call last):
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/run.py", line 170, in run_benchmarks
```

</details>

## djangocms on darwin-arm64 default

<details>
<summary>Log for djangocms on darwin-arm64 default</summary>

```
                                   ~~~~^^^^^^^^^^^^^^^^^^^^^^^^
        File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688-bm-djangocms/lib/python3.14/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 251, in build_wheel
          return _build_backend().build_wheel(wheel_directory, config_settings,
                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                                              metadata_directory)
                                              ^^^^^^^^^^^^^^^^^^^
        File "/private/tmp/pip-install-hxe1taju/pillow_05460d913d5a442b94576dc053e14352/_custom_build/backend.py", line 26, in build_wheel
          return super().build_wheel(wheel_directory, config_settings, metadata_directory)
                 ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "/private/tmp/pip-build-env-gdhggv7m/overlay/lib/python3.14/site-packages/setuptools/build_meta.py", line 438, in build_wheel
          return _build(['bdist_wheel', '--dist-info-dir', str(metadata_directory)])
        File "/private/tmp/pip-build-env-gdhggv7m/overlay/lib/python3.14/site-packages/setuptools/build_meta.py", line 426, in _build
          return self._build_with_temp_dir(
                 ~~~~~~~~~~~~~~~~~~~~~~~~~^
              cmd,
              ^^^^
          ...<3 lines>...
              self._arbitrary_args(config_settings),
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          )
          ^
        File "/private/tmp/pip-build-env-gdhggv7m/overlay/lib/python3.14/site-packages/setuptools/build_meta.py", line 407, in _build_with_temp_dir
          self.run_setup()
          ~~~~~~~~~~~~~~^^
        File "/private/tmp/pip-install-hxe1taju/pillow_05460d913d5a442b94576dc053e14352/_custom_build/backend.py", line 20, in run_setup
          return super().run_setup(setup_script)
                 ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^
        File "/private/tmp/pip-build-env-gdhggv7m/overlay/lib/python3.14/site-packages/setuptools/build_meta.py", line 320, in run_setup
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

## djangocms on windows-x86_64 default

<details>
<summary>Log for djangocms on windows-x86_64 default</summary>

```
    File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-81fae27ee7dd-compat-cb6a104a6688-bm-djangocms\Lib\site-packages\pip\_vendor\pyproject_hooks\_in_process\_in_process.py", line 251, in build_wheel
      return _build_backend().build_wheel(wheel_directory, config_settings,
             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                                          metadata_directory)
                                          ^^^^^^^^^^^^^^^^^^^
    File "C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\pip-install-uv6_9cpc\pillow_5db9d148dd70407da4ca107309ffb423\_custom_build\backend.py", line 26, in build_wheel
      return super().build_wheel(wheel_directory, config_settings, metadata_directory)
             ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\pip-build-env-sbebwssa\overlay\Lib\site-packages\setuptools\build_meta.py", line 438, in build_wheel
      return _build(['bdist_wheel', '--dist-info-dir', str(metadata_directory)])
    File "C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\pip-build-env-sbebwssa\overlay\Lib\site-packages\setuptools\build_meta.py", line 426, in _build
      return self._build_with_temp_dir(
             ~~~~~~~~~~~~~~~~~~~~~~~~~^
          cmd,
          ^^^^
      ...<3 lines>...
          self._arbitrary_args(config_settings),
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      )
      ^
    File "C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\pip-build-env-sbebwssa\overlay\Lib\site-packages\setuptools\build_meta.py", line 407, in _build_with_temp_dir
      self.run_setup()
      ~~~~~~~~~~~~~~^^
    File "C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\pip-install-uv6_9cpc\pillow_5db9d148dd70407da4ca107309ffb423\_custom_build\backend.py", line 20, in run_setup
      return super().run_setup(setup_script)
             ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^
    File "C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\pip-build-env-sbebwssa\overlay\Lib\site-packages\setuptools\build_meta.py", line 320, in run_setup
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

## djangocms on linux-x86_64 default

<details>
<summary>Log for djangocms on linux-x86_64 default</summary>

```
# /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688/bin/python -u /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_djangocms/run_benchmark.py --inherit-environ PYPERFORMANCE_RUNID,PYTHON_JIT --output /tmp/tmpvy303cb6

Clone template using django-admin

Install requirements in /tmp/djangocms_bench_dkkg6h6a/testsite/requirements.in

Run migrations
django-admin startproject "testsite" --template https://github.com/django-cms/cms-template/archive/4.1.tar.gz
cd "/tmp/djangocms_bench_dkkg6h6a/testsite"
python -m pip install -r "/tmp/djangocms_bench_dkkg6h6a/testsite/requirements.in"
python -m manage migrate

CommandError: /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688/bin/python -m manage migrate failed.
Traceback (most recent call last):
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_djangocms/run_benchmark.py", line 234, in <module>
    sitedir, elapsed = setup(datadir)
                       ~~~~~^^^^^^^^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_djangocms/run_benchmark.py", line 75, in setup
    subprocess.check_call(ARGV_CREATE, cwd=rootdir)
    ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/cpython/Lib/subprocess.py", line 419, in check_call
    raise CalledProcessError(retcode, cmd)
subprocess.CalledProcessError: Command '['/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688/bin/djangocms', 'testsite', '--no-input']' returned non-zero exit status 1.
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

## djangocms on windows-x86 default

<details>
<summary>Log for djangocms on windows-x86 default</summary>

```
    File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-89a32d3d62d8-compat-cb6a104a6688-bm-djangocms\Lib\site-packages\pip\_vendor\pyproject_hooks\_in_process\_in_process.py", line 251, in build_wheel
      return _build_backend().build_wheel(wheel_directory, config_settings,
             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                                          metadata_directory)
                                          ^^^^^^^^^^^^^^^^^^^
    File "C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\pip-install-86udrou8\pillow_794acbb7ff8045c6b3be823f2b0afc21\_custom_build\backend.py", line 26, in build_wheel
      return super().build_wheel(wheel_directory, config_settings, metadata_directory)
             ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\pip-build-env-j6gu_g07\overlay\Lib\site-packages\setuptools\build_meta.py", line 438, in build_wheel
      return _build(['bdist_wheel', '--dist-info-dir', str(metadata_directory)])
    File "C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\pip-build-env-j6gu_g07\overlay\Lib\site-packages\setuptools\build_meta.py", line 426, in _build
      return self._build_with_temp_dir(
             ~~~~~~~~~~~~~~~~~~~~~~~~~^
          cmd,
          ^^^^
      ...<3 lines>...
          self._arbitrary_args(config_settings),
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      )
      ^
    File "C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\pip-build-env-j6gu_g07\overlay\Lib\site-packages\setuptools\build_meta.py", line 407, in _build_with_temp_dir
      self.run_setup()
      ~~~~~~~~~~~~~~^^
    File "C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\pip-install-86udrou8\pillow_794acbb7ff8045c6b3be823f2b0afc21\_custom_build\backend.py", line 20, in run_setup
      return super().run_setup(setup_script)
             ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^
    File "C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\pip-build-env-j6gu_g07\overlay\Lib\site-packages\setuptools\build_meta.py", line 320, in run_setup
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

## flaskblogging on collect-stats pystats

<details>
<summary>Log for flaskblogging on collect-stats pystats</summary>

```
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_flaskblogging/netutils.py", line 66, in waitUntilUp
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

## flaskblogging on linux-aarch64 default

<details>
<summary>Log for flaskblogging on linux-aarch64 default</summary>

```
# /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688/bin/python -u /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_flaskblogging/run_benchmark.py --inherit-environ PYPERFORMANCE_RUNID,PYTHON_JIT --output /tmp/tmpr5s6t7gl
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

## flaskblogging on darwin-arm64 default

<details>
<summary>Log for flaskblogging on darwin-arm64 default</summary>

```
# /Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688/bin/python -u /Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_flaskblogging/run_benchmark.py --inherit-environ PYPERFORMANCE_RUNID,PYTHON_JIT --output /tmp/tmp8prpbr1z
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
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.13/site-packages/pyperformance/run.py", line 170, in run_benchmarks
    result = bench.run(
        bench_venv.python,
    ...<3 lines>...
        verbose=options.verbose,
    )
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.13/site-packages/pyperformance/_benchmark.py", line 189, in run
    bench = _run_perf_script(
        python,
    ...<4 lines>...
        verbose=verbose,
    )
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.13/site-packages/pyperformance/_benchmark.py", line 240, in _run_perf_script
    raise RuntimeError("Benchmark died")
RuntimeError: Benchmark died
Command failed with exit code 1
```

</details>

## flaskblogging on windows-x86_64 default

<details>
<summary>Log for flaskblogging on windows-x86_64 default</summary>

```
# 'C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-81fae27ee7dd-compat-cb6a104a6688\Scripts\python.exe' -u 'C:\actions-runner\_work\benchmarking\benchmarking\pyston-benchmarks\benchmarks\bm_flaskblogging\run_benchmark.py' --inherit-environ PYPERFORMANCE_RUNID,PYTHON_JIT --output 'C:\WINDOWS\SERVIC~1\NETWOR~1\AppData\Local\Temp\tmpz6h_k0r0'
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

## flaskblogging on linux-x86_64 default

<details>
<summary>Log for flaskblogging on linux-x86_64 default</summary>

```
# /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688/bin/python -u /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_flaskblogging/run_benchmark.py --inherit-environ PYPERFORMANCE_RUNID,PYTHON_JIT --output /tmp/tmpq78bsj3w
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
##[error]    raise Exception('Timeout reached when trying to connect')
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

## flaskblogging on windows-x86 default

<details>
<summary>Log for flaskblogging on windows-x86 default</summary>

```
# 'C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-89a32d3d62d8-compat-cb6a104a6688\Scripts\python.exe' -u 'C:\actions-runner\_work\benchmarking\benchmarking\pyston-benchmarks\benchmarks\bm_flaskblogging\run_benchmark.py' --inherit-environ PYTHON_JIT,PYPERFORMANCE_RUNID --output 'C:\WINDOWS\SERVIC~1\NETWOR~1\AppData\Local\Temp\tmph27h54ih'
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
Command failed with exit code 1
```

</details>

## gevent_hub on collect-stats pystats

<details>
<summary>Log for gevent_hub on collect-stats pystats</summary>

```
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0d57dd0c23e2-compat-cb6a104a6688/lib/python3.14/site-packages/gevent/_config.py", line 151, in get
    self.value = self.validate(self._default())
                 ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0d57dd0c23e2-compat-cb6a104a6688/lib/python3.14/site-packages/gevent/_config.py", line 259, in validate
    return self._import_one_of([self.shortname_map.get(x, x) for x in value])
           ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0d57dd0c23e2-compat-cb6a104a6688/lib/python3.14/site-packages/gevent/_config.py", line 230, in _import_one_of
    return self._import_one(item)
           ~~~~~~~~~~~~~~~~^^^^^^
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0d57dd0c23e2-compat-cb6a104a6688/lib/python3.14/site-packages/gevent/_config.py", line 248, in _import_one
    module = importlib.import_module(module)
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/cpython/Lib/importlib/__init__.py", line 88, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "src/gevent/libev/corecext.pyx", line 819, in init gevent.libev.corecext
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0d57dd0c23e2-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/__init__.py", line 58, in <module>
    _wire()
    ~~~~~^^
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0d57dd0c23e2-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 1154, in _wire
    from zope.interface.interfaces import IElement
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0d57dd0c23e2-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interfaces.py", line 56, in <module>
    class IElement(Interface):
    ...<93 lines>...
            """
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0d57dd0c23e2-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 794, in __init__
    self.__attrs = self.__compute_attrs(attrs)
                   ~~~~~~~~~~~~~~~~~~~~^^^^^^^
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0d57dd0c23e2-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 813, in __compute_attrs
    aname: update_value(aname, aval)
           ~~~~~~~~~~~~^^^^^^^^^^^^^
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0d57dd0c23e2-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 809, in update_value
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

## gevent_hub on linux-aarch64 default

<details>
<summary>Log for gevent_hub on linux-aarch64 default</summary>

```
    import gevent
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688/lib/python3.14/site-packages/gevent/__init__.py", line 71, in <module>
    from gevent._config import config
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688/lib/python3.14/site-packages/gevent/_config.py", line 730, in <module>
    Loop().get()
    ~~~~~~~~~~^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688/lib/python3.14/site-packages/gevent/_config.py", line 151, in get
    self.value = self.validate(self._default())
                 ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688/lib/python3.14/site-packages/gevent/_config.py", line 259, in validate
    return self._import_one_of([self.shortname_map.get(x, x) for x in value])
           ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688/lib/python3.14/site-packages/gevent/_config.py", line 230, in _import_one_of
    return self._import_one(item)
           ~~~~~~~~~~~~~~~~^^^^^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688/lib/python3.14/site-packages/gevent/_config.py", line 248, in _import_one
    module = importlib.import_module(module)
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/cpython/Lib/importlib/__init__.py", line 88, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "src/gevent/libev/corecext.pyx", line 819, in init gevent.libev.corecext
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/__init__.py", line 58, in <module>
    _wire()
    ~~~~~^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 1154, in _wire
    from zope.interface.interfaces import IElement
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interfaces.py", line 56, in <module>
    class IElement(Interface):
    ...<93 lines>...
            """
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 794, in __init__
    self.__attrs = self.__compute_attrs(attrs)
                   ~~~~~~~~~~~~~~~~~~~~^^^^^^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 813, in __compute_attrs
    aname: update_value(aname, aval)
           ~~~~~~~~~~~~^^^^^^^^^^^^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 809, in update_value
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

## gevent_hub on darwin-arm64 default

<details>
<summary>Log for gevent_hub on darwin-arm64 default</summary>

```
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688/lib/python3.14/site-packages/gevent/_config.py", line 151, in get
    self.value = self.validate(self._default())
                 ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688/lib/python3.14/site-packages/gevent/_config.py", line 259, in validate
    return self._import_one_of([self.shortname_map.get(x, x) for x in value])
           ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688/lib/python3.14/site-packages/gevent/_config.py", line 230, in _import_one_of
    return self._import_one(item)
           ~~~~~~~~~~~~~~~~^^^^^^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688/lib/python3.14/site-packages/gevent/_config.py", line 248, in _import_one
    module = importlib.import_module(module)
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/cpython/Lib/importlib/__init__.py", line 88, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "src/gevent/libev/corecext.pyx", line 819, in init gevent.libev.corecext
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/__init__.py", line 58, in <module>
    _wire()
    ~~~~~^^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 1154, in _wire
    from zope.interface.interfaces import IElement
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interfaces.py", line 56, in <module>
    class IElement(Interface):
    ...<93 lines>...
            """
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 794, in __init__
    self.__attrs = self.__compute_attrs(attrs)
                   ~~~~~~~~~~~~~~~~~~~~^^^^^^^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 813, in __compute_attrs
    aname: update_value(aname, aval)
           ~~~~~~~~~~~~^^^^^^^^^^^^^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 809, in update_value
    raise InvalidInterface("Concrete attribute, " + aname)
zope.interface.exceptions.InvalidInterface: Concrete attribute, __classdictcell__
Traceback (most recent call last):
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.13/site-packages/pyperformance/run.py", line 170, in run_benchmarks
    result = bench.run(
        bench_venv.python,
    ...<3 lines>...
        verbose=options.verbose,
    )
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.13/site-packages/pyperformance/_benchmark.py", line 189, in run
    bench = _run_perf_script(
        python,
    ...<4 lines>...
        verbose=verbose,
    )
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.13/site-packages/pyperformance/_benchmark.py", line 240, in _run_perf_script
    raise RuntimeError("Benchmark died")
RuntimeError: Benchmark died
Command failed with exit code 1
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
    "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.42.34433\bin\HostX86\x64\cl.exe" /c /nologo /O2 /W3 /GL /DNDEBUG /MD -DWIN32=1 -IC:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-81fae27ee7dd-compat-cb6a104a6688-bm-gevent_hub\include -IC:\actions-runner\_work\benchmarking\benchmarking\cpython\include -IC:\actions-runner\_work\benchmarking\benchmarking\cpython\PCBuild\amd64 -IC:\actions-runner\_work\benchmarking\benchmarking\cpython\PCBuild\amd64 "-IC:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.42.34433\include" "-IC:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\VS\include" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.22621.0\ucrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\um" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\shared" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\winrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\cppwinrt" /EHsc /Tpsrc/greenlet/greenlet.cpp /Fobuild\temp.win-amd64-cpython-314\Release\src\greenlet\greenlet.obj /EHsr /GT /std:c++20
    greenlet.cpp
    C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(196): error C4576: a parenthesized type followed by an initializer list is a non-standard explicit type conversion syntax
    C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(378): error C4576: a parenthesized type followed by an initializer list is a non-standard explicit type conversion syntax
    C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(379): error C4576: a parenthesized type followed by an initializer list is a non-standard explicit type conversion syntax
    error: command 'C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\VC\\Tools\\MSVC\\14.42.34433\\bin\\HostX86\\x64\\cl.exe' failed with exit code 2
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

## gevent_hub on linux-x86_64 default

<details>
<summary>Log for gevent_hub on linux-x86_64 default</summary>

```
    import gevent
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688/lib/python3.14/site-packages/gevent/__init__.py", line 71, in <module>
    from gevent._config import config
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688/lib/python3.14/site-packages/gevent/_config.py", line 730, in <module>
    Loop().get()
    ~~~~~~~~~~^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688/lib/python3.14/site-packages/gevent/_config.py", line 151, in get
    self.value = self.validate(self._default())
                 ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688/lib/python3.14/site-packages/gevent/_config.py", line 259, in validate
    return self._import_one_of([self.shortname_map.get(x, x) for x in value])
           ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688/lib/python3.14/site-packages/gevent/_config.py", line 230, in _import_one_of
    return self._import_one(item)
           ~~~~~~~~~~~~~~~~^^^^^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688/lib/python3.14/site-packages/gevent/_config.py", line 248, in _import_one
    module = importlib.import_module(module)
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/cpython/Lib/importlib/__init__.py", line 88, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "src/gevent/libev/corecext.pyx", line 819, in init gevent.libev.corecext
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/__init__.py", line 58, in <module>
    _wire()
    ~~~~~^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 1154, in _wire
    from zope.interface.interfaces import IElement
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interfaces.py", line 56, in <module>
    class IElement(Interface):
    ...<93 lines>...
            """
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 794, in __init__
    self.__attrs = self.__compute_attrs(attrs)
                   ~~~~~~~~~~~~~~~~~~~~^^^^^^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 813, in __compute_attrs
    aname: update_value(aname, aval)
           ~~~~~~~~~~~~^^^^^^^^^^^^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688/lib/python3.14/site-packages/zope/interface/interface.py", line 809, in update_value
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
    "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.42.34433\bin\HostX86\x86\cl.exe" /c /nologo /O2 /W3 /GL /DNDEBUG /MD -DWIN32=1 -IC:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-89a32d3d62d8-compat-cb6a104a6688-bm-gevent_hub\include -IC:\actions-runner\_work\benchmarking\benchmarking\cpython\include -IC:\actions-runner\_work\benchmarking\benchmarking\cpython\PCBuild\win32 -IC:\actions-runner\_work\benchmarking\benchmarking\cpython\PCBuild\win32 "-IC:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.42.34433\include" "-IC:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\VS\include" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.22621.0\ucrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\um" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\shared" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\winrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\cppwinrt" /EHsc /Tpsrc/greenlet/greenlet.cpp /Fobuild\temp.win32-cpython-314\Release\src\greenlet\greenlet.obj /EHsr /GT /std:c++20
    greenlet.cpp
    C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(196): error C4576: a parenthesized type followed by an initializer list is a non-standard explicit type conversion syntax
    C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(378): error C4576: a parenthesized type followed by an initializer list is a non-standard explicit type conversion syntax
    C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(379): error C4576: a parenthesized type followed by an initializer list is a non-standard explicit type conversion syntax
    error: command 'C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\VC\\Tools\\MSVC\\14.42.34433\\bin\\HostX86\\x86\\cl.exe' failed with exit code 2
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

## gunicorn on collect-stats pystats

<details>
<summary>Log for gunicorn on collect-stats pystats</summary>

```
# /home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0d57dd0c23e2-compat-cb6a104a6688/bin/python -u /home/mdboom/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_gunicorn/run_benchmark.py --inherit-environ PYTHON_JIT,PYPERFORMANCE_RUNID --hook=pystats --loops=128 --output /tmp/tmpjqie0phc
Traceback (most recent call last):
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_gunicorn/run_benchmark.py", line 84, in <module>
    with context:
         ^^^^^^^
Command failed with exit code 1

ERROR: No benchmark was run
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/cpython/Lib/contextlib.py", line 141, in __enter__
    return next(self.gen)
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_gunicorn/netutils.py", line 36, in serving
    waitUntilUp(addr)
    ~~~~~~~~~~~^^^^^^
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_gunicorn/netutils.py", line 66, in waitUntilUp
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
Python benchmark suite 1.11.0


==================================================
```

</details>

## gunicorn on linux-aarch64 default

<details>
<summary>Log for gunicorn on linux-aarch64 default</summary>

```
# /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688/bin/python -u /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_gunicorn/run_benchmark.py --inherit-environ PYPERFORMANCE_RUNID,PYTHON_JIT --output /tmp/tmp4ygeg6p7
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

## gunicorn on darwin-arm64 default

<details>
<summary>Log for gunicorn on darwin-arm64 default</summary>

```
# /Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688/bin/python -u /Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_gunicorn/run_benchmark.py --inherit-environ PYPERFORMANCE_RUNID,PYTHON_JIT --output /tmp/tmpgsybsifn
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
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.13/site-packages/pyperformance/run.py", line 170, in run_benchmarks
    result = bench.run(
        bench_venv.python,
    ...<3 lines>...
        verbose=options.verbose,
    )
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.13/site-packages/pyperformance/_benchmark.py", line 189, in run
    bench = _run_perf_script(
        python,
    ...<4 lines>...
        verbose=verbose,
    )
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.13/site-packages/pyperformance/_benchmark.py", line 240, in _run_perf_script
    raise RuntimeError("Benchmark died")
RuntimeError: Benchmark died
Command failed with exit code 1
```

</details>

## gunicorn on windows-x86_64 default

<details>
<summary>Log for gunicorn on windows-x86_64 default</summary>

```
# 'C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-81fae27ee7dd-compat-cb6a104a6688\Scripts\python.exe' -u 'C:\actions-runner\_work\benchmarking\benchmarking\pyston-benchmarks\benchmarks\bm_gunicorn\run_benchmark.py' --inherit-environ PYPERFORMANCE_RUNID,PYTHON_JIT --output 'C:\WINDOWS\SERVIC~1\NETWOR~1\AppData\Local\Temp\tmpkii39q5t'
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

## gunicorn on linux-x86_64 default

<details>
<summary>Log for gunicorn on linux-x86_64 default</summary>

```
# /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688/bin/python -u /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_gunicorn/run_benchmark.py --inherit-environ PYPERFORMANCE_RUNID,PYTHON_JIT --output /tmp/tmpkwg95i65
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
##[error]    raise Exception('Timeout reached when trying to connect')
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

## gunicorn on windows-x86 default

<details>
<summary>Log for gunicorn on windows-x86 default</summary>

```
# 'C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-89a32d3d62d8-compat-cb6a104a6688\Scripts\python.exe' -u 'C:\actions-runner\_work\benchmarking\benchmarking\pyston-benchmarks\benchmarks\bm_gunicorn\run_benchmark.py' --inherit-environ PYTHON_JIT,PYPERFORMANCE_RUNID --output 'C:\WINDOWS\SERVIC~1\NETWOR~1\AppData\Local\Temp\tmpho7tmy4y'
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

## kinto on collect-stats pystats

<details>
<summary>Log for kinto on collect-stats pystats</summary>

```
# /home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0d57dd0c23e2-compat-cb6a104a6688/bin/python -u /home/mdboom/actions-runner/_work/benchmarking/benchmarking/pyston-benchmarks/benchmarks/bm_kinto/run_benchmark.py --inherit-environ PYPERFORMANCE_RUNID,PYTHON_JIT --hook=pystats --output /tmp/tmpvxhhhu1e
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

## kinto on linux-aarch64 default

<details>
<summary>Log for kinto on linux-aarch64 default</summary>

```
      [thread 14][gcc] plugins/http/spdy3.o
      [thread 39][gcc] plugins/ugreen/ugreen.o
      [thread 70][gcc] plugins/signal/signal_plugin.o
      [thread 71][gcc] plugins/syslog/syslog_plugin.o
      [thread 54][gcc] plugins/rsyslog/rsyslog_plugin.o
      [thread 57][gcc] plugins/logsocket/logsocket_plugin.o
      [thread 33][gcc] plugins/router_uwsgi/router_uwsgi.o
      [thread 73][gcc] plugins/router_redirect/router_redirect.o
      [thread 51][gcc] plugins/router_basicauth/router_basicauth.o
      [thread 16][gcc] plugins/zergpool/zergpool.o
      [thread 32][gcc] plugins/redislog/redislog_plugin.o
      [thread 65][gcc] plugins/mongodblog/mongodblog_plugin.o
      [thread 64][gcc] plugins/router_rewrite/router_rewrite.o
      [thread 29][gcc] plugins/router_http/router_http.o
      [thread 0][gcc] plugins/logfile/logfile.o
      [thread 22][gcc] plugins/router_cache/router_cache.o
      [thread 40][gcc] plugins/rawrouter/rawrouter.o
      [thread 24][gcc] plugins/router_static/router_static.o
      [thread 19][gcc] plugins/sslrouter/sslrouter.o
      [thread 18][gcc] plugins/spooler/spooler_plugin.o
      [thread 34][gcc] plugins/cheaper_busyness/cheaper_busyness.o
      [thread 9][gcc] plugins/symcall/symcall_plugin.o
      [thread 63][gcc] plugins/transformation_tofile/tofile.o
      [thread 45][gcc] plugins/transformation_gzip/gzip.o
      [thread 74][gcc] plugins/transformation_chunked/chunked.o
      [thread 15][gcc] plugins/transformation_offload/offload.o
      [thread 46][gcc] plugins/router_memcached/router_memcached.o
      [thread 11][gcc] plugins/router_redis/router_redis.o
      [thread 28][gcc] plugins/router_hash/router_hash.o
      [thread 17][gcc] plugins/router_expires/expires.o
      [thread 72][gcc] plugins/router_metrics/plugin.o
      [thread 77][gcc] plugins/transformation_template/tt.o
      [thread 38][gcc] plugins/stats_pusher_socket/plugin.o
      *** uWSGI linking ***
      gcc -o build/bdist.linux-aarch64/wheel/uWSGI-2.0.28.data/scripts/uwsgi -L/usr/local/lib -Wl,-rpath,/usr/local/lib core/utils.o core/protocol.o core/socket.o core/logging.o core/master.o core/master_utils.o core/emperor.o core/notify.o core/mule.o core/subscription.o core/stats.o core/sendfile.o core/async.o core/master_checks.o core/fifo.o core/offload.o core/io.o core/static.o core/websockets.o core/spooler.o core/snmp.o core/exceptions.o core/config.o core/setup_utils.o core/clock.o core/init.o core/buffer.o core/reader.o core/writer.o core/alarm.o core/cron.o core/hooks.o core/plugins.o core/lock.o core/cache.o core/daemons.o core/errors.o core/hash.o core/master_events.o core/chunked.o core/queue.o core/event.o core/signal.o core/strings.o core/progress.o core/timebomb.o core/ini.o core/fsmon.o core/mount.o core/metrics.o core/plugins_builder.o core/sharedarea.o core/rpc.o core/gateway.o core/loop.o core/cookie.o core/querystring.o core/rb_timers.o core/transformations.o core/uwsgi.o proto/base.o proto/uwsgi.o proto/http.o proto/fastcgi.o proto/scgi.o proto/puwsgi.o lib/linux_ns.o core/zlib.o core/yaml.o core/ssl.o core/legion.o core/xmlconf.o core/dot_h.o core/config_py.o plugins/python/python_plugin.o plugins/python/pyutils.o plugins/python/pyloader.o plugins/python/wsgi_handlers.o plugins/python/wsgi_headers.o plugins/python/wsgi_subhandler.o plugins/python/web3_subhandler.o plugins/python/pump_subhandler.o plugins/python/gil.o plugins/python/uwsgi_pymodule.o plugins/python/profiler.o plugins/python/symimporter.o plugins/python/tracebacker.o plugins/python/raw.o plugins/gevent/gevent.o plugins/gevent/hooks.o plugins/ping/ping_plugin.o plugins/cache/cache.o plugins/nagios/nagios.o plugins/rrdtool/rrdtool.o plugins/carbon/carbon.o plugins/rpc/rpc_plugin.o plugins/corerouter/cr_common.o plugins/corerouter/cr_map.o plugins/corerouter/corerouter.o plugins/fastrouter/fastrouter.o plugins/http/http.o plugins/http/keepalive.o plugins/http/https.o plugins/http/spdy3.o plugins/ugreen/ugreen.o plugins/signal/signal_plugin.o plugins/syslog/syslog_plugin.o plugins/rsyslog/rsyslog_plugin.o plugins/logsocket/logsocket_plugin.o plugins/router_uwsgi/router_uwsgi.o plugins/router_redirect/router_redirect.o plugins/router_basicauth/router_basicauth.o plugins/zergpool/zergpool.o plugins/redislog/redislog_plugin.o plugins/mongodblog/mongodblog_plugin.o plugins/router_rewrite/router_rewrite.o plugins/router_http/router_http.o plugins/logfile/logfile.o plugins/router_cache/router_cache.o plugins/rawrouter/rawrouter.o plugins/router_static/router_static.o plugins/sslrouter/sslrouter.o plugins/spooler/spooler_plugin.o plugins/cheaper_busyness/cheaper_busyness.o plugins/symcall/symcall_plugin.o plugins/transformation_tofile/tofile.o plugins/transformation_gzip/gzip.o plugins/transformation_chunked/chunked.o plugins/transformation_offload/offload.o plugins/router_memcached/router_memcached.o plugins/router_redis/router_redis.o plugins/router_hash/router_hash.o plugins/router_expires/expires.o plugins/router_metrics/plugin.o plugins/transformation_template/tt.o plugins/stats_pusher_socket/plugin.o -lpthread -lm -rdynamic -ldl -lz -luuid -lssl -lcrypto -lxml2 -ldl -lm -lpython3.14 -lcrypt
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

## kinto on darwin-arm64 default

<details>
<summary>Log for kinto on darwin-arm64 default</summary>

```
      [thread 6][clang] plugins/http/https.o
      [thread 5][clang] plugins/http/spdy3.o
      [thread 4][clang] plugins/signal/signal_plugin.o
      [thread 7][clang] plugins/syslog/syslog_plugin.o
      [thread 2][clang] plugins/rsyslog/rsyslog_plugin.o
      [thread 1][clang] plugins/logsocket/logsocket_plugin.o
      [thread 0][clang] plugins/router_uwsgi/router_uwsgi.o
      [thread 6][clang] plugins/router_redirect/router_redirect.o
      [thread 4][clang] plugins/router_basicauth/router_basicauth.o
      [thread 5][clang] plugins/zergpool/zergpool.o
      [thread 7][clang] plugins/redislog/redislog_plugin.o
      [thread 3][clang] plugins/mongodblog/mongodblog_plugin.o
      [thread 2][clang] plugins/router_rewrite/router_rewrite.o
      [thread 0][clang] plugins/router_http/router_http.o
      [thread 1][clang] plugins/logfile/logfile.o
      [thread 6][clang] plugins/router_cache/router_cache.o
      [thread 4][clang] plugins/rawrouter/rawrouter.o
      [thread 5][clang] plugins/router_static/router_static.o
      [thread 7][clang] plugins/sslrouter/sslrouter.o
      [thread 3][clang] plugins/spooler/spooler_plugin.o
      [thread 2][clang] plugins/cheaper_busyness/cheaper_busyness.o
      [thread 0][clang] plugins/symcall/symcall_plugin.o
      [thread 1][clang] plugins/transformation_tofile/tofile.o
      [thread 6][clang] plugins/transformation_gzip/gzip.o
      [thread 4][clang] plugins/transformation_chunked/chunked.o
      [thread 5][clang] plugins/transformation_offload/offload.o
      [thread 7][clang] plugins/router_memcached/router_memcached.o
      [thread 3][clang] plugins/router_redis/router_redis.o
      [thread 2][clang] plugins/router_hash/router_hash.o
      [thread 6][clang] plugins/router_expires/expires.o
      [thread 0][clang] plugins/router_metrics/plugin.o
      [thread 1][clang] plugins/transformation_template/tt.o
      [thread 5][clang] plugins/stats_pusher_socket/plugin.o
      *** uWSGI linking ***
      clang -o build/bdist.macosx-15.2-arm64/wheel/uWSGI-2.0.28.data/scripts/uwsgi -L/usr/local/lib -Wl,-rpath,/usr/local/lib core/utils.o core/protocol.o core/socket.o core/logging.o core/master.o core/master_utils.o core/emperor.o core/notify.o core/mule.o core/subscription.o core/stats.o core/sendfile.o core/async.o core/master_checks.o core/fifo.o core/offload.o core/io.o core/static.o core/websockets.o core/spooler.o core/snmp.o core/exceptions.o core/config.o core/setup_utils.o core/clock.o core/init.o core/buffer.o core/reader.o core/writer.o core/alarm.o core/cron.o core/hooks.o core/plugins.o core/lock.o core/cache.o core/daemons.o core/errors.o core/hash.o core/master_events.o core/chunked.o core/queue.o core/event.o core/signal.o core/strings.o core/progress.o core/timebomb.o core/ini.o core/fsmon.o core/mount.o core/metrics.o core/plugins_builder.o core/sharedarea.o core/rpc.o core/gateway.o core/loop.o core/cookie.o core/querystring.o core/rb_timers.o core/transformations.o core/uwsgi.o proto/base.o proto/uwsgi.o proto/http.o proto/fastcgi.o proto/scgi.o proto/puwsgi.o core/zlib.o core/yaml.o core/xmlconf.o core/dot_h.o core/config_py.o plugins/python/python_plugin.o plugins/python/pyutils.o plugins/python/pyloader.o plugins/python/wsgi_handlers.o plugins/python/wsgi_headers.o plugins/python/wsgi_subhandler.o plugins/python/web3_subhandler.o plugins/python/pump_subhandler.o plugins/python/gil.o plugins/python/uwsgi_pymodule.o plugins/python/profiler.o plugins/python/symimporter.o plugins/python/tracebacker.o plugins/python/raw.o plugins/gevent/gevent.o plugins/gevent/hooks.o plugins/ping/ping_plugin.o plugins/cache/cache.o plugins/nagios/nagios.o plugins/rrdtool/rrdtool.o plugins/carbon/carbon.o plugins/rpc/rpc_plugin.o plugins/corerouter/cr_common.o plugins/corerouter/cr_map.o plugins/corerouter/corerouter.o plugins/fastrouter/fastrouter.o plugins/http/http.o plugins/http/keepalive.o plugins/http/https.o plugins/http/spdy3.o plugins/signal/signal_plugin.o plugins/syslog/syslog_plugin.o plugins/rsyslog/rsyslog_plugin.o plugins/logsocket/logsocket_plugin.o plugins/router_uwsgi/router_uwsgi.o plugins/router_redirect/router_redirect.o plugins/router_basicauth/router_basicauth.o plugins/zergpool/zergpool.o plugins/redislog/redislog_plugin.o plugins/mongodblog/mongodblog_plugin.o plugins/router_rewrite/router_rewrite.o plugins/router_http/router_http.o plugins/logfile/logfile.o plugins/router_cache/router_cache.o plugins/rawrouter/rawrouter.o plugins/router_static/router_static.o plugins/sslrouter/sslrouter.o plugins/spooler/spooler_plugin.o plugins/cheaper_busyness/cheaper_busyness.o plugins/symcall/symcall_plugin.o plugins/transformation_tofile/tofile.o plugins/transformation_gzip/gzip.o plugins/transformation_chunked/chunked.o plugins/transformation_offload/offload.o plugins/router_memcached/router_memcached.o plugins/router_redis/router_redis.o plugins/router_hash/router_hash.o plugins/router_expires/expires.o plugins/router_metrics/plugin.o plugins/transformation_template/tt.o plugins/stats_pusher_socket/plugin.o -lpthread -lm -lz -lexpat -ldl -framework CoreFoundation -lpython3.14
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
      ''' % ('C:\\Windows\\ServiceProfiles\\NetworkService\\AppData\\Local\\Temp\\pip-install-svbq7_rf\\uwsgi_2693a8de5d364bd0b6334d0b9c8f7348\\setup.py',), "<pip-setuptools-caller>", "exec"))
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "<pip-setuptools-caller>", line 34, in <module>
    File "C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\pip-install-svbq7_rf\uwsgi_2693a8de5d364bd0b6334d0b9c8f7348\setup.py", line 3, in <module>
      import uwsgiconfig as uc
    File "C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\pip-install-svbq7_rf\uwsgi_2693a8de5d364bd0b6334d0b9c8f7348\uwsgiconfig.py", line 8, in <module>
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

## kinto on linux-x86_64 default

<details>
<summary>Log for kinto on linux-x86_64 default</summary>

```
      [thread 10][gcc -pthread] plugins/http/spdy3.o
      [thread 8][gcc -pthread] plugins/ugreen/ugreen.o
      [thread 5][gcc -pthread] plugins/signal/signal_plugin.o
      [thread 7][gcc -pthread] plugins/syslog/syslog_plugin.o
      [thread 0][gcc -pthread] plugins/rsyslog/rsyslog_plugin.o
      [thread 12][gcc -pthread] plugins/logsocket/logsocket_plugin.o
      [thread 4][gcc -pthread] plugins/router_uwsgi/router_uwsgi.o
      [thread 11][gcc -pthread] plugins/router_redirect/router_redirect.o
      [thread 18][gcc -pthread] plugins/router_basicauth/router_basicauth.o
      [thread 16][gcc -pthread] plugins/zergpool/zergpool.o
      [thread 1][gcc -pthread] plugins/redislog/redislog_plugin.o
      [thread 14][gcc -pthread] plugins/mongodblog/mongodblog_plugin.o
      [thread 19][gcc -pthread] plugins/router_rewrite/router_rewrite.o
      [thread 9][gcc -pthread] plugins/router_http/router_http.o
      [thread 8][gcc -pthread] plugins/logfile/logfile.o
      [thread 0][gcc -pthread] plugins/router_cache/router_cache.o
      [thread 5][gcc -pthread] plugins/rawrouter/rawrouter.o
      [thread 13][gcc -pthread] plugins/router_static/router_static.o
      [thread 12][gcc -pthread] plugins/sslrouter/sslrouter.o
      [thread 18][gcc -pthread] plugins/spooler/spooler_plugin.o
      [thread 4][gcc -pthread] plugins/cheaper_busyness/cheaper_busyness.o
      [thread 11][gcc -pthread] plugins/symcall/symcall_plugin.o
      [thread 7][gcc -pthread] plugins/transformation_tofile/tofile.o
      [thread 15][gcc -pthread] plugins/transformation_gzip/gzip.o
      [thread 2][gcc -pthread] plugins/transformation_chunked/chunked.o
      [thread 19][gcc -pthread] plugins/transformation_offload/offload.o
      [thread 10][gcc -pthread] plugins/router_memcached/router_memcached.o
      [thread 16][gcc -pthread] plugins/router_redis/router_redis.o
      [thread 9][gcc -pthread] plugins/router_hash/router_hash.o
      [thread 14][gcc -pthread] plugins/router_expires/expires.o
      [thread 1][gcc -pthread] plugins/router_metrics/plugin.o
      [thread 17][gcc -pthread] plugins/transformation_template/tt.o
      [thread 13][gcc -pthread] plugins/stats_pusher_socket/plugin.o
      *** uWSGI linking ***
      gcc -pthread -o build/bdist.linux-x86_64/wheel/uWSGI-2.0.28.data/scripts/uwsgi -L/usr/local/lib -Wl,-rpath,/usr/local/lib core/utils.o core/protocol.o core/socket.o core/logging.o core/master.o core/master_utils.o core/emperor.o core/notify.o core/mule.o core/subscription.o core/stats.o core/sendfile.o core/async.o core/master_checks.o core/fifo.o core/offload.o core/io.o core/static.o core/websockets.o core/spooler.o core/snmp.o core/exceptions.o core/config.o core/setup_utils.o core/clock.o core/init.o core/buffer.o core/reader.o core/writer.o core/alarm.o core/cron.o core/hooks.o core/plugins.o core/lock.o core/cache.o core/daemons.o core/errors.o core/hash.o core/master_events.o core/chunked.o core/queue.o core/event.o core/signal.o core/strings.o core/progress.o core/timebomb.o core/ini.o core/fsmon.o core/mount.o core/metrics.o core/plugins_builder.o core/sharedarea.o core/rpc.o core/gateway.o core/loop.o core/cookie.o core/querystring.o core/rb_timers.o core/transformations.o core/uwsgi.o proto/base.o proto/uwsgi.o proto/http.o proto/fastcgi.o proto/scgi.o proto/puwsgi.o lib/linux_ns.o core/zlib.o core/yaml.o core/ssl.o core/legion.o core/xmlconf.o core/dot_h.o core/config_py.o plugins/python/python_plugin.o plugins/python/pyutils.o plugins/python/pyloader.o plugins/python/wsgi_handlers.o plugins/python/wsgi_headers.o plugins/python/wsgi_subhandler.o plugins/python/web3_subhandler.o plugins/python/pump_subhandler.o plugins/python/gil.o plugins/python/uwsgi_pymodule.o plugins/python/profiler.o plugins/python/symimporter.o plugins/python/tracebacker.o plugins/python/raw.o plugins/gevent/gevent.o plugins/gevent/hooks.o plugins/ping/ping_plugin.o plugins/cache/cache.o plugins/nagios/nagios.o plugins/rrdtool/rrdtool.o plugins/carbon/carbon.o plugins/rpc/rpc_plugin.o plugins/corerouter/cr_common.o plugins/corerouter/cr_map.o plugins/corerouter/corerouter.o plugins/fastrouter/fastrouter.o plugins/http/http.o plugins/http/keepalive.o plugins/http/https.o plugins/http/spdy3.o plugins/ugreen/ugreen.o plugins/signal/signal_plugin.o plugins/syslog/syslog_plugin.o plugins/rsyslog/rsyslog_plugin.o plugins/logsocket/logsocket_plugin.o plugins/router_uwsgi/router_uwsgi.o plugins/router_redirect/router_redirect.o plugins/router_basicauth/router_basicauth.o plugins/zergpool/zergpool.o plugins/redislog/redislog_plugin.o plugins/mongodblog/mongodblog_plugin.o plugins/router_rewrite/router_rewrite.o plugins/router_http/router_http.o plugins/logfile/logfile.o plugins/router_cache/router_cache.o plugins/rawrouter/rawrouter.o plugins/router_static/router_static.o plugins/sslrouter/sslrouter.o plugins/spooler/spooler_plugin.o plugins/cheaper_busyness/cheaper_busyness.o plugins/symcall/symcall_plugin.o plugins/transformation_tofile/tofile.o plugins/transformation_gzip/gzip.o plugins/transformation_chunked/chunked.o plugins/transformation_offload/offload.o plugins/router_memcached/router_memcached.o plugins/router_redis/router_redis.o plugins/router_hash/router_hash.o plugins/router_expires/expires.o plugins/router_metrics/plugin.o plugins/transformation_template/tt.o plugins/stats_pusher_socket/plugin.o -lpthread -lm -rdynamic -ldl -lz -luuid -lssl -lcrypto -lxml2 -lpthread -ldl -lutil -lm -lpython3.14 -lcrypt
      /usr/bin/ld: cannot find -lpython3.14
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
      ''' % ('C:\\Windows\\ServiceProfiles\\NetworkService\\AppData\\Local\\Temp\\pip-install-qfzk8xhs\\uwsgi_0e4d87f4b8904d96aa9afa953cfd19e3\\setup.py',), "<pip-setuptools-caller>", "exec"))
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "<pip-setuptools-caller>", line 34, in <module>
    File "C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\pip-install-qfzk8xhs\uwsgi_0e4d87f4b8904d96aa9afa953cfd19e3\setup.py", line 3, in <module>
      import uwsgiconfig as uc
    File "C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\pip-install-qfzk8xhs\uwsgi_0e4d87f4b8904d96aa9afa953cfd19e3\uwsgiconfig.py", line 8, in <module>
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

## mypy2 on collect-stats pystats

<details>
<summary>Log for mypy2 on collect-stats pystats</summary>

```

ERROR: ResolutionImpossible: for help visit https://pip.pypa.io/en/latest/topics/dependency-resolution/#dealing-with-dependency-conflicts
Command failed with exit code 1
(falling back to unique venv)
Creating the virtual environment /home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0d57dd0c23e2-compat-cb6a104a6688-bm-mypy2
# /home/mdboom/actions-runner/_work/benchmarking/benchmarking/cpython/python -m venv --without-pip /home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0d57dd0c23e2-compat-cb6a104a6688-bm-mypy2
# /home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0d57dd0c23e2-compat-cb6a104a6688-bm-mypy2/bin/python -m ensurepip -v -U
Using pip 24.3.1 from /tmp/tmpytu775yr/pip-24.3.1-py3-none-any.whl/pip (python 3.14)
Looking in links: /tmp/tmpytu775yr
Processing /tmp/tmpytu775yr/pip-24.3.1-py3-none-any.whl
Installing collected packages: pip
  changing mode of /home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0d57dd0c23e2-compat-cb6a104a6688-bm-mypy2/bin/pip3 to 755
  changing mode of /home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0d57dd0c23e2-compat-cb6a104a6688-bm-mypy2/bin/pip3.14 to 755
Successfully installed pip-24.3.1
# /home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0d57dd0c23e2-compat-cb6a104a6688-bm-mypy2/bin/python -m pip install -U 'setuptools>=18.5' wheel
Collecting setuptools>=18.5
  Using cached setuptools-75.8.0-py3-none-any.whl.metadata (6.7 kB)
Collecting wheel
  Using cached wheel-0.45.1-py3-none-any.whl.metadata (2.3 kB)
Using cached setuptools-75.8.0-py3-none-any.whl (1.2 MB)
Using cached wheel-0.45.1-py3-none-any.whl (72 kB)
Installing collected packages: wheel, setuptools
Successfully installed setuptools-75.8.0 wheel-0.45.1
# /home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0d57dd0c23e2-compat-cb6a104a6688-bm-mypy2/bin/python -m pip --version
pip 24.3.1 from /home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0d57dd0c23e2-compat-cb6a104a6688-bm-mypy2/lib/python3.14/site-packages/pip (python 3.14)
Installing requirements into the virtual environment /home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0d57dd0c23e2-compat-cb6a104a6688-bm-mypy2
# /home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0d57dd0c23e2-compat-cb6a104a6688-bm-mypy2/bin/python -m pip install --no-binary=mypy mypy==1.13.0 mypy-extensions==1.0.0 typing-extensions==4.2.0 pyperf==2.8.1
Collecting mypy==1.13.0
  Using cached mypy-1.13.0-py3-none-any.whl
Collecting mypy-extensions==1.0.0
  Using cached mypy_extensions-1.0.0-py3-none-any.whl.metadata (1.1 kB)
Collecting typing-extensions==4.2.0
  Using cached typing_extensions-4.2.0-py3-none-any.whl.metadata (6.2 kB)
Collecting pyperf==2.8.1
  Using cached pyperf-2.8.1-py3-none-any.whl.metadata (5.9 kB)
INFO: pip is looking at multiple versions of mypy to determine which version is compatible with other requirements. This could take a while.
ERROR: Cannot install mypy==1.13.0 and typing-extensions==4.2.0 because these package versions have conflicting dependencies.

The conflict is caused by:
    The user requested typing-extensions==4.2.0
    mypy 1.13.0 depends on typing_extensions>=4.6.0

To fix this you could try to:
1. loosen the range of package versions you've specified
2. remove package versions to allow pip to attempt to solve the dependency conflict

ERROR: ResolutionImpossible: for help visit https://pip.pypa.io/en/latest/topics/dependency-resolution/#dealing-with-dependency-conflicts
Command failed with exit code 1


```

</details>

## mypy2 on linux-aarch64 default

<details>
<summary>Log for mypy2 on linux-aarch64 default</summary>

```

Command failed with exit code 1
(falling back to unique venv)
Creating the virtual environment /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688-bm-mypy2
# /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/cpython/python -m venv --without-pip /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688-bm-mypy2
# /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688-bm-mypy2/bin/python -m ensurepip -v -U
Using pip 24.3.1 from /tmp/tmpvsnp9yps/pip-24.3.1-py3-none-any.whl/pip (python 3.14)
Looking in links: /tmp/tmpvsnp9yps
Processing /tmp/tmpvsnp9yps/pip-24.3.1-py3-none-any.whl
Installing collected packages: pip
  changing mode of /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688-bm-mypy2/bin/pip3 to 755
  changing mode of /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688-bm-mypy2/bin/pip3.14 to 755
Successfully installed pip-24.3.1
# /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688-bm-mypy2/bin/python -m pip install -U 'setuptools>=18.5' wheel
Collecting setuptools>=18.5
  Using cached setuptools-75.8.0-py3-none-any.whl.metadata (6.7 kB)
Collecting wheel
  Using cached wheel-0.45.1-py3-none-any.whl.metadata (2.3 kB)
Using cached setuptools-75.8.0-py3-none-any.whl (1.2 MB)
Using cached wheel-0.45.1-py3-none-any.whl (72 kB)
Installing collected packages: wheel, setuptools
Successfully installed setuptools-75.8.0 wheel-0.45.1
# /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688-bm-mypy2/bin/python -m pip --version
pip 24.3.1 from /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688-bm-mypy2/lib/python3.14/site-packages/pip (python 3.14)
Installing requirements into the virtual environment /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688-bm-mypy2
# /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688-bm-mypy2/bin/python -m pip install --no-binary=mypy mypy==1.13.0 mypy-extensions==1.0.0 typing-extensions==4.2.0 pyperf==2.8.1
Collecting mypy==1.13.0
  Using cached mypy-1.13.0-py3-none-any.whl
Collecting mypy-extensions==1.0.0
  Using cached mypy_extensions-1.0.0-py3-none-any.whl.metadata (1.1 kB)
Collecting typing-extensions==4.2.0
  Using cached typing_extensions-4.2.0-py3-none-any.whl.metadata (6.2 kB)
Collecting pyperf==2.8.1
  Using cached pyperf-2.8.1-py3-none-any.whl.metadata (5.9 kB)
INFO: pip is looking at multiple versions of mypy to determine which version is compatible with other requirements. This could take a while.
ERROR: Cannot install mypy==1.13.0 and typing-extensions==4.2.0 because these package versions have conflicting dependencies.

The conflict is caused by:
    The user requested typing-extensions==4.2.0
    mypy 1.13.0 depends on typing_extensions>=4.6.0

To fix this you could try to:
1. loosen the range of package versions you've specified
2. remove package versions to allow pip to attempt to solve the dependency conflict

ERROR: ResolutionImpossible: for help visit https://pip.pypa.io/en/latest/topics/dependency-resolution/#dealing-with-dependency-conflicts
Command failed with exit code 1


==================================================
```

</details>

## mypy2 on darwin-arm64 default

<details>
<summary>Log for mypy2 on darwin-arm64 default</summary>

```
ERROR: ResolutionImpossible: for help visit https://pip.pypa.io/en/latest/topics/dependency-resolution/#dealing-with-dependency-conflicts
Command failed with exit code 1
(falling back to unique venv)
Creating the virtual environment /Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688-bm-mypy2
# /Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/cpython/python.exe -m venv --without-pip /Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688-bm-mypy2
# /Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688-bm-mypy2/bin/python -m ensurepip -v -U
Using pip 24.3.1 from /tmp/tmpn_ennhc7/pip-24.3.1-py3-none-any.whl/pip (python 3.14)
Looking in links: /tmp/tmpn_ennhc7
Processing /tmp/tmpn_ennhc7/pip-24.3.1-py3-none-any.whl
Installing collected packages: pip
  changing mode of /Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688-bm-mypy2/bin/pip3 to 755
  changing mode of /Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688-bm-mypy2/bin/pip3.14 to 755
Successfully installed pip-24.3.1
# /Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688-bm-mypy2/bin/python -m pip install -U 'setuptools>=18.5' wheel
Collecting setuptools>=18.5
  Using cached setuptools-75.8.0-py3-none-any.whl.metadata (6.7 kB)
Collecting wheel
  Using cached wheel-0.45.1-py3-none-any.whl.metadata (2.3 kB)
Using cached setuptools-75.8.0-py3-none-any.whl (1.2 MB)
Using cached wheel-0.45.1-py3-none-any.whl (72 kB)
Installing collected packages: wheel, setuptools
Successfully installed setuptools-75.8.0 wheel-0.45.1
# /Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688-bm-mypy2/bin/python -m pip --version
pip 24.3.1 from /Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688-bm-mypy2/lib/python3.14/site-packages/pip (python 3.14)
Installing requirements into the virtual environment /Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688-bm-mypy2
# /Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688-bm-mypy2/bin/python -m pip install --no-binary=mypy mypy==1.13.0 mypy-extensions==1.0.0 typing-extensions==4.2.0 pyperf==2.8.1
Collecting mypy==1.13.0
  Using cached mypy-1.13.0-py3-none-any.whl
Collecting mypy-extensions==1.0.0
  Using cached mypy_extensions-1.0.0-py3-none-any.whl.metadata (1.1 kB)
Collecting typing-extensions==4.2.0
  Using cached typing_extensions-4.2.0-py3-none-any.whl.metadata (6.2 kB)
Collecting pyperf==2.8.1
  Using cached pyperf-2.8.1-py3-none-any.whl.metadata (5.9 kB)
INFO: pip is looking at multiple versions of mypy to determine which version is compatible with other requirements. This could take a while.
ERROR: Cannot install mypy==1.13.0 and typing-extensions==4.2.0 because these package versions have conflicting dependencies.

The conflict is caused by:
    The user requested typing-extensions==4.2.0
    mypy 1.13.0 depends on typing_extensions>=4.6.0

To fix this you could try to:
1. loosen the range of package versions you've specified
2. remove package versions to allow pip to attempt to solve the dependency conflict

ERROR: ResolutionImpossible: for help visit https://pip.pypa.io/en/latest/topics/dependency-resolution/#dealing-with-dependency-conflicts
Command failed with exit code 1


==================================================
```

</details>

## mypy2 on windows-x86_64 default

<details>
<summary>Log for mypy2 on windows-x86_64 default</summary>

```

ERROR: ResolutionImpossible: for help visit https://pip.pypa.io/en/latest/topics/dependency-resolution/#dealing-with-dependency-conflicts
Command failed with exit code 1
(falling back to unique venv)
Creating the virtual environment C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-81fae27ee7dd-compat-cb6a104a6688-bm-mypy2
# 'C:\actions-runner\_work\benchmarking\benchmarking\cpython\PCBuild\amd64\python.exe' -m venv --without-pip 'C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-81fae27ee7dd-compat-cb6a104a6688-bm-mypy2'
# 'C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-81fae27ee7dd-compat-cb6a104a6688-bm-mypy2\Scripts\python.exe' -m ensurepip -v -U
Using pip 24.3.1 from C:\WINDOWS\SERVIC~1\NETWOR~1\AppData\Local\Temp\tmpzqh6kzpm\pip-24.3.1-py3-none-any.whl\pip (python 3.14)
Looking in links: c:\WINDOWS\SERVIC~1\NETWOR~1\AppData\Local\Temp\tmpzqh6kzpm
Processing c:\windows\servic~1\networ~1\appdata\local\temp\tmpzqh6kzpm\pip-24.3.1-py3-none-any.whl
Installing collected packages: pip
Successfully installed pip-24.3.1
# 'C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-81fae27ee7dd-compat-cb6a104a6688-bm-mypy2\Scripts\python.exe' -m pip install -U 'setuptools>=18.5' wheel
Collecting setuptools>=18.5
  Using cached setuptools-75.8.0-py3-none-any.whl.metadata (6.7 kB)
Collecting wheel
  Using cached wheel-0.45.1-py3-none-any.whl.metadata (2.3 kB)
Using cached setuptools-75.8.0-py3-none-any.whl (1.2 MB)
Using cached wheel-0.45.1-py3-none-any.whl (72 kB)
Installing collected packages: wheel, setuptools
Successfully installed setuptools-75.8.0 wheel-0.45.1
# 'C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-81fae27ee7dd-compat-cb6a104a6688-bm-mypy2\Scripts\python.exe' -m pip --version
pip 24.3.1 from C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-81fae27ee7dd-compat-cb6a104a6688-bm-mypy2\Lib\site-packages\pip (python 3.14)

Installing requirements into the virtual environment C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-81fae27ee7dd-compat-cb6a104a6688-bm-mypy2
# 'C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-81fae27ee7dd-compat-cb6a104a6688-bm-mypy2\Scripts\python.exe' -m pip install --no-binary=mypy mypy==1.13.0 mypy-extensions==1.0.0 typing-extensions==4.2.0 pyperf==2.8.1
Collecting mypy==1.13.0
  Using cached mypy-1.13.0-py3-none-any.whl
Collecting mypy-extensions==1.0.0
  Using cached mypy_extensions-1.0.0-py3-none-any.whl.metadata (1.1 kB)
Collecting typing-extensions==4.2.0
  Using cached typing_extensions-4.2.0-py3-none-any.whl.metadata (6.2 kB)
Collecting pyperf==2.8.1
  Using cached pyperf-2.8.1-py3-none-any.whl.metadata (5.9 kB)
INFO: pip is looking at multiple versions of mypy to determine which version is compatible with other requirements. This could take a while.
ERROR: Cannot install mypy==1.13.0 and typing-extensions==4.2.0 because these package versions have conflicting dependencies.

The conflict is caused by:
    The user requested typing-extensions==4.2.0
    mypy 1.13.0 depends on typing_extensions>=4.6.0

To fix this you could try to:
1. loosen the range of package versions you've specified
2. remove package versions to allow pip to attempt to solve the dependency conflict

ERROR: ResolutionImpossible: for help visit https://pip.pypa.io/en/latest/topics/dependency-resolution/#dealing-with-dependency-conflicts
Command failed with exit code 1


==================================================
```

</details>

## mypy2 on linux-x86_64 default

<details>
<summary>Log for mypy2 on linux-x86_64 default</summary>

```
ERROR: ResolutionImpossible: for help visit https://pip.pypa.io/en/latest/topics/dependency-resolution/#dealing-with-dependency-conflicts
Command failed with exit code 1
(falling back to unique venv)
Creating the virtual environment /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688-bm-mypy2
# /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/cpython/python -m venv --without-pip /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688-bm-mypy2
# /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688-bm-mypy2/bin/python -m ensurepip -v -U
Using pip 24.3.1 from /tmp/tmp5lh1iqb8/pip-24.3.1-py3-none-any.whl/pip (python 3.14)
Looking in links: /tmp/tmp5lh1iqb8
Processing /tmp/tmp5lh1iqb8/pip-24.3.1-py3-none-any.whl
Installing collected packages: pip
  changing mode of /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688-bm-mypy2/bin/pip3 to 755
  changing mode of /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688-bm-mypy2/bin/pip3.14 to 755
Successfully installed pip-24.3.1
# /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688-bm-mypy2/bin/python -m pip install -U 'setuptools>=18.5' wheel
Collecting setuptools>=18.5
  Using cached setuptools-75.8.0-py3-none-any.whl.metadata (6.7 kB)
Collecting wheel
  Using cached wheel-0.45.1-py3-none-any.whl.metadata (2.3 kB)
Using cached setuptools-75.8.0-py3-none-any.whl (1.2 MB)
Using cached wheel-0.45.1-py3-none-any.whl (72 kB)
Installing collected packages: wheel, setuptools
Successfully installed setuptools-75.8.0 wheel-0.45.1
# /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688-bm-mypy2/bin/python -m pip --version
pip 24.3.1 from /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688-bm-mypy2/lib/python3.14/site-packages/pip (python 3.14)
Installing requirements into the virtual environment /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688-bm-mypy2
# /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688-bm-mypy2/bin/python -m pip install --no-binary=mypy mypy==1.13.0 mypy-extensions==1.0.0 typing-extensions==4.2.0 pyperf==2.8.1
Collecting mypy==1.13.0
  Using cached mypy-1.13.0-py3-none-any.whl
Collecting mypy-extensions==1.0.0
  Using cached mypy_extensions-1.0.0-py3-none-any.whl.metadata (1.1 kB)
Collecting typing-extensions==4.2.0
  Using cached typing_extensions-4.2.0-py3-none-any.whl.metadata (6.2 kB)
Collecting pyperf==2.8.1
  Using cached pyperf-2.8.1-py3-none-any.whl.metadata (5.9 kB)
INFO: pip is looking at multiple versions of mypy to determine which version is compatible with other requirements. This could take a while.
ERROR: Cannot install mypy==1.13.0 and typing-extensions==4.2.0 because these package versions have conflicting dependencies.

The conflict is caused by:
    The user requested typing-extensions==4.2.0
    mypy 1.13.0 depends on typing_extensions>=4.6.0

To fix this you could try to:
1. loosen the range of package versions you've specified
2. remove package versions to allow pip to attempt to solve the dependency conflict

ERROR: ResolutionImpossible: for help visit https://pip.pypa.io/en/latest/topics/dependency-resolution/#dealing-with-dependency-conflicts
Command failed with exit code 1


==================================================
```

</details>

## mypy2 on windows-x86 default

<details>
<summary>Log for mypy2 on windows-x86 default</summary>

```

ERROR: ResolutionImpossible: for help visit https://pip.pypa.io/en/latest/topics/dependency-resolution/#dealing-with-dependency-conflicts
Command failed with exit code 1
(falling back to unique venv)
Creating the virtual environment C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-89a32d3d62d8-compat-cb6a104a6688-bm-mypy2
# 'C:\actions-runner\_work\benchmarking\benchmarking\cpython\PCBuild\win32\python.exe' -m venv --without-pip 'C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-89a32d3d62d8-compat-cb6a104a6688-bm-mypy2'
# 'C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-89a32d3d62d8-compat-cb6a104a6688-bm-mypy2\Scripts\python.exe' -m ensurepip -v -U
Using pip 24.3.1 from C:\WINDOWS\SERVIC~1\NETWOR~1\AppData\Local\Temp\tmpzippb37g\pip-24.3.1-py3-none-any.whl\pip (python 3.14)
Looking in links: c:\WINDOWS\SERVIC~1\NETWOR~1\AppData\Local\Temp\tmpzippb37g
Processing c:\windows\servic~1\networ~1\appdata\local\temp\tmpzippb37g\pip-24.3.1-py3-none-any.whl
Installing collected packages: pip
Successfully installed pip-24.3.1
# 'C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-89a32d3d62d8-compat-cb6a104a6688-bm-mypy2\Scripts\python.exe' -m pip install -U 'setuptools>=18.5' wheel
Collecting setuptools>=18.5
  Using cached setuptools-75.8.0-py3-none-any.whl.metadata (6.7 kB)
Collecting wheel
  Using cached wheel-0.45.1-py3-none-any.whl.metadata (2.3 kB)
Using cached setuptools-75.8.0-py3-none-any.whl (1.2 MB)
Using cached wheel-0.45.1-py3-none-any.whl (72 kB)
Installing collected packages: wheel, setuptools
Successfully installed setuptools-75.8.0 wheel-0.45.1
# 'C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-89a32d3d62d8-compat-cb6a104a6688-bm-mypy2\Scripts\python.exe' -m pip --version
pip 24.3.1 from C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-89a32d3d62d8-compat-cb6a104a6688-bm-mypy2\Lib\site-packages\pip (python 3.14)

Installing requirements into the virtual environment C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-89a32d3d62d8-compat-cb6a104a6688-bm-mypy2
# 'C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-89a32d3d62d8-compat-cb6a104a6688-bm-mypy2\Scripts\python.exe' -m pip install --no-binary=mypy mypy==1.13.0 mypy-extensions==1.0.0 typing-extensions==4.2.0 pyperf==2.8.1
Collecting mypy==1.13.0
  Using cached mypy-1.13.0-py3-none-any.whl
Collecting mypy-extensions==1.0.0
  Using cached mypy_extensions-1.0.0-py3-none-any.whl.metadata (1.1 kB)
Collecting typing-extensions==4.2.0
  Using cached typing_extensions-4.2.0-py3-none-any.whl.metadata (6.2 kB)
Collecting pyperf==2.8.1
  Using cached pyperf-2.8.1-py3-none-any.whl.metadata (5.9 kB)
INFO: pip is looking at multiple versions of mypy to determine which version is compatible with other requirements. This could take a while.
ERROR: Cannot install mypy==1.13.0 and typing-extensions==4.2.0 because these package versions have conflicting dependencies.

The conflict is caused by:
    The user requested typing-extensions==4.2.0
    mypy 1.13.0 depends on typing_extensions>=4.6.0

To fix this you could try to:
1. loosen the range of package versions you've specified
2. remove package versions to allow pip to attempt to solve the dependency conflict

ERROR: ResolutionImpossible: for help visit https://pip.pypa.io/en/latest/topics/dependency-resolution/#dealing-with-dependency-conflicts
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
        File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0d57dd0c23e2-compat-cb6a104a6688-bm-pytorch_alexnet_inference/lib/python3.14/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 353, in <module>
          main()
          ~~~~^^
        File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0d57dd0c23e2-compat-cb6a104a6688-bm-pytorch_alexnet_inference/lib/python3.14/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 335, in main
          json_out['return_val'] = hook(**hook_input['kwargs'])
                                   ~~~~^^^^^^^^^^^^^^^^^^^^^^^^
        File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0d57dd0c23e2-compat-cb6a104a6688-bm-pytorch_alexnet_inference/lib/python3.14/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 149, in prepare_metadata_for_build_wheel
          return hook(metadata_directory, config_settings)
        File "/tmp/pip-build-env-bbvzltwx/overlay/lib/python3.14/site-packages/setuptools/build_meta.py", line 377, in prepare_metadata_for_build_wheel
          self.run_setup()
          ~~~~~~~~~~~~~~^^
        File "/tmp/pip-build-env-bbvzltwx/overlay/lib/python3.14/site-packages/setuptools/build_meta.py", line 522, in run_setup
          super().run_setup(setup_script=setup_script)
          ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "/tmp/pip-build-env-bbvzltwx/overlay/lib/python3.14/site-packages/setuptools/build_meta.py", line 320, in run_setup
          exec(code, locals())
          ~~~~^^^^^^^^^^^^^^^^
        File "<string>", line 489, in <module>
        File "<string>", line 465, in setup_package
        File "/tmp/pip-install-uo8u1j5g/numpy_19f7df0510f0416781b058956751d1bd/numpy/distutils/core.py", line 24, in <module>
          from numpy.distutils.command import config, config_compiler, \
          ...<2 lines>...
               install_clib
        File "/tmp/pip-install-uo8u1j5g/numpy_19f7df0510f0416781b058956751d1bd/numpy/distutils/command/config.py", line 19, in <module>
          from numpy.distutils.mingw32ccompiler import generate_manifest
        File "/tmp/pip-install-uo8u1j5g/numpy_19f7df0510f0416781b058956751d1bd/numpy/distutils/mingw32ccompiler.py", line 28, in <module>
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
        File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688-bm-pytorch_alexnet_inference/lib/python3.14/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 353, in <module>
          main()
          ~~~~^^
        File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688-bm-pytorch_alexnet_inference/lib/python3.14/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 335, in main
          json_out['return_val'] = hook(**hook_input['kwargs'])
                                   ~~~~^^^^^^^^^^^^^^^^^^^^^^^^
        File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688-bm-pytorch_alexnet_inference/lib/python3.14/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 149, in prepare_metadata_for_build_wheel
          return hook(metadata_directory, config_settings)
        File "/tmp/pip-build-env-1_8setbv/overlay/lib/python3.14/site-packages/setuptools/build_meta.py", line 377, in prepare_metadata_for_build_wheel
          self.run_setup()
          ~~~~~~~~~~~~~~^^
        File "/tmp/pip-build-env-1_8setbv/overlay/lib/python3.14/site-packages/setuptools/build_meta.py", line 522, in run_setup
          super().run_setup(setup_script=setup_script)
          ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "/tmp/pip-build-env-1_8setbv/overlay/lib/python3.14/site-packages/setuptools/build_meta.py", line 320, in run_setup
          exec(code, locals())
          ~~~~^^^^^^^^^^^^^^^^
        File "<string>", line 489, in <module>
        File "<string>", line 465, in setup_package
        File "/tmp/pip-install-cnxqzcfb/numpy_07a511e217924cdf80fd65e84e553dfa/numpy/distutils/core.py", line 24, in <module>
          from numpy.distutils.command import config, config_compiler, \
          ...<2 lines>...
               install_clib
        File "/tmp/pip-install-cnxqzcfb/numpy_07a511e217924cdf80fd65e84e553dfa/numpy/distutils/command/config.py", line 19, in <module>
          from numpy.distutils.mingw32ccompiler import generate_manifest
        File "/tmp/pip-install-cnxqzcfb/numpy_07a511e217924cdf80fd65e84e553dfa/numpy/distutils/mingw32ccompiler.py", line 28, in <module>
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
        File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688-bm-pytorch_alexnet_inference/lib/python3.14/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 353, in <module>
          main()
          ~~~~^^
        File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688-bm-pytorch_alexnet_inference/lib/python3.14/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 335, in main
          json_out['return_val'] = hook(**hook_input['kwargs'])
                                   ~~~~^^^^^^^^^^^^^^^^^^^^^^^^
        File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688-bm-pytorch_alexnet_inference/lib/python3.14/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 149, in prepare_metadata_for_build_wheel
          return hook(metadata_directory, config_settings)
        File "/private/tmp/pip-build-env-iddtxuf3/overlay/lib/python3.14/site-packages/setuptools/build_meta.py", line 377, in prepare_metadata_for_build_wheel
          self.run_setup()
          ~~~~~~~~~~~~~~^^
        File "/private/tmp/pip-build-env-iddtxuf3/overlay/lib/python3.14/site-packages/setuptools/build_meta.py", line 522, in run_setup
          super().run_setup(setup_script=setup_script)
          ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "/private/tmp/pip-build-env-iddtxuf3/overlay/lib/python3.14/site-packages/setuptools/build_meta.py", line 320, in run_setup
          exec(code, locals())
          ~~~~^^^^^^^^^^^^^^^^
        File "<string>", line 489, in <module>
        File "<string>", line 465, in setup_package
        File "/private/tmp/pip-install-vx97ji5u/numpy_3a56f78c9cf548ccb3bef89455b43ec0/numpy/distutils/core.py", line 24, in <module>
          from numpy.distutils.command import config, config_compiler, \
          ...<2 lines>...
               install_clib
        File "/private/tmp/pip-install-vx97ji5u/numpy_3a56f78c9cf548ccb3bef89455b43ec0/numpy/distutils/command/config.py", line 19, in <module>
          from numpy.distutils.mingw32ccompiler import generate_manifest
        File "/private/tmp/pip-install-vx97ji5u/numpy_3a56f78c9cf548ccb3bef89455b43ec0/numpy/distutils/mingw32ccompiler.py", line 28, in <module>
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
    File "C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\pip-build-env-chtjqteu\overlay\Lib\site-packages\setuptools\build_meta.py", line 320, in run_setup
      exec(code, locals())
      ~~~~^^^^^^^^^^^^^^^^
    File "<string>", line 489, in <module>
    File "<string>", line 465, in setup_package
    File "C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\pip-install-ch1auhh4\numpy_7c5651b3780146a39174f59d9c09990c\numpy\distutils\core.py", line 24, in <module>
      from numpy.distutils.command import config, config_compiler, \
      ...<2 lines>...
           install_clib
    File "C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\pip-install-ch1auhh4\numpy_7c5651b3780146a39174f59d9c09990c\numpy\distutils\command\config.py", line 19, in <module>
      from numpy.distutils.mingw32ccompiler import generate_manifest
    File "C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\pip-install-ch1auhh4\numpy_7c5651b3780146a39174f59d9c09990c\numpy\distutils\mingw32ccompiler.py", line 28, in <module>
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
Creating the virtual environment C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-81fae27ee7dd-compat-cb6a104a6688-bm-pytorch_alexnet_inference
# 'C:\actions-runner\_work\benchmarking\benchmarking\cpython\PCBuild\amd64\python.exe' -m venv --without-pip 'C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-81fae27ee7dd-compat-cb6a104a6688-bm-pytorch_alexnet_inference'
# 'C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-81fae27ee7dd-compat-cb6a104a6688-bm-pytorch_alexnet_inference\Scripts\python.exe' -m ensurepip -v -U
Using pip 24.3.1 from C:\WINDOWS\SERVIC~1\NETWOR~1\AppData\Local\Temp\tmperl3mz8k\pip-24.3.1-py3-none-any.whl\pip (python 3.14)
Looking in links: c:\WINDOWS\SERVIC~1\NETWOR~1\AppData\Local\Temp\tmperl3mz8k
Processing c:\windows\servic~1\networ~1\appdata\local\temp\tmperl3mz8k\pip-24.3.1-py3-none-any.whl
Installing collected packages: pip
Successfully installed pip-24.3.1
# 'C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-81fae27ee7dd-compat-cb6a104a6688-bm-pytorch_alexnet_inference\Scripts\python.exe' -m pip install -U 'setuptools>=18.5' wheel
Collecting setuptools>=18.5
  Using cached setuptools-75.8.0-py3-none-any.whl.metadata (6.7 kB)
Collecting wheel
  Using cached wheel-0.45.1-py3-none-any.whl.metadata (2.3 kB)
Using cached setuptools-75.8.0-py3-none-any.whl (1.2 MB)
Using cached wheel-0.45.1-py3-none-any.whl (72 kB)
Installing collected packages: wheel, setuptools
ERROR: Could not install packages due to an OSError: [Errno 2] No such file or directory: 'C:\\actions-runner\\_work\\benchmarking\\benchmarking\\venv\\cpython3.14-81fae27ee7dd-compat-cb6a104a6688-bm-pytorch_alexnet_inference\\Lib\\site-packages\\pkg_resources\\tests\\data\\my-test-package_unpacked-egg\\my_test_package-1.0-py3.7.egg\\EGG-INFO\\dependency_links.txt'

Command failed with exit code 1
Remove directory C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-81fae27ee7dd-compat-cb6a104a6688-bm-pytorch_alexnet_inference


==================================================
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
        File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688-bm-pytorch_alexnet_inference/lib/python3.14/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 353, in <module>
          main()
          ~~~~^^
        File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688-bm-pytorch_alexnet_inference/lib/python3.14/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 335, in main
          json_out['return_val'] = hook(**hook_input['kwargs'])
                                   ~~~~^^^^^^^^^^^^^^^^^^^^^^^^
        File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688-bm-pytorch_alexnet_inference/lib/python3.14/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 149, in prepare_metadata_for_build_wheel
          return hook(metadata_directory, config_settings)
        File "/tmp/pip-build-env-vc5wo2ja/overlay/lib/python3.14/site-packages/setuptools/build_meta.py", line 377, in prepare_metadata_for_build_wheel
          self.run_setup()
          ~~~~~~~~~~~~~~^^
        File "/tmp/pip-build-env-vc5wo2ja/overlay/lib/python3.14/site-packages/setuptools/build_meta.py", line 522, in run_setup
          super().run_setup(setup_script=setup_script)
          ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "/tmp/pip-build-env-vc5wo2ja/overlay/lib/python3.14/site-packages/setuptools/build_meta.py", line 320, in run_setup
          exec(code, locals())
          ~~~~^^^^^^^^^^^^^^^^
        File "<string>", line 489, in <module>
        File "<string>", line 465, in setup_package
        File "/tmp/pip-install-aygz4o23/numpy_999fd35efb1846799c6ad9c53685ca8a/numpy/distutils/core.py", line 24, in <module>
          from numpy.distutils.command import config, config_compiler, \
          ...<2 lines>...
               install_clib
        File "/tmp/pip-install-aygz4o23/numpy_999fd35efb1846799c6ad9c53685ca8a/numpy/distutils/command/config.py", line 19, in <module>
          from numpy.distutils.mingw32ccompiler import generate_manifest
        File "/tmp/pip-install-aygz4o23/numpy_999fd35efb1846799c6ad9c53685ca8a/numpy/distutils/mingw32ccompiler.py", line 28, in <module>
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

## pytorch_alexnet_inference on windows-x86 default

<details>
<summary>Log for pytorch_alexnet_inference on windows-x86 default</summary>

```
    File "C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\pip-build-env-lu_2gm7t\overlay\Lib\site-packages\setuptools\build_meta.py", line 320, in run_setup
      exec(code, locals())
      ~~~~^^^^^^^^^^^^^^^^
    File "<string>", line 489, in <module>
    File "<string>", line 465, in setup_package
    File "C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\pip-install-bsvpzyco\numpy_b9e69894f4d745d9b8670918e1b91c04\numpy\distutils\core.py", line 24, in <module>
      from numpy.distutils.command import config, config_compiler, \
      ...<2 lines>...
           install_clib
    File "C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\pip-install-bsvpzyco\numpy_b9e69894f4d745d9b8670918e1b91c04\numpy\distutils\command\config.py", line 19, in <module>
      from numpy.distutils.mingw32ccompiler import generate_manifest
    File "C:\Windows\ServiceProfiles\NetworkService\AppData\Local\Temp\pip-install-bsvpzyco\numpy_b9e69894f4d745d9b8670918e1b91c04\numpy\distutils\mingw32ccompiler.py", line 28, in <module>
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
Creating the virtual environment C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-89a32d3d62d8-compat-cb6a104a6688-bm-pytorch_alexnet_inference
# 'C:\actions-runner\_work\benchmarking\benchmarking\cpython\PCBuild\win32\python.exe' -m venv --without-pip 'C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-89a32d3d62d8-compat-cb6a104a6688-bm-pytorch_alexnet_inference'
# 'C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-89a32d3d62d8-compat-cb6a104a6688-bm-pytorch_alexnet_inference\Scripts\python.exe' -m ensurepip -v -U
Using pip 24.3.1 from C:\WINDOWS\SERVIC~1\NETWOR~1\AppData\Local\Temp\tmpawke1q3f\pip-24.3.1-py3-none-any.whl\pip (python 3.14)
Looking in links: c:\WINDOWS\SERVIC~1\NETWOR~1\AppData\Local\Temp\tmpawke1q3f
Processing c:\windows\servic~1\networ~1\appdata\local\temp\tmpawke1q3f\pip-24.3.1-py3-none-any.whl
Installing collected packages: pip
Successfully installed pip-24.3.1
# 'C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-89a32d3d62d8-compat-cb6a104a6688-bm-pytorch_alexnet_inference\Scripts\python.exe' -m pip install -U 'setuptools>=18.5' wheel
Collecting setuptools>=18.5
  Using cached setuptools-75.8.0-py3-none-any.whl.metadata (6.7 kB)
Collecting wheel
  Using cached wheel-0.45.1-py3-none-any.whl.metadata (2.3 kB)
Using cached setuptools-75.8.0-py3-none-any.whl (1.2 MB)
Using cached wheel-0.45.1-py3-none-any.whl (72 kB)
Installing collected packages: wheel, setuptools
ERROR: Could not install packages due to an OSError: [Errno 2] No such file or directory: 'C:\\actions-runner\\_work\\benchmarking\\benchmarking\\venv\\cpython3.14-89a32d3d62d8-compat-cb6a104a6688-bm-pytorch_alexnet_inference\\Lib\\site-packages\\pkg_resources\\tests\\data\\my-test-package_unpacked-egg\\my_test_package-1.0-py3.7.egg\\EGG-INFO\\dependency_links.txt'

Command failed with exit code 1
Remove directory C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-89a32d3d62d8-compat-cb6a104a6688-bm-pytorch_alexnet_inference


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
  "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.42.34433\bin\HostX86\x64\cl.exe" /c /nologo /O2 /W3 /GL /DNDEBUG /MD -DWIN32=1 -IC:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-81fae27ee7dd-compat-cb6a104a6688-bm-sqlalchemy_declarative\include -IC:\actions-runner\_work\benchmarking\benchmarking\cpython\include -IC:\actions-runner\_work\benchmarking\benchmarking\cpython\PCBuild\amd64 -IC:\actions-runner\_work\benchmarking\benchmarking\cpython\PCBuild\amd64 "-IC:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.42.34433\include" "-IC:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\VS\include" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.22621.0\ucrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\um" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\shared" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\winrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\cppwinrt" /EHsc /Tpsrc/greenlet/greenlet.cpp /Fobuild\temp.win-amd64-cpython-314\Release\src\greenlet\greenlet.obj /EHsr /GT
  greenlet.cpp
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal\pycore_stackref.h(278): error C7555: use of designated initializers requires at least '/std:c++20'
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal\pycore_stackref.h(278): error C2737: 'PyStackRef_NULL': const object must be initialized
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(196): error C7555: use of designated initializers requires at least '/std:c++20'
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(196): error C4576: a parenthesized type followed by an initializer list is a non-standard explicit type conversion syntax
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(378): error C7555: use of designated initializers requires at least '/std:c++20'
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(378): error C4576: a parenthesized type followed by an initializer list is a non-standard explicit type conversion syntax
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(379): error C7555: use of designated initializers requires at least '/std:c++20'
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(379): error C4576: a parenthesized type followed by an initializer list is a non-standard explicit type conversion syntax
  error: command 'C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\VC\\Tools\\MSVC\\14.42.34433\\bin\\HostX86\\x64\\cl.exe' failed with exit code 2
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
  "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.42.34433\bin\HostX86\x86\cl.exe" /c /nologo /O2 /W3 /GL /DNDEBUG /MD -DWIN32=1 -IC:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-89a32d3d62d8-compat-cb6a104a6688-bm-sqlalchemy_declarative\include -IC:\actions-runner\_work\benchmarking\benchmarking\cpython\include -IC:\actions-runner\_work\benchmarking\benchmarking\cpython\PCBuild\win32 -IC:\actions-runner\_work\benchmarking\benchmarking\cpython\PCBuild\win32 "-IC:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.42.34433\include" "-IC:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\VS\include" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.22621.0\ucrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\um" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\shared" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\winrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\cppwinrt" /EHsc /Tpsrc/greenlet/greenlet.cpp /Fobuild\temp.win32-cpython-314\Release\src\greenlet\greenlet.obj /EHsr /GT
  greenlet.cpp
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal\pycore_stackref.h(278): error C7555: use of designated initializers requires at least '/std:c++20'
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal\pycore_stackref.h(278): error C2737: 'PyStackRef_NULL': const object must be initialized
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(196): error C7555: use of designated initializers requires at least '/std:c++20'
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(196): error C4576: a parenthesized type followed by an initializer list is a non-standard explicit type conversion syntax
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(378): error C7555: use of designated initializers requires at least '/std:c++20'
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(378): error C4576: a parenthesized type followed by an initializer list is a non-standard explicit type conversion syntax
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(379): error C7555: use of designated initializers requires at least '/std:c++20'
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(379): error C4576: a parenthesized type followed by an initializer list is a non-standard explicit type conversion syntax
  error: command 'C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\VC\\Tools\\MSVC\\14.42.34433\\bin\\HostX86\\x86\\cl.exe' failed with exit code 2
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
  "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.42.34433\bin\HostX86\x64\cl.exe" /c /nologo /O2 /W3 /GL /DNDEBUG /MD -DWIN32=1 -IC:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-81fae27ee7dd-compat-cb6a104a6688-bm-sqlalchemy_imperative\include -IC:\actions-runner\_work\benchmarking\benchmarking\cpython\include -IC:\actions-runner\_work\benchmarking\benchmarking\cpython\PCBuild\amd64 -IC:\actions-runner\_work\benchmarking\benchmarking\cpython\PCBuild\amd64 "-IC:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.42.34433\include" "-IC:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\VS\include" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.22621.0\ucrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\um" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\shared" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\winrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\cppwinrt" /EHsc /Tpsrc/greenlet/greenlet.cpp /Fobuild\temp.win-amd64-cpython-314\Release\src\greenlet\greenlet.obj /EHsr /GT
  greenlet.cpp
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal\pycore_stackref.h(278): error C7555: use of designated initializers requires at least '/std:c++20'
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal\pycore_stackref.h(278): error C2737: 'PyStackRef_NULL': const object must be initialized
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(196): error C7555: use of designated initializers requires at least '/std:c++20'
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(196): error C4576: a parenthesized type followed by an initializer list is a non-standard explicit type conversion syntax
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(378): error C7555: use of designated initializers requires at least '/std:c++20'
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(378): error C4576: a parenthesized type followed by an initializer list is a non-standard explicit type conversion syntax
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(379): error C7555: use of designated initializers requires at least '/std:c++20'
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(379): error C4576: a parenthesized type followed by an initializer list is a non-standard explicit type conversion syntax
  error: command 'C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\VC\\Tools\\MSVC\\14.42.34433\\bin\\HostX86\\x64\\cl.exe' failed with exit code 2
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
  "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.42.34433\bin\HostX86\x86\cl.exe" /c /nologo /O2 /W3 /GL /DNDEBUG /MD -DWIN32=1 -IC:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-89a32d3d62d8-compat-cb6a104a6688-bm-sqlalchemy_imperative\include -IC:\actions-runner\_work\benchmarking\benchmarking\cpython\include -IC:\actions-runner\_work\benchmarking\benchmarking\cpython\PCBuild\win32 -IC:\actions-runner\_work\benchmarking\benchmarking\cpython\PCBuild\win32 "-IC:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.42.34433\include" "-IC:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\VS\include" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.22621.0\ucrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\um" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\shared" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\winrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\cppwinrt" /EHsc /Tpsrc/greenlet/greenlet.cpp /Fobuild\temp.win32-cpython-314\Release\src\greenlet\greenlet.obj /EHsr /GT
  greenlet.cpp
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal\pycore_stackref.h(278): error C7555: use of designated initializers requires at least '/std:c++20'
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal\pycore_stackref.h(278): error C2737: 'PyStackRef_NULL': const object must be initialized
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(196): error C7555: use of designated initializers requires at least '/std:c++20'
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(196): error C4576: a parenthesized type followed by an initializer list is a non-standard explicit type conversion syntax
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(378): error C7555: use of designated initializers requires at least '/std:c++20'
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(378): error C4576: a parenthesized type followed by an initializer list is a non-standard explicit type conversion syntax
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(379): error C7555: use of designated initializers requires at least '/std:c++20'
  C:\actions-runner\_work\benchmarking\benchmarking\cpython\include\internal/pycore_frame.h(379): error C4576: a parenthesized type followed by an initializer list is a non-standard explicit type conversion syntax
  error: command 'C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\VC\\Tools\\MSVC\\14.42.34433\\bin\\HostX86\\x86\\cl.exe' failed with exit code 2
  [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for greenlet
Failed to build greenlet
ERROR: ERROR: Failed to build installable wheels for some pyproject.toml based projects (greenlet)
Command failed with exit code 1


==================================================
```

</details>

## tornado_http on collect-stats pystats

<details>
<summary>Log for tornado_http on collect-stats pystats</summary>

```
        sock, self._handle_connection
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0d57dd0c23e2-compat-cb6a104a6688/lib/python3.14/site-packages/tornado/netutil.py", line 247, in add_accept_handler
    io_loop = IOLoop.current()
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0d57dd0c23e2-compat-cb6a104a6688/lib/python3.14/site-packages/tornado/ioloop.py", line 265, in current
    loop = asyncio.get_event_loop()
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/cpython/Lib/asyncio/events.py", line 719, in get_event_loop
    raise RuntimeError('There is no current event loop in thread %r.'
                       % threading.current_thread().name)
RuntimeError: There is no current event loop in thread 'MainThread'.
Traceback (most recent call last):
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/data-files/benchmarks/bm_tornado_http/run_benchmark.py", line 102, in <module>
    runner.bench_time_func('tornado_http', bench_tornado)
    ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0d57dd0c23e2-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_runner.py", line 499, in bench_time_func
    result = self._main(task)
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0d57dd0c23e2-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_runner.py", line 465, in _main
    bench = self._manager()
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0d57dd0c23e2-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_runner.py", line 678, in _manager
    bench = Manager(self).create_bench()
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0d57dd0c23e2-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_manager.py", line 243, in create_bench
    worker_bench, run = self.create_worker_bench()
                        ~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0d57dd0c23e2-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_manager.py", line 142, in create_worker_bench
    suite = self.create_suite()
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0d57dd0c23e2-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_manager.py", line 136, in create_suite
    suite = self.spawn_worker(0, 0)
  File "/home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0d57dd0c23e2-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_manager.py", line 118, in spawn_worker
    raise RuntimeError("%s failed with exit code %s"
                       % (cmd[0], exitcode))
RuntimeError: /home/mdboom/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-0d57dd0c23e2-compat-cb6a104a6688/bin/python failed with exit code 1
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

## tornado_http on linux-aarch64 default

<details>
<summary>Log for tornado_http on linux-aarch64 default</summary>

```
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/data-files/benchmarks/bm_tornado_http/run_benchmark.py", line 54, in make_http_server
    server.add_sockets(sockets)
    ~~~~~~~~~~~~~~~~~~^^^^^^^^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688/lib/python3.14/site-packages/tornado/tcpserver.py", line 204, in add_sockets
    self._handlers[sock.fileno()] = add_accept_handler(
                                    ~~~~~~~~~~~~~~~~~~^
        sock, self._handle_connection
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688/lib/python3.14/site-packages/tornado/netutil.py", line 247, in add_accept_handler
    io_loop = IOLoop.current()
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688/lib/python3.14/site-packages/tornado/ioloop.py", line 265, in current
    loop = asyncio.get_event_loop()
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/cpython/Lib/asyncio/events.py", line 719, in get_event_loop
    raise RuntimeError('There is no current event loop in thread %r.'
                       % threading.current_thread().name)
RuntimeError: There is no current event loop in thread 'MainThread'.
Traceback (most recent call last):
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/data-files/benchmarks/bm_tornado_http/run_benchmark.py", line 102, in <module>
    runner.bench_time_func('tornado_http', bench_tornado)
    ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_runner.py", line 499, in bench_time_func
    result = self._main(task)
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_runner.py", line 465, in _main
    bench = self._manager()
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_runner.py", line 678, in _manager
    bench = Manager(self).create_bench()
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_manager.py", line 243, in create_bench
    worker_bench, run = self.create_worker_bench()
                        ~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_manager.py", line 142, in create_worker_bench
    suite = self.create_suite()
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_manager.py", line 132, in create_suite
    suite = self.spawn_worker(self.calibrate_loops, 0)
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_manager.py", line 118, in spawn_worker
    raise RuntimeError("%s failed with exit code %s"
                       % (cmd[0], exitcode))
RuntimeError: /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-1bbac01bddc6-compat-cb6a104a6688/bin/python failed with exit code 1
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

## tornado_http on darwin-arm64 default

<details>
<summary>Log for tornado_http on darwin-arm64 default</summary>

```
        sock, self._handle_connection
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688/lib/python3.14/site-packages/tornado/netutil.py", line 247, in add_accept_handler
    io_loop = IOLoop.current()
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688/lib/python3.14/site-packages/tornado/ioloop.py", line 265, in current
    loop = asyncio.get_event_loop()
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/cpython/Lib/asyncio/events.py", line 719, in get_event_loop
    raise RuntimeError('There is no current event loop in thread %r.'
                       % threading.current_thread().name)
RuntimeError: There is no current event loop in thread 'MainThread'.
Traceback (most recent call last):
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.13/site-packages/pyperformance/data-files/benchmarks/bm_tornado_http/run_benchmark.py", line 102, in <module>
    runner.bench_time_func('tornado_http', bench_tornado)
    ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_runner.py", line 499, in bench_time_func
    result = self._main(task)
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_runner.py", line 465, in _main
    bench = self._manager()
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_runner.py", line 678, in _manager
    bench = Manager(self).create_bench()
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_manager.py", line 243, in create_bench
    worker_bench, run = self.create_worker_bench()
                        ~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_manager.py", line 142, in create_worker_bench
    suite = self.create_suite()
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_manager.py", line 132, in create_suite
    suite = self.spawn_worker(self.calibrate_loops, 0)
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_manager.py", line 118, in spawn_worker
    raise RuntimeError("%s failed with exit code %s"
                       % (cmd[0], exitcode))
RuntimeError: /Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-f0f9f90e3807-compat-cb6a104a6688/bin/python failed with exit code 1
Traceback (most recent call last):
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.13/site-packages/pyperformance/run.py", line 170, in run_benchmarks
    result = bench.run(
        bench_venv.python,
    ...<3 lines>...
        verbose=options.verbose,
    )
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.13/site-packages/pyperformance/_benchmark.py", line 189, in run
    bench = _run_perf_script(
        python,
    ...<4 lines>...
        verbose=verbose,
    )
  File "/Users/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.13/site-packages/pyperformance/_benchmark.py", line 240, in _run_perf_script
    raise RuntimeError("Benchmark died")
RuntimeError: Benchmark died
Command failed with exit code 1
```

</details>

## tornado_http on windows-x86_64 default

<details>
<summary>Log for tornado_http on windows-x86_64 default</summary>

```
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\Lib\site-packages\pyperformance\data-files\benchmarks\bm_tornado_http\run_benchmark.py", line 54, in make_http_server
    server.add_sockets(sockets)
    ~~~~~~~~~~~~~~~~~~^^^^^^^^^
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-81fae27ee7dd-compat-cb6a104a6688\Lib\site-packages\tornado\tcpserver.py", line 204, in add_sockets
    self._handlers[sock.fileno()] = add_accept_handler(
                                    ~~~~~~~~~~~~~~~~~~^
        sock, self._handle_connection
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-81fae27ee7dd-compat-cb6a104a6688\Lib\site-packages\tornado\netutil.py", line 247, in add_accept_handler
    io_loop = IOLoop.current()
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-81fae27ee7dd-compat-cb6a104a6688\Lib\site-packages\tornado\ioloop.py", line 265, in current
    loop = asyncio.get_event_loop()
  File "C:\actions-runner\_work\benchmarking\benchmarking\cpython\Lib\asyncio\events.py", line 719, in get_event_loop
    raise RuntimeError('There is no current event loop in thread %r.'
                       % threading.current_thread().name)
RuntimeError: There is no current event loop in thread 'MainThread'.
Traceback (most recent call last):
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\Lib\site-packages\pyperformance\data-files\benchmarks\bm_tornado_http\run_benchmark.py", line 102, in <module>
    runner.bench_time_func('tornado_http', bench_tornado)
    ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-81fae27ee7dd-compat-cb6a104a6688\Lib\site-packages\pyperf\_runner.py", line 499, in bench_time_func
    result = self._main(task)
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-81fae27ee7dd-compat-cb6a104a6688\Lib\site-packages\pyperf\_runner.py", line 465, in _main
    bench = self._manager()
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-81fae27ee7dd-compat-cb6a104a6688\Lib\site-packages\pyperf\_runner.py", line 678, in _manager
    bench = Manager(self).create_bench()
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-81fae27ee7dd-compat-cb6a104a6688\Lib\site-packages\pyperf\_manager.py", line 243, in create_bench
    worker_bench, run = self.create_worker_bench()
                        ~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-81fae27ee7dd-compat-cb6a104a6688\Lib\site-packages\pyperf\_manager.py", line 142, in create_worker_bench
    suite = self.create_suite()
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-81fae27ee7dd-compat-cb6a104a6688\Lib\site-packages\pyperf\_manager.py", line 132, in create_suite
    suite = self.spawn_worker(self.calibrate_loops, 0)
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-81fae27ee7dd-compat-cb6a104a6688\Lib\site-packages\pyperf\_manager.py", line 118, in spawn_worker
    raise RuntimeError("%s failed with exit code %s"
                       % (cmd[0], exitcode))
RuntimeError: C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-81fae27ee7dd-compat-cb6a104a6688\Scripts\python.exe failed with exit code 1
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

## tornado_http on linux-x86_64 default

<details>
<summary>Log for tornado_http on linux-x86_64 default</summary>

```
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/data-files/benchmarks/bm_tornado_http/run_benchmark.py", line 54, in make_http_server
    server.add_sockets(sockets)
    ~~~~~~~~~~~~~~~~~~^^^^^^^^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688/lib/python3.14/site-packages/tornado/tcpserver.py", line 204, in add_sockets
    self._handlers[sock.fileno()] = add_accept_handler(
                                    ~~~~~~~~~~~~~~~~~~^
        sock, self._handle_connection
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688/lib/python3.14/site-packages/tornado/netutil.py", line 247, in add_accept_handler
    io_loop = IOLoop.current()
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688/lib/python3.14/site-packages/tornado/ioloop.py", line 265, in current
    loop = asyncio.get_event_loop()
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/cpython/Lib/asyncio/events.py", line 719, in get_event_loop
    raise RuntimeError('There is no current event loop in thread %r.'
                       % threading.current_thread().name)
RuntimeError: There is no current event loop in thread 'MainThread'.
Traceback (most recent call last):
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/lib/python3.11/site-packages/pyperformance/data-files/benchmarks/bm_tornado_http/run_benchmark.py", line 102, in <module>
    runner.bench_time_func('tornado_http', bench_tornado)
    ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_runner.py", line 499, in bench_time_func
    result = self._main(task)
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_runner.py", line 465, in _main
    bench = self._manager()
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_runner.py", line 678, in _manager
    bench = Manager(self).create_bench()
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_manager.py", line 243, in create_bench
    worker_bench, run = self.create_worker_bench()
                        ~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_manager.py", line 142, in create_worker_bench
    suite = self.create_suite()
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_manager.py", line 132, in create_suite
    suite = self.spawn_worker(self.calibrate_loops, 0)
  File "/home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688/lib/python3.14/site-packages/pyperf/_manager.py", line 118, in spawn_worker
    raise RuntimeError("%s failed with exit code %s"
                       % (cmd[0], exitcode))
RuntimeError: /home/benchmarking/actions-runner/_work/benchmarking/benchmarking/venv/cpython3.14-b8f83472b670-compat-cb6a104a6688/bin/python failed with exit code 1
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

## tornado_http on windows-x86 default

<details>
<summary>Log for tornado_http on windows-x86 default</summary>

```
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\Lib\site-packages\pyperformance\data-files\benchmarks\bm_tornado_http\run_benchmark.py", line 54, in make_http_server
    server.add_sockets(sockets)
    ~~~~~~~~~~~~~~~~~~^^^^^^^^^
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-89a32d3d62d8-compat-cb6a104a6688\Lib\site-packages\tornado\tcpserver.py", line 204, in add_sockets
    self._handlers[sock.fileno()] = add_accept_handler(
                                    ~~~~~~~~~~~~~~~~~~^
        sock, self._handle_connection
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-89a32d3d62d8-compat-cb6a104a6688\Lib\site-packages\tornado\netutil.py", line 247, in add_accept_handler
    io_loop = IOLoop.current()
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-89a32d3d62d8-compat-cb6a104a6688\Lib\site-packages\tornado\ioloop.py", line 265, in current
    loop = asyncio.get_event_loop()
  File "C:\actions-runner\_work\benchmarking\benchmarking\cpython\Lib\asyncio\events.py", line 719, in get_event_loop
    raise RuntimeError('There is no current event loop in thread %r.'
                       % threading.current_thread().name)
RuntimeError: There is no current event loop in thread 'MainThread'.
Traceback (most recent call last):
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\Lib\site-packages\pyperformance\data-files\benchmarks\bm_tornado_http\run_benchmark.py", line 102, in <module>
    runner.bench_time_func('tornado_http', bench_tornado)
    ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-89a32d3d62d8-compat-cb6a104a6688\Lib\site-packages\pyperf\_runner.py", line 499, in bench_time_func
    result = self._main(task)
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-89a32d3d62d8-compat-cb6a104a6688\Lib\site-packages\pyperf\_runner.py", line 465, in _main
    bench = self._manager()
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-89a32d3d62d8-compat-cb6a104a6688\Lib\site-packages\pyperf\_runner.py", line 678, in _manager
    bench = Manager(self).create_bench()
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-89a32d3d62d8-compat-cb6a104a6688\Lib\site-packages\pyperf\_manager.py", line 243, in create_bench
    worker_bench, run = self.create_worker_bench()
                        ~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-89a32d3d62d8-compat-cb6a104a6688\Lib\site-packages\pyperf\_manager.py", line 142, in create_worker_bench
    suite = self.create_suite()
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-89a32d3d62d8-compat-cb6a104a6688\Lib\site-packages\pyperf\_manager.py", line 132, in create_suite
    suite = self.spawn_worker(self.calibrate_loops, 0)
  File "C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-89a32d3d62d8-compat-cb6a104a6688\Lib\site-packages\pyperf\_manager.py", line 118, in spawn_worker
    raise RuntimeError("%s failed with exit code %s"
                       % (cmd[0], exitcode))
RuntimeError: C:\actions-runner\_work\benchmarking\benchmarking\venv\cpython3.14-89a32d3d62d8-compat-cb6a104a6688\Scripts\python.exe failed with exit code 1
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

