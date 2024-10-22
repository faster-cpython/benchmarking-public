# Results

- fork: python
- version: 3.14.0a0
- config: 
- commit hash: [9b37498](https://github.com/python/cpython/commit/9b37498)
- commit date: 2024-08-25T01:41:44+01:00
- commit merge base: [52caaef6d01a94962576e9510d982f12c1de20c1](https://github.com/python/cpython/commit/52caaef6d01a94962576e9510d982f12c1de20c1)
- ref: 9b3749849eda4012261a

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10559923882)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240825-arminc-aarch64-python-9b3749849eda4012261a-3.14.0a0-9b37498.json)

### vs. 3.10.4

- Geometric mean: 1.34x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240825-arminc-aarch64-python-9b3749849eda4012261a-3.14.0a0-9b37498-vs-3.10.4.md)
- [📈time plot](bm-20240825-arminc-aarch64-python-9b3749849eda4012261a-3.14.0a0-9b37498-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 98.85%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser
- [📄table](bm-20240825-arminc-aarch64-python-9b3749849eda4012261a-3.14.0a0-9b37498-vs-3.12.0.md)
- [📈time plot](bm-20240825-arminc-aarch64-python-9b3749849eda4012261a-3.14.0a0-9b37498-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.02x faster (HPT: reliability of 99.71%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240825-arminc-aarch64-python-9b3749849eda4012261a-3.14.0a0-9b37498-vs-3.13.0.md)
- [📈time plot](bm-20240825-arminc-aarch64-python-9b3749849eda4012261a-3.14.0a0-9b37498-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 58.98%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240825-arminc-aarch64-python-9b3749849eda4012261a-3.14.0a0-9b37498-vs-base-mem.svg)
- [📄table](bm-20240825-arminc-aarch64-python-9b3749849eda4012261a-3.14.0a0-9b37498-vs-base.md)
- [📈time plot](bm-20240825-arminc-aarch64-python-9b3749849eda4012261a-3.14.0a0-9b37498-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240825-arminc-aarch64-python-9b3749849eda4012261a-3.14.0a0-9b37498-vs-3.13.0b2.md)
- [📈time plot](bm-20240825-arminc-aarch64-python-9b3749849eda4012261a-3.14.0a0-9b37498-vs-3.13.0b2.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10559923882)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-192-generic-x86_64-with-glibc2.31
- [raw results](bm-20240825-linux-x86_64-python-9b3749849eda4012261a-3.14.0a0-9b37498.json)

### vs. 3.10.4

- Geometric mean: 1.43x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240825-linux-x86_64-python-9b3749849eda4012261a-3.14.0a0-9b37498-vs-3.10.4.md)
- [📈time plot](bm-20240825-linux-x86_64-python-9b3749849eda4012261a-3.14.0a0-9b37498-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240825-linux-x86_64-python-9b3749849eda4012261a-3.14.0a0-9b37498-vs-3.12.0.md)
- [📈time plot](bm-20240825-linux-x86_64-python-9b3749849eda4012261a-3.14.0a0-9b37498-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.01x faster (HPT: reliability of 89.41%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240825-linux-x86_64-python-9b3749849eda4012261a-3.14.0a0-9b37498-vs-3.13.0.md)
- [📈time plot](bm-20240825-linux-x86_64-python-9b3749849eda4012261a-3.14.0a0-9b37498-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 99.28%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240825-linux-x86_64-python-9b3749849eda4012261a-3.14.0a0-9b37498-vs-base-mem.svg)
- [📄table](bm-20240825-linux-x86_64-python-9b3749849eda4012261a-3.14.0a0-9b37498-vs-base.md)
- [📈time plot](bm-20240825-linux-x86_64-python-9b3749849eda4012261a-3.14.0a0-9b37498-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240825-linux-x86_64-python-9b3749849eda4012261a-3.14.0a0-9b37498-vs-3.13.0b2.md)
- [📈time plot](bm-20240825-linux-x86_64-python-9b3749849eda4012261a-3.14.0a0-9b37498-vs-3.13.0b2.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10559923882)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240825-pythonperf2-x86_64-python-9b3749849eda4012261a-3.14.0a0-9b37498.json)

### vs. 3.10.4

- Geometric mean: 1.35x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240825-pythonperf2-x86_64-python-9b3749849eda4012261a-3.14.0a0-9b37498-vs-3.10.4.md)
- [📈time plot](bm-20240825-pythonperf2-x86_64-python-9b3749849eda4012261a-3.14.0a0-9b37498-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.02x faster (HPT: reliability of 76.84%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240825-pythonperf2-x86_64-python-9b3749849eda4012261a-3.14.0a0-9b37498-vs-3.12.0.md)
- [📈time plot](bm-20240825-pythonperf2-x86_64-python-9b3749849eda4012261a-3.14.0a0-9b37498-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.02x faster (HPT: reliability of 99.92%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240825-pythonperf2-x86_64-python-9b3749849eda4012261a-3.14.0a0-9b37498-vs-3.13.0.md)
- [📈time plot](bm-20240825-pythonperf2-x86_64-python-9b3749849eda4012261a-3.14.0a0-9b37498-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 92.04%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240825-pythonperf2-x86_64-python-9b3749849eda4012261a-3.14.0a0-9b37498-vs-base-mem.svg)
- [📄table](bm-20240825-pythonperf2-x86_64-python-9b3749849eda4012261a-3.14.0a0-9b37498-vs-base.md)
- [📈time plot](bm-20240825-pythonperf2-x86_64-python-9b3749849eda4012261a-3.14.0a0-9b37498-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240825-pythonperf2-x86_64-python-9b3749849eda4012261a-3.14.0a0-9b37498-vs-3.13.0b2.md)
- [📈time plot](bm-20240825-pythonperf2-x86_64-python-9b3749849eda4012261a-3.14.0a0-9b37498-vs-3.13.0b2.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10559923882)
- cpu model: missing
- platform: macOS-14.6.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20240825-darwin-arm64-python-9b3749849eda4012261a-3.14.0a0-9b37498.json)

### vs. 3.10.4

- Geometric mean: 1.30x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 0.57x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240825-darwin-arm64-python-9b3749849eda4012261a-3.14.0a0-9b37498-vs-3.10.4.md)
- [📈time plot](bm-20240825-darwin-arm64-python-9b3749849eda4012261a-3.14.0a0-9b37498-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.09x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.56x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240825-darwin-arm64-python-9b3749849eda4012261a-3.14.0a0-9b37498-vs-3.12.0.md)
- [📈time plot](bm-20240825-darwin-arm64-python-9b3749849eda4012261a-3.14.0a0-9b37498-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240825-darwin-arm64-python-9b3749849eda4012261a-3.14.0a0-9b37498-vs-3.13.0.md)
- [📈time plot](bm-20240825-darwin-arm64-python-9b3749849eda4012261a-3.14.0a0-9b37498-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.01x slower (HPT: reliability of 99.28%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240825-darwin-arm64-python-9b3749849eda4012261a-3.14.0a0-9b37498-vs-base-mem.svg)
- [📄table](bm-20240825-darwin-arm64-python-9b3749849eda4012261a-3.14.0a0-9b37498-vs-base.md)
- [📈time plot](bm-20240825-darwin-arm64-python-9b3749849eda4012261a-3.14.0a0-9b37498-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240825-darwin-arm64-python-9b3749849eda4012261a-3.14.0a0-9b37498-vs-3.13.0b2.md)
- [📈time plot](bm-20240825-darwin-arm64-python-9b3749849eda4012261a-3.14.0a0-9b37498-vs-3.13.0b2.svg)

