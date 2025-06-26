# Results vs. 3.12.0

- fork: faster-cpython
- ref: explicit_check_perio
- machine: linux-x86_64
- commit hash: 892a89d
- commit date: 2025-06-26
- overall geometric mean: 1.114x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 256 ms: 1.07x faster                                                            |
| docutils       | 2.77 sec                                               | 2.58 sec: 1.07x faster                                                          |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 599 ms: 1.93x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 311 ms: 1.85x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 641 ms: 1.84x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 315 ms: 1.83x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 248 ms: 1.81x faster                                                            |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 480 ms: 1.51x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 489 ms: 1.49x faster                                                            |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 72.9 ms: 1.16x faster                                                           |
| pidigits       | 187 ms                                                 | 196 ms: 1.05x slower                                                            |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                    |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                                            |
| regex_effbot   | 3.61 ms                                                | 3.31 ms: 1.09x faster                                                           |
| regex_dna      | 212 ms                                                 | 212 ms: 1.00x faster                                                            |
| regex_v8       | 23.1 ms                                                | 23.2 ms: 1.00x slower                                                           |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.98 sec: 1.18x faster                                                          |
| xml_etree_parse      | 159 ms                                                 | 145 ms: 1.10x faster                                                            |
| xml_etree_iterparse  | 107 ms                                                 | 99.5 ms: 1.07x faster                                                           |
| unpickle_pure_python | 230 us                                                 | 219 us: 1.05x faster                                                            |
| xml_etree_generate   | 89.2 ms                                                | 85.4 ms: 1.04x faster                                                           |
| xml_etree_process    | 61.7 ms                                                | 60.1 ms: 1.03x faster                                                           |
| json_loads           | 28.5 us                                                | 28.2 us: 1.01x faster                                                           |
| pickle_pure_python   | 324 us                                                 | 321 us: 1.01x faster                                                            |
| json_dumps           | 10.4 ms                                                | 11.0 ms: 1.06x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.93 ms: 1.00x faster                                                           |
| python_startup         | 9.55 ms                                                | 12.2 ms: 1.28x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.3 ms: 1.06x faster                                                           |
| django_template | 34.6 ms                                                | 33.1 ms: 1.04x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.22 sec: 2.15x faster                                                          |
| async_tree_io              | 1.16 sec                                               | 599 ms: 1.93x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 311 ms: 1.85x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 641 ms: 1.84x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 315 ms: 1.83x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 248 ms: 1.81x faster                                                            |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 480 ms: 1.51x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 489 ms: 1.49x faster                                                            |
| deepcopy                   | 371 us                                                 | 258 us: 1.44x faster                                                            |
| deepcopy_memo              | 40.7 us                                                | 29.8 us: 1.37x faster                                                           |
| comprehensions             | 21.8 us                                                | 16.1 us: 1.35x faster                                                           |
| go                         | 139 ms                                                 | 110 ms: 1.27x faster                                                            |
| deepcopy_reduce            | 3.35 us                                                | 2.72 us: 1.23x faster                                                           |
| tomli_loads                | 2.33 sec                                               | 1.98 sec: 1.18x faster                                                          |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                                            |
| raytrace                   | 312 ms                                                 | 268 ms: 1.17x faster                                                            |
| dulwich_log                | 68.5 ms                                                | 58.9 ms: 1.16x faster                                                           |
| float                      | 84.7 ms                                                | 72.9 ms: 1.16x faster                                                           |
| spectral_norm              | 115 ms                                                 | 100 ms: 1.14x faster                                                            |
| sympy_sum                  | 169 ms                                                 | 148 ms: 1.14x faster                                                            |
| pathlib                    | 19.3 ms                                                | 17.0 ms: 1.14x faster                                                           |
| async_generators           | 463 ms                                                 | 408 ms: 1.13x faster                                                            |
| pyflate                    | 482 ms                                                 | 428 ms: 1.13x faster                                                            |
| sympy_integrate            | 21.4 ms                                                | 19.0 ms: 1.13x faster                                                           |
| sympy_str                  | 300 ms                                                 | 267 ms: 1.12x faster                                                            |
| scimark_monte_carlo        | 75.1 ms                                                | 67.2 ms: 1.12x faster                                                           |
| chaos                      | 67.0 ms                                                | 60.0 ms: 1.12x faster                                                           |
| scimark_sor                | 129 ms                                                 | 117 ms: 1.10x faster                                                            |
| xml_etree_parse            | 159 ms                                                 | 145 ms: 1.10x faster                                                            |
| regex_effbot               | 3.61 ms                                                | 3.31 ms: 1.09x faster                                                           |
| crypto_pyaes               | 81.9 ms                                                | 75.4 ms: 1.09x faster                                                           |
| xml_etree_iterparse        | 107 ms                                                 | 99.5 ms: 1.07x faster                                                           |
| docutils                   | 2.77 sec                                               | 2.58 sec: 1.07x faster                                                          |
| 2to3                       | 274 ms                                                 | 256 ms: 1.07x faster                                                            |
| deltablue                  | 3.72 ms                                                | 3.47 ms: 1.07x faster                                                           |
| scimark_fft                | 382 ms                                                 | 359 ms: 1.06x faster                                                            |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                            |
| mako                       | 11.9 ms                                                | 11.3 ms: 1.06x faster                                                           |
| sympy_expand               | 478 ms                                                 | 453 ms: 1.05x faster                                                            |
| unpickle_pure_python       | 230 us                                                 | 219 us: 1.05x faster                                                            |
| richards                   | 45.8 ms                                                | 43.6 ms: 1.05x faster                                                           |
| hexiom                     | 6.41 ms                                                | 6.11 ms: 1.05x faster                                                           |
| django_template            | 34.6 ms                                                | 33.1 ms: 1.04x faster                                                           |
| xml_etree_generate         | 89.2 ms                                                | 85.4 ms: 1.04x faster                                                           |
| richards_super             | 51.5 ms                                                | 49.5 ms: 1.04x faster                                                           |
| scimark_lu                 | 118 ms                                                 | 114 ms: 1.03x faster                                                            |
| fannkuch                   | 417 ms                                                 | 404 ms: 1.03x faster                                                            |
| logging_simple             | 6.46 us                                                | 6.27 us: 1.03x faster                                                           |
| generators                 | 31.2 ms                                                | 30.4 ms: 1.03x faster                                                           |
| xml_etree_process          | 61.7 ms                                                | 60.1 ms: 1.03x faster                                                           |
| logging_format             | 7.23 us                                                | 7.06 us: 1.02x faster                                                           |
| nqueens                    | 83.3 ms                                                | 81.8 ms: 1.02x faster                                                           |
| json_loads                 | 28.5 us                                                | 28.2 us: 1.01x faster                                                           |
| pickle_pure_python         | 324 us                                                 | 321 us: 1.01x faster                                                            |
| regex_dna                  | 212 ms                                                 | 212 ms: 1.00x faster                                                            |
| python_startup_no_site     | 6.94 ms                                                | 6.93 ms: 1.00x faster                                                           |
| regex_v8                   | 23.1 ms                                                | 23.2 ms: 1.00x slower                                                           |
| sqlite_synth               | 2.83 us                                                | 2.85 us: 1.01x slower                                                           |
| pprint_safe_repr           | 776 ms                                                 | 798 ms: 1.03x slower                                                            |
| pprint_pformat             | 1.57 sec                                               | 1.64 sec: 1.05x slower                                                          |
| pidigits                   | 187 ms                                                 | 196 ms: 1.05x slower                                                            |
| json_dumps                 | 10.4 ms                                                | 11.0 ms: 1.06x slower                                                           |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                                            |
| coroutines                 | 23.2 ms                                                | 24.5 ms: 1.06x slower                                                           |
| telco                      | 7.10 ms                                                | 8.04 ms: 1.13x slower                                                           |
| coverage                   | 72.7 ms                                                | 87.6 ms: 1.20x slower                                                           |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.28x slower                                                           |
| gc_traversal               | 3.79 ms                                                | 5.13 ms: 1.35x slower                                                           |
| create_gc_cycles           | 1.48 ms                                                | 2.59 ms: 1.75x slower                                                           |
| logging_silent             | 104 ns                                                 | 481 ns: 4.61x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                                    |

Benchmark hidden because not significant (5): pycparser, nbody, asyncio_websockets, json, scimark_sparse_mat_mult
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250626-3.15.0a0-892a89d/bm-20250626-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.114x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.13x