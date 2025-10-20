# Results vs. 3.12.0

- fork: python
- ref: bedaea05987738c4c6b9
- machine: linux-x86_64
- commit hash: bedaea0
- commit date: 2025-10-19
- overall geometric mean: 1.043x slower
- HPT reliability: 95.03%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.37x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 313 ms: 1.10x slower                                                         |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                 |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 524 ms: 2.01x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 229 ms: 1.88x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 555 ms: 1.88x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 291 ms: 1.86x faster                                                         |
| async_tree_none            | 452 ms                                                       | 261 ms: 1.73x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 318 ms: 1.71x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 462 ms: 1.51x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 491 ms: 1.42x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.74x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 71.5 ms: 1.07x faster                                                        |
| pidigits       | 265 ms                                                       | 251 ms: 1.06x faster                                                         |
| nbody          | 88.0 ms                                                      | 124 ms: 1.41x slower                                                         |
| Geometric mean | (ref)                                                        | 1.08x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 239 ms                                                       | 219 ms: 1.09x faster                                                         |
| regex_effbot   | 3.57 ms                                                      | 3.36 ms: 1.06x faster                                                        |
| regex_v8       | 23.6 ms                                                      | 23.1 ms: 1.02x faster                                                        |
| regex_compile  | 144 ms                                                       | 153 ms: 1.06x slower                                                         |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 88.4 ms: 1.16x faster                                                        |
| xml_etree_parse      | 144 ms                                                       | 139 ms: 1.04x faster                                                         |
| pickle_dict          | 32.5 us                                                      | 34.0 us: 1.05x slower                                                        |
| unpickle             | 14.8 us                                                      | 16.5 us: 1.11x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 11.5 ms: 1.13x slower                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 97.3 ms: 1.13x slower                                                        |
| pickle_pure_python   | 318 us                                                       | 360 us: 1.13x slower                                                         |
| unpickle_pure_python | 210 us                                                       | 237 us: 1.13x slower                                                         |
| pickle_list          | 4.43 us                                                      | 5.08 us: 1.15x slower                                                        |
| pickle               | 10.5 us                                                      | 12.1 us: 1.15x slower                                                        |
| json_loads           | 24.4 us                                                      | 28.0 us: 1.15x slower                                                        |
| xml_etree_process    | 58.4 ms                                                      | 69.3 ms: 1.19x slower                                                        |
| unpickle_list        | 4.66 us                                                      | 5.64 us: 1.21x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.09x slower                                                                 |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 11.7 ms: 1.36x slower                                                        |
| python_startup         | 11.6 ms                                                      | 19.1 ms: 1.65x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.50x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 43.7 ms: 1.15x slower                                                        |
| mako            | 10.0 ms                                                      | 17.3 ms: 1.73x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.41x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 524 ms: 2.01x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 229 ms: 1.88x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 555 ms: 1.88x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 291 ms: 1.86x faster                                                         |
| mdp                        | 2.57 sec                                                     | 1.45 sec: 1.77x faster                                                       |
| async_tree_none            | 452 ms                                                       | 261 ms: 1.73x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 318 ms: 1.71x faster                                                         |
| gc_traversal               | 3.48 ms                                                      | 2.20 ms: 1.58x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 462 ms: 1.51x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 491 ms: 1.42x faster                                                         |
| generators                 | 37.4 ms                                                      | 29.8 ms: 1.26x faster                                                        |
| deepcopy                   | 368 us                                                       | 294 us: 1.25x faster                                                         |
| pathlib                    | 18.9 ms                                                      | 15.4 ms: 1.23x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 30.3 us: 1.22x faster                                                        |
| comprehensions             | 21.9 us                                                      | 18.1 us: 1.21x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 88.4 ms: 1.16x faster                                                        |
| regex_dna                  | 239 ms                                                       | 219 ms: 1.09x faster                                                         |
| sqlite_synth               | 2.77 us                                                      | 2.56 us: 1.08x faster                                                        |
| go                         | 150 ms                                                       | 139 ms: 1.08x faster                                                         |
| float                      | 76.6 ms                                                      | 71.5 ms: 1.07x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.36 ms: 1.06x faster                                                        |
| dulwich_log                | 65.4 ms                                                      | 61.7 ms: 1.06x faster                                                        |
| pidigits                   | 265 ms                                                       | 251 ms: 1.06x faster                                                         |
| asyncio_websockets         | 387 ms                                                       | 370 ms: 1.04x faster                                                         |
| xml_etree_parse            | 144 ms                                                       | 139 ms: 1.04x faster                                                         |
| coroutines                 | 23.0 ms                                                      | 22.4 ms: 1.03x faster                                                        |
| regex_v8                   | 23.6 ms                                                      | 23.1 ms: 1.02x faster                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 3.32 us: 1.02x faster                                                        |
| asyncio_tcp                | 378 ms                                                       | 381 ms: 1.01x slower                                                         |
| unpack_sequence            | 53.2 ns                                                      | 54.2 ns: 1.02x slower                                                        |
| logging_simple             | 6.71 us                                                      | 6.90 us: 1.03x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 97.1 ns: 1.03x slower                                                        |
| logging_format             | 7.48 us                                                      | 7.78 us: 1.04x slower                                                        |
| sympy_sum                  | 162 ms                                                       | 169 ms: 1.04x slower                                                         |
| sympy_integrate            | 23.9 ms                                                      | 24.9 ms: 1.04x slower                                                        |
| chaos                      | 64.0 ms                                                      | 66.7 ms: 1.04x slower                                                        |
| pickle_dict                | 32.5 us                                                      | 34.0 us: 1.05x slower                                                        |
| scimark_fft                | 301 ms                                                       | 317 ms: 1.05x slower                                                         |
| raytrace                   | 298 ms                                                       | 315 ms: 1.06x slower                                                         |
| regex_compile              | 144 ms                                                       | 153 ms: 1.06x slower                                                         |
| sympy_str                  | 302 ms                                                       | 323 ms: 1.07x slower                                                         |
| scimark_sor                | 109 ms                                                       | 117 ms: 1.07x slower                                                         |
| pyflate                    | 439 ms                                                       | 472 ms: 1.08x slower                                                         |
| json                       | 5.12 ms                                                      | 5.52 ms: 1.08x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 6.51 ms: 1.09x slower                                                        |
| 2to3                       | 285 ms                                                       | 313 ms: 1.10x slower                                                         |
| pprint_safe_repr           | 807 ms                                                       | 887 ms: 1.10x slower                                                         |
| spectral_norm              | 91.6 ms                                                      | 101 ms: 1.10x slower                                                         |
| pprint_pformat             | 1.65 sec                                                     | 1.83 sec: 1.11x slower                                                       |
| unpickle                   | 14.8 us                                                      | 16.5 us: 1.11x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 3.61 ms: 1.11x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 11.5 ms: 1.13x slower                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 97.3 ms: 1.13x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 360 us: 1.13x slower                                                         |
| unpickle_pure_python       | 210 us                                                       | 237 us: 1.13x slower                                                         |
| sympy_expand               | 484 ms                                                       | 550 ms: 1.14x slower                                                         |
| meteor_contest             | 128 ms                                                       | 146 ms: 1.14x slower                                                         |
| django_template            | 38.2 ms                                                      | 43.7 ms: 1.15x slower                                                        |
| pickle_list                | 4.43 us                                                      | 5.08 us: 1.15x slower                                                        |
| pickle                     | 10.5 us                                                      | 12.1 us: 1.15x slower                                                        |
| json_loads                 | 24.4 us                                                      | 28.0 us: 1.15x slower                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 93.4 ms: 1.16x slower                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 81.2 ms: 1.18x slower                                                        |
| scimark_lu                 | 98.8 ms                                                      | 116 ms: 1.18x slower                                                         |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.88 sec: 1.19x slower                                                       |
| xml_etree_process          | 58.4 ms                                                      | 69.3 ms: 1.19x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 107 ms: 1.19x slower                                                         |
| unpickle_list              | 4.66 us                                                      | 5.64 us: 1.21x slower                                                        |
| richards                   | 45.7 ms                                                      | 55.4 ms: 1.21x slower                                                        |
| async_generators           | 390 ms                                                       | 474 ms: 1.22x slower                                                         |
| create_gc_cycles           | 1.59 ms                                                      | 1.97 ms: 1.24x slower                                                        |
| richards_super             | 51.3 ms                                                      | 63.8 ms: 1.24x slower                                                        |
| fannkuch                   | 350 ms                                                       | 460 ms: 1.31x slower                                                         |
| bench_mp_pool              | 4.76 ms                                                      | 6.33 ms: 1.33x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 203 us: 1.34x slower                                                         |
| python_startup_no_site     | 8.64 ms                                                      | 11.7 ms: 1.36x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.76 ms: 1.37x slower                                                        |
| nbody                      | 88.0 ms                                                      | 124 ms: 1.41x slower                                                         |
| bench_thread_pool          | 950 us                                                       | 1.34 ms: 1.41x slower                                                        |
| python_startup             | 11.6 ms                                                      | 19.1 ms: 1.65x slower                                                        |
| mako                       | 10.0 ms                                                      | 17.3 ms: 1.73x slower                                                        |
| coverage                   | 66.7 ms                                                      | 119 ms: 1.78x slower                                                         |
| telco                      | 6.96 ms                                                      | 168 ms: 24.16x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.05x slower                                                                 |

Benchmark hidden because not significant (3): docutils, tomli_loads, pycparser
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20251019-3.15.0a1+-bedaea0-NOGIL/bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.043x slower

# HPT report

- Reliability score: 95.03% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.37x