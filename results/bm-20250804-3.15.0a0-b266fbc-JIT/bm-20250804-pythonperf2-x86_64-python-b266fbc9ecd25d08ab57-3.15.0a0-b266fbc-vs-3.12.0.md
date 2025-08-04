# Results vs. 3.12.0

- fork: python
- ref: b266fbc9ecd25d08ab57
- machine: linux-x86_64
- commit hash: b266fbc
- commit date: 2025-08-04
- overall geometric mean: 1.034x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250804-pythonperf2-x86_64-python-b266fbc9ecd25d08ab57-3.15.0a0-b266fbc |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 287 ms: 1.01x slower                                                        |
| docutils       | 2.87 sec                                                     | 2.93 sec: 1.02x slower                                                      |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250804-pythonperf2-x86_64-python-b266fbc9ecd25d08ab57-3.15.0a0-b266fbc |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization     | 544 ms                                                       | 326 ms: 1.67x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 625 ms: 1.67x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 637 ms: 1.65x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 332 ms: 1.63x faster                                                        |
| async_tree_none            | 452 ms                                                       | 280 ms: 1.61x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 270 ms: 1.59x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 501 ms: 1.39x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 507 ms: 1.37x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.57x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250804-pythonperf2-x86_64-python-b266fbc9ecd25d08ab57-3.15.0a0-b266fbc |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 64.2 ms: 1.19x faster                                                       |
| pidigits       | 265 ms                                                       | 255 ms: 1.04x faster                                                        |
| nbody          | 88.0 ms                                                      | 97.9 ms: 1.11x slower                                                       |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250804-pythonperf2-x86_64-python-b266fbc9ecd25d08ab57-3.15.0a0-b266fbc |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 133 ms: 1.08x faster                                                        |
| regex_dna      | 239 ms                                                       | 222 ms: 1.07x faster                                                        |
| regex_v8       | 23.6 ms                                                      | 23.5 ms: 1.01x faster                                                       |
| regex_effbot   | 3.57 ms                                                      | 3.71 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250804-pythonperf2-x86_64-python-b266fbc9ecd25d08ab57-3.15.0a0-b266fbc |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.16 sec                                                     | 1.93 sec: 1.12x faster                                                      |
| xml_etree_generate   | 86.1 ms                                                      | 79.6 ms: 1.08x faster                                                       |
| unpickle_pure_python | 210 us                                                       | 194 us: 1.08x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                       | 98.0 ms: 1.05x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 137 ms: 1.05x faster                                                        |
| xml_etree_process    | 58.4 ms                                                      | 55.8 ms: 1.05x faster                                                       |
| pickle_pure_python   | 318 us                                                       | 334 us: 1.05x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 11.2 ms: 1.09x slower                                                       |
| json_loads           | 24.4 us                                                      | 26.7 us: 1.09x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250804-pythonperf2-x86_64-python-b266fbc9ecd25d08ab57-3.15.0a0-b266fbc |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.83 ms: 1.02x slower                                                       |
| python_startup         | 11.6 ms                                                      | 15.4 ms: 1.33x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.16x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250804-pythonperf2-x86_64-python-b266fbc9ecd25d08ab57-3.15.0a0-b266fbc |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.6 ms: 1.07x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250804-pythonperf2-x86_64-python-b266fbc9ecd25d08ab57-3.15.0a0-b266fbc |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.32 sec: 1.95x faster                                                      |
| async_tree_memoization     | 544 ms                                                       | 326 ms: 1.67x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 625 ms: 1.67x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 637 ms: 1.65x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 332 ms: 1.63x faster                                                        |
| async_tree_none            | 452 ms                                                       | 280 ms: 1.61x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 270 ms: 1.59x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 501 ms: 1.39x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 507 ms: 1.37x faster                                                        |
| deepcopy                   | 368 us                                                       | 275 us: 1.34x faster                                                        |
| richards                   | 45.7 ms                                                      | 34.6 ms: 1.32x faster                                                       |
| deepcopy_memo              | 36.8 us                                                      | 27.9 us: 1.32x faster                                                       |
| richards_super             | 51.3 ms                                                      | 40.7 ms: 1.26x faster                                                       |
| comprehensions             | 21.9 us                                                      | 17.4 us: 1.26x faster                                                       |
| generators                 | 37.4 ms                                                      | 30.4 ms: 1.23x faster                                                       |
| float                      | 76.6 ms                                                      | 64.2 ms: 1.19x faster                                                       |
| go                         | 150 ms                                                       | 127 ms: 1.18x faster                                                        |
| spectral_norm              | 91.6 ms                                                      | 80.4 ms: 1.14x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.97 us: 1.14x faster                                                       |
| logging_format             | 7.48 us                                                      | 6.62 us: 1.13x faster                                                       |
| pathlib                    | 18.9 ms                                                      | 16.7 ms: 1.13x faster                                                       |
| deltablue                  | 3.24 ms                                                      | 2.87 ms: 1.13x faster                                                       |
| logging_simple             | 6.71 us                                                      | 6.00 us: 1.12x faster                                                       |
| tomli_loads                | 2.16 sec                                                     | 1.93 sec: 1.12x faster                                                      |
| pprint_pformat             | 1.65 sec                                                     | 1.49 sec: 1.11x faster                                                      |
| dulwich_log                | 65.4 ms                                                      | 59.1 ms: 1.11x faster                                                       |
| pprint_safe_repr           | 807 ms                                                       | 738 ms: 1.09x faster                                                        |
| regex_compile              | 144 ms                                                       | 133 ms: 1.08x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 79.6 ms: 1.08x faster                                                       |
| unpickle_pure_python       | 210 us                                                       | 194 us: 1.08x faster                                                        |
| pyflate                    | 439 ms                                                       | 407 ms: 1.08x faster                                                        |
| scimark_sor                | 109 ms                                                       | 101 ms: 1.08x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 64.1 ms: 1.08x faster                                                       |
| chaos                      | 64.0 ms                                                      | 59.5 ms: 1.08x faster                                                       |
| regex_dna                  | 239 ms                                                       | 222 ms: 1.07x faster                                                        |
| meteor_contest             | 128 ms                                                       | 119 ms: 1.07x faster                                                        |
| django_template            | 38.2 ms                                                      | 35.6 ms: 1.07x faster                                                       |
| sympy_sum                  | 162 ms                                                       | 152 ms: 1.07x faster                                                        |
| sympy_integrate            | 23.9 ms                                                      | 22.5 ms: 1.06x faster                                                       |
| raytrace                   | 298 ms                                                       | 283 ms: 1.05x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 98.0 ms: 1.05x faster                                                       |
| xml_etree_parse            | 144 ms                                                       | 137 ms: 1.05x faster                                                        |
| xml_etree_process          | 58.4 ms                                                      | 55.8 ms: 1.05x faster                                                       |
| scimark_lu                 | 98.8 ms                                                      | 95.0 ms: 1.04x faster                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 77.4 ms: 1.04x faster                                                       |
| pidigits                   | 265 ms                                                       | 255 ms: 1.04x faster                                                        |
| sympy_str                  | 302 ms                                                       | 292 ms: 1.03x faster                                                        |
| logging_silent             | 94.4 ns                                                      | 91.7 ns: 1.03x faster                                                       |
| coroutines                 | 23.0 ms                                                      | 22.5 ms: 1.02x faster                                                       |
| asyncio_websockets         | 387 ms                                                       | 380 ms: 1.02x faster                                                        |
| regex_v8                   | 23.6 ms                                                      | 23.5 ms: 1.01x faster                                                       |
| 2to3                       | 285 ms                                                       | 287 ms: 1.01x slower                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.81 us: 1.01x slower                                                       |
| pycparser                  | 1.23 sec                                                     | 1.26 sec: 1.02x slower                                                      |
| docutils                   | 2.87 sec                                                     | 2.93 sec: 1.02x slower                                                      |
| python_startup_no_site     | 8.64 ms                                                      | 8.83 ms: 1.02x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 6.16 ms: 1.03x slower                                                       |
| sympy_expand               | 484 ms                                                       | 500 ms: 1.03x slower                                                        |
| fannkuch                   | 350 ms                                                       | 362 ms: 1.04x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 93.3 ms: 1.04x slower                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.71 ms: 1.04x slower                                                       |
| pickle_pure_python         | 318 us                                                       | 334 us: 1.05x slower                                                        |
| json                       | 5.12 ms                                                      | 5.47 ms: 1.07x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 11.2 ms: 1.09x slower                                                       |
| json_loads                 | 24.4 us                                                      | 26.7 us: 1.09x slower                                                       |
| nbody                      | 88.0 ms                                                      | 97.9 ms: 1.11x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 171 us: 1.13x slower                                                        |
| coverage                   | 66.7 ms                                                      | 78.0 ms: 1.17x slower                                                       |
| async_generators           | 390 ms                                                       | 458 ms: 1.17x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.08 ms: 1.21x slower                                                       |
| python_startup             | 11.6 ms                                                      | 15.4 ms: 1.33x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 2.89 ms: 1.82x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 6.47 ms: 1.86x slower                                                       |
| telco                      | 6.96 ms                                                      | 162 ms: 23.29x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (2): scimark_fft, mako
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250804-3.15.0a0-b266fbc-JIT/bm-20250804-pythonperf2-x86_64-python-b266fbc9ecd25d08ab57-3.15.0a0-b266fbc.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.034x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.14x