# Results vs. 3.12.0

- fork: faster-cpython
- ref: specialize_call_ex
- machine: linux-x86_64
- commit hash: 852115b
- commit date: 2024-08-19
- overall geometric mean: 1.03x faster
- HPT reliability: 57.35%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240819-pythonperf2-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-852115b |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 289 ms: 1.02x slower                                                                |
| docutils       | 2.87 sec                                                     | 2.99 sec: 1.04x slower                                                              |
| tornado_http   | 121 ms                                                       | 118 ms: 1.03x faster                                                                |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240819-pythonperf2-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-852115b |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 300 ms: 1.44x faster                                                                |
| async_tree_memoization_tg  | 540 ms                                                       | 382 ms: 1.42x faster                                                                |
| async_tree_io_tg           | 1.05 sec                                                     | 764 ms: 1.38x faster                                                                |
| async_tree_none            | 452 ms                                                       | 333 ms: 1.35x faster                                                                |
| async_tree_memoization     | 544 ms                                                       | 403 ms: 1.35x faster                                                                |
| async_tree_io              | 1.04 sec                                                     | 798 ms: 1.31x faster                                                                |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 537 ms: 1.30x faster                                                                |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 574 ms: 1.21x faster                                                                |
| Geometric mean             | (ref)                                                        | 1.34x faster                                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240819-pythonperf2-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-852115b |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 253 ms: 1.05x faster                                                                |
| nbody          | 88.0 ms                                                      | 85.4 ms: 1.03x faster                                                               |
| float          | 76.6 ms                                                      | 80.1 ms: 1.05x slower                                                               |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240819-pythonperf2-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-852115b |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 140 ms: 1.03x faster                                                                |
| regex_dna      | 239 ms                                                       | 239 ms: 1.00x slower                                                                |
| regex_effbot   | 3.57 ms                                                      | 3.66 ms: 1.02x slower                                                               |
| regex_v8       | 23.6 ms                                                      | 25.2 ms: 1.07x slower                                                               |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240819-pythonperf2-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-852115b |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 84.2 ms: 1.02x faster                                                               |
| xml_etree_parse      | 144 ms                                                       | 143 ms: 1.01x faster                                                                |
| pickle_pure_python   | 318 us                                                       | 317 us: 1.00x faster                                                                |
| xml_etree_process    | 58.4 ms                                                      | 58.7 ms: 1.01x slower                                                               |
| unpickle_pure_python | 210 us                                                       | 213 us: 1.02x slower                                                                |
| json_loads           | 24.4 us                                                      | 25.0 us: 1.03x slower                                                               |
| json_dumps           | 10.2 ms                                                      | 10.6 ms: 1.03x slower                                                               |
| tomli_loads          | 2.16 sec                                                     | 2.28 sec: 1.06x slower                                                              |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                        |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240819-pythonperf2-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-852115b |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.03 ms: 1.05x slower                                                               |
| python_startup         | 11.6 ms                                                      | 13.3 ms: 1.15x slower                                                               |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240819-pythonperf2-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-852115b |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 39.6 ms: 1.04x slower                                                               |
| mako            | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                                               |
| Geometric mean  | (ref)                                                        | 1.04x slower                                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240819-pythonperf2-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-852115b |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 300 ms: 1.44x faster                                                                |
| async_tree_memoization_tg  | 540 ms                                                       | 382 ms: 1.42x faster                                                                |
| async_tree_io_tg           | 1.05 sec                                                     | 764 ms: 1.38x faster                                                                |
| async_tree_none            | 452 ms                                                       | 333 ms: 1.35x faster                                                                |
| async_tree_memoization     | 544 ms                                                       | 403 ms: 1.35x faster                                                                |
| async_tree_io              | 1.04 sec                                                     | 798 ms: 1.31x faster                                                                |
| deepcopy                   | 368 us                                                       | 284 us: 1.30x faster                                                                |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 537 ms: 1.30x faster                                                                |
| generators                 | 37.4 ms                                                      | 29.1 ms: 1.29x faster                                                               |
| comprehensions             | 21.9 us                                                      | 17.3 us: 1.27x faster                                                               |
| deepcopy_memo              | 36.8 us                                                      | 29.6 us: 1.24x faster                                                               |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 574 ms: 1.21x faster                                                                |
| pathlib                    | 18.9 ms                                                      | 16.1 ms: 1.17x faster                                                               |
| deepcopy_reduce            | 3.37 us                                                      | 2.87 us: 1.17x faster                                                               |
| raytrace                   | 298 ms                                                       | 263 ms: 1.13x faster                                                                |
| crypto_pyaes               | 80.3 ms                                                      | 73.3 ms: 1.10x faster                                                               |
| bench_thread_pool          | 950 us                                                       | 869 us: 1.09x faster                                                                |
| scimark_monte_carlo        | 69.0 ms                                                      | 64.7 ms: 1.07x faster                                                               |
| async_generators           | 390 ms                                                       | 368 ms: 1.06x faster                                                                |
| coroutines                 | 23.0 ms                                                      | 21.8 ms: 1.06x faster                                                               |
| logging_format             | 7.48 us                                                      | 7.09 us: 1.06x faster                                                               |
| pidigits                   | 265 ms                                                       | 253 ms: 1.05x faster                                                                |
| logging_simple             | 6.71 us                                                      | 6.43 us: 1.04x faster                                                               |
| sympy_sum                  | 162 ms                                                       | 155 ms: 1.04x faster                                                                |
| chaos                      | 64.0 ms                                                      | 61.8 ms: 1.04x faster                                                               |
| scimark_lu                 | 98.8 ms                                                      | 95.8 ms: 1.03x faster                                                               |
| nbody                      | 88.0 ms                                                      | 85.4 ms: 1.03x faster                                                               |
| sympy_integrate            | 23.9 ms                                                      | 23.2 ms: 1.03x faster                                                               |
| regex_compile              | 144 ms                                                       | 140 ms: 1.03x faster                                                                |
| tornado_http               | 121 ms                                                       | 118 ms: 1.03x faster                                                                |
| xml_etree_generate         | 86.1 ms                                                      | 84.2 ms: 1.02x faster                                                               |
| mdp                        | 2.57 sec                                                     | 2.51 sec: 1.02x faster                                                              |
| meteor_contest             | 128 ms                                                       | 125 ms: 1.02x faster                                                                |
| sympy_str                  | 302 ms                                                       | 297 ms: 1.02x faster                                                                |
| xml_etree_parse            | 144 ms                                                       | 143 ms: 1.01x faster                                                                |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                                              |
| asyncio_tcp                | 378 ms                                                       | 376 ms: 1.01x faster                                                                |
| pickle_pure_python         | 318 us                                                       | 317 us: 1.00x faster                                                                |
| regex_dna                  | 239 ms                                                       | 239 ms: 1.00x slower                                                                |
| xml_etree_process          | 58.4 ms                                                      | 58.7 ms: 1.01x slower                                                               |
| asyncio_websockets         | 387 ms                                                       | 390 ms: 1.01x slower                                                                |
| sqlglot_transpile          | 1.78 ms                                                      | 1.80 ms: 1.01x slower                                                               |
| nqueens                    | 89.9 ms                                                      | 90.9 ms: 1.01x slower                                                               |
| pycparser                  | 1.23 sec                                                     | 1.25 sec: 1.01x slower                                                              |
| scimark_fft                | 301 ms                                                       | 305 ms: 1.01x slower                                                                |
| 2to3                       | 285 ms                                                       | 289 ms: 1.02x slower                                                                |
| unpickle_pure_python       | 210 us                                                       | 213 us: 1.02x slower                                                                |
| pprint_pformat             | 1.65 sec                                                     | 1.69 sec: 1.02x slower                                                              |
| sqlglot_optimize           | 57.5 ms                                                      | 58.7 ms: 1.02x slower                                                               |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.30 ms: 1.02x slower                                                               |
| fannkuch                   | 350 ms                                                       | 358 ms: 1.02x slower                                                                |
| sqlglot_normalize          | 116 ms                                                       | 118 ms: 1.02x slower                                                                |
| regex_effbot               | 3.57 ms                                                      | 3.66 ms: 1.02x slower                                                               |
| pprint_safe_repr           | 807 ms                                                       | 827 ms: 1.02x slower                                                                |
| json_loads                 | 24.4 us                                                      | 25.0 us: 1.03x slower                                                               |
| logging_silent             | 94.4 ns                                                      | 97.4 ns: 1.03x slower                                                               |
| json_dumps                 | 10.2 ms                                                      | 10.6 ms: 1.03x slower                                                               |
| django_template            | 38.2 ms                                                      | 39.6 ms: 1.04x slower                                                               |
| sqlglot_parse              | 1.38 ms                                                      | 1.43 ms: 1.04x slower                                                               |
| sympy_expand               | 484 ms                                                       | 503 ms: 1.04x slower                                                                |
| mako                       | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                                               |
| docutils                   | 2.87 sec                                                     | 2.99 sec: 1.04x slower                                                              |
| spectral_norm              | 91.6 ms                                                      | 95.6 ms: 1.04x slower                                                               |
| float                      | 76.6 ms                                                      | 80.1 ms: 1.05x slower                                                               |
| hexiom                     | 5.96 ms                                                      | 6.23 ms: 1.05x slower                                                               |
| python_startup_no_site     | 8.64 ms                                                      | 9.03 ms: 1.05x slower                                                               |
| json                       | 5.12 ms                                                      | 5.37 ms: 1.05x slower                                                               |
| deltablue                  | 3.24 ms                                                      | 3.41 ms: 1.05x slower                                                               |
| tomli_loads                | 2.16 sec                                                     | 2.28 sec: 1.06x slower                                                              |
| scimark_sor                | 109 ms                                                       | 116 ms: 1.07x slower                                                                |
| regex_v8                   | 23.6 ms                                                      | 25.2 ms: 1.07x slower                                                               |
| go                         | 150 ms                                                       | 163 ms: 1.09x slower                                                                |
| richards                   | 45.7 ms                                                      | 50.6 ms: 1.11x slower                                                               |
| richards_super             | 51.3 ms                                                      | 57.1 ms: 1.11x slower                                                               |
| pyflate                    | 439 ms                                                       | 496 ms: 1.13x slower                                                                |
| python_startup             | 11.6 ms                                                      | 13.3 ms: 1.15x slower                                                               |
| telco                      | 6.96 ms                                                      | 8.01 ms: 1.15x slower                                                               |
| typing_runtime_protocols   | 152 us                                                       | 180 us: 1.19x slower                                                                |
| coverage                   | 66.7 ms                                                      | 80.3 ms: 1.20x slower                                                               |
| create_gc_cycles           | 1.59 ms                                                      | 1.99 ms: 1.25x slower                                                               |
| gc_traversal               | 3.48 ms                                                      | 4.44 ms: 1.28x slower                                                               |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                        |

Benchmark hidden because not significant (2): bench_mp_pool, xml_etree_iterparse
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240819-3.14.0a0-852115b/bm-20240819-pythonperf2-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-852115b.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 57.35% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x