# Results

- fork: python
- version: 3.14.0a0
- config: NOGIL
- commit hash: [68e279b](https://github.com/python/cpython/commit/68e279b)
- commit date: 2024-07-07T00:53:54+02:00
- commit merge base: [114389470ec3db457c589b3991b695258d23ce5a](https://github.com/python/cpython/commit/114389470ec3db457c589b3991b695258d23ce5a)
- ref: 68e279b37aae3019979a

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9822960106)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240707-arminc-aarch64-python-68e279b37aae3019979a-3.14.0a0-68e279b.json)

### vs. 3.10.4

- Geometric mean: 1.23x slower (HPT: reliability of 100.00%, 1.19x slower at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240707-arminc-aarch64-python-68e279b37aae3019979a-3.14.0a0-68e279b-vs-3.10.4.md)
- [📈time plot](bm-20240707-arminc-aarch64-python-68e279b37aae3019979a-3.14.0a0-68e279b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.58x slower (HPT: reliability of 100.00%, 1.38x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser
- [📄table](bm-20240707-arminc-aarch64-python-68e279b37aae3019979a-3.14.0a0-68e279b-vs-3.12.0.md)
- [📈time plot](bm-20240707-arminc-aarch64-python-68e279b37aae3019979a-3.14.0a0-68e279b-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.59x slower (HPT: reliability of 100.00%, 1.38x slower at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240707-arminc-aarch64-python-68e279b37aae3019979a-3.14.0a0-68e279b-vs-3.13.0b2.md)
- [📈time plot](bm-20240707-arminc-aarch64-python-68e279b37aae3019979a-3.14.0a0-68e279b-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.62x slower (HPT: reliability of 100.00%, 1.41x slower at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: 🔴 dask
- [🧠memory plot](bm-20240707-arminc-aarch64-python-68e279b37aae3019979a-3.14.0a0-68e279b-vs-base-mem.svg)
- [📄table](bm-20240707-arminc-aarch64-python-68e279b37aae3019979a-3.14.0a0-68e279b-vs-base.md)
- [📈time plot](bm-20240707-arminc-aarch64-python-68e279b37aae3019979a-3.14.0a0-68e279b-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9822960106)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240707-linux-x86_64-python-68e279b37aae3019979a-3.14.0a0-68e279b.json)

### vs. 3.10.4

- Geometric mean: 1.17x slower (HPT: reliability of 100.00%, 1.10x slower at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240707-linux-x86_64-python-68e279b37aae3019979a-3.14.0a0-68e279b-vs-3.10.4.md)
- [📈time plot](bm-20240707-linux-x86_64-python-68e279b37aae3019979a-3.14.0a0-68e279b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.52x slower (HPT: reliability of 100.00%, 1.32x slower at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240707-linux-x86_64-python-68e279b37aae3019979a-3.14.0a0-68e279b-vs-3.12.0.md)
- [📈time plot](bm-20240707-linux-x86_64-python-68e279b37aae3019979a-3.14.0a0-68e279b-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.57x slower (HPT: reliability of 100.00%, 1.37x slower at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240707-linux-x86_64-python-68e279b37aae3019979a-3.14.0a0-68e279b-vs-3.13.0b2.md)
- [📈time plot](bm-20240707-linux-x86_64-python-68e279b37aae3019979a-3.14.0a0-68e279b-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.66x slower (HPT: reliability of 100.00%, 1.45x slower at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: 🔴 dask
- [🧠memory plot](bm-20240707-linux-x86_64-python-68e279b37aae3019979a-3.14.0a0-68e279b-vs-base-mem.svg)
- [📄table](bm-20240707-linux-x86_64-python-68e279b37aae3019979a-3.14.0a0-68e279b-vs-base.md)
- [📈time plot](bm-20240707-linux-x86_64-python-68e279b37aae3019979a-3.14.0a0-68e279b-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9822960106)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240707-pythonperf2-x86_64-python-68e279b37aae3019979a-3.14.0a0-68e279b.json)

### vs. 3.10.4

- Geometric mean: 1.15x slower (HPT: reliability of 100.00%, 1.11x slower at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240707-pythonperf2-x86_64-python-68e279b37aae3019979a-3.14.0a0-68e279b-vs-3.10.4.md)
- [📈time plot](bm-20240707-pythonperf2-x86_64-python-68e279b37aae3019979a-3.14.0a0-68e279b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.50x slower (HPT: reliability of 100.00%, 1.31x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240707-pythonperf2-x86_64-python-68e279b37aae3019979a-3.14.0a0-68e279b-vs-3.12.0.md)
- [📈time plot](bm-20240707-pythonperf2-x86_64-python-68e279b37aae3019979a-3.14.0a0-68e279b-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.50x slower (HPT: reliability of 100.00%, 1.36x slower at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240707-pythonperf2-x86_64-python-68e279b37aae3019979a-3.14.0a0-68e279b-vs-3.13.0b2.md)
- [📈time plot](bm-20240707-pythonperf2-x86_64-python-68e279b37aae3019979a-3.14.0a0-68e279b-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.53x slower (HPT: reliability of 100.00%, 1.38x slower at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: 🔴 dask
- [🧠memory plot](bm-20240707-pythonperf2-x86_64-python-68e279b37aae3019979a-3.14.0a0-68e279b-vs-base-mem.svg)
- [📄table](bm-20240707-pythonperf2-x86_64-python-68e279b37aae3019979a-3.14.0a0-68e279b-vs-base.md)
- [📈time plot](bm-20240707-pythonperf2-x86_64-python-68e279b37aae3019979a-3.14.0a0-68e279b-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9822960106)
- cpu model: missing
- platform: macOS-14.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20240707-darwin-arm64-python-68e279b37aae3019979a-3.14.0a0-68e279b.json)

### vs. 3.10.4

- Geometric mean: 1.21x slower (HPT: reliability of 100.00%, 1.16x slower at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240707-darwin-arm64-python-68e279b37aae3019979a-3.14.0a0-68e279b-vs-3.10.4.md)
- [📈time plot](bm-20240707-darwin-arm64-python-68e279b37aae3019979a-3.14.0a0-68e279b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.41x slower (HPT: reliability of 100.00%, 1.21x slower at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240707-darwin-arm64-python-68e279b37aae3019979a-3.14.0a0-68e279b-vs-3.12.0.md)
- [📈time plot](bm-20240707-darwin-arm64-python-68e279b37aae3019979a-3.14.0a0-68e279b-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.50x slower (HPT: reliability of 100.00%, 1.26x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240707-darwin-arm64-python-68e279b37aae3019979a-3.14.0a0-68e279b-vs-3.13.0b2.md)
- [📈time plot](bm-20240707-darwin-arm64-python-68e279b37aae3019979a-3.14.0a0-68e279b-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.46x slower (HPT: reliability of 100.00%, 1.24x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: 🔴 dask
- [🧠memory plot](bm-20240707-darwin-arm64-python-68e279b37aae3019979a-3.14.0a0-68e279b-vs-base-mem.svg)
- [📄table](bm-20240707-darwin-arm64-python-68e279b37aae3019979a-3.14.0a0-68e279b-vs-base.md)
- [📈time plot](bm-20240707-darwin-arm64-python-68e279b37aae3019979a-3.14.0a0-68e279b-vs-base.svg)

