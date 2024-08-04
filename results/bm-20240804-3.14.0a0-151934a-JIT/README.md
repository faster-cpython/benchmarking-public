# Results

- fork: python
- version: 3.14.0a0
- config: JIT
- commit hash: [151934a](https://github.com/python/cpython/commit/151934a)
- commit date: 2024-08-04T00:55:47+03:00
- commit merge base: [95f5c89b545beaafad73f05a695742da3e90bc41](https://github.com/python/cpython/commit/95f5c89b545beaafad73f05a695742da3e90bc41)
- ref: 151934a324789c58cca9

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10231822849)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240804-arminc-aarch64-python-151934a324789c58cca9-3.14.0a0-151934a.json)

### vs. 3.10.4

- Geometric mean: 1.22x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240804-arminc-aarch64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.10.4.md)
- [📈time plot](bm-20240804-arminc-aarch64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.06x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser
- [📄table](bm-20240804-arminc-aarch64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.12.0.md)
- [📈time plot](bm-20240804-arminc-aarch64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.07x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240804-arminc-aarch64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.13.0b2.md)
- [📈time plot](bm-20240804-arminc-aarch64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.09x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: 1.08x
- [🧠memory plot](bm-20240804-arminc-aarch64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-base-mem.svg)
- [📄table](bm-20240804-arminc-aarch64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-base.md)
- [📈time plot](bm-20240804-arminc-aarch64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10231822849)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240804-linux-x86_64-python-151934a324789c58cca9-3.14.0a0-151934a.json)

### vs. 3.10.4

- Geometric mean: 1.43x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240804-linux-x86_64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.10.4.md)
- [📈time plot](bm-20240804-linux-x86_64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 99.98%, 1.01x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240804-linux-x86_64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.12.0.md)
- [📈time plot](bm-20240804-linux-x86_64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x faster (HPT: reliability of 99.97%, 1.01x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240804-linux-x86_64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.13.0b2.md)
- [📈time plot](bm-20240804-linux-x86_64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 63.20%, 1.00x slower at 99th %ile)
- Memory usage: 1.06x
- [🧠memory plot](bm-20240804-linux-x86_64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-base-mem.svg)
- [📄table](bm-20240804-linux-x86_64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-base.md)
- [📈time plot](bm-20240804-linux-x86_64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10231822849)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240804-pythonperf2-x86_64-python-151934a324789c58cca9-3.14.0a0-151934a.json)

### vs. 3.10.4

- Geometric mean: 1.33x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240804-pythonperf2-x86_64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.10.4.md)
- [📈time plot](bm-20240804-pythonperf2-x86_64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.02x faster (HPT: reliability of 72.99%, 1.00x faster at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240804-pythonperf2-x86_64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.12.0.md)
- [📈time plot](bm-20240804-pythonperf2-x86_64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x faster (HPT: reliability of 78.30%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240804-pythonperf2-x86_64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.13.0b2.md)
- [📈time plot](bm-20240804-pythonperf2-x86_64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 51.66%, 1.00x slower at 99th %ile)
- Memory usage: 1.07x
- [🧠memory plot](bm-20240804-pythonperf2-x86_64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-base-mem.svg)
- [📄table](bm-20240804-pythonperf2-x86_64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-base.md)
- [📈time plot](bm-20240804-pythonperf2-x86_64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10231822849)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240804-pythonperf1-amd64-python-151934a324789c58cca9-3.14.0a0-151934a.json)

### vs. 3.10.4

- Geometric mean: 1.25x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240804-pythonperf1-amd64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.10.4.md)
- [📈time plot](bm-20240804-pythonperf1-amd64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.05x faster (HPT: reliability of 92.75%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240804-pythonperf1-amd64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.12.0.md)
- [📈time plot](bm-20240804-pythonperf1-amd64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.00x slower (HPT: reliability of 98.36%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240804-pythonperf1-amd64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.13.0b2.md)
- [📈time plot](bm-20240804-pythonperf1-amd64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.09x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240804-pythonperf1-amd64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-base.md)
- [📈time plot](bm-20240804-pythonperf1-amd64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10231822849)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240804-pythonperf1_win32-x86-python-151934a324789c58cca9-3.14.0a0-151934a.json)

### vs. 3.10.4

- Geometric mean: 1.21x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240804-pythonperf1_win32-x86-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.10.4.md)
- [📈time plot](bm-20240804-pythonperf1_win32-x86-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.22x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240804-pythonperf1_win32-x86-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.12.0.md)
- [📈time plot](bm-20240804-pythonperf1_win32-x86-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.04x faster (HPT: reliability of 98.91%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- new benchmarks: dulwich_log
- [📄table](bm-20240804-pythonperf1_win32-x86-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.13.0b2.md)
- [📈time plot](bm-20240804-pythonperf1_win32-x86-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.09x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240804-pythonperf1_win32-x86-python-151934a324789c58cca9-3.14.0a0-151934a-vs-base.md)
- [📈time plot](bm-20240804-pythonperf1_win32-x86-python-151934a324789c58cca9-3.14.0a0-151934a-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10231822849)
- cpu model: missing
- platform: macOS-14.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20240804-darwin-arm64-python-151934a324789c58cca9-3.14.0a0-151934a.json)

### vs. 3.10.4

- Geometric mean: 1.27x faster (HPT: reliability of 100.00%, 1.15x faster at 99th %ile)
- Memory usage: 0.66x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240804-darwin-arm64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.10.4.md)
- [📈time plot](bm-20240804-darwin-arm64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.06x faster (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- Memory usage: 0.63x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240804-darwin-arm64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.12.0.md)
- [📈time plot](bm-20240804-darwin-arm64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x slower (HPT: reliability of 99.39%, 1.00x slower at 99th %ile)
- Memory usage: 0.51x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240804-darwin-arm64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.13.0b2.md)
- [📈time plot](bm-20240804-darwin-arm64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.02x slower (HPT: reliability of 99.99%, 1.00x slower at 99th %ile)
- Memory usage: 1.10x
- [🧠memory plot](bm-20240804-darwin-arm64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-base-mem.svg)
- [📄table](bm-20240804-darwin-arm64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-base.md)
- [📈time plot](bm-20240804-darwin-arm64-python-151934a324789c58cca9-3.14.0a0-151934a-vs-base.svg)

