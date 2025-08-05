# Results vs. 3.12.0

- fork: python
- ref: d5fa437dfb50e2e47632
- machine: linux-x86_64
- commit hash: d5fa437
- commit date: 2025-07-26
- overall geometric mean: 1.137x slower
- HPT reliability: 98.95%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf2-x86_64-python-d5fa437dfb50e2e47632-3.15.0a0-d5fa437 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 324 ms: 1.14x slower                                                        |
| docutils       | 2.87 sec                                                     | 3.13 sec: 1.09x slower                                                      |
| Geometric mean | (ref)                                                        | 1.11x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf2-x86_64-python-d5fa437dfb50e2e47632-3.15.0a0-d5fa437 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 668 ms: 1.58x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 664 ms: 1.57x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 351 ms: 1.54x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 360 ms: 1.51x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 288 ms: 1.49x faster                                                        |
| async_tree_none            | 452 ms                                                       | 304 ms: 1.49x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 527 ms: 1.32x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 530 ms: 1.31x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.47x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf2-x86_64-python-d5fa437dfb50e2e47632-3.15.0a0-d5fa437 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 256 ms: 1.04x faster                                                        |
| float          | 76.6 ms                                                      | 105 ms: 1.37x slower                                                        |
| nbody          | 88.0 ms                                                      | 184 ms: 2.09x slower                                                        |
| Geometric mean | (ref)                                                        | 1.40x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf2-x86_64-python-d5fa437dfb50e2e47632-3.15.0a0-d5fa437 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 239 ms                                                       | 222 ms: 1.08x faster                                                        |
| regex_effbot   | 3.57 ms                                                      | 3.44 ms: 1.04x faster                                                       |
| regex_v8       | 23.6 ms                                                      | 24.7 ms: 1.04x slower                                                       |
| regex_compile  | 144 ms                                                       | 159 ms: 1.11x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf2-x86_64-python-d5fa437dfb50e2e47632-3.15.0a0-d5fa437 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 144 ms                                                       | 142 ms: 1.01x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                       | 109 ms: 1.06x slower                                                        |
| json_loads           | 24.4 us                                                      | 26.4 us: 1.09x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 11.1 ms: 1.09x slower                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 107 ms: 1.25x slower                                                        |
| xml_etree_process    | 58.4 ms                                                      | 75.1 ms: 1.29x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 410 us: 1.29x slower                                                        |
| tomli_loads          | 2.16 sec                                                     | 3.11 sec: 1.44x slower                                                      |
| unpickle_pure_python | 210 us                                                       | 387 us: 1.85x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.24x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf2-x86_64-python-d5fa437dfb50e2e47632-3.15.0a0-d5fa437 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.81 ms: 1.02x slower                                                       |
| python_startup         | 11.6 ms                                                      | 15.4 ms: 1.32x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.16x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf2-x86_64-python-d5fa437dfb50e2e47632-3.15.0a0-d5fa437 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.3 ms: 1.08x faster                                                       |
| mako            | 10.0 ms                                                      | 17.1 ms: 1.71x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.26x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf2-x86_64-python-d5fa437dfb50e2e47632-3.15.0a0-d5fa437 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.47 sec: 1.75x faster                                                      |
| async_tree_io_tg           | 1.05 sec                                                     | 668 ms: 1.58x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 664 ms: 1.57x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 351 ms: 1.54x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 360 ms: 1.51x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 288 ms: 1.49x faster                                                        |
| async_tree_none            | 452 ms                                                       | 304 ms: 1.49x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 527 ms: 1.32x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 27.9 us: 1.32x faster                                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 530 ms: 1.31x faster                                                        |
| deepcopy                   | 368 us                                                       | 283 us: 1.30x faster                                                        |
| generators                 | 37.4 ms                                                      | 30.4 ms: 1.23x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.92 us: 1.15x faster                                                       |
| pathlib                    | 18.9 ms                                                      | 16.9 ms: 1.12x faster                                                       |
| logging_format             | 7.48 us                                                      | 6.77 us: 1.11x faster                                                       |
| logging_simple             | 6.71 us                                                      | 6.17 us: 1.09x faster                                                       |
| django_template            | 38.2 ms                                                      | 35.3 ms: 1.08x faster                                                       |
| regex_dna                  | 239 ms                                                       | 222 ms: 1.08x faster                                                        |
| scimark_sor                | 109 ms                                                       | 103 ms: 1.06x faster                                                        |
| dulwich_log                | 65.4 ms                                                      | 61.8 ms: 1.06x faster                                                       |
| scimark_lu                 | 98.8 ms                                                      | 93.9 ms: 1.05x faster                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.44 ms: 1.04x faster                                                       |
| pidigits                   | 265 ms                                                       | 256 ms: 1.04x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 22.2 ms: 1.03x faster                                                       |
| chaos                      | 64.0 ms                                                      | 62.3 ms: 1.03x faster                                                       |
| logging_silent             | 94.4 ns                                                      | 92.3 ns: 1.02x faster                                                       |
| asyncio_websockets         | 387 ms                                                       | 381 ms: 1.02x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 142 ms: 1.01x faster                                                        |
| sympy_integrate            | 23.9 ms                                                      | 23.8 ms: 1.01x faster                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 8.81 ms: 1.02x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 24.7 ms: 1.04x slower                                                       |
| sympy_str                  | 302 ms                                                       | 316 ms: 1.04x slower                                                        |
| json                       | 5.12 ms                                                      | 5.42 ms: 1.06x slower                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 109 ms: 1.06x slower                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.98 us: 1.07x slower                                                       |
| json_loads                 | 24.4 us                                                      | 26.4 us: 1.09x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 11.1 ms: 1.09x slower                                                       |
| raytrace                   | 298 ms                                                       | 325 ms: 1.09x slower                                                        |
| docutils                   | 2.87 sec                                                     | 3.13 sec: 1.09x slower                                                      |
| regex_compile              | 144 ms                                                       | 159 ms: 1.11x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 101 ms: 1.13x slower                                                        |
| sympy_expand               | 484 ms                                                       | 549 ms: 1.13x slower                                                        |
| 2to3                       | 285 ms                                                       | 324 ms: 1.14x slower                                                        |
| async_generators           | 390 ms                                                       | 455 ms: 1.17x slower                                                        |
| richards_super             | 51.3 ms                                                      | 60.2 ms: 1.17x slower                                                       |
| richards                   | 45.7 ms                                                      | 54.0 ms: 1.18x slower                                                       |
| coverage                   | 66.7 ms                                                      | 79.5 ms: 1.19x slower                                                       |
| pycparser                  | 1.23 sec                                                     | 1.49 sec: 1.21x slower                                                      |
| xml_etree_generate         | 86.1 ms                                                      | 107 ms: 1.25x slower                                                        |
| meteor_contest             | 128 ms                                                       | 160 ms: 1.25x slower                                                        |
| xml_etree_process          | 58.4 ms                                                      | 75.1 ms: 1.29x slower                                                       |
| pickle_pure_python         | 318 us                                                       | 410 us: 1.29x slower                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 89.5 ms: 1.30x slower                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 106 ms: 1.32x slower                                                        |
| python_startup             | 11.6 ms                                                      | 15.4 ms: 1.32x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 202 us: 1.33x slower                                                        |
| pprint_pformat             | 1.65 sec                                                     | 2.26 sec: 1.37x slower                                                      |
| float                      | 76.6 ms                                                      | 105 ms: 1.37x slower                                                        |
| comprehensions             | 21.9 us                                                      | 30.3 us: 1.38x slower                                                       |
| pprint_safe_repr           | 807 ms                                                       | 1.12 sec: 1.39x slower                                                      |
| pyflate                    | 439 ms                                                       | 628 ms: 1.43x slower                                                        |
| tomli_loads                | 2.16 sec                                                     | 3.11 sec: 1.44x slower                                                      |
| go                         | 150 ms                                                       | 219 ms: 1.47x slower                                                        |
| scimark_fft                | 301 ms                                                       | 465 ms: 1.55x slower                                                        |
| mako                       | 10.0 ms                                                      | 17.1 ms: 1.71x slower                                                       |
| fannkuch                   | 350 ms                                                       | 618 ms: 1.77x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 10.7 ms: 1.79x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 2.88 ms: 1.81x slower                                                       |
| spectral_norm              | 91.6 ms                                                      | 167 ms: 1.82x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 5.96 ms: 1.84x slower                                                       |
| unpickle_pure_python       | 210 us                                                       | 387 us: 1.85x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 6.48 ms: 1.86x slower                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 8.41 ms: 2.00x slower                                                       |
| nbody                      | 88.0 ms                                                      | 184 ms: 2.09x slower                                                        |
| telco                      | 6.96 ms                                                      | 158 ms: 22.73x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.15x slower                                                                |

Benchmark hidden because not significant (1): sympy_sum
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250726-3.15.0a0-d5fa437-PYTHON_UOPS/bm-20250726-pythonperf2-x86_64-python-d5fa437dfb50e2e47632-3.15.0a0-d5fa437.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.137x slower

# HPT report

- Reliability score: 98.95% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.13x