# Results

- fork: brandtbucher
- version: 3.14.0a0
- config: JIT
- commit hash: [bbb07e8](https://github.com/brandtbucher/cpython/commit/bbb07e8)
- commit date: 2024-07-13T17:04:11-07:00
- commit merge base: [006b53a42f72be83ecdfc39f3603cdd66bfcdc45](https://github.com/brandtbucher/cpython/commit/006b53a42f72be83ecdfc39f3603cdd66bfcdc45)
- ref: tier_two_improvement

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9933136383)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240713-arminc-aarch64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8.json)

### vs. 3.10.4

- Geometric mean: 1.23x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.23x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240713-arminc-aarch64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-3.10.4.md)
- [📈time plot](bm-20240713-arminc-aarch64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.05x slower (HPT: reliability of 99.99%, 1.02x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser
- [📄table](bm-20240713-arminc-aarch64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-3.12.0.md)
- [📈time plot](bm-20240713-arminc-aarch64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.07x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: dulwich_log
- [📄table](bm-20240713-arminc-aarch64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-3.13.0.md)
- [📈time plot](bm-20240713-arminc-aarch64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 99.83%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240713-arminc-aarch64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-base-mem.svg)
- [📄table](bm-20240713-arminc-aarch64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-base.md)
- [📈time plot](bm-20240713-arminc-aarch64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240713-arminc-aarch64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-3.13.0b2.md)
- [📈time plot](bm-20240713-arminc-aarch64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-3.13.0b2.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20240713-azure-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-pystats.json)
- [pystats table](bm-20240713-azure-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-pystats.md)

### vs. base

- [pystats diff](bm-20240713-azure-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9933136383)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8.json)

### vs. 3.10.4

- Geometric mean: 1.43x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-3.10.4.md)
- [📈time plot](bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-3.12.0.md)
- [📈time plot](bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.01x faster (HPT: reliability of 71.03%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-3.13.0.md)
- [📈time plot](bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.01x faster (HPT: reliability of 99.75%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-base-mem.svg)
- [📄table](bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-base.md)
- [📈time plot](bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-3.13.0b2.md)
- [📈time plot](bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-3.13.0b2.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9933136383)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8.json)

### vs. 3.10.4

- Geometric mean: 1.33x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-3.10.4.md)
- [📈time plot](bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.02x faster (HPT: reliability of 84.53%, 1.00x faster at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-3.12.0.md)
- [📈time plot](bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.01x faster (HPT: reliability of 76.31%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-3.13.0.md)
- [📈time plot](bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 96.47%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-base-mem.svg)
- [📄table](bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-base.md)
- [📈time plot](bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-3.13.0b2.md)
- [📈time plot](bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-3.13.0b2.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9933136383)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240713-pythonperf1-amd64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8.json)

### vs. 3.10.4

- Geometric mean: 1.27x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240713-pythonperf1-amd64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-3.10.4.md)
- [📈time plot](bm-20240713-pythonperf1-amd64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.07x faster (HPT: reliability of 98.01%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240713-pythonperf1-amd64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-3.12.0.md)
- [📈time plot](bm-20240713-pythonperf1-amd64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.03x faster (HPT: reliability of 73.67%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240713-pythonperf1-amd64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-3.13.0.md)
- [📈time plot](bm-20240713-pythonperf1-amd64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 74.13%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240713-pythonperf1-amd64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-base.md)
- [📈time plot](bm-20240713-pythonperf1-amd64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240713-pythonperf1-amd64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-3.13.0b2.md)
- [📈time plot](bm-20240713-pythonperf1-amd64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-3.13.0b2.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9933136383)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8.json)

### vs. 3.10.4

- Geometric mean: 1.22x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-3.10.4.md)
- [📈time plot](bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.24x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-3.12.0.md)
- [📈time plot](bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.11x faster (HPT: reliability of 99.86%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, dulwich_log, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-3.13.0.md)
- [📈time plot](bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 95.47%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-base.md)
- [📈time plot](bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-3.13.0b2.md)
- [📈time plot](bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-3.13.0b2.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9933136383)
- cpu model: missing
- platform: macOS-14.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20240713-darwin-arm64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8.json)

### vs. 3.10.4

- Geometric mean: 1.27x faster (HPT: reliability of 100.00%, 1.15x faster at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240713-darwin-arm64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-3.10.4.md)
- [📈time plot](bm-20240713-darwin-arm64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.06x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240713-darwin-arm64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-3.12.0.md)
- [📈time plot](bm-20240713-darwin-arm64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.06x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 6.32x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240713-darwin-arm64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-3.13.0.md)
- [📈time plot](bm-20240713-darwin-arm64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 79.55%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240713-darwin-arm64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-base-mem.svg)
- [📄table](bm-20240713-darwin-arm64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-base.md)
- [📈time plot](bm-20240713-darwin-arm64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240713-darwin-arm64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-3.13.0b2.md)
- [📈time plot](bm-20240713-darwin-arm64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8-vs-3.13.0b2.svg)

