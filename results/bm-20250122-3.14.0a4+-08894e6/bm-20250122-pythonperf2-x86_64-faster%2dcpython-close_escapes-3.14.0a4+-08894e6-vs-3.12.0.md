# Results vs. 3.12.0

- fork: faster-cpython
- ref: close_escapes
- machine: linux-x86_64
- commit hash: 08894e6
- commit date: 2025-01-22
- overall geometric mean: 1.046x faster
- HPT reliability: 99.47%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250122-pythonperf2-x86_64-faster%2dcpython-close_escapes-3.14.0a4+-08894e6 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 281 ms: 1.01x faster                                                            |
| docutils       | 2.87 sec                                                     | 2.89 sec: 1.01x slower                                                          |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250122-pythonperf2-x86_64-faster%2dcpython-close_escapes-3.14.0a4+-08894e6 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 624 ms: 1.69x faster                                                            |
| async_tree_io              | 1.04 sec                                                     | 624 ms: 1.67x faster                                                            |
| async_tree_memoization_tg  | 540 ms                                                       | 327 ms: 1.65x faster                                                            |
| async_tree_none            | 452 ms                                                       | 276 ms: 1.64x faster                                                            |
| async_tree_none_tg         | 431 ms                                                       | 267 ms: 1.61x faster                                                            |
| async_tree_memoization     | 544 ms                                                       | 343 ms: 1.59x faster                                                            |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 498 ms: 1.40x faster                                                            |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 508 ms: 1.37x faster                                                            |
| Geometric mean             | (ref)                                                        | 1.57x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250122-pythonperf2-x86_64-faster%2dcpython-close_escapes-3.14.0a4+-08894e6 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 69.9 ms: 1.10x faster                                                           |
| pidigits       | 265 ms                                                       | 254 ms: 1.04x faster                                                            |
| nbody          | 88.0 ms                                                      | 90.7 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250122-pythonperf2-x86_64-faster%2dcpython-close_escapes-3.14.0a4+-08894e6 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.17 ms: 1.13x faster                                                           |
| regex_compile  | 144 ms                                                       | 137 ms: 1.05x faster                                                            |
| regex_dna      | 239 ms                                                       | 248 ms: 1.04x slower                                                            |
| regex_v8       | 23.6 ms                                                      | 25.8 ms: 1.09x slower                                                           |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250122-pythonperf2-x86_64-faster%2dcpython-close_escapes-3.14.0a4+-08894e6 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 95.4 ms: 1.08x faster                                                           |
| xml_etree_parse      | 144 ms                                                       | 134 ms: 1.07x faster                                                            |
| xml_etree_generate   | 86.1 ms                                                      | 82.5 ms: 1.04x faster                                                           |
| tomli_loads          | 2.16 sec                                                     | 2.09 sec: 1.03x faster                                                          |
| unpickle_pure_python | 210 us                                                       | 219 us: 1.05x slower                                                            |
| json_loads           | 24.4 us                                                      | 25.5 us: 1.05x slower                                                           |
| pickle_pure_python   | 318 us                                                       | 335 us: 1.05x slower                                                            |
| xml_etree_process    | 58.4 ms                                                      | 61.8 ms: 1.06x slower                                                           |
| json_dumps           | 10.2 ms                                                      | 11.7 ms: 1.14x slower                                                           |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250122-pythonperf2-x86_64-faster%2dcpython-close_escapes-3.14.0a4+-08894e6 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.97 ms: 1.04x slower                                                           |
| python_startup         | 11.6 ms                                                      | 16.0 ms: 1.38x slower                                                           |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250122-pythonperf2-x86_64-faster%2dcpython-close_escapes-3.14.0a4+-08894e6 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 36.8 ms: 1.04x faster                                                           |
| mako            | 10.0 ms                                                      | 10.9 ms: 1.09x slower                                                           |
| Geometric mean  | (ref)                                                        | 1.02x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250122-pythonperf2-x86_64-faster%2dcpython-close_escapes-3.14.0a4+-08894e6 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 624 ms: 1.69x faster                                                            |
| async_tree_io              | 1.04 sec                                                     | 624 ms: 1.67x faster                                                            |
| async_tree_memoization_tg  | 540 ms                                                       | 327 ms: 1.65x faster                                                            |
| async_tree_none            | 452 ms                                                       | 276 ms: 1.64x faster                                                            |
| async_tree_none_tg         | 431 ms                                                       | 267 ms: 1.61x faster                                                            |
| async_tree_memoization     | 544 ms                                                       | 343 ms: 1.59x faster                                                            |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 498 ms: 1.40x faster                                                            |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 508 ms: 1.37x faster                                                            |
| generators                 | 37.4 ms                                                      | 28.8 ms: 1.30x faster                                                           |
| deepcopy                   | 368 us                                                       | 286 us: 1.29x faster                                                            |
| comprehensions             | 21.9 us                                                      | 17.9 us: 1.23x faster                                                           |
| deepcopy_memo              | 36.8 us                                                      | 30.2 us: 1.22x faster                                                           |
| pathlib                    | 18.9 ms                                                      | 15.9 ms: 1.19x faster                                                           |
| go                         | 150 ms                                                       | 128 ms: 1.17x faster                                                            |
| deepcopy_reduce            | 3.37 us                                                      | 2.95 us: 1.14x faster                                                           |
| regex_effbot               | 3.57 ms                                                      | 3.17 ms: 1.13x faster                                                           |
| scimark_monte_carlo        | 69.0 ms                                                      | 61.7 ms: 1.12x faster                                                           |
| float                      | 76.6 ms                                                      | 69.9 ms: 1.10x faster                                                           |
| coroutines                 | 23.0 ms                                                      | 21.0 ms: 1.10x faster                                                           |
| sqlalchemy_declarative     | 159 ms                                                       | 145 ms: 1.10x faster                                                            |
| spectral_norm              | 91.6 ms                                                      | 84.3 ms: 1.09x faster                                                           |
| chaos                      | 64.0 ms                                                      | 59.1 ms: 1.08x faster                                                           |
| crypto_pyaes               | 80.3 ms                                                      | 74.4 ms: 1.08x faster                                                           |
| xml_etree_iterparse        | 103 ms                                                       | 95.4 ms: 1.08x faster                                                           |
| raytrace                   | 298 ms                                                       | 277 ms: 1.07x faster                                                            |
| xml_etree_parse            | 144 ms                                                       | 134 ms: 1.07x faster                                                            |
| sympy_sum                  | 162 ms                                                       | 152 ms: 1.07x faster                                                            |
| regex_compile              | 144 ms                                                       | 137 ms: 1.05x faster                                                            |
| sqlglot_parse              | 1.38 ms                                                      | 1.31 ms: 1.05x faster                                                           |
| sqlglot_transpile          | 1.78 ms                                                      | 1.70 ms: 1.05x faster                                                           |
| sympy_str                  | 302 ms                                                       | 289 ms: 1.05x faster                                                            |
| mdp                        | 2.57 sec                                                     | 2.46 sec: 1.04x faster                                                          |
| xml_etree_generate         | 86.1 ms                                                      | 82.5 ms: 1.04x faster                                                           |
| sqlalchemy_imperative      | 18.7 ms                                                      | 18.0 ms: 1.04x faster                                                           |
| pidigits                   | 265 ms                                                       | 254 ms: 1.04x faster                                                            |
| django_template            | 38.2 ms                                                      | 36.8 ms: 1.04x faster                                                           |
| async_generators           | 390 ms                                                       | 377 ms: 1.03x faster                                                            |
| scimark_lu                 | 98.8 ms                                                      | 95.5 ms: 1.03x faster                                                           |
| tomli_loads                | 2.16 sec                                                     | 2.09 sec: 1.03x faster                                                          |
| sympy_integrate            | 23.9 ms                                                      | 23.2 ms: 1.03x faster                                                           |
| pprint_pformat             | 1.65 sec                                                     | 1.61 sec: 1.03x faster                                                          |
| logging_format             | 7.48 us                                                      | 7.27 us: 1.03x faster                                                           |
| bench_thread_pool          | 950 us                                                       | 923 us: 1.03x faster                                                            |
| meteor_contest             | 128 ms                                                       | 125 ms: 1.03x faster                                                            |
| pprint_safe_repr           | 807 ms                                                       | 789 ms: 1.02x faster                                                            |
| logging_simple             | 6.71 us                                                      | 6.61 us: 1.02x faster                                                           |
| 2to3                       | 285 ms                                                       | 281 ms: 1.01x faster                                                            |
| nqueens                    | 89.9 ms                                                      | 88.9 ms: 1.01x faster                                                           |
| asyncio_websockets         | 387 ms                                                       | 384 ms: 1.01x faster                                                            |
| sqlglot_optimize           | 57.5 ms                                                      | 57.7 ms: 1.00x slower                                                           |
| sqlglot_normalize          | 116 ms                                                       | 116 ms: 1.00x slower                                                            |
| hexiom                     | 5.96 ms                                                      | 6.01 ms: 1.01x slower                                                           |
| richards                   | 45.7 ms                                                      | 46.1 ms: 1.01x slower                                                           |
| docutils                   | 2.87 sec                                                     | 2.89 sec: 1.01x slower                                                          |
| dulwich_log                | 65.4 ms                                                      | 66.7 ms: 1.02x slower                                                           |
| sympy_expand               | 484 ms                                                       | 494 ms: 1.02x slower                                                            |
| sqlite_synth               | 2.77 us                                                      | 2.83 us: 1.02x slower                                                           |
| pycparser                  | 1.23 sec                                                     | 1.26 sec: 1.02x slower                                                          |
| logging_silent             | 94.4 ns                                                      | 96.6 ns: 1.02x slower                                                           |
| nbody                      | 88.0 ms                                                      | 90.7 ms: 1.03x slower                                                           |
| fannkuch                   | 350 ms                                                       | 361 ms: 1.03x slower                                                            |
| richards_super             | 51.3 ms                                                      | 53.3 ms: 1.04x slower                                                           |
| python_startup_no_site     | 8.64 ms                                                      | 8.97 ms: 1.04x slower                                                           |
| regex_dna                  | 239 ms                                                       | 248 ms: 1.04x slower                                                            |
| pyflate                    | 439 ms                                                       | 457 ms: 1.04x slower                                                            |
| unpickle_pure_python       | 210 us                                                       | 219 us: 1.05x slower                                                            |
| json_loads                 | 24.4 us                                                      | 25.5 us: 1.05x slower                                                           |
| json                       | 5.12 ms                                                      | 5.36 ms: 1.05x slower                                                           |
| pickle_pure_python         | 318 us                                                       | 335 us: 1.05x slower                                                            |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.44 ms: 1.06x slower                                                           |
| xml_etree_process          | 58.4 ms                                                      | 61.8 ms: 1.06x slower                                                           |
| deltablue                  | 3.24 ms                                                      | 3.44 ms: 1.06x slower                                                           |
| scimark_sor                | 109 ms                                                       | 116 ms: 1.07x slower                                                            |
| mako                       | 10.0 ms                                                      | 10.9 ms: 1.09x slower                                                           |
| regex_v8                   | 23.6 ms                                                      | 25.8 ms: 1.09x slower                                                           |
| coverage                   | 66.7 ms                                                      | 75.3 ms: 1.13x slower                                                           |
| json_dumps                 | 10.2 ms                                                      | 11.7 ms: 1.14x slower                                                           |
| telco                      | 6.96 ms                                                      | 8.14 ms: 1.17x slower                                                           |
| typing_runtime_protocols   | 152 us                                                       | 178 us: 1.17x slower                                                            |
| python_startup             | 11.6 ms                                                      | 16.0 ms: 1.38x slower                                                           |
| create_gc_cycles           | 1.59 ms                                                      | 2.80 ms: 1.76x slower                                                           |
| gc_traversal               | 3.48 ms                                                      | 6.65 ms: 1.91x slower                                                           |
| bench_mp_pool              | 4.76 ms                                                      | 1.94 sec: 408.12x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.03x slower                                                                    |

Benchmark hidden because not significant (1): scimark_fft
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250122-3.14.0a4+-08894e6/bm-20250122-pythonperf2-x86_64-faster%2dcpython-close_escapes-3.14.0a4+-08894e6.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.046x faster

# HPT report

- Reliability score: 99.47% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x