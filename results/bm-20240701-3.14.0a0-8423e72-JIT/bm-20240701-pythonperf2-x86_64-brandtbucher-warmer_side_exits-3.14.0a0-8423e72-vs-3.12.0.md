# Results vs. 3.12.0

- fork: brandtbucher
- ref: warmer_side_exits
- machine: linux-x86_64
- commit hash: 8423e72
- commit date: 2024-07-01
- overall geometric mean: 1.01x faster
- HPT reliability: 65.86%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-pythonperf2-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 309 ms: 1.08x slower                                                           |
| docutils       | 2.87 sec                                                     | 3.14 sec: 1.10x slower                                                         |
| Geometric mean | (ref)                                                        | 1.06x slower                                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-pythonperf2-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 307 ms: 1.40x faster                                                           |
| async_tree_memoization_tg  | 540 ms                                                       | 389 ms: 1.39x faster                                                           |
| async_tree_memoization     | 544 ms                                                       | 410 ms: 1.33x faster                                                           |
| async_tree_io_tg           | 1.05 sec                                                     | 796 ms: 1.32x faster                                                           |
| async_tree_none            | 452 ms                                                       | 343 ms: 1.31x faster                                                           |
| async_tree_io              | 1.04 sec                                                     | 808 ms: 1.29x faster                                                           |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 543 ms: 1.28x faster                                                           |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 584 ms: 1.19x faster                                                           |
| Geometric mean             | (ref)                                                        | 1.31x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-pythonperf2-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 83.1 ms: 1.06x faster                                                          |
| pidigits       | 265 ms                                                       | 250 ms: 1.06x faster                                                           |
| float          | 76.6 ms                                                      | 75.2 ms: 1.02x faster                                                          |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-pythonperf2-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 138 ms: 1.04x faster                                                           |
| regex_effbot   | 3.57 ms                                                      | 3.66 ms: 1.02x slower                                                          |
| regex_v8       | 23.6 ms                                                      | 25.5 ms: 1.08x slower                                                          |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                   |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-pythonperf2-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 82.5 ms: 1.04x faster                                                          |
| xml_etree_iterparse  | 103 ms                                                       | 98.9 ms: 1.04x faster                                                          |
| unpickle_pure_python | 210 us                                                       | 202 us: 1.03x faster                                                           |
| tomli_loads          | 2.16 sec                                                     | 2.10 sec: 1.03x faster                                                         |
| xml_etree_parse      | 144 ms                                                       | 143 ms: 1.01x faster                                                           |
| pickle_pure_python   | 318 us                                                       | 317 us: 1.00x faster                                                           |
| json_loads           | 24.4 us                                                      | 25.2 us: 1.03x slower                                                          |
| json_dumps           | 10.2 ms                                                      | 10.8 ms: 1.05x slower                                                          |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-pythonperf2-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.11 ms: 1.05x slower                                                          |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.16x slower                                                          |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-pythonperf2-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 8.97 ms: 1.12x faster                                                          |
| django_template | 38.2 ms                                                      | 42.2 ms: 1.11x slower                                                          |
| Geometric mean  | (ref)                                                        | 1.00x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240701-pythonperf2-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 307 ms: 1.40x faster                                                           |
| async_tree_memoization_tg  | 540 ms                                                       | 389 ms: 1.39x faster                                                           |
| async_tree_memoization     | 544 ms                                                       | 410 ms: 1.33x faster                                                           |
| async_tree_io_tg           | 1.05 sec                                                     | 796 ms: 1.32x faster                                                           |
| async_tree_none            | 452 ms                                                       | 343 ms: 1.31x faster                                                           |
| async_tree_io              | 1.04 sec                                                     | 808 ms: 1.29x faster                                                           |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 543 ms: 1.28x faster                                                           |
| deepcopy_memo              | 36.8 us                                                      | 29.1 us: 1.26x faster                                                          |
| deepcopy                   | 368 us                                                       | 307 us: 1.20x faster                                                           |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 584 ms: 1.19x faster                                                           |
| comprehensions             | 21.9 us                                                      | 18.5 us: 1.19x faster                                                          |
| pathlib                    | 18.9 ms                                                      | 16.1 ms: 1.17x faster                                                          |
| crypto_pyaes               | 80.3 ms                                                      | 71.2 ms: 1.13x faster                                                          |
| mako                       | 10.0 ms                                                      | 8.97 ms: 1.12x faster                                                          |
| deepcopy_reduce            | 3.37 us                                                      | 3.06 us: 1.10x faster                                                          |
| spectral_norm              | 91.6 ms                                                      | 83.2 ms: 1.10x faster                                                          |
| coroutines                 | 23.0 ms                                                      | 21.2 ms: 1.09x faster                                                          |
| generators                 | 37.4 ms                                                      | 35.2 ms: 1.06x faster                                                          |
| nbody                      | 88.0 ms                                                      | 83.1 ms: 1.06x faster                                                          |
| pidigits                   | 265 ms                                                       | 250 ms: 1.06x faster                                                           |
| logging_format             | 7.48 us                                                      | 7.11 us: 1.05x faster                                                          |
| logging_simple             | 6.71 us                                                      | 6.40 us: 1.05x faster                                                          |
| scimark_monte_carlo        | 69.0 ms                                                      | 65.9 ms: 1.05x faster                                                          |
| xml_etree_generate         | 86.1 ms                                                      | 82.5 ms: 1.04x faster                                                          |
| regex_compile              | 144 ms                                                       | 138 ms: 1.04x faster                                                           |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.05 ms: 1.04x faster                                                          |
| xml_etree_iterparse        | 103 ms                                                       | 98.9 ms: 1.04x faster                                                          |
| unpickle_pure_python       | 210 us                                                       | 202 us: 1.03x faster                                                           |
| tomli_loads                | 2.16 sec                                                     | 2.10 sec: 1.03x faster                                                         |
| scimark_fft                | 301 ms                                                       | 293 ms: 1.03x faster                                                           |
| bench_thread_pool          | 950 us                                                       | 926 us: 1.03x faster                                                           |
| float                      | 76.6 ms                                                      | 75.2 ms: 1.02x faster                                                          |
| mdp                        | 2.57 sec                                                     | 2.54 sec: 1.01x faster                                                         |
| async_generators           | 390 ms                                                       | 385 ms: 1.01x faster                                                           |
| pprint_safe_repr           | 807 ms                                                       | 797 ms: 1.01x faster                                                           |
| xml_etree_parse            | 144 ms                                                       | 143 ms: 1.01x faster                                                           |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                                         |
| pickle_pure_python         | 318 us                                                       | 317 us: 1.00x faster                                                           |
| asyncio_tcp                | 378 ms                                                       | 380 ms: 1.00x slower                                                           |
| fannkuch                   | 350 ms                                                       | 352 ms: 1.01x slower                                                           |
| raytrace                   | 298 ms                                                       | 300 ms: 1.01x slower                                                           |
| pyflate                    | 439 ms                                                       | 443 ms: 1.01x slower                                                           |
| dulwich_log                | 65.4 ms                                                      | 66.4 ms: 1.02x slower                                                          |
| dask                       | 392 ms                                                       | 399 ms: 1.02x slower                                                           |
| meteor_contest             | 128 ms                                                       | 131 ms: 1.02x slower                                                           |
| regex_effbot               | 3.57 ms                                                      | 3.66 ms: 1.02x slower                                                          |
| sqlglot_transpile          | 1.78 ms                                                      | 1.82 ms: 1.03x slower                                                          |
| sympy_str                  | 302 ms                                                       | 311 ms: 1.03x slower                                                           |
| sympy_sum                  | 162 ms                                                       | 167 ms: 1.03x slower                                                           |
| sqlglot_parse              | 1.38 ms                                                      | 1.42 ms: 1.03x slower                                                          |
| json_loads                 | 24.4 us                                                      | 25.2 us: 1.03x slower                                                          |
| richards_super             | 51.3 ms                                                      | 53.1 ms: 1.03x slower                                                          |
| asyncio_websockets         | 387 ms                                                       | 401 ms: 1.04x slower                                                           |
| pycparser                  | 1.23 sec                                                     | 1.29 sec: 1.04x slower                                                         |
| chaos                      | 64.0 ms                                                      | 67.0 ms: 1.05x slower                                                          |
| json_dumps                 | 10.2 ms                                                      | 10.8 ms: 1.05x slower                                                          |
| python_startup_no_site     | 8.64 ms                                                      | 9.11 ms: 1.05x slower                                                          |
| nqueens                    | 89.9 ms                                                      | 95.5 ms: 1.06x slower                                                          |
| json                       | 5.12 ms                                                      | 5.47 ms: 1.07x slower                                                          |
| logging_silent             | 94.4 ns                                                      | 101 ns: 1.07x slower                                                           |
| regex_v8                   | 23.6 ms                                                      | 25.5 ms: 1.08x slower                                                          |
| 2to3                       | 285 ms                                                       | 309 ms: 1.08x slower                                                           |
| sympy_integrate            | 23.9 ms                                                      | 26.0 ms: 1.09x slower                                                          |
| sympy_expand               | 484 ms                                                       | 528 ms: 1.09x slower                                                           |
| docutils                   | 2.87 sec                                                     | 3.14 sec: 1.10x slower                                                         |
| sqlglot_optimize           | 57.5 ms                                                      | 63.1 ms: 1.10x slower                                                          |
| sqlglot_normalize          | 116 ms                                                       | 128 ms: 1.10x slower                                                           |
| go                         | 150 ms                                                       | 165 ms: 1.11x slower                                                           |
| django_template            | 38.2 ms                                                      | 42.2 ms: 1.11x slower                                                          |
| hexiom                     | 5.96 ms                                                      | 6.70 ms: 1.12x slower                                                          |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.16x slower                                                          |
| scimark_lu                 | 98.8 ms                                                      | 115 ms: 1.16x slower                                                           |
| telco                      | 6.96 ms                                                      | 8.10 ms: 1.16x slower                                                          |
| deltablue                  | 3.24 ms                                                      | 3.80 ms: 1.18x slower                                                          |
| scimark_sor                | 109 ms                                                       | 132 ms: 1.21x slower                                                           |
| typing_runtime_protocols   | 152 us                                                       | 184 us: 1.22x slower                                                           |
| create_gc_cycles           | 1.59 ms                                                      | 1.95 ms: 1.23x slower                                                          |
| coverage                   | 66.7 ms                                                      | 82.0 ms: 1.23x slower                                                          |
| gc_traversal               | 3.48 ms                                                      | 4.49 ms: 1.29x slower                                                          |
| Geometric mean             | (ref)                                                        | 1.01x faster                                                                   |

Benchmark hidden because not significant (6): pprint_pformat, tornado_http, xml_etree_process, richards, regex_dna, bench_mp_pool
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240701-3.14.0a0-8423e72-JIT/bm-20240701-pythonperf2-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 65.86% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x