# Results

- fork: python
- version: 3.14.0a0
- config: 
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

- Geometric mean: 1.34x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.10.4.md)
- [📈time plot](bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 94.26%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser
- [📄table](bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.12.0.md)
- [📈time plot](bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x faster (HPT: reliability of 99.76%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.13.0b2.md)
- [📈time plot](bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.13.0b2.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20240720-azure-x86_64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-pystats.json)
- [pystats table](bm-20240720-azure-x86_64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10023971988)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240720-linux-x86_64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json)

### vs. 3.10.4

- Geometric mean: 1.43x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240720-linux-x86_64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.10.4.md)
- [📈time plot](bm-20240720-linux-x86_64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.09x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240720-linux-x86_64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.12.0.md)
- [📈time plot](bm-20240720-linux-x86_64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240720-linux-x86_64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.13.0b2.md)
- [📈time plot](bm-20240720-linux-x86_64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.13.0b2.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10023971988)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240720-pythonperf2-x86_64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json)

### vs. 3.10.4

- Geometric mean: 1.33x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240720-pythonperf2-x86_64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.10.4.md)
- [📈time plot](bm-20240720-pythonperf2-x86_64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.02x faster (HPT: reliability of 59.68%, 1.00x slower at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240720-pythonperf2-x86_64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.12.0.md)
- [📈time plot](bm-20240720-pythonperf2-x86_64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x faster (HPT: reliability of 86.75%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240720-pythonperf2-x86_64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.13.0b2.md)
- [📈time plot](bm-20240720-pythonperf2-x86_64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.13.0b2.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10023971988)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json)

### vs. 3.10.4

- Geometric mean: 1.21x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.10.4.md)
- [📈time plot](bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.02x faster (HPT: reliability of 63.69%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.12.0.md)
- [📈time plot](bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.03x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.13.0b2.md)
- [📈time plot](bm-20240720-pythonperf1-amd64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.13.0b2.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10023971988)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json)

### vs. 3.10.4

- Geometric mean: 1.13x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.10.4.md)
- [📈time plot](bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.14x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.12.0.md)
- [📈time plot](bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.13.0b2.md)
- [📈time plot](bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.13.0b2.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10023971988)
- cpu model: missing
- platform: macOS-14.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20240720-darwin-arm64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json)

### vs. 3.10.4

- Geometric mean: 1.30x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: 0.67x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240720-darwin-arm64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.10.4.md)
- [📈time plot](bm-20240720-darwin-arm64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.09x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 0.58x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240720-darwin-arm64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.12.0.md)
- [📈time plot](bm-20240720-darwin-arm64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x faster (HPT: reliability of 99.01%, 1.00x slower at 99th %ile)
- Memory usage: 0.46x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240720-darwin-arm64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.13.0b2.md)
- [📈time plot](bm-20240720-darwin-arm64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097-vs-3.13.0b2.svg)

