# Results

- fork: bdraco
- version: 3.14.0a0
- config: 
- commit hash: [f78838c](https://github.com/bdraco/cpython/commit/f78838c)
- commit date: 2024-08-24T11:31:59-10:00
- commit merge base: [e38d0afe3548b856ccf0b05c01ed3eefc69cb3e7](https://github.com/bdraco/cpython/commit/e38d0afe3548b856ccf0b05c01ed3eefc69cb3e7)
- ref: speed_up_async_sched

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10602102695)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c.json)

### vs. 3.10.4

- Geometric mean: 1.326x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c-vs-3.10.4.md)
- [📈time plot](bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.032x faster (HPT: reliability of 91.90%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser
- [📄table](bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c-vs-3.12.0.md)
- [📈time plot](bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.023x faster (HPT: reliability of 98.50%, 1.00x faster at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl
- [📄table](bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c-vs-3.13.0.md)
- [📈time plot](bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x slower (HPT: reliability of 88.99%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c-vs-base-mem.svg)
- [📄table](bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c-vs-base.md)
- [📈time plot](bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10602102695)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-192-generic-x86_64-with-glibc2.31
- [raw results](bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c.json)

### vs. 3.10.4

- Geometric mean: 1.440x faster (HPT: reliability of 100.00%, 1.32x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c-vs-3.10.4.md)
- [📈time plot](bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.089x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c-vs-3.12.0.md)
- [📈time plot](bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.034x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 0.92x
- missing benchmarks: chameleon, connected_components, dulwich_log, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl
- [📄table](bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c-vs-3.13.0.md)
- [📈time plot](bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.003x faster (HPT: reliability of 97.20%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c-vs-base-mem.svg)
- [📄table](bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c-vs-base.md)
- [📈time plot](bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10602102695)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c.json)

### vs. 3.10.4

- Geometric mean: 1.333x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c-vs-3.10.4.md)
- [📈time plot](bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.023x faster (HPT: reliability of 83.83%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c-vs-3.12.0.md)
- [📈time plot](bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.032x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: chameleon, connected_components, dulwich_log, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl
- [📄table](bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c-vs-3.13.0.md)
- [📈time plot](bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x faster (HPT: reliability of 53.08%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c-vs-base-mem.svg)
- [📄table](bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c-vs-base.md)
- [📈time plot](bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10602102695)
- cpu model: missing
- platform: macOS-14.6.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c.json)

### vs. 3.10.4

- Geometric mean: 1.302x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 0.77x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c-vs-3.10.4.md)
- [📈time plot](bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.086x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.70x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c-vs-3.12.0.md)
- [📈time plot](bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.091x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.63x
- missing benchmarks: chameleon, connected_components, dask, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl
- [📄table](bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c-vs-3.13.0.md)
- [📈time plot](bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x slower (HPT: reliability of 52.48%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c-vs-base-mem.svg)
- [📄table](bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c-vs-base.md)
- [📈time plot](bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c-vs-base.svg)

