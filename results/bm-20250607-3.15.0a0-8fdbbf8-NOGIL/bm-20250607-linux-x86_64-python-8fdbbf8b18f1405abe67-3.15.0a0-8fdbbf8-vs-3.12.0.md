# Results vs. 3.12.0

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: linux-x86_64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.155x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.07x slower
- Memory change: 1.38x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 339 ms: 1.24x slower                                                  |
| docutils       | 2.77 sec                                               | 3.14 sec: 1.13x slower                                                |
| Geometric mean | (ref)                                                  | 1.18x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 603 ms: 1.96x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 642 ms: 1.80x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 262 ms: 1.71x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 340 ms: 1.69x faster                                                  |
| async_tree_none            | 472 ms                                                 | 301 ms: 1.57x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 381 ms: 1.52x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 582 ms: 1.25x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 626 ms: 1.16x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.56x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 82.0 ms: 1.03x faster                                                 |
| pidigits       | 187 ms                                                 | 201 ms: 1.07x slower                                                  |
| nbody          | 97.0 ms                                                | 154 ms: 1.59x slower                                                  |
| Geometric mean | (ref)                                                  | 1.18x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 2.97 ms: 1.21x faster                                                 |
| regex_dna      | 212 ms                                                 | 192 ms: 1.11x faster                                                  |
| regex_v8       | 23.1 ms                                                | 23.7 ms: 1.02x slower                                                 |
| regex_compile  | 148 ms                                                 | 172 ms: 1.16x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_iterparse  | 107 ms                                                 | 108 ms: 1.01x slower                                                  |
| xml_etree_parse      | 159 ms                                                 | 164 ms: 1.03x slower                                                  |
| pickle_dict          | 35.5 us                                                | 36.9 us: 1.04x slower                                                 |
| tomli_loads          | 2.33 sec                                               | 2.63 sec: 1.13x slower                                                |
| pickle_list          | 5.08 us                                                | 5.95 us: 1.17x slower                                                 |
| unpickle_list        | 5.29 us                                                | 6.28 us: 1.19x slower                                                 |
| pickle_pure_python   | 324 us                                                 | 423 us: 1.31x slower                                                  |
| unpickle_pure_python | 230 us                                                 | 301 us: 1.31x slower                                                  |
| pickle               | 11.6 us                                                | 15.2 us: 1.31x slower                                                 |
| json_loads           | 28.5 us                                                | 37.7 us: 1.32x slower                                                 |
| unpickle             | 15.9 us                                                | 22.0 us: 1.39x slower                                                 |
| xml_etree_generate   | 89.2 ms                                                | 125 ms: 1.40x slower                                                  |
| xml_etree_process    | 61.7 ms                                                | 86.8 ms: 1.41x slower                                                 |
| json_dumps           | 10.4 ms                                                | 14.9 ms: 1.43x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.24x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 9.97 ms: 1.44x slower                                                 |
| python_startup         | 9.55 ms                                                | 17.1 ms: 1.79x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.60x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 53.2 ms: 1.54x slower                                                 |
| mako            | 11.9 ms                                                | 18.6 ms: 1.57x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.55x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 603 ms: 1.96x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 642 ms: 1.80x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 262 ms: 1.71x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 340 ms: 1.69x faster                                                  |
| async_tree_none            | 472 ms                                                 | 301 ms: 1.57x faster                                                  |
| gc_traversal               | 3.79 ms                                                | 2.48 ms: 1.53x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 381 ms: 1.52x faster                                                  |
| mdp                        | 2.63 sec                                               | 1.74 sec: 1.51x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 582 ms: 1.25x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 2.97 ms: 1.21x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 626 ms: 1.16x faster                                                  |
| regex_dna                  | 212 ms                                                 | 192 ms: 1.11x faster                                                  |
| float                      | 84.7 ms                                                | 82.0 ms: 1.03x faster                                                 |
| async_generators           | 463 ms                                                 | 455 ms: 1.02x faster                                                  |
| go                         | 139 ms                                                 | 141 ms: 1.01x slower                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 108 ms: 1.01x slower                                                  |
| deepcopy_memo              | 40.7 us                                                | 41.2 us: 1.01x slower                                                 |
| pathlib                    | 19.3 ms                                                | 19.7 ms: 1.02x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 23.7 ms: 1.02x slower                                                 |
| xml_etree_parse            | 159 ms                                                 | 164 ms: 1.03x slower                                                  |
| deepcopy                   | 371 us                                                 | 383 us: 1.03x slower                                                  |
| pickle_dict                | 35.5 us                                                | 36.9 us: 1.04x slower                                                 |
| comprehensions             | 21.8 us                                                | 22.6 us: 1.04x slower                                                 |
| unpack_sequence            | 54.0 ns                                                | 56.9 ns: 1.05x slower                                                 |
| dulwich_log                | 68.5 ms                                                | 72.4 ms: 1.06x slower                                                 |
| pidigits                   | 187 ms                                                 | 201 ms: 1.07x slower                                                  |
| pycparser                  | 1.18 sec                                               | 1.30 sec: 1.10x slower                                                |
| asyncio_tcp                | 491 ms                                                 | 544 ms: 1.11x slower                                                  |
| generators                 | 31.2 ms                                                | 34.8 ms: 1.11x slower                                                 |
| tomli_loads                | 2.33 sec                                               | 2.63 sec: 1.13x slower                                                |
| docutils                   | 2.77 sec                                               | 3.14 sec: 1.13x slower                                                |
| pyflate                    | 482 ms                                                 | 549 ms: 1.14x slower                                                  |
| sqlite_synth               | 2.83 us                                                | 3.24 us: 1.14x slower                                                 |
| asyncio_tcp_ssl            | 1.79 sec                                               | 2.07 sec: 1.16x slower                                                |
| regex_compile              | 148 ms                                                 | 172 ms: 1.16x slower                                                  |
| pickle_list                | 5.08 us                                                | 5.95 us: 1.17x slower                                                 |
| sympy_sum                  | 169 ms                                                 | 198 ms: 1.17x slower                                                  |
| sympy_integrate            | 21.4 ms                                                | 25.2 ms: 1.18x slower                                                 |
| unpickle_list              | 5.29 us                                                | 6.28 us: 1.19x slower                                                 |
| meteor_contest             | 112 ms                                                 | 135 ms: 1.20x slower                                                  |
| scimark_sor                | 129 ms                                                 | 158 ms: 1.23x slower                                                  |
| hexiom                     | 6.41 ms                                                | 7.87 ms: 1.23x slower                                                 |
| sympy_str                  | 300 ms                                                 | 369 ms: 1.23x slower                                                  |
| chaos                      | 67.0 ms                                                | 82.7 ms: 1.23x slower                                                 |
| deepcopy_reduce            | 3.35 us                                                | 4.13 us: 1.24x slower                                                 |
| 2to3                       | 274 ms                                                 | 339 ms: 1.24x slower                                                  |
| raytrace                   | 312 ms                                                 | 388 ms: 1.24x slower                                                  |
| json                       | 5.26 ms                                                | 6.54 ms: 1.24x slower                                                 |
| deltablue                  | 3.72 ms                                                | 4.63 ms: 1.25x slower                                                 |
| spectral_norm              | 115 ms                                                 | 144 ms: 1.25x slower                                                  |
| coroutines                 | 23.2 ms                                                | 29.1 ms: 1.25x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 1.86 ms: 1.26x slower                                                 |
| scimark_fft                | 382 ms                                                 | 485 ms: 1.27x slower                                                  |
| pickle_pure_python         | 324 us                                                 | 423 us: 1.31x slower                                                  |
| unpickle_pure_python       | 230 us                                                 | 301 us: 1.31x slower                                                  |
| sympy_expand               | 478 ms                                                 | 627 ms: 1.31x slower                                                  |
| pickle                     | 11.6 us                                                | 15.2 us: 1.31x slower                                                 |
| json_loads                 | 28.5 us                                                | 37.7 us: 1.32x slower                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 101 ms: 1.35x slower                                                  |
| crypto_pyaes               | 81.9 ms                                                | 112 ms: 1.37x slower                                                  |
| unpickle                   | 15.9 us                                                | 22.0 us: 1.39x slower                                                 |
| scimark_lu                 | 118 ms                                                 | 165 ms: 1.40x slower                                                  |
| xml_etree_generate         | 89.2 ms                                                | 125 ms: 1.40x slower                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 7.09 ms: 1.40x slower                                                 |
| xml_etree_process          | 61.7 ms                                                | 86.8 ms: 1.41x slower                                                 |
| logging_simple             | 6.46 us                                                | 9.10 us: 1.41x slower                                                 |
| fannkuch                   | 417 ms                                                 | 588 ms: 1.41x slower                                                  |
| nqueens                    | 83.3 ms                                                | 118 ms: 1.42x slower                                                  |
| logging_format             | 7.23 us                                                | 10.2 us: 1.42x slower                                                 |
| json_dumps                 | 10.4 ms                                                | 14.9 ms: 1.43x slower                                                 |
| python_startup_no_site     | 6.94 ms                                                | 9.97 ms: 1.44x slower                                                 |
| richards                   | 45.8 ms                                                | 68.0 ms: 1.48x slower                                                 |
| pprint_safe_repr           | 776 ms                                                 | 1.17 sec: 1.51x slower                                                |
| richards_super             | 51.5 ms                                                | 78.9 ms: 1.53x slower                                                 |
| pprint_pformat             | 1.57 sec                                               | 2.40 sec: 1.53x slower                                                |
| django_template            | 34.6 ms                                                | 53.2 ms: 1.54x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 244 us: 1.55x slower                                                  |
| mako                       | 11.9 ms                                                | 18.6 ms: 1.57x slower                                                 |
| nbody                      | 97.0 ms                                                | 154 ms: 1.59x slower                                                  |
| telco                      | 7.10 ms                                                | 11.9 ms: 1.67x slower                                                 |
| python_startup             | 9.55 ms                                                | 17.1 ms: 1.79x slower                                                 |
| coverage                   | 72.7 ms                                                | 132 ms: 1.81x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 3.51 ms: 4.17x slower                                                 |
| bench_mp_pool              | 24.0 ms                                                | 111 ms: 4.62x slower                                                  |
| logging_silent             | 104 ns                                                 | 705 ns: 6.75x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.21x slower                                                          |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250607-3.15.0a0-8fdbbf8-NOGIL/bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.155x slower

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.13x
- 95% likely to have a slowdown of 1.11x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: 1.38x