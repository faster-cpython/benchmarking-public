# Results

- fork: mdboom
- version: 3.14.0a0
- config: 
- commit hash: [c9a5962](https://github.com/mdboom/cpython/commit/c9a5962)
- commit date: 2024-08-29T14:38:36-04:00
- commit merge base: [58ce131037ecb34d506a613f21993cde2056f628](https://github.com/mdboom/cpython/commit/58ce131037ecb34d506a613f21993cde2056f628)
- ref: simplify_richcompare

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10620781194)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962.json)

### vs. 3.10.4

- Geometric mean: 1.35x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-3.10.4.md)
- [📈time plot](bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.04x faster (HPT: reliability of 99.27%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser
- [📄table](bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-3.12.0.md)
- [📈time plot](bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.02x faster (HPT: reliability of 99.93%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-3.13.0.md)
- [📈time plot](bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 78.39%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-base-mem.svg)
- [📄table](bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-base.md)
- [📈time plot](bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-3.13.0b2.md)
- [📈time plot](bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-3.13.0b2.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10620781194)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-192-generic-x86_64-with-glibc2.31
- [raw results](bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962.json)

### vs. 3.10.4

- Geometric mean: 1.45x faster (HPT: reliability of 100.00%, 1.32x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-3.10.4.md)
- [📈time plot](bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.09x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-3.12.0.md)
- [📈time plot](bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.02x faster (HPT: reliability of 99.96%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-3.13.0.md)
- [📈time plot](bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.01x faster (HPT: reliability of 99.66%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-base-mem.svg)
- [📄table](bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-base.md)
- [📈time plot](bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-3.13.0b2.md)
- [📈time plot](bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-3.13.0b2.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10620781194)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962.json)

### vs. 3.10.4

- Geometric mean: 1.36x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-3.10.4.md)
- [📈time plot](bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 96.90%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-3.12.0.md)
- [📈time plot](bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.03x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-3.13.0.md)
- [📈time plot](bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 99.90%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-base-mem.svg)
- [📄table](bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-base.md)
- [📈time plot](bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-3.13.0b2.md)
- [📈time plot](bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-3.13.0b2.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10620781194)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962.json)

### vs. 3.10.4

- Geometric mean: 1.16x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-3.10.4.md)
- [📈time plot](bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.02x slower (HPT: reliability of 99.95%, 1.02x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-3.12.0.md)
- [📈time plot](bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.06x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-3.13.0.md)
- [📈time plot](bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 60.48%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-base.md)
- [📈time plot](bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-3.13.0b2.md)
- [📈time plot](bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-3.13.0b2.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10620781194)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962.json)

### vs. 3.10.4

- Geometric mean: 1.13x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-3.10.4.md)
- [📈time plot](bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.14x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-3.12.0.md)
- [📈time plot](bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.03x faster (HPT: reliability of 99.33%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-3.13.0.md)
- [📈time plot](bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.01x faster (HPT: reliability of 78.06%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-base.md)
- [📈time plot](bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-3.13.0b2.md)
- [📈time plot](bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-3.13.0b2.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10620781194)
- cpu model: missing
- platform: macOS-14.6.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962.json)

### vs. 3.10.4

- Geometric mean: 1.30x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 0.74x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-3.10.4.md)
- [📈time plot](bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.09x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.65x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-3.12.0.md)
- [📈time plot](bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-3.13.0.md)
- [📈time plot](bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 52.79%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-base-mem.svg)
- [📄table](bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-base.md)
- [📈time plot](bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-3.13.0b2.md)
- [📈time plot](bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-c9a5962-vs-3.13.0b2.svg)

