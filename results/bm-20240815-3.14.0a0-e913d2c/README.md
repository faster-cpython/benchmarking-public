# Results

- fork: python
- version: 3.14.0a0
- config: 
- commit hash: [e913d2c](https://github.com/python/cpython/commit/e913d2c)
- commit date: 2024-08-15T15:32:05-04:00
- commit merge base: [d7a3df91505faa56c51d169648253bd0d57ddae2](https://github.com/python/cpython/commit/d7a3df91505faa56c51d169648253bd0d57ddae2)
- ref: e913d2c87f1ae4e7a4ae

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10600696475)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240815-arminc-aarch64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c.json)

### vs. 3.10.4

- Geometric mean: 1.34x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240815-arminc-aarch64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c-vs-3.10.4.md)
- [📈time plot](bm-20240815-arminc-aarch64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 90.94%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser
- [📄table](bm-20240815-arminc-aarch64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c-vs-3.12.0.md)
- [📈time plot](bm-20240815-arminc-aarch64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x faster (HPT: reliability of 99.64%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240815-arminc-aarch64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c-vs-3.13.0b2.md)
- [📈time plot](bm-20240815-arminc-aarch64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c-vs-3.13.0b2.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10600696475)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-192-generic-x86_64-with-glibc2.31
- [raw results](bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c.json)

### vs. 3.10.4

- Geometric mean: 1.44x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c-vs-3.10.4.md)
- [📈time plot](bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.09x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c-vs-3.12.0.md)
- [📈time plot](bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.06x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c-vs-3.13.0b2.md)
- [📈time plot](bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c-vs-3.13.0b2.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10600696475)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c.json)

### vs. 3.10.4

- Geometric mean: 1.35x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c-vs-3.10.4.md)
- [📈time plot](bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 88.64%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c-vs-3.12.0.md)
- [📈time plot](bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.03x faster (HPT: reliability of 99.98%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c-vs-3.13.0b2.md)
- [📈time plot](bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c-vs-3.13.0b2.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10600696475)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240815-pythonperf1-amd64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c.json)

### vs. 3.10.4

- Geometric mean: 1.17x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240815-pythonperf1-amd64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c-vs-3.10.4.md)
- [📈time plot](bm-20240815-pythonperf1-amd64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.01x slower (HPT: reliability of 99.67%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240815-pythonperf1-amd64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c-vs-3.12.0.md)
- [📈time plot](bm-20240815-pythonperf1-amd64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.06x slower (HPT: reliability of 100.00%, 1.08x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240815-pythonperf1-amd64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c-vs-3.13.0b2.md)
- [📈time plot](bm-20240815-pythonperf1-amd64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c-vs-3.13.0b2.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10600696475)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c.json)

### vs. 3.10.4

- Geometric mean: 1.12x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c-vs-3.10.4.md)
- [📈time plot](bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.13x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c-vs-3.12.0.md)
- [📈time plot](bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.04x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- new benchmarks: dulwich_log
- [📄table](bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c-vs-3.13.0b2.md)
- [📈time plot](bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c-vs-3.13.0b2.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10600696475)
- cpu model: missing
- platform: macOS-14.6.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20240815-darwin-arm64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c.json)

### vs. 3.10.4

- Geometric mean: 1.29x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 0.87x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240815-darwin-arm64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c-vs-3.10.4.md)
- [📈time plot](bm-20240815-darwin-arm64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 0.76x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240815-darwin-arm64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c-vs-3.12.0.md)
- [📈time plot](bm-20240815-darwin-arm64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.00x slower (HPT: reliability of 99.99%, 1.00x slower at 99th %ile)
- Memory usage: 0.66x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240815-darwin-arm64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c-vs-3.13.0b2.md)
- [📈time plot](bm-20240815-darwin-arm64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c-vs-3.13.0b2.svg)

