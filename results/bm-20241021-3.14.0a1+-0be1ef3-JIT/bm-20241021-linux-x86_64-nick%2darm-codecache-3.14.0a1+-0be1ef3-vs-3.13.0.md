# Results vs. 3.13.0

- fork: nick-arm
- ref: codecache
- machine: linux-x86_64
- commit hash: 0be1ef3
- commit date: 2024-10-21
- overall geometric mean: 1.009x faster
- HPT reliability: 56.70%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 276 ms: 1.03x slower                                            |
| docutils       | 2.59 sec                                               | 2.91 sec: 1.12x slower                                          |
| html5lib       | 64.2 ms                                                | 67.1 ms: 1.05x slower                                           |
| sphinx         | 1.03 sec                                               | 1.16 sec: 1.12x slower                                          |
| tornado_http   | 92.4 ms                                                | 94.8 ms: 1.03x slower                                           |
| Geometric mean | (ref)                                                  | 1.07x slower                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 377 ms: 1.23x faster                                            |
| async_tree_memoization     | 442 ms                                                 | 418 ms: 1.06x faster                                            |
| async_tree_none            | 351 ms                                                 | 339 ms: 1.04x faster                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 556 ms: 1.02x slower                                            |
| async_tree_io              | 842 ms                                                 | 858 ms: 1.02x slower                                            |
| coroutines                 | 22.7 ms                                                | 23.7 ms: 1.04x slower                                           |
| async_generators           | 436 ms                                                 | 457 ms: 1.05x slower                                            |
| async_tree_io_tg           | 857 ms                                                 | 976 ms: 1.14x slower                                            |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                    |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, async_tree_none_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 87.0 ms                                                | 82.3 ms: 1.06x faster                                           |
| float          | 79.2 ms                                                | 75.6 ms: 1.05x faster                                           |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                            |
| Geometric mean | (ref)                                                  | 1.03x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.7 ms: 1.06x faster                                           |
| regex_dna      | 218 ms                                                 | 214 ms: 1.02x faster                                            |
| regex_effbot   | 3.73 ms                                                | 3.72 ms: 1.00x faster                                           |
| regex_compile  | 132 ms                                                 | 139 ms: 1.05x slower                                            |
| Geometric mean | (ref)                                                  | 1.01x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|--------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| tomli_loads        | 2.14 sec                                               | 1.90 sec: 1.13x faster                                          |
| xml_etree_generate | 86.7 ms                                                | 78.2 ms: 1.11x faster                                           |
| xml_etree_process  | 60.6 ms                                                | 54.8 ms: 1.11x faster                                           |
| xml_etree_parse    | 156 ms                                                 | 148 ms: 1.05x faster                                            |
| json_loads         | 27.2 us                                                | 26.8 us: 1.02x faster                                           |
| json_dumps         | 10.6 ms                                                | 10.8 ms: 1.02x slower                                           |
| Geometric mean     | (ref)                                                  | 1.04x faster                                                    |

Benchmark hidden because not significant (3): unpickle_pure_python, pickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 11.8 ms: 1.06x faster                                           |
| python_startup_no_site | 6.96 ms                                                | 7.07 ms: 1.02x slower                                           |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.2 ms: 1.09x faster                                           |
| django_template | 35.2 ms                                                | 35.8 ms: 1.02x slower                                           |
| genshi_text     | 23.5 ms                                                | 25.8 ms: 1.09x slower                                           |
| genshi_xml      | 50.9 ms                                                | 60.4 ms: 1.19x slower                                           |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| deepcopy                   | 358 us                                                 | 266 us: 1.35x faster                                            |
| deepcopy_memo              | 39.1 us                                                | 29.1 us: 1.34x faster                                           |
| async_tree_memoization_tg  | 464 ms                                                 | 377 ms: 1.23x faster                                            |
| richards                   | 48.7 ms                                                | 40.8 ms: 1.19x faster                                           |
| deepcopy_reduce            | 3.20 us                                                | 2.73 us: 1.17x faster                                           |
| scimark_fft                | 364 ms                                                 | 315 ms: 1.16x faster                                            |
| richards_super             | 54.9 ms                                                | 47.6 ms: 1.15x faster                                           |
| telco                      | 8.54 ms                                                | 7.58 ms: 1.13x faster                                           |
| tomli_loads                | 2.14 sec                                               | 1.90 sec: 1.13x faster                                          |
| xml_etree_generate         | 86.7 ms                                                | 78.2 ms: 1.11x faster                                           |
| xml_etree_process          | 60.6 ms                                                | 54.8 ms: 1.11x faster                                           |
| crypto_pyaes               | 75.3 ms                                                | 68.6 ms: 1.10x faster                                           |
| pathlib                    | 17.5 ms                                                | 16.0 ms: 1.10x faster                                           |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.63 ms: 1.09x faster                                           |
| mako                       | 11.1 ms                                                | 10.2 ms: 1.09x faster                                           |
| go                         | 144 ms                                                 | 133 ms: 1.08x faster                                            |
| json                       | 5.36 ms                                                | 5.00 ms: 1.07x faster                                           |
| mdp                        | 2.72 sec                                               | 2.54 sec: 1.07x faster                                          |
| regex_v8                   | 26.2 ms                                                | 24.7 ms: 1.06x faster                                           |
| bpe_tokeniser              | 4.75 sec                                               | 4.46 sec: 1.06x faster                                          |
| fannkuch                   | 404 ms                                                 | 381 ms: 1.06x faster                                            |
| async_tree_memoization     | 442 ms                                                 | 418 ms: 1.06x faster                                            |
| pycparser                  | 1.20 sec                                               | 1.14 sec: 1.06x faster                                          |
| nbody                      | 87.0 ms                                                | 82.3 ms: 1.06x faster                                           |
| python_startup             | 12.5 ms                                                | 11.8 ms: 1.06x faster                                           |
| pyflate                    | 471 ms                                                 | 447 ms: 1.05x faster                                            |
| scimark_monte_carlo        | 67.4 ms                                                | 64.3 ms: 1.05x faster                                           |
| xml_etree_parse            | 156 ms                                                 | 148 ms: 1.05x faster                                            |
| logging_format             | 6.40 us                                                | 6.10 us: 1.05x faster                                           |
| logging_silent             | 102 ns                                                 | 97.1 ns: 1.05x faster                                           |
| float                      | 79.2 ms                                                | 75.6 ms: 1.05x faster                                           |
| pprint_safe_repr           | 728 ms                                                 | 696 ms: 1.05x faster                                            |
| thrift                     | 809 us                                                 | 779 us: 1.04x faster                                            |
| scimark_sor                | 124 ms                                                 | 119 ms: 1.04x faster                                            |
| async_tree_none            | 351 ms                                                 | 339 ms: 1.04x faster                                            |
| logging_simple             | 5.72 us                                                | 5.57 us: 1.03x faster                                           |
| pprint_pformat             | 1.49 sec                                               | 1.46 sec: 1.02x faster                                          |
| regex_dna                  | 218 ms                                                 | 214 ms: 1.02x faster                                            |
| meteor_contest             | 109 ms                                                 | 107 ms: 1.02x faster                                            |
| json_loads                 | 27.2 us                                                | 26.8 us: 1.02x faster                                           |
| spectral_norm              | 115 ms                                                 | 115 ms: 1.00x faster                                            |
| regex_effbot               | 3.73 ms                                                | 3.72 ms: 1.00x faster                                           |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                            |
| gc_traversal               | 4.37 ms                                                | 4.37 ms: 1.00x slower                                           |
| coverage                   | 84.0 ms                                                | 84.4 ms: 1.00x slower                                           |
| deltablue                  | 3.23 ms                                                | 3.27 ms: 1.01x slower                                           |
| python_startup_no_site     | 6.96 ms                                                | 7.07 ms: 1.02x slower                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 556 ms: 1.02x slower                                            |
| chaos                      | 58.1 ms                                                | 59.1 ms: 1.02x slower                                           |
| django_template            | 35.2 ms                                                | 35.8 ms: 1.02x slower                                           |
| async_tree_io              | 842 ms                                                 | 858 ms: 1.02x slower                                            |
| raytrace                   | 267 ms                                                 | 273 ms: 1.02x slower                                            |
| json_dumps                 | 10.6 ms                                                | 10.8 ms: 1.02x slower                                           |
| tornado_http               | 92.4 ms                                                | 94.8 ms: 1.03x slower                                           |
| comprehensions             | 16.5 us                                                | 17.0 us: 1.03x slower                                           |
| 2to3                       | 267 ms                                                 | 276 ms: 1.03x slower                                            |
| dulwich_log                | 64.3 ms                                                | 66.9 ms: 1.04x slower                                           |
| coroutines                 | 22.7 ms                                                | 23.7 ms: 1.04x slower                                           |
| html5lib                   | 64.2 ms                                                | 67.1 ms: 1.05x slower                                           |
| regex_compile              | 132 ms                                                 | 139 ms: 1.05x slower                                            |
| async_generators           | 436 ms                                                 | 457 ms: 1.05x slower                                            |
| sqlglot_parse              | 1.27 ms                                                | 1.34 ms: 1.05x slower                                           |
| sqlglot_normalize          | 108 ms                                                 | 113 ms: 1.05x slower                                            |
| sqlglot_transpile          | 1.58 ms                                                | 1.70 ms: 1.07x slower                                           |
| bench_thread_pool          | 822 us                                                 | 881 us: 1.07x slower                                            |
| sympy_expand               | 463 ms                                                 | 498 ms: 1.08x slower                                            |
| sympy_str                  | 275 ms                                                 | 299 ms: 1.09x slower                                            |
| genshi_text                | 23.5 ms                                                | 25.8 ms: 1.09x slower                                           |
| sqlglot_optimize           | 53.7 ms                                                | 59.3 ms: 1.10x slower                                           |
| create_gc_cycles           | 2.41 ms                                                | 2.66 ms: 1.10x slower                                           |
| nqueens                    | 78.4 ms                                                | 87.6 ms: 1.12x slower                                           |
| sphinx                     | 1.03 sec                                               | 1.16 sec: 1.12x slower                                          |
| docutils                   | 2.59 sec                                               | 2.91 sec: 1.12x slower                                          |
| hexiom                     | 6.16 ms                                                | 7.01 ms: 1.14x slower                                           |
| async_tree_io_tg           | 857 ms                                                 | 976 ms: 1.14x slower                                            |
| sympy_sum                  | 150 ms                                                 | 175 ms: 1.16x slower                                            |
| sympy_integrate            | 19.9 ms                                                | 23.3 ms: 1.17x slower                                           |
| genshi_xml                 | 50.9 ms                                                | 60.4 ms: 1.19x slower                                           |
| pylint                     | 313 ms                                                 | 374 ms: 1.19x slower                                            |
| generators                 | 29.0 ms                                                | 35.5 ms: 1.23x slower                                           |
| bench_mp_pool              | 24.0 ms                                                | 83.8 ms: 3.49x slower                                           |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                    |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed, unpickle_pure_python, scimark_lu, pickle_pure_python, typing_runtime_protocols, async_tree_none_tg, xml_etree_iterparse, asyncio_websockets
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.009x faster
# HPT report

- Reliability score: 56.70% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x