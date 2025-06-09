# Results

- fork: python/aac22ea212849f8fffee
- version: 3.15.0a0
- config: 
- commit hash: [aac22ea](https://github.com/python/cpython/commit/aac22ea)
- commit date: 2025-06-08T17:55:12+01:00
- commit merge base: [254bdac71121ee8028967388104a3f083250211e](https://github.com/python/cpython/commit/254bdac71121ee8028967388104a3f083250211e)
- ref: aac22ea212849f8fffee

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15537976389)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250608-arminc-aarch64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea.json)

### vs. 3.10.4

- Geometric mean: 1.225x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.35x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250608-arminc-aarch64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea-vs-3.10.4.md)
- [📈time plot](bm-20250608-arminc-aarch64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.028x slower (HPT: reliability of 99.91%, 1.00x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250608-arminc-aarch64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea-vs-3.12.0.md)
- [📈time plot](bm-20250608-arminc-aarch64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.026x slower (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250608-arminc-aarch64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea-vs-3.13.0.md)
- [📈time plot](bm-20250608-arminc-aarch64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea-vs-3.13.0.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15537976389)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-216-generic-x86_64-with-glibc2.31
- [raw results](bm-20250608-linux-x86_64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea.json)

### vs. 3.10.4

- Geometric mean: 1.314x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250608-linux-x86_64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea-vs-3.10.4.md)
- [📈time plot](bm-20250608-linux-x86_64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.085x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250608-linux-x86_64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea-vs-3.12.0.md)
- [📈time plot](bm-20250608-linux-x86_64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.042x slower (HPT: reliability of 97.79%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250608-linux-x86_64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea-vs-3.13.0.md)
- [📈time plot](bm-20250608-linux-x86_64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15537976389)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250608-pythonperf1-amd64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea.json)

### vs. 3.10.4

- Geometric mean: 1.158x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250608-pythonperf1-amd64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea-vs-3.10.4.md)
- [📈time plot](bm-20250608-pythonperf1-amd64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.057x faster (HPT: reliability of 99.92%, 1.01x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250608-pythonperf1-amd64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea-vs-3.12.0.md)
- [📈time plot](bm-20250608-pythonperf1-amd64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.030x slower (HPT: reliability of 98.41%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250608-pythonperf1-amd64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea-vs-3.13.0.md)
- [📈time plot](bm-20250608-pythonperf1-amd64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15537976389)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250608-darwin-arm64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea.json)

### vs. 3.10.4

- Geometric mean: 1.200x faster (HPT: reliability of 100.00%, 1.15x faster at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250608-darwin-arm64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea-vs-3.10.4.md)
- [📈time plot](bm-20250608-darwin-arm64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.044x slower (HPT: reliability of 65.03%, 1.00x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250608-darwin-arm64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea-vs-3.12.0.md)
- [📈time plot](bm-20250608-darwin-arm64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.043x slower (HPT: reliability of 99.98%, 1.01x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250608-darwin-arm64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea-vs-3.13.0.md)
- [📈time plot](bm-20250608-darwin-arm64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea-vs-3.13.0.svg)

