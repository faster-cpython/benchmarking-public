# Results

- fork: python
- version: 3.14.0a0
- config: 
- commit hash: [22b0de2](https://github.com/python/cpython/commit/22b0de2)
- commit date: 2024-06-27T03:10:43+08:00
- commit merge base: [d611c4c8e9893c0816969e19ab6ca4992a3a15e3](https://github.com/python/cpython/commit/d611c4c8e9893c0816969e19ab6ca4992a3a15e3)
- ref: 22b0de2755ee2d0e2dd2

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9749749417)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240627-arminc-aarch64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2.json)

### vs. 3.10.4

- Geometric mean: 1.33x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240627-arminc-aarch64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2-vs-3.10.4.md)
- [📈time plot](bm-20240627-arminc-aarch64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 87.20%, 1.00x faster at 99th %ile)
- Memory usage: 0.92x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser
- [📄table](bm-20240627-arminc-aarch64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2-vs-3.12.0.md)
- [📈time plot](bm-20240627-arminc-aarch64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x faster (HPT: reliability of 64.44%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240627-arminc-aarch64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2-vs-3.13.0b2.md)
- [📈time plot](bm-20240627-arminc-aarch64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 99.67%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240627-arminc-aarch64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2-vs-base-mem.svg)
- [📄table](bm-20240627-arminc-aarch64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2-vs-base.md)
- [📈time plot](bm-20240627-arminc-aarch64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9749775420)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240627-linux-x86_64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2.json)

### vs. 3.10.4

- Geometric mean: 1.42x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240627-linux-x86_64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2-vs-3.10.4.md)
- [📈time plot](bm-20240627-linux-x86_64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240627-linux-x86_64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2-vs-3.12.0.md)
- [📈time plot](bm-20240627-linux-x86_64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240627-linux-x86_64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2-vs-3.13.0b2.md)
- [📈time plot](bm-20240627-linux-x86_64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240627-linux-x86_64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2-vs-base-mem.svg)
- [📄table](bm-20240627-linux-x86_64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2-vs-base.md)
- [📈time plot](bm-20240627-linux-x86_64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9748134543)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240627-pythonperf1-amd64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2.json)

### vs. 3.10.4

- Geometric mean: 1.17x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240627-pythonperf1-amd64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2-vs-3.10.4.md)
- [📈time plot](bm-20240627-pythonperf1-amd64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.01x slower (HPT: reliability of 98.97%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240627-pythonperf1-amd64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2-vs-3.12.0.md)
- [📈time plot](bm-20240627-pythonperf1-amd64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.06x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240627-pythonperf1-amd64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2-vs-3.13.0b2.md)
- [📈time plot](bm-20240627-pythonperf1-amd64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.11x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240627-pythonperf1-amd64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2-vs-base.md)
- [📈time plot](bm-20240627-pythonperf1-amd64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9753134569)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240627-pythonperf1_win32-x86-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2.json)

### vs. 3.10.4

- Geometric mean: 1.07x faster (HPT: reliability of 96.49%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240627-pythonperf1_win32-x86-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2-vs-3.10.4.md)
- [📈time plot](bm-20240627-pythonperf1_win32-x86-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240627-pythonperf1_win32-x86-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2-vs-3.12.0.md)
- [📈time plot](bm-20240627-pythonperf1_win32-x86-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.08x slower (HPT: reliability of 100.00%, 1.08x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240627-pythonperf1_win32-x86-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2-vs-3.13.0b2.md)
- [📈time plot](bm-20240627-pythonperf1_win32-x86-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.08x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240627-pythonperf1_win32-x86-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2-vs-base.md)
- [📈time plot](bm-20240627-pythonperf1_win32-x86-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9749953752)
- cpu model: missing
- platform: macOS-14.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20240627-darwin-arm64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2.json)

### vs. 3.10.4

- Geometric mean: 1.28x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240627-darwin-arm64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2-vs-3.10.4.md)
- [📈time plot](bm-20240627-darwin-arm64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.07x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240627-darwin-arm64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2-vs-3.12.0.md)
- [📈time plot](bm-20240627-darwin-arm64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x slower (HPT: reliability of 99.99%, 1.00x slower at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240627-darwin-arm64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2-vs-3.13.0b2.md)
- [📈time plot](bm-20240627-darwin-arm64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240627-darwin-arm64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2-vs-base-mem.svg)
- [📄table](bm-20240627-darwin-arm64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2-vs-base.md)
- [📈time plot](bm-20240627-darwin-arm64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2-vs-base.svg)

