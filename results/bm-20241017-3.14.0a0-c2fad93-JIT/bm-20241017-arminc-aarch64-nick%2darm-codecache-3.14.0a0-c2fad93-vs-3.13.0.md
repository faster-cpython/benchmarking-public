# Results vs. 3.13.0

- fork: nick-arm
- ref: codecache
- machine: linux-aarch64
- commit hash: c2fad93
- commit date: 2024-10-17
- overall geometric mean: 1.087x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 375 ms: 1.24x slower                                             |
| docutils       | 2.89 sec                                                 | 3.67 sec: 1.27x slower                                           |
| html5lib       | 66.4 ms                                                  | 71.1 ms: 1.07x slower                                            |
| sphinx         | 1.17 sec                                                 | 1.42 sec: 1.21x slower                                           |
| tornado_http   | 128 ms                                                   | 146 ms: 1.14x slower                                             |
| Geometric mean | (ref)                                                    | 1.18x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 544 ms: 1.19x faster                                             |
| async_tree_memoization     | 651 ms                                                   | 582 ms: 1.12x faster                                             |
| async_tree_none_tg         | 470 ms                                                   | 422 ms: 1.11x faster                                             |
| async_tree_none            | 497 ms                                                   | 455 ms: 1.09x faster                                             |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 718 ms: 1.07x faster                                             |
| async_generators           | 489 ms                                                   | 510 ms: 1.04x slower                                             |
| async_tree_io_tg           | 1.13 sec                                                 | 1.19 sec: 1.05x slower                                           |
| async_tree_io              | 1.11 sec                                                 | 1.20 sec: 1.08x slower                                           |
| Geometric mean             | (ref)                                                    | 1.04x faster                                                     |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 110 ms: 1.04x faster                                             |
| float          | 93.3 ms                                                  | 93.8 ms: 1.01x slower                                            |
| Geometric mean | (ref)                                                    | 1.01x faster                                                     |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_dna      | 253 ms                                                   | 247 ms: 1.03x faster                                             |
| regex_v8       | 31.8 ms                                                  | 31.5 ms: 1.01x faster                                            |
| regex_compile  | 127 ms                                                   | 176 ms: 1.39x slower                                             |
| Geometric mean | (ref)                                                    | 1.08x slower                                                     |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| xml_etree_parse      | 197 ms                                                   | 188 ms: 1.05x faster                                             |
| json_loads           | 31.7 us                                                  | 31.2 us: 1.01x faster                                            |
| xml_etree_iterparse  | 149 ms                                                   | 151 ms: 1.01x slower                                             |
| tomli_loads          | 2.54 sec                                                 | 2.64 sec: 1.04x slower                                           |
| unpickle_pure_python | 251 us                                                   | 267 us: 1.07x slower                                             |
| pickle_pure_python   | 357 us                                                   | 388 us: 1.09x slower                                             |
| Geometric mean       | (ref)                                                    | 1.01x slower                                                     |

Benchmark hidden because not significant (3): json_dumps, xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup | 15.4 ms                                                  | 14.7 ms: 1.05x faster                                            |
| Geometric mean | (ref)                                                    | 1.02x faster                                                     |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|-----------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 13.4 ms                                                  | 12.9 ms: 1.03x faster                                            |
| django_template | 41.6 ms                                                  | 52.3 ms: 1.26x slower                                            |
| genshi_text     | 27.7 ms                                                  | 35.0 ms: 1.26x slower                                            |
| genshi_xml      | 60.3 ms                                                  | 85.1 ms: 1.41x slower                                            |
| Geometric mean  | (ref)                                                    | 1.21x slower                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| deepcopy_memo              | 50.4 us                                                  | 37.7 us: 1.34x faster                                            |
| async_tree_memoization_tg  | 649 ms                                                   | 544 ms: 1.19x faster                                             |
| deepcopy                   | 447 us                                                   | 397 us: 1.13x faster                                             |
| async_tree_memoization     | 651 ms                                                   | 582 ms: 1.12x faster                                             |
| async_tree_none_tg         | 470 ms                                                   | 422 ms: 1.11x faster                                             |
| async_tree_none            | 497 ms                                                   | 455 ms: 1.09x faster                                             |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 718 ms: 1.07x faster                                             |
| deepcopy_reduce            | 4.07 us                                                  | 3.83 us: 1.06x faster                                            |
| pathlib                    | 22.7 ms                                                  | 21.6 ms: 1.05x faster                                            |
| scimark_sor                | 160 ms                                                   | 152 ms: 1.05x faster                                             |
| xml_etree_parse            | 197 ms                                                   | 188 ms: 1.05x faster                                             |
| python_startup             | 15.4 ms                                                  | 14.7 ms: 1.05x faster                                            |
| nbody                      | 114 ms                                                   | 110 ms: 1.04x faster                                             |
| json                       | 5.73 ms                                                  | 5.53 ms: 1.04x faster                                            |
| mako                       | 13.4 ms                                                  | 12.9 ms: 1.03x faster                                            |
| regex_dna                  | 253 ms                                                   | 247 ms: 1.03x faster                                             |
| telco                      | 9.74 ms                                                  | 9.53 ms: 1.02x faster                                            |
| json_loads                 | 31.7 us                                                  | 31.2 us: 1.01x faster                                            |
| thrift                     | 968 us                                                   | 958 us: 1.01x faster                                             |
| scimark_fft                | 447 ms                                                   | 443 ms: 1.01x faster                                             |
| regex_v8                   | 31.8 ms                                                  | 31.5 ms: 1.01x faster                                            |
| float                      | 93.3 ms                                                  | 93.8 ms: 1.01x slower                                            |
| xml_etree_iterparse        | 149 ms                                                   | 151 ms: 1.01x slower                                             |
| logging_silent             | 133 ns                                                   | 135 ns: 1.02x slower                                             |
| coverage                   | 99.1 ms                                                  | 103 ms: 1.04x slower                                             |
| tomli_loads                | 2.54 sec                                                 | 2.64 sec: 1.04x slower                                           |
| scimark_sparse_mat_mult    | 6.51 ms                                                  | 6.80 ms: 1.04x slower                                            |
| async_generators           | 489 ms                                                   | 510 ms: 1.04x slower                                             |
| bpe_tokeniser              | 5.87 sec                                                 | 6.13 sec: 1.04x slower                                           |
| mdp                        | 3.34 sec                                                 | 3.49 sec: 1.05x slower                                           |
| async_tree_io_tg           | 1.13 sec                                                 | 1.19 sec: 1.05x slower                                           |
| logging_format             | 7.82 us                                                  | 8.22 us: 1.05x slower                                            |
| crypto_pyaes               | 83.7 ms                                                  | 88.5 ms: 1.06x slower                                            |
| spectral_norm              | 143 ms                                                   | 152 ms: 1.06x slower                                             |
| unpickle_pure_python       | 251 us                                                   | 267 us: 1.07x slower                                             |
| gc_traversal               | 5.77 ms                                                  | 6.17 ms: 1.07x slower                                            |
| create_gc_cycles           | 3.35 ms                                                  | 3.58 ms: 1.07x slower                                            |
| scimark_lu                 | 139 ms                                                   | 149 ms: 1.07x slower                                             |
| typing_runtime_protocols   | 193 us                                                   | 207 us: 1.07x slower                                             |
| html5lib                   | 66.4 ms                                                  | 71.1 ms: 1.07x slower                                            |
| logging_simple             | 7.07 us                                                  | 7.62 us: 1.08x slower                                            |
| async_tree_io              | 1.11 sec                                                 | 1.20 sec: 1.08x slower                                           |
| pickle_pure_python         | 357 us                                                   | 388 us: 1.09x slower                                             |
| scimark_monte_carlo        | 83.6 ms                                                  | 90.9 ms: 1.09x slower                                            |
| meteor_contest             | 114 ms                                                   | 125 ms: 1.10x slower                                             |
| bench_thread_pool          | 1.27 ms                                                  | 1.40 ms: 1.10x slower                                            |
| pyflate                    | 556 ms                                                   | 621 ms: 1.12x slower                                             |
| fannkuch                   | 461 ms                                                   | 519 ms: 1.13x slower                                             |
| tornado_http               | 128 ms                                                   | 146 ms: 1.14x slower                                             |
| raytrace                   | 300 ms                                                   | 347 ms: 1.16x slower                                             |
| pycparser                  | 1.27 sec                                                 | 1.48 sec: 1.16x slower                                           |
| deltablue                  | 3.82 ms                                                  | 4.47 ms: 1.17x slower                                            |
| go                         | 160 ms                                                   | 189 ms: 1.18x slower                                             |
| nqueens                    | 100 ms                                                   | 121 ms: 1.21x slower                                             |
| sphinx                     | 1.17 sec                                                 | 1.42 sec: 1.21x slower                                           |
| sqlglot_normalize          | 127 ms                                                   | 154 ms: 1.22x slower                                             |
| sqlglot_parse              | 1.38 ms                                                  | 1.69 ms: 1.22x slower                                            |
| comprehensions             | 20.4 us                                                  | 24.9 us: 1.22x slower                                            |
| 2to3                       | 304 ms                                                   | 375 ms: 1.24x slower                                             |
| django_template            | 41.6 ms                                                  | 52.3 ms: 1.26x slower                                            |
| genshi_text                | 27.7 ms                                                  | 35.0 ms: 1.26x slower                                            |
| chaos                      | 68.0 ms                                                  | 86.0 ms: 1.27x slower                                            |
| sqlglot_transpile          | 1.73 ms                                                  | 2.20 ms: 1.27x slower                                            |
| docutils                   | 2.89 sec                                                 | 3.67 sec: 1.27x slower                                           |
| richards_super             | 60.1 ms                                                  | 76.3 ms: 1.27x slower                                            |
| sqlglot_optimize           | 62.2 ms                                                  | 79.2 ms: 1.27x slower                                            |
| richards                   | 53.6 ms                                                  | 68.8 ms: 1.28x slower                                            |
| sympy_expand               | 457 ms                                                   | 593 ms: 1.30x slower                                             |
| pprint_safe_repr           | 926 ms                                                   | 1.22 sec: 1.32x slower                                           |
| sympy_str                  | 264 ms                                                   | 355 ms: 1.34x slower                                             |
| pprint_pformat             | 1.90 sec                                                 | 2.60 sec: 1.37x slower                                           |
| regex_compile              | 127 ms                                                   | 176 ms: 1.39x slower                                             |
| sympy_integrate            | 20.8 ms                                                  | 28.9 ms: 1.39x slower                                            |
| genshi_xml                 | 60.3 ms                                                  | 85.1 ms: 1.41x slower                                            |
| pylint                     | 342 ms                                                   | 483 ms: 1.41x slower                                             |
| hexiom                     | 7.11 ms                                                  | 10.4 ms: 1.46x slower                                            |
| sympy_sum                  | 144 ms                                                   | 210 ms: 1.46x slower                                             |
| generators                 | 37.6 ms                                                  | 59.3 ms: 1.58x slower                                            |
| bench_mp_pool              | 7.68 ms                                                  | 3.29 sec: 427.70x slower                                         |
| Geometric mean             | (ref)                                                    | 1.17x slower                                                     |

Benchmark hidden because not significant (9): json_dumps, async_tree_cpu_io_mixed, xml_etree_generate, coroutines, xml_etree_process, regex_effbot, python_startup_no_site, asyncio_websockets, pidigits
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (10) of results/bm-20241017-3.14.0a0-c2fad93-JIT/bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.087x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: 1.09x