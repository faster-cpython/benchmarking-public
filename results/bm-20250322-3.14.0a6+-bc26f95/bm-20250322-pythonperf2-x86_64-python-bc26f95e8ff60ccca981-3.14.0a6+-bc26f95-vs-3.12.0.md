# Results vs. 3.12.0

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: linux-x86_64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.022x faster
- HPT reliability: 84.73%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 287 ms: 1.01x slower                                                         |
| docutils       | 2.87 sec                                                     | 2.92 sec: 1.02x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 332 ms: 1.63x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 653 ms: 1.60x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 660 ms: 1.60x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 343 ms: 1.59x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 275 ms: 1.56x faster                                                         |
| async_tree_none            | 452 ms                                                       | 295 ms: 1.53x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 501 ms: 1.39x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 520 ms: 1.34x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.53x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 71.7 ms: 1.07x faster                                                        |
| pidigits       | 265 ms                                                       | 254 ms: 1.04x faster                                                         |
| nbody          | 88.0 ms                                                      | 109 ms: 1.24x slower                                                         |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.02 ms: 1.18x faster                                                        |
| regex_compile  | 144 ms                                                       | 136 ms: 1.05x faster                                                         |
| regex_dna      | 239 ms                                                       | 235 ms: 1.02x faster                                                         |
| regex_v8       | 23.6 ms                                                      | 24.3 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle             | 14.8 us                                                      | 14.0 us: 1.06x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                       | 98.0 ms: 1.05x faster                                                        |
| xml_etree_parse      | 144 ms                                                       | 138 ms: 1.04x faster                                                         |
| xml_etree_generate   | 86.1 ms                                                      | 85.2 ms: 1.01x faster                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.22 sec: 1.03x slower                                                       |
| xml_etree_process    | 58.4 ms                                                      | 60.3 ms: 1.03x slower                                                        |
| unpickle_pure_python | 210 us                                                       | 220 us: 1.05x slower                                                         |
| pickle_pure_python   | 318 us                                                       | 337 us: 1.06x slower                                                         |
| pickle_dict          | 32.5 us                                                      | 35.2 us: 1.08x slower                                                        |
| json_loads           | 24.4 us                                                      | 26.4 us: 1.08x slower                                                        |
| unpickle_list        | 4.66 us                                                      | 5.05 us: 1.08x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 11.5 ms: 1.12x slower                                                        |
| pickle_list          | 4.43 us                                                      | 5.12 us: 1.16x slower                                                        |
| pickle               | 10.5 us                                                      | 12.5 us: 1.18x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.05x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 10.5 ms: 1.21x slower                                                        |
| python_startup         | 11.6 ms                                                      | 16.4 ms: 1.41x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 37.4 ms: 1.02x faster                                                        |
| mako            | 10.0 ms                                                      | 10.9 ms: 1.09x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 332 ms: 1.63x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 653 ms: 1.60x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 660 ms: 1.60x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 343 ms: 1.59x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 275 ms: 1.56x faster                                                         |
| async_tree_none            | 452 ms                                                       | 295 ms: 1.53x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 501 ms: 1.39x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 520 ms: 1.34x faster                                                         |
| generators                 | 37.4 ms                                                      | 29.2 ms: 1.28x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 29.1 us: 1.26x faster                                                        |
| deepcopy                   | 368 us                                                       | 294 us: 1.25x faster                                                         |
| comprehensions             | 21.9 us                                                      | 17.7 us: 1.24x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.02 ms: 1.18x faster                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 2.98 us: 1.13x faster                                                        |
| go                         | 150 ms                                                       | 134 ms: 1.11x faster                                                         |
| pathlib                    | 18.9 ms                                                      | 17.1 ms: 1.10x faster                                                        |
| sqlalchemy_declarative     | 159 ms                                                       | 146 ms: 1.09x faster                                                         |
| coroutines                 | 23.0 ms                                                      | 21.2 ms: 1.08x faster                                                        |
| float                      | 76.6 ms                                                      | 71.7 ms: 1.07x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 64.7 ms: 1.07x faster                                                        |
| unpickle                   | 14.8 us                                                      | 14.0 us: 1.06x faster                                                        |
| regex_compile              | 144 ms                                                       | 136 ms: 1.05x faster                                                         |
| sympy_sum                  | 162 ms                                                       | 154 ms: 1.05x faster                                                         |
| raytrace                   | 298 ms                                                       | 284 ms: 1.05x faster                                                         |
| sympy_integrate            | 23.9 ms                                                      | 22.8 ms: 1.05x faster                                                        |
| dulwich_log                | 65.4 ms                                                      | 62.3 ms: 1.05x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 98.0 ms: 1.05x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 138 ms: 1.04x faster                                                         |
| pidigits                   | 265 ms                                                       | 254 ms: 1.04x faster                                                         |
| sqlalchemy_imperative      | 18.7 ms                                                      | 18.1 ms: 1.04x faster                                                        |
| mdp                        | 2.57 sec                                                     | 2.49 sec: 1.03x faster                                                       |
| sympy_str                  | 302 ms                                                       | 293 ms: 1.03x faster                                                         |
| logging_format             | 7.48 us                                                      | 7.27 us: 1.03x faster                                                        |
| spectral_norm              | 91.6 ms                                                      | 89.8 ms: 1.02x faster                                                        |
| django_template            | 38.2 ms                                                      | 37.4 ms: 1.02x faster                                                        |
| unpack_sequence            | 53.2 ns                                                      | 52.2 ns: 1.02x faster                                                        |
| regex_dna                  | 239 ms                                                       | 235 ms: 1.02x faster                                                         |
| logging_silent             | 94.4 ns                                                      | 93.2 ns: 1.01x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 85.2 ms: 1.01x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.65 us: 1.01x faster                                                        |
| asyncio_tcp                | 378 ms                                                       | 375 ms: 1.01x faster                                                         |
| chaos                      | 64.0 ms                                                      | 63.7 ms: 1.00x faster                                                        |
| scimark_sor                | 109 ms                                                       | 109 ms: 1.00x faster                                                         |
| 2to3                       | 285 ms                                                       | 287 ms: 1.01x slower                                                         |
| pprint_safe_repr           | 807 ms                                                       | 817 ms: 1.01x slower                                                         |
| docutils                   | 2.87 sec                                                     | 2.92 sec: 1.02x slower                                                       |
| scimark_lu                 | 98.8 ms                                                      | 101 ms: 1.02x slower                                                         |
| sqlite_synth               | 2.77 us                                                      | 2.83 us: 1.02x slower                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.22 sec: 1.03x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 24.3 ms: 1.03x slower                                                        |
| sympy_expand               | 484 ms                                                       | 499 ms: 1.03x slower                                                         |
| xml_etree_process          | 58.4 ms                                                      | 60.3 ms: 1.03x slower                                                        |
| pycparser                  | 1.23 sec                                                     | 1.28 sec: 1.04x slower                                                       |
| deltablue                  | 3.24 ms                                                      | 3.36 ms: 1.04x slower                                                        |
| scimark_fft                | 301 ms                                                       | 314 ms: 1.04x slower                                                         |
| unpickle_pure_python       | 210 us                                                       | 220 us: 1.05x slower                                                         |
| crypto_pyaes               | 80.3 ms                                                      | 84.6 ms: 1.05x slower                                                        |
| json                       | 5.12 ms                                                      | 5.40 ms: 1.05x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 337 us: 1.06x slower                                                         |
| nqueens                    | 89.9 ms                                                      | 95.3 ms: 1.06x slower                                                        |
| richards                   | 45.7 ms                                                      | 48.7 ms: 1.06x slower                                                        |
| pyflate                    | 439 ms                                                       | 468 ms: 1.07x slower                                                         |
| richards_super             | 51.3 ms                                                      | 55.2 ms: 1.07x slower                                                        |
| pickle_dict                | 32.5 us                                                      | 35.2 us: 1.08x slower                                                        |
| async_generators           | 390 ms                                                       | 423 ms: 1.08x slower                                                         |
| json_loads                 | 24.4 us                                                      | 26.4 us: 1.08x slower                                                        |
| unpickle_list              | 4.66 us                                                      | 5.05 us: 1.08x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 6.49 ms: 1.09x slower                                                        |
| mako                       | 10.0 ms                                                      | 10.9 ms: 1.09x slower                                                        |
| fannkuch                   | 350 ms                                                       | 384 ms: 1.10x slower                                                         |
| json_dumps                 | 10.2 ms                                                      | 11.5 ms: 1.12x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.78 ms: 1.14x slower                                                        |
| pickle_list                | 4.43 us                                                      | 5.12 us: 1.16x slower                                                        |
| telco                      | 6.96 ms                                                      | 8.10 ms: 1.16x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 178 us: 1.18x slower                                                         |
| pickle                     | 10.5 us                                                      | 12.5 us: 1.18x slower                                                        |
| coverage                   | 66.7 ms                                                      | 80.2 ms: 1.20x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 10.5 ms: 1.21x slower                                                        |
| nbody                      | 88.0 ms                                                      | 109 ms: 1.24x slower                                                         |
| python_startup             | 11.6 ms                                                      | 16.4 ms: 1.41x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.82 ms: 1.77x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 6.62 ms: 1.90x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 957 ms: 200.85x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.05x slower                                                                 |

Benchmark hidden because not significant (5): bench_thread_pool, asyncio_tcp_ssl, pprint_pformat, asyncio_websockets, meteor_contest
Ignored benchmarks (10) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.022x faster

# HPT report

- Reliability score: 84.73% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x