# Results

- fork: python
- version: 3.14.0a1+
- config: NOGIL
- commit hash: [f6cc7c8](https://github.com/python/cpython/commit/f6cc7c8)
- commit date: 2024-10-26T23:40:31+02:00
- commit merge base: [26d627779f79d8d5650fe7be348432eccc28f8f9](https://github.com/python/cpython/commit/26d627779f79d8d5650fe7be348432eccc28f8f9)
- ref: f6cc7c8bd01d8468af70

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11535901955)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8.json)

### vs. 3.10.4

- Geometric mean: 1.193x slower (HPT: reliability of 100.00%, 1.19x slower at 99th %ile)
- Memory usage: 1.50x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.10.4.md)
- [📈time plot](bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.362x slower (HPT: reliability of 100.00%, 1.39x slower at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, sphinx
- [📄table](bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.12.0.md)
- [📈time plot](bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.369x slower (HPT: reliability of 100.00%, 1.40x slower at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlite_synth, subparsers
- new benchmarks: dulwich_log
- [📄table](bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.13.0.md)
- [📈time plot](bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.377x slower (HPT: reliability of 100.00%, 1.40x slower at 99th %ile)
- Memory usage: 1.16x
- [🧠memory plot](bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-base-mem.svg)
- [📄table](bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-base.md)
- [📈time plot](bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11535901955)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241026-linux-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8.json)

### vs. 3.10.4

- Geometric mean: 1.055x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: 1.44x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241026-linux-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.10.4.md)
- [📈time plot](bm-20241026-linux-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.270x slower (HPT: reliability of 100.00%, 1.25x slower at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241026-linux-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.12.0.md)
- [📈time plot](bm-20241026-linux-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.307x slower (HPT: reliability of 100.00%, 1.30x slower at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlite_synth, subparsers
- [📄table](bm-20241026-linux-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.13.0.md)
- [📈time plot](bm-20241026-linux-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.313x slower (HPT: reliability of 100.00%, 1.32x slower at 99th %ile)
- Memory usage: 1.15x
- [🧠memory plot](bm-20241026-linux-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-base-mem.svg)
- [📄table](bm-20241026-linux-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-base.md)
- [📈time plot](bm-20241026-linux-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11535901955)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8.json)

### vs. 3.10.4

- Geometric mean: 1.104x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: 1.47x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.10.4.md)
- [📈time plot](bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.302x slower (HPT: reliability of 100.00%, 1.27x slower at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.12.0.md)
- [📈time plot](bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.296x slower (HPT: reliability of 100.00%, 1.28x slower at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlite_synth, subparsers
- [📄table](bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.13.0.md)
- [📈time plot](bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.310x slower (HPT: reliability of 100.00%, 1.33x slower at 99th %ile)
- Memory usage: 1.17x
- [🧠memory plot](bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-base-mem.svg)
- [📄table](bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-base.md)
- [📈time plot](bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11535901955)
- cpu model: missing
- platform: macOS-15.0.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8.json)

### vs. 3.10.4

- Geometric mean: 1.109x slower (HPT: reliability of 100.00%, 1.10x slower at 99th %ile)
- Memory usage: 1.45x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.10.4.md)
- [📈time plot](bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.242x slower (HPT: reliability of 100.00%, 1.16x slower at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.12.0.md)
- [📈time plot](bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.223x slower (HPT: reliability of 100.00%, 1.16x slower at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlite_synth, subparsers
- [📄table](bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.13.0.md)
- [📈time plot](bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.282x slower (HPT: reliability of 100.00%, 1.23x slower at 99th %ile)
- Memory usage: 1.11x
- [🧠memory plot](bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-base-mem.svg)
- [📄table](bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-base.md)
- [📈time plot](bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-base.svg)

