# Results vs. 3.13.0

- fork: python
- ref: v3.13.0b2
- machine: linux-x86_64
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.01x slower
- HPT reliability: 99.35%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 305 ms: 1.05x slower                                             |
| chameleon      | 7.42 ms                                                      | 7.48 ms: 1.01x slower                                            |
| html5lib       | 71.9 ms                                                      | 75.4 ms: 1.05x slower                                            |
| tornado_http   | 120 ms                                                       | 123 ms: 1.03x slower                                             |
| Geometric mean | (ref)                                                        | 1.03x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|---------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg | 461 ms                                                       | 441 ms: 1.05x faster                                             |
| asyncio_tcp               | 380 ms                                                       | 382 ms: 1.01x slower                                             |
| async_tree_none           | 372 ms                                                       | 380 ms: 1.02x slower                                             |
| asyncio_websockets        | 382 ms                                                       | 391 ms: 1.02x slower                                             |
| async_tree_none_tg        | 340 ms                                                       | 349 ms: 1.03x slower                                             |
| coroutines                | 21.6 ms                                                      | 22.3 ms: 1.03x slower                                            |
| async_tree_cpu_io_mixed   | 600 ms                                                       | 628 ms: 1.05x slower                                             |
| async_generators          | 359 ms                                                       | 389 ms: 1.08x slower                                             |
| async_tree_io_tg          | 819 ms                                                       | 891 ms: 1.09x slower                                             |
| async_tree_io             | 847 ms                                                       | 921 ms: 1.09x slower                                             |
| Geometric mean            | (ref)                                                        | 1.03x slower                                                     |

Benchmark hidden because not significant (3): asyncio_tcp_ssl, async_tree_memoization, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 74.2 ms: 1.10x faster                                            |
| nbody          | 88.0 ms                                                      | 82.9 ms: 1.06x faster                                            |
| pidigits       | 253 ms                                                       | 250 ms: 1.01x faster                                             |
| Geometric mean | (ref)                                                        | 1.06x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 139 ms: 1.04x faster                                             |
| regex_v8       | 26.2 ms                                                      | 25.2 ms: 1.04x faster                                            |
| regex_dna      | 244 ms                                                       | 248 ms: 1.02x slower                                             |
| regex_effbot   | 3.37 ms                                                      | 3.56 ms: 1.06x slower                                            |
| Geometric mean | (ref)                                                        | 1.00x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| tomli_loads          | 2.41 sec                                                     | 2.09 sec: 1.15x faster                                           |
| pickle_list          | 4.59 us                                                      | 4.35 us: 1.06x faster                                            |
| xml_etree_process    | 60.9 ms                                                      | 58.5 ms: 1.04x faster                                            |
| pickle_dict          | 32.1 us                                                      | 30.9 us: 1.04x faster                                            |
| xml_etree_generate   | 85.3 ms                                                      | 82.4 ms: 1.04x faster                                            |
| json_dumps           | 11.0 ms                                                      | 10.7 ms: 1.03x faster                                            |
| pickle_pure_python   | 318 us                                                       | 310 us: 1.03x faster                                             |
| unpickle_pure_python | 214 us                                                       | 211 us: 1.02x faster                                             |
| xml_etree_iterparse  | 100 ms                                                       | 99.3 ms: 1.01x faster                                            |
| pickle               | 10.5 us                                                      | 10.6 us: 1.00x slower                                            |
| json_loads           | 24.0 us                                                      | 24.4 us: 1.02x slower                                            |
| unpickle_list        | 4.62 us                                                      | 4.75 us: 1.03x slower                                            |
| unpickle             | 15.1 us                                                      | 15.6 us: 1.03x slower                                            |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                     |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 13.8 ms: 1.04x slower                                            |
| python_startup_no_site | 8.94 ms                                                      | 9.44 ms: 1.05x slower                                            |
| Geometric mean         | (ref)                                                        | 1.05x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 10.4 ms                                                      | 9.10 ms: 1.14x faster                                            |
| genshi_text     | 26.6 ms                                                      | 28.2 ms: 1.06x slower                                            |
| django_template | 38.9 ms                                                      | 41.4 ms: 1.07x slower                                            |
| genshi_xml      | 57.3 ms                                                      | 65.3 ms: 1.14x slower                                            |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                     |

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|---------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mypy2                     | 1.05 sec                                                     | 852 ms: 1.23x faster                                             |
| spectral_norm             | 97.4 ms                                                      | 82.3 ms: 1.18x faster                                            |
| tomli_loads               | 2.41 sec                                                     | 2.09 sec: 1.15x faster                                           |
| mako                      | 10.4 ms                                                      | 9.10 ms: 1.14x faster                                            |
| richards_super            | 59.8 ms                                                      | 52.8 ms: 1.13x faster                                            |
| richards                  | 52.7 ms                                                      | 46.5 ms: 1.13x faster                                            |
| float                     | 81.9 ms                                                      | 74.2 ms: 1.10x faster                                            |
| fannkuch                  | 365 ms                                                       | 331 ms: 1.10x faster                                             |
| pyflate                   | 492 ms                                                       | 449 ms: 1.10x faster                                             |
| scimark_fft               | 314 ms                                                       | 292 ms: 1.08x faster                                             |
| scimark_sparse_mat_mult   | 4.29 ms                                                      | 3.99 ms: 1.07x faster                                            |
| telco                     | 8.58 ms                                                      | 8.05 ms: 1.07x faster                                            |
| nbody                     | 88.0 ms                                                      | 82.9 ms: 1.06x faster                                            |
| deepcopy_memo             | 39.5 us                                                      | 37.2 us: 1.06x faster                                            |
| pickle_list               | 4.59 us                                                      | 4.35 us: 1.06x faster                                            |
| async_tree_memoization_tg | 461 ms                                                       | 441 ms: 1.05x faster                                             |
| xml_etree_process         | 60.9 ms                                                      | 58.5 ms: 1.04x faster                                            |
| regex_compile             | 144 ms                                                       | 139 ms: 1.04x faster                                             |
| pickle_dict               | 32.1 us                                                      | 30.9 us: 1.04x faster                                            |
| regex_v8                  | 26.2 ms                                                      | 25.2 ms: 1.04x faster                                            |
| xml_etree_generate        | 85.3 ms                                                      | 82.4 ms: 1.04x faster                                            |
| crypto_pyaes              | 72.8 ms                                                      | 70.6 ms: 1.03x faster                                            |
| json_dumps                | 11.0 ms                                                      | 10.7 ms: 1.03x faster                                            |
| pickle_pure_python        | 318 us                                                       | 310 us: 1.03x faster                                             |
| pprint_safe_repr          | 812 ms                                                       | 792 ms: 1.03x faster                                             |
| unpickle_pure_python      | 214 us                                                       | 211 us: 1.02x faster                                             |
| pprint_pformat            | 1.65 sec                                                     | 1.63 sec: 1.01x faster                                           |
| pidigits                  | 253 ms                                                       | 250 ms: 1.01x faster                                             |
| xml_etree_iterparse       | 100 ms                                                       | 99.3 ms: 1.01x faster                                            |
| coverage                  | 81.1 ms                                                      | 80.7 ms: 1.00x faster                                            |
| pickle                    | 10.5 us                                                      | 10.6 us: 1.00x slower                                            |
| bpe_tokeniser             | 5.10 sec                                                     | 5.13 sec: 1.01x slower                                           |
| asyncio_tcp               | 380 ms                                                       | 382 ms: 1.01x slower                                             |
| chameleon                 | 7.42 ms                                                      | 7.48 ms: 1.01x slower                                            |
| mdp                       | 2.52 sec                                                     | 2.55 sec: 1.01x slower                                           |
| dulwich_log               | 65.5 ms                                                      | 66.2 ms: 1.01x slower                                            |
| logging_format            | 7.07 us                                                      | 7.17 us: 1.01x slower                                            |
| json                      | 5.22 ms                                                      | 5.30 ms: 1.01x slower                                            |
| scimark_monte_carlo       | 64.9 ms                                                      | 65.9 ms: 1.02x slower                                            |
| meteor_contest            | 128 ms                                                       | 130 ms: 1.02x slower                                             |
| json_loads                | 24.0 us                                                      | 24.4 us: 1.02x slower                                            |
| regex_dna                 | 244 ms                                                       | 248 ms: 1.02x slower                                             |
| async_tree_none           | 372 ms                                                       | 380 ms: 1.02x slower                                             |
| asyncio_websockets        | 382 ms                                                       | 391 ms: 1.02x slower                                             |
| sqlglot_transpile         | 1.78 ms                                                      | 1.82 ms: 1.02x slower                                            |
| tornado_http              | 120 ms                                                       | 123 ms: 1.03x slower                                             |
| generators                | 33.5 ms                                                      | 34.3 ms: 1.03x slower                                            |
| raytrace                  | 289 ms                                                       | 297 ms: 1.03x slower                                             |
| unpickle_list             | 4.62 us                                                      | 4.75 us: 1.03x slower                                            |
| async_tree_none_tg        | 340 ms                                                       | 349 ms: 1.03x slower                                             |
| comprehensions            | 17.3 us                                                      | 17.8 us: 1.03x slower                                            |
| unpickle                  | 15.1 us                                                      | 15.6 us: 1.03x slower                                            |
| bench_mp_pool             | 4.65 ms                                                      | 4.80 ms: 1.03x slower                                            |
| sqlglot_parse             | 1.38 ms                                                      | 1.42 ms: 1.03x slower                                            |
| coroutines                | 21.6 ms                                                      | 22.3 ms: 1.03x slower                                            |
| deepcopy                  | 397 us                                                       | 410 us: 1.03x slower                                             |
| go                        | 160 ms                                                       | 166 ms: 1.03x slower                                             |
| logging_simple            | 6.40 us                                                      | 6.61 us: 1.03x slower                                            |
| python_startup            | 13.3 ms                                                      | 13.8 ms: 1.04x slower                                            |
| deepcopy_reduce           | 3.54 us                                                      | 3.68 us: 1.04x slower                                            |
| thrift                    | 877 us                                                       | 913 us: 1.04x slower                                             |
| bench_thread_pool         | 901 us                                                       | 941 us: 1.04x slower                                             |
| chaos                     | 61.7 ms                                                      | 64.4 ms: 1.04x slower                                            |
| async_tree_cpu_io_mixed   | 600 ms                                                       | 628 ms: 1.05x slower                                             |
| sympy_str                 | 296 ms                                                       | 310 ms: 1.05x slower                                             |
| html5lib                  | 71.9 ms                                                      | 75.4 ms: 1.05x slower                                            |
| hexiom                    | 6.33 ms                                                      | 6.65 ms: 1.05x slower                                            |
| 2to3                      | 291 ms                                                       | 305 ms: 1.05x slower                                             |
| sqlglot_optimize          | 59.7 ms                                                      | 62.9 ms: 1.05x slower                                            |
| sympy_expand              | 505 ms                                                       | 532 ms: 1.05x slower                                             |
| typing_runtime_protocols  | 174 us                                                       | 184 us: 1.05x slower                                             |
| python_startup_no_site    | 8.94 ms                                                      | 9.44 ms: 1.05x slower                                            |
| regex_effbot              | 3.37 ms                                                      | 3.56 ms: 1.06x slower                                            |
| genshi_text               | 26.6 ms                                                      | 28.2 ms: 1.06x slower                                            |
| flaskblogging             | 4.62 ms                                                      | 4.92 ms: 1.07x slower                                            |
| django_template           | 38.9 ms                                                      | 41.4 ms: 1.07x slower                                            |
| sympy_sum                 | 154 ms                                                       | 165 ms: 1.07x slower                                             |
| dask                      | 379 ms                                                       | 408 ms: 1.08x slower                                             |
| sqlglot_normalize         | 118 ms                                                       | 127 ms: 1.08x slower                                             |
| async_generators          | 359 ms                                                       | 389 ms: 1.08x slower                                             |
| pylint                    | 346 ms                                                       | 376 ms: 1.09x slower                                             |
| async_tree_io_tg          | 819 ms                                                       | 891 ms: 1.09x slower                                             |
| async_tree_io             | 847 ms                                                       | 921 ms: 1.09x slower                                             |
| sympy_integrate           | 23.3 ms                                                      | 25.4 ms: 1.09x slower                                            |
| gc_traversal              | 4.11 ms                                                      | 4.49 ms: 1.09x slower                                            |
| aiohttp                   | 1.07 ms                                                      | 1.17 ms: 1.10x slower                                            |
| create_gc_cycles          | 1.76 ms                                                      | 1.94 ms: 1.10x slower                                            |
| nqueens                   | 88.2 ms                                                      | 97.2 ms: 1.10x slower                                            |
| gunicorn                  | 1.04 ms                                                      | 1.15 ms: 1.10x slower                                            |
| deltablue                 | 3.41 ms                                                      | 3.81 ms: 1.12x slower                                            |
| genshi_xml                | 57.3 ms                                                      | 65.3 ms: 1.14x slower                                            |
| scimark_sor               | 126 ms                                                       | 144 ms: 1.15x slower                                             |
| scimark_lu                | 97.8 ms                                                      | 114 ms: 1.16x slower                                             |
| logging_silent            | 97.7 ns                                                      | 123 ns: 1.26x slower                                             |
| Geometric mean            | (ref)                                                        | 1.01x slower                                                     |

Benchmark hidden because not significant (7): pycparser, pathlib, asyncio_tcp_ssl, xml_etree_parse, sqlite_synth, async_tree_memoization, async_tree_cpu_io_mixed_tg
Ignored benchmarks (2) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: docutils, unpack_sequence

# HPT report

- Reliability score: 99.35% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.10x