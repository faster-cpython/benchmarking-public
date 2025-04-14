# Results

- fork: brandtbucher/jit_compact_alt
- version: 3.14.0a4+
- config: JIT
- commit hash: [3aecbaa](https://github.com/brandtbucher/cpython/commit/3aecbaa)
- commit date: 2025-01-26T20:12:27-08:00
- commit merge base: [86c1a60d5a28cfb51f8843b307f8969c40e3bbec](https://github.com/python/cpython/commit/86c1a60d5a28cfb51f8843b307f8969c40e3bbec)
- ref: jit_compact_alt

## linux x86_64 (azure)

- [pystats raw](bm-20250126-azure-x86_64-brandtbucher-jit_compact_alt-3.14.0a4%2B-3aecbaa-pystats.json)
- [pystats table](bm-20250126-azure-x86_64-brandtbucher-jit_compact_alt-3.14.0a4%2B-3aecbaa-pystats.md)

### vs. base

- [pystats diff](bm-20250126-azure-x86_64-brandtbucher-jit_compact_alt-3.14.0a4%2B-3aecbaa-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12981910906)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250126-linux-x86_64-brandtbucher-jit_compact_alt-3.14.0a4%2B-3aecbaa.json)

### vs. 3.10.4

- Geometric mean: 1.392x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.45x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250126-linux-x86_64-brandtbucher-jit_compact_alt-3.14.0a4%2B-3aecbaa-vs-3.10.4.md)
- [📈time plot](bm-20250126-linux-x86_64-brandtbucher-jit_compact_alt-3.14.0a4%2B-3aecbaa-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.074x faster (HPT: reliability of 99.98%, 1.02x faster at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250126-linux-x86_64-brandtbucher-jit_compact_alt-3.14.0a4%2B-3aecbaa-vs-3.12.0.md)
- [📈time plot](bm-20250126-linux-x86_64-brandtbucher-jit_compact_alt-3.14.0a4%2B-3aecbaa-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.005x faster (HPT: reliability of 84.34%, 1.00x faster at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250126-linux-x86_64-brandtbucher-jit_compact_alt-3.14.0a4%2B-3aecbaa-vs-3.13.0.md)
- [📈time plot](bm-20250126-linux-x86_64-brandtbucher-jit_compact_alt-3.14.0a4%2B-3aecbaa-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.029x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 1.12x
- [🧠memory plot](bm-20250126-linux-x86_64-brandtbucher-jit_compact_alt-3.14.0a4%2B-3aecbaa-vs-base-mem.svg)
- [📄table](bm-20250126-linux-x86_64-brandtbucher-jit_compact_alt-3.14.0a4%2B-3aecbaa-vs-base.md)
- [📈time plot](bm-20250126-linux-x86_64-brandtbucher-jit_compact_alt-3.14.0a4%2B-3aecbaa-vs-base.svg)

