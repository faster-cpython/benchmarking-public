# Results vs. 3.13.0

- fork: faster-cpython
- ref: spill_before_escapin
- machine: linux-x86_64
- commit hash: e5d0e67
- commit date: 2024-09-17
- overall geometric mean: 1.00x faster
- HPT reliability: 73.67%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 310 ms: 1.07x slower                                                                  |
| docutils       | 2.81 sec                                                     | 3.17 sec: 1.13x slower                                                                |
| tornado_http   | 120 ms                                                       | 122 ms: 1.02x slower                                                                  |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 391 ms: 1.18x faster                                                                  |
| async_tree_none            | 372 ms                                                       | 325 ms: 1.14x faster                                                                  |
| async_tree_memoization     | 452 ms                                                       | 406 ms: 1.11x faster                                                                  |
| async_tree_none_tg         | 340 ms                                                       | 310 ms: 1.10x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 549 ms: 1.05x faster                                                                  |
| async_tree_io              | 847 ms                                                       | 814 ms: 1.04x faster                                                                  |
| async_tree_io_tg           | 819 ms                                                       | 791 ms: 1.04x faster                                                                  |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 579 ms: 1.04x faster                                                                  |
| asyncio_tcp                | 380 ms                                                       | 376 ms: 1.01x faster                                                                  |
| asyncio_websockets         | 382 ms                                                       | 393 ms: 1.03x slower                                                                  |
| async_generators           | 359 ms                                                       | 386 ms: 1.07x slower                                                                  |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                                          |

Benchmark hidden because not significant (2): asyncio_tcp_ssl, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 78.2 ms: 1.13x faster                                                                 |
| float          | 81.9 ms                                                      | 76.7 ms: 1.07x faster                                                                 |
| pidigits       | 253 ms                                                       | 250 ms: 1.01x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 148 ms: 1.02x slower                                                                  |
| regex_dna      | 244 ms                                                       | 252 ms: 1.04x slower                                                                  |
| regex_effbot   | 3.37 ms                                                      | 3.58 ms: 1.06x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| tomli_loads          | 2.41 sec                                                     | 2.13 sec: 1.13x faster                                                                |
| xml_etree_process    | 60.9 ms                                                      | 55.8 ms: 1.09x faster                                                                 |
| xml_etree_generate   | 85.3 ms                                                      | 80.7 ms: 1.06x faster                                                                 |
| json_dumps           | 11.0 ms                                                      | 10.5 ms: 1.05x faster                                                                 |
| xml_etree_iterparse  | 100 ms                                                       | 97.8 ms: 1.02x faster                                                                 |
| xml_etree_parse      | 145 ms                                                       | 142 ms: 1.02x faster                                                                  |
| unpickle             | 15.1 us                                                      | 14.9 us: 1.02x faster                                                                 |
| pickle_list          | 4.59 us                                                      | 4.52 us: 1.01x faster                                                                 |
| pickle_dict          | 32.1 us                                                      | 31.9 us: 1.00x faster                                                                 |
| unpickle_pure_python | 214 us                                                       | 215 us: 1.00x slower                                                                  |
| pickle               | 10.5 us                                                      | 10.6 us: 1.01x slower                                                                 |
| unpickle_list        | 4.62 us                                                      | 4.66 us: 1.01x slower                                                                 |
| pickle_pure_python   | 318 us                                                       | 325 us: 1.02x slower                                                                  |
| Geometric mean       | (ref)                                                        | 1.03x faster                                                                          |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                                 |
| python_startup_no_site | 8.94 ms                                                      | 8.99 ms: 1.01x slower                                                                 |
| Geometric mean         | (ref)                                                        | 1.00x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                      | 9.23 ms: 1.13x faster                                                                 |
| django_template | 38.9 ms                                                      | 43.6 ms: 1.12x slower                                                                 |
| genshi_text     | 26.6 ms                                                      | 29.9 ms: 1.12x slower                                                                 |
| genshi_xml      | 57.3 ms                                                      | 65.0 ms: 1.13x slower                                                                 |
| Geometric mean  | (ref)                                                        | 1.06x slower                                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| deepcopy_memo              | 39.5 us                                                      | 28.3 us: 1.39x faster                                                                 |
| deepcopy                   | 397 us                                                       | 300 us: 1.33x faster                                                                  |
| richards                   | 52.7 ms                                                      | 42.8 ms: 1.23x faster                                                                 |
| scimark_sor                | 126 ms                                                       | 103 ms: 1.22x faster                                                                  |
| spectral_norm              | 97.4 ms                                                      | 80.4 ms: 1.21x faster                                                                 |
| richards_super             | 59.8 ms                                                      | 49.7 ms: 1.20x faster                                                                 |
| deepcopy_reduce            | 3.54 us                                                      | 2.99 us: 1.18x faster                                                                 |
| async_tree_memoization_tg  | 461 ms                                                       | 391 ms: 1.18x faster                                                                  |
| async_tree_none            | 372 ms                                                       | 325 ms: 1.14x faster                                                                  |
| tomli_loads                | 2.41 sec                                                     | 2.13 sec: 1.13x faster                                                                |
| mako                       | 10.4 ms                                                      | 9.23 ms: 1.13x faster                                                                 |
| nbody                      | 88.0 ms                                                      | 78.2 ms: 1.13x faster                                                                 |
| async_tree_memoization     | 452 ms                                                       | 406 ms: 1.11x faster                                                                  |
| pathlib                    | 17.4 ms                                                      | 15.8 ms: 1.10x faster                                                                 |
| async_tree_none_tg         | 340 ms                                                       | 310 ms: 1.10x faster                                                                  |
| xml_etree_process          | 60.9 ms                                                      | 55.8 ms: 1.09x faster                                                                 |
| scimark_fft                | 314 ms                                                       | 288 ms: 1.09x faster                                                                  |
| telco                      | 8.58 ms                                                      | 8.01 ms: 1.07x faster                                                                 |
| deltablue                  | 3.41 ms                                                      | 3.19 ms: 1.07x faster                                                                 |
| float                      | 81.9 ms                                                      | 76.7 ms: 1.07x faster                                                                 |
| bpe_tokeniser              | 5.10 sec                                                     | 4.80 sec: 1.06x faster                                                                |
| go                         | 160 ms                                                       | 151 ms: 1.06x faster                                                                  |
| xml_etree_generate         | 85.3 ms                                                      | 80.7 ms: 1.06x faster                                                                 |
| crypto_pyaes               | 72.8 ms                                                      | 68.8 ms: 1.06x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 549 ms: 1.05x faster                                                                  |
| json_dumps                 | 11.0 ms                                                      | 10.5 ms: 1.05x faster                                                                 |
| async_tree_io              | 847 ms                                                       | 814 ms: 1.04x faster                                                                  |
| async_tree_io_tg           | 819 ms                                                       | 791 ms: 1.04x faster                                                                  |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 579 ms: 1.04x faster                                                                  |
| pyflate                    | 492 ms                                                       | 476 ms: 1.03x faster                                                                  |
| sqlite_synth               | 2.79 us                                                      | 2.70 us: 1.03x faster                                                                 |
| xml_etree_iterparse        | 100 ms                                                       | 97.8 ms: 1.02x faster                                                                 |
| xml_etree_parse            | 145 ms                                                       | 142 ms: 1.02x faster                                                                  |
| fannkuch                   | 365 ms                                                       | 357 ms: 1.02x faster                                                                  |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.20 ms: 1.02x faster                                                                 |
| unpickle                   | 15.1 us                                                      | 14.9 us: 1.02x faster                                                                 |
| pprint_safe_repr           | 812 ms                                                       | 797 ms: 1.02x faster                                                                  |
| scimark_lu                 | 97.8 ms                                                      | 96.3 ms: 1.02x faster                                                                 |
| pickle_list                | 4.59 us                                                      | 4.52 us: 1.01x faster                                                                 |
| asyncio_tcp                | 380 ms                                                       | 376 ms: 1.01x faster                                                                  |
| pidigits                   | 253 ms                                                       | 250 ms: 1.01x faster                                                                  |
| dulwich_log                | 65.5 ms                                                      | 65.0 ms: 1.01x faster                                                                 |
| pickle_dict                | 32.1 us                                                      | 31.9 us: 1.00x faster                                                                 |
| unpickle_pure_python       | 214 us                                                       | 215 us: 1.00x slower                                                                  |
| pprint_pformat             | 1.65 sec                                                     | 1.66 sec: 1.00x slower                                                                |
| python_startup             | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                                 |
| python_startup_no_site     | 8.94 ms                                                      | 8.99 ms: 1.01x slower                                                                 |
| pickle                     | 10.5 us                                                      | 10.6 us: 1.01x slower                                                                 |
| unpickle_list              | 4.62 us                                                      | 4.66 us: 1.01x slower                                                                 |
| pycparser                  | 1.26 sec                                                     | 1.27 sec: 1.01x slower                                                                |
| meteor_contest             | 128 ms                                                       | 130 ms: 1.01x slower                                                                  |
| mdp                        | 2.52 sec                                                     | 2.55 sec: 1.01x slower                                                                |
| thrift                     | 877 us                                                       | 892 us: 1.02x slower                                                                  |
| logging_format             | 7.07 us                                                      | 7.21 us: 1.02x slower                                                                 |
| tornado_http               | 120 ms                                                       | 122 ms: 1.02x slower                                                                  |
| pickle_pure_python         | 318 us                                                       | 325 us: 1.02x slower                                                                  |
| regex_compile              | 144 ms                                                       | 148 ms: 1.02x slower                                                                  |
| bench_thread_pool          | 901 us                                                       | 924 us: 1.02x slower                                                                  |
| asyncio_websockets         | 382 ms                                                       | 393 ms: 1.03x slower                                                                  |
| logging_simple             | 6.40 us                                                      | 6.60 us: 1.03x slower                                                                 |
| regex_dna                  | 244 ms                                                       | 252 ms: 1.04x slower                                                                  |
| sympy_expand               | 505 ms                                                       | 525 ms: 1.04x slower                                                                  |
| scimark_monte_carlo        | 64.9 ms                                                      | 67.7 ms: 1.04x slower                                                                 |
| logging_silent             | 97.7 ns                                                      | 102 ns: 1.05x slower                                                                  |
| comprehensions             | 17.3 us                                                      | 18.2 us: 1.05x slower                                                                 |
| typing_runtime_protocols   | 174 us                                                       | 184 us: 1.06x slower                                                                  |
| sympy_str                  | 296 ms                                                       | 313 ms: 1.06x slower                                                                  |
| gc_traversal               | 4.11 ms                                                      | 4.36 ms: 1.06x slower                                                                 |
| regex_effbot               | 3.37 ms                                                      | 3.58 ms: 1.06x slower                                                                 |
| 2to3                       | 291 ms                                                       | 310 ms: 1.07x slower                                                                  |
| sqlglot_normalize          | 118 ms                                                       | 127 ms: 1.07x slower                                                                  |
| create_gc_cycles           | 1.76 ms                                                      | 1.89 ms: 1.07x slower                                                                 |
| async_generators           | 359 ms                                                       | 386 ms: 1.07x slower                                                                  |
| chaos                      | 61.7 ms                                                      | 66.4 ms: 1.08x slower                                                                 |
| sqlglot_parse              | 1.38 ms                                                      | 1.49 ms: 1.08x slower                                                                 |
| sqlglot_optimize           | 59.7 ms                                                      | 64.5 ms: 1.08x slower                                                                 |
| sqlglot_transpile          | 1.78 ms                                                      | 1.94 ms: 1.09x slower                                                                 |
| hexiom                     | 6.33 ms                                                      | 6.99 ms: 1.10x slower                                                                 |
| sympy_sum                  | 154 ms                                                       | 170 ms: 1.10x slower                                                                  |
| bench_mp_pool              | 4.65 ms                                                      | 5.19 ms: 1.11x slower                                                                 |
| generators                 | 33.5 ms                                                      | 37.3 ms: 1.12x slower                                                                 |
| django_template            | 38.9 ms                                                      | 43.6 ms: 1.12x slower                                                                 |
| genshi_text                | 26.6 ms                                                      | 29.9 ms: 1.12x slower                                                                 |
| docutils                   | 2.81 sec                                                     | 3.17 sec: 1.13x slower                                                                |
| genshi_xml                 | 57.3 ms                                                      | 65.0 ms: 1.13x slower                                                                 |
| raytrace                   | 289 ms                                                       | 328 ms: 1.13x slower                                                                  |
| nqueens                    | 88.2 ms                                                      | 101 ms: 1.14x slower                                                                  |
| sympy_integrate            | 23.3 ms                                                      | 26.7 ms: 1.15x slower                                                                 |
| pylint                     | 346 ms                                                       | 411 ms: 1.19x slower                                                                  |
| unpack_sequence            | 56.8 ns                                                      | 88.0 ns: 1.55x slower                                                                 |
| Geometric mean             | (ref)                                                        | 1.00x faster                                                                          |

Benchmark hidden because not significant (7): json_loads, json, asyncio_tcp_ssl, coverage, regex_v8, html5lib, coroutines
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 73.67% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x