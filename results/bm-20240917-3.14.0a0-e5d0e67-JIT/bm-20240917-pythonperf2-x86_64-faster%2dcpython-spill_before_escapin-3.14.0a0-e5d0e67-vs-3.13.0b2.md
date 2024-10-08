# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: spill_before_escapin
- machine: linux-x86_64
- commit hash: e5d0e67
- commit date: 2024-09-17
- overall geometric mean: 1.01x faster
- HPT reliability: 83.72%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67 |
|----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 310 ms: 1.06x slower                                                                  |
| docutils       | 2.98 sec                                                         | 3.17 sec: 1.06x slower                                                                |
| html5lib       | 74.7 ms                                                          | 72.0 ms: 1.04x faster                                                                 |
| tornado_http   | 119 ms                                                           | 122 ms: 1.02x slower                                                                  |
| Geometric mean | (ref)                                                            | 1.03x slower                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67 |
|----------------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 900 ms                                                           | 791 ms: 1.14x faster                                                                  |
| async_tree_memoization     | 460 ms                                                           | 406 ms: 1.13x faster                                                                  |
| async_tree_none            | 365 ms                                                           | 325 ms: 1.12x faster                                                                  |
| async_tree_none_tg         | 340 ms                                                           | 310 ms: 1.10x faster                                                                  |
| async_tree_memoization_tg  | 421 ms                                                           | 391 ms: 1.07x faster                                                                  |
| async_tree_io              | 873 ms                                                           | 814 ms: 1.07x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 549 ms: 1.04x faster                                                                  |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 579 ms: 1.04x faster                                                                  |
| Geometric mean             | (ref)                                                            | 1.09x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67 |
|----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 87.8 ms                                                          | 78.2 ms: 1.12x faster                                                                 |
| float          | 80.2 ms                                                          | 76.7 ms: 1.05x faster                                                                 |
| pidigits       | 254 ms                                                           | 250 ms: 1.01x faster                                                                  |
| Geometric mean | (ref)                                                            | 1.06x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67 |
|----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 252 ms: 1.01x slower                                                                  |
| regex_compile  | 144 ms                                                           | 148 ms: 1.03x slower                                                                  |
| regex_effbot   | 3.40 ms                                                          | 3.58 ms: 1.05x slower                                                                 |
| Geometric mean | (ref)                                                            | 1.03x slower                                                                          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67 |
|----------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.13 sec: 1.13x faster                                                                |
| xml_etree_process    | 59.7 ms                                                          | 55.8 ms: 1.07x faster                                                                 |
| xml_etree_generate   | 85.7 ms                                                          | 80.7 ms: 1.06x faster                                                                 |
| unpickle             | 15.7 us                                                          | 14.9 us: 1.05x faster                                                                 |
| xml_etree_iterparse  | 103 ms                                                           | 97.8 ms: 1.05x faster                                                                 |
| json_loads           | 25.0 us                                                          | 23.9 us: 1.05x faster                                                                 |
| unpickle_pure_python | 224 us                                                           | 215 us: 1.04x faster                                                                  |
| pickle_dict          | 32.8 us                                                          | 31.9 us: 1.03x faster                                                                 |
| json_dumps           | 10.8 ms                                                          | 10.5 ms: 1.03x faster                                                                 |
| xml_etree_parse      | 144 ms                                                           | 142 ms: 1.01x faster                                                                  |
| unpickle_list        | 4.70 us                                                          | 4.66 us: 1.01x faster                                                                 |
| pickle_list          | 4.44 us                                                          | 4.52 us: 1.02x slower                                                                 |
| pickle_pure_python   | 307 us                                                           | 325 us: 1.06x slower                                                                  |
| Geometric mean       | (ref)                                                            | 1.03x faster                                                                          |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67 |
|------------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                                 |
| python_startup_no_site | 8.85 ms                                                          | 8.99 ms: 1.02x slower                                                                 |
| Geometric mean         | (ref)                                                            | 1.01x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67 |
|-----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                          | 9.23 ms: 1.12x faster                                                                 |
| django_template | 39.0 ms                                                          | 43.6 ms: 1.12x slower                                                                 |
| genshi_xml      | 58.1 ms                                                          | 65.0 ms: 1.12x slower                                                                 |
| genshi_text     | 25.9 ms                                                          | 29.9 ms: 1.15x slower                                                                 |
| Geometric mean  | (ref)                                                            | 1.07x slower                                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67 |
|----------------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| deepcopy_memo              | 37.3 us                                                          | 28.3 us: 1.32x faster                                                                 |
| deepcopy                   | 377 us                                                           | 300 us: 1.26x faster                                                                  |
| richards                   | 53.4 ms                                                          | 42.8 ms: 1.25x faster                                                                 |
| richards_super             | 61.2 ms                                                          | 49.7 ms: 1.23x faster                                                                 |
| spectral_norm              | 97.3 ms                                                          | 80.4 ms: 1.21x faster                                                                 |
| scimark_sor                | 119 ms                                                           | 103 ms: 1.15x faster                                                                  |
| async_tree_io_tg           | 900 ms                                                           | 791 ms: 1.14x faster                                                                  |
| deepcopy_reduce            | 3.39 us                                                          | 2.99 us: 1.13x faster                                                                 |
| async_tree_memoization     | 460 ms                                                           | 406 ms: 1.13x faster                                                                  |
| tomli_loads                | 2.40 sec                                                         | 2.13 sec: 1.13x faster                                                                |
| async_tree_none            | 365 ms                                                           | 325 ms: 1.12x faster                                                                  |
| nbody                      | 87.8 ms                                                          | 78.2 ms: 1.12x faster                                                                 |
| mako                       | 10.4 ms                                                          | 9.23 ms: 1.12x faster                                                                 |
| async_tree_none_tg         | 340 ms                                                           | 310 ms: 1.10x faster                                                                  |
| go                         | 165 ms                                                           | 151 ms: 1.09x faster                                                                  |
| pathlib                    | 17.1 ms                                                          | 15.8 ms: 1.09x faster                                                                 |
| scimark_fft                | 312 ms                                                           | 288 ms: 1.08x faster                                                                  |
| gc_traversal               | 4.69 ms                                                          | 4.36 ms: 1.08x faster                                                                 |
| async_tree_memoization_tg  | 421 ms                                                           | 391 ms: 1.07x faster                                                                  |
| async_tree_io              | 873 ms                                                           | 814 ms: 1.07x faster                                                                  |
| xml_etree_process          | 59.7 ms                                                          | 55.8 ms: 1.07x faster                                                                 |
| bpe_tokeniser              | 5.14 sec                                                         | 4.80 sec: 1.07x faster                                                                |
| crypto_pyaes               | 73.6 ms                                                          | 68.8 ms: 1.07x faster                                                                 |
| xml_etree_generate         | 85.7 ms                                                          | 80.7 ms: 1.06x faster                                                                 |
| create_gc_cycles           | 2.00 ms                                                          | 1.89 ms: 1.06x faster                                                                 |
| deltablue                  | 3.37 ms                                                          | 3.19 ms: 1.06x faster                                                                 |
| unpickle                   | 15.7 us                                                          | 14.9 us: 1.05x faster                                                                 |
| telco                      | 8.40 ms                                                          | 8.01 ms: 1.05x faster                                                                 |
| xml_etree_iterparse        | 103 ms                                                           | 97.8 ms: 1.05x faster                                                                 |
| json_loads                 | 25.0 us                                                          | 23.9 us: 1.05x faster                                                                 |
| float                      | 80.2 ms                                                          | 76.7 ms: 1.05x faster                                                                 |
| unpickle_pure_python       | 224 us                                                           | 215 us: 1.04x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 549 ms: 1.04x faster                                                                  |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 579 ms: 1.04x faster                                                                  |
| html5lib                   | 74.7 ms                                                          | 72.0 ms: 1.04x faster                                                                 |
| sqlite_synth               | 2.80 us                                                          | 2.70 us: 1.04x faster                                                                 |
| dulwich_log                | 67.3 ms                                                          | 65.0 ms: 1.03x faster                                                                 |
| pickle_dict                | 32.8 us                                                          | 31.9 us: 1.03x faster                                                                 |
| json_dumps                 | 10.8 ms                                                          | 10.5 ms: 1.03x faster                                                                 |
| coverage                   | 83.5 ms                                                          | 81.2 ms: 1.03x faster                                                                 |
| json                       | 5.35 ms                                                          | 5.22 ms: 1.03x faster                                                                 |
| pprint_safe_repr           | 818 ms                                                           | 797 ms: 1.03x faster                                                                  |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.20 ms: 1.02x faster                                                                 |
| coroutines                 | 22.0 ms                                                          | 21.6 ms: 1.02x faster                                                                 |
| xml_etree_parse            | 144 ms                                                           | 142 ms: 1.01x faster                                                                  |
| pidigits                   | 254 ms                                                           | 250 ms: 1.01x faster                                                                  |
| scimark_lu                 | 97.5 ms                                                          | 96.3 ms: 1.01x faster                                                                 |
| pyflate                    | 482 ms                                                           | 476 ms: 1.01x faster                                                                  |
| unpickle_list              | 4.70 us                                                          | 4.66 us: 1.01x faster                                                                 |
| asyncio_tcp                | 378 ms                                                           | 376 ms: 1.01x faster                                                                  |
| regex_dna                  | 249 ms                                                           | 252 ms: 1.01x slower                                                                  |
| fannkuch                   | 353 ms                                                           | 357 ms: 1.01x slower                                                                  |
| meteor_contest             | 128 ms                                                           | 130 ms: 1.01x slower                                                                  |
| python_startup             | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                                 |
| thrift                     | 880 us                                                           | 892 us: 1.01x slower                                                                  |
| logging_format             | 7.11 us                                                          | 7.21 us: 1.01x slower                                                                 |
| python_startup_no_site     | 8.85 ms                                                          | 8.99 ms: 1.02x slower                                                                 |
| pickle_list                | 4.44 us                                                          | 4.52 us: 1.02x slower                                                                 |
| tornado_http               | 119 ms                                                           | 122 ms: 1.02x slower                                                                  |
| regex_compile              | 144 ms                                                           | 148 ms: 1.03x slower                                                                  |
| logging_simple             | 6.40 us                                                          | 6.60 us: 1.03x slower                                                                 |
| scimark_monte_carlo        | 65.5 ms                                                          | 67.7 ms: 1.03x slower                                                                 |
| pycparser                  | 1.22 sec                                                         | 1.27 sec: 1.04x slower                                                                |
| mdp                        | 2.46 sec                                                         | 2.55 sec: 1.04x slower                                                                |
| sympy_expand               | 501 ms                                                           | 525 ms: 1.05x slower                                                                  |
| regex_effbot               | 3.40 ms                                                          | 3.58 ms: 1.05x slower                                                                 |
| sqlglot_normalize          | 120 ms                                                           | 127 ms: 1.06x slower                                                                  |
| bench_mp_pool              | 4.91 ms                                                          | 5.19 ms: 1.06x slower                                                                 |
| pickle_pure_python         | 307 us                                                           | 325 us: 1.06x slower                                                                  |
| logging_silent             | 96.3 ns                                                          | 102 ns: 1.06x slower                                                                  |
| sympy_str                  | 295 ms                                                           | 313 ms: 1.06x slower                                                                  |
| 2to3                       | 291 ms                                                           | 310 ms: 1.06x slower                                                                  |
| async_generators           | 363 ms                                                           | 386 ms: 1.06x slower                                                                  |
| docutils                   | 2.98 sec                                                         | 3.17 sec: 1.06x slower                                                                |
| sqlglot_parse              | 1.39 ms                                                          | 1.49 ms: 1.07x slower                                                                 |
| comprehensions             | 17.0 us                                                          | 18.2 us: 1.07x slower                                                                 |
| typing_runtime_protocols   | 171 us                                                           | 184 us: 1.08x slower                                                                  |
| sqlglot_optimize           | 59.5 ms                                                          | 64.5 ms: 1.08x slower                                                                 |
| sympy_sum                  | 155 ms                                                           | 170 ms: 1.10x slower                                                                  |
| hexiom                     | 6.35 ms                                                          | 6.99 ms: 1.10x slower                                                                 |
| sqlglot_transpile          | 1.76 ms                                                          | 1.94 ms: 1.10x slower                                                                 |
| chaos                      | 59.6 ms                                                          | 66.4 ms: 1.11x slower                                                                 |
| generators                 | 33.5 ms                                                          | 37.3 ms: 1.11x slower                                                                 |
| django_template            | 39.0 ms                                                          | 43.6 ms: 1.12x slower                                                                 |
| genshi_xml                 | 58.1 ms                                                          | 65.0 ms: 1.12x slower                                                                 |
| nqueens                    | 88.4 ms                                                          | 101 ms: 1.14x slower                                                                  |
| sympy_integrate            | 23.2 ms                                                          | 26.7 ms: 1.15x slower                                                                 |
| genshi_text                | 25.9 ms                                                          | 29.9 ms: 1.15x slower                                                                 |
| pylint                     | 339 ms                                                           | 411 ms: 1.21x slower                                                                  |
| raytrace                   | 260 ms                                                           | 328 ms: 1.26x slower                                                                  |
| Geometric mean             | (ref)                                                            | 1.01x faster                                                                          |

Benchmark hidden because not significant (6): asyncio_websockets, pprint_pformat, pickle, asyncio_tcp_ssl, regex_v8, bench_thread_pool
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240917-3.14.0a0-e5d0e67-JIT/bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67.json: unpack_sequence

# HPT report

- Reliability score: 83.72% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x