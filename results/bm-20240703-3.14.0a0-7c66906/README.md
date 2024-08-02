# Results

- fork: python
- version: 3.14.0a0
- config: 
- commit hash: [7c66906](https://github.com/python/cpython/commit/7c66906)
- commit date: 2024-07-03T20:33:56+05:30
- commit merge base: [ca2e8765009d0d3eb9fe6c75465825c50808f4dd](https://github.com/python/cpython/commit/ca2e8765009d0d3eb9fe6c75465825c50808f4dd)
- ref: main

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9781018205)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240703-arminc-aarch64-python-main-3.14.0a0-7c66906.json)

### vs. 3.10.4

- Geometric mean: 1.33x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240703-arminc-aarch64-python-main-3.14.0a0-7c66906-vs-3.10.4.md)
- [📈time plot](bm-20240703-arminc-aarch64-python-main-3.14.0a0-7c66906-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 83.69%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser
- [📄table](bm-20240703-arminc-aarch64-python-main-3.14.0a0-7c66906-vs-3.12.0.md)
- [📈time plot](bm-20240703-arminc-aarch64-python-main-3.14.0a0-7c66906-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x faster (HPT: reliability of 58.34%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240703-arminc-aarch64-python-main-3.14.0a0-7c66906-vs-3.13.0b2.md)
- [📈time plot](bm-20240703-arminc-aarch64-python-main-3.14.0a0-7c66906-vs-3.13.0b2.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9781018205)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240703-linux-x86_64-python-main-3.14.0a0-7c66906.json)

### vs. 3.10.4

- Geometric mean: 1.43x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240703-linux-x86_64-python-main-3.14.0a0-7c66906-vs-3.10.4.md)
- [📈time plot](bm-20240703-linux-x86_64-python-main-3.14.0a0-7c66906-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.09x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240703-linux-x86_64-python-main-3.14.0a0-7c66906-vs-3.12.0.md)
- [📈time plot](bm-20240703-linux-x86_64-python-main-3.14.0a0-7c66906-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240703-linux-x86_64-python-main-3.14.0a0-7c66906-vs-3.13.0b2.md)
- [📈time plot](bm-20240703-linux-x86_64-python-main-3.14.0a0-7c66906-vs-3.13.0b2.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9781018205)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240703-pythonperf2-x86_64-python-main-3.14.0a0-7c66906.json)

### vs. 3.10.4

- Geometric mean: 1.34x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240703-pythonperf2-x86_64-python-main-3.14.0a0-7c66906-vs-3.10.4.md)
- [📈time plot](bm-20240703-pythonperf2-x86_64-python-main-3.14.0a0-7c66906-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.02x faster (HPT: reliability of 58.80%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240703-pythonperf2-x86_64-python-main-3.14.0a0-7c66906-vs-3.12.0.md)
- [📈time plot](bm-20240703-pythonperf2-x86_64-python-main-3.14.0a0-7c66906-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x faster (HPT: reliability of 90.09%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240703-pythonperf2-x86_64-python-main-3.14.0a0-7c66906-vs-3.13.0b2.md)
- [📈time plot](bm-20240703-pythonperf2-x86_64-python-main-3.14.0a0-7c66906-vs-3.13.0b2.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9781018205)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240703-pythonperf1_win32-x86-python-main-3.14.0a0-7c66906.json)

### vs. 3.10.4

- Geometric mean: 1.15x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240703-pythonperf1_win32-x86-python-main-3.14.0a0-7c66906-vs-3.10.4.md)
- [📈time plot](bm-20240703-pythonperf1_win32-x86-python-main-3.14.0a0-7c66906-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.16x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240703-pythonperf1_win32-x86-python-main-3.14.0a0-7c66906-vs-3.12.0.md)
- [📈time plot](bm-20240703-pythonperf1_win32-x86-python-main-3.14.0a0-7c66906-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240703-pythonperf1_win32-x86-python-main-3.14.0a0-7c66906-vs-3.13.0b2.md)
- [📈time plot](bm-20240703-pythonperf1_win32-x86-python-main-3.14.0a0-7c66906-vs-3.13.0b2.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9781018205)
- cpu model: missing
- platform: macOS-14.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20240703-darwin-arm64-python-main-3.14.0a0-7c66906.json)

### vs. 3.10.4

- Geometric mean: 1.26x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240703-darwin-arm64-python-main-3.14.0a0-7c66906-vs-3.10.4.md)
- [📈time plot](bm-20240703-darwin-arm64-python-main-3.14.0a0-7c66906-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.05x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240703-darwin-arm64-python-main-3.14.0a0-7c66906-vs-3.12.0.md)
- [📈time plot](bm-20240703-darwin-arm64-python-main-3.14.0a0-7c66906-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x slower (HPT: reliability of 99.99%, 1.00x slower at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240703-darwin-arm64-python-main-3.14.0a0-7c66906-vs-3.13.0b2.md)
- [📈time plot](bm-20240703-darwin-arm64-python-main-3.14.0a0-7c66906-vs-3.13.0b2.svg)

