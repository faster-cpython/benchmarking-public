# Results

- fork: python
- version: 3.14.0a0
- config: NOGIL
- commit hash: [151934a](https://github.com/python/cpython/commit/151934a)
- commit date: 2024-08-04T00:55:47+03:00
- commit merge base: [95f5c89b545beaafad73f05a695742da3e90bc41](https://github.com/python/cpython/commit/95f5c89b545beaafad73f05a695742da3e90bc41)
- ref: 151934a324789c58cca9

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10231822849)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240804-arminc-aarch64-python-151934a324789c58cca9-3.14.0a0-151934a.json)

### vs. 3.10.4

- Geometric mean: 1.21x slower (HPT: reliability of 100.00%, 1.18x slower at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240804-arminc-aarch64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.10.4.md)
- [📈time plot](bm-20240804-arminc-aarch64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.56x slower (HPT: reliability of 100.00%, 1.36x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser
- [📄table](bm-20240804-arminc-aarch64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.12.0.md)
- [📈time plot](bm-20240804-arminc-aarch64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.57x slower (HPT: reliability of 100.00%, 1.36x slower at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240804-arminc-aarch64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.13.0b2.md)
- [📈time plot](bm-20240804-arminc-aarch64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.61x slower (HPT: reliability of 100.00%, 1.41x slower at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: 🔴 dask
- [🧠memory plot](bm-20240804-arminc-aarch64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-base-mem.svg)
- [📄table](bm-20240804-arminc-aarch64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-base.md)
- [📈time plot](bm-20240804-arminc-aarch64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10231822849)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240804-linux-x86_64-python-151934a324789c58cca9-3.14.0a0-151934a.json)

### vs. 3.10.4

- Geometric mean: 1.05x slower (HPT: reliability of 99.78%, 1.02x slower at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240804-linux-x86_64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.10.4.md)
- [📈time plot](bm-20240804-linux-x86_64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.36x slower (HPT: reliability of 100.00%, 1.21x slower at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240804-linux-x86_64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.12.0.md)
- [📈time plot](bm-20240804-linux-x86_64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.41x slower (HPT: reliability of 100.00%, 1.24x slower at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240804-linux-x86_64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.13.0b2.md)
- [📈time plot](bm-20240804-linux-x86_64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.47x slower (HPT: reliability of 100.00%, 1.29x slower at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: 🔴 dask
- [🧠memory plot](bm-20240804-linux-x86_64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-base-mem.svg)
- [📄table](bm-20240804-linux-x86_64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-base.md)
- [📈time plot](bm-20240804-linux-x86_64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10231822849)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240804-pythonperf2-x86_64-python-151934a324789c58cca9-3.14.0a0-151934a.json)

### vs. 3.10.4

- Geometric mean: 1.11x slower (HPT: reliability of 99.99%, 1.06x slower at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240804-pythonperf2-x86_64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.10.4.md)
- [📈time plot](bm-20240804-pythonperf2-x86_64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.44x slower (HPT: reliability of 100.00%, 1.26x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240804-pythonperf2-x86_64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.12.0.md)
- [📈time plot](bm-20240804-pythonperf2-x86_64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.44x slower (HPT: reliability of 100.00%, 1.31x slower at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240804-pythonperf2-x86_64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.13.0b2.md)
- [📈time plot](bm-20240804-pythonperf2-x86_64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.47x slower (HPT: reliability of 100.00%, 1.32x slower at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: 🔴 dask
- [🧠memory plot](bm-20240804-pythonperf2-x86_64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-base-mem.svg)
- [📄table](bm-20240804-pythonperf2-x86_64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-base.md)
- [📈time plot](bm-20240804-pythonperf2-x86_64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10231822849)
- cpu model: missing
- platform: macOS-14.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20240804-darwin-arm64-python-151934a324789c58cca9-3.14.0a0-151934a.json)

### vs. 3.10.4

- Geometric mean: 1.18x slower (HPT: reliability of 100.00%, 1.13x slower at 99th %ile)
- Memory usage: 0.74x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240804-darwin-arm64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.10.4.md)
- [📈time plot](bm-20240804-darwin-arm64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.38x slower (HPT: reliability of 100.00%, 1.19x slower at 99th %ile)
- Memory usage: 0.65x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240804-darwin-arm64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.12.0.md)
- [📈time plot](bm-20240804-darwin-arm64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.47x slower (HPT: reliability of 100.00%, 1.25x slower at 99th %ile)
- Memory usage: 0.56x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240804-darwin-arm64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.13.0b2.md)
- [📈time plot](bm-20240804-darwin-arm64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.48x slower (HPT: reliability of 100.00%, 1.25x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: 🔴 dask
- [🧠memory plot](bm-20240804-darwin-arm64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-base-mem.svg)
- [📄table](bm-20240804-darwin-arm64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-base.md)
- [📈time plot](bm-20240804-darwin-arm64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-base.svg)

