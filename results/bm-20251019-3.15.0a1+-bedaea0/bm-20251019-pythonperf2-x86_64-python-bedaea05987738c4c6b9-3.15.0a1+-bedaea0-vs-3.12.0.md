# Results vs. 3.12.0

- fork: python
- ref: bedaea05987738c4c6b9
- machine: linux-x86_64
- commit hash: bedaea0
- commit date: 2025-10-19
- overall geometric mean: 1.045x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 277 ms: 1.03x faster                                                         |
| docutils       | 2.87 sec                                                     | 2.83 sec: 1.01x faster                                                       |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io              | 1.04 sec                                                     | 614 ms: 1.70x faster                                                         |
| async_tree_none            | 452 ms                                                       | 269 ms: 1.68x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 629 ms: 1.68x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 325 ms: 1.67x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 328 ms: 1.65x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 268 ms: 1.61x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 500 ms: 1.39x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 507 ms: 1.37x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.59x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 68.0 ms: 1.13x faster                                                        |
| pidigits       | 265 ms                                                       | 254 ms: 1.04x faster                                                         |
| nbody          | 88.0 ms                                                      | 96.5 ms: 1.10x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 131 ms: 1.10x faster                                                         |
| regex_dna      | 239 ms                                                       | 218 ms: 1.10x faster                                                         |
| regex_effbot   | 3.57 ms                                                      | 3.41 ms: 1.05x faster                                                        |
| regex_v8       | 23.6 ms                                                      | 23.9 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.16 sec                                                     | 1.97 sec: 1.09x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 96.7 ms: 1.06x faster                                                        |
| unpickle_pure_python | 210 us                                                       | 203 us: 1.03x faster                                                         |
| xml_etree_generate   | 86.1 ms                                                      | 83.6 ms: 1.03x faster                                                        |
| xml_etree_parse      | 144 ms                                                       | 140 ms: 1.03x faster                                                         |
| xml_etree_process    | 58.4 ms                                                      | 57.9 ms: 1.01x faster                                                        |
| json_dumps           | 10.2 ms                                                      | 10.2 ms: 1.01x faster                                                        |
| pickle_pure_python   | 318 us                                                       | 324 us: 1.02x slower                                                         |
| unpickle             | 14.8 us                                                      | 15.1 us: 1.02x slower                                                        |
| unpickle_list        | 4.66 us                                                      | 4.98 us: 1.07x slower                                                        |
| pickle_dict          | 32.5 us                                                      | 35.1 us: 1.08x slower                                                        |
| json_loads           | 24.4 us                                                      | 26.4 us: 1.08x slower                                                        |
| pickle_list          | 4.43 us                                                      | 5.03 us: 1.14x slower                                                        |
| pickle               | 10.5 us                                                      | 12.4 us: 1.17x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.84 ms: 1.02x slower                                                        |
| python_startup         | 11.6 ms                                                      | 15.4 ms: 1.32x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.16x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.1 ms: 1.09x faster                                                        |
| mako            | 10.0 ms                                                      | 10.7 ms: 1.07x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.25 sec: 2.05x faster                                                       |
| async_tree_io              | 1.04 sec                                                     | 614 ms: 1.70x faster                                                         |
| async_tree_none            | 452 ms                                                       | 269 ms: 1.68x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 629 ms: 1.68x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 325 ms: 1.67x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 328 ms: 1.65x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 268 ms: 1.61x faster                                                         |
| deepcopy_memo              | 36.8 us                                                      | 24.8 us: 1.48x faster                                                        |
| deepcopy                   | 368 us                                                       | 257 us: 1.43x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 500 ms: 1.39x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 507 ms: 1.37x faster                                                         |
| comprehensions             | 21.9 us                                                      | 16.0 us: 1.37x faster                                                        |
| generators                 | 37.4 ms                                                      | 28.4 ms: 1.32x faster                                                        |
| go                         | 150 ms                                                       | 116 ms: 1.29x faster                                                         |
| pathlib                    | 18.9 ms                                                      | 15.0 ms: 1.26x faster                                                        |
| unpack_sequence            | 53.2 ns                                                      | 43.2 ns: 1.23x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 58.2 ms: 1.19x faster                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 2.85 us: 1.18x faster                                                        |
| logging_format             | 7.48 us                                                      | 6.37 us: 1.17x faster                                                        |
| logging_simple             | 6.71 us                                                      | 5.74 us: 1.17x faster                                                        |
| float                      | 76.6 ms                                                      | 68.0 ms: 1.13x faster                                                        |
| dulwich_log                | 65.4 ms                                                      | 59.0 ms: 1.11x faster                                                        |
| chaos                      | 64.0 ms                                                      | 57.8 ms: 1.11x faster                                                        |
| regex_compile              | 144 ms                                                       | 131 ms: 1.10x faster                                                         |
| pyflate                    | 439 ms                                                       | 399 ms: 1.10x faster                                                         |
| regex_dna                  | 239 ms                                                       | 218 ms: 1.10x faster                                                         |
| tomli_loads                | 2.16 sec                                                     | 1.97 sec: 1.09x faster                                                       |
| sympy_sum                  | 162 ms                                                       | 148 ms: 1.09x faster                                                         |
| sympy_integrate            | 23.9 ms                                                      | 22.0 ms: 1.09x faster                                                        |
| django_template            | 38.2 ms                                                      | 35.1 ms: 1.09x faster                                                        |
| raytrace                   | 298 ms                                                       | 274 ms: 1.09x faster                                                         |
| scimark_sor                | 109 ms                                                       | 101 ms: 1.08x faster                                                         |
| scimark_fft                | 301 ms                                                       | 281 ms: 1.07x faster                                                         |
| meteor_contest             | 128 ms                                                       | 120 ms: 1.07x faster                                                         |
| pprint_safe_repr           | 807 ms                                                       | 758 ms: 1.07x faster                                                         |
| scimark_lu                 | 98.8 ms                                                      | 92.7 ms: 1.07x faster                                                        |
| sympy_str                  | 302 ms                                                       | 284 ms: 1.07x faster                                                         |
| pprint_pformat             | 1.65 sec                                                     | 1.55 sec: 1.06x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 96.7 ms: 1.06x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 75.9 ms: 1.06x faster                                                        |
| spectral_norm              | 91.6 ms                                                      | 86.9 ms: 1.05x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.41 ms: 1.05x faster                                                        |
| pidigits                   | 265 ms                                                       | 254 ms: 1.04x faster                                                         |
| hexiom                     | 5.96 ms                                                      | 5.72 ms: 1.04x faster                                                        |
| richards                   | 45.7 ms                                                      | 44.1 ms: 1.04x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 22.2 ms: 1.04x faster                                                        |
| unpickle_pure_python       | 210 us                                                       | 203 us: 1.03x faster                                                         |
| bench_thread_pool          | 950 us                                                       | 920 us: 1.03x faster                                                         |
| xml_etree_generate         | 86.1 ms                                                      | 83.6 ms: 1.03x faster                                                        |
| 2to3                       | 285 ms                                                       | 277 ms: 1.03x faster                                                         |
| deltablue                  | 3.24 ms                                                      | 3.14 ms: 1.03x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 140 ms: 1.03x faster                                                         |
| asyncio_tcp                | 378 ms                                                       | 369 ms: 1.03x faster                                                         |
| richards_super             | 51.3 ms                                                      | 50.4 ms: 1.02x faster                                                        |
| logging_silent             | 94.4 ns                                                      | 92.7 ns: 1.02x faster                                                        |
| docutils                   | 2.87 sec                                                     | 2.83 sec: 1.01x faster                                                       |
| pycparser                  | 1.23 sec                                                     | 1.22 sec: 1.01x faster                                                       |
| xml_etree_process          | 58.4 ms                                                      | 57.9 ms: 1.01x faster                                                        |
| json_dumps                 | 10.2 ms                                                      | 10.2 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                                       |
| regex_v8                   | 23.6 ms                                                      | 23.9 ms: 1.01x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 324 us: 1.02x slower                                                         |
| unpickle                   | 14.8 us                                                      | 15.1 us: 1.02x slower                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.84 us: 1.02x slower                                                        |
| fannkuch                   | 350 ms                                                       | 358 ms: 1.02x slower                                                         |
| python_startup_no_site     | 8.64 ms                                                      | 8.84 ms: 1.02x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 94.0 ms: 1.05x slower                                                        |
| asyncio_websockets         | 387 ms                                                       | 410 ms: 1.06x slower                                                         |
| json                       | 5.12 ms                                                      | 5.45 ms: 1.06x slower                                                        |
| mako                       | 10.0 ms                                                      | 10.7 ms: 1.07x slower                                                        |
| unpickle_list              | 4.66 us                                                      | 4.98 us: 1.07x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.51 ms: 1.07x slower                                                        |
| pickle_dict                | 32.5 us                                                      | 35.1 us: 1.08x slower                                                        |
| json_loads                 | 24.4 us                                                      | 26.4 us: 1.08x slower                                                        |
| async_generators           | 390 ms                                                       | 423 ms: 1.09x slower                                                         |
| typing_runtime_protocols   | 152 us                                                       | 166 us: 1.10x slower                                                         |
| nbody                      | 88.0 ms                                                      | 96.5 ms: 1.10x slower                                                        |
| pickle_list                | 4.43 us                                                      | 5.03 us: 1.14x slower                                                        |
| pickle                     | 10.5 us                                                      | 12.4 us: 1.17x slower                                                        |
| coverage                   | 66.7 ms                                                      | 83.2 ms: 1.25x slower                                                        |
| python_startup             | 11.6 ms                                                      | 15.4 ms: 1.32x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.82 ms: 1.78x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 6.52 ms: 1.87x slower                                                        |
| telco                      | 6.96 ms                                                      | 155 ms: 22.23x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 2.36 sec: 495.81x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.03x slower                                                                 |

Benchmark hidden because not significant (1): sympy_expand
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20251019-3.15.0a1+-bedaea0/bm-20251019-pythonperf2-x86_64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.045x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.13x