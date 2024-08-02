# Results

- fork: faster-cpython
- version: 3.14.0a0
- config: 
- commit hash: [5787d3e](https://github.com/faster%2dcpython/cpython/commit/5787d3e)
- commit date: 2024-07-23T14:32:51+01:00
- commit merge base: [2c1b1e7a07eba0138b9858c6f2bea3cae9af0808](https://github.com/faster%2dcpython/cpython/commit/2c1b1e7a07eba0138b9858c6f2bea3cae9af0808)
- ref: bound_method_instrum

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10060196265)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240723-arminc-aarch64-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e.json)

### vs. 3.10.4

- Geometric mean: 1.34x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240723-arminc-aarch64-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e-vs-3.10.4.md)
- [📈time plot](bm-20240723-arminc-aarch64-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.04x faster (HPT: reliability of 94.45%, 1.00x faster at 99th %ile)
- Memory usage: 0.92x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser
- [📄table](bm-20240723-arminc-aarch64-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e-vs-3.12.0.md)
- [📈time plot](bm-20240723-arminc-aarch64-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x faster (HPT: reliability of 98.87%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240723-arminc-aarch64-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e-vs-3.13.0b2.md)
- [📈time plot](bm-20240723-arminc-aarch64-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 65.05%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240723-arminc-aarch64-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e-vs-base-mem.svg)
- [📄table](bm-20240723-arminc-aarch64-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e-vs-base.md)
- [📈time plot](bm-20240723-arminc-aarch64-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10060196265)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240723-linux-x86_64-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e.json)

### vs. 3.10.4

- Geometric mean: 1.44x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240723-linux-x86_64-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e-vs-3.10.4.md)
- [📈time plot](bm-20240723-linux-x86_64-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.09x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240723-linux-x86_64-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e-vs-3.12.0.md)
- [📈time plot](bm-20240723-linux-x86_64-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.06x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240723-linux-x86_64-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e-vs-3.13.0b2.md)
- [📈time plot](bm-20240723-linux-x86_64-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 99.09%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240723-linux-x86_64-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e-vs-base-mem.svg)
- [📄table](bm-20240723-linux-x86_64-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e-vs-base.md)
- [📈time plot](bm-20240723-linux-x86_64-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10060196265)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240723-pythonperf2-x86_64-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e.json)

### vs. 3.10.4

- Geometric mean: 1.34x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240723-pythonperf2-x86_64-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e-vs-3.10.4.md)
- [📈time plot](bm-20240723-pythonperf2-x86_64-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.02x faster (HPT: reliability of 69.76%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240723-pythonperf2-x86_64-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e-vs-3.12.0.md)
- [📈time plot](bm-20240723-pythonperf2-x86_64-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x faster (HPT: reliability of 99.87%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240723-pythonperf2-x86_64-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e-vs-3.13.0b2.md)
- [📈time plot](bm-20240723-pythonperf2-x86_64-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 98.85%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240723-pythonperf2-x86_64-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e-vs-base-mem.svg)
- [📄table](bm-20240723-pythonperf2-x86_64-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e-vs-base.md)
- [📈time plot](bm-20240723-pythonperf2-x86_64-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10060196265)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240723-pythonperf1-amd64-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e.json)

### vs. 3.10.4

- Geometric mean: 1.19x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240723-pythonperf1-amd64-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e-vs-3.10.4.md)
- [📈time plot](bm-20240723-pythonperf1-amd64-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.00x slower (HPT: reliability of 97.88%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240723-pythonperf1-amd64-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e-vs-3.12.0.md)
- [📈time plot](bm-20240723-pythonperf1-amd64-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240723-pythonperf1-amd64-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e-vs-3.13.0b2.md)
- [📈time plot](bm-20240723-pythonperf1-amd64-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.04x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240723-pythonperf1-amd64-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e-vs-base.md)
- [📈time plot](bm-20240723-pythonperf1-amd64-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10060196265)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240723-pythonperf1_win32-x86-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e.json)

### vs. 3.10.4

- Geometric mean: 1.13x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240723-pythonperf1_win32-x86-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e-vs-3.10.4.md)
- [📈time plot](bm-20240723-pythonperf1_win32-x86-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.15x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240723-pythonperf1_win32-x86-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e-vs-3.12.0.md)
- [📈time plot](bm-20240723-pythonperf1_win32-x86-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240723-pythonperf1_win32-x86-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e-vs-3.13.0b2.md)
- [📈time plot](bm-20240723-pythonperf1_win32-x86-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e-vs-3.13.0b2.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10060196265)
- cpu model: missing
- platform: macOS-14.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20240723-darwin-arm64-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e.json)

### vs. 3.10.4

- Geometric mean: 1.31x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 0.85x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240723-darwin-arm64-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e-vs-3.10.4.md)
- [📈time plot](bm-20240723-darwin-arm64-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.09x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.66x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240723-darwin-arm64-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e-vs-3.12.0.md)
- [📈time plot](bm-20240723-darwin-arm64-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x faster (HPT: reliability of 79.35%, 1.00x slower at 99th %ile)
- Memory usage: 0.62x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240723-darwin-arm64-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e-vs-3.13.0b2.md)
- [📈time plot](bm-20240723-darwin-arm64-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240723-darwin-arm64-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e-vs-base-mem.svg)
- [📄table](bm-20240723-darwin-arm64-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e-vs-base.md)
- [📈time plot](bm-20240723-darwin-arm64-faster%252dcpython-bound_method_instrum-3.14.0a0-5787d3e-vs-base.svg)

