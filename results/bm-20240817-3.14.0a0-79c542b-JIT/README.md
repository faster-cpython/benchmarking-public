# Results

- fork: python
- version: 3.14.0a0
- config: JIT
- commit hash: [79c542b](https://github.com/python/cpython/commit/79c542b)
- commit date: 2024-08-17T20:58:06+00:00
- commit merge base: [d061ffea7b408861d0a9d311e92c363da284971d](https://github.com/python/cpython/commit/d061ffea7b408861d0a9d311e92c363da284971d)
- ref: 79c542b5cc774ba758ac

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10436129942)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json)

### vs. 3.10.4

- Geometric mean: 1.20x faster (HPT: reliability of 99.99%, 1.04x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.10.4.md)
- [📈time plot](bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.07x slower (HPT: reliability of 99.99%, 1.01x slower at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser
- [📄table](bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.12.0.md)
- [📈time plot](bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.09x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.13.0.md)
- [📈time plot](bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.11x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.09x
- [🧠memory plot](bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-base-mem.svg)
- [📄table](bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-base.md)
- [📈time plot](bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.13.0b2.md)
- [📈time plot](bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.13.0b2.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10436129942)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-192-generic-x86_64-with-glibc2.31
- [raw results](bm-20240817-linux-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json)

### vs. 3.10.4

- Geometric mean: 1.43x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240817-linux-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.10.4.md)
- [📈time plot](bm-20240817-linux-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 99.98%, 1.01x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240817-linux-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.12.0.md)
- [📈time plot](bm-20240817-linux-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.01x faster (HPT: reliability of 61.43%, 1.00x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240817-linux-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.13.0.md)
- [📈time plot](bm-20240817-linux-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 66.36%, 1.00x slower at 99th %ile)
- Memory usage: 1.08x
- [🧠memory plot](bm-20240817-linux-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-base-mem.svg)
- [📄table](bm-20240817-linux-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-base.md)
- [📈time plot](bm-20240817-linux-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240817-linux-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.13.0b2.md)
- [📈time plot](bm-20240817-linux-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.13.0b2.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10436129942)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json)

### vs. 3.10.4

- Geometric mean: 1.33x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 1.23x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.10.4.md)
- [📈time plot](bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.02x faster (HPT: reliability of 71.61%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.12.0.md)
- [📈time plot](bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.01x faster (HPT: reliability of 76.90%, 1.00x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.13.0.md)
- [📈time plot](bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.02x slower (HPT: reliability of 86.99%, 1.00x slower at 99th %ile)
- Memory usage: 1.08x
- [🧠memory plot](bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-base-mem.svg)
- [📄table](bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-base.md)
- [📈time plot](bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.13.0b2.md)
- [📈time plot](bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.13.0b2.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10436129942)
- cpu model: missing
- platform: macOS-14.6.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json)

### vs. 3.10.4

- Geometric mean: 1.24x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: 0.85x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.10.4.md)
- [📈time plot](bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.05x faster (HPT: reliability of 94.42%, 1.00x faster at 99th %ile)
- Memory usage: 0.67x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.12.0.md)
- [📈time plot](bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.04x faster (HPT: reliability of 99.95%, 1.00x faster at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.13.0.md)
- [📈time plot](bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.05x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-base-mem.svg)
- [📄table](bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-base.md)
- [📈time plot](bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.13.0b2.md)
- [📈time plot](bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b-vs-3.13.0b2.svg)

