# Results vs. 3.12.0

- fork: colesbury
- ref: gh_117376_pydecref_m
- machine: linux-x86_64
- commit hash: 4b27f3a
- commit date: 2024-08-13
- overall geometric mean: 1.43x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 431 ms: 1.51x slower                                                           |
| docutils       | 2.87 sec                                                     | 3.48 sec: 1.21x slower                                                         |
| tornado_http   | 121 ms                                                       | 165 ms: 1.36x slower                                                           |
| Geometric mean | (ref)                                                        | 1.36x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 360 ms: 1.20x faster                                                           |
| async_tree_io_tg           | 1.05 sec                                                     | 880 ms: 1.20x faster                                                           |
| async_tree_memoization_tg  | 540 ms                                                       | 462 ms: 1.17x faster                                                           |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 626 ms: 1.11x faster                                                           |
| async_tree_io              | 1.04 sec                                                     | 940 ms: 1.11x faster                                                           |
| async_tree_none            | 452 ms                                                       | 413 ms: 1.09x faster                                                           |
| async_tree_memoization     | 544 ms                                                       | 514 ms: 1.06x faster                                                           |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 678 ms: 1.03x faster                                                           |
| Geometric mean             | (ref)                                                        | 1.12x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 250 ms: 1.06x faster                                                           |
| float          | 76.6 ms                                                      | 142 ms: 1.85x slower                                                           |
| nbody          | 88.0 ms                                                      | 193 ms: 2.20x slower                                                           |
| Geometric mean | (ref)                                                        | 1.57x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.65 ms: 1.02x slower                                                          |
| regex_dna      | 239 ms                                                       | 248 ms: 1.04x slower                                                           |
| regex_v8       | 23.6 ms                                                      | 27.4 ms: 1.16x slower                                                          |
| regex_compile  | 144 ms                                                       | 229 ms: 1.59x slower                                                           |
| Geometric mean | (ref)                                                        | 1.18x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_parse      | 144 ms                                                       | 138 ms: 1.05x faster                                                           |
| xml_etree_iterparse  | 103 ms                                                       | 109 ms: 1.06x slower                                                           |
| json_loads           | 24.4 us                                                      | 30.0 us: 1.23x slower                                                          |
| xml_etree_generate   | 86.1 ms                                                      | 118 ms: 1.37x slower                                                           |
| json_dumps           | 10.2 ms                                                      | 14.1 ms: 1.38x slower                                                          |
| tomli_loads          | 2.16 sec                                                     | 3.32 sec: 1.54x slower                                                         |
| xml_etree_process    | 58.4 ms                                                      | 96.1 ms: 1.64x slower                                                          |
| pickle_pure_python   | 318 us                                                       | 594 us: 1.87x slower                                                           |
| unpickle_pure_python | 210 us                                                       | 409 us: 1.95x slower                                                           |
| Geometric mean       | (ref)                                                        | 1.41x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 11.8 ms: 1.36x slower                                                          |
| python_startup         | 11.6 ms                                                      | 17.1 ms: 1.47x slower                                                          |
| Geometric mean         | (ref)                                                        | 1.42x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 67.7 ms: 1.77x slower                                                          |
| mako            | 10.0 ms                                                      | 22.3 ms: 2.23x slower                                                          |
| Geometric mean  | (ref)                                                        | 1.99x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 360 ms: 1.20x faster                                                           |
| async_tree_io_tg           | 1.05 sec                                                     | 880 ms: 1.20x faster                                                           |
| async_tree_memoization_tg  | 540 ms                                                       | 462 ms: 1.17x faster                                                           |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 626 ms: 1.11x faster                                                           |
| async_tree_io              | 1.04 sec                                                     | 940 ms: 1.11x faster                                                           |
| async_tree_none            | 452 ms                                                       | 413 ms: 1.09x faster                                                           |
| gc_traversal               | 3.48 ms                                                      | 3.27 ms: 1.06x faster                                                          |
| pidigits                   | 265 ms                                                       | 250 ms: 1.06x faster                                                           |
| async_tree_memoization     | 544 ms                                                       | 514 ms: 1.06x faster                                                           |
| xml_etree_parse            | 144 ms                                                       | 138 ms: 1.05x faster                                                           |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 678 ms: 1.03x faster                                                           |
| asyncio_websockets         | 387 ms                                                       | 384 ms: 1.01x faster                                                           |
| regex_effbot               | 3.57 ms                                                      | 3.65 ms: 1.02x slower                                                          |
| regex_dna                  | 239 ms                                                       | 248 ms: 1.04x slower                                                           |
| pathlib                    | 18.9 ms                                                      | 19.9 ms: 1.05x slower                                                          |
| create_gc_cycles           | 1.59 ms                                                      | 1.68 ms: 1.05x slower                                                          |
| xml_etree_iterparse        | 103 ms                                                       | 109 ms: 1.06x slower                                                           |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.77 sec: 1.11x slower                                                         |
| generators                 | 37.4 ms                                                      | 41.7 ms: 1.11x slower                                                          |
| regex_v8                   | 23.6 ms                                                      | 27.4 ms: 1.16x slower                                                          |
| asyncio_tcp                | 378 ms                                                       | 449 ms: 1.19x slower                                                           |
| json                       | 5.12 ms                                                      | 6.15 ms: 1.20x slower                                                          |
| docutils                   | 2.87 sec                                                     | 3.48 sec: 1.21x slower                                                         |
| deepcopy                   | 368 us                                                       | 451 us: 1.22x slower                                                           |
| json_loads                 | 24.4 us                                                      | 30.0 us: 1.23x slower                                                          |
| coroutines                 | 23.0 ms                                                      | 28.3 ms: 1.23x slower                                                          |
| mdp                        | 2.57 sec                                                     | 3.21 sec: 1.25x slower                                                         |
| async_generators           | 390 ms                                                       | 499 ms: 1.28x slower                                                           |
| sympy_integrate            | 23.9 ms                                                      | 32.1 ms: 1.34x slower                                                          |
| meteor_contest             | 128 ms                                                       | 174 ms: 1.36x slower                                                           |
| python_startup_no_site     | 8.64 ms                                                      | 11.8 ms: 1.36x slower                                                          |
| tornado_http               | 121 ms                                                       | 165 ms: 1.36x slower                                                           |
| comprehensions             | 21.9 us                                                      | 30.0 us: 1.37x slower                                                          |
| xml_etree_generate         | 86.1 ms                                                      | 118 ms: 1.37x slower                                                           |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.80 ms: 1.38x slower                                                          |
| json_dumps                 | 10.2 ms                                                      | 14.1 ms: 1.38x slower                                                          |
| pycparser                  | 1.23 sec                                                     | 1.73 sec: 1.40x slower                                                         |
| scimark_fft                | 301 ms                                                       | 425 ms: 1.41x slower                                                           |
| deepcopy_reduce            | 3.37 us                                                      | 4.77 us: 1.41x slower                                                          |
| nqueens                    | 89.9 ms                                                      | 128 ms: 1.42x slower                                                           |
| deepcopy_memo              | 36.8 us                                                      | 53.0 us: 1.44x slower                                                          |
| python_startup             | 11.6 ms                                                      | 17.1 ms: 1.47x slower                                                          |
| sympy_str                  | 302 ms                                                       | 453 ms: 1.50x slower                                                           |
| crypto_pyaes               | 80.3 ms                                                      | 121 ms: 1.50x slower                                                           |
| telco                      | 6.96 ms                                                      | 10.5 ms: 1.50x slower                                                          |
| 2to3                       | 285 ms                                                       | 431 ms: 1.51x slower                                                           |
| tomli_loads                | 2.16 sec                                                     | 3.32 sec: 1.54x slower                                                         |
| coverage                   | 66.7 ms                                                      | 104 ms: 1.56x slower                                                           |
| regex_compile              | 144 ms                                                       | 229 ms: 1.59x slower                                                           |
| sqlglot_normalize          | 116 ms                                                       | 186 ms: 1.61x slower                                                           |
| sympy_sum                  | 162 ms                                                       | 262 ms: 1.62x slower                                                           |
| sqlglot_optimize           | 57.5 ms                                                      | 93.5 ms: 1.63x slower                                                          |
| fannkuch                   | 350 ms                                                       | 569 ms: 1.63x slower                                                           |
| xml_etree_process          | 58.4 ms                                                      | 96.1 ms: 1.64x slower                                                          |
| logging_format             | 7.48 us                                                      | 12.6 us: 1.68x slower                                                          |
| sympy_expand               | 484 ms                                                       | 819 ms: 1.69x slower                                                           |
| pyflate                    | 439 ms                                                       | 763 ms: 1.74x slower                                                           |
| logging_simple             | 6.71 us                                                      | 11.7 us: 1.74x slower                                                          |
| pprint_safe_repr           | 807 ms                                                       | 1.42 sec: 1.76x slower                                                         |
| pprint_pformat             | 1.65 sec                                                     | 2.92 sec: 1.77x slower                                                         |
| richards                   | 45.7 ms                                                      | 80.8 ms: 1.77x slower                                                          |
| django_template            | 38.2 ms                                                      | 67.7 ms: 1.77x slower                                                          |
| bench_thread_pool          | 950 us                                                       | 1.71 ms: 1.80x slower                                                          |
| spectral_norm              | 91.6 ms                                                      | 166 ms: 1.82x slower                                                           |
| float                      | 76.6 ms                                                      | 142 ms: 1.85x slower                                                           |
| typing_runtime_protocols   | 152 us                                                       | 282 us: 1.86x slower                                                           |
| pickle_pure_python         | 318 us                                                       | 594 us: 1.87x slower                                                           |
| sqlglot_transpile          | 1.78 ms                                                      | 3.40 ms: 1.92x slower                                                          |
| richards_super             | 51.3 ms                                                      | 98.7 ms: 1.92x slower                                                          |
| chaos                      | 64.0 ms                                                      | 124 ms: 1.93x slower                                                           |
| scimark_monte_carlo        | 69.0 ms                                                      | 134 ms: 1.94x slower                                                           |
| logging_silent             | 94.4 ns                                                      | 183 ns: 1.94x slower                                                           |
| unpickle_pure_python       | 210 us                                                       | 409 us: 1.95x slower                                                           |
| hexiom                     | 5.96 ms                                                      | 11.7 ms: 1.96x slower                                                          |
| raytrace                   | 298 ms                                                       | 599 ms: 2.01x slower                                                           |
| sqlglot_parse              | 1.38 ms                                                      | 2.87 ms: 2.09x slower                                                          |
| nbody                      | 88.0 ms                                                      | 193 ms: 2.20x slower                                                           |
| scimark_sor                | 109 ms                                                       | 240 ms: 2.20x slower                                                           |
| go                         | 150 ms                                                       | 330 ms: 2.21x slower                                                           |
| mako                       | 10.0 ms                                                      | 22.3 ms: 2.23x slower                                                          |
| scimark_lu                 | 98.8 ms                                                      | 235 ms: 2.38x slower                                                           |
| deltablue                  | 3.24 ms                                                      | 8.25 ms: 2.55x slower                                                          |
| Geometric mean             | (ref)                                                        | 1.43x slower                                                                   |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240813-3.14.0a0-4b27f3a-NOGIL/bm-20240813-pythonperf2-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.36x
- 95% likely to have a slowdown of 1.32x
- 99% likely to have a slowdown of 1.26x

# Memory
- memory change: 1.08x