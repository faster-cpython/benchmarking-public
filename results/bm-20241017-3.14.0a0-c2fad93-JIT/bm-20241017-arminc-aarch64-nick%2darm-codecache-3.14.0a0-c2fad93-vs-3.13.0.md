# Results vs. 3.13.0

- fork: nick-arm
- ref: codecache
- machine: linux-aarch64
- commit hash: c2fad93
- commit date: 2024-10-17
- overall geometric mean: 1.18x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 375 ms: 1.23x slower                                             |
| docutils       | 2.91 sec                                                 | 3.67 sec: 1.26x slower                                           |
| html5lib       | 64.3 ms                                                  | 71.1 ms: 1.11x slower                                            |
| tornado_http   | 131 ms                                                   | 146 ms: 1.11x slower                                             |
| Geometric mean | (ref)                                                    | 1.17x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 544 ms: 1.19x faster                                             |
| async_tree_none_tg         | 467 ms                                                   | 422 ms: 1.11x faster                                             |
| async_tree_none            | 493 ms                                                   | 455 ms: 1.09x faster                                             |
| async_tree_memoization     | 626 ms                                                   | 582 ms: 1.07x faster                                             |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 718 ms: 1.02x faster                                             |
| coroutines                 | 28.2 ms                                                  | 28.5 ms: 1.01x slower                                            |
| asyncio_websockets         | 656 ms                                                   | 663 ms: 1.01x slower                                             |
| async_generators           | 496 ms                                                   | 510 ms: 1.03x slower                                             |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.28 sec: 1.04x slower                                           |
| async_tree_io              | 1.11 sec                                                 | 1.20 sec: 1.08x slower                                           |
| async_tree_io_tg           | 1.09 sec                                                 | 1.19 sec: 1.09x slower                                           |
| asyncio_tcp                | 568 ms                                                   | 623 ms: 1.10x slower                                             |
| Geometric mean             | (ref)                                                    | 1.01x faster                                                     |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 110 ms: 1.04x faster                                             |
| float          | 94.4 ms                                                  | 93.8 ms: 1.01x faster                                            |
| Geometric mean | (ref)                                                    | 1.01x faster                                                     |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 128 ms                                                   | 176 ms: 1.37x slower                                             |
| Geometric mean | (ref)                                                    | 1.08x slower                                                     |

Benchmark hidden because not significant (3): regex_v8, regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle             | 20.2 us                                                  | 19.2 us: 1.05x faster                                            |
| pickle_list          | 5.34 us                                                  | 5.21 us: 1.03x faster                                            |
| pickle               | 13.5 us                                                  | 13.8 us: 1.03x slower                                            |
| xml_etree_iterparse  | 147 ms                                                   | 151 ms: 1.03x slower                                             |
| tomli_loads          | 2.53 sec                                                 | 2.64 sec: 1.05x slower                                           |
| unpickle_pure_python | 254 us                                                   | 267 us: 1.05x slower                                             |
| pickle_pure_python   | 359 us                                                   | 388 us: 1.08x slower                                             |
| Geometric mean       | (ref)                                                    | 1.01x slower                                                     |

Benchmark hidden because not significant (7): xml_etree_generate, unpickle_list, json_loads, json_dumps, pickle_dict, xml_etree_parse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup | 13.3 ms                                                  | 14.7 ms: 1.11x slower                                            |
| Geometric mean | (ref)                                                    | 1.05x slower                                                     |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|-----------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 13.3 ms                                                  | 12.9 ms: 1.03x faster                                            |
| django_template | 42.3 ms                                                  | 52.3 ms: 1.24x slower                                            |
| genshi_text     | 27.7 ms                                                  | 35.0 ms: 1.26x slower                                            |
| genshi_xml      | 60.2 ms                                                  | 85.1 ms: 1.41x slower                                            |
| Geometric mean  | (ref)                                                    | 1.21x slower                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| deepcopy_memo              | 51.0 us                                                  | 37.7 us: 1.35x faster                                            |
| async_tree_memoization_tg  | 649 ms                                                   | 544 ms: 1.19x faster                                             |
| deepcopy                   | 451 us                                                   | 397 us: 1.14x faster                                             |
| async_tree_none_tg         | 467 ms                                                   | 422 ms: 1.11x faster                                             |
| async_tree_none            | 493 ms                                                   | 455 ms: 1.09x faster                                             |
| async_tree_memoization     | 626 ms                                                   | 582 ms: 1.07x faster                                             |
| deepcopy_reduce            | 4.07 us                                                  | 3.83 us: 1.06x faster                                            |
| unpickle                   | 20.2 us                                                  | 19.2 us: 1.05x faster                                            |
| scimark_sor                | 159 ms                                                   | 152 ms: 1.05x faster                                             |
| nbody                      | 114 ms                                                   | 110 ms: 1.04x faster                                             |
| pathlib                    | 22.4 ms                                                  | 21.6 ms: 1.04x faster                                            |
| mako                       | 13.3 ms                                                  | 12.9 ms: 1.03x faster                                            |
| pickle_list                | 5.34 us                                                  | 5.21 us: 1.03x faster                                            |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 718 ms: 1.02x faster                                             |
| telco                      | 9.73 ms                                                  | 9.53 ms: 1.02x faster                                            |
| json                       | 5.61 ms                                                  | 5.53 ms: 1.01x faster                                            |
| scimark_fft                | 447 ms                                                   | 443 ms: 1.01x faster                                             |
| float                      | 94.4 ms                                                  | 93.8 ms: 1.01x faster                                            |
| coroutines                 | 28.2 ms                                                  | 28.5 ms: 1.01x slower                                            |
| asyncio_websockets         | 656 ms                                                   | 663 ms: 1.01x slower                                             |
| thrift                     | 946 us                                                   | 958 us: 1.01x slower                                             |
| pickle                     | 13.5 us                                                  | 13.8 us: 1.03x slower                                            |
| xml_etree_iterparse        | 147 ms                                                   | 151 ms: 1.03x slower                                             |
| async_generators           | 496 ms                                                   | 510 ms: 1.03x slower                                             |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 6.80 ms: 1.03x slower                                            |
| mdp                        | 3.36 sec                                                 | 3.49 sec: 1.04x slower                                           |
| bpe_tokeniser              | 5.90 sec                                                 | 6.13 sec: 1.04x slower                                           |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.28 sec: 1.04x slower                                           |
| coverage                   | 98.5 ms                                                  | 103 ms: 1.04x slower                                             |
| tomli_loads                | 2.53 sec                                                 | 2.64 sec: 1.05x slower                                           |
| unpickle_pure_python       | 254 us                                                   | 267 us: 1.05x slower                                             |
| logging_format             | 7.83 us                                                  | 8.22 us: 1.05x slower                                            |
| scimark_lu                 | 139 ms                                                   | 149 ms: 1.07x slower                                             |
| crypto_pyaes               | 82.7 ms                                                  | 88.5 ms: 1.07x slower                                            |
| spectral_norm              | 141 ms                                                   | 152 ms: 1.07x slower                                             |
| typing_runtime_protocols   | 192 us                                                   | 207 us: 1.08x slower                                             |
| pickle_pure_python         | 359 us                                                   | 388 us: 1.08x slower                                             |
| logging_simple             | 7.04 us                                                  | 7.62 us: 1.08x slower                                            |
| async_tree_io              | 1.11 sec                                                 | 1.20 sec: 1.08x slower                                           |
| scimark_monte_carlo        | 83.8 ms                                                  | 90.9 ms: 1.08x slower                                            |
| async_tree_io_tg           | 1.09 sec                                                 | 1.19 sec: 1.09x slower                                           |
| asyncio_tcp                | 568 ms                                                   | 623 ms: 1.10x slower                                             |
| meteor_contest             | 113 ms                                                   | 125 ms: 1.10x slower                                             |
| bench_thread_pool          | 1.28 ms                                                  | 1.40 ms: 1.10x slower                                            |
| html5lib                   | 64.3 ms                                                  | 71.1 ms: 1.11x slower                                            |
| python_startup             | 13.3 ms                                                  | 14.7 ms: 1.11x slower                                            |
| tornado_http               | 131 ms                                                   | 146 ms: 1.11x slower                                             |
| pyflate                    | 556 ms                                                   | 621 ms: 1.12x slower                                             |
| fannkuch                   | 452 ms                                                   | 519 ms: 1.15x slower                                             |
| deltablue                  | 3.85 ms                                                  | 4.47 ms: 1.16x slower                                            |
| go                         | 163 ms                                                   | 189 ms: 1.16x slower                                             |
| raytrace                   | 298 ms                                                   | 347 ms: 1.17x slower                                             |
| pycparser                  | 1.26 sec                                                 | 1.48 sec: 1.17x slower                                           |
| sqlglot_normalize          | 128 ms                                                   | 154 ms: 1.20x slower                                             |
| sqlglot_parse              | 1.38 ms                                                  | 1.69 ms: 1.22x slower                                            |
| comprehensions             | 20.4 us                                                  | 24.9 us: 1.22x slower                                            |
| nqueens                    | 98.7 ms                                                  | 121 ms: 1.23x slower                                             |
| 2to3                       | 306 ms                                                   | 375 ms: 1.23x slower                                             |
| django_template            | 42.3 ms                                                  | 52.3 ms: 1.24x slower                                            |
| chaos                      | 68.8 ms                                                  | 86.0 ms: 1.25x slower                                            |
| genshi_text                | 27.7 ms                                                  | 35.0 ms: 1.26x slower                                            |
| docutils                   | 2.91 sec                                                 | 3.67 sec: 1.26x slower                                           |
| richards_super             | 60.3 ms                                                  | 76.3 ms: 1.27x slower                                            |
| sqlglot_transpile          | 1.73 ms                                                  | 2.20 ms: 1.27x slower                                            |
| sqlglot_optimize           | 62.4 ms                                                  | 79.2 ms: 1.27x slower                                            |
| richards                   | 53.5 ms                                                  | 68.8 ms: 1.29x slower                                            |
| sympy_expand               | 455 ms                                                   | 593 ms: 1.30x slower                                             |
| pprint_safe_repr           | 926 ms                                                   | 1.22 sec: 1.32x slower                                           |
| sympy_str                  | 264 ms                                                   | 355 ms: 1.35x slower                                             |
| gc_traversal               | 4.53 ms                                                  | 6.17 ms: 1.36x slower                                            |
| pprint_pformat             | 1.90 sec                                                 | 2.60 sec: 1.37x slower                                           |
| regex_compile              | 128 ms                                                   | 176 ms: 1.37x slower                                             |
| sympy_integrate            | 21.0 ms                                                  | 28.9 ms: 1.38x slower                                            |
| pylint                     | 343 ms                                                   | 483 ms: 1.41x slower                                             |
| genshi_xml                 | 60.2 ms                                                  | 85.1 ms: 1.41x slower                                            |
| hexiom                     | 7.13 ms                                                  | 10.4 ms: 1.45x slower                                            |
| sympy_sum                  | 143 ms                                                   | 210 ms: 1.46x slower                                             |
| generators                 | 37.8 ms                                                  | 59.3 ms: 1.57x slower                                            |
| create_gc_cycles           | 2.12 ms                                                  | 3.58 ms: 1.69x slower                                            |
| unpack_sequence            | 57.2 ns                                                  | 147 ns: 2.57x slower                                             |
| bench_mp_pool              | 7.30 ms                                                  | 3.29 sec: 450.25x slower                                         |
| Geometric mean             | (ref)                                                    | 1.18x slower                                                     |

Benchmark hidden because not significant (15): xml_etree_generate, async_tree_cpu_io_mixed, unpickle_list, json_loads, sqlite_synth, json_dumps, pickle_dict, logging_silent, regex_v8, xml_etree_parse, regex_dna, python_startup_no_site, regex_effbot, xml_etree_process, pidigits
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (2) of results/bm-20241017-3.14.0a0-c2fad93-JIT/bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93.json: dulwich_log, sphinx

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: 1.22x