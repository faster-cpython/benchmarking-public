# Results

- fork: python
- version: 3.14.0a0
- config: NOGIL
- commit hash: [c4c7097](https://github.com/python/cpython/commit/c4c7097)
- commit date: 2024-07-20T23:32:52+01:00
- commit merge base: [094375b9b7e087a4f0f60541dc7f2dc53be92646](https://github.com/python/cpython/commit/094375b9b7e087a4f0f60541dc7f2dc53be92646)
- ref: c4c7097e64b0c9cb0081

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10023971988)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json)

### vs. 3.10.4

- Geometric mean: 1.21x slower (HPT: reliability of 100.00%, 1.19x slower at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.10.4.md)
- [📈time plot](bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.55x slower (HPT: reliability of 100.00%, 1.38x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser
- [📄table](bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.12.0.md)
- [📈time plot](bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.57x slower (HPT: reliability of 100.00%, 1.40x slower at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: dulwich_log
- [📄table](bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.13.0.md)
- [📈time plot](bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.60x slower (HPT: reliability of 100.00%, 1.42x slower at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: 🔴 dask
- [🧠memory plot](bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-base-mem.svg)
- [📄table](bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-base.md)
- [📈time plot](bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.13.0b2.md)
- [📈time plot](bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.13.0b2.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10023971988)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240720-linux-x86_64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json)

### vs. 3.10.4

- Geometric mean: 1.06x slower (HPT: reliability of 99.98%, 1.04x slower at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240720-linux-x86_64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.10.4.md)
- [📈time plot](bm-20240720-linux-x86_64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.38x slower (HPT: reliability of 100.00%, 1.24x slower at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240720-linux-x86_64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.12.0.md)
- [📈time plot](bm-20240720-linux-x86_64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.47x slower (HPT: reliability of 100.00%, 1.31x slower at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240720-linux-x86_64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.13.0.md)
- [📈time plot](bm-20240720-linux-x86_64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.50x slower (HPT: reliability of 100.00%, 1.34x slower at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: 🔴 dask
- [🧠memory plot](bm-20240720-linux-x86_64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-base-mem.svg)
- [📄table](bm-20240720-linux-x86_64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-base.md)
- [📈time plot](bm-20240720-linux-x86_64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240720-linux-x86_64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.13.0b2.md)
- [📈time plot](bm-20240720-linux-x86_64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.13.0b2.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10023971988)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240720-pythonperf2-x86_64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json)

### vs. 3.10.4

- Geometric mean: 1.11x slower (HPT: reliability of 100.00%, 1.09x slower at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240720-pythonperf2-x86_64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.10.4.md)
- [📈time plot](bm-20240720-pythonperf2-x86_64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.44x slower (HPT: reliability of 100.00%, 1.28x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240720-pythonperf2-x86_64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.12.0.md)
- [📈time plot](bm-20240720-pythonperf2-x86_64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.45x slower (HPT: reliability of 100.00%, 1.31x slower at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240720-pythonperf2-x86_64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.13.0.md)
- [📈time plot](bm-20240720-pythonperf2-x86_64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.46x slower (HPT: reliability of 100.00%, 1.34x slower at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: 🔴 dask
- [🧠memory plot](bm-20240720-pythonperf2-x86_64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-base-mem.svg)
- [📄table](bm-20240720-pythonperf2-x86_64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-base.md)
- [📈time plot](bm-20240720-pythonperf2-x86_64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240720-pythonperf2-x86_64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.13.0b2.md)
- [📈time plot](bm-20240720-pythonperf2-x86_64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.13.0b2.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10023971988)
- cpu model: missing
- platform: macOS-14.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20240720-darwin-arm64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json)

### vs. 3.10.4

- Geometric mean: 1.14x slower (HPT: reliability of 100.00%, 1.12x slower at 99th %ile)
- Memory usage: 0.71x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240720-darwin-arm64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.10.4.md)
- [📈time plot](bm-20240720-darwin-arm64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.33x slower (HPT: reliability of 100.00%, 1.18x slower at 99th %ile)
- Memory usage: 0.73x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240720-darwin-arm64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.12.0.md)
- [📈time plot](bm-20240720-darwin-arm64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.31x slower (HPT: reliability of 100.00%, 1.20x slower at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240720-darwin-arm64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.13.0.md)
- [📈time plot](bm-20240720-darwin-arm64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.43x slower (HPT: reliability of 100.00%, 1.25x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: 🔴 dask
- [🧠memory plot](bm-20240720-darwin-arm64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-base-mem.svg)
- [📄table](bm-20240720-darwin-arm64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-base.md)
- [📈time plot](bm-20240720-darwin-arm64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240720-darwin-arm64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.13.0b2.md)
- [📈time plot](bm-20240720-darwin-arm64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.13.0b2.svg)

