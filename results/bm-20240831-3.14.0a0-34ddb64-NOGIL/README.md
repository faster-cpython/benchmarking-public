# Results

- fork: python
- version: 3.14.0a0
- config: NOGIL
- commit hash: [34ddb64](https://github.com/python/cpython/commit/34ddb64)
- commit date: 2024-08-31T15:17:05-07:00
- commit merge base: [0cba289870d5cd41f24b2f63b9480e4593aa2330](https://github.com/python/cpython/commit/0cba289870d5cd41f24b2f63b9480e4593aa2330)
- ref: 34ddb64d088dd7ccc321

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10649186889)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json)

### vs. 3.10.4

- Geometric mean: 1.21x slower (HPT: reliability of 100.00%, 1.16x slower at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.10.4.md)
- [📈time plot](bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.55x slower (HPT: reliability of 100.00%, 1.36x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser
- [📄table](bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.12.0.md)
- [📈time plot](bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.57x slower (HPT: reliability of 100.00%, 1.35x slower at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.13.0b2.md)
- [📈time plot](bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.61x slower (HPT: reliability of 100.00%, 1.41x slower at 99th %ile)
- Memory usage: 1.16x
- [🧠memory plot](bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-base-mem.svg)
- [📄table](bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-base.md)
- [📈time plot](bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10649186889)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-192-generic-x86_64-with-glibc2.31
- [raw results](bm-20240831-linux-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json)

### vs. 3.10.4

- Geometric mean: 1.04x slower (HPT: reliability of 99.58%, 1.00x slower at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240831-linux-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.10.4.md)
- [📈time plot](bm-20240831-linux-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.35x slower (HPT: reliability of 100.00%, 1.19x slower at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240831-linux-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.12.0.md)
- [📈time plot](bm-20240831-linux-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.39x slower (HPT: reliability of 100.00%, 1.23x slower at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240831-linux-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.13.0b2.md)
- [📈time plot](bm-20240831-linux-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.46x slower (HPT: reliability of 100.00%, 1.28x slower at 99th %ile)
- Memory usage: 1.15x
- [🧠memory plot](bm-20240831-linux-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-base-mem.svg)
- [📄table](bm-20240831-linux-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-base.md)
- [📈time plot](bm-20240831-linux-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10649186889)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json)

### vs. 3.10.4

- Geometric mean: 1.10x slower (HPT: reliability of 99.99%, 1.06x slower at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.10.4.md)
- [📈time plot](bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.44x slower (HPT: reliability of 100.00%, 1.26x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.12.0.md)
- [📈time plot](bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.44x slower (HPT: reliability of 100.00%, 1.30x slower at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.13.0b2.md)
- [📈time plot](bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.49x slower (HPT: reliability of 100.00%, 1.32x slower at 99th %ile)
- Memory usage: 1.16x
- [🧠memory plot](bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-base-mem.svg)
- [📄table](bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-base.md)
- [📈time plot](bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10649186889)
- cpu model: missing
- platform: macOS-14.6.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json)

### vs. 3.10.4

- Geometric mean: 1.16x slower (HPT: reliability of 100.00%, 1.12x slower at 99th %ile)
- Memory usage: 0.84x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.10.4.md)
- [📈time plot](bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.36x slower (HPT: reliability of 100.00%, 1.17x slower at 99th %ile)
- Memory usage: 0.74x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.12.0.md)
- [📈time plot](bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.45x slower (HPT: reliability of 100.00%, 1.24x slower at 99th %ile)
- Memory usage: 0.63x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.13.0b2.md)
- [📈time plot](bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.46x slower (HPT: reliability of 100.00%, 1.22x slower at 99th %ile)
- Memory usage: 1.10x
- [🧠memory plot](bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-base-mem.svg)
- [📄table](bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-base.md)
- [📈time plot](bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-base.svg)

