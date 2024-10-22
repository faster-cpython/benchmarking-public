# Results vs. 3.13.0

- fork: mdboom
- ref: pysequence_tuple
- machine: linux-x86_64
- commit hash: 3b5fdc8
- commit date: 2024-09-11
- overall geometric mean: 1.02x faster
- HPT reliability: 99.80%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 287 ms: 1.01x faster                                                    |
| docutils       | 2.81 sec                                                     | 2.91 sec: 1.03x slower                                                  |
| html5lib       | 71.9 ms                                                      | 72.9 ms: 1.01x slower                                                   |
| tornado_http   | 120 ms                                                       | 118 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                        | 1.00x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 392 ms: 1.18x faster                                                    |
| async_tree_none            | 372 ms                                                       | 326 ms: 1.14x faster                                                    |
| async_tree_memoization     | 452 ms                                                       | 403 ms: 1.12x faster                                                    |
| async_tree_none_tg         | 340 ms                                                       | 312 ms: 1.09x faster                                                    |
| async_tree_io              | 847 ms                                                       | 807 ms: 1.05x faster                                                    |
| async_tree_io_tg           | 819 ms                                                       | 784 ms: 1.04x faster                                                    |
| asyncio_tcp                | 380 ms                                                       | 367 ms: 1.03x faster                                                    |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 580 ms: 1.03x faster                                                    |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 570 ms: 1.01x faster                                                    |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x faster                                                  |
| asyncio_websockets         | 382 ms                                                       | 392 ms: 1.03x slower                                                    |
| coroutines                 | 21.6 ms                                                      | 22.3 ms: 1.03x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                            |

Benchmark hidden because not significant (1): async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 85.3 ms: 1.03x faster                                                   |
| float          | 81.9 ms                                                      | 80.4 ms: 1.02x faster                                                   |
| pidigits       | 253 ms                                                       | 254 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 140 ms: 1.03x faster                                                    |
| regex_v8       | 26.2 ms                                                      | 25.8 ms: 1.01x faster                                                   |
| regex_dna      | 244 ms                                                       | 240 ms: 1.01x faster                                                    |
| regex_effbot   | 3.37 ms                                                      | 3.46 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_list          | 4.59 us                                                      | 4.13 us: 1.11x faster                                                   |
| pickle_dict          | 32.1 us                                                      | 29.8 us: 1.08x faster                                                   |
| pickle               | 10.5 us                                                      | 10.2 us: 1.04x faster                                                   |
| xml_etree_process    | 60.9 ms                                                      | 59.2 ms: 1.03x faster                                                   |
| pickle_pure_python   | 318 us                                                       | 315 us: 1.01x faster                                                    |
| xml_etree_parse      | 145 ms                                                       | 143 ms: 1.01x faster                                                    |
| unpickle_list        | 4.62 us                                                      | 4.66 us: 1.01x slower                                                   |
| json_dumps           | 11.0 ms                                                      | 11.1 ms: 1.01x slower                                                   |
| xml_etree_iterparse  | 100 ms                                                       | 101 ms: 1.01x slower                                                    |
| unpickle             | 15.1 us                                                      | 15.5 us: 1.02x slower                                                   |
| json_loads           | 24.0 us                                                      | 24.9 us: 1.04x slower                                                   |
| unpickle_pure_python | 214 us                                                       | 226 us: 1.05x slower                                                    |
| tomli_loads          | 2.41 sec                                                     | 2.56 sec: 1.07x slower                                                  |
| Geometric mean       | (ref)                                                        | 1.00x faster                                                            |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.94 ms                                                      | 8.95 ms: 1.00x slower                                                   |
| python_startup         | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.00x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 57.3 ms                                                      | 54.2 ms: 1.06x faster                                                   |
| genshi_text     | 26.6 ms                                                      | 25.2 ms: 1.06x faster                                                   |
| django_template | 38.9 ms                                                      | 41.3 ms: 1.06x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                   | 397 us                                                       | 287 us: 1.38x faster                                                    |
| deepcopy_memo              | 39.5 us                                                      | 29.7 us: 1.33x faster                                                   |
| deepcopy_reduce            | 3.54 us                                                      | 2.87 us: 1.23x faster                                                   |
| async_tree_memoization_tg  | 461 ms                                                       | 392 ms: 1.18x faster                                                    |
| go                         | 160 ms                                                       | 139 ms: 1.16x faster                                                    |
| unpack_sequence            | 56.8 ns                                                      | 49.4 ns: 1.15x faster                                                   |
| async_tree_none            | 372 ms                                                       | 326 ms: 1.14x faster                                                    |
| generators                 | 33.5 ms                                                      | 29.7 ms: 1.13x faster                                                   |
| async_tree_memoization     | 452 ms                                                       | 403 ms: 1.12x faster                                                    |
| pathlib                    | 17.4 ms                                                      | 15.6 ms: 1.11x faster                                                   |
| pickle_list                | 4.59 us                                                      | 4.13 us: 1.11x faster                                                   |
| async_tree_none_tg         | 340 ms                                                       | 312 ms: 1.09x faster                                                    |
| pickle_dict                | 32.1 us                                                      | 29.8 us: 1.08x faster                                                   |
| scimark_sor                | 126 ms                                                       | 118 ms: 1.06x faster                                                    |
| genshi_xml                 | 57.3 ms                                                      | 54.2 ms: 1.06x faster                                                   |
| genshi_text                | 26.6 ms                                                      | 25.2 ms: 1.06x faster                                                   |
| bench_thread_pool          | 901 us                                                       | 859 us: 1.05x faster                                                    |
| async_tree_io              | 847 ms                                                       | 807 ms: 1.05x faster                                                    |
| coverage                   | 81.1 ms                                                      | 77.4 ms: 1.05x faster                                                   |
| async_tree_io_tg           | 819 ms                                                       | 784 ms: 1.04x faster                                                    |
| raytrace                   | 289 ms                                                       | 278 ms: 1.04x faster                                                    |
| pickle                     | 10.5 us                                                      | 10.2 us: 1.04x faster                                                   |
| asyncio_tcp                | 380 ms                                                       | 367 ms: 1.03x faster                                                    |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 580 ms: 1.03x faster                                                    |
| richards_super             | 59.8 ms                                                      | 57.9 ms: 1.03x faster                                                   |
| regex_compile              | 144 ms                                                       | 140 ms: 1.03x faster                                                    |
| nbody                      | 88.0 ms                                                      | 85.3 ms: 1.03x faster                                                   |
| scimark_fft                | 314 ms                                                       | 305 ms: 1.03x faster                                                    |
| xml_etree_process          | 60.9 ms                                                      | 59.2 ms: 1.03x faster                                                   |
| telco                      | 8.58 ms                                                      | 8.35 ms: 1.03x faster                                                   |
| bpe_tokeniser              | 5.10 sec                                                     | 4.97 sec: 1.03x faster                                                  |
| sqlglot_optimize           | 59.7 ms                                                      | 58.5 ms: 1.02x faster                                                   |
| float                      | 81.9 ms                                                      | 80.4 ms: 1.02x faster                                                   |
| pyflate                    | 492 ms                                                       | 484 ms: 1.02x faster                                                    |
| 2to3                       | 291 ms                                                       | 287 ms: 1.01x faster                                                    |
| regex_v8                   | 26.2 ms                                                      | 25.8 ms: 1.01x faster                                                   |
| richards                   | 52.7 ms                                                      | 52.0 ms: 1.01x faster                                                   |
| regex_dna                  | 244 ms                                                       | 240 ms: 1.01x faster                                                    |
| pickle_pure_python         | 318 us                                                       | 315 us: 1.01x faster                                                    |
| tornado_http               | 120 ms                                                       | 118 ms: 1.01x faster                                                    |
| meteor_contest             | 128 ms                                                       | 127 ms: 1.01x faster                                                    |
| sympy_str                  | 296 ms                                                       | 293 ms: 1.01x faster                                                    |
| typing_runtime_protocols   | 174 us                                                       | 172 us: 1.01x faster                                                    |
| xml_etree_parse            | 145 ms                                                       | 143 ms: 1.01x faster                                                    |
| thrift                     | 877 us                                                       | 868 us: 1.01x faster                                                    |
| sqlite_synth               | 2.79 us                                                      | 2.76 us: 1.01x faster                                                   |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.25 ms: 1.01x faster                                                   |
| mdp                        | 2.52 sec                                                     | 2.51 sec: 1.01x faster                                                  |
| hexiom                     | 6.33 ms                                                      | 6.29 ms: 1.01x faster                                                   |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 570 ms: 1.01x faster                                                    |
| sympy_integrate            | 23.3 ms                                                      | 23.2 ms: 1.01x faster                                                   |
| spectral_norm              | 97.4 ms                                                      | 97.1 ms: 1.00x faster                                                   |
| sqlglot_normalize          | 118 ms                                                       | 118 ms: 1.00x faster                                                    |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x faster                                                  |
| python_startup_no_site     | 8.94 ms                                                      | 8.95 ms: 1.00x slower                                                   |
| python_startup             | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                   |
| scimark_lu                 | 97.8 ms                                                      | 98.1 ms: 1.00x slower                                                   |
| pidigits                   | 253 ms                                                       | 254 ms: 1.01x slower                                                    |
| json                       | 5.22 ms                                                      | 5.26 ms: 1.01x slower                                                   |
| unpickle_list              | 4.62 us                                                      | 4.66 us: 1.01x slower                                                   |
| comprehensions             | 17.3 us                                                      | 17.4 us: 1.01x slower                                                   |
| pprint_pformat             | 1.65 sec                                                     | 1.67 sec: 1.01x slower                                                  |
| logging_simple             | 6.40 us                                                      | 6.47 us: 1.01x slower                                                   |
| logging_silent             | 97.7 ns                                                      | 98.8 ns: 1.01x slower                                                   |
| json_dumps                 | 11.0 ms                                                      | 11.1 ms: 1.01x slower                                                   |
| html5lib                   | 71.9 ms                                                      | 72.9 ms: 1.01x slower                                                   |
| xml_etree_iterparse        | 100 ms                                                       | 101 ms: 1.01x slower                                                    |
| unpickle                   | 15.1 us                                                      | 15.5 us: 1.02x slower                                                   |
| dulwich_log                | 65.5 ms                                                      | 67.2 ms: 1.03x slower                                                   |
| chaos                      | 61.7 ms                                                      | 63.2 ms: 1.03x slower                                                   |
| asyncio_websockets         | 382 ms                                                       | 392 ms: 1.03x slower                                                    |
| nqueens                    | 88.2 ms                                                      | 90.5 ms: 1.03x slower                                                   |
| regex_effbot               | 3.37 ms                                                      | 3.46 ms: 1.03x slower                                                   |
| coroutines                 | 21.6 ms                                                      | 22.3 ms: 1.03x slower                                                   |
| deltablue                  | 3.41 ms                                                      | 3.51 ms: 1.03x slower                                                   |
| sqlglot_transpile          | 1.78 ms                                                      | 1.84 ms: 1.03x slower                                                   |
| docutils                   | 2.81 sec                                                     | 2.91 sec: 1.03x slower                                                  |
| json_loads                 | 24.0 us                                                      | 24.9 us: 1.04x slower                                                   |
| fannkuch                   | 365 ms                                                       | 380 ms: 1.04x slower                                                    |
| unpickle_pure_python       | 214 us                                                       | 226 us: 1.05x slower                                                    |
| scimark_monte_carlo        | 64.9 ms                                                      | 68.3 ms: 1.05x slower                                                   |
| sqlglot_parse              | 1.38 ms                                                      | 1.46 ms: 1.06x slower                                                   |
| django_template            | 38.9 ms                                                      | 41.3 ms: 1.06x slower                                                   |
| tomli_loads                | 2.41 sec                                                     | 2.56 sec: 1.07x slower                                                  |
| gc_traversal               | 4.11 ms                                                      | 4.42 ms: 1.07x slower                                                   |
| create_gc_cycles           | 1.76 ms                                                      | 1.95 ms: 1.11x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                            |

Benchmark hidden because not significant (11): mako, sympy_sum, crypto_pyaes, sympy_expand, xml_etree_generate, pycparser, async_generators, pprint_safe_repr, logging_format, pylint, bench_mp_pool
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 99.80% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x