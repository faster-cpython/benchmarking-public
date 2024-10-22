# Results

- fork: faster-cpython
- version: 3.14.0a0
- config: 
- commit hash: [1a2b0b8](https://github.com/faster%2dcpython/cpython/commit/1a2b0b8)
- commit date: 2024-07-31T10:50:00+01:00
- commit merge base: [d27a53fc02a87e76066fc4e15ff1fff3922a482d](https://github.com/faster%2dcpython/cpython/commit/d27a53fc02a87e76066fc4e15ff1fff3922a482d)
- ref: experimental_branch_

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10178007028)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240731-arminc-aarch64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8.json)

### vs. 3.10.4

- Geometric mean: 1.33x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240731-arminc-aarch64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-3.10.4.md)
- [📈time plot](bm-20240731-arminc-aarch64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 91.20%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser
- [📄table](bm-20240731-arminc-aarch64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-3.12.0.md)
- [📈time plot](bm-20240731-arminc-aarch64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.01x faster (HPT: reliability of 65.92%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240731-arminc-aarch64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-3.13.0.md)
- [📈time plot](bm-20240731-arminc-aarch64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.01x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240731-arminc-aarch64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-base-mem.svg)
- [📄table](bm-20240731-arminc-aarch64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-base.md)
- [📈time plot](bm-20240731-arminc-aarch64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240731-arminc-aarch64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-3.13.0b2.md)
- [📈time plot](bm-20240731-arminc-aarch64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-3.13.0b2.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10178007028)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240731-linux-x86_64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8.json)

### vs. 3.10.4

- Geometric mean: 1.42x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240731-linux-x86_64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-3.10.4.md)
- [📈time plot](bm-20240731-linux-x86_64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.07x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240731-linux-x86_64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-3.12.0.md)
- [📈time plot](bm-20240731-linux-x86_64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.01x faster (HPT: reliability of 79.41%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240731-linux-x86_64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-3.13.0.md)
- [📈time plot](bm-20240731-linux-x86_64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.01x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240731-linux-x86_64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-base-mem.svg)
- [📄table](bm-20240731-linux-x86_64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-base.md)
- [📈time plot](bm-20240731-linux-x86_64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240731-linux-x86_64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-3.13.0b2.md)
- [📈time plot](bm-20240731-linux-x86_64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-3.13.0b2.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10178007028)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240731-pythonperf2-x86_64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8.json)

### vs. 3.10.4

- Geometric mean: 1.34x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240731-pythonperf2-x86_64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-3.10.4.md)
- [📈time plot](bm-20240731-pythonperf2-x86_64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.02x faster (HPT: reliability of 50.89%, 1.00x slower at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240731-pythonperf2-x86_64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-3.12.0.md)
- [📈time plot](bm-20240731-pythonperf2-x86_64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.02x faster (HPT: reliability of 95.19%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240731-pythonperf2-x86_64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-3.13.0.md)
- [📈time plot](bm-20240731-pythonperf2-x86_64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.01x slower (HPT: reliability of 99.99%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240731-pythonperf2-x86_64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-base-mem.svg)
- [📄table](bm-20240731-pythonperf2-x86_64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-base.md)
- [📈time plot](bm-20240731-pythonperf2-x86_64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240731-pythonperf2-x86_64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-3.13.0b2.md)
- [📈time plot](bm-20240731-pythonperf2-x86_64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-3.13.0b2.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10178007028)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240731-pythonperf1-amd64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8.json)

### vs. 3.10.4

- Geometric mean: 1.16x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240731-pythonperf1-amd64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-3.10.4.md)
- [📈time plot](bm-20240731-pythonperf1-amd64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.02x slower (HPT: reliability of 99.99%, 1.02x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240731-pythonperf1-amd64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-3.12.0.md)
- [📈time plot](bm-20240731-pythonperf1-amd64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.07x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240731-pythonperf1-amd64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-3.13.0.md)
- [📈time plot](bm-20240731-pythonperf1-amd64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 90.81%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240731-pythonperf1-amd64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-base.md)
- [📈time plot](bm-20240731-pythonperf1-amd64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240731-pythonperf1-amd64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-3.13.0b2.md)
- [📈time plot](bm-20240731-pythonperf1-amd64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-3.13.0b2.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10178007028)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240731-pythonperf1_win32-x86-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8.json)

### vs. 3.10.4

- Geometric mean: 1.11x faster (HPT: reliability of 99.96%, 1.01x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240731-pythonperf1_win32-x86-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-3.10.4.md)
- [📈time plot](bm-20240731-pythonperf1_win32-x86-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.12x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240731-pythonperf1_win32-x86-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-3.12.0.md)
- [📈time plot](bm-20240731-pythonperf1_win32-x86-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.01x faster (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240731-pythonperf1_win32-x86-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-3.13.0.md)
- [📈time plot](bm-20240731-pythonperf1_win32-x86-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.03x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240731-pythonperf1_win32-x86-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-base.md)
- [📈time plot](bm-20240731-pythonperf1_win32-x86-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240731-pythonperf1_win32-x86-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-3.13.0b2.md)
- [📈time plot](bm-20240731-pythonperf1_win32-x86-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-3.13.0b2.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10178007028)
- cpu model: missing
- platform: macOS-14.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20240731-darwin-arm64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8.json)

### vs. 3.10.4

- Geometric mean: 1.29x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240731-darwin-arm64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-3.10.4.md)
- [📈time plot](bm-20240731-darwin-arm64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 0.75x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240731-darwin-arm64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-3.12.0.md)
- [📈time plot](bm-20240731-darwin-arm64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240731-darwin-arm64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-3.13.0.md)
- [📈time plot](bm-20240731-darwin-arm64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240731-darwin-arm64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-base-mem.svg)
- [📄table](bm-20240731-darwin-arm64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-base.md)
- [📈time plot](bm-20240731-darwin-arm64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240731-darwin-arm64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-3.13.0b2.md)
- [📈time plot](bm-20240731-darwin-arm64-faster%252dcpython-experimental_branch_-3.14.0a0-1a2b0b8-vs-3.13.0b2.svg)

