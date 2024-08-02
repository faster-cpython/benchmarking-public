# Results

- fork: python
- version: 3.14.0a0
- config: JIT
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

- Geometric mean: 1.23x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.10.4.md)
- [📈time plot](bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.05x slower (HPT: reliability of 99.99%, 1.01x slower at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser
- [📄table](bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.12.0.md)
- [📈time plot](bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.06x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.13.0b2.md)
- [📈time plot](bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.08x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.09x
- [🧠memory plot](bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-base-mem.svg)
- [📄table](bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-base.md)
- [📈time plot](bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9727767593)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240629-linux-x86_64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json)

### vs. 3.10.4

- Geometric mean: 1.42x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240629-linux-x86_64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.10.4.md)
- [📈time plot](bm-20240629-linux-x86_64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 99.95%, 1.01x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240629-linux-x86_64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.12.0.md)
- [📈time plot](bm-20240629-linux-x86_64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.04x faster (HPT: reliability of 99.93%, 1.00x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240629-linux-x86_64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.13.0b2.md)
- [📈time plot](bm-20240629-linux-x86_64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 93.26%, 1.00x slower at 99th %ile)
- Memory usage: 1.08x
- [🧠memory plot](bm-20240629-linux-x86_64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-base-mem.svg)
- [📄table](bm-20240629-linux-x86_64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-base.md)
- [📈time plot](bm-20240629-linux-x86_64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9727767593)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240629-pythonperf2-x86_64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json)

### vs. 3.10.4

- Geometric mean: 1.32x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240629-pythonperf2-x86_64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.10.4.md)
- [📈time plot](bm-20240629-pythonperf2-x86_64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.01x faster (HPT: reliability of 71.79%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240629-pythonperf2-x86_64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.12.0.md)
- [📈time plot](bm-20240629-pythonperf2-x86_64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.00x faster (HPT: reliability of 64.75%, 1.00x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240629-pythonperf2-x86_64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.13.0b2.md)
- [📈time plot](bm-20240629-pythonperf2-x86_64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.02x slower (HPT: reliability of 99.86%, 1.00x slower at 99th %ile)
- Memory usage: 1.09x
- [🧠memory plot](bm-20240629-pythonperf2-x86_64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-base-mem.svg)
- [📄table](bm-20240629-pythonperf2-x86_64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-base.md)
- [📈time plot](bm-20240629-pythonperf2-x86_64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9727767593)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json)

### vs. 3.10.4

- Geometric mean: 1.23x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.10.4.md)
- [📈time plot](bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.04x faster (HPT: reliability of 89.56%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.12.0.md)
- [📈time plot](bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x slower (HPT: reliability of 99.63%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.13.0b2.md)
- [📈time plot](bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.04x faster (HPT: reliability of 72.66%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-base.md)
- [📈time plot](bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9727767593)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json)

### vs. 3.10.4

- Geometric mean: 1.19x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.10.4.md)
- [📈time plot](bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.20x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.12.0.md)
- [📈time plot](bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x faster (HPT: reliability of 99.48%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.13.0b2.md)
- [📈time plot](bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.10x faster (HPT: reliability of 99.97%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-base.md)
- [📈time plot](bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9727767593)
- cpu model: missing
- platform: macOS-14.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20240629-darwin-arm64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json)

### vs. 3.10.4

- Geometric mean: 1.26x faster (HPT: reliability of 100.00%, 1.15x faster at 99th %ile)
- Memory usage: 1.43x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240629-darwin-arm64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.10.4.md)
- [📈time plot](bm-20240629-darwin-arm64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.06x faster (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240629-darwin-arm64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.12.0.md)
- [📈time plot](bm-20240629-darwin-arm64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x slower (HPT: reliability of 99.82%, 1.00x slower at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240629-darwin-arm64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.13.0b2.md)
- [📈time plot](bm-20240629-darwin-arm64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 99.51%, 1.00x slower at 99th %ile)
- Memory usage: 1.21x
- [🧠memory plot](bm-20240629-darwin-arm64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-base-mem.svg)
- [📄table](bm-20240629-darwin-arm64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-base.md)
- [📈time plot](bm-20240629-darwin-arm64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8-vs-base.svg)

