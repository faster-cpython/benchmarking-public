# Results

- fork: savannahostrowski
- version: 3.14.0a1+
- config: JIT
- commit hash: [9827ade](https://github.com/savannahostrowski/cpython/commit/9827ade)
- commit date: 2024-10-16T09:10:58-07:00
- commit merge base: [760872efecb95017db8e38a8eda614bf23d2a22c](https://github.com/savannahostrowski/cpython/commit/760872efecb95017db8e38a8eda614bf23d2a22c)
- ref: remove_ghccc

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11373872551)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1%2B-9827ade.json)

### vs. 3.10.4

- Geometric mean: 1.199x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.37x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx, unpack_sequence
- [📄table](bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1%2B-9827ade-vs-3.10.4.md)
- [📈time plot](bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1%2B-9827ade-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.060x slower (HPT: reliability of 99.92%, 1.01x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, sphinx, unpack_sequence
- [📄table](bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1%2B-9827ade-vs-3.12.0.md)
- [📈time plot](bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1%2B-9827ade-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.070x slower (HPT: reliability of 99.98%, 1.01x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1%2B-9827ade-vs-3.13.0.md)
- [📈time plot](bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1%2B-9827ade-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.024x faster (HPT: reliability of 99.99%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1%2B-9827ade-vs-base-mem.svg)
- [📄table](bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1%2B-9827ade-vs-base.md)
- [📈time plot](bm-20241016-arminc-aarch64-savannahostrowski-remove_ghccc-3.14.0a1%2B-9827ade-vs-base.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20241016-azure-x86_64-savannahostrowski-remove_ghccc-3.14.0a1%2B-9827ade-pystats.json)
- [pystats table](bm-20241016-azure-x86_64-savannahostrowski-remove_ghccc-3.14.0a1%2B-9827ade-pystats.md)

### vs. base

- [pystats diff](bm-20241016-azure-x86_64-savannahostrowski-remove_ghccc-3.14.0a1%2B-9827ade-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11373872551)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1%2B-9827ade.json)

### vs. 3.10.4

- Geometric mean: 1.392x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1%2B-9827ade-vs-3.10.4.md)
- [📈time plot](bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1%2B-9827ade-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.063x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1%2B-9827ade-vs-3.12.0.md)
- [📈time plot](bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1%2B-9827ade-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.004x faster (HPT: reliability of 57.39%, 1.00x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1%2B-9827ade-vs-3.13.0.md)
- [📈time plot](bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1%2B-9827ade-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x slower (HPT: reliability of 82.99%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1%2B-9827ade-vs-base-mem.svg)
- [📄table](bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1%2B-9827ade-vs-base.md)
- [📈time plot](bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1%2B-9827ade-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11373872551)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1%2B-9827ade.json)

### vs. 3.10.4

- Geometric mean: 1.286x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: 1.34x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1%2B-9827ade-vs-3.10.4.md)
- [📈time plot](bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1%2B-9827ade-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.007x slower (HPT: reliability of 68.92%, 1.00x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1%2B-9827ade-vs-3.12.0.md)
- [📈time plot](bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1%2B-9827ade-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.003x slower (HPT: reliability of 50.96%, 1.00x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1%2B-9827ade-vs-3.13.0.md)
- [📈time plot](bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1%2B-9827ade-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.000x faster (HPT: reliability of 67.52%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1%2B-9827ade-vs-base-mem.svg)
- [📄table](bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1%2B-9827ade-vs-base.md)
- [📈time plot](bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1%2B-9827ade-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11373872551)
- cpu model: missing
- platform: macOS-15.0.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1%2B-9827ade.json)

### vs. 3.10.4

- Geometric mean: 1.234x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: 1.43x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1%2B-9827ade-vs-3.10.4.md)
- [📈time plot](bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1%2B-9827ade-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.040x faster (HPT: reliability of 99.73%, 1.00x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1%2B-9827ade-vs-3.12.0.md)
- [📈time plot](bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1%2B-9827ade-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.043x faster (HPT: reliability of 99.86%, 1.00x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: chameleon, connected_components, dask, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1%2B-9827ade-vs-3.13.0.md)
- [📈time plot](bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1%2B-9827ade-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.003x faster (HPT: reliability of 87.92%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1%2B-9827ade-vs-base-mem.svg)
- [📄table](bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1%2B-9827ade-vs-base.md)
- [📈time plot](bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1%2B-9827ade-vs-base.svg)

