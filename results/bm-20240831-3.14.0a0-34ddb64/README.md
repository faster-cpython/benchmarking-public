# Results

- fork: python
- version: 3.14.0a0
- config: 
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

- Geometric mean: 1.35x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.10.4.md)
- [📈time plot](bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.04x faster (HPT: reliability of 99.58%, 1.00x faster at 99th %ile)
- Memory usage: 0.92x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser
- [📄table](bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.12.0.md)
- [📈time plot](bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.03x faster (HPT: reliability of 99.98%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.13.0b2.md)
- [📈time plot](bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.13.0b2.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20240831-azure-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-pystats.json)
- [pystats table](bm-20240831-azure-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10649186889)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-192-generic-x86_64-with-glibc2.31
- [raw results](bm-20240831-linux-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json)

### vs. 3.10.4

- Geometric mean: 1.43x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240831-linux-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.10.4.md)
- [📈time plot](bm-20240831-linux-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240831-linux-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.12.0.md)
- [📈time plot](bm-20240831-linux-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240831-linux-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.13.0b2.md)
- [📈time plot](bm-20240831-linux-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.13.0b2.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10649186889)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json)

### vs. 3.10.4

- Geometric mean: 1.36x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.10.4.md)
- [📈time plot](bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 99.33%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.12.0.md)
- [📈time plot](bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.03x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.13.0b2.md)
- [📈time plot](bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.13.0b2.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10649186889)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json)

### vs. 3.10.4

- Geometric mean: 1.19x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.10.4.md)
- [📈time plot](bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.00x slower (HPT: reliability of 97.19%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.12.0.md)
- [📈time plot](bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.13.0b2.md)
- [📈time plot](bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.13.0b2.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10649186889)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json)

### vs. 3.10.4

- Geometric mean: 1.13x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.10.4.md)
- [📈time plot](bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.13x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.12.0.md)
- [📈time plot](bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.03x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- new benchmarks: dulwich_log
- [📄table](bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.13.0b2.md)
- [📈time plot](bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.13.0b2.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10649186889)
- cpu model: missing
- platform: macOS-14.6.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json)

### vs. 3.10.4

- Geometric mean: 1.30x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 0.56x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.10.4.md)
- [📈time plot](bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.09x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.47x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.12.0.md)
- [📈time plot](bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.00x faster (HPT: reliability of 95.93%, 1.00x slower at 99th %ile)
- Memory usage: 0.38x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.13.0b2.md)
- [📈time plot](bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64-vs-3.13.0b2.svg)

