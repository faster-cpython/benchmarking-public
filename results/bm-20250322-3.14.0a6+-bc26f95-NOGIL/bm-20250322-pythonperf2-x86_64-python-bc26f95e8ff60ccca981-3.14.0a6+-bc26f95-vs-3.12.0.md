# Results vs. 3.12.0

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: linux-x86_64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.052x slower
- HPT reliability: 99.86%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 326 ms: 1.14x slower                                                         |
| docutils       | 2.87 sec                                                     | 2.95 sec: 1.03x slower                                                       |
| Geometric mean | (ref)                                                        | 1.08x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 547 ms: 1.93x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 579 ms: 1.80x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 242 ms: 1.78x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 306 ms: 1.77x faster                                                         |
| async_tree_none            | 452 ms                                                       | 278 ms: 1.63x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 337 ms: 1.61x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 472 ms: 1.48x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 507 ms: 1.37x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.66x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 249 ms: 1.06x faster                                                         |
| nbody          | 88.0 ms                                                      | 132 ms: 1.51x slower                                                         |
| Geometric mean | (ref)                                                        | 1.12x slower                                                                 |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.18 ms: 1.12x faster                                                        |
| regex_dna      | 239 ms                                                       | 249 ms: 1.04x slower                                                         |
| regex_v8       | 23.6 ms                                                      | 25.3 ms: 1.07x slower                                                        |
| regex_compile  | 144 ms                                                       | 160 ms: 1.11x slower                                                         |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 88.1 ms: 1.17x faster                                                        |
| xml_etree_parse      | 144 ms                                                       | 134 ms: 1.07x faster                                                         |
| unpickle             | 14.8 us                                                      | 15.8 us: 1.07x slower                                                        |
| pickle_dict          | 32.5 us                                                      | 35.0 us: 1.08x slower                                                        |
| pickle_list          | 4.43 us                                                      | 4.85 us: 1.10x slower                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 96.3 ms: 1.12x slower                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.42 sec: 1.12x slower                                                       |
| pickle               | 10.5 us                                                      | 12.0 us: 1.14x slower                                                        |
| pickle_pure_python   | 318 us                                                       | 370 us: 1.16x slower                                                         |
| unpickle_pure_python | 210 us                                                       | 244 us: 1.16x slower                                                         |
| unpickle_list        | 4.66 us                                                      | 5.51 us: 1.18x slower                                                        |
| xml_etree_process    | 58.4 ms                                                      | 69.5 ms: 1.19x slower                                                        |
| json_loads           | 24.4 us                                                      | 29.7 us: 1.22x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 13.3 ms: 1.30x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.11x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 13.8 ms: 1.60x slower                                                        |
| python_startup         | 11.6 ms                                                      | 19.4 ms: 1.67x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.63x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 45.5 ms: 1.19x slower                                                        |
| mako            | 10.0 ms                                                      | 17.7 ms: 1.77x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.45x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 547 ms: 1.93x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 579 ms: 1.80x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 242 ms: 1.78x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 306 ms: 1.77x faster                                                         |
| async_tree_none            | 452 ms                                                       | 278 ms: 1.63x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 337 ms: 1.61x faster                                                         |
| gc_traversal               | 3.48 ms                                                      | 2.18 ms: 1.59x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 472 ms: 1.48x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 507 ms: 1.37x faster                                                         |
| generators                 | 37.4 ms                                                      | 29.9 ms: 1.25x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 88.1 ms: 1.17x faster                                                        |
| deepcopy                   | 368 us                                                       | 328 us: 1.12x faster                                                         |
| regex_effbot               | 3.57 ms                                                      | 3.18 ms: 1.12x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 17.4 ms: 1.09x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 21.3 ms: 1.08x faster                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.57 us: 1.08x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 134 ms: 1.07x faster                                                         |
| comprehensions             | 21.9 us                                                      | 20.5 us: 1.07x faster                                                        |
| pidigits                   | 265 ms                                                       | 249 ms: 1.06x faster                                                         |
| asyncio_websockets         | 387 ms                                                       | 375 ms: 1.03x faster                                                         |
| deepcopy_memo              | 36.8 us                                                      | 36.1 us: 1.02x faster                                                        |
| dulwich_log                | 65.4 ms                                                      | 64.5 ms: 1.01x faster                                                        |
| go                         | 150 ms                                                       | 151 ms: 1.01x slower                                                         |
| pycparser                  | 1.23 sec                                                     | 1.25 sec: 1.01x slower                                                       |
| docutils                   | 2.87 sec                                                     | 2.95 sec: 1.03x slower                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 3.51 us: 1.04x slower                                                        |
| regex_dna                  | 239 ms                                                       | 249 ms: 1.04x slower                                                         |
| logging_silent             | 94.4 ns                                                      | 101 ns: 1.07x slower                                                         |
| unpickle                   | 14.8 us                                                      | 15.8 us: 1.07x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 25.3 ms: 1.07x slower                                                        |
| pickle_dict                | 32.5 us                                                      | 35.0 us: 1.08x slower                                                        |
| mdp                        | 2.57 sec                                                     | 2.77 sec: 1.08x slower                                                       |
| sympy_sum                  | 162 ms                                                       | 175 ms: 1.08x slower                                                         |
| sqlalchemy_declarative     | 159 ms                                                       | 172 ms: 1.08x slower                                                         |
| logging_format             | 7.48 us                                                      | 8.12 us: 1.09x slower                                                        |
| chaos                      | 64.0 ms                                                      | 69.5 ms: 1.09x slower                                                        |
| logging_simple             | 6.71 us                                                      | 7.31 us: 1.09x slower                                                        |
| pickle_list                | 4.43 us                                                      | 4.85 us: 1.10x slower                                                        |
| spectral_norm              | 91.6 ms                                                      | 101 ms: 1.10x slower                                                         |
| sqlalchemy_imperative      | 18.7 ms                                                      | 20.6 ms: 1.10x slower                                                        |
| sympy_integrate            | 23.9 ms                                                      | 26.5 ms: 1.11x slower                                                        |
| sympy_str                  | 302 ms                                                       | 336 ms: 1.11x slower                                                         |
| json                       | 5.12 ms                                                      | 5.69 ms: 1.11x slower                                                        |
| scimark_sor                | 109 ms                                                       | 121 ms: 1.11x slower                                                         |
| regex_compile              | 144 ms                                                       | 160 ms: 1.11x slower                                                         |
| pyflate                    | 439 ms                                                       | 489 ms: 1.12x slower                                                         |
| raytrace                   | 298 ms                                                       | 333 ms: 1.12x slower                                                         |
| xml_etree_generate         | 86.1 ms                                                      | 96.3 ms: 1.12x slower                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.42 sec: 1.12x slower                                                       |
| asyncio_tcp                | 378 ms                                                       | 424 ms: 1.12x slower                                                         |
| pprint_safe_repr           | 807 ms                                                       | 909 ms: 1.13x slower                                                         |
| pprint_pformat             | 1.65 sec                                                     | 1.88 sec: 1.13x slower                                                       |
| pickle                     | 10.5 us                                                      | 12.0 us: 1.14x slower                                                        |
| 2to3                       | 285 ms                                                       | 326 ms: 1.14x slower                                                         |
| pickle_pure_python         | 318 us                                                       | 370 us: 1.16x slower                                                         |
| unpickle_pure_python       | 210 us                                                       | 244 us: 1.16x slower                                                         |
| sympy_expand               | 484 ms                                                       | 565 ms: 1.17x slower                                                         |
| scimark_fft                | 301 ms                                                       | 353 ms: 1.17x slower                                                         |
| unpack_sequence            | 53.2 ns                                                      | 62.8 ns: 1.18x slower                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 95.0 ms: 1.18x slower                                                        |
| unpickle_list              | 4.66 us                                                      | 5.51 us: 1.18x slower                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.88 sec: 1.19x slower                                                       |
| xml_etree_process          | 58.4 ms                                                      | 69.5 ms: 1.19x slower                                                        |
| django_template            | 38.2 ms                                                      | 45.5 ms: 1.19x slower                                                        |
| meteor_contest             | 128 ms                                                       | 155 ms: 1.21x slower                                                         |
| json_loads                 | 24.4 us                                                      | 29.7 us: 1.22x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 1.95 ms: 1.23x slower                                                        |
| async_generators           | 390 ms                                                       | 480 ms: 1.23x slower                                                         |
| scimark_lu                 | 98.8 ms                                                      | 122 ms: 1.23x slower                                                         |
| nqueens                    | 89.9 ms                                                      | 111 ms: 1.24x slower                                                         |
| scimark_monte_carlo        | 69.0 ms                                                      | 85.4 ms: 1.24x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 7.39 ms: 1.24x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 4.02 ms: 1.24x slower                                                        |
| richards                   | 45.7 ms                                                      | 57.0 ms: 1.24x slower                                                        |
| richards_super             | 51.3 ms                                                      | 65.6 ms: 1.28x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 13.3 ms: 1.30x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.62 ms: 1.33x slower                                                        |
| fannkuch                   | 350 ms                                                       | 474 ms: 1.35x slower                                                         |
| telco                      | 6.96 ms                                                      | 9.62 ms: 1.38x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 217 us: 1.43x slower                                                         |
| nbody                      | 88.0 ms                                                      | 132 ms: 1.51x slower                                                         |
| bench_thread_pool          | 950 us                                                       | 1.45 ms: 1.53x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 13.8 ms: 1.60x slower                                                        |
| python_startup             | 11.6 ms                                                      | 19.4 ms: 1.67x slower                                                        |
| mako                       | 10.0 ms                                                      | 17.7 ms: 1.77x slower                                                        |
| coverage                   | 66.7 ms                                                      | 118 ms: 1.78x slower                                                         |
| bench_mp_pool              | 4.76 ms                                                      | 50.4 ms: 10.57x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.09x slower                                                                 |

Benchmark hidden because not significant (1): float
Ignored benchmarks (10) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250322-3.14.0a6+-bc26f95-NOGIL/bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.052x slower

# HPT report

- Reliability score: 99.86% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.28x