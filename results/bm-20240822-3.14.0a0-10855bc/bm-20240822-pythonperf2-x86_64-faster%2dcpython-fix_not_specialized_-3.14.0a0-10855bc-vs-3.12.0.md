# Results vs. 3.12.0

- fork: faster-cpython
- ref: fix_not_specialized_
- machine: linux-x86_64
- commit hash: 10855bc
- commit date: 2024-08-22
- overall geometric mean: 1.03x faster
- HPT reliability: 64.17%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240822-pythonperf2-x86_64-faster%2dcpython-fix_not_specialized_-3.14.0a0-10855bc |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 287 ms: 1.01x slower                                                                  |
| docutils       | 2.87 sec                                                     | 2.94 sec: 1.03x slower                                                                |
| tornado_http   | 121 ms                                                       | 117 ms: 1.04x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240822-pythonperf2-x86_64-faster%2dcpython-fix_not_specialized_-3.14.0a0-10855bc |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 318 ms: 1.42x faster                                                                  |
| async_tree_none_tg         | 431 ms                                                       | 307 ms: 1.40x faster                                                                  |
| async_tree_memoization_tg  | 540 ms                                                       | 388 ms: 1.39x faster                                                                  |
| async_tree_memoization     | 544 ms                                                       | 398 ms: 1.37x faster                                                                  |
| async_tree_io_tg           | 1.05 sec                                                     | 781 ms: 1.35x faster                                                                  |
| async_tree_io              | 1.04 sec                                                     | 797 ms: 1.31x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 544 ms: 1.28x faster                                                                  |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 568 ms: 1.22x faster                                                                  |
| Geometric mean             | (ref)                                                        | 1.34x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240822-pythonperf2-x86_64-faster%2dcpython-fix_not_specialized_-3.14.0a0-10855bc |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 253 ms: 1.05x faster                                                                  |
| nbody          | 88.0 ms                                                      | 86.9 ms: 1.01x faster                                                                 |
| float          | 76.6 ms                                                      | 79.3 ms: 1.04x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240822-pythonperf2-x86_64-faster%2dcpython-fix_not_specialized_-3.14.0a0-10855bc |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 138 ms: 1.04x faster                                                                  |
| regex_dna      | 239 ms                                                       | 240 ms: 1.01x slower                                                                  |
| regex_effbot   | 3.57 ms                                                      | 3.62 ms: 1.01x slower                                                                 |
| regex_v8       | 23.6 ms                                                      | 26.1 ms: 1.11x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240822-pythonperf2-x86_64-faster%2dcpython-fix_not_specialized_-3.14.0a0-10855bc |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 84.2 ms: 1.02x faster                                                                 |
| xml_etree_iterparse  | 103 ms                                                       | 101 ms: 1.02x faster                                                                  |
| xml_etree_parse      | 144 ms                                                       | 142 ms: 1.01x faster                                                                  |
| pickle_pure_python   | 318 us                                                       | 321 us: 1.01x slower                                                                  |
| unpickle_pure_python | 210 us                                                       | 212 us: 1.01x slower                                                                  |
| xml_etree_process    | 58.4 ms                                                      | 59.3 ms: 1.01x slower                                                                 |
| json_loads           | 24.4 us                                                      | 24.9 us: 1.02x slower                                                                 |
| json_dumps           | 10.2 ms                                                      | 10.7 ms: 1.04x slower                                                                 |
| tomli_loads          | 2.16 sec                                                     | 2.30 sec: 1.06x slower                                                                |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240822-pythonperf2-x86_64-faster%2dcpython-fix_not_specialized_-3.14.0a0-10855bc |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.04 ms: 1.05x slower                                                                 |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                                 |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240822-pythonperf2-x86_64-faster%2dcpython-fix_not_specialized_-3.14.0a0-10855bc |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                                                 |
| django_template | 38.2 ms                                                      | 39.7 ms: 1.04x slower                                                                 |
| Geometric mean  | (ref)                                                        | 1.04x slower                                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240822-pythonperf2-x86_64-faster%2dcpython-fix_not_specialized_-3.14.0a0-10855bc |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 318 ms: 1.42x faster                                                                  |
| async_tree_none_tg         | 431 ms                                                       | 307 ms: 1.40x faster                                                                  |
| async_tree_memoization_tg  | 540 ms                                                       | 388 ms: 1.39x faster                                                                  |
| async_tree_memoization     | 544 ms                                                       | 398 ms: 1.37x faster                                                                  |
| async_tree_io_tg           | 1.05 sec                                                     | 781 ms: 1.35x faster                                                                  |
| generators                 | 37.4 ms                                                      | 28.4 ms: 1.32x faster                                                                 |
| async_tree_io              | 1.04 sec                                                     | 797 ms: 1.31x faster                                                                  |
| deepcopy                   | 368 us                                                       | 287 us: 1.28x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 544 ms: 1.28x faster                                                                  |
| comprehensions             | 21.9 us                                                      | 17.8 us: 1.23x faster                                                                 |
| deepcopy_memo              | 36.8 us                                                      | 29.9 us: 1.23x faster                                                                 |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 568 ms: 1.22x faster                                                                  |
| pathlib                    | 18.9 ms                                                      | 15.9 ms: 1.18x faster                                                                 |
| deepcopy_reduce            | 3.37 us                                                      | 2.94 us: 1.15x faster                                                                 |
| raytrace                   | 298 ms                                                       | 267 ms: 1.12x faster                                                                  |
| crypto_pyaes               | 80.3 ms                                                      | 72.6 ms: 1.11x faster                                                                 |
| bench_thread_pool          | 950 us                                                       | 862 us: 1.10x faster                                                                  |
| async_generators           | 390 ms                                                       | 362 ms: 1.08x faster                                                                  |
| sympy_sum                  | 162 ms                                                       | 151 ms: 1.08x faster                                                                  |
| logging_format             | 7.48 us                                                      | 7.01 us: 1.07x faster                                                                 |
| coroutines                 | 23.0 ms                                                      | 21.7 ms: 1.06x faster                                                                 |
| logging_simple             | 6.71 us                                                      | 6.34 us: 1.06x faster                                                                 |
| chaos                      | 64.0 ms                                                      | 61.1 ms: 1.05x faster                                                                 |
| pidigits                   | 265 ms                                                       | 253 ms: 1.05x faster                                                                  |
| scimark_monte_carlo        | 69.0 ms                                                      | 66.0 ms: 1.04x faster                                                                 |
| scimark_lu                 | 98.8 ms                                                      | 94.7 ms: 1.04x faster                                                                 |
| sympy_integrate            | 23.9 ms                                                      | 22.9 ms: 1.04x faster                                                                 |
| regex_compile              | 144 ms                                                       | 138 ms: 1.04x faster                                                                  |
| tornado_http               | 121 ms                                                       | 117 ms: 1.04x faster                                                                  |
| sympy_str                  | 302 ms                                                       | 291 ms: 1.04x faster                                                                  |
| asyncio_tcp                | 378 ms                                                       | 368 ms: 1.03x faster                                                                  |
| xml_etree_generate         | 86.1 ms                                                      | 84.2 ms: 1.02x faster                                                                 |
| xml_etree_iterparse        | 103 ms                                                       | 101 ms: 1.02x faster                                                                  |
| nqueens                    | 89.9 ms                                                      | 88.5 ms: 1.02x faster                                                                 |
| mdp                        | 2.57 sec                                                     | 2.53 sec: 1.02x faster                                                                |
| xml_etree_parse            | 144 ms                                                       | 142 ms: 1.01x faster                                                                  |
| nbody                      | 88.0 ms                                                      | 86.9 ms: 1.01x faster                                                                 |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.18 ms: 1.01x faster                                                                 |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                                                |
| meteor_contest             | 128 ms                                                       | 128 ms: 1.00x faster                                                                  |
| 2to3                       | 285 ms                                                       | 287 ms: 1.01x slower                                                                  |
| regex_dna                  | 239 ms                                                       | 240 ms: 1.01x slower                                                                  |
| pickle_pure_python         | 318 us                                                       | 321 us: 1.01x slower                                                                  |
| asyncio_websockets         | 387 ms                                                       | 391 ms: 1.01x slower                                                                  |
| unpickle_pure_python       | 210 us                                                       | 212 us: 1.01x slower                                                                  |
| scimark_fft                | 301 ms                                                       | 305 ms: 1.01x slower                                                                  |
| regex_effbot               | 3.57 ms                                                      | 3.62 ms: 1.01x slower                                                                 |
| pprint_pformat             | 1.65 sec                                                     | 1.68 sec: 1.01x slower                                                                |
| xml_etree_process          | 58.4 ms                                                      | 59.3 ms: 1.01x slower                                                                 |
| sqlglot_optimize           | 57.5 ms                                                      | 58.5 ms: 1.02x slower                                                                 |
| sqlglot_parse              | 1.38 ms                                                      | 1.41 ms: 1.02x slower                                                                 |
| json_loads                 | 24.4 us                                                      | 24.9 us: 1.02x slower                                                                 |
| pprint_safe_repr           | 807 ms                                                       | 827 ms: 1.02x slower                                                                  |
| docutils                   | 2.87 sec                                                     | 2.94 sec: 1.03x slower                                                                |
| pycparser                  | 1.23 sec                                                     | 1.27 sec: 1.03x slower                                                                |
| sympy_expand               | 484 ms                                                       | 501 ms: 1.03x slower                                                                  |
| float                      | 76.6 ms                                                      | 79.3 ms: 1.04x slower                                                                 |
| mako                       | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                                                 |
| django_template            | 38.2 ms                                                      | 39.7 ms: 1.04x slower                                                                 |
| sqlglot_normalize          | 116 ms                                                       | 121 ms: 1.04x slower                                                                  |
| json                       | 5.12 ms                                                      | 5.33 ms: 1.04x slower                                                                 |
| logging_silent             | 94.4 ns                                                      | 98.5 ns: 1.04x slower                                                                 |
| json_dumps                 | 10.2 ms                                                      | 10.7 ms: 1.04x slower                                                                 |
| python_startup_no_site     | 8.64 ms                                                      | 9.04 ms: 1.05x slower                                                                 |
| fannkuch                   | 350 ms                                                       | 371 ms: 1.06x slower                                                                  |
| deltablue                  | 3.24 ms                                                      | 3.43 ms: 1.06x slower                                                                 |
| spectral_norm              | 91.6 ms                                                      | 97.2 ms: 1.06x slower                                                                 |
| tomli_loads                | 2.16 sec                                                     | 2.30 sec: 1.06x slower                                                                |
| hexiom                     | 5.96 ms                                                      | 6.36 ms: 1.07x slower                                                                 |
| richards                   | 45.7 ms                                                      | 49.0 ms: 1.07x slower                                                                 |
| richards_super             | 51.3 ms                                                      | 55.1 ms: 1.07x slower                                                                 |
| pyflate                    | 439 ms                                                       | 471 ms: 1.07x slower                                                                  |
| regex_v8                   | 23.6 ms                                                      | 26.1 ms: 1.11x slower                                                                 |
| go                         | 150 ms                                                       | 166 ms: 1.11x slower                                                                  |
| telco                      | 6.96 ms                                                      | 7.98 ms: 1.15x slower                                                                 |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                                 |
| scimark_sor                | 109 ms                                                       | 126 ms: 1.16x slower                                                                  |
| typing_runtime_protocols   | 152 us                                                       | 176 us: 1.16x slower                                                                  |
| coverage                   | 66.7 ms                                                      | 78.0 ms: 1.17x slower                                                                 |
| create_gc_cycles           | 1.59 ms                                                      | 2.01 ms: 1.26x slower                                                                 |
| gc_traversal               | 3.48 ms                                                      | 4.50 ms: 1.29x slower                                                                 |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                          |

Benchmark hidden because not significant (2): bench_mp_pool, sqlglot_transpile
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240822-3.14.0a0-10855bc/bm-20240822-pythonperf2-x86_64-faster%2dcpython-fix_not_specialized_-3.14.0a0-10855bc.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 64.17% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x