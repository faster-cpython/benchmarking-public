# Results

- fork: colesbury
- version: 3.14.0a0
- config: 
- commit hash: [85453d0](https://github.com/colesbury/cpython/commit/85453d0)
- commit date: 2024-07-17T19:17:03+00:00
- commit merge base: [f4bc84d261c828ed81f137f2a48fa2f0de7a0211](https://github.com/colesbury/cpython/commit/f4bc84d261c828ed81f137f2a48fa2f0de7a0211)
- ref: gh_100240_freelist

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9987143875)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0.json)

### vs. 3.10.4

- Geometric mean: 1.34x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0-vs-3.10.4.md)
- [📈time plot](bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 94.99%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser
- [📄table](bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0-vs-3.12.0.md)
- [📈time plot](bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.01x faster (HPT: reliability of 89.24%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: dulwich_log
- [📄table](bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0-vs-3.13.0.md)
- [📈time plot](bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.01x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0-vs-base-mem.svg)
- [📄table](bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0-vs-base.md)
- [📈time plot](bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0-vs-3.13.0b2.md)
- [📈time plot](bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0-vs-3.13.0b2.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9987143875)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0.json)

### vs. 3.10.4

- Geometric mean: 1.44x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0-vs-3.10.4.md)
- [📈time plot](bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.09x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0-vs-3.12.0.md)
- [📈time plot](bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.02x faster (HPT: reliability of 98.77%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0-vs-3.13.0.md)
- [📈time plot](bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 68.18%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0-vs-base-mem.svg)
- [📄table](bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0-vs-base.md)
- [📈time plot](bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0-vs-3.13.0b2.md)
- [📈time plot](bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0-vs-3.13.0b2.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9987143875)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0.json)

### vs. 3.10.4

- Geometric mean: 1.35x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0-vs-3.10.4.md)
- [📈time plot](bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 92.81%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0-vs-3.12.0.md)
- [📈time plot](bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.03x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0-vs-3.13.0.md)
- [📈time plot](bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 99.93%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0-vs-base-mem.svg)
- [📄table](bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0-vs-base.md)
- [📈time plot](bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0-vs-3.13.0b2.md)
- [📈time plot](bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0-vs-3.13.0b2.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9987143875)
- cpu model: missing
- platform: macOS-14.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20240717-darwin-arm64-colesbury-gh_100240_freelist-3.14.0a0-85453d0.json)

### vs. 3.10.4

- Geometric mean: 1.31x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240717-darwin-arm64-colesbury-gh_100240_freelist-3.14.0a0-85453d0-vs-3.10.4.md)
- [📈time plot](bm-20240717-darwin-arm64-colesbury-gh_100240_freelist-3.14.0a0-85453d0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.09x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240717-darwin-arm64-colesbury-gh_100240_freelist-3.14.0a0-85453d0-vs-3.12.0.md)
- [📈time plot](bm-20240717-darwin-arm64-colesbury-gh_100240_freelist-3.14.0a0-85453d0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.09x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 5.93x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240717-darwin-arm64-colesbury-gh_100240_freelist-3.14.0a0-85453d0-vs-3.13.0.md)
- [📈time plot](bm-20240717-darwin-arm64-colesbury-gh_100240_freelist-3.14.0a0-85453d0-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 68.82%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240717-darwin-arm64-colesbury-gh_100240_freelist-3.14.0a0-85453d0-vs-base-mem.svg)
- [📄table](bm-20240717-darwin-arm64-colesbury-gh_100240_freelist-3.14.0a0-85453d0-vs-base.md)
- [📈time plot](bm-20240717-darwin-arm64-colesbury-gh_100240_freelist-3.14.0a0-85453d0-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240717-darwin-arm64-colesbury-gh_100240_freelist-3.14.0a0-85453d0-vs-3.13.0b2.md)
- [📈time plot](bm-20240717-darwin-arm64-colesbury-gh_100240_freelist-3.14.0a0-85453d0-vs-3.13.0b2.svg)

