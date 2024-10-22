# Results

- fork: brandtbucher
- version: 3.14.0a0
- config: JIT
- commit hash: [60b7e71](https://github.com/brandtbucher/cpython/commit/60b7e71)
- commit date: 2024-07-27T08:47:31-07:00
- commit merge base: [5f6001130f8ada871193377954cfcfee01ef93b6](https://github.com/brandtbucher/cpython/commit/5f6001130f8ada871193377954cfcfee01ef93b6)
- ref: faster_jit_builds

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10238223182)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71.json)

### vs. 3.10.4

- Geometric mean: 1.22x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-3.10.4.md)
- [📈time plot](bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.05x slower (HPT: reliability of 99.98%, 1.02x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser
- [📄table](bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-3.12.0.md)
- [📈time plot](bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.07x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-3.13.0.md)
- [📈time plot](bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 81.26%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-base-mem.svg)
- [📄table](bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-base.md)
- [📈time plot](bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-3.13.0b2.md)
- [📈time plot](bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-3.13.0b2.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20240727-azure-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-pystats.json)

### vs. base

- [pystats diff](bm-20240727-azure-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10238223182)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71.json)

### vs. 3.10.4

- Geometric mean: 1.42x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-3.10.4.md)
- [📈time plot](bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-3.12.0.md)
- [📈time plot](bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.01x faster (HPT: reliability of 54.79%, 1.00x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-3.13.0.md)
- [📈time plot](bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.01x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-base-mem.svg)
- [📄table](bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-base.md)
- [📈time plot](bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-3.13.0b2.md)
- [📈time plot](bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-3.13.0b2.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10238223182)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240727-pythonperf2-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71.json)

### vs. 3.10.4

- Geometric mean: 1.33x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240727-pythonperf2-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-3.10.4.md)
- [📈time plot](bm-20240727-pythonperf2-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.02x faster (HPT: reliability of 85.16%, 1.00x faster at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240727-pythonperf2-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-3.12.0.md)
- [📈time plot](bm-20240727-pythonperf2-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.01x faster (HPT: reliability of 79.15%, 1.00x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240727-pythonperf2-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-3.13.0.md)
- [📈time plot](bm-20240727-pythonperf2-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 99.59%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240727-pythonperf2-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-base-mem.svg)
- [📄table](bm-20240727-pythonperf2-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-base.md)
- [📈time plot](bm-20240727-pythonperf2-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240727-pythonperf2-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-3.13.0b2.md)
- [📈time plot](bm-20240727-pythonperf2-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-3.13.0b2.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10238223182)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71.json)

### vs. 3.10.4

- Geometric mean: 1.26x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-3.10.4.md)
- [📈time plot](bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.07x faster (HPT: reliability of 96.07%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-3.12.0.md)
- [📈time plot](bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.02x faster (HPT: reliability of 97.89%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-3.13.0.md)
- [📈time plot](bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 52.67%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-base.md)
- [📈time plot](bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-3.13.0b2.md)
- [📈time plot](bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-3.13.0b2.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10238223182)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71.json)

### vs. 3.10.4

- Geometric mean: 1.21x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-3.10.4.md)
- [📈time plot](bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.22x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-3.12.0.md)
- [📈time plot](bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.10x faster (HPT: reliability of 98.65%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-3.13.0.md)
- [📈time plot](bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.01x faster (HPT: reliability of 99.64%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-base.md)
- [📈time plot](bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-3.13.0b2.md)
- [📈time plot](bm-20240727-pythonperf1_win32-x86-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-3.13.0b2.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10238223182)
- cpu model: missing
- platform: macOS-14.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71.json)

### vs. 3.10.4

- Geometric mean: 1.27x faster (HPT: reliability of 100.00%, 1.15x faster at 99th %ile)
- Memory usage: 0.64x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-3.10.4.md)
- [📈time plot](bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.07x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 0.52x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-3.12.0.md)
- [📈time plot](bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.07x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-3.13.0.md)
- [📈time plot](bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 98.30%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-base-mem.svg)
- [📄table](bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-base.md)
- [📈time plot](bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-3.13.0b2.md)
- [📈time plot](bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71-vs-3.13.0b2.svg)

