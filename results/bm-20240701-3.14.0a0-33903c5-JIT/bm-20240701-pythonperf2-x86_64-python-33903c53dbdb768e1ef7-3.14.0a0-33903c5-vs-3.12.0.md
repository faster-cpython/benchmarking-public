# Results vs. 3.12.0

- fork: python
- ref: 33903c53dbdb768e1ef7
- machine: linux-x86_64
- commit hash: 33903c5
- commit date: 2024-07-01
- overall geometric mean: 1.01x faster
- HPT reliability: 50.18%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-pythonperf2-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 305 ms: 1.07x slower                                                        |
| docutils       | 2.87 sec                                                     | 3.12 sec: 1.09x slower                                                      |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-pythonperf2-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 304 ms: 1.42x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 385 ms: 1.40x faster                                                        |
| async_tree_none            | 452 ms                                                       | 338 ms: 1.34x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 409 ms: 1.33x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 799 ms: 1.32x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 541 ms: 1.29x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 813 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 582 ms: 1.20x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.32x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-pythonperf2-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 250 ms: 1.06x faster                                                        |
| nbody          | 88.0 ms                                                      | 85.2 ms: 1.03x faster                                                       |
| float          | 76.6 ms                                                      | 75.0 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-pythonperf2-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 137 ms: 1.05x faster                                                        |
| regex_effbot   | 3.57 ms                                                      | 3.74 ms: 1.05x slower                                                       |
| regex_dna      | 239 ms                                                       | 264 ms: 1.11x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 27.0 ms: 1.14x slower                                                       |
| Geometric mean | (ref)                                                        | 1.06x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-pythonperf2-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 82.1 ms: 1.05x faster                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.09 sec: 1.03x faster                                                      |
| xml_etree_iterparse  | 103 ms                                                       | 99.4 ms: 1.03x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 141 ms: 1.02x faster                                                        |
| pickle_pure_python   | 318 us                                                       | 317 us: 1.01x faster                                                        |
| json_loads           | 24.4 us                                                      | 25.0 us: 1.03x slower                                                       |
| unpickle_pure_python | 210 us                                                       | 216 us: 1.03x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 10.9 ms: 1.07x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.00x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-pythonperf2-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.08 ms: 1.05x slower                                                       |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-pythonperf2-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.26 ms: 1.08x faster                                                       |
| django_template | 38.2 ms                                                      | 41.3 ms: 1.08x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.00x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-pythonperf2-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 304 ms: 1.42x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 385 ms: 1.40x faster                                                        |
| async_tree_none            | 452 ms                                                       | 338 ms: 1.34x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 409 ms: 1.33x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 799 ms: 1.32x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 541 ms: 1.29x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 813 ms: 1.28x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 29.5 us: 1.24x faster                                                       |
| deepcopy                   | 368 us                                                       | 306 us: 1.20x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 582 ms: 1.20x faster                                                        |
| comprehensions             | 21.9 us                                                      | 18.5 us: 1.19x faster                                                       |
| pathlib                    | 18.9 ms                                                      | 16.2 ms: 1.17x faster                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 70.7 ms: 1.14x faster                                                       |
| logging_format             | 7.48 us                                                      | 6.84 us: 1.09x faster                                                       |
| logging_simple             | 6.71 us                                                      | 6.13 us: 1.09x faster                                                       |
| generators                 | 37.4 ms                                                      | 34.6 ms: 1.08x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 3.12 us: 1.08x faster                                                       |
| mako                       | 10.0 ms                                                      | 9.26 ms: 1.08x faster                                                       |
| coroutines                 | 23.0 ms                                                      | 21.5 ms: 1.07x faster                                                       |
| pidigits                   | 265 ms                                                       | 250 ms: 1.06x faster                                                        |
| regex_compile              | 144 ms                                                       | 137 ms: 1.05x faster                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.01 ms: 1.05x faster                                                       |
| spectral_norm              | 91.6 ms                                                      | 87.4 ms: 1.05x faster                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 82.1 ms: 1.05x faster                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 66.0 ms: 1.05x faster                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.09 sec: 1.03x faster                                                      |
| xml_etree_iterparse        | 103 ms                                                       | 99.4 ms: 1.03x faster                                                       |
| raytrace                   | 298 ms                                                       | 288 ms: 1.03x faster                                                        |
| nbody                      | 88.0 ms                                                      | 85.2 ms: 1.03x faster                                                       |
| scimark_fft                | 301 ms                                                       | 294 ms: 1.03x faster                                                        |
| float                      | 76.6 ms                                                      | 75.0 ms: 1.02x faster                                                       |
| fannkuch                   | 350 ms                                                       | 343 ms: 1.02x faster                                                        |
| pycparser                  | 1.23 sec                                                     | 1.21 sec: 1.02x faster                                                      |
| xml_etree_parse            | 144 ms                                                       | 141 ms: 1.02x faster                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                                      |
| pickle_pure_python         | 318 us                                                       | 317 us: 1.01x faster                                                        |
| mdp                        | 2.57 sec                                                     | 2.59 sec: 1.01x slower                                                      |
| asyncio_websockets         | 387 ms                                                       | 390 ms: 1.01x slower                                                        |
| dask                       | 392 ms                                                       | 397 ms: 1.01x slower                                                        |
| dulwich_log                | 65.4 ms                                                      | 66.4 ms: 1.02x slower                                                       |
| sympy_sum                  | 162 ms                                                       | 165 ms: 1.02x slower                                                        |
| async_generators           | 390 ms                                                       | 398 ms: 1.02x slower                                                        |
| meteor_contest             | 128 ms                                                       | 131 ms: 1.02x slower                                                        |
| sympy_str                  | 302 ms                                                       | 309 ms: 1.02x slower                                                        |
| json_loads                 | 24.4 us                                                      | 25.0 us: 1.03x slower                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 1.83 ms: 1.03x slower                                                       |
| unpickle_pure_python       | 210 us                                                       | 216 us: 1.03x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.42 ms: 1.03x slower                                                       |
| chaos                      | 64.0 ms                                                      | 66.4 ms: 1.04x slower                                                       |
| richards_super             | 51.3 ms                                                      | 53.7 ms: 1.05x slower                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.74 ms: 1.05x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 9.08 ms: 1.05x slower                                                       |
| json                       | 5.12 ms                                                      | 5.43 ms: 1.06x slower                                                       |
| pyflate                    | 439 ms                                                       | 466 ms: 1.06x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 10.9 ms: 1.07x slower                                                       |
| sympy_integrate            | 23.9 ms                                                      | 25.5 ms: 1.07x slower                                                       |
| nqueens                    | 89.9 ms                                                      | 96.1 ms: 1.07x slower                                                       |
| 2to3                       | 285 ms                                                       | 305 ms: 1.07x slower                                                        |
| sympy_expand               | 484 ms                                                       | 522 ms: 1.08x slower                                                        |
| django_template            | 38.2 ms                                                      | 41.3 ms: 1.08x slower                                                       |
| docutils                   | 2.87 sec                                                     | 3.12 sec: 1.09x slower                                                      |
| go                         | 150 ms                                                       | 163 ms: 1.09x slower                                                        |
| sqlglot_optimize           | 57.5 ms                                                      | 62.7 ms: 1.09x slower                                                       |
| regex_dna                  | 239 ms                                                       | 264 ms: 1.11x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 105 ns: 1.11x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 3.63 ms: 1.12x slower                                                       |
| sqlglot_normalize          | 116 ms                                                       | 130 ms: 1.13x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 6.75 ms: 1.13x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 27.0 ms: 1.14x slower                                                       |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                       |
| scimark_lu                 | 98.8 ms                                                      | 114 ms: 1.16x slower                                                        |
| telco                      | 6.96 ms                                                      | 8.21 ms: 1.18x slower                                                       |
| scimark_sor                | 109 ms                                                       | 129 ms: 1.18x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 1.93 ms: 1.22x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 185 us: 1.22x slower                                                        |
| coverage                   | 66.7 ms                                                      | 83.5 ms: 1.25x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 4.66 ms: 1.34x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (8): bench_thread_pool, tornado_http, bench_mp_pool, pprint_pformat, pprint_safe_repr, xml_etree_process, asyncio_tcp, richards
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240701-3.14.0a0-33903c5-JIT/bm-20240701-pythonperf2-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 50.18% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x