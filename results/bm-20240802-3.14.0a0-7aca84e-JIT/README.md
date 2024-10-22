# Results

- fork: python
- version: 3.14.0a0
- config: JIT
- commit hash: [7aca84e](https://github.com/python/cpython/commit/7aca84e)
- commit date: 2024-08-02T16:31:17+01:00
- commit merge base: [498376d7a7d6f704f22a2c963130cc15c17e7a6f](https://github.com/python/cpython/commit/498376d7a7d6f704f22a2c963130cc15c17e7a6f)
- ref: 7aca84e557d0a6d242f3

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10218493151)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json)

### vs. 3.10.4

- Geometric mean: 1.22x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-3.10.4.md)
- [📈time plot](bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.06x slower (HPT: reliability of 99.99%, 1.02x slower at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser
- [📄table](bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-3.12.0.md)
- [📈time plot](bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.08x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-3.13.0.md)
- [📈time plot](bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 99.96%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-base-mem.svg)
- [📄table](bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-base.md)
- [📈time plot](bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-3.13.0b2.md)
- [📈time plot](bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-3.13.0b2.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10218493151)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240802-linux-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json)

### vs. 3.10.4

- Geometric mean: 1.43x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240802-linux-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-3.10.4.md)
- [📈time plot](bm-20240802-linux-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240802-linux-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-3.12.0.md)
- [📈time plot](bm-20240802-linux-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.01x faster (HPT: reliability of 65.43%, 1.00x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240802-linux-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-3.13.0.md)
- [📈time plot](bm-20240802-linux-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 98.18%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240802-linux-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-base-mem.svg)
- [📄table](bm-20240802-linux-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-base.md)
- [📈time plot](bm-20240802-linux-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240802-linux-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-3.13.0b2.md)
- [📈time plot](bm-20240802-linux-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-3.13.0b2.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10218493151)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json)

### vs. 3.10.4

- Geometric mean: 1.33x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-3.10.4.md)
- [📈time plot](bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.02x faster (HPT: reliability of 65.76%, 1.00x faster at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-3.12.0.md)
- [📈time plot](bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.01x faster (HPT: reliability of 64.93%, 1.00x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-3.13.0.md)
- [📈time plot](bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.01x slower (HPT: reliability of 73.82%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-base-mem.svg)
- [📄table](bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-base.md)
- [📈time plot](bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-3.13.0b2.md)
- [📈time plot](bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-3.13.0b2.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10218493151)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json)

### vs. 3.10.4

- Geometric mean: 1.24x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-3.10.4.md)
- [📈time plot](bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.05x faster (HPT: reliability of 94.76%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-3.12.0.md)
- [📈time plot](bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.00x faster (HPT: reliability of 99.16%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-3.13.0.md)
- [📈time plot](bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.01x slower (HPT: reliability of 99.97%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-base.md)
- [📈time plot](bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-3.13.0b2.md)
- [📈time plot](bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-3.13.0b2.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10218493151)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json)

### vs. 3.10.4

- Geometric mean: 1.20x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-3.10.4.md)
- [📈time plot](bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.22x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-3.12.0.md)
- [📈time plot](bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.10x faster (HPT: reliability of 89.10%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-3.13.0.md)
- [📈time plot](bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 98.68%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-base.md)
- [📈time plot](bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-3.13.0b2.md)
- [📈time plot](bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-3.13.0b2.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10218493151)
- cpu model: missing
- platform: macOS-14.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json)

### vs. 3.10.4

- Geometric mean: 1.27x faster (HPT: reliability of 100.00%, 1.15x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-3.10.4.md)
- [📈time plot](bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.07x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 0.85x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-3.12.0.md)
- [📈time plot](bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.07x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-3.13.0.md)
- [📈time plot](bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 65.70%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-base-mem.svg)
- [📄table](bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-base.md)
- [📈time plot](bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-3.13.0b2.md)
- [📈time plot](bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e-vs-3.13.0b2.svg)

