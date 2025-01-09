# Results vs. 3.12.0

- fork: kumaraditya303
- ref: fast_coro
- machine: linux-x86_64
- commit hash: e4984ea
- commit date: 2025-01-09
- overall geometric mean: 1.111x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 254 ms: 1.08x faster                                                |
| docutils       | 2.77 sec                                               | 2.60 sec: 1.07x faster                                              |
| Geometric mean | (ref)                                                  | 1.07x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 585 ms: 2.02x faster                                                |
| async_tree_io              | 1.16 sec                                               | 604 ms: 1.91x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 308 ms: 1.86x faster                                                |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.80x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.80x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 326 ms: 1.77x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 470 ms: 1.54x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 492 ms: 1.47x faster                                                |
| Geometric mean             | (ref)                                                  | 1.77x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 72.6 ms: 1.17x faster                                               |
| nbody          | 97.0 ms                                                | 94.0 ms: 1.03x faster                                               |
| pidigits       | 187 ms                                                 | 190 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                  | 1.06x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                                |
| regex_effbot   | 3.61 ms                                                | 3.34 ms: 1.08x faster                                               |
| regex_dna      | 212 ms                                                 | 211 ms: 1.00x faster                                                |
| regex_v8       | 23.1 ms                                                | 25.5 ms: 1.10x slower                                               |
| Geometric mean | (ref)                                                  | 1.04x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.99 sec: 1.17x faster                                              |
| xml_etree_parse      | 159 ms                                                 | 139 ms: 1.15x faster                                                |
| xml_etree_iterparse  | 107 ms                                                 | 96.5 ms: 1.11x faster                                               |
| json_loads           | 28.5 us                                                | 26.6 us: 1.07x faster                                               |
| unpickle_pure_python | 230 us                                                 | 216 us: 1.07x faster                                                |
| xml_etree_generate   | 89.2 ms                                                | 85.0 ms: 1.05x faster                                               |
| xml_etree_process    | 61.7 ms                                                | 59.3 ms: 1.04x faster                                               |
| pickle_pure_python   | 324 us                                                 | 322 us: 1.01x faster                                                |
| json_dumps           | 10.4 ms                                                | 11.6 ms: 1.11x slower                                               |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.06 ms: 1.02x slower                                               |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                               |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.6 ms: 1.09x faster                                               |
| mako            | 11.9 ms                                                | 11.6 ms: 1.02x faster                                               |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 585 ms: 2.02x faster                                                |
| async_tree_io              | 1.16 sec                                               | 604 ms: 1.91x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 308 ms: 1.86x faster                                                |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.80x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.80x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 326 ms: 1.77x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 470 ms: 1.54x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 492 ms: 1.47x faster                                                |
| deepcopy                   | 371 us                                                 | 261 us: 1.42x faster                                                |
| deepcopy_memo              | 40.7 us                                                | 30.6 us: 1.33x faster                                               |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.31x faster                                               |
| deepcopy_reduce            | 3.35 us                                                | 2.71 us: 1.23x faster                                               |
| go                         | 139 ms                                                 | 116 ms: 1.20x faster                                                |
| pathlib                    | 19.3 ms                                                | 16.3 ms: 1.19x faster                                               |
| tomli_loads                | 2.33 sec                                               | 1.99 sec: 1.17x faster                                              |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                                |
| logging_format             | 7.23 us                                                | 6.20 us: 1.17x faster                                               |
| float                      | 84.7 ms                                                | 72.6 ms: 1.17x faster                                               |
| generators                 | 31.2 ms                                                | 27.1 ms: 1.15x faster                                               |
| xml_etree_parse            | 159 ms                                                 | 139 ms: 1.15x faster                                                |
| logging_simple             | 6.46 us                                                | 5.62 us: 1.15x faster                                               |
| sympy_sum                  | 169 ms                                                 | 148 ms: 1.15x faster                                                |
| raytrace                   | 312 ms                                                 | 273 ms: 1.14x faster                                                |
| deltablue                  | 3.72 ms                                                | 3.25 ms: 1.14x faster                                               |
| crypto_pyaes               | 81.9 ms                                                | 71.9 ms: 1.14x faster                                               |
| sqlalchemy_declarative     | 147 ms                                                 | 129 ms: 1.14x faster                                                |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.5 ms: 1.13x faster                                               |
| sympy_str                  | 300 ms                                                 | 268 ms: 1.12x faster                                                |
| scimark_monte_carlo        | 75.1 ms                                                | 67.6 ms: 1.11x faster                                               |
| xml_etree_iterparse        | 107 ms                                                 | 96.5 ms: 1.11x faster                                               |
| chaos                      | 67.0 ms                                                | 61.0 ms: 1.10x faster                                               |
| django_template            | 34.6 ms                                                | 31.6 ms: 1.09x faster                                               |
| async_generators           | 463 ms                                                 | 424 ms: 1.09x faster                                                |
| sympy_integrate            | 21.4 ms                                                | 19.7 ms: 1.08x faster                                               |
| regex_effbot               | 3.61 ms                                                | 3.34 ms: 1.08x faster                                               |
| spectral_norm              | 115 ms                                                 | 106 ms: 1.08x faster                                                |
| 2to3                       | 274 ms                                                 | 254 ms: 1.08x faster                                                |
| scimark_fft                | 382 ms                                                 | 354 ms: 1.08x faster                                                |
| dulwich_log                | 68.5 ms                                                | 63.8 ms: 1.07x faster                                               |
| sqlglot_normalize          | 110 ms                                                 | 103 ms: 1.07x faster                                                |
| json_loads                 | 28.5 us                                                | 26.6 us: 1.07x faster                                               |
| sqlglot_parse              | 1.36 ms                                                | 1.27 ms: 1.07x faster                                               |
| unpickle_pure_python       | 230 us                                                 | 216 us: 1.07x faster                                                |
| docutils                   | 2.77 sec                                               | 2.60 sec: 1.07x faster                                              |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.06x faster                                               |
| json                       | 5.26 ms                                                | 4.95 ms: 1.06x faster                                               |
| pyflate                    | 482 ms                                                 | 455 ms: 1.06x faster                                                |
| pprint_safe_repr           | 776 ms                                                 | 732 ms: 1.06x faster                                                |
| scimark_sor                | 129 ms                                                 | 122 ms: 1.06x faster                                                |
| nqueens                    | 83.3 ms                                                | 79.0 ms: 1.05x faster                                               |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.80 ms: 1.05x faster                                               |
| sympy_expand               | 478 ms                                                 | 455 ms: 1.05x faster                                                |
| sqlglot_optimize           | 54.8 ms                                                | 52.2 ms: 1.05x faster                                               |
| fannkuch                   | 417 ms                                                 | 397 ms: 1.05x faster                                                |
| pprint_pformat             | 1.57 sec                                               | 1.49 sec: 1.05x faster                                              |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                |
| xml_etree_generate         | 89.2 ms                                                | 85.0 ms: 1.05x faster                                               |
| xml_etree_process          | 61.7 ms                                                | 59.3 ms: 1.04x faster                                               |
| mdp                        | 2.63 sec                                               | 2.53 sec: 1.04x faster                                              |
| richards                   | 45.8 ms                                                | 44.3 ms: 1.04x faster                                               |
| nbody                      | 97.0 ms                                                | 94.0 ms: 1.03x faster                                               |
| hexiom                     | 6.41 ms                                                | 6.22 ms: 1.03x faster                                               |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.03x faster                                                |
| richards_super             | 51.5 ms                                                | 50.1 ms: 1.03x faster                                               |
| mako                       | 11.9 ms                                                | 11.6 ms: 1.02x faster                                               |
| pickle_pure_python         | 324 us                                                 | 322 us: 1.01x faster                                                |
| regex_dna                  | 212 ms                                                 | 211 ms: 1.00x faster                                                |
| pidigits                   | 187 ms                                                 | 190 ms: 1.01x slower                                                |
| logging_silent             | 104 ns                                                 | 106 ns: 1.02x slower                                                |
| python_startup_no_site     | 6.94 ms                                                | 7.06 ms: 1.02x slower                                               |
| bench_thread_pool          | 842 us                                                 | 863 us: 1.02x slower                                                |
| typing_runtime_protocols   | 158 us                                                 | 162 us: 1.03x slower                                                |
| regex_v8                   | 23.1 ms                                                | 25.5 ms: 1.10x slower                                               |
| telco                      | 7.10 ms                                                | 7.87 ms: 1.11x slower                                               |
| json_dumps                 | 10.4 ms                                                | 11.6 ms: 1.11x slower                                               |
| coverage                   | 72.7 ms                                                | 84.4 ms: 1.16x slower                                               |
| gc_traversal               | 3.79 ms                                                | 5.02 ms: 1.32x slower                                               |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                               |
| create_gc_cycles           | 1.48 ms                                                | 2.46 ms: 1.67x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 81.6 ms: 3.40x slower                                               |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                        |

Benchmark hidden because not significant (4): pycparser, coroutines, asyncio_websockets, sqlite_synth
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250109-3.14.0a3+-e4984ea/bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.111x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.09x