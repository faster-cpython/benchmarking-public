# Results vs. 3.12.0

- fork: iritkatriel
- ref: stats
- machine: linux-x86_64
- commit hash: fb33c24
- commit date: 2025-02-21
- overall geometric mean: 1.110x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 256 ms: 1.07x faster                                         |
| docutils       | 2.77 sec                                               | 2.62 sec: 1.06x faster                                       |
| Geometric mean | (ref)                                                  | 1.07x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 612 ms: 1.93x faster                                         |
| async_tree_io              | 1.16 sec                                               | 611 ms: 1.89x faster                                         |
| async_tree_none            | 472 ms                                                 | 260 ms: 1.81x faster                                         |
| async_tree_memoization     | 578 ms                                                 | 320 ms: 1.80x faster                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 319 ms: 1.80x faster                                         |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.79x faster                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 476 ms: 1.52x faster                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 493 ms: 1.47x faster                                         |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 84.7 ms                                                | 72.7 ms: 1.16x faster                                        |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                         |
| nbody          | 97.0 ms                                                | 97.6 ms: 1.01x slower                                        |
| Geometric mean | (ref)                                                  | 1.05x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 126 ms: 1.18x faster                                         |
| regex_effbot   | 3.61 ms                                                | 3.46 ms: 1.04x faster                                        |
| regex_v8       | 23.1 ms                                                | 23.3 ms: 1.01x slower                                        |
| regex_dna      | 212 ms                                                 | 221 ms: 1.04x slower                                         |
| Geometric mean | (ref)                                                  | 1.04x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.96 sec: 1.19x faster                                       |
| xml_etree_parse      | 159 ms                                                 | 139 ms: 1.15x faster                                         |
| xml_etree_iterparse  | 107 ms                                                 | 98.1 ms: 1.09x faster                                        |
| xml_etree_generate   | 89.2 ms                                                | 83.9 ms: 1.06x faster                                        |
| xml_etree_process    | 61.7 ms                                                | 58.7 ms: 1.05x faster                                        |
| unpickle_pure_python | 230 us                                                 | 222 us: 1.04x faster                                         |
| pickle_pure_python   | 324 us                                                 | 319 us: 1.02x faster                                         |
| json_loads           | 28.5 us                                                | 29.7 us: 1.04x slower                                        |
| json_dumps           | 10.4 ms                                                | 11.8 ms: 1.13x slower                                        |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.06 ms: 1.02x slower                                        |
| python_startup         | 9.55 ms                                                | 12.9 ms: 1.35x slower                                        |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.8 ms: 1.09x faster                                        |
| mako            | 11.9 ms                                                | 11.2 ms: 1.06x faster                                        |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 612 ms: 1.93x faster                                         |
| async_tree_io              | 1.16 sec                                               | 611 ms: 1.89x faster                                         |
| async_tree_none            | 472 ms                                                 | 260 ms: 1.81x faster                                         |
| async_tree_memoization     | 578 ms                                                 | 320 ms: 1.80x faster                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 319 ms: 1.80x faster                                         |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.79x faster                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 476 ms: 1.52x faster                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 493 ms: 1.47x faster                                         |
| deepcopy                   | 371 us                                                 | 257 us: 1.45x faster                                         |
| deepcopy_memo              | 40.7 us                                                | 30.1 us: 1.35x faster                                        |
| comprehensions             | 21.8 us                                                | 16.4 us: 1.33x faster                                        |
| deepcopy_reduce            | 3.35 us                                                | 2.66 us: 1.26x faster                                        |
| async_generators           | 463 ms                                                 | 387 ms: 1.20x faster                                         |
| deltablue                  | 3.72 ms                                                | 3.12 ms: 1.19x faster                                        |
| tomli_loads                | 2.33 sec                                               | 1.96 sec: 1.19x faster                                       |
| go                         | 139 ms                                                 | 118 ms: 1.19x faster                                         |
| spectral_norm              | 115 ms                                                 | 97.4 ms: 1.18x faster                                        |
| regex_compile              | 148 ms                                                 | 126 ms: 1.18x faster                                         |
| float                      | 84.7 ms                                                | 72.7 ms: 1.16x faster                                        |
| logging_format             | 7.23 us                                                | 6.22 us: 1.16x faster                                        |
| logging_simple             | 6.46 us                                                | 5.56 us: 1.16x faster                                        |
| pathlib                    | 19.3 ms                                                | 16.7 ms: 1.16x faster                                        |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                         |
| sqlalchemy_declarative     | 147 ms                                                 | 128 ms: 1.15x faster                                         |
| xml_etree_parse            | 159 ms                                                 | 139 ms: 1.15x faster                                         |
| raytrace                   | 312 ms                                                 | 273 ms: 1.14x faster                                         |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.4 ms: 1.14x faster                                        |
| chaos                      | 67.0 ms                                                | 59.4 ms: 1.13x faster                                        |
| sympy_str                  | 300 ms                                                 | 267 ms: 1.12x faster                                         |
| generators                 | 31.2 ms                                                | 28.0 ms: 1.11x faster                                        |
| scimark_monte_carlo        | 75.1 ms                                                | 67.8 ms: 1.11x faster                                        |
| scimark_fft                | 382 ms                                                 | 348 ms: 1.10x faster                                         |
| crypto_pyaes               | 81.9 ms                                                | 74.7 ms: 1.10x faster                                        |
| xml_etree_iterparse        | 107 ms                                                 | 98.1 ms: 1.09x faster                                        |
| sympy_integrate            | 21.4 ms                                                | 19.7 ms: 1.09x faster                                        |
| django_template            | 34.6 ms                                                | 31.8 ms: 1.09x faster                                        |
| 2to3                       | 274 ms                                                 | 256 ms: 1.07x faster                                         |
| pprint_safe_repr           | 776 ms                                                 | 723 ms: 1.07x faster                                         |
| dulwich_log                | 68.5 ms                                                | 64.0 ms: 1.07x faster                                        |
| pprint_pformat             | 1.57 sec                                               | 1.47 sec: 1.06x faster                                       |
| xml_etree_generate         | 89.2 ms                                                | 83.9 ms: 1.06x faster                                        |
| mako                       | 11.9 ms                                                | 11.2 ms: 1.06x faster                                        |
| docutils                   | 2.77 sec                                               | 2.62 sec: 1.06x faster                                       |
| mdp                        | 2.63 sec                                               | 2.50 sec: 1.05x faster                                       |
| sympy_expand               | 478 ms                                                 | 454 ms: 1.05x faster                                         |
| scimark_sor                | 129 ms                                                 | 123 ms: 1.05x faster                                         |
| xml_etree_process          | 61.7 ms                                                | 58.7 ms: 1.05x faster                                        |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.83 ms: 1.05x faster                                        |
| regex_effbot               | 3.61 ms                                                | 3.46 ms: 1.04x faster                                        |
| unpickle_pure_python       | 230 us                                                 | 222 us: 1.04x faster                                         |
| richards                   | 45.8 ms                                                | 44.4 ms: 1.03x faster                                        |
| hexiom                     | 6.41 ms                                                | 6.23 ms: 1.03x faster                                        |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                         |
| sqlite_synth               | 2.83 us                                                | 2.76 us: 1.03x faster                                        |
| pyflate                    | 482 ms                                                 | 470 ms: 1.03x faster                                         |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.02x faster                                         |
| nqueens                    | 83.3 ms                                                | 81.6 ms: 1.02x faster                                        |
| pickle_pure_python         | 324 us                                                 | 319 us: 1.02x faster                                         |
| richards_super             | 51.5 ms                                                | 50.7 ms: 1.02x faster                                        |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                         |
| fannkuch                   | 417 ms                                                 | 415 ms: 1.01x faster                                         |
| logging_silent             | 104 ns                                                 | 105 ns: 1.00x slower                                         |
| nbody                      | 97.0 ms                                                | 97.6 ms: 1.01x slower                                        |
| regex_v8                   | 23.1 ms                                                | 23.3 ms: 1.01x slower                                        |
| typing_runtime_protocols   | 158 us                                                 | 160 us: 1.01x slower                                         |
| json                       | 5.26 ms                                                | 5.32 ms: 1.01x slower                                        |
| python_startup_no_site     | 6.94 ms                                                | 7.06 ms: 1.02x slower                                        |
| coroutines                 | 23.2 ms                                                | 23.8 ms: 1.03x slower                                        |
| bench_thread_pool          | 842 us                                                 | 867 us: 1.03x slower                                         |
| regex_dna                  | 212 ms                                                 | 221 ms: 1.04x slower                                         |
| json_loads                 | 28.5 us                                                | 29.7 us: 1.04x slower                                        |
| telco                      | 7.10 ms                                                | 7.84 ms: 1.10x slower                                        |
| json_dumps                 | 10.4 ms                                                | 11.8 ms: 1.13x slower                                        |
| coverage                   | 72.7 ms                                                | 91.0 ms: 1.25x slower                                        |
| gc_traversal               | 3.79 ms                                                | 4.78 ms: 1.26x slower                                        |
| python_startup             | 9.55 ms                                                | 12.9 ms: 1.35x slower                                        |
| create_gc_cycles           | 1.48 ms                                                | 2.48 ms: 1.68x slower                                        |
| bench_mp_pool              | 24.0 ms                                                | 83.5 ms: 3.48x slower                                        |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                 |

Benchmark hidden because not significant (2): pycparser, asyncio_websockets
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.110x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.10x