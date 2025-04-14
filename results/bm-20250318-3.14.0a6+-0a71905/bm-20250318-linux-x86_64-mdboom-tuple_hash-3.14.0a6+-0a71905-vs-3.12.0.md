# Results vs. 3.12.0

- fork: mdboom
- ref: tuple_hash
- machine: linux-x86_64
- commit hash: 0a71905
- commit date: 2025-03-18
- overall geometric mean: 1.111x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-linux-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 256 ms: 1.07x faster                                         |
| docutils       | 2.77 sec                                               | 2.62 sec: 1.06x faster                                       |
| Geometric mean | (ref)                                                  | 1.06x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-linux-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 611 ms: 1.94x faster                                         |
| async_tree_io              | 1.16 sec                                               | 610 ms: 1.89x faster                                         |
| async_tree_none            | 472 ms                                                 | 256 ms: 1.84x faster                                         |
| async_tree_memoization     | 578 ms                                                 | 315 ms: 1.83x faster                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                         |
| async_tree_none_tg         | 450 ms                                                 | 248 ms: 1.81x faster                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 471 ms: 1.54x faster                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 487 ms: 1.49x faster                                         |
| Geometric mean             | (ref)                                                  | 1.77x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-linux-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.0 ms: 1.21x faster                                        |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                         |
| nbody          | 97.0 ms                                                | 98.1 ms: 1.01x slower                                        |
| Geometric mean | (ref)                                                  | 1.06x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-linux-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 126 ms: 1.17x faster                                         |
| regex_effbot   | 3.61 ms                                                | 3.26 ms: 1.11x faster                                        |
| regex_dna      | 212 ms                                                 | 221 ms: 1.04x slower                                         |
| regex_v8       | 23.1 ms                                                | 24.2 ms: 1.05x slower                                        |
| Geometric mean | (ref)                                                  | 1.04x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-linux-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.00 sec: 1.16x faster                                       |
| xml_etree_parse      | 159 ms                                                 | 142 ms: 1.13x faster                                         |
| xml_etree_iterparse  | 107 ms                                                 | 98.2 ms: 1.09x faster                                        |
| xml_etree_process    | 61.7 ms                                                | 58.3 ms: 1.06x faster                                        |
| xml_etree_generate   | 89.2 ms                                                | 84.2 ms: 1.06x faster                                        |
| unpickle_pure_python | 230 us                                                 | 218 us: 1.06x faster                                         |
| pickle_pure_python   | 324 us                                                 | 315 us: 1.03x faster                                         |
| json_loads           | 28.5 us                                                | 30.1 us: 1.06x slower                                        |
| json_dumps           | 10.4 ms                                                | 11.4 ms: 1.10x slower                                        |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-linux-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.21 ms: 1.18x slower                                        |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.37x slower                                        |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-linux-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.6 ms: 1.10x faster                                        |
| mako            | 11.9 ms                                                | 11.3 ms: 1.05x faster                                        |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-linux-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 611 ms: 1.94x faster                                         |
| async_tree_io              | 1.16 sec                                               | 610 ms: 1.89x faster                                         |
| async_tree_none            | 472 ms                                                 | 256 ms: 1.84x faster                                         |
| async_tree_memoization     | 578 ms                                                 | 315 ms: 1.83x faster                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                         |
| async_tree_none_tg         | 450 ms                                                 | 248 ms: 1.81x faster                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 471 ms: 1.54x faster                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 487 ms: 1.49x faster                                         |
| deepcopy                   | 371 us                                                 | 255 us: 1.46x faster                                         |
| deepcopy_memo              | 40.7 us                                                | 29.1 us: 1.40x faster                                        |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.30x faster                                        |
| deepcopy_reduce            | 3.35 us                                                | 2.66 us: 1.26x faster                                        |
| go                         | 139 ms                                                 | 113 ms: 1.23x faster                                         |
| float                      | 84.7 ms                                                | 70.0 ms: 1.21x faster                                        |
| deltablue                  | 3.72 ms                                                | 3.11 ms: 1.20x faster                                        |
| async_generators           | 463 ms                                                 | 390 ms: 1.19x faster                                         |
| raytrace                   | 312 ms                                                 | 265 ms: 1.18x faster                                         |
| spectral_norm              | 115 ms                                                 | 97.7 ms: 1.18x faster                                        |
| dulwich_log                | 68.5 ms                                                | 58.3 ms: 1.18x faster                                        |
| regex_compile              | 148 ms                                                 | 126 ms: 1.17x faster                                         |
| pathlib                    | 19.3 ms                                                | 16.5 ms: 1.17x faster                                        |
| tomli_loads                | 2.33 sec                                               | 2.00 sec: 1.16x faster                                       |
| logging_simple             | 6.46 us                                                | 5.54 us: 1.16x faster                                        |
| logging_format             | 7.23 us                                                | 6.23 us: 1.16x faster                                        |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                         |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.4 ms: 1.14x faster                                        |
| xml_etree_parse            | 159 ms                                                 | 142 ms: 1.13x faster                                         |
| sqlalchemy_declarative     | 147 ms                                                 | 131 ms: 1.12x faster                                         |
| chaos                      | 67.0 ms                                                | 59.8 ms: 1.12x faster                                        |
| sympy_str                  | 300 ms                                                 | 269 ms: 1.12x faster                                         |
| logging_silent             | 104 ns                                                 | 94.2 ns: 1.11x faster                                        |
| regex_effbot               | 3.61 ms                                                | 3.26 ms: 1.11x faster                                        |
| scimark_monte_carlo        | 75.1 ms                                                | 68.5 ms: 1.10x faster                                        |
| django_template            | 34.6 ms                                                | 31.6 ms: 1.10x faster                                        |
| generators                 | 31.2 ms                                                | 28.6 ms: 1.09x faster                                        |
| scimark_fft                | 382 ms                                                 | 350 ms: 1.09x faster                                         |
| scimark_sor                | 129 ms                                                 | 118 ms: 1.09x faster                                         |
| richards                   | 45.8 ms                                                | 42.1 ms: 1.09x faster                                        |
| xml_etree_iterparse        | 107 ms                                                 | 98.2 ms: 1.09x faster                                        |
| sympy_integrate            | 21.4 ms                                                | 19.8 ms: 1.08x faster                                        |
| crypto_pyaes               | 81.9 ms                                                | 75.8 ms: 1.08x faster                                        |
| 2to3                       | 274 ms                                                 | 256 ms: 1.07x faster                                         |
| pprint_safe_repr           | 776 ms                                                 | 725 ms: 1.07x faster                                         |
| pprint_pformat             | 1.57 sec                                               | 1.47 sec: 1.07x faster                                       |
| pyflate                    | 482 ms                                                 | 454 ms: 1.06x faster                                         |
| xml_etree_process          | 61.7 ms                                                | 58.3 ms: 1.06x faster                                        |
| richards_super             | 51.5 ms                                                | 48.6 ms: 1.06x faster                                        |
| xml_etree_generate         | 89.2 ms                                                | 84.2 ms: 1.06x faster                                        |
| docutils                   | 2.77 sec                                               | 2.62 sec: 1.06x faster                                       |
| unpickle_pure_python       | 230 us                                                 | 218 us: 1.06x faster                                         |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                         |
| mako                       | 11.9 ms                                                | 11.3 ms: 1.05x faster                                        |
| sympy_expand               | 478 ms                                                 | 456 ms: 1.05x faster                                         |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.04x faster                                       |
| pickle_pure_python         | 324 us                                                 | 315 us: 1.03x faster                                         |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.03x faster                                         |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.94 ms: 1.02x faster                                        |
| sqlite_synth               | 2.83 us                                                | 2.77 us: 1.02x faster                                        |
| hexiom                     | 6.41 ms                                                | 6.31 ms: 1.02x faster                                        |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                         |
| nbody                      | 97.0 ms                                                | 98.1 ms: 1.01x slower                                        |
| nqueens                    | 83.3 ms                                                | 84.3 ms: 1.01x slower                                        |
| mdp                        | 2.63 sec                                               | 2.66 sec: 1.01x slower                                       |
| json                       | 5.26 ms                                                | 5.32 ms: 1.01x slower                                        |
| bench_thread_pool          | 842 us                                                 | 869 us: 1.03x slower                                         |
| fannkuch                   | 417 ms                                                 | 432 ms: 1.04x slower                                         |
| regex_dna                  | 212 ms                                                 | 221 ms: 1.04x slower                                         |
| coroutines                 | 23.2 ms                                                | 24.2 ms: 1.04x slower                                        |
| regex_v8                   | 23.1 ms                                                | 24.2 ms: 1.05x slower                                        |
| typing_runtime_protocols   | 158 us                                                 | 166 us: 1.05x slower                                         |
| json_loads                 | 28.5 us                                                | 30.1 us: 1.06x slower                                        |
| telco                      | 7.10 ms                                                | 7.80 ms: 1.10x slower                                        |
| json_dumps                 | 10.4 ms                                                | 11.4 ms: 1.10x slower                                        |
| python_startup_no_site     | 6.94 ms                                                | 8.21 ms: 1.18x slower                                        |
| coverage                   | 72.7 ms                                                | 90.8 ms: 1.25x slower                                        |
| gc_traversal               | 3.79 ms                                                | 4.92 ms: 1.30x slower                                        |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.37x slower                                        |
| create_gc_cycles           | 1.48 ms                                                | 2.50 ms: 1.69x slower                                        |
| bench_mp_pool              | 24.0 ms                                                | 82.9 ms: 3.45x slower                                        |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                 |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250318-3.14.0a6+-0a71905/bm-20250318-linux-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.111x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.10x