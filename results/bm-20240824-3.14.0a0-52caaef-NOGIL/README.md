# Results

- fork: python
- version: 3.14.0a0
- config: NOGIL
- commit hash: [52caaef](https://github.com/python/cpython/commit/52caaef)
- commit date: 2024-08-24T21:54:31+00:00
- commit merge base: [e38d0afe3548b856ccf0b05c01ed3eefc69cb3e7](https://github.com/python/cpython/commit/e38d0afe3548b856ccf0b05c01ed3eefc69cb3e7)
- ref: 52caaef6d01a94962576

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10542438091)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef.json)

### vs. 3.10.4

- Geometric mean: 1.21x slower (HPT: reliability of 100.00%, 1.15x slower at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef-vs-3.10.4.md)
- [📈time plot](bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.56x slower (HPT: reliability of 100.00%, 1.35x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser
- [📄table](bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef-vs-3.12.0.md)
- [📈time plot](bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.57x slower (HPT: reliability of 100.00%, 1.35x slower at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef-vs-3.13.0b2.md)
- [📈time plot](bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.61x slower (HPT: reliability of 100.00%, 1.40x slower at 99th %ile)
- Memory usage: 1.17x
- [🧠memory plot](bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef-vs-base-mem.svg)
- [📄table](bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef-vs-base.md)
- [📈time plot](bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10542438091)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-192-generic-x86_64-with-glibc2.31
- [raw results](bm-20240824-linux-x86_64-python-52caaef6d01a94962576-3.14.0a0-52caaef.json)

### vs. 3.10.4

- Geometric mean: 1.05x slower (HPT: reliability of 99.52%, 1.00x slower at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240824-linux-x86_64-python-52caaef6d01a94962576-3.14.0a0-52caaef-vs-3.10.4.md)
- [📈time plot](bm-20240824-linux-x86_64-python-52caaef6d01a94962576-3.14.0a0-52caaef-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.36x slower (HPT: reliability of 100.00%, 1.20x slower at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240824-linux-x86_64-python-52caaef6d01a94962576-3.14.0a0-52caaef-vs-3.12.0.md)
- [📈time plot](bm-20240824-linux-x86_64-python-52caaef6d01a94962576-3.14.0a0-52caaef-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.41x slower (HPT: reliability of 100.00%, 1.24x slower at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240824-linux-x86_64-python-52caaef6d01a94962576-3.14.0a0-52caaef-vs-3.13.0b2.md)
- [📈time plot](bm-20240824-linux-x86_64-python-52caaef6d01a94962576-3.14.0a0-52caaef-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.47x slower (HPT: reliability of 100.00%, 1.29x slower at 99th %ile)
- Memory usage: 1.15x
- [🧠memory plot](bm-20240824-linux-x86_64-python-52caaef6d01a94962576-3.14.0a0-52caaef-vs-base-mem.svg)
- [📄table](bm-20240824-linux-x86_64-python-52caaef6d01a94962576-3.14.0a0-52caaef-vs-base.md)
- [📈time plot](bm-20240824-linux-x86_64-python-52caaef6d01a94962576-3.14.0a0-52caaef-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10542438091)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240824-pythonperf2-x86_64-python-52caaef6d01a94962576-3.14.0a0-52caaef.json)

### vs. 3.10.4

- Geometric mean: 1.11x slower (HPT: reliability of 99.99%, 1.07x slower at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240824-pythonperf2-x86_64-python-52caaef6d01a94962576-3.14.0a0-52caaef-vs-3.10.4.md)
- [📈time plot](bm-20240824-pythonperf2-x86_64-python-52caaef6d01a94962576-3.14.0a0-52caaef-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.44x slower (HPT: reliability of 100.00%, 1.25x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240824-pythonperf2-x86_64-python-52caaef6d01a94962576-3.14.0a0-52caaef-vs-3.12.0.md)
- [📈time plot](bm-20240824-pythonperf2-x86_64-python-52caaef6d01a94962576-3.14.0a0-52caaef-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.44x slower (HPT: reliability of 100.00%, 1.30x slower at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240824-pythonperf2-x86_64-python-52caaef6d01a94962576-3.14.0a0-52caaef-vs-3.13.0b2.md)
- [📈time plot](bm-20240824-pythonperf2-x86_64-python-52caaef6d01a94962576-3.14.0a0-52caaef-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.47x slower (HPT: reliability of 100.00%, 1.32x slower at 99th %ile)
- Memory usage: 1.16x
- [🧠memory plot](bm-20240824-pythonperf2-x86_64-python-52caaef6d01a94962576-3.14.0a0-52caaef-vs-base-mem.svg)
- [📄table](bm-20240824-pythonperf2-x86_64-python-52caaef6d01a94962576-3.14.0a0-52caaef-vs-base.md)
- [📈time plot](bm-20240824-pythonperf2-x86_64-python-52caaef6d01a94962576-3.14.0a0-52caaef-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10542438091)
- cpu model: missing
- platform: macOS-14.6.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20240824-darwin-arm64-python-52caaef6d01a94962576-3.14.0a0-52caaef.json)

### vs. 3.10.4

- Geometric mean: 1.20x slower (HPT: reliability of 100.00%, 1.15x slower at 99th %ile)
- Memory usage: 0.55x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240824-darwin-arm64-python-52caaef6d01a94962576-3.14.0a0-52caaef-vs-3.10.4.md)
- [📈time plot](bm-20240824-darwin-arm64-python-52caaef6d01a94962576-3.14.0a0-52caaef-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.40x slower (HPT: reliability of 100.00%, 1.19x slower at 99th %ile)
- Memory usage: 0.55x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240824-darwin-arm64-python-52caaef6d01a94962576-3.14.0a0-52caaef-vs-3.12.0.md)
- [📈time plot](bm-20240824-darwin-arm64-python-52caaef6d01a94962576-3.14.0a0-52caaef-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.49x slower (HPT: reliability of 100.00%, 1.24x slower at 99th %ile)
- Memory usage: 0.40x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240824-darwin-arm64-python-52caaef6d01a94962576-3.14.0a0-52caaef-vs-3.13.0b2.md)
- [📈time plot](bm-20240824-darwin-arm64-python-52caaef6d01a94962576-3.14.0a0-52caaef-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.51x slower (HPT: reliability of 100.00%, 1.25x slower at 99th %ile)
- Memory usage: 1.09x
- [🧠memory plot](bm-20240824-darwin-arm64-python-52caaef6d01a94962576-3.14.0a0-52caaef-vs-base-mem.svg)
- [📄table](bm-20240824-darwin-arm64-python-52caaef6d01a94962576-3.14.0a0-52caaef-vs-base.md)
- [📈time plot](bm-20240824-darwin-arm64-python-52caaef6d01a94962576-3.14.0a0-52caaef-vs-base.svg)

