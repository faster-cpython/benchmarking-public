# Results vs. 3.12.0

- fork: PeterYang12
- ref: accelerate_DJBX33A
- machine: linux-x86_64
- commit hash: bf9cfa8
- commit date: 2024-08-24
- overall geometric mean: 1.02x faster
- HPT reliability: 68.43%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240824-pythonperf2-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 282 ms: 1.01x faster                                                           |
| docutils       | 2.87 sec                                                     | 2.96 sec: 1.03x slower                                                         |
| tornado_http   | 121 ms                                                       | 117 ms: 1.04x faster                                                           |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240824-pythonperf2-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 320 ms: 1.41x faster                                                           |
| async_tree_none_tg         | 431 ms                                                       | 309 ms: 1.39x faster                                                           |
| async_tree_memoization_tg  | 540 ms                                                       | 389 ms: 1.39x faster                                                           |
| async_tree_memoization     | 544 ms                                                       | 397 ms: 1.37x faster                                                           |
| async_tree_io_tg           | 1.05 sec                                                     | 784 ms: 1.34x faster                                                           |
| async_tree_io              | 1.04 sec                                                     | 803 ms: 1.30x faster                                                           |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 548 ms: 1.27x faster                                                           |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 571 ms: 1.22x faster                                                           |
| Geometric mean             | (ref)                                                        | 1.34x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240824-pythonperf2-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 254 ms: 1.04x faster                                                           |
| float          | 76.6 ms                                                      | 80.3 ms: 1.05x slower                                                          |
| nbody          | 88.0 ms                                                      | 92.6 ms: 1.05x slower                                                          |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240824-pythonperf2-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 141 ms: 1.02x faster                                                           |
| regex_effbot   | 3.57 ms                                                      | 3.51 ms: 1.02x faster                                                          |
| regex_dna      | 239 ms                                                       | 255 ms: 1.07x slower                                                           |
| regex_v8       | 23.6 ms                                                      | 27.1 ms: 1.14x slower                                                          |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240824-pythonperf2-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 100 ms: 1.03x faster                                                           |
| pickle_pure_python   | 318 us                                                       | 313 us: 1.02x faster                                                           |
| xml_etree_parse      | 144 ms                                                       | 142 ms: 1.01x faster                                                           |
| xml_etree_generate   | 86.1 ms                                                      | 85.8 ms: 1.00x faster                                                          |
| json_loads           | 24.4 us                                                      | 24.9 us: 1.02x slower                                                          |
| xml_etree_process    | 58.4 ms                                                      | 60.2 ms: 1.03x slower                                                          |
| json_dumps           | 10.2 ms                                                      | 10.6 ms: 1.03x slower                                                          |
| unpickle_pure_python | 210 us                                                       | 218 us: 1.04x slower                                                           |
| tomli_loads          | 2.16 sec                                                     | 2.51 sec: 1.16x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240824-pythonperf2-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.04 ms: 1.05x slower                                                          |
| python_startup         | 11.6 ms                                                      | 13.3 ms: 1.15x slower                                                          |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240824-pythonperf2-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 10.3 ms: 1.03x slower                                                          |
| django_template | 38.2 ms                                                      | 40.5 ms: 1.06x slower                                                          |
| Geometric mean  | (ref)                                                        | 1.05x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240824-pythonperf2-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 320 ms: 1.41x faster                                                           |
| async_tree_none_tg         | 431 ms                                                       | 309 ms: 1.39x faster                                                           |
| async_tree_memoization_tg  | 540 ms                                                       | 389 ms: 1.39x faster                                                           |
| async_tree_memoization     | 544 ms                                                       | 397 ms: 1.37x faster                                                           |
| async_tree_io_tg           | 1.05 sec                                                     | 784 ms: 1.34x faster                                                           |
| async_tree_io              | 1.04 sec                                                     | 803 ms: 1.30x faster                                                           |
| generators                 | 37.4 ms                                                      | 29.3 ms: 1.28x faster                                                          |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 548 ms: 1.27x faster                                                           |
| deepcopy                   | 368 us                                                       | 290 us: 1.27x faster                                                           |
| comprehensions             | 21.9 us                                                      | 17.3 us: 1.27x faster                                                          |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 571 ms: 1.22x faster                                                           |
| deepcopy_memo              | 36.8 us                                                      | 30.2 us: 1.22x faster                                                          |
| pathlib                    | 18.9 ms                                                      | 15.8 ms: 1.20x faster                                                          |
| deepcopy_reduce            | 3.37 us                                                      | 2.92 us: 1.15x faster                                                          |
| crypto_pyaes               | 80.3 ms                                                      | 72.4 ms: 1.11x faster                                                          |
| raytrace                   | 298 ms                                                       | 270 ms: 1.10x faster                                                           |
| bench_thread_pool          | 950 us                                                       | 862 us: 1.10x faster                                                           |
| logging_format             | 7.48 us                                                      | 6.92 us: 1.08x faster                                                          |
| async_generators           | 390 ms                                                       | 362 ms: 1.08x faster                                                           |
| logging_simple             | 6.71 us                                                      | 6.24 us: 1.08x faster                                                          |
| coroutines                 | 23.0 ms                                                      | 21.4 ms: 1.07x faster                                                          |
| sympy_sum                  | 162 ms                                                       | 153 ms: 1.06x faster                                                           |
| bench_mp_pool              | 4.76 ms                                                      | 4.48 ms: 1.06x faster                                                          |
| chaos                      | 64.0 ms                                                      | 61.2 ms: 1.05x faster                                                          |
| pidigits                   | 265 ms                                                       | 254 ms: 1.04x faster                                                           |
| sympy_integrate            | 23.9 ms                                                      | 23.0 ms: 1.04x faster                                                          |
| tornado_http               | 121 ms                                                       | 117 ms: 1.04x faster                                                           |
| sympy_str                  | 302 ms                                                       | 292 ms: 1.03x faster                                                           |
| xml_etree_iterparse        | 103 ms                                                       | 100 ms: 1.03x faster                                                           |
| scimark_monte_carlo        | 69.0 ms                                                      | 67.2 ms: 1.03x faster                                                          |
| asyncio_tcp                | 378 ms                                                       | 368 ms: 1.03x faster                                                           |
| scimark_lu                 | 98.8 ms                                                      | 96.5 ms: 1.02x faster                                                          |
| mdp                        | 2.57 sec                                                     | 2.52 sec: 1.02x faster                                                         |
| regex_compile              | 144 ms                                                       | 141 ms: 1.02x faster                                                           |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.12 ms: 1.02x faster                                                          |
| regex_effbot               | 3.57 ms                                                      | 3.51 ms: 1.02x faster                                                          |
| pickle_pure_python         | 318 us                                                       | 313 us: 1.02x faster                                                           |
| 2to3                       | 285 ms                                                       | 282 ms: 1.01x faster                                                           |
| meteor_contest             | 128 ms                                                       | 127 ms: 1.01x faster                                                           |
| xml_etree_parse            | 144 ms                                                       | 142 ms: 1.01x faster                                                           |
| nqueens                    | 89.9 ms                                                      | 88.9 ms: 1.01x faster                                                          |
| scimark_fft                | 301 ms                                                       | 298 ms: 1.01x faster                                                           |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.57 sec: 1.01x faster                                                         |
| xml_etree_generate         | 86.1 ms                                                      | 85.8 ms: 1.00x faster                                                          |
| pprint_pformat             | 1.65 sec                                                     | 1.66 sec: 1.00x slower                                                         |
| pprint_safe_repr           | 807 ms                                                       | 813 ms: 1.01x slower                                                           |
| sqlglot_transpile          | 1.78 ms                                                      | 1.79 ms: 1.01x slower                                                          |
| asyncio_websockets         | 387 ms                                                       | 391 ms: 1.01x slower                                                           |
| sqlglot_optimize           | 57.5 ms                                                      | 58.8 ms: 1.02x slower                                                          |
| json_loads                 | 24.4 us                                                      | 24.9 us: 1.02x slower                                                          |
| docutils                   | 2.87 sec                                                     | 2.96 sec: 1.03x slower                                                         |
| sqlglot_parse              | 1.38 ms                                                      | 1.42 ms: 1.03x slower                                                          |
| xml_etree_process          | 58.4 ms                                                      | 60.2 ms: 1.03x slower                                                          |
| mako                       | 10.0 ms                                                      | 10.3 ms: 1.03x slower                                                          |
| json_dumps                 | 10.2 ms                                                      | 10.6 ms: 1.03x slower                                                          |
| sqlglot_normalize          | 116 ms                                                       | 120 ms: 1.04x slower                                                           |
| unpickle_pure_python       | 210 us                                                       | 218 us: 1.04x slower                                                           |
| spectral_norm              | 91.6 ms                                                      | 95.3 ms: 1.04x slower                                                          |
| deltablue                  | 3.24 ms                                                      | 3.37 ms: 1.04x slower                                                          |
| hexiom                     | 5.96 ms                                                      | 6.22 ms: 1.04x slower                                                          |
| json                       | 5.12 ms                                                      | 5.34 ms: 1.04x slower                                                          |
| fannkuch                   | 350 ms                                                       | 365 ms: 1.04x slower                                                           |
| sympy_expand               | 484 ms                                                       | 505 ms: 1.04x slower                                                           |
| python_startup_no_site     | 8.64 ms                                                      | 9.04 ms: 1.05x slower                                                          |
| logging_silent             | 94.4 ns                                                      | 98.9 ns: 1.05x slower                                                          |
| float                      | 76.6 ms                                                      | 80.3 ms: 1.05x slower                                                          |
| nbody                      | 88.0 ms                                                      | 92.6 ms: 1.05x slower                                                          |
| django_template            | 38.2 ms                                                      | 40.5 ms: 1.06x slower                                                          |
| regex_dna                  | 239 ms                                                       | 255 ms: 1.07x slower                                                           |
| pyflate                    | 439 ms                                                       | 472 ms: 1.08x slower                                                           |
| richards                   | 45.7 ms                                                      | 49.6 ms: 1.08x slower                                                          |
| richards_super             | 51.3 ms                                                      | 55.7 ms: 1.08x slower                                                          |
| scimark_sor                | 109 ms                                                       | 118 ms: 1.08x slower                                                           |
| regex_v8                   | 23.6 ms                                                      | 27.1 ms: 1.14x slower                                                          |
| python_startup             | 11.6 ms                                                      | 13.3 ms: 1.15x slower                                                          |
| typing_runtime_protocols   | 152 us                                                       | 175 us: 1.15x slower                                                           |
| tomli_loads                | 2.16 sec                                                     | 2.51 sec: 1.16x slower                                                         |
| telco                      | 6.96 ms                                                      | 8.19 ms: 1.18x slower                                                          |
| go                         | 150 ms                                                       | 177 ms: 1.18x slower                                                           |
| coverage                   | 66.7 ms                                                      | 79.7 ms: 1.20x slower                                                          |
| create_gc_cycles           | 1.59 ms                                                      | 1.99 ms: 1.25x slower                                                          |
| gc_traversal               | 3.48 ms                                                      | 4.46 ms: 1.28x slower                                                          |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                   |

Benchmark hidden because not significant (1): pycparser
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240824-3.14.0a0-bf9cfa8/bm-20240824-pythonperf2-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 68.43% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x