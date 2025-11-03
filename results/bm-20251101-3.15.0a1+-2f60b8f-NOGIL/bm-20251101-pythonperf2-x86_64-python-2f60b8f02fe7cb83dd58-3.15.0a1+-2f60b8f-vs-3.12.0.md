# Results vs. 3.12.0

- fork: python
- ref: 2f60b8f02fe7cb83dd58
- machine: linux-x86_64
- commit hash: 2f60b8f
- commit date: 2025-11-01
- overall geometric mean: 1.048x slower
- HPT reliability: 91.51%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.37x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 310 ms: 1.09x slower                                                         |
| docutils       | 2.87 sec                                                     | 2.84 sec: 1.01x faster                                                       |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 527 ms: 2.00x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 559 ms: 1.86x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 231 ms: 1.86x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 293 ms: 1.85x faster                                                         |
| async_tree_none            | 452 ms                                                       | 262 ms: 1.72x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 319 ms: 1.70x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 467 ms: 1.49x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 498 ms: 1.40x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.72x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 71.4 ms: 1.07x faster                                                        |
| pidigits       | 265 ms                                                       | 253 ms: 1.05x faster                                                         |
| nbody          | 88.0 ms                                                      | 125 ms: 1.42x slower                                                         |
| Geometric mean | (ref)                                                        | 1.08x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.40 ms: 1.05x faster                                                        |
| regex_v8       | 23.6 ms                                                      | 23.3 ms: 1.02x faster                                                        |
| regex_dna      | 239 ms                                                       | 248 ms: 1.04x slower                                                         |
| regex_compile  | 144 ms                                                       | 154 ms: 1.07x slower                                                         |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 88.2 ms: 1.17x faster                                                        |
| xml_etree_parse      | 144 ms                                                       | 137 ms: 1.05x faster                                                         |
| tomli_loads          | 2.16 sec                                                     | 2.14 sec: 1.01x faster                                                       |
| pickle_dict          | 32.5 us                                                      | 35.8 us: 1.10x slower                                                        |
| unpickle             | 14.8 us                                                      | 16.4 us: 1.11x slower                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 97.9 ms: 1.14x slower                                                        |
| json_loads           | 24.4 us                                                      | 27.9 us: 1.15x slower                                                        |
| unpickle_pure_python | 210 us                                                       | 240 us: 1.15x slower                                                         |
| pickle_pure_python   | 318 us                                                       | 366 us: 1.15x slower                                                         |
| pickle_list          | 4.43 us                                                      | 5.11 us: 1.15x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 11.9 ms: 1.17x slower                                                        |
| unpickle_list        | 4.66 us                                                      | 5.46 us: 1.17x slower                                                        |
| pickle               | 10.5 us                                                      | 12.4 us: 1.17x slower                                                        |
| xml_etree_process    | 58.4 ms                                                      | 69.4 ms: 1.19x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.10x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 11.8 ms: 1.36x slower                                                        |
| python_startup         | 11.6 ms                                                      | 19.2 ms: 1.65x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.50x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 43.8 ms: 1.15x slower                                                        |
| mako            | 10.0 ms                                                      | 17.3 ms: 1.73x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.41x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 527 ms: 2.00x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 559 ms: 1.86x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 231 ms: 1.86x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 293 ms: 1.85x faster                                                         |
| mdp                        | 2.57 sec                                                     | 1.43 sec: 1.79x faster                                                       |
| async_tree_none            | 452 ms                                                       | 262 ms: 1.72x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 319 ms: 1.70x faster                                                         |
| gc_traversal               | 3.48 ms                                                      | 2.21 ms: 1.57x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 467 ms: 1.49x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 498 ms: 1.40x faster                                                         |
| generators                 | 37.4 ms                                                      | 29.8 ms: 1.25x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 15.3 ms: 1.24x faster                                                        |
| deepcopy                   | 368 us                                                       | 301 us: 1.22x faster                                                         |
| deepcopy_memo              | 36.8 us                                                      | 30.5 us: 1.21x faster                                                        |
| comprehensions             | 21.9 us                                                      | 18.3 us: 1.20x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 88.2 ms: 1.17x faster                                                        |
| float                      | 76.6 ms                                                      | 71.4 ms: 1.07x faster                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.60 us: 1.07x faster                                                        |
| go                         | 150 ms                                                       | 140 ms: 1.07x faster                                                         |
| dulwich_log                | 65.4 ms                                                      | 61.9 ms: 1.06x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 137 ms: 1.05x faster                                                         |
| regex_effbot               | 3.57 ms                                                      | 3.40 ms: 1.05x faster                                                        |
| pidigits                   | 265 ms                                                       | 253 ms: 1.05x faster                                                         |
| asyncio_websockets         | 387 ms                                                       | 375 ms: 1.03x faster                                                         |
| pycparser                  | 1.23 sec                                                     | 1.21 sec: 1.02x faster                                                       |
| coroutines                 | 23.0 ms                                                      | 22.6 ms: 1.02x faster                                                        |
| regex_v8                   | 23.6 ms                                                      | 23.3 ms: 1.02x faster                                                        |
| docutils                   | 2.87 sec                                                     | 2.84 sec: 1.01x faster                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.14 sec: 1.01x faster                                                       |
| asyncio_tcp                | 378 ms                                                       | 381 ms: 1.01x slower                                                         |
| logging_simple             | 6.71 us                                                      | 6.83 us: 1.02x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 97.0 ns: 1.03x slower                                                        |
| logging_format             | 7.48 us                                                      | 7.75 us: 1.04x slower                                                        |
| unpack_sequence            | 53.2 ns                                                      | 55.1 ns: 1.04x slower                                                        |
| chaos                      | 64.0 ms                                                      | 66.5 ms: 1.04x slower                                                        |
| regex_dna                  | 239 ms                                                       | 248 ms: 1.04x slower                                                         |
| sympy_integrate            | 23.9 ms                                                      | 25.0 ms: 1.04x slower                                                        |
| sympy_sum                  | 162 ms                                                       | 170 ms: 1.05x slower                                                         |
| scimark_fft                | 301 ms                                                       | 322 ms: 1.07x slower                                                         |
| regex_compile              | 144 ms                                                       | 154 ms: 1.07x slower                                                         |
| scimark_sor                | 109 ms                                                       | 117 ms: 1.07x slower                                                         |
| pyflate                    | 439 ms                                                       | 471 ms: 1.07x slower                                                         |
| sympy_str                  | 302 ms                                                       | 325 ms: 1.08x slower                                                         |
| raytrace                   | 298 ms                                                       | 322 ms: 1.08x slower                                                         |
| json                       | 5.12 ms                                                      | 5.53 ms: 1.08x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 6.48 ms: 1.09x slower                                                        |
| 2to3                       | 285 ms                                                       | 310 ms: 1.09x slower                                                         |
| pprint_safe_repr           | 807 ms                                                       | 883 ms: 1.09x slower                                                         |
| pickle_dict                | 32.5 us                                                      | 35.8 us: 1.10x slower                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.83 sec: 1.10x slower                                                       |
| unpickle                   | 14.8 us                                                      | 16.4 us: 1.11x slower                                                        |
| spectral_norm              | 91.6 ms                                                      | 102 ms: 1.11x slower                                                         |
| meteor_contest             | 128 ms                                                       | 143 ms: 1.12x slower                                                         |
| deltablue                  | 3.24 ms                                                      | 3.64 ms: 1.12x slower                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 97.9 ms: 1.14x slower                                                        |
| sympy_expand               | 484 ms                                                       | 552 ms: 1.14x slower                                                         |
| json_loads                 | 24.4 us                                                      | 27.9 us: 1.15x slower                                                        |
| django_template            | 38.2 ms                                                      | 43.8 ms: 1.15x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 240 us: 1.15x slower                                                         |
| pickle_pure_python         | 318 us                                                       | 366 us: 1.15x slower                                                         |
| pickle_list                | 4.43 us                                                      | 5.11 us: 1.15x slower                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 93.5 ms: 1.16x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 11.9 ms: 1.17x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 105 ms: 1.17x slower                                                         |
| unpickle_list              | 4.66 us                                                      | 5.46 us: 1.17x slower                                                        |
| pickle                     | 10.5 us                                                      | 12.4 us: 1.17x slower                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.88 sec: 1.18x slower                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 81.5 ms: 1.18x slower                                                        |
| xml_etree_process          | 58.4 ms                                                      | 69.4 ms: 1.19x slower                                                        |
| scimark_lu                 | 98.8 ms                                                      | 118 ms: 1.19x slower                                                         |
| async_generators           | 390 ms                                                       | 466 ms: 1.19x slower                                                         |
| create_gc_cycles           | 1.59 ms                                                      | 1.92 ms: 1.21x slower                                                        |
| richards                   | 45.7 ms                                                      | 56.4 ms: 1.23x slower                                                        |
| richards_super             | 51.3 ms                                                      | 64.5 ms: 1.26x slower                                                        |
| fannkuch                   | 350 ms                                                       | 445 ms: 1.27x slower                                                         |
| bench_mp_pool              | 4.76 ms                                                      | 6.39 ms: 1.34x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.69 ms: 1.35x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 11.8 ms: 1.36x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 213 us: 1.40x slower                                                         |
| nbody                      | 88.0 ms                                                      | 125 ms: 1.42x slower                                                         |
| bench_thread_pool          | 950 us                                                       | 1.35 ms: 1.43x slower                                                        |
| python_startup             | 11.6 ms                                                      | 19.2 ms: 1.65x slower                                                        |
| mako                       | 10.0 ms                                                      | 17.3 ms: 1.73x slower                                                        |
| coverage                   | 66.7 ms                                                      | 121 ms: 1.81x slower                                                         |
| telco                      | 6.96 ms                                                      | 174 ms: 25.02x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.06x slower                                                                 |

Benchmark hidden because not significant (1): deepcopy_reduce
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20251101-3.15.0a1+-2f60b8f-NOGIL/bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.048x slower

# HPT report

- Reliability score: 91.51% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.37x