# Results vs. 3.13.0

- fork: faster-cpython
- ref: spill_before_escapin
- machine: linux-x86_64
- commit hash: dd0e9f6
- commit date: 2024-09-17
- overall geometric mean: 1.034x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-linux-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-dd0e9f6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 256 ms: 1.04x faster                                                            |
| docutils       | 2.59 sec                                               | 2.67 sec: 1.03x slower                                                          |
| tornado_http   | 92.4 ms                                                | 90.2 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-linux-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-dd0e9f6 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 391 ms: 1.19x faster                                                            |
| async_tree_memoization     | 442 ms                                                 | 394 ms: 1.12x faster                                                            |
| async_tree_none            | 351 ms                                                 | 315 ms: 1.11x faster                                                            |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 560 ms: 1.03x faster                                                            |
| async_generators           | 436 ms                                                 | 430 ms: 1.01x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 551 ms: 1.01x slower                                                            |
| asyncio_websockets         | 552 ms                                                 | 558 ms: 1.01x slower                                                            |
| async_tree_io_tg           | 857 ms                                                 | 878 ms: 1.02x slower                                                            |
| async_tree_io              | 842 ms                                                 | 874 ms: 1.04x slower                                                            |
| coroutines                 | 22.7 ms                                                | 23.7 ms: 1.04x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                    |

Benchmark hidden because not significant (1): async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-linux-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-dd0e9f6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 77.0 ms: 1.03x faster                                                           |
| nbody          | 87.0 ms                                                | 86.2 ms: 1.01x faster                                                           |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                            |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-linux-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-dd0e9f6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 25.3 ms: 1.04x faster                                                           |
| regex_compile  | 132 ms                                                 | 129 ms: 1.02x faster                                                            |
| regex_effbot   | 3.73 ms                                                | 3.89 ms: 1.04x slower                                                           |
| regex_dna      | 218 ms                                                 | 228 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-linux-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-dd0e9f6 |
|---------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python  | 310 us                                                 | 299 us: 1.04x faster                                                            |
| xml_etree_process   | 60.6 ms                                                | 58.8 ms: 1.03x faster                                                           |
| tomli_loads         | 2.14 sec                                               | 2.08 sec: 1.03x faster                                                          |
| json_dumps          | 10.6 ms                                                | 10.3 ms: 1.02x faster                                                           |
| xml_etree_generate  | 86.7 ms                                                | 84.8 ms: 1.02x faster                                                           |
| json_loads          | 27.2 us                                                | 26.8 us: 1.01x faster                                                           |
| xml_etree_iterparse | 101 ms                                                 | 104 ms: 1.03x slower                                                            |
| Geometric mean      | (ref)                                                  | 1.02x faster                                                                    |

Benchmark hidden because not significant (2): xml_etree_parse, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-linux-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-dd0e9f6 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                           |
| python_startup_no_site | 6.96 ms                                                | 6.98 ms: 1.00x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.09x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-linux-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-dd0e9f6 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 23.5 ms                                                | 21.9 ms: 1.07x faster                                                           |
| django_template | 35.2 ms                                                | 34.1 ms: 1.03x faster                                                           |
| genshi_xml      | 50.9 ms                                                | 49.6 ms: 1.03x faster                                                           |
| mako            | 11.1 ms                                                | 11.5 ms: 1.04x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-linux-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-dd0e9f6 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                   | 358 us                                                 | 256 us: 1.40x faster                                                            |
| create_gc_cycles           | 2.41 ms                                                | 1.72 ms: 1.40x faster                                                           |
| deepcopy_memo              | 39.1 us                                                | 30.1 us: 1.30x faster                                                           |
| deepcopy_reduce            | 3.20 us                                                | 2.66 us: 1.20x faster                                                           |
| python_startup             | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                           |
| async_tree_memoization_tg  | 464 ms                                                 | 391 ms: 1.19x faster                                                            |
| go                         | 144 ms                                                 | 121 ms: 1.19x faster                                                            |
| gc_traversal               | 4.37 ms                                                | 3.69 ms: 1.18x faster                                                           |
| async_tree_memoization     | 442 ms                                                 | 394 ms: 1.12x faster                                                            |
| async_tree_none            | 351 ms                                                 | 315 ms: 1.11x faster                                                            |
| pathlib                    | 17.5 ms                                                | 16.0 ms: 1.10x faster                                                           |
| json                       | 5.36 ms                                                | 4.91 ms: 1.09x faster                                                           |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.65 ms: 1.09x faster                                                           |
| mdp                        | 2.72 sec                                               | 2.52 sec: 1.08x faster                                                          |
| genshi_text                | 23.5 ms                                                | 21.9 ms: 1.07x faster                                                           |
| thrift                     | 809 us                                                 | 768 us: 1.05x faster                                                            |
| generators                 | 29.0 ms                                                | 27.6 ms: 1.05x faster                                                           |
| 2to3                       | 267 ms                                                 | 256 ms: 1.04x faster                                                            |
| bench_thread_pool          | 822 us                                                 | 789 us: 1.04x faster                                                            |
| crypto_pyaes               | 75.3 ms                                                | 72.4 ms: 1.04x faster                                                           |
| pickle_pure_python         | 310 us                                                 | 299 us: 1.04x faster                                                            |
| typing_runtime_protocols   | 165 us                                                 | 159 us: 1.04x faster                                                            |
| regex_v8                   | 26.2 ms                                                | 25.3 ms: 1.04x faster                                                           |
| richards_super             | 54.9 ms                                                | 52.9 ms: 1.04x faster                                                           |
| richards                   | 48.7 ms                                                | 46.9 ms: 1.04x faster                                                           |
| spectral_norm              | 115 ms                                                 | 111 ms: 1.04x faster                                                            |
| django_template            | 35.2 ms                                                | 34.1 ms: 1.03x faster                                                           |
| xml_etree_process          | 60.6 ms                                                | 58.8 ms: 1.03x faster                                                           |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 560 ms: 1.03x faster                                                            |
| tomli_loads                | 2.14 sec                                               | 2.08 sec: 1.03x faster                                                          |
| float                      | 79.2 ms                                                | 77.0 ms: 1.03x faster                                                           |
| genshi_xml                 | 50.9 ms                                                | 49.6 ms: 1.03x faster                                                           |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.03x faster                                                            |
| tornado_http               | 92.4 ms                                                | 90.2 ms: 1.02x faster                                                           |
| regex_compile              | 132 ms                                                 | 129 ms: 1.02x faster                                                            |
| json_dumps                 | 10.6 ms                                                | 10.3 ms: 1.02x faster                                                           |
| logging_format             | 6.40 us                                                | 6.25 us: 1.02x faster                                                           |
| pyflate                    | 471 ms                                                 | 461 ms: 1.02x faster                                                            |
| xml_etree_generate         | 86.7 ms                                                | 84.8 ms: 1.02x faster                                                           |
| telco                      | 8.54 ms                                                | 8.36 ms: 1.02x faster                                                           |
| sympy_str                  | 275 ms                                                 | 269 ms: 1.02x faster                                                            |
| meteor_contest             | 109 ms                                                 | 107 ms: 1.02x faster                                                            |
| logging_simple             | 5.72 us                                                | 5.61 us: 1.02x faster                                                           |
| fannkuch                   | 404 ms                                                 | 397 ms: 1.02x faster                                                            |
| sympy_integrate            | 19.9 ms                                                | 19.6 ms: 1.02x faster                                                           |
| pycparser                  | 1.20 sec                                               | 1.18 sec: 1.02x faster                                                          |
| json_loads                 | 27.2 us                                                | 26.8 us: 1.01x faster                                                           |
| pprint_safe_repr           | 728 ms                                                 | 719 ms: 1.01x faster                                                            |
| async_generators           | 436 ms                                                 | 430 ms: 1.01x faster                                                            |
| sympy_expand               | 463 ms                                                 | 458 ms: 1.01x faster                                                            |
| nbody                      | 87.0 ms                                                | 86.2 ms: 1.01x faster                                                           |
| pprint_pformat             | 1.49 sec                                               | 1.48 sec: 1.01x faster                                                          |
| raytrace                   | 267 ms                                                 | 265 ms: 1.01x faster                                                            |
| sqlglot_optimize           | 53.7 ms                                                | 53.4 ms: 1.01x faster                                                           |
| sqlglot_transpile          | 1.58 ms                                                | 1.58 ms: 1.00x faster                                                           |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                            |
| python_startup_no_site     | 6.96 ms                                                | 6.98 ms: 1.00x slower                                                           |
| dulwich_log                | 64.3 ms                                                | 64.6 ms: 1.00x slower                                                           |
| sqlglot_normalize          | 108 ms                                                 | 108 ms: 1.01x slower                                                            |
| scimark_monte_carlo        | 67.4 ms                                                | 67.8 ms: 1.01x slower                                                           |
| scimark_fft                | 364 ms                                                 | 366 ms: 1.01x slower                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 551 ms: 1.01x slower                                                            |
| asyncio_websockets         | 552 ms                                                 | 558 ms: 1.01x slower                                                            |
| hexiom                     | 6.16 ms                                                | 6.23 ms: 1.01x slower                                                           |
| comprehensions             | 16.5 us                                                | 16.7 us: 1.01x slower                                                           |
| bpe_tokeniser              | 4.75 sec                                               | 4.83 sec: 1.02x slower                                                          |
| deltablue                  | 3.23 ms                                                | 3.28 ms: 1.02x slower                                                           |
| coverage                   | 84.0 ms                                                | 85.5 ms: 1.02x slower                                                           |
| nqueens                    | 78.4 ms                                                | 79.9 ms: 1.02x slower                                                           |
| chaos                      | 58.1 ms                                                | 59.3 ms: 1.02x slower                                                           |
| async_tree_io_tg           | 857 ms                                                 | 878 ms: 1.02x slower                                                            |
| xml_etree_iterparse        | 101 ms                                                 | 104 ms: 1.03x slower                                                            |
| docutils                   | 2.59 sec                                               | 2.67 sec: 1.03x slower                                                          |
| mako                       | 11.1 ms                                                | 11.5 ms: 1.04x slower                                                           |
| async_tree_io              | 842 ms                                                 | 874 ms: 1.04x slower                                                            |
| coroutines                 | 22.7 ms                                                | 23.7 ms: 1.04x slower                                                           |
| regex_effbot               | 3.73 ms                                                | 3.89 ms: 1.04x slower                                                           |
| regex_dna                  | 218 ms                                                 | 228 ms: 1.04x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                    |

Benchmark hidden because not significant (10): async_tree_none_tg, xml_etree_parse, logging_silent, unpickle_pure_python, scimark_lu, bench_mp_pool, html5lib, scimark_sor, sqlglot_parse, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240917-3.14.0a0-dd0e9f6/bm-20240917-linux-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-dd0e9f6.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.034x faster
# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x