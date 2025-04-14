# Results vs. 3.12.0

- fork: mdboom
- ref: tuple_hash_cache
- machine: linux-x86_64
- commit hash: bd82b00
- commit date: 2025-03-19
- overall geometric mean: 1.018x faster
- HPT reliability: 59.01%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-pythonperf2-x86_64-mdboom-tuple_hash_cache-3.14.0a6+-bd82b00 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 289 ms: 1.01x slower                                                     |
| docutils       | 2.87 sec                                                     | 2.94 sec: 1.02x slower                                                   |
| Geometric mean | (ref)                                                        | 1.02x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-pythonperf2-x86_64-mdboom-tuple_hash_cache-3.14.0a6+-bd82b00 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 654 ms: 1.61x faster                                                     |
| async_tree_io              | 1.04 sec                                                     | 649 ms: 1.61x faster                                                     |
| async_tree_memoization     | 544 ms                                                       | 357 ms: 1.53x faster                                                     |
| async_tree_none_tg         | 431 ms                                                       | 286 ms: 1.51x faster                                                     |
| async_tree_none            | 452 ms                                                       | 300 ms: 1.51x faster                                                     |
| async_tree_memoization_tg  | 540 ms                                                       | 360 ms: 1.50x faster                                                     |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 523 ms: 1.33x faster                                                     |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 529 ms: 1.32x faster                                                     |
| Geometric mean             | (ref)                                                        | 1.48x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-pythonperf2-x86_64-mdboom-tuple_hash_cache-3.14.0a6+-bd82b00 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 71.7 ms: 1.07x faster                                                    |
| pidigits       | 265 ms                                                       | 254 ms: 1.04x faster                                                     |
| nbody          | 88.0 ms                                                      | 104 ms: 1.19x slower                                                     |
| Geometric mean | (ref)                                                        | 1.02x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-pythonperf2-x86_64-mdboom-tuple_hash_cache-3.14.0a6+-bd82b00 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.23 ms: 1.10x faster                                                    |
| regex_compile  | 144 ms                                                       | 138 ms: 1.04x faster                                                     |
| regex_v8       | 23.6 ms                                                      | 24.0 ms: 1.01x slower                                                    |
| regex_dna      | 239 ms                                                       | 246 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                        | 1.02x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-pythonperf2-x86_64-mdboom-tuple_hash_cache-3.14.0a6+-bd82b00 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 144 ms                                                       | 137 ms: 1.05x faster                                                     |
| xml_etree_iterparse  | 103 ms                                                       | 100 ms: 1.02x faster                                                     |
| xml_etree_generate   | 86.1 ms                                                      | 85.1 ms: 1.01x faster                                                    |
| tomli_loads          | 2.16 sec                                                     | 2.17 sec: 1.01x slower                                                   |
| xml_etree_process    | 58.4 ms                                                      | 60.6 ms: 1.04x slower                                                    |
| unpickle_pure_python | 210 us                                                       | 222 us: 1.06x slower                                                     |
| pickle_pure_python   | 318 us                                                       | 346 us: 1.09x slower                                                     |
| json_loads           | 24.4 us                                                      | 26.6 us: 1.09x slower                                                    |
| json_dumps           | 10.2 ms                                                      | 11.7 ms: 1.14x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.04x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-pythonperf2-x86_64-mdboom-tuple_hash_cache-3.14.0a6+-bd82b00 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 10.5 ms: 1.22x slower                                                    |
| python_startup         | 11.6 ms                                                      | 16.5 ms: 1.42x slower                                                    |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-pythonperf2-x86_64-mdboom-tuple_hash_cache-3.14.0a6+-bd82b00 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 37.9 ms: 1.01x faster                                                    |
| mako            | 10.0 ms                                                      | 11.2 ms: 1.12x slower                                                    |
| Geometric mean  | (ref)                                                        | 1.06x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-pythonperf2-x86_64-mdboom-tuple_hash_cache-3.14.0a6+-bd82b00 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.36 sec: 1.89x faster                                                   |
| async_tree_io_tg           | 1.05 sec                                                     | 654 ms: 1.61x faster                                                     |
| async_tree_io              | 1.04 sec                                                     | 649 ms: 1.61x faster                                                     |
| async_tree_memoization     | 544 ms                                                       | 357 ms: 1.53x faster                                                     |
| async_tree_none_tg         | 431 ms                                                       | 286 ms: 1.51x faster                                                     |
| async_tree_none            | 452 ms                                                       | 300 ms: 1.51x faster                                                     |
| async_tree_memoization_tg  | 540 ms                                                       | 360 ms: 1.50x faster                                                     |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 523 ms: 1.33x faster                                                     |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 529 ms: 1.32x faster                                                     |
| generators                 | 37.4 ms                                                      | 29.0 ms: 1.29x faster                                                    |
| deepcopy_memo              | 36.8 us                                                      | 29.4 us: 1.25x faster                                                    |
| deepcopy                   | 368 us                                                       | 297 us: 1.24x faster                                                     |
| comprehensions             | 21.9 us                                                      | 17.8 us: 1.23x faster                                                    |
| deepcopy_reduce            | 3.37 us                                                      | 3.02 us: 1.11x faster                                                    |
| go                         | 150 ms                                                       | 135 ms: 1.11x faster                                                     |
| regex_effbot               | 3.57 ms                                                      | 3.23 ms: 1.10x faster                                                    |
| pathlib                    | 18.9 ms                                                      | 17.1 ms: 1.10x faster                                                    |
| coroutines                 | 23.0 ms                                                      | 21.3 ms: 1.08x faster                                                    |
| float                      | 76.6 ms                                                      | 71.7 ms: 1.07x faster                                                    |
| sqlalchemy_declarative     | 159 ms                                                       | 149 ms: 1.07x faster                                                     |
| xml_etree_parse            | 144 ms                                                       | 137 ms: 1.05x faster                                                     |
| regex_compile              | 144 ms                                                       | 138 ms: 1.04x faster                                                     |
| pidigits                   | 265 ms                                                       | 254 ms: 1.04x faster                                                     |
| dulwich_log                | 65.4 ms                                                      | 63.0 ms: 1.04x faster                                                    |
| sympy_sum                  | 162 ms                                                       | 157 ms: 1.03x faster                                                     |
| xml_etree_iterparse        | 103 ms                                                       | 100 ms: 1.02x faster                                                     |
| logging_format             | 7.48 us                                                      | 7.34 us: 1.02x faster                                                    |
| sympy_integrate            | 23.9 ms                                                      | 23.6 ms: 1.01x faster                                                    |
| sqlalchemy_imperative      | 18.7 ms                                                      | 18.5 ms: 1.01x faster                                                    |
| xml_etree_generate         | 86.1 ms                                                      | 85.1 ms: 1.01x faster                                                    |
| spectral_norm              | 91.6 ms                                                      | 90.9 ms: 1.01x faster                                                    |
| django_template            | 38.2 ms                                                      | 37.9 ms: 1.01x faster                                                    |
| sympy_str                  | 302 ms                                                       | 301 ms: 1.01x faster                                                     |
| meteor_contest             | 128 ms                                                       | 129 ms: 1.00x slower                                                     |
| tomli_loads                | 2.16 sec                                                     | 2.17 sec: 1.01x slower                                                   |
| logging_simple             | 6.71 us                                                      | 6.76 us: 1.01x slower                                                    |
| logging_silent             | 94.4 ns                                                      | 95.4 ns: 1.01x slower                                                    |
| 2to3                       | 285 ms                                                       | 289 ms: 1.01x slower                                                     |
| regex_v8                   | 23.6 ms                                                      | 24.0 ms: 1.01x slower                                                    |
| sqlite_synth               | 2.77 us                                                      | 2.82 us: 1.02x slower                                                    |
| scimark_lu                 | 98.8 ms                                                      | 100 ms: 1.02x slower                                                     |
| bench_thread_pool          | 950 us                                                       | 968 us: 1.02x slower                                                     |
| scimark_sor                | 109 ms                                                       | 111 ms: 1.02x slower                                                     |
| pprint_pformat             | 1.65 sec                                                     | 1.69 sec: 1.02x slower                                                   |
| docutils                   | 2.87 sec                                                     | 2.94 sec: 1.02x slower                                                   |
| crypto_pyaes               | 80.3 ms                                                      | 82.4 ms: 1.03x slower                                                    |
| regex_dna                  | 239 ms                                                       | 246 ms: 1.03x slower                                                     |
| pprint_safe_repr           | 807 ms                                                       | 836 ms: 1.04x slower                                                     |
| xml_etree_process          | 58.4 ms                                                      | 60.6 ms: 1.04x slower                                                    |
| richards                   | 45.7 ms                                                      | 47.7 ms: 1.04x slower                                                    |
| richards_super             | 51.3 ms                                                      | 53.6 ms: 1.04x slower                                                    |
| chaos                      | 64.0 ms                                                      | 67.1 ms: 1.05x slower                                                    |
| pyflate                    | 439 ms                                                       | 461 ms: 1.05x slower                                                     |
| pycparser                  | 1.23 sec                                                     | 1.30 sec: 1.05x slower                                                   |
| deltablue                  | 3.24 ms                                                      | 3.42 ms: 1.06x slower                                                    |
| sympy_expand               | 484 ms                                                       | 512 ms: 1.06x slower                                                     |
| unpickle_pure_python       | 210 us                                                       | 222 us: 1.06x slower                                                     |
| nqueens                    | 89.9 ms                                                      | 96.1 ms: 1.07x slower                                                    |
| scimark_fft                | 301 ms                                                       | 325 ms: 1.08x slower                                                     |
| pickle_pure_python         | 318 us                                                       | 346 us: 1.09x slower                                                     |
| hexiom                     | 5.96 ms                                                      | 6.48 ms: 1.09x slower                                                    |
| fannkuch                   | 350 ms                                                       | 382 ms: 1.09x slower                                                     |
| json                       | 5.12 ms                                                      | 5.59 ms: 1.09x slower                                                    |
| json_loads                 | 24.4 us                                                      | 26.6 us: 1.09x slower                                                    |
| async_generators           | 390 ms                                                       | 432 ms: 1.11x slower                                                     |
| mako                       | 10.0 ms                                                      | 11.2 ms: 1.12x slower                                                    |
| json_dumps                 | 10.2 ms                                                      | 11.7 ms: 1.14x slower                                                    |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.84 ms: 1.15x slower                                                    |
| typing_runtime_protocols   | 152 us                                                       | 177 us: 1.16x slower                                                     |
| telco                      | 6.96 ms                                                      | 8.22 ms: 1.18x slower                                                    |
| nbody                      | 88.0 ms                                                      | 104 ms: 1.19x slower                                                     |
| coverage                   | 66.7 ms                                                      | 79.6 ms: 1.19x slower                                                    |
| python_startup_no_site     | 8.64 ms                                                      | 10.5 ms: 1.22x slower                                                    |
| python_startup             | 11.6 ms                                                      | 16.5 ms: 1.42x slower                                                    |
| create_gc_cycles           | 1.59 ms                                                      | 2.83 ms: 1.78x slower                                                    |
| gc_traversal               | 3.48 ms                                                      | 6.39 ms: 1.84x slower                                                    |
| bench_mp_pool              | 4.76 ms                                                      | 1.58 sec: 331.51x slower                                                 |
| Geometric mean             | (ref)                                                        | 1.06x slower                                                             |

Benchmark hidden because not significant (3): scimark_monte_carlo, asyncio_websockets, raytrace
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250319-3.14.0a6+-bd82b00/bm-20250319-pythonperf2-x86_64-mdboom-tuple_hash_cache-3.14.0a6+-bd82b00.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.018x faster

# HPT report

- Reliability score: 59.01% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.06x