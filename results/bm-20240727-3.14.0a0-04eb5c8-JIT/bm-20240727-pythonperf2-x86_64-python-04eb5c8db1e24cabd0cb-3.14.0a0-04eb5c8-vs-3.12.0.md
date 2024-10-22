# Results vs. 3.12.0

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: linux-x86_64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.01x faster
- HPT reliability: 77.33%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 308 ms: 1.08x slower                                                        |
| docutils       | 2.87 sec                                                     | 3.15 sec: 1.10x slower                                                      |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 306 ms: 1.41x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 387 ms: 1.40x faster                                                        |
| async_tree_none            | 452 ms                                                       | 323 ms: 1.40x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 789 ms: 1.33x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 413 ms: 1.32x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 544 ms: 1.28x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 826 ms: 1.26x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 568 ms: 1.23x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.33x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 250 ms: 1.06x faster                                                        |
| nbody          | 88.0 ms                                                      | 84.0 ms: 1.05x faster                                                       |
| float          | 76.6 ms                                                      | 74.5 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 134 ms: 1.07x faster                                                        |
| regex_effbot   | 3.57 ms                                                      | 3.60 ms: 1.01x slower                                                       |
| regex_dna      | 239 ms                                                       | 259 ms: 1.08x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 27.1 ms: 1.15x slower                                                       |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 97.8 ms: 1.05x faster                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 82.3 ms: 1.05x faster                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.10 sec: 1.03x faster                                                      |
| xml_etree_parse      | 144 ms                                                       | 141 ms: 1.02x faster                                                        |
| xml_etree_process    | 58.4 ms                                                      | 57.6 ms: 1.01x faster                                                       |
| unpickle_pure_python | 210 us                                                       | 211 us: 1.01x slower                                                        |
| json_loads           | 24.4 us                                                      | 25.5 us: 1.05x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 10.8 ms: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.06 ms: 1.05x slower                                                       |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.07 ms: 1.10x faster                                                       |
| django_template | 38.2 ms                                                      | 41.4 ms: 1.09x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 306 ms: 1.41x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 387 ms: 1.40x faster                                                        |
| async_tree_none            | 452 ms                                                       | 323 ms: 1.40x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 789 ms: 1.33x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 413 ms: 1.32x faster                                                        |
| generators                 | 37.4 ms                                                      | 28.9 ms: 1.30x faster                                                       |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 544 ms: 1.28x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 28.8 us: 1.28x faster                                                       |
| async_tree_io              | 1.04 sec                                                     | 826 ms: 1.26x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 568 ms: 1.23x faster                                                        |
| comprehensions             | 21.9 us                                                      | 18.2 us: 1.21x faster                                                       |
| deepcopy                   | 368 us                                                       | 308 us: 1.20x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 16.2 ms: 1.17x faster                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 69.9 ms: 1.15x faster                                                       |
| spectral_norm              | 91.6 ms                                                      | 81.4 ms: 1.13x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 3.02 us: 1.12x faster                                                       |
| mako                       | 10.0 ms                                                      | 9.07 ms: 1.10x faster                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 64.3 ms: 1.07x faster                                                       |
| regex_compile              | 144 ms                                                       | 134 ms: 1.07x faster                                                        |
| logging_format             | 7.48 us                                                      | 7.03 us: 1.07x faster                                                       |
| pidigits                   | 265 ms                                                       | 250 ms: 1.06x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 21.7 ms: 1.06x faster                                                       |
| logging_simple             | 6.71 us                                                      | 6.35 us: 1.06x faster                                                       |
| bench_thread_pool          | 950 us                                                       | 902 us: 1.05x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 97.8 ms: 1.05x faster                                                       |
| nbody                      | 88.0 ms                                                      | 84.0 ms: 1.05x faster                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 82.3 ms: 1.05x faster                                                       |
| scimark_fft                | 301 ms                                                       | 292 ms: 1.03x faster                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.10 sec: 1.03x faster                                                      |
| float                      | 76.6 ms                                                      | 74.5 ms: 1.03x faster                                                       |
| xml_etree_parse            | 144 ms                                                       | 141 ms: 1.02x faster                                                        |
| pprint_safe_repr           | 807 ms                                                       | 796 ms: 1.01x faster                                                        |
| pyflate                    | 439 ms                                                       | 433 ms: 1.01x faster                                                        |
| xml_etree_process          | 58.4 ms                                                      | 57.6 ms: 1.01x faster                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.16 ms: 1.01x faster                                                       |
| meteor_contest             | 128 ms                                                       | 127 ms: 1.01x faster                                                        |
| async_generators           | 390 ms                                                       | 387 ms: 1.01x faster                                                        |
| asyncio_tcp                | 378 ms                                                       | 376 ms: 1.00x faster                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.00x faster                                                      |
| unpickle_pure_python       | 210 us                                                       | 211 us: 1.01x slower                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.60 ms: 1.01x slower                                                       |
| raytrace                   | 298 ms                                                       | 300 ms: 1.01x slower                                                        |
| asyncio_websockets         | 387 ms                                                       | 391 ms: 1.01x slower                                                        |
| richards_super             | 51.3 ms                                                      | 52.3 ms: 1.02x slower                                                       |
| sympy_sum                  | 162 ms                                                       | 166 ms: 1.02x slower                                                        |
| sympy_str                  | 302 ms                                                       | 310 ms: 1.02x slower                                                        |
| chaos                      | 64.0 ms                                                      | 66.0 ms: 1.03x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.42 ms: 1.03x slower                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 1.84 ms: 1.04x slower                                                       |
| json_loads                 | 24.4 us                                                      | 25.5 us: 1.05x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 9.06 ms: 1.05x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 10.8 ms: 1.06x slower                                                       |
| logging_silent             | 94.4 ns                                                      | 100 ns: 1.06x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 96.1 ms: 1.07x slower                                                       |
| sympy_integrate            | 23.9 ms                                                      | 25.6 ms: 1.07x slower                                                       |
| 2to3                       | 285 ms                                                       | 308 ms: 1.08x slower                                                        |
| sympy_expand               | 484 ms                                                       | 524 ms: 1.08x slower                                                        |
| regex_dna                  | 239 ms                                                       | 259 ms: 1.08x slower                                                        |
| json                       | 5.12 ms                                                      | 5.56 ms: 1.09x slower                                                       |
| django_template            | 38.2 ms                                                      | 41.4 ms: 1.09x slower                                                       |
| docutils                   | 2.87 sec                                                     | 3.15 sec: 1.10x slower                                                      |
| hexiom                     | 5.96 ms                                                      | 6.60 ms: 1.11x slower                                                       |
| go                         | 150 ms                                                       | 166 ms: 1.11x slower                                                        |
| sqlglot_optimize           | 57.5 ms                                                      | 63.8 ms: 1.11x slower                                                       |
| deltablue                  | 3.24 ms                                                      | 3.61 ms: 1.12x slower                                                       |
| sqlglot_normalize          | 116 ms                                                       | 131 ms: 1.14x slower                                                        |
| scimark_lu                 | 98.8 ms                                                      | 113 ms: 1.14x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 27.1 ms: 1.15x slower                                                       |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                       |
| telco                      | 6.96 ms                                                      | 8.02 ms: 1.15x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 1.94 ms: 1.22x slower                                                       |
| coverage                   | 66.7 ms                                                      | 81.9 ms: 1.23x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 188 us: 1.24x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 4.35 ms: 1.25x slower                                                       |
| scimark_sor                | 109 ms                                                       | 142 ms: 1.30x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (9): tornado_http, pprint_pformat, richards, dask, pycparser, fannkuch, mdp, pickle_pure_python, bench_mp_pool
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 77.33% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x