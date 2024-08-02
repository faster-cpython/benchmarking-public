# Results

- fork: python
- version: 3.14.0a0
- config: NOGIL
- commit hash: [6b280a8](https://github.com/python/cpython/commit/6b280a8)
- commit date: 2024-06-29T17:46:53+00:00
- commit merge base: [d6d8707ff217f211f3a2e48084cc0ddfa41efc4d](https://github.com/python/cpython/commit/d6d8707ff217f211f3a2e48084cc0ddfa41efc4d)
- ref: 6b280a84988ca221b5bd

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9727767593)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json)

### vs. 3.10.4

- Geometric mean: 1.21x slower (HPT: reliability of 100.00%, 1.17x slower at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.10.4.md)
- [📈time plot](bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.56x slower (HPT: reliability of 100.00%, 1.36x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser
- [📄table](bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.12.0.md)
- [📈time plot](bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.57x slower (HPT: reliability of 100.00%, 1.36x slower at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.13.0b2.md)
- [📈time plot](bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.60x slower (HPT: reliability of 100.00%, 1.41x slower at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: 🔴 dask
- [🧠memory plot](bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-base-mem.svg)
- [📄table](bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-base.md)
- [📈time plot](bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9727767593)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240629-linux-x86_64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json)

### vs. 3.10.4

- Geometric mean: 1.18x slower (HPT: reliability of 100.00%, 1.10x slower at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240629-linux-x86_64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.10.4.md)
- [📈time plot](bm-20240629-linux-x86_64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.53x slower (HPT: reliability of 100.00%, 1.32x slower at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240629-linux-x86_64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.12.0.md)
- [📈time plot](bm-20240629-linux-x86_64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.58x slower (HPT: reliability of 100.00%, 1.37x slower at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240629-linux-x86_64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.13.0b2.md)
- [📈time plot](bm-20240629-linux-x86_64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.65x slower (HPT: reliability of 100.00%, 1.44x slower at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: 🔴 dask
- [🧠memory plot](bm-20240629-linux-x86_64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-base-mem.svg)
- [📄table](bm-20240629-linux-x86_64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-base.md)
- [📈time plot](bm-20240629-linux-x86_64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9727767593)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240629-pythonperf2-x86_64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json)

### vs. 3.10.4

- Geometric mean: 1.15x slower (HPT: reliability of 100.00%, 1.10x slower at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240629-pythonperf2-x86_64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.10.4.md)
- [📈time plot](bm-20240629-pythonperf2-x86_64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.50x slower (HPT: reliability of 100.00%, 1.30x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240629-pythonperf2-x86_64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.12.0.md)
- [📈time plot](bm-20240629-pythonperf2-x86_64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.50x slower (HPT: reliability of 100.00%, 1.35x slower at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240629-pythonperf2-x86_64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.13.0b2.md)
- [📈time plot](bm-20240629-pythonperf2-x86_64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.53x slower (HPT: reliability of 100.00%, 1.36x slower at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: 🔴 dask
- [🧠memory plot](bm-20240629-pythonperf2-x86_64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-base-mem.svg)
- [📄table](bm-20240629-pythonperf2-x86_64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-base.md)
- [📈time plot](bm-20240629-pythonperf2-x86_64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9727767593)
- cpu model: missing
- platform: macOS-14.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20240629-darwin-arm64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json)

### vs. 3.10.4

- Geometric mean: 1.20x slower (HPT: reliability of 100.00%, 1.15x slower at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240629-darwin-arm64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.10.4.md)
- [📈time plot](bm-20240629-darwin-arm64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.40x slower (HPT: reliability of 100.00%, 1.20x slower at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240629-darwin-arm64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.12.0.md)
- [📈time plot](bm-20240629-darwin-arm64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.49x slower (HPT: reliability of 100.00%, 1.25x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240629-darwin-arm64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.13.0b2.md)
- [📈time plot](bm-20240629-darwin-arm64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.45x slower (HPT: reliability of 100.00%, 1.23x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: 🔴 dask
- [🧠memory plot](bm-20240629-darwin-arm64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-base-mem.svg)
- [📄table](bm-20240629-darwin-arm64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-base.md)
- [📈time plot](bm-20240629-darwin-arm64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-base.svg)

