# Results vs. 3.13.0

- fork: brandtbucher
- ref: tier_two_improvement
- machine: linux-x86_64
- commit hash: bbb07e8
- commit date: 2024-07-13
- overall geometric mean: 1.01x faster
- HPT reliability: 76.31%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 306 ms: 1.05x slower                                                              |
| docutils       | 2.81 sec                                                     | 3.08 sec: 1.10x slower                                                            |
| html5lib       | 71.9 ms                                                      | 70.4 ms: 1.02x faster                                                             |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                      |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 382 ms: 1.21x faster                                                              |
| async_tree_none_tg         | 340 ms                                                       | 304 ms: 1.12x faster                                                              |
| async_tree_memoization     | 452 ms                                                       | 407 ms: 1.11x faster                                                              |
| async_tree_none            | 372 ms                                                       | 338 ms: 1.10x faster                                                              |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 538 ms: 1.07x faster                                                              |
| async_tree_io_tg           | 819 ms                                                       | 776 ms: 1.06x faster                                                              |
| async_tree_io              | 847 ms                                                       | 813 ms: 1.04x faster                                                              |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 581 ms: 1.03x faster                                                              |
| asyncio_tcp                | 380 ms                                                       | 373 ms: 1.02x faster                                                              |
| coroutines                 | 21.6 ms                                                      | 22.1 ms: 1.02x slower                                                             |
| asyncio_websockets         | 382 ms                                                       | 395 ms: 1.03x slower                                                              |
| async_generators           | 359 ms                                                       | 383 ms: 1.07x slower                                                              |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                                      |

Benchmark hidden because not significant (1): asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 74.1 ms: 1.11x faster                                                             |
| nbody          | 88.0 ms                                                      | 83.7 ms: 1.05x faster                                                             |
| pidigits       | 253 ms                                                       | 250 ms: 1.01x faster                                                              |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 135 ms: 1.07x faster                                                              |
| regex_dna      | 244 ms                                                       | 235 ms: 1.04x faster                                                              |
| regex_v8       | 26.2 ms                                                      | 25.6 ms: 1.02x faster                                                             |
| regex_effbot   | 3.37 ms                                                      | 3.49 ms: 1.04x slower                                                             |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| tomli_loads          | 2.41 sec                                                     | 2.09 sec: 1.15x faster                                                            |
| xml_etree_process    | 60.9 ms                                                      | 58.0 ms: 1.05x faster                                                             |
| xml_etree_generate   | 85.3 ms                                                      | 81.8 ms: 1.04x faster                                                             |
| unpickle_pure_python | 214 us                                                       | 211 us: 1.01x faster                                                              |
| xml_etree_parse      | 145 ms                                                       | 143 ms: 1.01x faster                                                              |
| pickle_pure_python   | 318 us                                                       | 315 us: 1.01x faster                                                              |
| json_dumps           | 11.0 ms                                                      | 10.9 ms: 1.01x faster                                                             |
| xml_etree_iterparse  | 100 ms                                                       | 99.4 ms: 1.01x faster                                                             |
| json_loads           | 24.0 us                                                      | 25.1 us: 1.05x slower                                                             |
| Geometric mean       | (ref)                                                        | 1.03x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 13.4 ms: 1.01x slower                                                             |
| python_startup_no_site | 8.94 ms                                                      | 9.09 ms: 1.02x slower                                                             |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                      | 9.24 ms: 1.13x faster                                                             |
| django_template | 38.9 ms                                                      | 40.8 ms: 1.05x slower                                                             |
| genshi_xml      | 57.3 ms                                                      | 61.9 ms: 1.08x slower                                                             |
| genshi_text     | 26.6 ms                                                      | 29.2 ms: 1.10x slower                                                             |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| deepcopy_memo              | 39.5 us                                                      | 28.2 us: 1.40x faster                                                             |
| deepcopy                   | 397 us                                                       | 307 us: 1.30x faster                                                              |
| async_tree_memoization_tg  | 461 ms                                                       | 382 ms: 1.21x faster                                                              |
| spectral_norm              | 97.4 ms                                                      | 82.3 ms: 1.18x faster                                                             |
| richards                   | 52.7 ms                                                      | 44.7 ms: 1.18x faster                                                             |
| deepcopy_reduce            | 3.54 us                                                      | 3.04 us: 1.16x faster                                                             |
| tomli_loads                | 2.41 sec                                                     | 2.09 sec: 1.15x faster                                                            |
| richards_super             | 59.8 ms                                                      | 52.1 ms: 1.15x faster                                                             |
| mako                       | 10.4 ms                                                      | 9.24 ms: 1.13x faster                                                             |
| pyflate                    | 492 ms                                                       | 437 ms: 1.13x faster                                                              |
| async_tree_none_tg         | 340 ms                                                       | 304 ms: 1.12x faster                                                              |
| async_tree_memoization     | 452 ms                                                       | 407 ms: 1.11x faster                                                              |
| float                      | 81.9 ms                                                      | 74.1 ms: 1.11x faster                                                             |
| async_tree_none            | 372 ms                                                       | 338 ms: 1.10x faster                                                              |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 3.92 ms: 1.09x faster                                                             |
| scimark_fft                | 314 ms                                                       | 290 ms: 1.08x faster                                                              |
| pathlib                    | 17.4 ms                                                      | 16.3 ms: 1.07x faster                                                             |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 538 ms: 1.07x faster                                                              |
| regex_compile              | 144 ms                                                       | 135 ms: 1.07x faster                                                              |
| fannkuch                   | 365 ms                                                       | 345 ms: 1.06x faster                                                              |
| async_tree_io_tg           | 819 ms                                                       | 776 ms: 1.06x faster                                                              |
| telco                      | 8.58 ms                                                      | 8.14 ms: 1.05x faster                                                             |
| nbody                      | 88.0 ms                                                      | 83.7 ms: 1.05x faster                                                             |
| xml_etree_process          | 60.9 ms                                                      | 58.0 ms: 1.05x faster                                                             |
| bpe_tokeniser              | 5.10 sec                                                     | 4.88 sec: 1.05x faster                                                            |
| crypto_pyaes               | 72.8 ms                                                      | 69.7 ms: 1.04x faster                                                             |
| xml_etree_generate         | 85.3 ms                                                      | 81.8 ms: 1.04x faster                                                             |
| async_tree_io              | 847 ms                                                       | 813 ms: 1.04x faster                                                              |
| regex_dna                  | 244 ms                                                       | 235 ms: 1.04x faster                                                              |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 581 ms: 1.03x faster                                                              |
| regex_v8                   | 26.2 ms                                                      | 25.6 ms: 1.02x faster                                                             |
| html5lib                   | 71.9 ms                                                      | 70.4 ms: 1.02x faster                                                             |
| asyncio_tcp                | 380 ms                                                       | 373 ms: 1.02x faster                                                              |
| logging_format             | 7.07 us                                                      | 6.96 us: 1.02x faster                                                             |
| unpickle_pure_python       | 214 us                                                       | 211 us: 1.01x faster                                                              |
| pprint_safe_repr           | 812 ms                                                       | 800 ms: 1.01x faster                                                              |
| xml_etree_parse            | 145 ms                                                       | 143 ms: 1.01x faster                                                              |
| pprint_pformat             | 1.65 sec                                                     | 1.63 sec: 1.01x faster                                                            |
| pidigits                   | 253 ms                                                       | 250 ms: 1.01x faster                                                              |
| pickle_pure_python         | 318 us                                                       | 315 us: 1.01x faster                                                              |
| json_dumps                 | 11.0 ms                                                      | 10.9 ms: 1.01x faster                                                             |
| xml_etree_iterparse        | 100 ms                                                       | 99.4 ms: 1.01x faster                                                             |
| scimark_sor                | 126 ms                                                       | 126 ms: 1.00x slower                                                              |
| python_startup             | 13.3 ms                                                      | 13.4 ms: 1.01x slower                                                             |
| meteor_contest             | 128 ms                                                       | 130 ms: 1.01x slower                                                              |
| scimark_monte_carlo        | 64.9 ms                                                      | 65.7 ms: 1.01x slower                                                             |
| python_startup_no_site     | 8.94 ms                                                      | 9.09 ms: 1.02x slower                                                             |
| go                         | 160 ms                                                       | 163 ms: 1.02x slower                                                              |
| bench_thread_pool          | 901 us                                                       | 918 us: 1.02x slower                                                              |
| raytrace                   | 289 ms                                                       | 295 ms: 1.02x slower                                                              |
| coroutines                 | 21.6 ms                                                      | 22.1 ms: 1.02x slower                                                             |
| sqlglot_transpile          | 1.78 ms                                                      | 1.82 ms: 1.02x slower                                                             |
| sqlglot_parse              | 1.38 ms                                                      | 1.41 ms: 1.02x slower                                                             |
| bench_mp_pool              | 4.65 ms                                                      | 4.77 ms: 1.03x slower                                                             |
| sympy_expand               | 505 ms                                                       | 519 ms: 1.03x slower                                                              |
| mdp                        | 2.52 sec                                                     | 2.61 sec: 1.03x slower                                                            |
| thrift                     | 877 us                                                       | 906 us: 1.03x slower                                                              |
| asyncio_websockets         | 382 ms                                                       | 395 ms: 1.03x slower                                                              |
| dask                       | 379 ms                                                       | 393 ms: 1.04x slower                                                              |
| regex_effbot               | 3.37 ms                                                      | 3.49 ms: 1.04x slower                                                             |
| sympy_str                  | 296 ms                                                       | 308 ms: 1.04x slower                                                              |
| json                       | 5.22 ms                                                      | 5.45 ms: 1.04x slower                                                             |
| hexiom                     | 6.33 ms                                                      | 6.62 ms: 1.04x slower                                                             |
| sqlglot_optimize           | 59.7 ms                                                      | 62.4 ms: 1.05x slower                                                             |
| json_loads                 | 24.0 us                                                      | 25.1 us: 1.05x slower                                                             |
| typing_runtime_protocols   | 174 us                                                       | 182 us: 1.05x slower                                                              |
| django_template            | 38.9 ms                                                      | 40.8 ms: 1.05x slower                                                             |
| 2to3                       | 291 ms                                                       | 306 ms: 1.05x slower                                                              |
| comprehensions             | 17.3 us                                                      | 18.3 us: 1.06x slower                                                             |
| chaos                      | 61.7 ms                                                      | 65.5 ms: 1.06x slower                                                             |
| pylint                     | 346 ms                                                       | 368 ms: 1.06x slower                                                              |
| async_generators           | 359 ms                                                       | 383 ms: 1.07x slower                                                              |
| nqueens                    | 88.2 ms                                                      | 94.0 ms: 1.07x slower                                                             |
| deltablue                  | 3.41 ms                                                      | 3.64 ms: 1.07x slower                                                             |
| sympy_sum                  | 154 ms                                                       | 165 ms: 1.07x slower                                                              |
| generators                 | 33.5 ms                                                      | 36.0 ms: 1.08x slower                                                             |
| logging_silent             | 97.7 ns                                                      | 105 ns: 1.08x slower                                                              |
| sqlglot_normalize          | 118 ms                                                       | 128 ms: 1.08x slower                                                              |
| genshi_xml                 | 57.3 ms                                                      | 61.9 ms: 1.08x slower                                                             |
| sympy_integrate            | 23.3 ms                                                      | 25.5 ms: 1.09x slower                                                             |
| docutils                   | 2.81 sec                                                     | 3.08 sec: 1.10x slower                                                            |
| genshi_text                | 26.6 ms                                                      | 29.2 ms: 1.10x slower                                                             |
| create_gc_cycles           | 1.76 ms                                                      | 1.94 ms: 1.10x slower                                                             |
| gc_traversal               | 4.11 ms                                                      | 4.68 ms: 1.14x slower                                                             |
| scimark_lu                 | 97.8 ms                                                      | 113 ms: 1.15x slower                                                              |
| Geometric mean             | (ref)                                                        | 1.01x faster                                                                      |

Benchmark hidden because not significant (6): pycparser, logging_simple, dulwich_log, coverage, asyncio_tcp_ssl, tornado_http
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 76.31% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x