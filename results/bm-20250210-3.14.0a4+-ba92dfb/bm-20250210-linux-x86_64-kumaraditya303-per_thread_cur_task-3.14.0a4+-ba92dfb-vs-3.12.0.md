# Results vs. 3.12.0

- fork: kumaraditya303
- ref: per_thread_cur_task
- machine: linux-x86_64
- commit hash: ba92dfb
- commit date: 2025-02-10
- overall geometric mean: 1.121x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 252 ms: 1.09x faster                                                          |
| docutils       | 2.77 sec                                               | 2.58 sec: 1.07x faster                                                        |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 612 ms: 1.93x faster                                                          |
| async_tree_io              | 1.16 sec                                               | 605 ms: 1.91x faster                                                          |
| async_tree_none            | 472 ms                                                 | 259 ms: 1.82x faster                                                          |
| async_tree_memoization     | 578 ms                                                 | 318 ms: 1.81x faster                                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                                          |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.80x faster                                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 481 ms: 1.51x faster                                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 490 ms: 1.48x faster                                                          |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.0 ms: 1.23x faster                                                         |
| nbody          | 97.0 ms                                                | 94.3 ms: 1.03x faster                                                         |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                          |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 126 ms: 1.18x faster                                                          |
| regex_effbot   | 3.61 ms                                                | 3.24 ms: 1.11x faster                                                         |
| regex_dna      | 212 ms                                                 | 216 ms: 1.02x slower                                                          |
| regex_v8       | 23.1 ms                                                | 24.3 ms: 1.05x slower                                                         |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.98 sec: 1.18x faster                                                        |
| xml_etree_parse      | 159 ms                                                 | 139 ms: 1.15x faster                                                          |
| xml_etree_iterparse  | 107 ms                                                 | 96.5 ms: 1.11x faster                                                         |
| xml_etree_generate   | 89.2 ms                                                | 83.6 ms: 1.07x faster                                                         |
| xml_etree_process    | 61.7 ms                                                | 58.6 ms: 1.05x faster                                                         |
| unpickle_pure_python | 230 us                                                 | 218 us: 1.05x faster                                                          |
| pickle_pure_python   | 324 us                                                 | 320 us: 1.01x faster                                                          |
| json_loads           | 28.5 us                                                | 28.7 us: 1.01x slower                                                         |
| json_dumps           | 10.4 ms                                                | 11.5 ms: 1.11x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.02 ms: 1.01x slower                                                         |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.16x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.6 ms: 1.12x faster                                                         |
| django_template | 34.6 ms                                                | 32.1 ms: 1.08x faster                                                         |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 612 ms: 1.93x faster                                                          |
| async_tree_io              | 1.16 sec                                               | 605 ms: 1.91x faster                                                          |
| async_tree_none            | 472 ms                                                 | 259 ms: 1.82x faster                                                          |
| async_tree_memoization     | 578 ms                                                 | 318 ms: 1.81x faster                                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                                          |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.80x faster                                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 481 ms: 1.51x faster                                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 490 ms: 1.48x faster                                                          |
| deepcopy                   | 371 us                                                 | 262 us: 1.42x faster                                                          |
| comprehensions             | 21.8 us                                                | 16.2 us: 1.34x faster                                                         |
| deepcopy_memo              | 40.7 us                                                | 30.9 us: 1.32x faster                                                         |
| deepcopy_reduce            | 3.35 us                                                | 2.71 us: 1.23x faster                                                         |
| async_generators           | 463 ms                                                 | 377 ms: 1.23x faster                                                          |
| float                      | 84.7 ms                                                | 69.0 ms: 1.23x faster                                                         |
| logging_format             | 7.23 us                                                | 5.99 us: 1.21x faster                                                         |
| go                         | 139 ms                                                 | 116 ms: 1.20x faster                                                          |
| logging_simple             | 6.46 us                                                | 5.42 us: 1.19x faster                                                         |
| pathlib                    | 19.3 ms                                                | 16.3 ms: 1.19x faster                                                         |
| spectral_norm              | 115 ms                                                 | 97.1 ms: 1.18x faster                                                         |
| regex_compile              | 148 ms                                                 | 126 ms: 1.18x faster                                                          |
| tomli_loads                | 2.33 sec                                               | 1.98 sec: 1.18x faster                                                        |
| deltablue                  | 3.72 ms                                                | 3.15 ms: 1.18x faster                                                         |
| crypto_pyaes               | 81.9 ms                                                | 70.1 ms: 1.17x faster                                                         |
| sympy_sum                  | 169 ms                                                 | 146 ms: 1.16x faster                                                          |
| sqlalchemy_declarative     | 147 ms                                                 | 127 ms: 1.16x faster                                                          |
| xml_etree_parse            | 159 ms                                                 | 139 ms: 1.15x faster                                                          |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.3 ms: 1.15x faster                                                         |
| chaos                      | 67.0 ms                                                | 58.6 ms: 1.14x faster                                                         |
| raytrace                   | 312 ms                                                 | 274 ms: 1.14x faster                                                          |
| sympy_str                  | 300 ms                                                 | 264 ms: 1.14x faster                                                          |
| generators                 | 31.2 ms                                                | 27.5 ms: 1.13x faster                                                         |
| mako                       | 11.9 ms                                                | 10.6 ms: 1.12x faster                                                         |
| scimark_fft                | 382 ms                                                 | 341 ms: 1.12x faster                                                          |
| regex_effbot               | 3.61 ms                                                | 3.24 ms: 1.11x faster                                                         |
| scimark_monte_carlo        | 75.1 ms                                                | 67.7 ms: 1.11x faster                                                         |
| xml_etree_iterparse        | 107 ms                                                 | 96.5 ms: 1.11x faster                                                         |
| sqlglot_parse              | 1.36 ms                                                | 1.24 ms: 1.10x faster                                                         |
| sympy_integrate            | 21.4 ms                                                | 19.6 ms: 1.09x faster                                                         |
| pyflate                    | 482 ms                                                 | 443 ms: 1.09x faster                                                          |
| 2to3                       | 274 ms                                                 | 252 ms: 1.09x faster                                                          |
| sqlglot_transpile          | 1.68 ms                                                | 1.55 ms: 1.09x faster                                                         |
| meteor_contest             | 112 ms                                                 | 104 ms: 1.08x faster                                                          |
| django_template            | 34.6 ms                                                | 32.1 ms: 1.08x faster                                                         |
| docutils                   | 2.77 sec                                               | 2.58 sec: 1.07x faster                                                        |
| pprint_safe_repr           | 776 ms                                                 | 724 ms: 1.07x faster                                                          |
| dulwich_log                | 68.5 ms                                                | 64.2 ms: 1.07x faster                                                         |
| sqlglot_normalize          | 110 ms                                                 | 103 ms: 1.07x faster                                                          |
| xml_etree_generate         | 89.2 ms                                                | 83.6 ms: 1.07x faster                                                         |
| sympy_expand               | 478 ms                                                 | 449 ms: 1.07x faster                                                          |
| pprint_pformat             | 1.57 sec                                               | 1.48 sec: 1.06x faster                                                        |
| mdp                        | 2.63 sec                                               | 2.48 sec: 1.06x faster                                                        |
| sqlglot_optimize           | 54.8 ms                                                | 51.7 ms: 1.06x faster                                                         |
| scimark_sor                | 129 ms                                                 | 122 ms: 1.06x faster                                                          |
| xml_etree_process          | 61.7 ms                                                | 58.6 ms: 1.05x faster                                                         |
| unpickle_pure_python       | 230 us                                                 | 218 us: 1.05x faster                                                          |
| nqueens                    | 83.3 ms                                                | 79.4 ms: 1.05x faster                                                         |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.05x faster                                                        |
| richards                   | 45.8 ms                                                | 44.0 ms: 1.04x faster                                                         |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.87 ms: 1.04x faster                                                         |
| nbody                      | 97.0 ms                                                | 94.3 ms: 1.03x faster                                                         |
| hexiom                     | 6.41 ms                                                | 6.24 ms: 1.03x faster                                                         |
| richards_super             | 51.5 ms                                                | 50.2 ms: 1.03x faster                                                         |
| fannkuch                   | 417 ms                                                 | 407 ms: 1.03x faster                                                          |
| json                       | 5.26 ms                                                | 5.14 ms: 1.02x faster                                                         |
| sqlite_synth               | 2.83 us                                                | 2.78 us: 1.02x faster                                                         |
| pickle_pure_python         | 324 us                                                 | 320 us: 1.01x faster                                                          |
| coroutines                 | 23.2 ms                                                | 23.0 ms: 1.01x faster                                                         |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                          |
| typing_runtime_protocols   | 158 us                                                 | 159 us: 1.01x slower                                                          |
| json_loads                 | 28.5 us                                                | 28.7 us: 1.01x slower                                                         |
| logging_silent             | 104 ns                                                 | 105 ns: 1.01x slower                                                          |
| python_startup_no_site     | 6.94 ms                                                | 7.02 ms: 1.01x slower                                                         |
| regex_dna                  | 212 ms                                                 | 216 ms: 1.02x slower                                                          |
| bench_thread_pool          | 842 us                                                 | 860 us: 1.02x slower                                                          |
| regex_v8                   | 23.1 ms                                                | 24.3 ms: 1.05x slower                                                         |
| telco                      | 7.10 ms                                                | 7.76 ms: 1.09x slower                                                         |
| json_dumps                 | 10.4 ms                                                | 11.5 ms: 1.11x slower                                                         |
| gc_traversal               | 3.79 ms                                                | 4.78 ms: 1.26x slower                                                         |
| coverage                   | 72.7 ms                                                | 91.6 ms: 1.26x slower                                                         |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                         |
| create_gc_cycles           | 1.48 ms                                                | 2.46 ms: 1.67x slower                                                         |
| bench_mp_pool              | 24.0 ms                                                | 80.9 ms: 3.37x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                                  |

Benchmark hidden because not significant (2): scimark_lu, asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250210-3.14.0a4+-ba92dfb/bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.121x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.09x