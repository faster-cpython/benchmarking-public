# Results vs. 3.12.0

- fork: kumaraditya303
- ref: per_thread_tasks
- machine: linux-x86_64
- commit hash: 4014e70
- commit date: 2025-01-29
- overall geometric mean: 1.039x faster
- HPT reliability: 99.79%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-pythonperf2-x86_64-kumaraditya303-per_thread_tasks-3.14.0a4+-4014e70 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 282 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                     |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-pythonperf2-x86_64-kumaraditya303-per_thread_tasks-3.14.0a4+-4014e70 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 648 ms: 1.63x faster                                                             |
| async_tree_io              | 1.04 sec                                                     | 644 ms: 1.62x faster                                                             |
| async_tree_memoization_tg  | 540 ms                                                       | 335 ms: 1.61x faster                                                             |
| async_tree_none            | 452 ms                                                       | 289 ms: 1.56x faster                                                             |
| async_tree_none_tg         | 431 ms                                                       | 277 ms: 1.56x faster                                                             |
| async_tree_memoization     | 544 ms                                                       | 350 ms: 1.55x faster                                                             |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 504 ms: 1.38x faster                                                             |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 516 ms: 1.35x faster                                                             |
| Geometric mean             | (ref)                                                        | 1.53x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-pythonperf2-x86_64-kumaraditya303-per_thread_tasks-3.14.0a4+-4014e70 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 69.6 ms: 1.10x faster                                                            |
| pidigits       | 265 ms                                                       | 254 ms: 1.04x faster                                                             |
| nbody          | 88.0 ms                                                      | 89.4 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-pythonperf2-x86_64-kumaraditya303-per_thread_tasks-3.14.0a4+-4014e70 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.17 ms: 1.13x faster                                                            |
| regex_compile  | 144 ms                                                       | 134 ms: 1.07x faster                                                             |
| regex_dna      | 239 ms                                                       | 249 ms: 1.05x slower                                                             |
| regex_v8       | 23.6 ms                                                      | 25.5 ms: 1.08x slower                                                            |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-pythonperf2-x86_64-kumaraditya303-per_thread_tasks-3.14.0a4+-4014e70 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| xml_etree_parse      | 144 ms                                                       | 136 ms: 1.06x faster                                                             |
| tomli_loads          | 2.16 sec                                                     | 2.05 sec: 1.05x faster                                                           |
| xml_etree_generate   | 86.1 ms                                                      | 82.9 ms: 1.04x faster                                                            |
| unpickle_pure_python | 210 us                                                       | 207 us: 1.01x faster                                                             |
| pickle_pure_python   | 318 us                                                       | 322 us: 1.01x slower                                                             |
| xml_etree_iterparse  | 103 ms                                                       | 106 ms: 1.03x slower                                                             |
| json_dumps           | 10.2 ms                                                      | 11.6 ms: 1.14x slower                                                            |
| json_loads           | 24.4 us                                                      | 37.8 us: 1.55x slower                                                            |
| Geometric mean       | (ref)                                                        | 1.05x slower                                                                     |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-pythonperf2-x86_64-kumaraditya303-per_thread_tasks-3.14.0a4+-4014e70 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.96 ms: 1.04x slower                                                            |
| python_startup         | 11.6 ms                                                      | 16.0 ms: 1.37x slower                                                            |
| Geometric mean         | (ref)                                                        | 1.19x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-pythonperf2-x86_64-kumaraditya303-per_thread_tasks-3.14.0a4+-4014e70 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 36.8 ms: 1.04x faster                                                            |
| mako            | 10.0 ms                                                      | 10.9 ms: 1.09x slower                                                            |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-pythonperf2-x86_64-kumaraditya303-per_thread_tasks-3.14.0a4+-4014e70 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 648 ms: 1.63x faster                                                             |
| async_tree_io              | 1.04 sec                                                     | 644 ms: 1.62x faster                                                             |
| async_tree_memoization_tg  | 540 ms                                                       | 335 ms: 1.61x faster                                                             |
| async_tree_none            | 452 ms                                                       | 289 ms: 1.56x faster                                                             |
| async_tree_none_tg         | 431 ms                                                       | 277 ms: 1.56x faster                                                             |
| async_tree_memoization     | 544 ms                                                       | 350 ms: 1.55x faster                                                             |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 504 ms: 1.38x faster                                                             |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 516 ms: 1.35x faster                                                             |
| deepcopy                   | 368 us                                                       | 280 us: 1.31x faster                                                             |
| generators                 | 37.4 ms                                                      | 28.6 ms: 1.31x faster                                                            |
| comprehensions             | 21.9 us                                                      | 17.5 us: 1.25x faster                                                            |
| deepcopy_memo              | 36.8 us                                                      | 29.5 us: 1.24x faster                                                            |
| pathlib                    | 18.9 ms                                                      | 15.5 ms: 1.21x faster                                                            |
| go                         | 150 ms                                                       | 129 ms: 1.16x faster                                                             |
| deepcopy_reduce            | 3.37 us                                                      | 2.91 us: 1.16x faster                                                            |
| regex_effbot               | 3.57 ms                                                      | 3.17 ms: 1.13x faster                                                            |
| sqlalchemy_declarative     | 159 ms                                                       | 142 ms: 1.12x faster                                                             |
| coroutines                 | 23.0 ms                                                      | 20.8 ms: 1.11x faster                                                            |
| logging_format             | 7.48 us                                                      | 6.77 us: 1.11x faster                                                            |
| float                      | 76.6 ms                                                      | 69.6 ms: 1.10x faster                                                            |
| logging_simple             | 6.71 us                                                      | 6.09 us: 1.10x faster                                                            |
| crypto_pyaes               | 80.3 ms                                                      | 73.4 ms: 1.10x faster                                                            |
| spectral_norm              | 91.6 ms                                                      | 84.0 ms: 1.09x faster                                                            |
| chaos                      | 64.0 ms                                                      | 58.7 ms: 1.09x faster                                                            |
| raytrace                   | 298 ms                                                       | 273 ms: 1.09x faster                                                             |
| regex_compile              | 144 ms                                                       | 134 ms: 1.07x faster                                                             |
| sqlalchemy_imperative      | 18.7 ms                                                      | 17.5 ms: 1.07x faster                                                            |
| sympy_sum                  | 162 ms                                                       | 152 ms: 1.07x faster                                                             |
| scimark_monte_carlo        | 69.0 ms                                                      | 64.9 ms: 1.06x faster                                                            |
| xml_etree_parse            | 144 ms                                                       | 136 ms: 1.06x faster                                                             |
| tomli_loads                | 2.16 sec                                                     | 2.05 sec: 1.05x faster                                                           |
| mdp                        | 2.57 sec                                                     | 2.45 sec: 1.05x faster                                                           |
| sympy_str                  | 302 ms                                                       | 290 ms: 1.04x faster                                                             |
| pidigits                   | 265 ms                                                       | 254 ms: 1.04x faster                                                             |
| xml_etree_generate         | 86.1 ms                                                      | 82.9 ms: 1.04x faster                                                            |
| pprint_pformat             | 1.65 sec                                                     | 1.59 sec: 1.04x faster                                                           |
| django_template            | 38.2 ms                                                      | 36.8 ms: 1.04x faster                                                            |
| scimark_lu                 | 98.8 ms                                                      | 95.4 ms: 1.03x faster                                                            |
| meteor_contest             | 128 ms                                                       | 124 ms: 1.03x faster                                                             |
| sympy_integrate            | 23.9 ms                                                      | 23.2 ms: 1.03x faster                                                            |
| sqlglot_parse              | 1.38 ms                                                      | 1.33 ms: 1.03x faster                                                            |
| bench_thread_pool          | 950 us                                                       | 921 us: 1.03x faster                                                             |
| sqlglot_transpile          | 1.78 ms                                                      | 1.72 ms: 1.03x faster                                                            |
| pprint_safe_repr           | 807 ms                                                       | 786 ms: 1.03x faster                                                             |
| pyflate                    | 439 ms                                                       | 429 ms: 1.02x faster                                                             |
| nqueens                    | 89.9 ms                                                      | 87.9 ms: 1.02x faster                                                            |
| unpickle_pure_python       | 210 us                                                       | 207 us: 1.01x faster                                                             |
| 2to3                       | 285 ms                                                       | 282 ms: 1.01x faster                                                             |
| sqlglot_normalize          | 116 ms                                                       | 115 ms: 1.01x faster                                                             |
| sqlglot_optimize           | 57.5 ms                                                      | 57.7 ms: 1.00x slower                                                            |
| scimark_fft                | 301 ms                                                       | 303 ms: 1.01x slower                                                             |
| pickle_pure_python         | 318 us                                                       | 322 us: 1.01x slower                                                             |
| hexiom                     | 5.96 ms                                                      | 6.06 ms: 1.02x slower                                                            |
| nbody                      | 88.0 ms                                                      | 89.4 ms: 1.02x slower                                                            |
| sqlite_synth               | 2.77 us                                                      | 2.82 us: 1.02x slower                                                            |
| pycparser                  | 1.23 sec                                                     | 1.26 sec: 1.02x slower                                                           |
| dulwich_log                | 65.4 ms                                                      | 66.8 ms: 1.02x slower                                                            |
| sympy_expand               | 484 ms                                                       | 495 ms: 1.02x slower                                                             |
| xml_etree_iterparse        | 103 ms                                                       | 106 ms: 1.03x slower                                                             |
| scimark_sor                | 109 ms                                                       | 112 ms: 1.03x slower                                                             |
| logging_silent             | 94.4 ns                                                      | 97.5 ns: 1.03x slower                                                            |
| richards_super             | 51.3 ms                                                      | 53.1 ms: 1.03x slower                                                            |
| python_startup_no_site     | 8.64 ms                                                      | 8.96 ms: 1.04x slower                                                            |
| deltablue                  | 3.24 ms                                                      | 3.37 ms: 1.04x slower                                                            |
| regex_dna                  | 239 ms                                                       | 249 ms: 1.05x slower                                                             |
| richards                   | 45.7 ms                                                      | 47.9 ms: 1.05x slower                                                            |
| fannkuch                   | 350 ms                                                       | 368 ms: 1.05x slower                                                             |
| async_generators           | 390 ms                                                       | 413 ms: 1.06x slower                                                             |
| regex_v8                   | 23.6 ms                                                      | 25.5 ms: 1.08x slower                                                            |
| mako                       | 10.0 ms                                                      | 10.9 ms: 1.09x slower                                                            |
| telco                      | 6.96 ms                                                      | 7.75 ms: 1.11x slower                                                            |
| typing_runtime_protocols   | 152 us                                                       | 172 us: 1.14x slower                                                             |
| json_dumps                 | 10.2 ms                                                      | 11.6 ms: 1.14x slower                                                            |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.80 ms: 1.14x slower                                                            |
| coverage                   | 66.7 ms                                                      | 77.8 ms: 1.17x slower                                                            |
| json                       | 5.12 ms                                                      | 6.88 ms: 1.35x slower                                                            |
| python_startup             | 11.6 ms                                                      | 16.0 ms: 1.37x slower                                                            |
| json_loads                 | 24.4 us                                                      | 37.8 us: 1.55x slower                                                            |
| create_gc_cycles           | 1.59 ms                                                      | 2.81 ms: 1.77x slower                                                            |
| gc_traversal               | 3.48 ms                                                      | 6.58 ms: 1.89x slower                                                            |
| bench_mp_pool              | 4.76 ms                                                      | 929 ms: 195.05x slower                                                           |
| Geometric mean             | (ref)                                                        | 1.03x slower                                                                     |

Benchmark hidden because not significant (3): xml_etree_process, asyncio_websockets, docutils
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250129-3.14.0a4+-4014e70/bm-20250129-pythonperf2-x86_64-kumaraditya303-per_thread_tasks-3.14.0a4+-4014e70.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.039x faster

# HPT report

- Reliability score: 99.79% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.31x