# Results vs. 3.13.0

- fork: faster-cpython
- ref: variable_offset_inli
- machine: linux-x86_64
- commit hash: a3e6464
- commit date: 2024-08-20
- overall geometric mean: 1.02x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240820-pythonperf2-x86_64-faster%2dcpython-variable_offset_inli-3.14.0a0-a3e6464 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 288 ms: 1.01x faster                                                                  |
| docutils       | 2.81 sec                                                     | 2.94 sec: 1.05x slower                                                                |
| html5lib       | 71.9 ms                                                      | 73.8 ms: 1.03x slower                                                                 |
| tornado_http   | 120 ms                                                       | 118 ms: 1.01x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240820-pythonperf2-x86_64-faster%2dcpython-variable_offset_inli-3.14.0a0-a3e6464 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 393 ms: 1.17x faster                                                                  |
| async_tree_none            | 372 ms                                                       | 320 ms: 1.16x faster                                                                  |
| async_tree_memoization     | 452 ms                                                       | 399 ms: 1.13x faster                                                                  |
| async_tree_none_tg         | 340 ms                                                       | 311 ms: 1.09x faster                                                                  |
| async_tree_io              | 847 ms                                                       | 806 ms: 1.05x faster                                                                  |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 573 ms: 1.05x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 552 ms: 1.04x faster                                                                  |
| async_tree_io_tg           | 819 ms                                                       | 787 ms: 1.04x faster                                                                  |
| asyncio_tcp                | 380 ms                                                       | 368 ms: 1.03x faster                                                                  |
| coroutines                 | 21.6 ms                                                      | 21.4 ms: 1.01x faster                                                                 |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x faster                                                                |
| async_generators           | 359 ms                                                       | 368 ms: 1.03x slower                                                                  |
| Geometric mean             | (ref)                                                        | 1.06x faster                                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240820-pythonperf2-x86_64-faster%2dcpython-variable_offset_inli-3.14.0a0-a3e6464 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 79.7 ms: 1.03x faster                                                                 |
| pidigits       | 253 ms                                                       | 256 ms: 1.01x slower                                                                  |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240820-pythonperf2-x86_64-faster%2dcpython-variable_offset_inli-3.14.0a0-a3e6464 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 139 ms: 1.04x faster                                                                  |
| regex_effbot   | 3.37 ms                                                      | 3.52 ms: 1.05x slower                                                                 |
| regex_dna      | 244 ms                                                       | 255 ms: 1.05x slower                                                                  |
| regex_v8       | 26.2 ms                                                      | 27.6 ms: 1.05x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240820-pythonperf2-x86_64-faster%2dcpython-variable_offset_inli-3.14.0a0-a3e6464 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| tomli_loads          | 2.41 sec                                                     | 2.24 sec: 1.08x faster                                                                |
| xml_etree_process    | 60.9 ms                                                      | 58.4 ms: 1.04x faster                                                                 |
| json_dumps           | 11.0 ms                                                      | 10.7 ms: 1.03x faster                                                                 |
| xml_etree_generate   | 85.3 ms                                                      | 84.3 ms: 1.01x faster                                                                 |
| xml_etree_parse      | 145 ms                                                       | 144 ms: 1.01x faster                                                                  |
| unpickle_pure_python | 214 us                                                       | 218 us: 1.02x slower                                                                  |
| xml_etree_iterparse  | 100 ms                                                       | 103 ms: 1.03x slower                                                                  |
| json_loads           | 24.0 us                                                      | 25.0 us: 1.04x slower                                                                 |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                          |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240820-pythonperf2-x86_64-faster%2dcpython-variable_offset_inli-3.14.0a0-a3e6464 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                                 |
| python_startup_no_site | 8.94 ms                                                      | 9.07 ms: 1.01x slower                                                                 |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240820-pythonperf2-x86_64-faster%2dcpython-variable_offset_inli-3.14.0a0-a3e6464 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| genshi_xml      | 57.3 ms                                                      | 54.9 ms: 1.04x faster                                                                 |
| genshi_text     | 26.6 ms                                                      | 25.9 ms: 1.03x faster                                                                 |
| django_template | 38.9 ms                                                      | 39.4 ms: 1.01x slower                                                                 |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                                          |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240820-pythonperf2-x86_64-faster%2dcpython-variable_offset_inli-3.14.0a0-a3e6464 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| deepcopy                   | 397 us                                                       | 286 us: 1.39x faster                                                                  |
| deepcopy_memo              | 39.5 us                                                      | 29.2 us: 1.35x faster                                                                 |
| deepcopy_reduce            | 3.54 us                                                      | 2.91 us: 1.22x faster                                                                 |
| async_tree_memoization_tg  | 461 ms                                                       | 393 ms: 1.17x faster                                                                  |
| async_tree_none            | 372 ms                                                       | 320 ms: 1.16x faster                                                                  |
| async_tree_memoization     | 452 ms                                                       | 399 ms: 1.13x faster                                                                  |
| generators                 | 33.5 ms                                                      | 30.2 ms: 1.11x faster                                                                 |
| async_tree_none_tg         | 340 ms                                                       | 311 ms: 1.09x faster                                                                  |
| pathlib                    | 17.4 ms                                                      | 16.0 ms: 1.09x faster                                                                 |
| telco                      | 8.58 ms                                                      | 7.95 ms: 1.08x faster                                                                 |
| tomli_loads                | 2.41 sec                                                     | 2.24 sec: 1.08x faster                                                                |
| scimark_sor                | 126 ms                                                       | 117 ms: 1.08x faster                                                                  |
| richards_super             | 59.8 ms                                                      | 56.5 ms: 1.06x faster                                                                 |
| bench_thread_pool          | 901 us                                                       | 854 us: 1.06x faster                                                                  |
| richards                   | 52.7 ms                                                      | 50.1 ms: 1.05x faster                                                                 |
| async_tree_io              | 847 ms                                                       | 806 ms: 1.05x faster                                                                  |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 573 ms: 1.05x faster                                                                  |
| genshi_xml                 | 57.3 ms                                                      | 54.9 ms: 1.04x faster                                                                 |
| xml_etree_process          | 60.9 ms                                                      | 58.4 ms: 1.04x faster                                                                 |
| scimark_fft                | 314 ms                                                       | 301 ms: 1.04x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 552 ms: 1.04x faster                                                                  |
| async_tree_io_tg           | 819 ms                                                       | 787 ms: 1.04x faster                                                                  |
| bpe_tokeniser              | 5.10 sec                                                     | 4.92 sec: 1.04x faster                                                                |
| regex_compile              | 144 ms                                                       | 139 ms: 1.04x faster                                                                  |
| coverage                   | 81.1 ms                                                      | 78.4 ms: 1.03x faster                                                                 |
| fannkuch                   | 365 ms                                                       | 353 ms: 1.03x faster                                                                  |
| asyncio_tcp                | 380 ms                                                       | 368 ms: 1.03x faster                                                                  |
| genshi_text                | 26.6 ms                                                      | 25.9 ms: 1.03x faster                                                                 |
| float                      | 81.9 ms                                                      | 79.7 ms: 1.03x faster                                                                 |
| scimark_lu                 | 97.8 ms                                                      | 95.3 ms: 1.03x faster                                                                 |
| json_dumps                 | 11.0 ms                                                      | 10.7 ms: 1.03x faster                                                                 |
| pycparser                  | 1.26 sec                                                     | 1.23 sec: 1.02x faster                                                                |
| sympy_str                  | 296 ms                                                       | 290 ms: 1.02x faster                                                                  |
| meteor_contest             | 128 ms                                                       | 126 ms: 1.02x faster                                                                  |
| sqlglot_optimize           | 59.7 ms                                                      | 58.4 ms: 1.02x faster                                                                 |
| logging_format             | 7.07 us                                                      | 6.95 us: 1.02x faster                                                                 |
| sympy_integrate            | 23.3 ms                                                      | 22.9 ms: 1.02x faster                                                                 |
| thrift                     | 877 us                                                       | 864 us: 1.01x faster                                                                  |
| sympy_expand               | 505 ms                                                       | 497 ms: 1.01x faster                                                                  |
| spectral_norm              | 97.4 ms                                                      | 96.1 ms: 1.01x faster                                                                 |
| sympy_sum                  | 154 ms                                                       | 152 ms: 1.01x faster                                                                  |
| mdp                        | 2.52 sec                                                     | 2.49 sec: 1.01x faster                                                                |
| xml_etree_generate         | 85.3 ms                                                      | 84.3 ms: 1.01x faster                                                                 |
| tornado_http               | 120 ms                                                       | 118 ms: 1.01x faster                                                                  |
| pyflate                    | 492 ms                                                       | 487 ms: 1.01x faster                                                                  |
| sqlglot_transpile          | 1.78 ms                                                      | 1.76 ms: 1.01x faster                                                                 |
| coroutines                 | 21.6 ms                                                      | 21.4 ms: 1.01x faster                                                                 |
| xml_etree_parse            | 145 ms                                                       | 144 ms: 1.01x faster                                                                  |
| 2to3                       | 291 ms                                                       | 288 ms: 1.01x faster                                                                  |
| go                         | 160 ms                                                       | 160 ms: 1.00x faster                                                                  |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x faster                                                                |
| sqlglot_normalize          | 118 ms                                                       | 119 ms: 1.00x slower                                                                  |
| python_startup             | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                                 |
| nqueens                    | 88.2 ms                                                      | 88.6 ms: 1.00x slower                                                                 |
| sqlglot_parse              | 1.38 ms                                                      | 1.39 ms: 1.01x slower                                                                 |
| logging_simple             | 6.40 us                                                      | 6.44 us: 1.01x slower                                                                 |
| crypto_pyaes               | 72.8 ms                                                      | 73.6 ms: 1.01x slower                                                                 |
| pidigits                   | 253 ms                                                       | 256 ms: 1.01x slower                                                                  |
| python_startup_no_site     | 8.94 ms                                                      | 9.07 ms: 1.01x slower                                                                 |
| django_template            | 38.9 ms                                                      | 39.4 ms: 1.01x slower                                                                 |
| deltablue                  | 3.41 ms                                                      | 3.46 ms: 1.01x slower                                                                 |
| unpickle_pure_python       | 214 us                                                       | 218 us: 1.02x slower                                                                  |
| json                       | 5.22 ms                                                      | 5.34 ms: 1.02x slower                                                                 |
| async_generators           | 359 ms                                                       | 368 ms: 1.03x slower                                                                  |
| html5lib                   | 71.9 ms                                                      | 73.8 ms: 1.03x slower                                                                 |
| pprint_safe_repr           | 812 ms                                                       | 834 ms: 1.03x slower                                                                  |
| xml_etree_iterparse        | 100 ms                                                       | 103 ms: 1.03x slower                                                                  |
| pprint_pformat             | 1.65 sec                                                     | 1.70 sec: 1.03x slower                                                                |
| chaos                      | 61.7 ms                                                      | 63.8 ms: 1.03x slower                                                                 |
| json_loads                 | 24.0 us                                                      | 25.0 us: 1.04x slower                                                                 |
| regex_effbot               | 3.37 ms                                                      | 3.52 ms: 1.05x slower                                                                 |
| regex_dna                  | 244 ms                                                       | 255 ms: 1.05x slower                                                                  |
| docutils                   | 2.81 sec                                                     | 2.94 sec: 1.05x slower                                                                |
| scimark_monte_carlo        | 64.9 ms                                                      | 68.2 ms: 1.05x slower                                                                 |
| regex_v8                   | 26.2 ms                                                      | 27.6 ms: 1.05x slower                                                                 |
| logging_silent             | 97.7 ns                                                      | 103 ns: 1.06x slower                                                                  |
| gc_traversal               | 4.11 ms                                                      | 4.58 ms: 1.11x slower                                                                 |
| create_gc_cycles           | 1.76 ms                                                      | 2.05 ms: 1.17x slower                                                                 |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                          |

Benchmark hidden because not significant (11): bench_mp_pool, typing_runtime_protocols, nbody, scimark_sparse_mat_mult, mako, pickle_pure_python, comprehensions, hexiom, asyncio_websockets, raytrace, pylint
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x