# Results vs. 3.12.0

- fork: faster-cpython
- ref: experimental_branch_
- machine: linux-x86_64
- commit hash: cc98bb5
- commit date: 2024-07-31
- overall geometric mean: 1.03x faster
- HPT reliability: 82.78%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 283 ms: 1.01x faster                                                                  |
| docutils       | 2.87 sec                                                     | 2.98 sec: 1.04x slower                                                                |
| tornado_http   | 121 ms                                                       | 117 ms: 1.04x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 300 ms: 1.44x faster                                                                  |
| async_tree_memoization_tg  | 540 ms                                                       | 380 ms: 1.42x faster                                                                  |
| async_tree_io_tg           | 1.05 sec                                                     | 758 ms: 1.39x faster                                                                  |
| async_tree_none            | 452 ms                                                       | 331 ms: 1.37x faster                                                                  |
| async_tree_memoization     | 544 ms                                                       | 401 ms: 1.36x faster                                                                  |
| async_tree_io              | 1.04 sec                                                     | 788 ms: 1.32x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 537 ms: 1.30x faster                                                                  |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 572 ms: 1.22x faster                                                                  |
| Geometric mean             | (ref)                                                        | 1.35x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 253 ms: 1.05x faster                                                                  |
| nbody          | 88.0 ms                                                      | 85.7 ms: 1.03x faster                                                                 |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                          |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 139 ms: 1.03x faster                                                                  |
| regex_effbot   | 3.57 ms                                                      | 3.51 ms: 1.02x faster                                                                 |
| regex_v8       | 23.6 ms                                                      | 25.3 ms: 1.07x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 101 ms: 1.02x faster                                                                  |
| unpickle_pure_python | 210 us                                                       | 205 us: 1.02x faster                                                                  |
| xml_etree_generate   | 86.1 ms                                                      | 84.4 ms: 1.02x faster                                                                 |
| xml_etree_parse      | 144 ms                                                       | 142 ms: 1.01x faster                                                                  |
| xml_etree_process    | 58.4 ms                                                      | 58.8 ms: 1.01x slower                                                                 |
| json_dumps           | 10.2 ms                                                      | 10.7 ms: 1.05x slower                                                                 |
| json_loads           | 24.4 us                                                      | 25.7 us: 1.05x slower                                                                 |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                                          |

Benchmark hidden because not significant (2): tomli_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.06 ms: 1.05x slower                                                                 |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                                 |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 39.1 ms: 1.02x slower                                                                 |
| mako            | 10.0 ms                                                      | 10.5 ms: 1.05x slower                                                                 |
| Geometric mean  | (ref)                                                        | 1.04x slower                                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 300 ms: 1.44x faster                                                                  |
| async_tree_memoization_tg  | 540 ms                                                       | 380 ms: 1.42x faster                                                                  |
| async_tree_io_tg           | 1.05 sec                                                     | 758 ms: 1.39x faster                                                                  |
| async_tree_none            | 452 ms                                                       | 331 ms: 1.37x faster                                                                  |
| async_tree_memoization     | 544 ms                                                       | 401 ms: 1.36x faster                                                                  |
| generators                 | 37.4 ms                                                      | 28.1 ms: 1.33x faster                                                                 |
| async_tree_io              | 1.04 sec                                                     | 788 ms: 1.32x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 537 ms: 1.30x faster                                                                  |
| deepcopy                   | 368 us                                                       | 292 us: 1.26x faster                                                                  |
| comprehensions             | 21.9 us                                                      | 17.4 us: 1.26x faster                                                                 |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 572 ms: 1.22x faster                                                                  |
| deepcopy_memo              | 36.8 us                                                      | 30.5 us: 1.21x faster                                                                 |
| pathlib                    | 18.9 ms                                                      | 16.1 ms: 1.18x faster                                                                 |
| deepcopy_reduce            | 3.37 us                                                      | 2.97 us: 1.13x faster                                                                 |
| raytrace                   | 298 ms                                                       | 267 ms: 1.12x faster                                                                  |
| bench_thread_pool          | 950 us                                                       | 853 us: 1.11x faster                                                                  |
| async_generators           | 390 ms                                                       | 351 ms: 1.11x faster                                                                  |
| logging_format             | 7.48 us                                                      | 6.80 us: 1.10x faster                                                                 |
| logging_simple             | 6.71 us                                                      | 6.18 us: 1.09x faster                                                                 |
| coroutines                 | 23.0 ms                                                      | 21.4 ms: 1.08x faster                                                                 |
| crypto_pyaes               | 80.3 ms                                                      | 74.7 ms: 1.08x faster                                                                 |
| sympy_sum                  | 162 ms                                                       | 153 ms: 1.06x faster                                                                  |
| pidigits                   | 265 ms                                                       | 253 ms: 1.05x faster                                                                  |
| dask                       | 392 ms                                                       | 376 ms: 1.04x faster                                                                  |
| scimark_monte_carlo        | 69.0 ms                                                      | 66.1 ms: 1.04x faster                                                                 |
| chaos                      | 64.0 ms                                                      | 61.4 ms: 1.04x faster                                                                 |
| scimark_lu                 | 98.8 ms                                                      | 95.0 ms: 1.04x faster                                                                 |
| sympy_str                  | 302 ms                                                       | 291 ms: 1.04x faster                                                                  |
| tornado_http               | 121 ms                                                       | 117 ms: 1.04x faster                                                                  |
| regex_compile              | 144 ms                                                       | 139 ms: 1.03x faster                                                                  |
| nbody                      | 88.0 ms                                                      | 85.7 ms: 1.03x faster                                                                 |
| sympy_integrate            | 23.9 ms                                                      | 23.4 ms: 1.02x faster                                                                 |
| xml_etree_iterparse        | 103 ms                                                       | 101 ms: 1.02x faster                                                                  |
| unpickle_pure_python       | 210 us                                                       | 205 us: 1.02x faster                                                                  |
| xml_etree_generate         | 86.1 ms                                                      | 84.4 ms: 1.02x faster                                                                 |
| regex_effbot               | 3.57 ms                                                      | 3.51 ms: 1.02x faster                                                                 |
| xml_etree_parse            | 144 ms                                                       | 142 ms: 1.01x faster                                                                  |
| 2to3                       | 285 ms                                                       | 283 ms: 1.01x faster                                                                  |
| asyncio_tcp                | 378 ms                                                       | 376 ms: 1.01x faster                                                                  |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                                                |
| meteor_contest             | 128 ms                                                       | 127 ms: 1.01x faster                                                                  |
| mdp                        | 2.57 sec                                                     | 2.58 sec: 1.00x slower                                                                |
| xml_etree_process          | 58.4 ms                                                      | 58.8 ms: 1.01x slower                                                                 |
| sqlglot_parse              | 1.38 ms                                                      | 1.39 ms: 1.01x slower                                                                 |
| pprint_pformat             | 1.65 sec                                                     | 1.67 sec: 1.01x slower                                                                |
| asyncio_websockets         | 387 ms                                                       | 391 ms: 1.01x slower                                                                  |
| pprint_safe_repr           | 807 ms                                                       | 817 ms: 1.01x slower                                                                  |
| logging_silent             | 94.4 ns                                                      | 95.6 ns: 1.01x slower                                                                 |
| nqueens                    | 89.9 ms                                                      | 91.1 ms: 1.01x slower                                                                 |
| pycparser                  | 1.23 sec                                                     | 1.26 sec: 1.02x slower                                                                |
| django_template            | 38.2 ms                                                      | 39.1 ms: 1.02x slower                                                                 |
| scimark_fft                | 301 ms                                                       | 309 ms: 1.02x slower                                                                  |
| sympy_expand               | 484 ms                                                       | 496 ms: 1.03x slower                                                                  |
| sqlglot_optimize           | 57.5 ms                                                      | 59.0 ms: 1.03x slower                                                                 |
| sqlglot_normalize          | 116 ms                                                       | 119 ms: 1.03x slower                                                                  |
| docutils                   | 2.87 sec                                                     | 2.98 sec: 1.04x slower                                                                |
| fannkuch                   | 350 ms                                                       | 365 ms: 1.04x slower                                                                  |
| hexiom                     | 5.96 ms                                                      | 6.22 ms: 1.04x slower                                                                 |
| pyflate                    | 439 ms                                                       | 458 ms: 1.04x slower                                                                  |
| deltablue                  | 3.24 ms                                                      | 3.38 ms: 1.05x slower                                                                 |
| json_dumps                 | 10.2 ms                                                      | 10.7 ms: 1.05x slower                                                                 |
| python_startup_no_site     | 8.64 ms                                                      | 9.06 ms: 1.05x slower                                                                 |
| mako                       | 10.0 ms                                                      | 10.5 ms: 1.05x slower                                                                 |
| go                         | 150 ms                                                       | 158 ms: 1.05x slower                                                                  |
| json_loads                 | 24.4 us                                                      | 25.7 us: 1.05x slower                                                                 |
| spectral_norm              | 91.6 ms                                                      | 96.7 ms: 1.06x slower                                                                 |
| richards                   | 45.7 ms                                                      | 48.4 ms: 1.06x slower                                                                 |
| richards_super             | 51.3 ms                                                      | 54.7 ms: 1.07x slower                                                                 |
| json                       | 5.12 ms                                                      | 5.45 ms: 1.07x slower                                                                 |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.49 ms: 1.07x slower                                                                 |
| regex_v8                   | 23.6 ms                                                      | 25.3 ms: 1.07x slower                                                                 |
| scimark_sor                | 109 ms                                                       | 119 ms: 1.09x slower                                                                  |
| telco                      | 6.96 ms                                                      | 7.97 ms: 1.14x slower                                                                 |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                                 |
| coverage                   | 66.7 ms                                                      | 78.7 ms: 1.18x slower                                                                 |
| typing_runtime_protocols   | 152 us                                                       | 180 us: 1.19x slower                                                                  |
| create_gc_cycles           | 1.59 ms                                                      | 1.94 ms: 1.22x slower                                                                 |
| gc_traversal               | 3.48 ms                                                      | 4.49 ms: 1.29x slower                                                                 |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                          |

Benchmark hidden because not significant (6): bench_mp_pool, regex_dna, tomli_loads, sqlglot_transpile, float, pickle_pure_python
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240731-3.14.0a0-cc98bb5/bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 82.78% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x