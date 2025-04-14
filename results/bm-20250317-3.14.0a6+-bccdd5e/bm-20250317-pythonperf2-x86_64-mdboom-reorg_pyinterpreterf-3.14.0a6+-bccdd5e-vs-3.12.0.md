# Results vs. 3.12.0

- fork: mdboom
- ref: reorg_pyinterpreterf
- machine: linux-x86_64
- commit hash: bccdd5e
- commit date: 2025-03-17
- overall geometric mean: 1.022x faster
- HPT reliability: 72.94%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-bccdd5e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| docutils       | 2.87 sec                                                     | 2.93 sec: 1.02x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-bccdd5e |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 647 ms: 1.63x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 642 ms: 1.62x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 339 ms: 1.60x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 275 ms: 1.57x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 350 ms: 1.55x faster                                                         |
| async_tree_none            | 452 ms                                                       | 292 ms: 1.55x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 507 ms: 1.38x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 523 ms: 1.33x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.52x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-bccdd5e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 71.6 ms: 1.07x faster                                                        |
| pidigits       | 265 ms                                                       | 254 ms: 1.04x faster                                                         |
| nbody          | 88.0 ms                                                      | 108 ms: 1.23x slower                                                         |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-bccdd5e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.14 ms: 1.14x faster                                                        |
| regex_compile  | 144 ms                                                       | 136 ms: 1.06x faster                                                         |
| regex_dna      | 239 ms                                                       | 234 ms: 1.02x faster                                                         |
| regex_v8       | 23.6 ms                                                      | 23.5 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-bccdd5e |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 101 ms: 1.02x faster                                                         |
| xml_etree_parse      | 144 ms                                                       | 141 ms: 1.02x faster                                                         |
| xml_etree_generate   | 86.1 ms                                                      | 84.8 ms: 1.02x faster                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.20 sec: 1.02x slower                                                       |
| xml_etree_process    | 58.4 ms                                                      | 60.2 ms: 1.03x slower                                                        |
| pickle_pure_python   | 318 us                                                       | 335 us: 1.05x slower                                                         |
| json_loads           | 24.4 us                                                      | 25.7 us: 1.05x slower                                                        |
| unpickle_pure_python | 210 us                                                       | 226 us: 1.08x slower                                                         |
| json_dumps           | 10.2 ms                                                      | 11.4 ms: 1.11x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.03x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-bccdd5e |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 10.5 ms: 1.21x slower                                                        |
| python_startup         | 11.6 ms                                                      | 16.4 ms: 1.41x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-bccdd5e |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 37.0 ms: 1.03x faster                                                        |
| mako            | 10.0 ms                                                      | 11.1 ms: 1.11x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.04x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-bccdd5e |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 647 ms: 1.63x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 642 ms: 1.62x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 339 ms: 1.60x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 275 ms: 1.57x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 350 ms: 1.55x faster                                                         |
| async_tree_none            | 452 ms                                                       | 292 ms: 1.55x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 507 ms: 1.38x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 523 ms: 1.33x faster                                                         |
| generators                 | 37.4 ms                                                      | 28.2 ms: 1.33x faster                                                        |
| deepcopy                   | 368 us                                                       | 295 us: 1.25x faster                                                         |
| comprehensions             | 21.9 us                                                      | 17.7 us: 1.24x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 29.7 us: 1.24x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.14 ms: 1.14x faster                                                        |
| go                         | 150 ms                                                       | 133 ms: 1.12x faster                                                         |
| deepcopy_reduce            | 3.37 us                                                      | 3.01 us: 1.12x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 17.2 ms: 1.10x faster                                                        |
| sqlalchemy_declarative     | 159 ms                                                       | 146 ms: 1.09x faster                                                         |
| coroutines                 | 23.0 ms                                                      | 21.1 ms: 1.09x faster                                                        |
| float                      | 76.6 ms                                                      | 71.6 ms: 1.07x faster                                                        |
| logging_format             | 7.48 us                                                      | 7.05 us: 1.06x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.33 us: 1.06x faster                                                        |
| regex_compile              | 144 ms                                                       | 136 ms: 1.06x faster                                                         |
| scimark_monte_carlo        | 69.0 ms                                                      | 66.0 ms: 1.05x faster                                                        |
| pidigits                   | 265 ms                                                       | 254 ms: 1.04x faster                                                         |
| dulwich_log                | 65.4 ms                                                      | 62.7 ms: 1.04x faster                                                        |
| sympy_sum                  | 162 ms                                                       | 156 ms: 1.04x faster                                                         |
| django_template            | 38.2 ms                                                      | 37.0 ms: 1.03x faster                                                        |
| mdp                        | 2.57 sec                                                     | 2.50 sec: 1.03x faster                                                       |
| sqlalchemy_imperative      | 18.7 ms                                                      | 18.3 ms: 1.02x faster                                                        |
| sympy_str                  | 302 ms                                                       | 296 ms: 1.02x faster                                                         |
| xml_etree_iterparse        | 103 ms                                                       | 101 ms: 1.02x faster                                                         |
| regex_dna                  | 239 ms                                                       | 234 ms: 1.02x faster                                                         |
| sympy_integrate            | 23.9 ms                                                      | 23.5 ms: 1.02x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 141 ms: 1.02x faster                                                         |
| spectral_norm              | 91.6 ms                                                      | 90.1 ms: 1.02x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 84.8 ms: 1.02x faster                                                        |
| asyncio_websockets         | 387 ms                                                       | 383 ms: 1.01x faster                                                         |
| regex_v8                   | 23.6 ms                                                      | 23.5 ms: 1.00x faster                                                        |
| chaos                      | 64.0 ms                                                      | 64.3 ms: 1.00x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 95.7 ns: 1.01x slower                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.68 sec: 1.02x slower                                                       |
| scimark_sor                | 109 ms                                                       | 111 ms: 1.02x slower                                                         |
| tomli_loads                | 2.16 sec                                                     | 2.20 sec: 1.02x slower                                                       |
| sqlite_synth               | 2.77 us                                                      | 2.82 us: 1.02x slower                                                        |
| pprint_safe_repr           | 807 ms                                                       | 822 ms: 1.02x slower                                                         |
| docutils                   | 2.87 sec                                                     | 2.93 sec: 1.02x slower                                                       |
| scimark_lu                 | 98.8 ms                                                      | 102 ms: 1.03x slower                                                         |
| json                       | 5.12 ms                                                      | 5.27 ms: 1.03x slower                                                        |
| xml_etree_process          | 58.4 ms                                                      | 60.2 ms: 1.03x slower                                                        |
| sympy_expand               | 484 ms                                                       | 503 ms: 1.04x slower                                                         |
| crypto_pyaes               | 80.3 ms                                                      | 83.6 ms: 1.04x slower                                                        |
| richards                   | 45.7 ms                                                      | 47.8 ms: 1.04x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 3.39 ms: 1.05x slower                                                        |
| pycparser                  | 1.23 sec                                                     | 1.29 sec: 1.05x slower                                                       |
| richards_super             | 51.3 ms                                                      | 54.0 ms: 1.05x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 335 us: 1.05x slower                                                         |
| json_loads                 | 24.4 us                                                      | 25.7 us: 1.05x slower                                                        |
| scimark_fft                | 301 ms                                                       | 319 ms: 1.06x slower                                                         |
| async_generators           | 390 ms                                                       | 416 ms: 1.06x slower                                                         |
| pyflate                    | 439 ms                                                       | 470 ms: 1.07x slower                                                         |
| nqueens                    | 89.9 ms                                                      | 96.3 ms: 1.07x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 226 us: 1.08x slower                                                         |
| hexiom                     | 5.96 ms                                                      | 6.44 ms: 1.08x slower                                                        |
| mako                       | 10.0 ms                                                      | 11.1 ms: 1.11x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 11.4 ms: 1.11x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.71 ms: 1.12x slower                                                        |
| fannkuch                   | 350 ms                                                       | 393 ms: 1.12x slower                                                         |
| telco                      | 6.96 ms                                                      | 7.98 ms: 1.15x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 174 us: 1.15x slower                                                         |
| python_startup_no_site     | 8.64 ms                                                      | 10.5 ms: 1.21x slower                                                        |
| nbody                      | 88.0 ms                                                      | 108 ms: 1.23x slower                                                         |
| coverage                   | 66.7 ms                                                      | 82.6 ms: 1.24x slower                                                        |
| python_startup             | 11.6 ms                                                      | 16.4 ms: 1.41x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.82 ms: 1.77x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 6.58 ms: 1.89x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 1.69 sec: 355.49x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.05x slower                                                                 |

Benchmark hidden because not significant (4): raytrace, 2to3, bench_thread_pool, meteor_contest
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250317-3.14.0a6+-bccdd5e/bm-20250317-pythonperf2-x86_64-mdboom-reorg_pyinterpreterf-3.14.0a6+-bccdd5e.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.022x faster

# HPT report

- Reliability score: 72.94% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x