# Results

- fork: python/cebae977a63f32c3c03d
- version: 3.15.0a0
- config: JIT
- commit hash: [cebae97](https://github.com/python/cpython/commit/cebae97)
- commit date: 2025-06-01T00:33:02+03:00
- commit merge base: [3704171415c1ea6ebbeb2f992758b6565f42e378](https://github.com/python/cpython/commit/3704171415c1ea6ebbeb2f992758b6565f42e378)
- ref: cebae977a63f32c3c03d

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15368744364)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json)

### vs. 3.10.4

- Geometric mean: 1.375x faster (HPT: reliability of 99.41%, 1.00x faster at 99th %ile)
- Memory usage: 1.40x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, regex_compile, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.10.4.md)
- [📈time plot](bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.074x faster (HPT: reliability of 99.97%, 1.05x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, regex_compile, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.12.0.md)
- [📈time plot](bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.062x faster (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, regex_compile, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.13.0.md)
- [📈time plot](bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.365x faster (HPT: reliability of 85.38%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: 🔴 regex_compile
- [🧠memory plot](bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-base-mem.svg)
- [📄table](bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-base.md)
- [📈time plot](bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15368744364)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json)

### vs. 3.10.4

- Geometric mean: 1.662x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, regex_compile, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.10.4.md)
- [📈time plot](bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.383x faster (HPT: reliability of 51.26%, 1.00x slower at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, regex_compile, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.12.0.md)
- [📈time plot](bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.170x faster (HPT: reliability of 99.89%, 1.02x slower at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, regex_compile, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.13.0.md)
- [📈time plot](bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.374x faster (HPT: reliability of 90.49%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: 🔴 regex_compile
- [🧠memory plot](bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-base-mem.svg)
- [📄table](bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-base.md)
- [📈time plot](bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15368744364)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json)

### vs. 3.10.4

- Geometric mean: 1.627x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.37x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, regex_compile, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.10.4.md)
- [📈time plot](bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.269x faster (HPT: reliability of 98.65%, 1.00x slower at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, regex_compile, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.12.0.md)
- [📈time plot](bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.230x faster (HPT: reliability of 98.86%, 1.00x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: chameleon, gevent_hub, gunicorn, regex_compile, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.13.0.md)
- [📈time plot](bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.347x faster (HPT: reliability of 99.69%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: 🔴 regex_compile
- [🧠memory plot](bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-base-mem.svg)
- [📄table](bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-base.md)
- [📈time plot](bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15368744364)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json)

### vs. 3.10.4

- Geometric mean: 1.218x faster (HPT: reliability of 98.22%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.10.4.md)
- [📈time plot](bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.120x faster (HPT: reliability of 99.86%, 1.07x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.12.0.md)
- [📈time plot](bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.001x slower (HPT: reliability of 100.00%, 1.12x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.13.0.md)
- [📈time plot](bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.449x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-base.md)
- [📈time plot](bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-base.svg)

## windows amd64 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15368744364)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json)

### vs. 3.10.4

- Geometric mean: 1.369x faster (HPT: reliability of 77.82%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.10.4.md)
- [📈time plot](bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.492x faster (HPT: reliability of 99.83%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.12.0.md)
- [📈time plot](bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.198x faster (HPT: reliability of 99.87%, 1.02x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.13.0.md)
- [📈time plot](bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.453x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-base.md)
- [📈time plot](bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15368744364)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json)

### vs. 3.10.4

- Geometric mean: 1.539x faster (HPT: reliability of 99.96%, 1.04x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.10.4.md)
- [📈time plot](bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.199x faster (HPT: reliability of 99.58%, 1.00x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.12.0.md)
- [📈time plot](bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.202x faster (HPT: reliability of 97.25%, 1.00x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.13.0.md)
- [📈time plot](bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.300x faster (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-base-mem.svg)
- [📄table](bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-base.md)
- [📈time plot](bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-base.svg)

