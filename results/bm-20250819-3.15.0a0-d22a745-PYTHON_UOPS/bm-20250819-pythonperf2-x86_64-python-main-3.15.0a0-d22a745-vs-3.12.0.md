# Results vs. 3.12.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: d22a745
- commit date: 2025-08-19
- overall geometric mean: 1.108x slower
- HPT reliability: 98.76%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250819-pythonperf2-x86_64-python-main-3.15.0a0-d22a745 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 320 ms: 1.12x slower                                        |
| docutils       | 2.87 sec                                                     | 3.11 sec: 1.08x slower                                      |
| Geometric mean | (ref)                                                        | 1.10x slower                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250819-pythonperf2-x86_64-python-main-3.15.0a0-d22a745 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 653 ms: 1.61x faster                                        |
| async_tree_io              | 1.04 sec                                                     | 656 ms: 1.59x faster                                        |
| async_tree_none            | 452 ms                                                       | 290 ms: 1.55x faster                                        |
| async_tree_memoization     | 544 ms                                                       | 352 ms: 1.54x faster                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 350 ms: 1.54x faster                                        |
| async_tree_none_tg         | 431 ms                                                       | 287 ms: 1.50x faster                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 521 ms: 1.34x faster                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 526 ms: 1.32x faster                                        |
| Geometric mean             | (ref)                                                        | 1.50x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250819-pythonperf2-x86_64-python-main-3.15.0a0-d22a745 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 257 ms: 1.03x faster                                        |
| float          | 76.6 ms                                                      | 94.0 ms: 1.23x slower                                       |
| nbody          | 88.0 ms                                                      | 159 ms: 1.81x slower                                        |
| Geometric mean | (ref)                                                        | 1.29x slower                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250819-pythonperf2-x86_64-python-main-3.15.0a0-d22a745 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_dna      | 239 ms                                                       | 222 ms: 1.08x faster                                        |
| regex_v8       | 23.6 ms                                                      | 24.1 ms: 1.02x slower                                       |
| regex_effbot   | 3.57 ms                                                      | 3.66 ms: 1.02x slower                                       |
| regex_compile  | 144 ms                                                       | 154 ms: 1.07x slower                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250819-pythonperf2-x86_64-python-main-3.15.0a0-d22a745 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 10.2 ms                                                      | 10.1 ms: 1.01x faster                                       |
| xml_etree_parse      | 144 ms                                                       | 148 ms: 1.03x slower                                        |
| xml_etree_iterparse  | 103 ms                                                       | 108 ms: 1.05x slower                                        |
| json_loads           | 24.4 us                                                      | 25.8 us: 1.06x slower                                       |
| xml_etree_generate   | 86.1 ms                                                      | 102 ms: 1.19x slower                                        |
| xml_etree_process    | 58.4 ms                                                      | 71.1 ms: 1.22x slower                                       |
| pickle_pure_python   | 318 us                                                       | 400 us: 1.26x slower                                        |
| tomli_loads          | 2.16 sec                                                     | 2.81 sec: 1.30x slower                                      |
| unpickle_pure_python | 210 us                                                       | 338 us: 1.61x slower                                        |
| Geometric mean       | (ref)                                                        | 1.18x slower                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250819-pythonperf2-x86_64-python-main-3.15.0a0-d22a745 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.84 ms: 1.02x slower                                       |
| python_startup         | 11.6 ms                                                      | 15.4 ms: 1.32x slower                                       |
| Geometric mean         | (ref)                                                        | 1.16x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250819-pythonperf2-x86_64-python-main-3.15.0a0-d22a745 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.0 ms: 1.09x faster                                       |
| mako            | 10.0 ms                                                      | 15.3 ms: 1.53x slower                                       |
| Geometric mean  | (ref)                                                        | 1.18x slower                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250819-pythonperf2-x86_64-python-main-3.15.0a0-d22a745 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.42 sec: 1.81x faster                                      |
| async_tree_io_tg           | 1.05 sec                                                     | 653 ms: 1.61x faster                                        |
| async_tree_io              | 1.04 sec                                                     | 656 ms: 1.59x faster                                        |
| async_tree_none            | 452 ms                                                       | 290 ms: 1.55x faster                                        |
| async_tree_memoization     | 544 ms                                                       | 352 ms: 1.54x faster                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 350 ms: 1.54x faster                                        |
| async_tree_none_tg         | 431 ms                                                       | 287 ms: 1.50x faster                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 521 ms: 1.34x faster                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 526 ms: 1.32x faster                                        |
| deepcopy_memo              | 36.8 us                                                      | 28.0 us: 1.31x faster                                       |
| deepcopy                   | 368 us                                                       | 286 us: 1.29x faster                                        |
| generators                 | 37.4 ms                                                      | 29.2 ms: 1.28x faster                                       |
| pathlib                    | 18.9 ms                                                      | 16.6 ms: 1.14x faster                                       |
| logging_format             | 7.48 us                                                      | 6.58 us: 1.14x faster                                       |
| logging_simple             | 6.71 us                                                      | 5.91 us: 1.13x faster                                       |
| deepcopy_reduce            | 3.37 us                                                      | 3.07 us: 1.10x faster                                       |
| django_template            | 38.2 ms                                                      | 35.0 ms: 1.09x faster                                       |
| regex_dna                  | 239 ms                                                       | 222 ms: 1.08x faster                                        |
| dulwich_log                | 65.4 ms                                                      | 61.5 ms: 1.06x faster                                       |
| scimark_sor                | 109 ms                                                       | 104 ms: 1.04x faster                                        |
| coroutines                 | 23.0 ms                                                      | 22.1 ms: 1.04x faster                                       |
| scimark_lu                 | 98.8 ms                                                      | 95.1 ms: 1.04x faster                                       |
| pidigits                   | 265 ms                                                       | 257 ms: 1.03x faster                                        |
| chaos                      | 64.0 ms                                                      | 62.0 ms: 1.03x faster                                       |
| logging_silent             | 94.4 ns                                                      | 92.0 ns: 1.03x faster                                       |
| json_dumps                 | 10.2 ms                                                      | 10.1 ms: 1.01x faster                                       |
| sympy_integrate            | 23.9 ms                                                      | 23.6 ms: 1.01x faster                                       |
| asyncio_websockets         | 387 ms                                                       | 385 ms: 1.01x faster                                        |
| sympy_sum                  | 162 ms                                                       | 161 ms: 1.01x faster                                        |
| regex_v8                   | 23.6 ms                                                      | 24.1 ms: 1.02x slower                                       |
| python_startup_no_site     | 8.64 ms                                                      | 8.84 ms: 1.02x slower                                       |
| regex_effbot               | 3.57 ms                                                      | 3.66 ms: 1.02x slower                                       |
| xml_etree_parse            | 144 ms                                                       | 148 ms: 1.03x slower                                        |
| sympy_str                  | 302 ms                                                       | 315 ms: 1.04x slower                                        |
| xml_etree_iterparse        | 103 ms                                                       | 108 ms: 1.05x slower                                        |
| json_loads                 | 24.4 us                                                      | 25.8 us: 1.06x slower                                       |
| sqlite_synth               | 2.77 us                                                      | 2.95 us: 1.06x slower                                       |
| json                       | 5.12 ms                                                      | 5.46 ms: 1.07x slower                                       |
| regex_compile              | 144 ms                                                       | 154 ms: 1.07x slower                                        |
| raytrace                   | 298 ms                                                       | 323 ms: 1.08x slower                                        |
| docutils                   | 2.87 sec                                                     | 3.11 sec: 1.08x slower                                      |
| nqueens                    | 89.9 ms                                                      | 99.6 ms: 1.11x slower                                       |
| 2to3                       | 285 ms                                                       | 320 ms: 1.12x slower                                        |
| sympy_expand               | 484 ms                                                       | 553 ms: 1.14x slower                                        |
| async_generators           | 390 ms                                                       | 453 ms: 1.16x slower                                        |
| meteor_contest             | 128 ms                                                       | 149 ms: 1.17x slower                                        |
| richards                   | 45.7 ms                                                      | 53.5 ms: 1.17x slower                                       |
| richards_super             | 51.3 ms                                                      | 60.1 ms: 1.17x slower                                       |
| xml_etree_generate         | 86.1 ms                                                      | 102 ms: 1.19x slower                                        |
| pycparser                  | 1.23 sec                                                     | 1.47 sec: 1.19x slower                                      |
| scimark_monte_carlo        | 69.0 ms                                                      | 82.3 ms: 1.19x slower                                       |
| xml_etree_process          | 58.4 ms                                                      | 71.1 ms: 1.22x slower                                       |
| crypto_pyaes               | 80.3 ms                                                      | 98.4 ms: 1.23x slower                                       |
| float                      | 76.6 ms                                                      | 94.0 ms: 1.23x slower                                       |
| coverage                   | 66.7 ms                                                      | 81.9 ms: 1.23x slower                                       |
| comprehensions             | 21.9 us                                                      | 27.4 us: 1.25x slower                                       |
| pickle_pure_python         | 318 us                                                       | 400 us: 1.26x slower                                        |
| pprint_pformat             | 1.65 sec                                                     | 2.08 sec: 1.26x slower                                      |
| pprint_safe_repr           | 807 ms                                                       | 1.03 sec: 1.27x slower                                      |
| typing_runtime_protocols   | 152 us                                                       | 193 us: 1.27x slower                                        |
| pyflate                    | 439 ms                                                       | 560 ms: 1.28x slower                                        |
| tomli_loads                | 2.16 sec                                                     | 2.81 sec: 1.30x slower                                      |
| python_startup             | 11.6 ms                                                      | 15.4 ms: 1.32x slower                                       |
| go                         | 150 ms                                                       | 202 ms: 1.35x slower                                        |
| scimark_fft                | 301 ms                                                       | 425 ms: 1.41x slower                                        |
| mako                       | 10.0 ms                                                      | 15.3 ms: 1.53x slower                                       |
| fannkuch                   | 350 ms                                                       | 562 ms: 1.61x slower                                        |
| spectral_norm              | 91.6 ms                                                      | 147 ms: 1.61x slower                                        |
| unpickle_pure_python       | 210 us                                                       | 338 us: 1.61x slower                                        |
| hexiom                     | 5.96 ms                                                      | 9.70 ms: 1.63x slower                                       |
| deltablue                  | 3.24 ms                                                      | 5.30 ms: 1.64x slower                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 7.36 ms: 1.75x slower                                       |
| nbody                      | 88.0 ms                                                      | 159 ms: 1.81x slower                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.89 ms: 1.82x slower                                       |
| gc_traversal               | 3.48 ms                                                      | 6.73 ms: 1.93x slower                                       |
| telco                      | 6.96 ms                                                      | 161 ms: 23.09x slower                                       |
| Geometric mean             | (ref)                                                        | 1.12x slower                                                |
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250819-3.15.0a0-d22a745-PYTHON_UOPS/bm-20250819-pythonperf2-x86_64-python-main-3.15.0a0-d22a745.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.108x slower

# HPT report

- Reliability score: 98.76% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.13x