# Results

- fork: python
- version: 3.14.0a0
- config: NOGIL
- commit hash: [363374c](https://github.com/python/cpython/commit/363374c)
- commit date: 2024-08-10T21:21:17+00:00
- commit merge base: [0959142e4defcf7a9fcbbb228d2e2b97a074f7ea](https://github.com/python/cpython/commit/0959142e4defcf7a9fcbbb228d2e2b97a074f7ea)
- ref: 363374cf69a7e2292fe3

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10335362273)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240810-arminc-aarch64-python-363374cf69a7e2292fe3-3.14.0a0-363374c.json)

### vs. 3.10.4

- Geometric mean: 1.22x slower (HPT: reliability of 100.00%, 1.17x slower at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240810-arminc-aarch64-python-363374cf69a7e2292fe3-3.14.0a0-363374c-vs-3.10.4.md)
- [📈time plot](bm-20240810-arminc-aarch64-python-363374cf69a7e2292fe3-3.14.0a0-363374c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.56x slower (HPT: reliability of 100.00%, 1.36x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser
- [📄table](bm-20240810-arminc-aarch64-python-363374cf69a7e2292fe3-3.14.0a0-363374c-vs-3.12.0.md)
- [📈time plot](bm-20240810-arminc-aarch64-python-363374cf69a7e2292fe3-3.14.0a0-363374c-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.58x slower (HPT: reliability of 100.00%, 1.36x slower at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240810-arminc-aarch64-python-363374cf69a7e2292fe3-3.14.0a0-363374c-vs-3.13.0b2.md)
- [📈time plot](bm-20240810-arminc-aarch64-python-363374cf69a7e2292fe3-3.14.0a0-363374c-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.62x slower (HPT: reliability of 100.00%, 1.41x slower at 99th %ile)
- Memory usage: 1.16x
- [🧠memory plot](bm-20240810-arminc-aarch64-python-363374cf69a7e2292fe3-3.14.0a0-363374c-vs-base-mem.svg)
- [📄table](bm-20240810-arminc-aarch64-python-363374cf69a7e2292fe3-3.14.0a0-363374c-vs-base.md)
- [📈time plot](bm-20240810-arminc-aarch64-python-363374cf69a7e2292fe3-3.14.0a0-363374c-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10335362273)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240810-linux-x86_64-python-363374cf69a7e2292fe3-3.14.0a0-363374c.json)

### vs. 3.10.4

- Geometric mean: 1.04x slower (HPT: reliability of 99.83%, 1.01x slower at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240810-linux-x86_64-python-363374cf69a7e2292fe3-3.14.0a0-363374c-vs-3.10.4.md)
- [📈time plot](bm-20240810-linux-x86_64-python-363374cf69a7e2292fe3-3.14.0a0-363374c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.36x slower (HPT: reliability of 100.00%, 1.20x slower at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240810-linux-x86_64-python-363374cf69a7e2292fe3-3.14.0a0-363374c-vs-3.12.0.md)
- [📈time plot](bm-20240810-linux-x86_64-python-363374cf69a7e2292fe3-3.14.0a0-363374c-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.40x slower (HPT: reliability of 100.00%, 1.23x slower at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240810-linux-x86_64-python-363374cf69a7e2292fe3-3.14.0a0-363374c-vs-3.13.0b2.md)
- [📈time plot](bm-20240810-linux-x86_64-python-363374cf69a7e2292fe3-3.14.0a0-363374c-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.47x slower (HPT: reliability of 100.00%, 1.29x slower at 99th %ile)
- Memory usage: 1.15x
- [🧠memory plot](bm-20240810-linux-x86_64-python-363374cf69a7e2292fe3-3.14.0a0-363374c-vs-base-mem.svg)
- [📄table](bm-20240810-linux-x86_64-python-363374cf69a7e2292fe3-3.14.0a0-363374c-vs-base.md)
- [📈time plot](bm-20240810-linux-x86_64-python-363374cf69a7e2292fe3-3.14.0a0-363374c-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10335362273)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240810-pythonperf2-x86_64-python-363374cf69a7e2292fe3-3.14.0a0-363374c.json)

### vs. 3.10.4

- Geometric mean: 1.11x slower (HPT: reliability of 99.99%, 1.05x slower at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240810-pythonperf2-x86_64-python-363374cf69a7e2292fe3-3.14.0a0-363374c-vs-3.10.4.md)
- [📈time plot](bm-20240810-pythonperf2-x86_64-python-363374cf69a7e2292fe3-3.14.0a0-363374c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.44x slower (HPT: reliability of 100.00%, 1.25x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240810-pythonperf2-x86_64-python-363374cf69a7e2292fe3-3.14.0a0-363374c-vs-3.12.0.md)
- [📈time plot](bm-20240810-pythonperf2-x86_64-python-363374cf69a7e2292fe3-3.14.0a0-363374c-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.44x slower (HPT: reliability of 100.00%, 1.31x slower at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240810-pythonperf2-x86_64-python-363374cf69a7e2292fe3-3.14.0a0-363374c-vs-3.13.0b2.md)
- [📈time plot](bm-20240810-pythonperf2-x86_64-python-363374cf69a7e2292fe3-3.14.0a0-363374c-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.48x slower (HPT: reliability of 100.00%, 1.33x slower at 99th %ile)
- Memory usage: 1.16x
- [🧠memory plot](bm-20240810-pythonperf2-x86_64-python-363374cf69a7e2292fe3-3.14.0a0-363374c-vs-base-mem.svg)
- [📄table](bm-20240810-pythonperf2-x86_64-python-363374cf69a7e2292fe3-3.14.0a0-363374c-vs-base.md)
- [📈time plot](bm-20240810-pythonperf2-x86_64-python-363374cf69a7e2292fe3-3.14.0a0-363374c-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10335362273)
- cpu model: missing
- platform: macOS-14.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20240810-darwin-arm64-python-363374cf69a7e2292fe3-3.14.0a0-363374c.json)

### vs. 3.10.4

- Geometric mean: 1.19x slower (HPT: reliability of 100.00%, 1.13x slower at 99th %ile)
- Memory usage: 0.60x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240810-darwin-arm64-python-363374cf69a7e2292fe3-3.14.0a0-363374c-vs-3.10.4.md)
- [📈time plot](bm-20240810-darwin-arm64-python-363374cf69a7e2292fe3-3.14.0a0-363374c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.39x slower (HPT: reliability of 100.00%, 1.18x slower at 99th %ile)
- Memory usage: 0.49x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240810-darwin-arm64-python-363374cf69a7e2292fe3-3.14.0a0-363374c-vs-3.12.0.md)
- [📈time plot](bm-20240810-darwin-arm64-python-363374cf69a7e2292fe3-3.14.0a0-363374c-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.48x slower (HPT: reliability of 100.00%, 1.25x slower at 99th %ile)
- Memory usage: 0.46x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240810-darwin-arm64-python-363374cf69a7e2292fe3-3.14.0a0-363374c-vs-3.13.0b2.md)
- [📈time plot](bm-20240810-darwin-arm64-python-363374cf69a7e2292fe3-3.14.0a0-363374c-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.48x slower (HPT: reliability of 100.00%, 1.26x slower at 99th %ile)
- Memory usage: 1.10x
- [🧠memory plot](bm-20240810-darwin-arm64-python-363374cf69a7e2292fe3-3.14.0a0-363374c-vs-base-mem.svg)
- [📄table](bm-20240810-darwin-arm64-python-363374cf69a7e2292fe3-3.14.0a0-363374c-vs-base.md)
- [📈time plot](bm-20240810-darwin-arm64-python-363374cf69a7e2292fe3-3.14.0a0-363374c-vs-base.svg)

