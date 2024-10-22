# Results vs. 3.13.0

- fork: faster-cpython
- ref: spill_before_escapin
- machine: linux-x86_64
- commit hash: dd0e9f6
- commit date: 2024-09-17
- overall geometric mean: 1.02x faster
- HPT reliability: 96.82%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-linux-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-dd0e9f6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 256 ms: 1.04x faster                                                            |
| docutils       | 2.58 sec                                               | 2.67 sec: 1.03x slower                                                          |
| html5lib       | 64.5 ms                                                | 64.3 ms: 1.00x faster                                                           |
| tornado_http   | 91.5 ms                                                | 90.2 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-linux-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-dd0e9f6 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 391 ms: 1.19x faster                                                            |
| async_tree_memoization     | 442 ms                                                 | 394 ms: 1.12x faster                                                            |
| async_tree_none            | 354 ms                                                 | 315 ms: 1.12x faster                                                            |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 560 ms: 1.03x faster                                                            |
| asyncio_tcp                | 488 ms                                                 | 482 ms: 1.01x faster                                                            |
| async_generators           | 433 ms                                                 | 430 ms: 1.01x faster                                                            |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.00x slower                                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 551 ms: 1.01x slower                                                            |
| async_tree_io              | 843 ms                                                 | 874 ms: 1.04x slower                                                            |
| coroutines                 | 22.5 ms                                                | 23.7 ms: 1.05x slower                                                           |
| async_tree_io_tg           | 825 ms                                                 | 878 ms: 1.06x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                    |

Benchmark hidden because not significant (2): async_tree_none_tg, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-linux-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-dd0e9f6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 77.0 ms: 1.02x faster                                                           |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                            |
| nbody          | 85.7 ms                                                | 86.2 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-linux-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-dd0e9f6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 131 ms                                                 | 129 ms: 1.02x faster                                                            |
| regex_dna      | 220 ms                                                 | 228 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                    |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-linux-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-dd0e9f6 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_list          | 5.01 us                                                | 4.78 us: 1.05x faster                                                           |
| xml_etree_process    | 60.4 ms                                                | 58.8 ms: 1.03x faster                                                           |
| pickle               | 11.6 us                                                | 11.3 us: 1.03x faster                                                           |
| xml_etree_generate   | 87.0 ms                                                | 84.8 ms: 1.03x faster                                                           |
| tomli_loads          | 2.11 sec                                               | 2.08 sec: 1.02x faster                                                          |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                           |
| unpickle             | 14.9 us                                                | 14.7 us: 1.01x faster                                                           |
| json_loads           | 27.0 us                                                | 26.8 us: 1.01x faster                                                           |
| pickle_pure_python   | 300 us                                                 | 299 us: 1.00x faster                                                            |
| unpickle_pure_python | 213 us                                                 | 216 us: 1.01x slower                                                            |
| xml_etree_iterparse  | 102 ms                                                 | 104 ms: 1.02x slower                                                            |
| pickle_dict          | 33.2 us                                                | 34.1 us: 1.03x slower                                                           |
| unpickle_list        | 4.96 us                                                | 5.17 us: 1.04x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-linux-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-dd0e9f6 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                           |
| python_startup_no_site | 6.99 ms                                                | 6.98 ms: 1.00x faster                                                           |
| Geometric mean         | (ref)                                                  | 1.00x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-linux-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-dd0e9f6 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 22.9 ms                                                | 21.9 ms: 1.04x faster                                                           |
| genshi_xml      | 50.3 ms                                                | 49.6 ms: 1.02x faster                                                           |
| django_template | 34.4 ms                                                | 34.1 ms: 1.01x faster                                                           |
| mako            | 11.1 ms                                                | 11.5 ms: 1.03x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240917-linux-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-dd0e9f6 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                   | 352 us                                                 | 256 us: 1.38x faster                                                            |
| deepcopy_memo              | 38.0 us                                                | 30.1 us: 1.26x faster                                                           |
| deepcopy_reduce            | 3.17 us                                                | 2.66 us: 1.19x faster                                                           |
| async_tree_memoization_tg  | 465 ms                                                 | 391 ms: 1.19x faster                                                            |
| go                         | 142 ms                                                 | 121 ms: 1.17x faster                                                            |
| async_tree_memoization     | 442 ms                                                 | 394 ms: 1.12x faster                                                            |
| async_tree_none            | 354 ms                                                 | 315 ms: 1.12x faster                                                            |
| mdp                        | 2.74 sec                                               | 2.52 sec: 1.09x faster                                                          |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.65 ms: 1.08x faster                                                           |
| pathlib                    | 17.1 ms                                                | 16.0 ms: 1.07x faster                                                           |
| json                       | 5.20 ms                                                | 4.91 ms: 1.06x faster                                                           |
| pickle_list                | 5.01 us                                                | 4.78 us: 1.05x faster                                                           |
| generators                 | 28.8 ms                                                | 27.6 ms: 1.04x faster                                                           |
| genshi_text                | 22.9 ms                                                | 21.9 ms: 1.04x faster                                                           |
| thrift                     | 796 us                                                 | 768 us: 1.04x faster                                                            |
| 2to3                       | 265 ms                                                 | 256 ms: 1.04x faster                                                            |
| pprint_safe_repr           | 744 ms                                                 | 719 ms: 1.04x faster                                                            |
| spectral_norm              | 115 ms                                                 | 111 ms: 1.03x faster                                                            |
| bench_thread_pool          | 815 us                                                 | 789 us: 1.03x faster                                                            |
| gc_traversal               | 3.81 ms                                                | 3.69 ms: 1.03x faster                                                           |
| richards_super             | 54.4 ms                                                | 52.9 ms: 1.03x faster                                                           |
| xml_etree_process          | 60.4 ms                                                | 58.8 ms: 1.03x faster                                                           |
| pickle                     | 11.6 us                                                | 11.3 us: 1.03x faster                                                           |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 560 ms: 1.03x faster                                                            |
| richards                   | 48.1 ms                                                | 46.9 ms: 1.03x faster                                                           |
| xml_etree_generate         | 87.0 ms                                                | 84.8 ms: 1.03x faster                                                           |
| scimark_lu                 | 115 ms                                                 | 113 ms: 1.02x faster                                                            |
| pprint_pformat             | 1.51 sec                                               | 1.48 sec: 1.02x faster                                                          |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                                            |
| float                      | 78.5 ms                                                | 77.0 ms: 1.02x faster                                                           |
| sympy_integrate            | 19.9 ms                                                | 19.6 ms: 1.02x faster                                                           |
| tomli_loads                | 2.11 sec                                               | 2.08 sec: 1.02x faster                                                          |
| regex_compile              | 131 ms                                                 | 129 ms: 1.02x faster                                                            |
| sympy_str                  | 274 ms                                                 | 269 ms: 1.02x faster                                                            |
| genshi_xml                 | 50.3 ms                                                | 49.6 ms: 1.02x faster                                                           |
| tornado_http               | 91.5 ms                                                | 90.2 ms: 1.01x faster                                                           |
| asyncio_tcp                | 488 ms                                                 | 482 ms: 1.01x faster                                                            |
| telco                      | 8.45 ms                                                | 8.36 ms: 1.01x faster                                                           |
| django_template            | 34.4 ms                                                | 34.1 ms: 1.01x faster                                                           |
| pycparser                  | 1.19 sec                                               | 1.18 sec: 1.01x faster                                                          |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                           |
| logging_simple             | 5.66 us                                                | 5.61 us: 1.01x faster                                                           |
| sqlglot_optimize           | 53.9 ms                                                | 53.4 ms: 1.01x faster                                                           |
| nqueens                    | 80.6 ms                                                | 79.9 ms: 1.01x faster                                                           |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                           |
| unpickle                   | 14.9 us                                                | 14.7 us: 1.01x faster                                                           |
| crypto_pyaes               | 73.0 ms                                                | 72.4 ms: 1.01x faster                                                           |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                                            |
| scimark_fft                | 369 ms                                                 | 366 ms: 1.01x faster                                                            |
| json_loads                 | 27.0 us                                                | 26.8 us: 1.01x faster                                                           |
| async_generators           | 433 ms                                                 | 430 ms: 1.01x faster                                                            |
| pickle_pure_python         | 300 us                                                 | 299 us: 1.00x faster                                                            |
| html5lib                   | 64.5 ms                                                | 64.3 ms: 1.00x faster                                                           |
| python_startup_no_site     | 6.99 ms                                                | 6.98 ms: 1.00x faster                                                           |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                            |
| sqlglot_transpile          | 1.57 ms                                                | 1.58 ms: 1.00x slower                                                           |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.00x slower                                                            |
| nbody                      | 85.7 ms                                                | 86.2 ms: 1.01x slower                                                           |
| sqlglot_normalize          | 107 ms                                                 | 108 ms: 1.01x slower                                                            |
| sqlglot_parse              | 1.27 ms                                                | 1.28 ms: 1.01x slower                                                           |
| unpickle_pure_python       | 213 us                                                 | 216 us: 1.01x slower                                                            |
| scimark_sor                | 122 ms                                                 | 124 ms: 1.01x slower                                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 551 ms: 1.01x slower                                                            |
| chaos                      | 58.4 ms                                                | 59.3 ms: 1.01x slower                                                           |
| raytrace                   | 262 ms                                                 | 265 ms: 1.02x slower                                                            |
| hexiom                     | 6.13 ms                                                | 6.23 ms: 1.02x slower                                                           |
| comprehensions             | 16.4 us                                                | 16.7 us: 1.02x slower                                                           |
| xml_etree_iterparse        | 102 ms                                                 | 104 ms: 1.02x slower                                                            |
| coverage                   | 83.7 ms                                                | 85.5 ms: 1.02x slower                                                           |
| scimark_monte_carlo        | 66.3 ms                                                | 67.8 ms: 1.02x slower                                                           |
| dulwich_log                | 63.0 ms                                                | 64.6 ms: 1.03x slower                                                           |
| pickle_dict                | 33.2 us                                                | 34.1 us: 1.03x slower                                                           |
| bpe_tokeniser              | 4.69 sec                                               | 4.83 sec: 1.03x slower                                                          |
| docutils                   | 2.58 sec                                               | 2.67 sec: 1.03x slower                                                          |
| mako                       | 11.1 ms                                                | 11.5 ms: 1.03x slower                                                           |
| async_tree_io              | 843 ms                                                 | 874 ms: 1.04x slower                                                            |
| regex_dna                  | 220 ms                                                 | 228 ms: 1.04x slower                                                            |
| deltablue                  | 3.15 ms                                                | 3.28 ms: 1.04x slower                                                           |
| unpickle_list              | 4.96 us                                                | 5.17 us: 1.04x slower                                                           |
| fannkuch                   | 381 ms                                                 | 397 ms: 1.04x slower                                                            |
| coroutines                 | 22.5 ms                                                | 23.7 ms: 1.05x slower                                                           |
| async_tree_io_tg           | 825 ms                                                 | 878 ms: 1.06x slower                                                            |
| create_gc_cycles           | 1.61 ms                                                | 1.72 ms: 1.07x slower                                                           |
| unpack_sequence            | 42.4 ns                                                | 46.7 ns: 1.10x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                    |

Benchmark hidden because not significant (13): async_tree_none_tg, sympy_expand, xml_etree_parse, logging_silent, typing_runtime_protocols, logging_format, regex_v8, asyncio_tcp_ssl, bench_mp_pool, regex_effbot, pyflate, sqlite_synth, pylint
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 96.82% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x