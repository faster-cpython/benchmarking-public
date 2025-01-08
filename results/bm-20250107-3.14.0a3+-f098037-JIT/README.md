# Results

- fork: brandtbucher/nojit
- version: 3.14.0a3+
- config: JIT
- commit hash: [f098037](https://github.com/brandtbucher/cpython/commit/f098037)
- commit date: 2025-01-07T14:31:59-08:00
- commit merge base: [7363476b6405e3d288a61282aa7bc6aca9c2114d](https://github.com/python/cpython/commit/7363476b6405e3d288a61282aa7bc6aca9c2114d)
- ref: nojit

## linux x86_64 (azure)

- [pystats raw](bm-20250107-azure-x86_64-brandtbucher-nojit-3.14.0a3%2B-f098037-pystats.json)
- [pystats table](bm-20250107-azure-x86_64-brandtbucher-nojit-3.14.0a3%2B-f098037-pystats.md)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12660451851)
- cpu model: missing
- platform: macOS-15.2-arm64-arm-64bit-Mach-O
- [raw results](bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3%2B-f098037.json)

### vs. 3.10.4

- Geometric mean: 1.273x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: 1.37x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.10.4.md)
- [📈time plot](bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.079x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.12.0.md)
- [📈time plot](bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.091x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.13.0.md)
- [📈time plot](bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x faster (HPT: reliability of 52.09%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-base-mem.svg)
- [📄table](bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-base.md)
- [📈time plot](bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3%2B-f098037-vs-base.svg)

