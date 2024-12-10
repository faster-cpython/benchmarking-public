# Results

- fork: brandtbucher/justin_dwarf
- version: 3.14.0a1+
- config: JIT
- commit hash: [1ce520b](https://github.com/brandtbucher/cpython/commit/1ce520b)
- commit date: 2024-11-15T14:20:58-08:00
- commit merge base: [09d6f5dc7824c74672add512619e978844ff8051](https://github.com/python/cpython/commit/09d6f5dc7824c74672add512619e978844ff8051)
- ref: justin_dwarf

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11864432015)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1%2B-1ce520b.json)

### vs. 3.10.4

- Geometric mean: 1.396x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.41x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1%2B-1ce520b-vs-3.10.4.md)
- [📈time plot](bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1%2B-1ce520b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.066x faster (HPT: reliability of 99.98%, 1.01x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1%2B-1ce520b-vs-3.12.0.md)
- [📈time plot](bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1%2B-1ce520b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.002x faster (HPT: reliability of 51.06%, 1.00x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1%2B-1ce520b-vs-3.13.0.md)
- [📈time plot](bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1%2B-1ce520b-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.009x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- [🧠memory plot](bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1%2B-1ce520b-vs-base-mem.svg)
- [📄table](bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1%2B-1ce520b-vs-base.md)
- [📈time plot](bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1%2B-1ce520b-vs-base.svg)

