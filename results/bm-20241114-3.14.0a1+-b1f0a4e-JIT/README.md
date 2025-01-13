# Results

- fork: brandtbucher/justin_frame_pointer
- version: 3.14.0a1+
- config: JIT
- commit hash: [b1f0a4e](https://github.com/brandtbucher/cpython/commit/b1f0a4e)
- commit date: 2024-11-14T18:40:56-08:00
- commit merge base: [09d6f5dc7824c74672add512619e978844ff8051](https://github.com/python/cpython/commit/09d6f5dc7824c74672add512619e978844ff8051)
- ref: justin_frame_pointer

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11871663114)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241114-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e.json)

### vs. 3.10.4

- Geometric mean: 1.111x faster (HPT: reliability of 99.08%, 1.00x faster at 99th %ile)
- Memory usage: 1.38x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241114-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-3.10.4.md)
- [📈time plot](bm-20241114-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.126x slower (HPT: reliability of 100.00%, 1.09x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241114-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-3.12.0.md)
- [📈time plot](bm-20241114-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.138x slower (HPT: reliability of 100.00%, 1.08x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log
- [📄table](bm-20241114-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-3.13.0.md)
- [📈time plot](bm-20241114-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.031x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241114-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-base-mem.svg)
- [📄table](bm-20241114-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-base.md)
- [📈time plot](bm-20241114-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11871663114)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e.json)

### vs. 3.10.4

- Geometric mean: 1.350x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.34x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-3.10.4.md)
- [📈time plot](bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.030x faster (HPT: reliability of 99.22%, 1.00x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-3.12.0.md)
- [📈time plot](bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.029x slower (HPT: reliability of 99.97%, 1.01x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-3.13.0.md)
- [📈time plot](bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.021x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-base-mem.svg)
- [📄table](bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-base.md)
- [📈time plot](bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11871663114)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20241114-pythonperf2-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e.json)

### vs. 3.10.4

- Geometric mean: 1.219x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: 1.35x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241114-pythonperf2-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-3.10.4.md)
- [📈time plot](bm-20241114-pythonperf2-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.056x slower (HPT: reliability of 99.99%, 1.03x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241114-pythonperf2-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-3.12.0.md)
- [📈time plot](bm-20241114-pythonperf2-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.051x slower (HPT: reliability of 99.99%, 1.01x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241114-pythonperf2-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-3.13.0.md)
- [📈time plot](bm-20241114-pythonperf2-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.028x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241114-pythonperf2-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-base-mem.svg)
- [📄table](bm-20241114-pythonperf2-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-base.md)
- [📈time plot](bm-20241114-pythonperf2-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11871663114)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241114-pythonperf1-amd64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e.json)

### vs. 3.10.4

- Geometric mean: 1.181x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241114-pythonperf1-amd64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-3.10.4.md)
- [📈time plot](bm-20241114-pythonperf1-amd64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.000x faster (HPT: reliability of 65.86%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241114-pythonperf1-amd64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-3.12.0.md)
- [📈time plot](bm-20241114-pythonperf1-amd64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.021x slower (HPT: reliability of 99.21%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20241114-pythonperf1-amd64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-3.13.0.md)
- [📈time plot](bm-20241114-pythonperf1-amd64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.023x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241114-pythonperf1-amd64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-base.md)
- [📈time plot](bm-20241114-pythonperf1-amd64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11871663114)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241114-pythonperf1_win32-x86-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e.json)

### vs. 3.10.4

- Geometric mean: 1.003x slower (HPT: reliability of 91.42%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241114-pythonperf1_win32-x86-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-3.10.4.md)
- [📈time plot](bm-20241114-pythonperf1_win32-x86-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.007x faster (HPT: reliability of 57.35%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241114-pythonperf1_win32-x86-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-3.12.0.md)
- [📈time plot](bm-20241114-pythonperf1_win32-x86-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.096x slower (HPT: reliability of 100.00%, 1.12x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20241114-pythonperf1_win32-x86-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-3.13.0.md)
- [📈time plot](bm-20241114-pythonperf1_win32-x86-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.034x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241114-pythonperf1_win32-x86-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-base.md)
- [📈time plot](bm-20241114-pythonperf1_win32-x86-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11871663114)
- cpu model: missing
- platform: macOS-15.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241114-darwin-arm64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e.json)

### vs. 3.10.4

- Geometric mean: 1.181x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: 1.44x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20241114-darwin-arm64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-3.10.4.md)
- [📈time plot](bm-20241114-darwin-arm64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.008x slower (HPT: reliability of 89.47%, 1.00x slower at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241114-darwin-arm64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-3.12.0.md)
- [📈time plot](bm-20241114-darwin-arm64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.005x slower (HPT: reliability of 67.81%, 1.00x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241114-darwin-arm64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-3.13.0.md)
- [📈time plot](bm-20241114-darwin-arm64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.021x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241114-darwin-arm64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-base-mem.svg)
- [📄table](bm-20241114-darwin-arm64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-base.md)
- [📈time plot](bm-20241114-darwin-arm64-brandtbucher-justin_frame_pointer-3.14.0a1%2B-b1f0a4e-vs-base.svg)

