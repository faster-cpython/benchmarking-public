# Results vs. 3.12.0

- fork: faster-cpython
- ref: experimental_branch_
- machine: linux-x86_64
- commit hash: 1a2b0b8
- commit date: 2024-07-31
- overall geometric mean: 1.02x faster
- HPT reliability: 60.48%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 288 ms: 1.01x slower                                                                  |
| docutils       | 2.87 sec                                                     | 3.01 sec: 1.05x slower                                                                |
| tornado_http   | 121 ms                                                       | 118 ms: 1.03x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 304 ms: 1.42x faster                                                                  |
| async_tree_memoization_tg  | 540 ms                                                       | 388 ms: 1.39x faster                                                                  |
| async_tree_io_tg           | 1.05 sec                                                     | 781 ms: 1.35x faster                                                                  |
| async_tree_none            | 452 ms                                                       | 336 ms: 1.34x faster                                                                  |
| async_tree_memoization     | 544 ms                                                       | 409 ms: 1.33x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 546 ms: 1.28x faster                                                                  |
| async_tree_io              | 1.04 sec                                                     | 818 ms: 1.27x faster                                                                  |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 582 ms: 1.19x faster                                                                  |
| Geometric mean             | (ref)                                                        | 1.32x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 254 ms: 1.04x faster                                                                  |
| nbody          | 88.0 ms                                                      | 85.6 ms: 1.03x faster                                                                 |
| float          | 76.6 ms                                                      | 80.2 ms: 1.05x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_dna      | 239 ms                                                       | 236 ms: 1.01x faster                                                                  |
| regex_compile  | 144 ms                                                       | 143 ms: 1.01x faster                                                                  |
| regex_effbot   | 3.57 ms                                                      | 3.56 ms: 1.00x faster                                                                 |
| regex_v8       | 23.6 ms                                                      | 25.6 ms: 1.08x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|--------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| xml_etree_generate | 86.1 ms                                                      | 85.3 ms: 1.01x faster                                                                 |
| pickle_pure_python | 318 us                                                       | 321 us: 1.01x slower                                                                  |
| xml_etree_parse    | 144 ms                                                       | 145 ms: 1.01x slower                                                                  |
| xml_etree_process  | 58.4 ms                                                      | 59.2 ms: 1.01x slower                                                                 |
| tomli_loads        | 2.16 sec                                                     | 2.21 sec: 1.03x slower                                                                |
| json_dumps         | 10.2 ms                                                      | 10.8 ms: 1.05x slower                                                                 |
| json_loads         | 24.4 us                                                      | 25.8 us: 1.06x slower                                                                 |
| Geometric mean     | (ref)                                                        | 1.02x slower                                                                          |

Benchmark hidden because not significant (2): unpickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.08 ms: 1.05x slower                                                                 |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                                 |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 10.6 ms: 1.06x slower                                                                 |
| django_template | 38.2 ms                                                      | 40.7 ms: 1.07x slower                                                                 |
| Geometric mean  | (ref)                                                        | 1.06x slower                                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 304 ms: 1.42x faster                                                                  |
| async_tree_memoization_tg  | 540 ms                                                       | 388 ms: 1.39x faster                                                                  |
| async_tree_io_tg           | 1.05 sec                                                     | 781 ms: 1.35x faster                                                                  |
| async_tree_none            | 452 ms                                                       | 336 ms: 1.34x faster                                                                  |
| async_tree_memoization     | 544 ms                                                       | 409 ms: 1.33x faster                                                                  |
| generators                 | 37.4 ms                                                      | 28.7 ms: 1.30x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 546 ms: 1.28x faster                                                                  |
| async_tree_io              | 1.04 sec                                                     | 818 ms: 1.27x faster                                                                  |
| deepcopy                   | 368 us                                                       | 290 us: 1.27x faster                                                                  |
| comprehensions             | 21.9 us                                                      | 17.6 us: 1.24x faster                                                                 |
| deepcopy_memo              | 36.8 us                                                      | 30.5 us: 1.21x faster                                                                 |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 582 ms: 1.19x faster                                                                  |
| pathlib                    | 18.9 ms                                                      | 16.2 ms: 1.17x faster                                                                 |
| deepcopy_reduce            | 3.37 us                                                      | 2.95 us: 1.14x faster                                                                 |
| crypto_pyaes               | 80.3 ms                                                      | 71.0 ms: 1.13x faster                                                                 |
| raytrace                   | 298 ms                                                       | 266 ms: 1.12x faster                                                                  |
| bench_thread_pool          | 950 us                                                       | 874 us: 1.09x faster                                                                  |
| logging_format             | 7.48 us                                                      | 6.91 us: 1.08x faster                                                                 |
| logging_simple             | 6.71 us                                                      | 6.25 us: 1.07x faster                                                                 |
| coroutines                 | 23.0 ms                                                      | 21.5 ms: 1.07x faster                                                                 |
| async_generators           | 390 ms                                                       | 365 ms: 1.07x faster                                                                  |
| pidigits                   | 265 ms                                                       | 254 ms: 1.04x faster                                                                  |
| sympy_sum                  | 162 ms                                                       | 156 ms: 1.04x faster                                                                  |
| scimark_monte_carlo        | 69.0 ms                                                      | 66.5 ms: 1.04x faster                                                                 |
| tornado_http               | 121 ms                                                       | 118 ms: 1.03x faster                                                                  |
| nbody                      | 88.0 ms                                                      | 85.6 ms: 1.03x faster                                                                 |
| mdp                        | 2.57 sec                                                     | 2.50 sec: 1.03x faster                                                                |
| chaos                      | 64.0 ms                                                      | 62.5 ms: 1.02x faster                                                                 |
| sympy_integrate            | 23.9 ms                                                      | 23.5 ms: 1.02x faster                                                                 |
| dask                       | 392 ms                                                       | 386 ms: 1.02x faster                                                                  |
| sympy_str                  | 302 ms                                                       | 299 ms: 1.01x faster                                                                  |
| regex_dna                  | 239 ms                                                       | 236 ms: 1.01x faster                                                                  |
| xml_etree_generate         | 86.1 ms                                                      | 85.3 ms: 1.01x faster                                                                 |
| regex_compile              | 144 ms                                                       | 143 ms: 1.01x faster                                                                  |
| asyncio_tcp                | 378 ms                                                       | 375 ms: 1.01x faster                                                                  |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                                                |
| meteor_contest             | 128 ms                                                       | 128 ms: 1.00x faster                                                                  |
| regex_effbot               | 3.57 ms                                                      | 3.56 ms: 1.00x faster                                                                 |
| pickle_pure_python         | 318 us                                                       | 321 us: 1.01x slower                                                                  |
| 2to3                       | 285 ms                                                       | 288 ms: 1.01x slower                                                                  |
| nqueens                    | 89.9 ms                                                      | 90.7 ms: 1.01x slower                                                                 |
| xml_etree_parse            | 144 ms                                                       | 145 ms: 1.01x slower                                                                  |
| xml_etree_process          | 58.4 ms                                                      | 59.2 ms: 1.01x slower                                                                 |
| sqlglot_parse              | 1.38 ms                                                      | 1.40 ms: 1.02x slower                                                                 |
| tomli_loads                | 2.16 sec                                                     | 2.21 sec: 1.03x slower                                                                |
| pprint_safe_repr           | 807 ms                                                       | 829 ms: 1.03x slower                                                                  |
| fannkuch                   | 350 ms                                                       | 360 ms: 1.03x slower                                                                  |
| pprint_pformat             | 1.65 sec                                                     | 1.70 sec: 1.03x slower                                                                |
| scimark_fft                | 301 ms                                                       | 310 ms: 1.03x slower                                                                  |
| sqlglot_optimize           | 57.5 ms                                                      | 59.3 ms: 1.03x slower                                                                 |
| logging_silent             | 94.4 ns                                                      | 97.4 ns: 1.03x slower                                                                 |
| sqlglot_normalize          | 116 ms                                                       | 120 ms: 1.03x slower                                                                  |
| pycparser                  | 1.23 sec                                                     | 1.28 sec: 1.03x slower                                                                |
| deltablue                  | 3.24 ms                                                      | 3.36 ms: 1.04x slower                                                                 |
| float                      | 76.6 ms                                                      | 80.2 ms: 1.05x slower                                                                 |
| spectral_norm              | 91.6 ms                                                      | 96.1 ms: 1.05x slower                                                                 |
| docutils                   | 2.87 sec                                                     | 3.01 sec: 1.05x slower                                                                |
| json_dumps                 | 10.2 ms                                                      | 10.8 ms: 1.05x slower                                                                 |
| python_startup_no_site     | 8.64 ms                                                      | 9.08 ms: 1.05x slower                                                                 |
| scimark_sor                | 109 ms                                                       | 115 ms: 1.05x slower                                                                  |
| sympy_expand               | 484 ms                                                       | 511 ms: 1.05x slower                                                                  |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.44 ms: 1.06x slower                                                                 |
| mako                       | 10.0 ms                                                      | 10.6 ms: 1.06x slower                                                                 |
| json_loads                 | 24.4 us                                                      | 25.8 us: 1.06x slower                                                                 |
| django_template            | 38.2 ms                                                      | 40.7 ms: 1.07x slower                                                                 |
| go                         | 150 ms                                                       | 160 ms: 1.07x slower                                                                  |
| json                       | 5.12 ms                                                      | 5.48 ms: 1.07x slower                                                                 |
| hexiom                     | 5.96 ms                                                      | 6.39 ms: 1.07x slower                                                                 |
| regex_v8                   | 23.6 ms                                                      | 25.6 ms: 1.08x slower                                                                 |
| richards                   | 45.7 ms                                                      | 51.0 ms: 1.12x slower                                                                 |
| richards_super             | 51.3 ms                                                      | 57.3 ms: 1.12x slower                                                                 |
| pyflate                    | 439 ms                                                       | 491 ms: 1.12x slower                                                                  |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                                 |
| typing_runtime_protocols   | 152 us                                                       | 176 us: 1.16x slower                                                                  |
| telco                      | 6.96 ms                                                      | 8.09 ms: 1.16x slower                                                                 |
| coverage                   | 66.7 ms                                                      | 78.8 ms: 1.18x slower                                                                 |
| create_gc_cycles           | 1.59 ms                                                      | 2.04 ms: 1.28x slower                                                                 |
| gc_traversal               | 3.48 ms                                                      | 4.75 ms: 1.36x slower                                                                 |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                          |

Benchmark hidden because not significant (6): bench_mp_pool, unpickle_pure_python, sqlglot_transpile, scimark_lu, asyncio_websockets, xml_etree_iterparse
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240731-3.14.0a0-1a2b0b8/bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 60.48% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x