# Results vs. 3.13.0

- fork: faster-cpython
- ref: specialize_call_ex
- machine: linux-x86_64
- commit hash: 852115b
- commit date: 2024-08-19
- overall geometric mean: 1.02x faster
- HPT reliability: 99.87%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240819-pythonperf2-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-852115b |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 289 ms: 1.00x faster                                                                |
| docutils       | 2.81 sec                                                     | 2.99 sec: 1.06x slower                                                              |
| html5lib       | 71.9 ms                                                      | 75.4 ms: 1.05x slower                                                               |
| tornado_http   | 120 ms                                                       | 118 ms: 1.01x faster                                                                |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240819-pythonperf2-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-852115b |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 382 ms: 1.21x faster                                                                |
| async_tree_none_tg         | 340 ms                                                       | 300 ms: 1.13x faster                                                                |
| async_tree_memoization     | 452 ms                                                       | 403 ms: 1.12x faster                                                                |
| async_tree_none            | 372 ms                                                       | 333 ms: 1.12x faster                                                                |
| async_tree_io_tg           | 819 ms                                                       | 764 ms: 1.07x faster                                                                |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 537 ms: 1.07x faster                                                                |
| async_tree_io              | 847 ms                                                       | 798 ms: 1.06x faster                                                                |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 574 ms: 1.04x faster                                                                |
| asyncio_tcp                | 380 ms                                                       | 376 ms: 1.01x faster                                                                |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x faster                                                              |
| coroutines                 | 21.6 ms                                                      | 21.8 ms: 1.01x slower                                                               |
| asyncio_websockets         | 382 ms                                                       | 390 ms: 1.02x slower                                                                |
| async_generators           | 359 ms                                                       | 368 ms: 1.03x slower                                                                |
| Geometric mean             | (ref)                                                        | 1.06x faster                                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240819-pythonperf2-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-852115b |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 85.4 ms: 1.03x faster                                                               |
| float          | 81.9 ms                                                      | 80.1 ms: 1.02x faster                                                               |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                        |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240819-pythonperf2-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-852115b |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                      | 25.2 ms: 1.04x faster                                                               |
| regex_compile  | 144 ms                                                       | 140 ms: 1.03x faster                                                                |
| regex_dna      | 244 ms                                                       | 239 ms: 1.02x faster                                                                |
| regex_effbot   | 3.37 ms                                                      | 3.66 ms: 1.09x slower                                                               |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240819-pythonperf2-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-852115b |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| tomli_loads          | 2.41 sec                                                     | 2.28 sec: 1.06x faster                                                              |
| json_dumps           | 11.0 ms                                                      | 10.6 ms: 1.04x faster                                                               |
| xml_etree_process    | 60.9 ms                                                      | 58.7 ms: 1.04x faster                                                               |
| xml_etree_parse      | 145 ms                                                       | 143 ms: 1.02x faster                                                                |
| xml_etree_generate   | 85.3 ms                                                      | 84.2 ms: 1.01x faster                                                               |
| unpickle_pure_python | 214 us                                                       | 213 us: 1.00x faster                                                                |
| xml_etree_iterparse  | 100 ms                                                       | 102 ms: 1.02x slower                                                                |
| json_loads           | 24.0 us                                                      | 25.0 us: 1.04x slower                                                               |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                        |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240819-pythonperf2-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-852115b |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 13.3 ms: 1.00x slower                                                               |
| python_startup_no_site | 8.94 ms                                                      | 9.03 ms: 1.01x slower                                                               |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240819-pythonperf2-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-852115b |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| genshi_xml      | 57.3 ms                                                      | 55.1 ms: 1.04x faster                                                               |
| genshi_text     | 26.6 ms                                                      | 25.7 ms: 1.04x faster                                                               |
| django_template | 38.9 ms                                                      | 39.6 ms: 1.02x slower                                                               |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                                        |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240819-pythonperf2-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-852115b |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| deepcopy                   | 397 us                                                       | 284 us: 1.40x faster                                                                |
| deepcopy_memo              | 39.5 us                                                      | 29.6 us: 1.33x faster                                                               |
| deepcopy_reduce            | 3.54 us                                                      | 2.87 us: 1.23x faster                                                               |
| async_tree_memoization_tg  | 461 ms                                                       | 382 ms: 1.21x faster                                                                |
| generators                 | 33.5 ms                                                      | 29.1 ms: 1.15x faster                                                               |
| async_tree_none_tg         | 340 ms                                                       | 300 ms: 1.13x faster                                                                |
| async_tree_memoization     | 452 ms                                                       | 403 ms: 1.12x faster                                                                |
| async_tree_none            | 372 ms                                                       | 333 ms: 1.12x faster                                                                |
| raytrace                   | 289 ms                                                       | 263 ms: 1.10x faster                                                                |
| pathlib                    | 17.4 ms                                                      | 16.1 ms: 1.08x faster                                                               |
| scimark_sor                | 126 ms                                                       | 116 ms: 1.08x faster                                                                |
| telco                      | 8.58 ms                                                      | 8.01 ms: 1.07x faster                                                               |
| async_tree_io_tg           | 819 ms                                                       | 764 ms: 1.07x faster                                                                |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 537 ms: 1.07x faster                                                                |
| async_tree_io              | 847 ms                                                       | 798 ms: 1.06x faster                                                                |
| tomli_loads                | 2.41 sec                                                     | 2.28 sec: 1.06x faster                                                              |
| richards_super             | 59.8 ms                                                      | 57.1 ms: 1.05x faster                                                               |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 574 ms: 1.04x faster                                                                |
| richards                   | 52.7 ms                                                      | 50.6 ms: 1.04x faster                                                               |
| genshi_xml                 | 57.3 ms                                                      | 55.1 ms: 1.04x faster                                                               |
| regex_v8                   | 26.2 ms                                                      | 25.2 ms: 1.04x faster                                                               |
| bench_thread_pool          | 901 us                                                       | 869 us: 1.04x faster                                                                |
| json_dumps                 | 11.0 ms                                                      | 10.6 ms: 1.04x faster                                                               |
| xml_etree_process          | 60.9 ms                                                      | 58.7 ms: 1.04x faster                                                               |
| genshi_text                | 26.6 ms                                                      | 25.7 ms: 1.04x faster                                                               |
| nbody                      | 88.0 ms                                                      | 85.4 ms: 1.03x faster                                                               |
| scimark_fft                | 314 ms                                                       | 305 ms: 1.03x faster                                                                |
| regex_compile              | 144 ms                                                       | 140 ms: 1.03x faster                                                                |
| meteor_contest             | 128 ms                                                       | 125 ms: 1.02x faster                                                                |
| float                      | 81.9 ms                                                      | 80.1 ms: 1.02x faster                                                               |
| scimark_lu                 | 97.8 ms                                                      | 95.8 ms: 1.02x faster                                                               |
| bpe_tokeniser              | 5.10 sec                                                     | 5.00 sec: 1.02x faster                                                              |
| spectral_norm              | 97.4 ms                                                      | 95.6 ms: 1.02x faster                                                               |
| fannkuch                   | 365 ms                                                       | 358 ms: 1.02x faster                                                                |
| regex_dna                  | 244 ms                                                       | 239 ms: 1.02x faster                                                                |
| xml_etree_parse            | 145 ms                                                       | 143 ms: 1.02x faster                                                                |
| sqlglot_optimize           | 59.7 ms                                                      | 58.7 ms: 1.02x faster                                                               |
| hexiom                     | 6.33 ms                                                      | 6.23 ms: 1.02x faster                                                               |
| xml_etree_generate         | 85.3 ms                                                      | 84.2 ms: 1.01x faster                                                               |
| tornado_http               | 120 ms                                                       | 118 ms: 1.01x faster                                                                |
| asyncio_tcp                | 380 ms                                                       | 376 ms: 1.01x faster                                                                |
| coverage                   | 81.1 ms                                                      | 80.3 ms: 1.01x faster                                                               |
| unpickle_pure_python       | 214 us                                                       | 213 us: 1.00x faster                                                                |
| 2to3                       | 291 ms                                                       | 289 ms: 1.00x faster                                                                |
| mdp                        | 2.52 sec                                                     | 2.51 sec: 1.00x faster                                                              |
| sympy_integrate            | 23.3 ms                                                      | 23.2 ms: 1.00x faster                                                               |
| scimark_monte_carlo        | 64.9 ms                                                      | 64.7 ms: 1.00x faster                                                               |
| sympy_expand               | 505 ms                                                       | 503 ms: 1.00x faster                                                                |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x faster                                                              |
| python_startup             | 13.3 ms                                                      | 13.3 ms: 1.00x slower                                                               |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.30 ms: 1.00x slower                                                               |
| sympy_str                  | 296 ms                                                       | 297 ms: 1.00x slower                                                                |
| coroutines                 | 21.6 ms                                                      | 21.8 ms: 1.01x slower                                                               |
| pyflate                    | 492 ms                                                       | 496 ms: 1.01x slower                                                                |
| crypto_pyaes               | 72.8 ms                                                      | 73.3 ms: 1.01x slower                                                               |
| sqlglot_transpile          | 1.78 ms                                                      | 1.80 ms: 1.01x slower                                                               |
| python_startup_no_site     | 8.94 ms                                                      | 9.03 ms: 1.01x slower                                                               |
| sympy_sum                  | 154 ms                                                       | 155 ms: 1.01x slower                                                                |
| thrift                     | 877 us                                                       | 888 us: 1.01x slower                                                                |
| go                         | 160 ms                                                       | 163 ms: 1.02x slower                                                                |
| pprint_safe_repr           | 812 ms                                                       | 827 ms: 1.02x slower                                                                |
| django_template            | 38.9 ms                                                      | 39.6 ms: 1.02x slower                                                               |
| xml_etree_iterparse        | 100 ms                                                       | 102 ms: 1.02x slower                                                                |
| asyncio_websockets         | 382 ms                                                       | 390 ms: 1.02x slower                                                                |
| pprint_pformat             | 1.65 sec                                                     | 1.69 sec: 1.02x slower                                                              |
| async_generators           | 359 ms                                                       | 368 ms: 1.03x slower                                                                |
| json                       | 5.22 ms                                                      | 5.37 ms: 1.03x slower                                                               |
| nqueens                    | 88.2 ms                                                      | 90.9 ms: 1.03x slower                                                               |
| typing_runtime_protocols   | 174 us                                                       | 180 us: 1.03x slower                                                                |
| sqlglot_parse              | 1.38 ms                                                      | 1.43 ms: 1.04x slower                                                               |
| json_loads                 | 24.0 us                                                      | 25.0 us: 1.04x slower                                                               |
| html5lib                   | 71.9 ms                                                      | 75.4 ms: 1.05x slower                                                               |
| docutils                   | 2.81 sec                                                     | 2.99 sec: 1.06x slower                                                              |
| gc_traversal               | 4.11 ms                                                      | 4.44 ms: 1.08x slower                                                               |
| regex_effbot               | 3.37 ms                                                      | 3.66 ms: 1.09x slower                                                               |
| create_gc_cycles           | 1.76 ms                                                      | 1.99 ms: 1.13x slower                                                               |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                        |

Benchmark hidden because not significant (13): bench_mp_pool, pycparser, pickle_pure_python, logging_silent, pidigits, mako, sqlglot_normalize, deltablue, comprehensions, chaos, logging_format, logging_simple, pylint
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.87% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x