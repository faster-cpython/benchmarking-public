# Results

- fork: python
- version: 3.14.0a0
- config: JIT
- commit hash: [5f60011](https://github.com/python/cpython/commit/5f60011)
- commit date: 2024-07-25T10:45:28-07:00
- commit merge base: [5e686ff57d6bc2fd8c675bd2c59a064be6da2839](https://github.com/python/cpython/commit/5e686ff57d6bc2fd8c675bd2c59a064be6da2839)
- ref: 5f6001130f8ada871193

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10238223182)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240725-arminc-aarch64-python-5f6001130f8ada871193-3.14.0a0-5f60011.json)

### vs. 3.10.4

- Geometric mean: 1.23x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240725-arminc-aarch64-python-5f6001130f8ada871193-3.14.0a0-5f60011-vs-3.10.4.md)
- [📈time plot](bm-20240725-arminc-aarch64-python-5f6001130f8ada871193-3.14.0a0-5f60011-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.05x slower (HPT: reliability of 99.99%, 1.02x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser
- [📄table](bm-20240725-arminc-aarch64-python-5f6001130f8ada871193-3.14.0a0-5f60011-vs-3.12.0.md)
- [📈time plot](bm-20240725-arminc-aarch64-python-5f6001130f8ada871193-3.14.0a0-5f60011-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.07x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240725-arminc-aarch64-python-5f6001130f8ada871193-3.14.0a0-5f60011-vs-3.13.0.md)
- [📈time plot](bm-20240725-arminc-aarch64-python-5f6001130f8ada871193-3.14.0a0-5f60011-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20240725-arminc-aarch64-python-5f6001130f8ada871193-3.14.0a0-5f60011-vs-3.13.0b2.md)
- [📈time plot](bm-20240725-arminc-aarch64-python-5f6001130f8ada871193-3.14.0a0-5f60011-vs-3.13.0b2.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20240725-azure-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011-pystats.json)
- [pystats table](bm-20240725-azure-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10238223182)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011.json)

### vs. 3.10.4

- Geometric mean: 1.43x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011-vs-3.10.4.md)
- [📈time plot](bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.09x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011-vs-3.12.0.md)
- [📈time plot](bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.02x faster (HPT: reliability of 79.28%, 1.00x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011-vs-3.13.0.md)
- [📈time plot](bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011-vs-3.13.0b2.md)
- [📈time plot](bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011-vs-3.13.0b2.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10238223182)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240725-pythonperf2-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011.json)

### vs. 3.10.4

- Geometric mean: 1.33x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240725-pythonperf2-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011-vs-3.10.4.md)
- [📈time plot](bm-20240725-pythonperf2-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.01x faster (HPT: reliability of 59.35%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240725-pythonperf2-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011-vs-3.12.0.md)
- [📈time plot](bm-20240725-pythonperf2-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.01x faster (HPT: reliability of 74.40%, 1.00x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240725-pythonperf2-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011-vs-3.13.0.md)
- [📈time plot](bm-20240725-pythonperf2-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20240725-pythonperf2-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011-vs-3.13.0b2.md)
- [📈time plot](bm-20240725-pythonperf2-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011-vs-3.13.0b2.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10238223182)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240725-pythonperf1-amd64-python-5f6001130f8ada871193-3.14.0a0-5f60011.json)

### vs. 3.10.4

- Geometric mean: 1.26x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240725-pythonperf1-amd64-python-5f6001130f8ada871193-3.14.0a0-5f60011-vs-3.10.4.md)
- [📈time plot](bm-20240725-pythonperf1-amd64-python-5f6001130f8ada871193-3.14.0a0-5f60011-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.06x faster (HPT: reliability of 97.48%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240725-pythonperf1-amd64-python-5f6001130f8ada871193-3.14.0a0-5f60011-vs-3.12.0.md)
- [📈time plot](bm-20240725-pythonperf1-amd64-python-5f6001130f8ada871193-3.14.0a0-5f60011-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.02x faster (HPT: reliability of 98.37%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240725-pythonperf1-amd64-python-5f6001130f8ada871193-3.14.0a0-5f60011-vs-3.13.0.md)
- [📈time plot](bm-20240725-pythonperf1-amd64-python-5f6001130f8ada871193-3.14.0a0-5f60011-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20240725-pythonperf1-amd64-python-5f6001130f8ada871193-3.14.0a0-5f60011-vs-3.13.0b2.md)
- [📈time plot](bm-20240725-pythonperf1-amd64-python-5f6001130f8ada871193-3.14.0a0-5f60011-vs-3.13.0b2.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10238223182)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240725-pythonperf1_win32-x86-python-5f6001130f8ada871193-3.14.0a0-5f60011.json)

### vs. 3.10.4

- Geometric mean: 1.20x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240725-pythonperf1_win32-x86-python-5f6001130f8ada871193-3.14.0a0-5f60011-vs-3.10.4.md)
- [📈time plot](bm-20240725-pythonperf1_win32-x86-python-5f6001130f8ada871193-3.14.0a0-5f60011-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.22x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240725-pythonperf1_win32-x86-python-5f6001130f8ada871193-3.14.0a0-5f60011-vs-3.12.0.md)
- [📈time plot](bm-20240725-pythonperf1_win32-x86-python-5f6001130f8ada871193-3.14.0a0-5f60011-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.09x faster (HPT: reliability of 90.50%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240725-pythonperf1_win32-x86-python-5f6001130f8ada871193-3.14.0a0-5f60011-vs-3.13.0.md)
- [📈time plot](bm-20240725-pythonperf1_win32-x86-python-5f6001130f8ada871193-3.14.0a0-5f60011-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20240725-pythonperf1_win32-x86-python-5f6001130f8ada871193-3.14.0a0-5f60011-vs-3.13.0b2.md)
- [📈time plot](bm-20240725-pythonperf1_win32-x86-python-5f6001130f8ada871193-3.14.0a0-5f60011-vs-3.13.0b2.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10238223182)
- cpu model: missing
- platform: macOS-14.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20240725-darwin-arm64-python-5f6001130f8ada871193-3.14.0a0-5f60011.json)

### vs. 3.10.4

- Geometric mean: 1.27x faster (HPT: reliability of 100.00%, 1.15x faster at 99th %ile)
- Memory usage: 0.80x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240725-darwin-arm64-python-5f6001130f8ada871193-3.14.0a0-5f60011-vs-3.10.4.md)
- [📈time plot](bm-20240725-darwin-arm64-python-5f6001130f8ada871193-3.14.0a0-5f60011-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.07x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 0.73x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240725-darwin-arm64-python-5f6001130f8ada871193-3.14.0a0-5f60011-vs-3.12.0.md)
- [📈time plot](bm-20240725-darwin-arm64-python-5f6001130f8ada871193-3.14.0a0-5f60011-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.07x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240725-darwin-arm64-python-5f6001130f8ada871193-3.14.0a0-5f60011-vs-3.13.0.md)
- [📈time plot](bm-20240725-darwin-arm64-python-5f6001130f8ada871193-3.14.0a0-5f60011-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20240725-darwin-arm64-python-5f6001130f8ada871193-3.14.0a0-5f60011-vs-3.13.0b2.md)
- [📈time plot](bm-20240725-darwin-arm64-python-5f6001130f8ada871193-3.14.0a0-5f60011-vs-3.13.0b2.svg)

