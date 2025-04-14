# Results vs. 3.12.0

- fork: kumaraditya303
- ref: per_thread_cur_task
- machine: linux-x86_64
- commit hash: ba92dfb
- commit date: 2025-02-10
- overall geometric mean: 1.016x slower
- HPT reliability: 99.79%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 304 ms: 1.11x slower                                                          |
| docutils       | 2.77 sec                                               | 2.82 sec: 1.02x slower                                                        |
| Geometric mean | (ref)                                                  | 1.06x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 546 ms: 2.17x faster                                                          |
| async_tree_io              | 1.16 sec                                               | 590 ms: 1.96x faster                                                          |
| async_tree_none_tg         | 450 ms                                                 | 241 ms: 1.86x faster                                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 320 ms: 1.79x faster                                                          |
| async_tree_none            | 472 ms                                                 | 281 ms: 1.68x faster                                                          |
| async_tree_memoization     | 578 ms                                                 | 360 ms: 1.61x faster                                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 473 ms: 1.53x faster                                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 516 ms: 1.41x faster                                                          |
| Geometric mean             | (ref)                                                  | 1.74x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 76.9 ms: 1.10x faster                                                         |
| pidigits       | 187 ms                                                 | 192 ms: 1.02x slower                                                          |
| nbody          | 97.0 ms                                                | 136 ms: 1.40x slower                                                          |
| Geometric mean | (ref)                                                  | 1.09x slower                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.46 ms: 1.04x faster                                                         |
| regex_compile  | 148 ms                                                 | 146 ms: 1.02x faster                                                          |
| regex_dna      | 212 ms                                                 | 227 ms: 1.07x slower                                                          |
| regex_v8       | 23.1 ms                                                | 25.7 ms: 1.11x slower                                                         |
| Geometric mean | (ref)                                                  | 1.03x slower                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 107 ms                                                 | 95.2 ms: 1.12x faster                                                         |
| xml_etree_parse      | 159 ms                                                 | 149 ms: 1.07x faster                                                          |
| tomli_loads          | 2.33 sec                                               | 2.31 sec: 1.01x faster                                                        |
| xml_etree_generate   | 89.2 ms                                                | 94.9 ms: 1.06x slower                                                         |
| xml_etree_process    | 61.7 ms                                                | 67.3 ms: 1.09x slower                                                         |
| unpickle_pure_python | 230 us                                                 | 257 us: 1.12x slower                                                          |
| pickle_pure_python   | 324 us                                                 | 370 us: 1.14x slower                                                          |
| json_loads           | 28.5 us                                                | 33.0 us: 1.16x slower                                                         |
| json_dumps           | 10.4 ms                                                | 12.8 ms: 1.23x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.06x slower                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 9.31 ms: 1.34x slower                                                         |
| python_startup         | 9.55 ms                                                | 15.0 ms: 1.57x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.45x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 40.4 ms: 1.17x slower                                                         |
| mako            | 11.9 ms                                                | 16.3 ms: 1.37x slower                                                         |
| Geometric mean  | (ref)                                                  | 1.27x slower                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 546 ms: 2.17x faster                                                          |
| async_tree_io              | 1.16 sec                                               | 590 ms: 1.96x faster                                                          |
| gc_traversal               | 3.79 ms                                                | 1.98 ms: 1.91x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 241 ms: 1.86x faster                                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 320 ms: 1.79x faster                                                          |
| async_tree_none            | 472 ms                                                 | 281 ms: 1.68x faster                                                          |
| async_tree_memoization     | 578 ms                                                 | 360 ms: 1.61x faster                                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 473 ms: 1.53x faster                                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 516 ms: 1.41x faster                                                          |
| deepcopy                   | 371 us                                                 | 305 us: 1.22x faster                                                          |
| pathlib                    | 19.3 ms                                                | 16.7 ms: 1.16x faster                                                         |
| xml_etree_iterparse        | 107 ms                                                 | 95.2 ms: 1.12x faster                                                         |
| comprehensions             | 21.8 us                                                | 19.6 us: 1.11x faster                                                         |
| float                      | 84.7 ms                                                | 76.9 ms: 1.10x faster                                                         |
| xml_etree_parse            | 159 ms                                                 | 149 ms: 1.07x faster                                                          |
| deepcopy_memo              | 40.7 us                                                | 38.2 us: 1.07x faster                                                         |
| async_generators           | 463 ms                                                 | 438 ms: 1.06x faster                                                          |
| regex_effbot               | 3.61 ms                                                | 3.46 ms: 1.04x faster                                                         |
| sqlite_synth               | 2.83 us                                                | 2.72 us: 1.04x faster                                                         |
| deepcopy_reduce            | 3.35 us                                                | 3.23 us: 1.04x faster                                                         |
| regex_compile              | 148 ms                                                 | 146 ms: 1.02x faster                                                          |
| tomli_loads                | 2.33 sec                                               | 2.31 sec: 1.01x faster                                                        |
| spectral_norm              | 115 ms                                                 | 114 ms: 1.01x faster                                                          |
| go                         | 139 ms                                                 | 141 ms: 1.01x slower                                                          |
| generators                 | 31.2 ms                                                | 31.6 ms: 1.01x slower                                                         |
| pycparser                  | 1.18 sec                                               | 1.20 sec: 1.02x slower                                                        |
| docutils                   | 2.77 sec                                               | 2.82 sec: 1.02x slower                                                        |
| pidigits                   | 187 ms                                                 | 192 ms: 1.02x slower                                                          |
| coroutines                 | 23.2 ms                                                | 23.8 ms: 1.03x slower                                                         |
| logging_format             | 7.23 us                                                | 7.46 us: 1.03x slower                                                         |
| logging_simple             | 6.46 us                                                | 6.67 us: 1.03x slower                                                         |
| sympy_sum                  | 169 ms                                                 | 176 ms: 1.04x slower                                                          |
| pyflate                    | 482 ms                                                 | 506 ms: 1.05x slower                                                          |
| sympy_str                  | 300 ms                                                 | 315 ms: 1.05x slower                                                          |
| sqlglot_normalize          | 110 ms                                                 | 117 ms: 1.06x slower                                                          |
| xml_etree_generate         | 89.2 ms                                                | 94.9 ms: 1.06x slower                                                         |
| regex_dna                  | 212 ms                                                 | 227 ms: 1.07x slower                                                          |
| logging_silent             | 104 ns                                                 | 112 ns: 1.07x slower                                                          |
| scimark_sor                | 129 ms                                                 | 138 ms: 1.07x slower                                                          |
| json                       | 5.26 ms                                                | 5.65 ms: 1.07x slower                                                         |
| scimark_fft                | 382 ms                                                 | 413 ms: 1.08x slower                                                          |
| crypto_pyaes               | 81.9 ms                                                | 88.6 ms: 1.08x slower                                                         |
| mdp                        | 2.63 sec                                               | 2.85 sec: 1.08x slower                                                        |
| sqlalchemy_declarative     | 147 ms                                                 | 159 ms: 1.09x slower                                                          |
| xml_etree_process          | 61.7 ms                                                | 67.3 ms: 1.09x slower                                                         |
| sqlglot_optimize           | 54.8 ms                                                | 59.8 ms: 1.09x slower                                                         |
| chaos                      | 67.0 ms                                                | 73.1 ms: 1.09x slower                                                         |
| sympy_integrate            | 21.4 ms                                                | 23.5 ms: 1.10x slower                                                         |
| sympy_expand               | 478 ms                                                 | 529 ms: 1.11x slower                                                          |
| pprint_safe_repr           | 776 ms                                                 | 859 ms: 1.11x slower                                                          |
| regex_v8                   | 23.1 ms                                                | 25.7 ms: 1.11x slower                                                         |
| 2to3                       | 274 ms                                                 | 304 ms: 1.11x slower                                                          |
| sqlglot_transpile          | 1.68 ms                                                | 1.88 ms: 1.11x slower                                                         |
| unpickle_pure_python       | 230 us                                                 | 257 us: 1.12x slower                                                          |
| sqlalchemy_imperative      | 18.7 ms                                                | 20.9 ms: 1.12x slower                                                         |
| pprint_pformat             | 1.57 sec                                               | 1.76 sec: 1.12x slower                                                        |
| raytrace                   | 312 ms                                                 | 351 ms: 1.13x slower                                                          |
| sqlglot_parse              | 1.36 ms                                                | 1.54 ms: 1.13x slower                                                         |
| scimark_monte_carlo        | 75.1 ms                                                | 85.7 ms: 1.14x slower                                                         |
| pickle_pure_python         | 324 us                                                 | 370 us: 1.14x slower                                                          |
| json_loads                 | 28.5 us                                                | 33.0 us: 1.16x slower                                                         |
| django_template            | 34.6 ms                                                | 40.4 ms: 1.17x slower                                                         |
| meteor_contest             | 112 ms                                                 | 132 ms: 1.17x slower                                                          |
| richards                   | 45.8 ms                                                | 54.0 ms: 1.18x slower                                                         |
| create_gc_cycles           | 1.48 ms                                                | 1.74 ms: 1.18x slower                                                         |
| nqueens                    | 83.3 ms                                                | 98.8 ms: 1.19x slower                                                         |
| scimark_lu                 | 118 ms                                                 | 141 ms: 1.20x slower                                                          |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 6.06 ms: 1.20x slower                                                         |
| hexiom                     | 6.41 ms                                                | 7.69 ms: 1.20x slower                                                         |
| richards_super             | 51.5 ms                                                | 63.1 ms: 1.22x slower                                                         |
| fannkuch                   | 417 ms                                                 | 512 ms: 1.23x slower                                                          |
| json_dumps                 | 10.4 ms                                                | 12.8 ms: 1.23x slower                                                         |
| deltablue                  | 3.72 ms                                                | 4.72 ms: 1.27x slower                                                         |
| typing_runtime_protocols   | 158 us                                                 | 203 us: 1.28x slower                                                          |
| telco                      | 7.10 ms                                                | 9.38 ms: 1.32x slower                                                         |
| python_startup_no_site     | 6.94 ms                                                | 9.31 ms: 1.34x slower                                                         |
| mako                       | 11.9 ms                                                | 16.3 ms: 1.37x slower                                                         |
| nbody                      | 97.0 ms                                                | 136 ms: 1.40x slower                                                          |
| coverage                   | 72.7 ms                                                | 106 ms: 1.46x slower                                                          |
| python_startup             | 9.55 ms                                                | 15.0 ms: 1.57x slower                                                         |
| bench_mp_pool              | 24.0 ms                                                | 88.6 ms: 3.69x slower                                                         |
| bench_thread_pool          | 842 us                                                 | 3.46 ms: 4.11x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.05x slower                                                                  |

Benchmark hidden because not significant (2): dulwich_log, asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250210-3.14.0a4+-ba92dfb-NOGIL/bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.016x slower

# HPT report

- Reliability score: 99.79% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.31x