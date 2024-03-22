# Results vs. 3.12.0

- fork: python
- ref: dcaf33a41d5d220523d7
- machine: linux-x86_64
- commit hash: dcaf33a
- commit date: 2024-03-20
- overall geometric mean: 1.27x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240320-pythonperf2-x86_64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 332 ms: 1.16x slower                                                         |
| docutils       | 2.87 sec                                                     | 4.70 sec: 1.64x slower                                                       |
| tornado_http   | 121 ms                                                       | 128 ms: 1.05x slower                                                         |
| Geometric mean | (ref)                                                        | 1.19x slower                                                                 |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240320-pythonperf2-x86_64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 696 ms                                                       | 3.32 sec: 4.77x slower                                                       |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 3.44 sec: 4.93x slower                                                       |
| async_tree_none            | 452 ms                                                       | 2.74 sec: 6.07x slower                                                       |
| async_tree_memoization     | 544 ms                                                       | 3.44 sec: 6.33x slower                                                       |
| async_tree_memoization_tg  | 540 ms                                                       | 3.53 sec: 6.53x slower                                                       |
| async_tree_none_tg         | 431 ms                                                       | 2.88 sec: 6.68x slower                                                       |
| async_tree_io              | 1.04 sec                                                     | 9.75 sec: 9.35x slower                                                       |
| async_tree_io_tg           | 1.05 sec                                                     | 10.2 sec: 9.69x slower                                                       |
| Geometric mean             | (ref)                                                        | 6.59x slower                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240320-pythonperf2-x86_64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 261 ms: 1.02x faster                                                         |
| nbody          | 88.0 ms                                                      | 94.7 ms: 1.08x slower                                                        |
| float          | 76.6 ms                                                      | 154 ms: 2.00x slower                                                         |
| Geometric mean | (ref)                                                        | 1.29x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240320-pythonperf2-x86_64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 239 ms                                                       | 241 ms: 1.01x slower                                                         |
| regex_compile  | 144 ms                                                       | 146 ms: 1.01x slower                                                         |
| regex_v8       | 23.6 ms                                                      | 25.9 ms: 1.09x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                 |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240320-pythonperf2-x86_64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.16 sec                                                     | 2.15 sec: 1.00x faster                                                       |
| unpickle_list        | 4.66 us                                                      | 4.64 us: 1.00x faster                                                        |
| pickle_dict          | 32.5 us                                                      | 33.0 us: 1.01x slower                                                        |
| json_loads           | 24.4 us                                                      | 24.8 us: 1.02x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 10.5 ms: 1.03x slower                                                        |
| unpickle             | 14.8 us                                                      | 15.4 us: 1.04x slower                                                        |
| unpickle_pure_python | 210 us                                                       | 229 us: 1.09x slower                                                         |
| xml_etree_generate   | 86.1 ms                                                      | 98.9 ms: 1.15x slower                                                        |
| xml_etree_process    | 58.4 ms                                                      | 68.1 ms: 1.17x slower                                                        |
| xml_etree_parse      | 144 ms                                                       | 209 ms: 1.45x slower                                                         |
| xml_etree_iterparse  | 103 ms                                                       | 168 ms: 1.64x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.10x slower                                                                 |

Benchmark hidden because not significant (3): pickle, pickle_pure_python, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240320-pythonperf2-x86_64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.6 ms                                                      | 14.5 ms: 1.25x slower                                                        |
| python_startup_no_site | 8.64 ms                                                      | 12.6 ms: 1.46x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.35x slower                                                                 |

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240320-pythonperf2-x86_64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols   | 152 us                                                       | 115 us: 1.32x faster                                                         |
| comprehensions             | 21.9 us                                                      | 19.1 us: 1.15x faster                                                        |
| generators                 | 37.4 ms                                                      | 33.3 ms: 1.12x faster                                                        |
| logging_format             | 7.48 us                                                      | 7.16 us: 1.04x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 77.8 ms: 1.03x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.52 us: 1.03x faster                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.71 us: 1.03x faster                                                        |
| sympy_sum                  | 162 ms                                                       | 159 ms: 1.02x faster                                                         |
| asyncio_tcp                | 378 ms                                                       | 371 ms: 1.02x faster                                                         |
| pidigits                   | 265 ms                                                       | 261 ms: 1.02x faster                                                         |
| coroutines                 | 23.0 ms                                                      | 22.8 ms: 1.01x faster                                                        |
| sympy_str                  | 302 ms                                                       | 300 ms: 1.01x faster                                                         |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.15 sec: 1.00x faster                                                       |
| unpickle_list              | 4.66 us                                                      | 4.64 us: 1.00x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 36.9 us: 1.00x slower                                                        |
| regex_dna                  | 239 ms                                                       | 241 ms: 1.01x slower                                                         |
| pickle_dict                | 32.5 us                                                      | 33.0 us: 1.01x slower                                                        |
| regex_compile              | 144 ms                                                       | 146 ms: 1.01x slower                                                         |
| pathlib                    | 18.9 ms                                                      | 19.2 ms: 1.02x slower                                                        |
| sympy_integrate            | 23.9 ms                                                      | 24.3 ms: 1.02x slower                                                        |
| json_loads                 | 24.4 us                                                      | 24.8 us: 1.02x slower                                                        |
| spectral_norm              | 91.6 ms                                                      | 93.8 ms: 1.02x slower                                                        |
| meteor_contest             | 128 ms                                                       | 131 ms: 1.03x slower                                                         |
| pprint_pformat             | 1.65 sec                                                     | 1.70 sec: 1.03x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 10.5 ms: 1.03x slower                                                        |
| pprint_safe_repr           | 807 ms                                                       | 830 ms: 1.03x slower                                                         |
| deepcopy                   | 368 us                                                       | 379 us: 1.03x slower                                                         |
| sqlglot_normalize          | 116 ms                                                       | 119 ms: 1.03x slower                                                         |
| logging_silent             | 94.4 ns                                                      | 97.7 ns: 1.03x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.37 ms: 1.04x slower                                                        |
| unpickle                   | 14.8 us                                                      | 15.4 us: 1.04x slower                                                        |
| raytrace                   | 298 ms                                                       | 310 ms: 1.04x slower                                                         |
| chaos                      | 64.0 ms                                                      | 66.7 ms: 1.04x slower                                                        |
| mdp                        | 2.57 sec                                                     | 2.68 sec: 1.04x slower                                                       |
| json                       | 5.12 ms                                                      | 5.36 ms: 1.05x slower                                                        |
| tornado_http               | 121 ms                                                       | 128 ms: 1.05x slower                                                         |
| dulwich_log                | 65.4 ms                                                      | 68.9 ms: 1.05x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 1.68 ms: 1.05x slower                                                        |
| sympy_expand               | 484 ms                                                       | 511 ms: 1.06x slower                                                         |
| scimark_fft                | 301 ms                                                       | 322 ms: 1.07x slower                                                         |
| nbody                      | 88.0 ms                                                      | 94.7 ms: 1.08x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 229 us: 1.09x slower                                                         |
| regex_v8                   | 23.6 ms                                                      | 25.9 ms: 1.09x slower                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 76.6 ms: 1.11x slower                                                        |
| richards_super             | 51.3 ms                                                      | 57.3 ms: 1.12x slower                                                        |
| gunicorn                   | 1.00 ms                                                      | 1.12 ms: 1.12x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 100 ms: 1.12x slower                                                         |
| sqlglot_optimize           | 57.5 ms                                                      | 64.5 ms: 1.12x slower                                                        |
| richards                   | 45.7 ms                                                      | 51.5 ms: 1.13x slower                                                        |
| aiohttp                    | 1.02 ms                                                      | 1.15 ms: 1.13x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.55 ms: 1.13x slower                                                        |
| fannkuch                   | 350 ms                                                       | 396 ms: 1.13x slower                                                         |
| sqlglot_transpile          | 1.78 ms                                                      | 2.02 ms: 1.14x slower                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 98.9 ms: 1.15x slower                                                        |
| telco                      | 6.96 ms                                                      | 8.07 ms: 1.16x slower                                                        |
| 2to3                       | 285 ms                                                       | 332 ms: 1.16x slower                                                         |
| xml_etree_process          | 58.4 ms                                                      | 68.1 ms: 1.17x slower                                                        |
| scimark_lu                 | 98.8 ms                                                      | 115 ms: 1.17x slower                                                         |
| pyflate                    | 439 ms                                                       | 513 ms: 1.17x slower                                                         |
| go                         | 150 ms                                                       | 175 ms: 1.17x slower                                                         |
| hexiom                     | 5.96 ms                                                      | 7.21 ms: 1.21x slower                                                        |
| coverage                   | 66.7 ms                                                      | 81.0 ms: 1.21x slower                                                        |
| async_generators           | 390 ms                                                       | 474 ms: 1.22x slower                                                         |
| deltablue                  | 3.24 ms                                                      | 4.02 ms: 1.24x slower                                                        |
| python_startup             | 11.6 ms                                                      | 14.5 ms: 1.25x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 4.47 ms: 1.28x slower                                                        |
| pycparser                  | 1.23 sec                                                     | 1.60 sec: 1.30x slower                                                       |
| unpack_sequence            | 53.2 ns                                                      | 74.0 ns: 1.39x slower                                                        |
| scimark_sor                | 109 ms                                                       | 153 ms: 1.40x slower                                                         |
| xml_etree_parse            | 144 ms                                                       | 209 ms: 1.45x slower                                                         |
| python_startup_no_site     | 8.64 ms                                                      | 12.6 ms: 1.46x slower                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 168 ms: 1.64x slower                                                         |
| docutils                   | 2.87 sec                                                     | 4.70 sec: 1.64x slower                                                       |
| dask                       | 392 ms                                                       | 711 ms: 1.81x slower                                                         |
| float                      | 76.6 ms                                                      | 154 ms: 2.00x slower                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 3.32 sec: 4.77x slower                                                       |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 3.44 sec: 4.93x slower                                                       |
| async_tree_none            | 452 ms                                                       | 2.74 sec: 6.07x slower                                                       |
| async_tree_memoization     | 544 ms                                                       | 3.44 sec: 6.33x slower                                                       |
| async_tree_memoization_tg  | 540 ms                                                       | 3.53 sec: 6.53x slower                                                       |
| async_tree_none_tg         | 431 ms                                                       | 2.88 sec: 6.68x slower                                                       |
| async_tree_io              | 1.04 sec                                                     | 9.75 sec: 9.35x slower                                                       |
| async_tree_io_tg           | 1.05 sec                                                     | 10.2 sec: 9.69x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.27x slower                                                                 |

Benchmark hidden because not significant (12): bench_thread_pool, django_template, chameleon, mako, regex_effbot, bench_mp_pool, asyncio_websockets, pickle, pickle_pure_python, pickle_list, deepcopy_reduce, mypy2
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240320-3.13.0a5+-dcaf33a-JIT/bm-20240320-pythonperf2-x86_64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a.json: genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x


# Memory

- memory change: 1.01x