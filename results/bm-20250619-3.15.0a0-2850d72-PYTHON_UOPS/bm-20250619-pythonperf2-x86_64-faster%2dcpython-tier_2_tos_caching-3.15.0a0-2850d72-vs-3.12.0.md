# Results vs. 3.12.0

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-x86_64
- commit hash: 2850d72
- commit date: 2025-06-19
- overall geometric mean: 1.140x slower
- HPT reliability: 99.46%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 333 ms: 1.17x slower                                                                |
| docutils       | 2.87 sec                                                     | 3.17 sec: 1.10x slower                                                              |
| Geometric mean | (ref)                                                        | 1.14x slower                                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 681 ms: 1.55x faster                                                                |
| async_tree_io              | 1.04 sec                                                     | 675 ms: 1.54x faster                                                                |
| async_tree_memoization     | 544 ms                                                       | 361 ms: 1.51x faster                                                                |
| async_tree_memoization_tg  | 540 ms                                                       | 360 ms: 1.50x faster                                                                |
| async_tree_none_tg         | 431 ms                                                       | 295 ms: 1.46x faster                                                                |
| async_tree_none            | 452 ms                                                       | 312 ms: 1.45x faster                                                                |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 534 ms: 1.30x faster                                                                |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 536 ms: 1.30x faster                                                                |
| Geometric mean             | (ref)                                                        | 1.45x faster                                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 259 ms: 1.02x faster                                                                |
| float          | 76.6 ms                                                      | 113 ms: 1.47x slower                                                                |
| nbody          | 88.0 ms                                                      | 218 ms: 2.47x slower                                                                |
| Geometric mean | (ref)                                                        | 1.53x slower                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_dna      | 239 ms                                                       | 220 ms: 1.08x faster                                                                |
| regex_effbot   | 3.57 ms                                                      | 3.53 ms: 1.01x faster                                                               |
| regex_v8       | 23.6 ms                                                      | 23.9 ms: 1.01x slower                                                               |
| regex_compile  | 144 ms                                                       | 164 ms: 1.14x slower                                                                |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| xml_etree_parse      | 144 ms                                                       | 147 ms: 1.02x slower                                                                |
| json_loads           | 24.4 us                                                      | 25.3 us: 1.04x slower                                                               |
| json_dumps           | 10.2 ms                                                      | 11.2 ms: 1.09x slower                                                               |
| xml_etree_iterparse  | 103 ms                                                       | 113 ms: 1.10x slower                                                                |
| pickle_pure_python   | 318 us                                                       | 429 us: 1.35x slower                                                                |
| xml_etree_generate   | 86.1 ms                                                      | 119 ms: 1.38x slower                                                                |
| xml_etree_process    | 58.4 ms                                                      | 82.4 ms: 1.41x slower                                                               |
| tomli_loads          | 2.16 sec                                                     | 3.17 sec: 1.47x slower                                                              |
| unpickle_pure_python | 210 us                                                       | 428 us: 2.04x slower                                                                |
| Geometric mean       | (ref)                                                        | 1.29x slower                                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.83 ms: 1.02x slower                                                               |
| python_startup         | 11.6 ms                                                      | 15.3 ms: 1.32x slower                                                               |
| Geometric mean         | (ref)                                                        | 1.16x slower                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 36.7 ms: 1.04x faster                                                               |
| mako            | 10.0 ms                                                      | 20.8 ms: 2.08x slower                                                               |
| Geometric mean  | (ref)                                                        | 1.41x slower                                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.52 sec: 1.69x faster                                                              |
| async_tree_io_tg           | 1.05 sec                                                     | 681 ms: 1.55x faster                                                                |
| async_tree_io              | 1.04 sec                                                     | 675 ms: 1.54x faster                                                                |
| async_tree_memoization     | 544 ms                                                       | 361 ms: 1.51x faster                                                                |
| async_tree_memoization_tg  | 540 ms                                                       | 360 ms: 1.50x faster                                                                |
| async_tree_none_tg         | 431 ms                                                       | 295 ms: 1.46x faster                                                                |
| async_tree_none            | 452 ms                                                       | 312 ms: 1.45x faster                                                                |
| deepcopy                   | 368 us                                                       | 279 us: 1.32x faster                                                                |
| deepcopy_memo              | 36.8 us                                                      | 28.1 us: 1.31x faster                                                               |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 534 ms: 1.30x faster                                                                |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 536 ms: 1.30x faster                                                                |
| generators                 | 37.4 ms                                                      | 29.1 ms: 1.28x faster                                                               |
| deepcopy_reduce            | 3.37 us                                                      | 2.98 us: 1.13x faster                                                               |
| pathlib                    | 18.9 ms                                                      | 16.9 ms: 1.12x faster                                                               |
| regex_dna                  | 239 ms                                                       | 220 ms: 1.08x faster                                                                |
| scimark_lu                 | 98.8 ms                                                      | 92.9 ms: 1.06x faster                                                               |
| scimark_sor                | 109 ms                                                       | 103 ms: 1.06x faster                                                                |
| logging_format             | 7.48 us                                                      | 7.11 us: 1.05x faster                                                               |
| django_template            | 38.2 ms                                                      | 36.7 ms: 1.04x faster                                                               |
| dulwich_log                | 65.4 ms                                                      | 62.9 ms: 1.04x faster                                                               |
| logging_simple             | 6.71 us                                                      | 6.49 us: 1.03x faster                                                               |
| coroutines                 | 23.0 ms                                                      | 22.3 ms: 1.03x faster                                                               |
| pidigits                   | 265 ms                                                       | 259 ms: 1.02x faster                                                                |
| regex_effbot               | 3.57 ms                                                      | 3.53 ms: 1.01x faster                                                               |
| chaos                      | 64.0 ms                                                      | 63.4 ms: 1.01x faster                                                               |
| asyncio_websockets         | 387 ms                                                       | 384 ms: 1.01x faster                                                                |
| sympy_integrate            | 23.9 ms                                                      | 23.7 ms: 1.01x faster                                                               |
| regex_v8                   | 23.6 ms                                                      | 23.9 ms: 1.01x slower                                                               |
| sympy_sum                  | 162 ms                                                       | 164 ms: 1.01x slower                                                                |
| python_startup_no_site     | 8.64 ms                                                      | 8.83 ms: 1.02x slower                                                               |
| xml_etree_parse            | 144 ms                                                       | 147 ms: 1.02x slower                                                                |
| json_loads                 | 24.4 us                                                      | 25.3 us: 1.04x slower                                                               |
| json                       | 5.12 ms                                                      | 5.36 ms: 1.05x slower                                                               |
| sympy_str                  | 302 ms                                                       | 321 ms: 1.06x slower                                                                |
| json_dumps                 | 10.2 ms                                                      | 11.2 ms: 1.09x slower                                                               |
| xml_etree_iterparse        | 103 ms                                                       | 113 ms: 1.10x slower                                                                |
| docutils                   | 2.87 sec                                                     | 3.17 sec: 1.10x slower                                                              |
| sqlite_synth               | 2.77 us                                                      | 3.06 us: 1.10x slower                                                               |
| regex_compile              | 144 ms                                                       | 164 ms: 1.14x slower                                                                |
| raytrace                   | 298 ms                                                       | 343 ms: 1.15x slower                                                                |
| sympy_expand               | 484 ms                                                       | 562 ms: 1.16x slower                                                                |
| coverage                   | 66.7 ms                                                      | 77.8 ms: 1.17x slower                                                               |
| 2to3                       | 285 ms                                                       | 333 ms: 1.17x slower                                                                |
| async_generators           | 390 ms                                                       | 462 ms: 1.18x slower                                                                |
| nqueens                    | 89.9 ms                                                      | 107 ms: 1.20x slower                                                                |
| richards                   | 45.7 ms                                                      | 57.5 ms: 1.26x slower                                                               |
| richards_super             | 51.3 ms                                                      | 64.7 ms: 1.26x slower                                                               |
| pycparser                  | 1.23 sec                                                     | 1.56 sec: 1.27x slower                                                              |
| meteor_contest             | 128 ms                                                       | 169 ms: 1.32x slower                                                                |
| python_startup             | 11.6 ms                                                      | 15.3 ms: 1.32x slower                                                               |
| pickle_pure_python         | 318 us                                                       | 429 us: 1.35x slower                                                                |
| scimark_monte_carlo        | 69.0 ms                                                      | 95.0 ms: 1.38x slower                                                               |
| xml_etree_generate         | 86.1 ms                                                      | 119 ms: 1.38x slower                                                                |
| telco                      | 6.96 ms                                                      | 9.73 ms: 1.40x slower                                                               |
| typing_runtime_protocols   | 152 us                                                       | 214 us: 1.41x slower                                                                |
| xml_etree_process          | 58.4 ms                                                      | 82.4 ms: 1.41x slower                                                               |
| crypto_pyaes               | 80.3 ms                                                      | 118 ms: 1.46x slower                                                                |
| tomli_loads                | 2.16 sec                                                     | 3.17 sec: 1.47x slower                                                              |
| float                      | 76.6 ms                                                      | 113 ms: 1.47x slower                                                                |
| comprehensions             | 21.9 us                                                      | 32.4 us: 1.48x slower                                                               |
| pyflate                    | 439 ms                                                       | 671 ms: 1.53x slower                                                                |
| pprint_pformat             | 1.65 sec                                                     | 2.69 sec: 1.63x slower                                                              |
| go                         | 150 ms                                                       | 246 ms: 1.64x slower                                                                |
| pprint_safe_repr           | 807 ms                                                       | 1.33 sec: 1.64x slower                                                              |
| scimark_fft                | 301 ms                                                       | 513 ms: 1.70x slower                                                                |
| create_gc_cycles           | 1.59 ms                                                      | 2.88 ms: 1.81x slower                                                               |
| gc_traversal               | 3.48 ms                                                      | 6.72 ms: 1.93x slower                                                               |
| deltablue                  | 3.24 ms                                                      | 6.35 ms: 1.96x slower                                                               |
| hexiom                     | 5.96 ms                                                      | 11.7 ms: 1.97x slower                                                               |
| fannkuch                   | 350 ms                                                       | 690 ms: 1.97x slower                                                                |
| unpickle_pure_python       | 210 us                                                       | 428 us: 2.04x slower                                                                |
| spectral_norm              | 91.6 ms                                                      | 189 ms: 2.07x slower                                                                |
| mako                       | 10.0 ms                                                      | 20.8 ms: 2.08x slower                                                               |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 9.49 ms: 2.26x slower                                                               |
| nbody                      | 88.0 ms                                                      | 218 ms: 2.47x slower                                                                |
| logging_silent             | 94.4 ns                                                      | 504 ns: 5.34x slower                                                                |
| Geometric mean             | (ref)                                                        | 1.18x slower                                                                        |
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250619-3.15.0a0-2850d72-PYTHON_UOPS/bm-20250619-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.140x slower

# HPT report

- Reliability score: 99.46% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.13x