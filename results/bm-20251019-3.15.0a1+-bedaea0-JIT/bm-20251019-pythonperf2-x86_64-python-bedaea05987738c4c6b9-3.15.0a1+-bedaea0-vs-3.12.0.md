# Results vs. 3.12.0

- fork: python
- ref: bedaea05987738c4c6b9
- machine: linux-x86_64
- commit hash: bedaea0
- commit date: 2025-10-19
- overall geometric mean: 1.038x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 281 ms: 1.01x faster                                                         |
| docutils       | 2.87 sec                                                     | 2.89 sec: 1.01x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io              | 1.04 sec                                                     | 616 ms: 1.69x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 634 ms: 1.66x faster                                                         |
| async_tree_none            | 452 ms                                                       | 274 ms: 1.65x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 331 ms: 1.64x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 331 ms: 1.63x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 272 ms: 1.58x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 500 ms: 1.39x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 510 ms: 1.37x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.57x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 69.5 ms: 1.10x faster                                                        |
| pidigits       | 265 ms                                                       | 255 ms: 1.04x faster                                                         |
| nbody          | 88.0 ms                                                      | 96.9 ms: 1.10x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 133 ms: 1.09x faster                                                         |
| regex_dna      | 239 ms                                                       | 223 ms: 1.07x faster                                                         |
| regex_effbot   | 3.57 ms                                                      | 3.40 ms: 1.05x faster                                                        |
| regex_v8       | 23.6 ms                                                      | 24.0 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.16 sec                                                     | 1.89 sec: 1.14x faster                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 79.4 ms: 1.09x faster                                                        |
| unpickle_pure_python | 210 us                                                       | 194 us: 1.08x faster                                                         |
| xml_etree_process    | 58.4 ms                                                      | 55.3 ms: 1.06x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                       | 98.4 ms: 1.04x faster                                                        |
| xml_etree_parse      | 144 ms                                                       | 140 ms: 1.03x faster                                                         |
| json_dumps           | 10.2 ms                                                      | 10.1 ms: 1.01x faster                                                        |
| unpickle             | 14.8 us                                                      | 14.6 us: 1.01x faster                                                        |
| pickle_pure_python   | 318 us                                                       | 328 us: 1.03x slower                                                         |
| unpickle_list        | 4.66 us                                                      | 4.94 us: 1.06x slower                                                        |
| pickle_dict          | 32.5 us                                                      | 34.8 us: 1.07x slower                                                        |
| json_loads           | 24.4 us                                                      | 26.4 us: 1.09x slower                                                        |
| pickle_list          | 4.43 us                                                      | 4.99 us: 1.13x slower                                                        |
| pickle               | 10.5 us                                                      | 12.8 us: 1.22x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.82 ms: 1.02x slower                                                        |
| python_startup         | 11.6 ms                                                      | 15.4 ms: 1.32x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.16x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 34.6 ms: 1.10x faster                                                        |
| mako            | 10.0 ms                                                      | 9.82 ms: 1.02x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.06x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.29 sec: 1.99x faster                                                       |
| async_tree_io              | 1.04 sec                                                     | 616 ms: 1.69x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 634 ms: 1.66x faster                                                         |
| async_tree_none            | 452 ms                                                       | 274 ms: 1.65x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 331 ms: 1.64x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 331 ms: 1.63x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 272 ms: 1.58x faster                                                         |
| deepcopy_memo              | 36.8 us                                                      | 25.1 us: 1.47x faster                                                        |
| deepcopy                   | 368 us                                                       | 259 us: 1.42x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 500 ms: 1.39x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 510 ms: 1.37x faster                                                         |
| go                         | 150 ms                                                       | 118 ms: 1.26x faster                                                         |
| comprehensions             | 21.9 us                                                      | 17.4 us: 1.26x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 15.3 ms: 1.24x faster                                                        |
| generators                 | 37.4 ms                                                      | 30.6 ms: 1.22x faster                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 2.86 us: 1.18x faster                                                        |
| logging_format             | 7.48 us                                                      | 6.42 us: 1.17x faster                                                        |
| logging_simple             | 6.71 us                                                      | 5.76 us: 1.16x faster                                                        |
| tomli_loads                | 2.16 sec                                                     | 1.89 sec: 1.14x faster                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.48 sec: 1.12x faster                                                       |
| pprint_safe_repr           | 807 ms                                                       | 730 ms: 1.11x faster                                                         |
| scimark_monte_carlo        | 69.0 ms                                                      | 62.4 ms: 1.11x faster                                                        |
| django_template            | 38.2 ms                                                      | 34.6 ms: 1.10x faster                                                        |
| float                      | 76.6 ms                                                      | 69.5 ms: 1.10x faster                                                        |
| pyflate                    | 439 ms                                                       | 400 ms: 1.10x faster                                                         |
| dulwich_log                | 65.4 ms                                                      | 60.0 ms: 1.09x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 79.4 ms: 1.09x faster                                                        |
| regex_compile              | 144 ms                                                       | 133 ms: 1.09x faster                                                         |
| scimark_fft                | 301 ms                                                       | 278 ms: 1.08x faster                                                         |
| chaos                      | 64.0 ms                                                      | 59.2 ms: 1.08x faster                                                        |
| unpickle_pure_python       | 210 us                                                       | 194 us: 1.08x faster                                                         |
| sympy_sum                  | 162 ms                                                       | 150 ms: 1.08x faster                                                         |
| sympy_integrate            | 23.9 ms                                                      | 22.2 ms: 1.08x faster                                                        |
| regex_dna                  | 239 ms                                                       | 223 ms: 1.07x faster                                                         |
| meteor_contest             | 128 ms                                                       | 121 ms: 1.06x faster                                                         |
| raytrace                   | 298 ms                                                       | 281 ms: 1.06x faster                                                         |
| xml_etree_process          | 58.4 ms                                                      | 55.3 ms: 1.06x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 76.1 ms: 1.06x faster                                                        |
| scimark_sor                | 109 ms                                                       | 104 ms: 1.05x faster                                                         |
| regex_effbot               | 3.57 ms                                                      | 3.40 ms: 1.05x faster                                                        |
| spectral_norm              | 91.6 ms                                                      | 87.2 ms: 1.05x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 98.4 ms: 1.04x faster                                                        |
| scimark_lu                 | 98.8 ms                                                      | 94.6 ms: 1.04x faster                                                        |
| sympy_str                  | 302 ms                                                       | 290 ms: 1.04x faster                                                         |
| pidigits                   | 265 ms                                                       | 255 ms: 1.04x faster                                                         |
| xml_etree_parse            | 144 ms                                                       | 140 ms: 1.03x faster                                                         |
| deltablue                  | 3.24 ms                                                      | 3.16 ms: 1.03x faster                                                        |
| bench_thread_pool          | 950 us                                                       | 928 us: 1.02x faster                                                         |
| richards                   | 45.7 ms                                                      | 44.7 ms: 1.02x faster                                                        |
| logging_silent             | 94.4 ns                                                      | 92.3 ns: 1.02x faster                                                        |
| asyncio_tcp                | 378 ms                                                       | 370 ms: 1.02x faster                                                         |
| mako                       | 10.0 ms                                                      | 9.82 ms: 1.02x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 22.6 ms: 1.02x faster                                                        |
| hexiom                     | 5.96 ms                                                      | 5.87 ms: 1.01x faster                                                        |
| 2to3                       | 285 ms                                                       | 281 ms: 1.01x faster                                                         |
| json_dumps                 | 10.2 ms                                                      | 10.1 ms: 1.01x faster                                                        |
| unpickle                   | 14.8 us                                                      | 14.6 us: 1.01x faster                                                        |
| docutils                   | 2.87 sec                                                     | 2.89 sec: 1.01x slower                                                       |
| richards_super             | 51.3 ms                                                      | 51.8 ms: 1.01x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 24.0 ms: 1.01x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 8.82 ms: 1.02x slower                                                        |
| sympy_expand               | 484 ms                                                       | 497 ms: 1.03x slower                                                         |
| nqueens                    | 89.9 ms                                                      | 92.4 ms: 1.03x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 328 us: 1.03x slower                                                         |
| fannkuch                   | 350 ms                                                       | 365 ms: 1.04x slower                                                         |
| asyncio_websockets         | 387 ms                                                       | 409 ms: 1.06x slower                                                         |
| unpickle_list              | 4.66 us                                                      | 4.94 us: 1.06x slower                                                        |
| json                       | 5.12 ms                                                      | 5.44 ms: 1.06x slower                                                        |
| pickle_dict                | 32.5 us                                                      | 34.8 us: 1.07x slower                                                        |
| json_loads                 | 24.4 us                                                      | 26.4 us: 1.09x slower                                                        |
| nbody                      | 88.0 ms                                                      | 96.9 ms: 1.10x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 168 us: 1.10x slower                                                         |
| pickle_list                | 4.43 us                                                      | 4.99 us: 1.13x slower                                                        |
| async_generators           | 390 ms                                                       | 447 ms: 1.15x slower                                                         |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.85 ms: 1.15x slower                                                        |
| coverage                   | 66.7 ms                                                      | 77.8 ms: 1.17x slower                                                        |
| pickle                     | 10.5 us                                                      | 12.8 us: 1.22x slower                                                        |
| python_startup             | 11.6 ms                                                      | 15.4 ms: 1.32x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.85 ms: 1.79x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 6.49 ms: 1.87x slower                                                        |
| telco                      | 6.96 ms                                                      | 157 ms: 22.50x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 2.74 sec: 574.93x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.04x slower                                                                 |

Benchmark hidden because not significant (4): unpack_sequence, pycparser, asyncio_tcp_ssl, sqlite_synth
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20251019-3.15.0a1+-bedaea0-JIT/bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.038x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.14x