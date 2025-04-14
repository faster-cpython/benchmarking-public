# Results vs. 3.12.0

- fork: mdboom
- ref: reorg_pyinterpreterf
- machine: linux-x86_64
- commit hash: 37fd664
- commit date: 2025-03-17
- overall geometric mean: 1.023x faster
- HPT reliability: 70.49%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-37fd664 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| docutils       | 2.87 sec                                                     | 2.91 sec: 1.02x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-37fd664 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 649 ms: 1.62x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 645 ms: 1.62x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 341 ms: 1.59x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 275 ms: 1.56x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 351 ms: 1.55x faster                                                         |
| async_tree_none            | 452 ms                                                       | 292 ms: 1.54x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 508 ms: 1.37x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 523 ms: 1.33x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.52x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-37fd664 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 72.9 ms: 1.05x faster                                                        |
| pidigits       | 265 ms                                                       | 255 ms: 1.04x faster                                                         |
| nbody          | 88.0 ms                                                      | 101 ms: 1.15x slower                                                         |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-37fd664 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.13 ms: 1.14x faster                                                        |
| regex_compile  | 144 ms                                                       | 138 ms: 1.05x faster                                                         |
| regex_dna      | 239 ms                                                       | 237 ms: 1.01x faster                                                         |
| regex_v8       | 23.6 ms                                                      | 23.7 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-37fd664 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse      | 144 ms                                                       | 136 ms: 1.06x faster                                                         |
| xml_etree_iterparse  | 103 ms                                                       | 97.4 ms: 1.06x faster                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 85.0 ms: 1.01x faster                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.19 sec: 1.02x slower                                                       |
| xml_etree_process    | 58.4 ms                                                      | 60.4 ms: 1.03x slower                                                        |
| json_loads           | 24.4 us                                                      | 25.5 us: 1.05x slower                                                        |
| pickle_pure_python   | 318 us                                                       | 338 us: 1.06x slower                                                         |
| unpickle_pure_python | 210 us                                                       | 225 us: 1.07x slower                                                         |
| json_dumps           | 10.2 ms                                                      | 11.4 ms: 1.11x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-37fd664 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 10.5 ms: 1.21x slower                                                        |
| python_startup         | 11.6 ms                                                      | 16.3 ms: 1.40x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.30x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-37fd664 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 36.8 ms: 1.04x faster                                                        |
| mako            | 10.0 ms                                                      | 11.0 ms: 1.10x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-37fd664 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 649 ms: 1.62x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 645 ms: 1.62x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 341 ms: 1.59x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 275 ms: 1.56x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 351 ms: 1.55x faster                                                         |
| async_tree_none            | 452 ms                                                       | 292 ms: 1.54x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 508 ms: 1.37x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 523 ms: 1.33x faster                                                         |
| generators                 | 37.4 ms                                                      | 29.4 ms: 1.27x faster                                                        |
| deepcopy                   | 368 us                                                       | 292 us: 1.26x faster                                                         |
| deepcopy_memo              | 36.8 us                                                      | 29.6 us: 1.24x faster                                                        |
| comprehensions             | 21.9 us                                                      | 17.8 us: 1.23x faster                                                        |
| go                         | 150 ms                                                       | 131 ms: 1.15x faster                                                         |
| regex_effbot               | 3.57 ms                                                      | 3.13 ms: 1.14x faster                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 3.04 us: 1.11x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 17.3 ms: 1.09x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 21.1 ms: 1.09x faster                                                        |
| sqlalchemy_declarative     | 159 ms                                                       | 147 ms: 1.08x faster                                                         |
| xml_etree_parse            | 144 ms                                                       | 136 ms: 1.06x faster                                                         |
| xml_etree_iterparse        | 103 ms                                                       | 97.4 ms: 1.06x faster                                                        |
| float                      | 76.6 ms                                                      | 72.9 ms: 1.05x faster                                                        |
| logging_format             | 7.48 us                                                      | 7.13 us: 1.05x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.41 us: 1.05x faster                                                        |
| regex_compile              | 144 ms                                                       | 138 ms: 1.05x faster                                                         |
| dulwich_log                | 65.4 ms                                                      | 62.6 ms: 1.04x faster                                                        |
| sqlalchemy_imperative      | 18.7 ms                                                      | 18.0 ms: 1.04x faster                                                        |
| pidigits                   | 265 ms                                                       | 255 ms: 1.04x faster                                                         |
| sympy_sum                  | 162 ms                                                       | 156 ms: 1.04x faster                                                         |
| django_template            | 38.2 ms                                                      | 36.8 ms: 1.04x faster                                                        |
| sympy_integrate            | 23.9 ms                                                      | 23.4 ms: 1.02x faster                                                        |
| sympy_str                  | 302 ms                                                       | 297 ms: 1.02x faster                                                         |
| xml_etree_generate         | 86.1 ms                                                      | 85.0 ms: 1.01x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 68.1 ms: 1.01x faster                                                        |
| regex_dna                  | 239 ms                                                       | 237 ms: 1.01x faster                                                         |
| asyncio_websockets         | 387 ms                                                       | 384 ms: 1.01x faster                                                         |
| mdp                        | 2.57 sec                                                     | 2.56 sec: 1.00x faster                                                       |
| regex_v8                   | 23.6 ms                                                      | 23.7 ms: 1.00x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 95.0 ns: 1.01x slower                                                        |
| chaos                      | 64.0 ms                                                      | 64.5 ms: 1.01x slower                                                        |
| scimark_sor                | 109 ms                                                       | 110 ms: 1.01x slower                                                         |
| pycparser                  | 1.23 sec                                                     | 1.25 sec: 1.01x slower                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.19 sec: 1.02x slower                                                       |
| docutils                   | 2.87 sec                                                     | 2.91 sec: 1.02x slower                                                       |
| sqlite_synth               | 2.77 us                                                      | 2.82 us: 1.02x slower                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.69 sec: 1.02x slower                                                       |
| json                       | 5.12 ms                                                      | 5.24 ms: 1.02x slower                                                        |
| pyflate                    | 439 ms                                                       | 452 ms: 1.03x slower                                                         |
| xml_etree_process          | 58.4 ms                                                      | 60.4 ms: 1.03x slower                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 83.4 ms: 1.04x slower                                                        |
| pprint_safe_repr           | 807 ms                                                       | 838 ms: 1.04x slower                                                         |
| richards_super             | 51.3 ms                                                      | 53.6 ms: 1.04x slower                                                        |
| scimark_fft                | 301 ms                                                       | 314 ms: 1.04x slower                                                         |
| json_loads                 | 24.4 us                                                      | 25.5 us: 1.05x slower                                                        |
| sympy_expand               | 484 ms                                                       | 508 ms: 1.05x slower                                                         |
| deltablue                  | 3.24 ms                                                      | 3.40 ms: 1.05x slower                                                        |
| async_generators           | 390 ms                                                       | 413 ms: 1.06x slower                                                         |
| pickle_pure_python         | 318 us                                                       | 338 us: 1.06x slower                                                         |
| richards                   | 45.7 ms                                                      | 48.7 ms: 1.06x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 95.9 ms: 1.07x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 225 us: 1.07x slower                                                         |
| fannkuch                   | 350 ms                                                       | 378 ms: 1.08x slower                                                         |
| hexiom                     | 5.96 ms                                                      | 6.48 ms: 1.09x slower                                                        |
| mako                       | 10.0 ms                                                      | 11.0 ms: 1.10x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 168 us: 1.11x slower                                                         |
| json_dumps                 | 10.2 ms                                                      | 11.4 ms: 1.11x slower                                                        |
| nbody                      | 88.0 ms                                                      | 101 ms: 1.15x slower                                                         |
| telco                      | 6.96 ms                                                      | 7.99 ms: 1.15x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.86 ms: 1.15x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 10.5 ms: 1.21x slower                                                        |
| coverage                   | 66.7 ms                                                      | 82.0 ms: 1.23x slower                                                        |
| python_startup             | 11.6 ms                                                      | 16.3 ms: 1.40x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.77 ms: 1.74x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 6.58 ms: 1.89x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 1.74 sec: 366.01x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.05x slower                                                                 |

Benchmark hidden because not significant (6): 2to3, spectral_norm, raytrace, meteor_contest, scimark_lu, bench_thread_pool
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250317-3.14.0a6+-37fd664/bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-37fd664.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.023x faster

# HPT report

- Reliability score: 70.49% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x