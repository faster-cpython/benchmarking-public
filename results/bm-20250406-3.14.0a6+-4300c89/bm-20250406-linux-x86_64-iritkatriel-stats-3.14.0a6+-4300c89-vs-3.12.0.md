# Results vs. 3.12.0

- fork: iritkatriel
- ref: stats
- machine: linux-x86_64
- commit hash: 4300c89
- commit date: 2025-04-06
- overall geometric mean: 1.130x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250406-linux-x86_64-iritkatriel-stats-3.14.0a6+-4300c89 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 251 ms: 1.09x faster                                         |
| docutils       | 2.77 sec                                               | 2.59 sec: 1.07x faster                                       |
| Geometric mean | (ref)                                                  | 1.08x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250406-linux-x86_64-iritkatriel-stats-3.14.0a6+-4300c89 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 615 ms: 1.92x faster                                         |
| async_tree_io              | 1.16 sec                                               | 615 ms: 1.88x faster                                         |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                         |
| async_tree_none            | 472 ms                                                 | 259 ms: 1.82x faster                                         |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.81x faster                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 479 ms: 1.51x faster                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 483 ms: 1.50x faster                                         |
| Geometric mean             | (ref)                                                  | 1.76x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250406-linux-x86_64-iritkatriel-stats-3.14.0a6+-4300c89 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 84.7 ms                                                | 68.2 ms: 1.24x faster                                        |
| nbody          | 97.0 ms                                                | 92.2 ms: 1.05x faster                                        |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                         |
| Geometric mean | (ref)                                                  | 1.10x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250406-linux-x86_64-iritkatriel-stats-3.14.0a6+-4300c89 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 125 ms: 1.19x faster                                         |
| regex_effbot   | 3.61 ms                                                | 3.32 ms: 1.09x faster                                        |
| regex_v8       | 23.1 ms                                                | 23.0 ms: 1.01x faster                                        |
| regex_dna      | 212 ms                                                 | 220 ms: 1.04x slower                                         |
| Geometric mean | (ref)                                                  | 1.06x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250406-linux-x86_64-iritkatriel-stats-3.14.0a6+-4300c89 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.96 sec: 1.19x faster                                       |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                         |
| xml_etree_iterparse  | 107 ms                                                 | 98.3 ms: 1.09x faster                                        |
| unpickle_pure_python | 230 us                                                 | 215 us: 1.07x faster                                         |
| xml_etree_generate   | 89.2 ms                                                | 83.5 ms: 1.07x faster                                        |
| xml_etree_process    | 61.7 ms                                                | 58.3 ms: 1.06x faster                                        |
| pickle_pure_python   | 324 us                                                 | 315 us: 1.03x faster                                         |
| json_loads           | 28.5 us                                                | 29.7 us: 1.04x slower                                        |
| json_dumps           | 10.4 ms                                                | 11.7 ms: 1.12x slower                                        |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250406-linux-x86_64-iritkatriel-stats-3.14.0a6+-4300c89 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.18 ms: 1.18x slower                                        |
| python_startup         | 9.55 ms                                                | 13.2 ms: 1.38x slower                                        |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250406-linux-x86_64-iritkatriel-stats-3.14.0a6+-4300c89 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.5 ms: 1.10x faster                                        |
| mako            | 11.9 ms                                                | 11.3 ms: 1.05x faster                                        |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250406-linux-x86_64-iritkatriel-stats-3.14.0a6+-4300c89 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.23 sec: 2.15x faster                                       |
| async_tree_io_tg           | 1.18 sec                                               | 615 ms: 1.92x faster                                         |
| async_tree_io              | 1.16 sec                                               | 615 ms: 1.88x faster                                         |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                         |
| async_tree_none            | 472 ms                                                 | 259 ms: 1.82x faster                                         |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.81x faster                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 479 ms: 1.51x faster                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 483 ms: 1.50x faster                                         |
| deepcopy                   | 371 us                                                 | 249 us: 1.49x faster                                         |
| deepcopy_memo              | 40.7 us                                                | 28.8 us: 1.42x faster                                        |
| deepcopy_reduce            | 3.35 us                                                | 2.57 us: 1.30x faster                                        |
| comprehensions             | 21.8 us                                                | 17.0 us: 1.28x faster                                        |
| go                         | 139 ms                                                 | 111 ms: 1.25x faster                                         |
| float                      | 84.7 ms                                                | 68.2 ms: 1.24x faster                                        |
| raytrace                   | 312 ms                                                 | 261 ms: 1.20x faster                                         |
| tomli_loads                | 2.33 sec                                               | 1.96 sec: 1.19x faster                                       |
| chaos                      | 67.0 ms                                                | 56.4 ms: 1.19x faster                                        |
| regex_compile              | 148 ms                                                 | 125 ms: 1.19x faster                                         |
| logging_format             | 7.23 us                                                | 6.11 us: 1.18x faster                                        |
| pathlib                    | 19.3 ms                                                | 16.5 ms: 1.18x faster                                        |
| logging_simple             | 6.46 us                                                | 5.51 us: 1.17x faster                                        |
| async_generators           | 463 ms                                                 | 397 ms: 1.17x faster                                         |
| dulwich_log                | 68.5 ms                                                | 59.4 ms: 1.15x faster                                        |
| scimark_monte_carlo        | 75.1 ms                                                | 65.5 ms: 1.15x faster                                        |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.14x faster                                         |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                         |
| sympy_integrate            | 21.4 ms                                                | 19.0 ms: 1.13x faster                                        |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.12x faster                                         |
| scimark_fft                | 382 ms                                                 | 342 ms: 1.12x faster                                         |
| sqlalchemy_declarative     | 147 ms                                                 | 131 ms: 1.12x faster                                         |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.7 ms: 1.12x faster                                        |
| crypto_pyaes               | 81.9 ms                                                | 73.3 ms: 1.12x faster                                        |
| sympy_str                  | 300 ms                                                 | 269 ms: 1.12x faster                                         |
| pprint_safe_repr           | 776 ms                                                 | 701 ms: 1.11x faster                                         |
| deltablue                  | 3.72 ms                                                | 3.37 ms: 1.10x faster                                        |
| django_template            | 34.6 ms                                                | 31.5 ms: 1.10x faster                                        |
| 2to3                       | 274 ms                                                 | 251 ms: 1.09x faster                                         |
| pprint_pformat             | 1.57 sec                                               | 1.44 sec: 1.09x faster                                       |
| logging_silent             | 104 ns                                                 | 96.1 ns: 1.09x faster                                        |
| xml_etree_iterparse        | 107 ms                                                 | 98.3 ms: 1.09x faster                                        |
| regex_effbot               | 3.61 ms                                                | 3.32 ms: 1.09x faster                                        |
| richards                   | 45.8 ms                                                | 42.2 ms: 1.09x faster                                        |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.08x faster                                         |
| unpickle_pure_python       | 230 us                                                 | 215 us: 1.07x faster                                         |
| docutils                   | 2.77 sec                                               | 2.59 sec: 1.07x faster                                       |
| xml_etree_generate         | 89.2 ms                                                | 83.5 ms: 1.07x faster                                        |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.75 ms: 1.07x faster                                        |
| richards_super             | 51.5 ms                                                | 48.4 ms: 1.06x faster                                        |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                         |
| xml_etree_process          | 61.7 ms                                                | 58.3 ms: 1.06x faster                                        |
| generators                 | 31.2 ms                                                | 29.6 ms: 1.06x faster                                        |
| mako                       | 11.9 ms                                                | 11.3 ms: 1.05x faster                                        |
| nbody                      | 97.0 ms                                                | 92.2 ms: 1.05x faster                                        |
| sympy_expand               | 478 ms                                                 | 456 ms: 1.05x faster                                         |
| pyflate                    | 482 ms                                                 | 462 ms: 1.04x faster                                         |
| hexiom                     | 6.41 ms                                                | 6.14 ms: 1.04x faster                                        |
| nqueens                    | 83.3 ms                                                | 80.6 ms: 1.03x faster                                        |
| pickle_pure_python         | 324 us                                                 | 315 us: 1.03x faster                                         |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                       |
| sqlite_synth               | 2.83 us                                                | 2.78 us: 1.02x faster                                        |
| fannkuch                   | 417 ms                                                 | 413 ms: 1.01x faster                                         |
| regex_v8                   | 23.1 ms                                                | 23.0 ms: 1.01x faster                                        |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                         |
| coroutines                 | 23.2 ms                                                | 23.3 ms: 1.01x slower                                        |
| json                       | 5.26 ms                                                | 5.32 ms: 1.01x slower                                        |
| regex_dna                  | 212 ms                                                 | 220 ms: 1.04x slower                                         |
| json_loads                 | 28.5 us                                                | 29.7 us: 1.04x slower                                        |
| bench_thread_pool          | 842 us                                                 | 883 us: 1.05x slower                                         |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                         |
| telco                      | 7.10 ms                                                | 7.70 ms: 1.08x slower                                        |
| json_dumps                 | 10.4 ms                                                | 11.7 ms: 1.12x slower                                        |
| coverage                   | 72.7 ms                                                | 84.8 ms: 1.17x slower                                        |
| python_startup_no_site     | 6.94 ms                                                | 8.18 ms: 1.18x slower                                        |
| gc_traversal               | 3.79 ms                                                | 4.77 ms: 1.26x slower                                        |
| python_startup             | 9.55 ms                                                | 13.2 ms: 1.38x slower                                        |
| create_gc_cycles           | 1.48 ms                                                | 2.47 ms: 1.68x slower                                        |
| bench_mp_pool              | 24.0 ms                                                | 81.9 ms: 3.41x slower                                        |
| Geometric mean             | (ref)                                                  | 1.11x faster                                                 |

Benchmark hidden because not significant (2): scimark_lu, asyncio_websockets
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250406-3.14.0a6+-4300c89/bm-20250406-linux-x86_64-iritkatriel-stats-3.14.0a6+-4300c89.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.130x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.10x