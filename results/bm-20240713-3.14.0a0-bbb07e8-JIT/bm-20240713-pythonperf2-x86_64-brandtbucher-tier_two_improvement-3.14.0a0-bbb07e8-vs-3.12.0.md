# Results vs. 3.12.0

- fork: brandtbucher
- ref: tier_two_improvement
- machine: linux-x86_64
- commit hash: bbb07e8
- commit date: 2024-07-13
- overall geometric mean: 1.02x faster
- HPT reliability: 84.53%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 306 ms: 1.07x slower                                                              |
| docutils       | 2.87 sec                                                     | 3.08 sec: 1.08x slower                                                            |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                      |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 304 ms: 1.42x faster                                                              |
| async_tree_memoization_tg  | 540 ms                                                       | 382 ms: 1.41x faster                                                              |
| async_tree_io_tg           | 1.05 sec                                                     | 776 ms: 1.36x faster                                                              |
| async_tree_none            | 452 ms                                                       | 338 ms: 1.34x faster                                                              |
| async_tree_memoization     | 544 ms                                                       | 407 ms: 1.34x faster                                                              |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 538 ms: 1.30x faster                                                              |
| async_tree_io              | 1.04 sec                                                     | 813 ms: 1.28x faster                                                              |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 581 ms: 1.20x faster                                                              |
| Geometric mean             | (ref)                                                        | 1.33x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 250 ms: 1.06x faster                                                              |
| nbody          | 88.0 ms                                                      | 83.7 ms: 1.05x faster                                                             |
| float          | 76.6 ms                                                      | 74.1 ms: 1.03x faster                                                             |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 135 ms: 1.06x faster                                                              |
| regex_effbot   | 3.57 ms                                                      | 3.49 ms: 1.02x faster                                                             |
| regex_dna      | 239 ms                                                       | 235 ms: 1.01x faster                                                              |
| regex_v8       | 23.6 ms                                                      | 25.6 ms: 1.08x slower                                                             |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 81.8 ms: 1.05x faster                                                             |
| xml_etree_iterparse  | 103 ms                                                       | 99.4 ms: 1.03x faster                                                             |
| tomli_loads          | 2.16 sec                                                     | 2.09 sec: 1.03x faster                                                            |
| pickle_pure_python   | 318 us                                                       | 315 us: 1.01x faster                                                              |
| xml_etree_process    | 58.4 ms                                                      | 58.0 ms: 1.01x faster                                                             |
| xml_etree_parse      | 144 ms                                                       | 143 ms: 1.01x faster                                                              |
| unpickle_pure_python | 210 us                                                       | 211 us: 1.01x slower                                                              |
| json_loads           | 24.4 us                                                      | 25.1 us: 1.03x slower                                                             |
| json_dumps           | 10.2 ms                                                      | 10.9 ms: 1.06x slower                                                             |
| Geometric mean       | (ref)                                                        | 1.00x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.09 ms: 1.05x slower                                                             |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                             |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.24 ms: 1.08x faster                                                             |
| django_template | 38.2 ms                                                      | 40.8 ms: 1.07x slower                                                             |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 304 ms: 1.42x faster                                                              |
| async_tree_memoization_tg  | 540 ms                                                       | 382 ms: 1.41x faster                                                              |
| async_tree_io_tg           | 1.05 sec                                                     | 776 ms: 1.36x faster                                                              |
| async_tree_none            | 452 ms                                                       | 338 ms: 1.34x faster                                                              |
| async_tree_memoization     | 544 ms                                                       | 407 ms: 1.34x faster                                                              |
| deepcopy_memo              | 36.8 us                                                      | 28.2 us: 1.30x faster                                                             |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 538 ms: 1.30x faster                                                              |
| async_tree_io              | 1.04 sec                                                     | 813 ms: 1.28x faster                                                              |
| deepcopy                   | 368 us                                                       | 307 us: 1.20x faster                                                              |
| comprehensions             | 21.9 us                                                      | 18.3 us: 1.20x faster                                                             |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 581 ms: 1.20x faster                                                              |
| pathlib                    | 18.9 ms                                                      | 16.3 ms: 1.16x faster                                                             |
| crypto_pyaes               | 80.3 ms                                                      | 69.7 ms: 1.15x faster                                                             |
| spectral_norm              | 91.6 ms                                                      | 82.3 ms: 1.11x faster                                                             |
| deepcopy_reduce            | 3.37 us                                                      | 3.04 us: 1.11x faster                                                             |
| mako                       | 10.0 ms                                                      | 9.24 ms: 1.08x faster                                                             |
| logging_format             | 7.48 us                                                      | 6.96 us: 1.07x faster                                                             |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 3.92 ms: 1.07x faster                                                             |
| regex_compile              | 144 ms                                                       | 135 ms: 1.06x faster                                                              |
| pidigits                   | 265 ms                                                       | 250 ms: 1.06x faster                                                              |
| logging_simple             | 6.71 us                                                      | 6.36 us: 1.05x faster                                                             |
| xml_etree_generate         | 86.1 ms                                                      | 81.8 ms: 1.05x faster                                                             |
| nbody                      | 88.0 ms                                                      | 83.7 ms: 1.05x faster                                                             |
| scimark_monte_carlo        | 69.0 ms                                                      | 65.7 ms: 1.05x faster                                                             |
| coroutines                 | 23.0 ms                                                      | 22.1 ms: 1.04x faster                                                             |
| generators                 | 37.4 ms                                                      | 36.0 ms: 1.04x faster                                                             |
| scimark_fft                | 301 ms                                                       | 290 ms: 1.04x faster                                                              |
| bench_thread_pool          | 950 us                                                       | 918 us: 1.03x faster                                                              |
| xml_etree_iterparse        | 103 ms                                                       | 99.4 ms: 1.03x faster                                                             |
| float                      | 76.6 ms                                                      | 74.1 ms: 1.03x faster                                                             |
| tomli_loads                | 2.16 sec                                                     | 2.09 sec: 1.03x faster                                                            |
| richards                   | 45.7 ms                                                      | 44.7 ms: 1.02x faster                                                             |
| regex_effbot               | 3.57 ms                                                      | 3.49 ms: 1.02x faster                                                             |
| async_generators           | 390 ms                                                       | 383 ms: 1.02x faster                                                              |
| fannkuch                   | 350 ms                                                       | 345 ms: 1.02x faster                                                              |
| pprint_pformat             | 1.65 sec                                                     | 1.63 sec: 1.02x faster                                                            |
| regex_dna                  | 239 ms                                                       | 235 ms: 1.01x faster                                                              |
| asyncio_tcp                | 378 ms                                                       | 373 ms: 1.01x faster                                                              |
| raytrace                   | 298 ms                                                       | 295 ms: 1.01x faster                                                              |
| pickle_pure_python         | 318 us                                                       | 315 us: 1.01x faster                                                              |
| pprint_safe_repr           | 807 ms                                                       | 800 ms: 1.01x faster                                                              |
| xml_etree_process          | 58.4 ms                                                      | 58.0 ms: 1.01x faster                                                             |
| xml_etree_parse            | 144 ms                                                       | 143 ms: 1.01x faster                                                              |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.00x faster                                                            |
| pyflate                    | 439 ms                                                       | 437 ms: 1.00x faster                                                              |
| unpickle_pure_python       | 210 us                                                       | 211 us: 1.01x slower                                                              |
| pycparser                  | 1.23 sec                                                     | 1.25 sec: 1.01x slower                                                            |
| meteor_contest             | 128 ms                                                       | 130 ms: 1.01x slower                                                              |
| mdp                        | 2.57 sec                                                     | 2.61 sec: 1.01x slower                                                            |
| richards_super             | 51.3 ms                                                      | 52.1 ms: 1.02x slower                                                             |
| sympy_str                  | 302 ms                                                       | 308 ms: 1.02x slower                                                              |
| sympy_sum                  | 162 ms                                                       | 165 ms: 1.02x slower                                                              |
| asyncio_websockets         | 387 ms                                                       | 395 ms: 1.02x slower                                                              |
| chaos                      | 64.0 ms                                                      | 65.5 ms: 1.02x slower                                                             |
| sqlglot_transpile          | 1.78 ms                                                      | 1.82 ms: 1.02x slower                                                             |
| sqlglot_parse              | 1.38 ms                                                      | 1.41 ms: 1.03x slower                                                             |
| json_loads                 | 24.4 us                                                      | 25.1 us: 1.03x slower                                                             |
| nqueens                    | 89.9 ms                                                      | 94.0 ms: 1.05x slower                                                             |
| python_startup_no_site     | 8.64 ms                                                      | 9.09 ms: 1.05x slower                                                             |
| json_dumps                 | 10.2 ms                                                      | 10.9 ms: 1.06x slower                                                             |
| sympy_integrate            | 23.9 ms                                                      | 25.5 ms: 1.06x slower                                                             |
| json                       | 5.12 ms                                                      | 5.45 ms: 1.06x slower                                                             |
| django_template            | 38.2 ms                                                      | 40.8 ms: 1.07x slower                                                             |
| sympy_expand               | 484 ms                                                       | 519 ms: 1.07x slower                                                              |
| 2to3                       | 285 ms                                                       | 306 ms: 1.07x slower                                                              |
| docutils                   | 2.87 sec                                                     | 3.08 sec: 1.08x slower                                                            |
| regex_v8                   | 23.6 ms                                                      | 25.6 ms: 1.08x slower                                                             |
| sqlglot_optimize           | 57.5 ms                                                      | 62.4 ms: 1.09x slower                                                             |
| go                         | 150 ms                                                       | 163 ms: 1.09x slower                                                              |
| sqlglot_normalize          | 116 ms                                                       | 128 ms: 1.10x slower                                                              |
| hexiom                     | 5.96 ms                                                      | 6.62 ms: 1.11x slower                                                             |
| logging_silent             | 94.4 ns                                                      | 105 ns: 1.11x slower                                                              |
| deltablue                  | 3.24 ms                                                      | 3.64 ms: 1.12x slower                                                             |
| scimark_lu                 | 98.8 ms                                                      | 113 ms: 1.14x slower                                                              |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                             |
| scimark_sor                | 109 ms                                                       | 126 ms: 1.16x slower                                                              |
| telco                      | 6.96 ms                                                      | 8.14 ms: 1.17x slower                                                             |
| typing_runtime_protocols   | 152 us                                                       | 182 us: 1.20x slower                                                              |
| coverage                   | 66.7 ms                                                      | 81.1 ms: 1.22x slower                                                             |
| create_gc_cycles           | 1.59 ms                                                      | 1.94 ms: 1.22x slower                                                             |
| gc_traversal               | 3.48 ms                                                      | 4.68 ms: 1.34x slower                                                             |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                      |

Benchmark hidden because not significant (4): tornado_http, dulwich_log, dask, bench_mp_pool
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240713-3.14.0a0-bbb07e8-JIT/bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 84.53% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x