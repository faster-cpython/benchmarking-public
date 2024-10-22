# Results vs. 3.12.0

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: linux-x86_64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.02x faster
- HPT reliability: 51.69%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 2.87 sec                                                     | 2.98 sec: 1.04x slower                                                      |
| tornado_http   | 121 ms                                                       | 117 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 303 ms: 1.42x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 381 ms: 1.42x faster                                                        |
| async_tree_none            | 452 ms                                                       | 333 ms: 1.36x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 778 ms: 1.35x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 402 ms: 1.35x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 537 ms: 1.30x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 813 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 573 ms: 1.22x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.34x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 253 ms: 1.05x faster                                                        |
| nbody          | 88.0 ms                                                      | 86.7 ms: 1.01x faster                                                       |
| float          | 76.6 ms                                                      | 81.0 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 140 ms: 1.03x faster                                                        |
| regex_effbot   | 3.57 ms                                                      | 3.50 ms: 1.02x faster                                                       |
| regex_dna      | 239 ms                                                       | 242 ms: 1.01x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 26.8 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 85.0 ms: 1.01x faster                                                       |
| pickle_pure_python   | 318 us                                                       | 320 us: 1.01x slower                                                        |
| xml_etree_parse      | 144 ms                                                       | 145 ms: 1.01x slower                                                        |
| xml_etree_process    | 58.4 ms                                                      | 59.3 ms: 1.01x slower                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 105 ms: 1.02x slower                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.20 sec: 1.02x slower                                                      |
| unpickle_pure_python | 210 us                                                       | 218 us: 1.04x slower                                                        |
| json_loads           | 24.4 us                                                      | 25.7 us: 1.05x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 10.9 ms: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.05 ms: 1.05x slower                                                       |
| python_startup         | 11.6 ms                                                      | 13.3 ms: 1.15x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 38.7 ms: 1.01x slower                                                       |
| mako            | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 303 ms: 1.42x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 381 ms: 1.42x faster                                                        |
| async_tree_none            | 452 ms                                                       | 333 ms: 1.36x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 778 ms: 1.35x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 402 ms: 1.35x faster                                                        |
| generators                 | 37.4 ms                                                      | 28.8 ms: 1.30x faster                                                       |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 537 ms: 1.30x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 813 ms: 1.28x faster                                                        |
| deepcopy                   | 368 us                                                       | 292 us: 1.26x faster                                                        |
| comprehensions             | 21.9 us                                                      | 17.4 us: 1.26x faster                                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 573 ms: 1.22x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 30.5 us: 1.21x faster                                                       |
| pathlib                    | 18.9 ms                                                      | 16.0 ms: 1.18x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.91 us: 1.16x faster                                                       |
| bench_thread_pool          | 950 us                                                       | 861 us: 1.10x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 73.7 ms: 1.09x faster                                                       |
| raytrace                   | 298 ms                                                       | 274 ms: 1.09x faster                                                        |
| logging_format             | 7.48 us                                                      | 6.87 us: 1.09x faster                                                       |
| coroutines                 | 23.0 ms                                                      | 21.3 ms: 1.08x faster                                                       |
| logging_simple             | 6.71 us                                                      | 6.22 us: 1.08x faster                                                       |
| async_generators           | 390 ms                                                       | 367 ms: 1.06x faster                                                        |
| sympy_sum                  | 162 ms                                                       | 153 ms: 1.06x faster                                                        |
| pidigits                   | 265 ms                                                       | 253 ms: 1.05x faster                                                        |
| sympy_integrate            | 23.9 ms                                                      | 23.1 ms: 1.04x faster                                                       |
| tornado_http               | 121 ms                                                       | 117 ms: 1.04x faster                                                        |
| sympy_str                  | 302 ms                                                       | 292 ms: 1.03x faster                                                        |
| mdp                        | 2.57 sec                                                     | 2.49 sec: 1.03x faster                                                      |
| dask                       | 392 ms                                                       | 380 ms: 1.03x faster                                                        |
| regex_compile              | 144 ms                                                       | 140 ms: 1.03x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.50 ms: 1.02x faster                                                       |
| nqueens                    | 89.9 ms                                                      | 88.1 ms: 1.02x faster                                                       |
| chaos                      | 64.0 ms                                                      | 62.8 ms: 1.02x faster                                                       |
| pycparser                  | 1.23 sec                                                     | 1.22 sec: 1.01x faster                                                      |
| nbody                      | 88.0 ms                                                      | 86.7 ms: 1.01x faster                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 85.0 ms: 1.01x faster                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 1.76 ms: 1.01x faster                                                       |
| asyncio_tcp                | 378 ms                                                       | 374 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.57 sec: 1.01x faster                                                      |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.19 ms: 1.00x faster                                                       |
| pickle_pure_python         | 318 us                                                       | 320 us: 1.01x slower                                                        |
| xml_etree_parse            | 144 ms                                                       | 145 ms: 1.01x slower                                                        |
| asyncio_websockets         | 387 ms                                                       | 390 ms: 1.01x slower                                                        |
| meteor_contest             | 128 ms                                                       | 129 ms: 1.01x slower                                                        |
| scimark_fft                | 301 ms                                                       | 304 ms: 1.01x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.39 ms: 1.01x slower                                                       |
| regex_dna                  | 239 ms                                                       | 242 ms: 1.01x slower                                                        |
| django_template            | 38.2 ms                                                      | 38.7 ms: 1.01x slower                                                       |
| xml_etree_process          | 58.4 ms                                                      | 59.3 ms: 1.01x slower                                                       |
| sqlglot_optimize           | 57.5 ms                                                      | 58.4 ms: 1.02x slower                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 105 ms: 1.02x slower                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.20 sec: 1.02x slower                                                      |
| sqlglot_normalize          | 116 ms                                                       | 118 ms: 1.02x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 96.6 ns: 1.02x slower                                                       |
| fannkuch                   | 350 ms                                                       | 359 ms: 1.03x slower                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.71 sec: 1.03x slower                                                      |
| docutils                   | 2.87 sec                                                     | 2.98 sec: 1.04x slower                                                      |
| sympy_expand               | 484 ms                                                       | 502 ms: 1.04x slower                                                        |
| pprint_safe_repr           | 807 ms                                                       | 838 ms: 1.04x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 218 us: 1.04x slower                                                        |
| mako                       | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 9.05 ms: 1.05x slower                                                       |
| spectral_norm              | 91.6 ms                                                      | 96.2 ms: 1.05x slower                                                       |
| deltablue                  | 3.24 ms                                                      | 3.40 ms: 1.05x slower                                                       |
| go                         | 150 ms                                                       | 158 ms: 1.05x slower                                                        |
| json_loads                 | 24.4 us                                                      | 25.7 us: 1.05x slower                                                       |
| json                       | 5.12 ms                                                      | 5.41 ms: 1.06x slower                                                       |
| float                      | 76.6 ms                                                      | 81.0 ms: 1.06x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 6.34 ms: 1.06x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 10.9 ms: 1.06x slower                                                       |
| pyflate                    | 439 ms                                                       | 479 ms: 1.09x slower                                                        |
| scimark_sor                | 109 ms                                                       | 120 ms: 1.11x slower                                                        |
| richards_super             | 51.3 ms                                                      | 57.2 ms: 1.11x slower                                                       |
| richards                   | 45.7 ms                                                      | 51.4 ms: 1.12x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 26.8 ms: 1.13x slower                                                       |
| python_startup             | 11.6 ms                                                      | 13.3 ms: 1.15x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 175 us: 1.16x slower                                                        |
| telco                      | 6.96 ms                                                      | 8.11 ms: 1.16x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 1.98 ms: 1.24x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 4.35 ms: 1.25x slower                                                       |
| coverage                   | 66.7 ms                                                      | 84.2 ms: 1.26x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (4): bench_mp_pool, scimark_lu, 2to3, scimark_monte_carlo
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 51.69% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x