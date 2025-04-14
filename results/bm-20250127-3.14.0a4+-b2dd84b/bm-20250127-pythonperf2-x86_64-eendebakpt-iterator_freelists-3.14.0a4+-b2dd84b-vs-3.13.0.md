# Results vs. 3.13.0

- fork: eendebakpt
- ref: iterator_freelists
- machine: linux-x86_64
- commit hash: b2dd84b
- commit date: 2025-01-27
- overall geometric mean: 1.071x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250127-pythonperf2-x86_64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 279 ms: 1.05x faster                                                           |
| docutils       | 2.83 sec                                                     | 2.85 sec: 1.01x slower                                                         |
| html5lib       | 73.5 ms                                                      | 65.0 ms: 1.13x faster                                                          |
| sphinx         | 1.12 sec                                                     | 1.10 sec: 1.02x faster                                                         |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250127-pythonperf2-x86_64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 334 ms: 1.40x faster                                                           |
| async_tree_io              | 843 ms                                                       | 640 ms: 1.32x faster                                                           |
| async_tree_none            | 376 ms                                                       | 287 ms: 1.31x faster                                                           |
| async_tree_memoization     | 453 ms                                                       | 346 ms: 1.31x faster                                                           |
| async_tree_io_tg           | 831 ms                                                       | 646 ms: 1.29x faster                                                           |
| async_tree_none_tg         | 346 ms                                                       | 279 ms: 1.24x faster                                                           |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 514 ms: 1.17x faster                                                           |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 504 ms: 1.15x faster                                                           |
| async_generators           | 457 ms                                                       | 410 ms: 1.11x faster                                                           |
| coroutines                 | 21.6 ms                                                      | 20.8 ms: 1.04x faster                                                          |
| asyncio_websockets         | 388 ms                                                       | 384 ms: 1.01x faster                                                           |
| Geometric mean             | (ref)                                                        | 1.21x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250127-pythonperf2-x86_64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 69.2 ms: 1.18x faster                                                          |
| nbody          | 89.3 ms                                                      | 86.9 ms: 1.03x faster                                                          |
| pidigits       | 252 ms                                                       | 254 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250127-pythonperf2-x86_64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.10 ms: 1.18x faster                                                          |
| regex_dna      | 247 ms                                                       | 231 ms: 1.07x faster                                                           |
| regex_compile  | 143 ms                                                       | 134 ms: 1.07x faster                                                           |
| regex_v8       | 26.1 ms                                                      | 25.2 ms: 1.04x faster                                                          |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250127-pythonperf2-x86_64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.05 sec: 1.20x faster                                                         |
| xml_etree_parse      | 150 ms                                                       | 136 ms: 1.11x faster                                                           |
| xml_etree_iterparse  | 103 ms                                                       | 96.1 ms: 1.07x faster                                                          |
| unpickle_pure_python | 217 us                                                       | 207 us: 1.05x faster                                                           |
| xml_etree_generate   | 86.5 ms                                                      | 82.7 ms: 1.05x faster                                                          |
| xml_etree_process    | 61.2 ms                                                      | 58.5 ms: 1.04x faster                                                          |
| json_dumps           | 11.1 ms                                                      | 11.4 ms: 1.03x slower                                                          |
| json_loads           | 24.7 us                                                      | 26.0 us: 1.05x slower                                                          |
| Geometric mean       | (ref)                                                        | 1.05x faster                                                                   |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250127-pythonperf2-x86_64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 8.96 ms                                                      | 8.93 ms: 1.00x faster                                                          |
| Geometric mean         | (ref)                                                        | 1.00x faster                                                                   |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250127-pythonperf2-x86_64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 23.0 ms: 1.14x faster                                                          |
| genshi_xml      | 57.1 ms                                                      | 51.7 ms: 1.10x faster                                                          |
| django_template | 36.4 ms                                                      | 35.0 ms: 1.04x faster                                                          |
| mako            | 10.4 ms                                                      | 10.8 ms: 1.05x slower                                                          |
| Geometric mean  | (ref)                                                        | 1.06x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250127-pythonperf2-x86_64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy                   | 392 us                                                       | 278 us: 1.41x faster                                                           |
| async_tree_memoization_tg  | 466 ms                                                       | 334 ms: 1.40x faster                                                           |
| go                         | 162 ms                                                       | 122 ms: 1.33x faster                                                           |
| deepcopy_memo              | 38.6 us                                                      | 29.2 us: 1.32x faster                                                          |
| async_tree_io              | 843 ms                                                       | 640 ms: 1.32x faster                                                           |
| async_tree_none            | 376 ms                                                       | 287 ms: 1.31x faster                                                           |
| async_tree_memoization     | 453 ms                                                       | 346 ms: 1.31x faster                                                           |
| async_tree_io_tg           | 831 ms                                                       | 646 ms: 1.29x faster                                                           |
| async_tree_none_tg         | 346 ms                                                       | 279 ms: 1.24x faster                                                           |
| deepcopy_reduce            | 3.54 us                                                      | 2.93 us: 1.21x faster                                                          |
| tomli_loads                | 2.46 sec                                                     | 2.05 sec: 1.20x faster                                                         |
| generators                 | 33.6 ms                                                      | 28.3 ms: 1.19x faster                                                          |
| regex_effbot               | 3.67 ms                                                      | 3.10 ms: 1.18x faster                                                          |
| float                      | 81.3 ms                                                      | 69.2 ms: 1.18x faster                                                          |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 514 ms: 1.17x faster                                                           |
| pyflate                    | 503 ms                                                       | 432 ms: 1.16x faster                                                           |
| spectral_norm              | 97.0 ms                                                      | 83.6 ms: 1.16x faster                                                          |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 504 ms: 1.15x faster                                                           |
| richards_super             | 59.6 ms                                                      | 51.7 ms: 1.15x faster                                                          |
| richards                   | 52.9 ms                                                      | 46.2 ms: 1.15x faster                                                          |
| genshi_text                | 26.2 ms                                                      | 23.0 ms: 1.14x faster                                                          |
| html5lib                   | 73.5 ms                                                      | 65.0 ms: 1.13x faster                                                          |
| bpe_tokeniser              | 5.09 sec                                                     | 4.55 sec: 1.12x faster                                                         |
| pylint                     | 347 ms                                                       | 311 ms: 1.12x faster                                                           |
| pathlib                    | 17.5 ms                                                      | 15.7 ms: 1.11x faster                                                          |
| async_generators           | 457 ms                                                       | 410 ms: 1.11x faster                                                           |
| xml_etree_parse            | 150 ms                                                       | 136 ms: 1.11x faster                                                           |
| genshi_xml                 | 57.1 ms                                                      | 51.7 ms: 1.10x faster                                                          |
| telco                      | 8.79 ms                                                      | 7.97 ms: 1.10x faster                                                          |
| pprint_safe_repr           | 843 ms                                                       | 770 ms: 1.09x faster                                                           |
| pprint_pformat             | 1.72 sec                                                     | 1.57 sec: 1.09x faster                                                         |
| hexiom                     | 6.55 ms                                                      | 6.07 ms: 1.08x faster                                                          |
| scimark_sor                | 123 ms                                                       | 114 ms: 1.08x faster                                                           |
| regex_dna                  | 247 ms                                                       | 231 ms: 1.07x faster                                                           |
| xml_etree_iterparse        | 103 ms                                                       | 96.1 ms: 1.07x faster                                                          |
| thrift                     | 901 us                                                       | 843 us: 1.07x faster                                                           |
| regex_compile              | 143 ms                                                       | 134 ms: 1.07x faster                                                           |
| sqlglot_optimize           | 59.3 ms                                                      | 55.7 ms: 1.06x faster                                                          |
| sqlglot_parse              | 1.40 ms                                                      | 1.32 ms: 1.06x faster                                                          |
| scimark_fft                | 328 ms                                                       | 309 ms: 1.06x faster                                                           |
| sqlglot_normalize          | 119 ms                                                       | 113 ms: 1.06x faster                                                           |
| scimark_lu                 | 98.7 ms                                                      | 93.2 ms: 1.06x faster                                                          |
| logging_simple             | 6.39 us                                                      | 6.06 us: 1.06x faster                                                          |
| unpickle_pure_python       | 217 us                                                       | 207 us: 1.05x faster                                                           |
| json                       | 5.69 ms                                                      | 5.41 ms: 1.05x faster                                                          |
| sqlglot_transpile          | 1.79 ms                                                      | 1.70 ms: 1.05x faster                                                          |
| deltablue                  | 3.42 ms                                                      | 3.25 ms: 1.05x faster                                                          |
| sympy_expand               | 509 ms                                                       | 485 ms: 1.05x faster                                                           |
| 2to3                       | 293 ms                                                       | 279 ms: 1.05x faster                                                           |
| mdp                        | 2.54 sec                                                     | 2.42 sec: 1.05x faster                                                         |
| xml_etree_generate         | 86.5 ms                                                      | 82.7 ms: 1.05x faster                                                          |
| sympy_str                  | 298 ms                                                       | 285 ms: 1.05x faster                                                           |
| sqlalchemy_declarative     | 148 ms                                                       | 142 ms: 1.05x faster                                                           |
| shortest_path              | 460 ms                                                       | 440 ms: 1.05x faster                                                           |
| xml_etree_process          | 61.2 ms                                                      | 58.5 ms: 1.04x faster                                                          |
| sqlalchemy_imperative      | 18.3 ms                                                      | 17.5 ms: 1.04x faster                                                          |
| logging_format             | 6.94 us                                                      | 6.66 us: 1.04x faster                                                          |
| connected_components       | 432 ms                                                       | 415 ms: 1.04x faster                                                           |
| django_template            | 36.4 ms                                                      | 35.0 ms: 1.04x faster                                                          |
| regex_v8                   | 26.1 ms                                                      | 25.2 ms: 1.04x faster                                                          |
| k_core                     | 2.17 sec                                                     | 2.09 sec: 1.04x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 20.8 ms: 1.04x faster                                                          |
| sympy_sum                  | 155 ms                                                       | 149 ms: 1.04x faster                                                           |
| sqlite_synth               | 2.91 us                                                      | 2.80 us: 1.04x faster                                                          |
| meteor_contest             | 130 ms                                                       | 125 ms: 1.03x faster                                                           |
| bench_thread_pool          | 942 us                                                       | 911 us: 1.03x faster                                                           |
| dulwich_log                | 68.2 ms                                                      | 66.0 ms: 1.03x faster                                                          |
| sympy_integrate            | 23.6 ms                                                      | 22.8 ms: 1.03x faster                                                          |
| typing_runtime_protocols   | 169 us                                                       | 164 us: 1.03x faster                                                           |
| nbody                      | 89.3 ms                                                      | 86.9 ms: 1.03x faster                                                          |
| sphinx                     | 1.12 sec                                                     | 1.10 sec: 1.02x faster                                                         |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.69 ms: 1.02x faster                                                          |
| comprehensions             | 17.0 us                                                      | 16.7 us: 1.02x faster                                                          |
| chaos                      | 60.2 ms                                                      | 59.5 ms: 1.01x faster                                                          |
| asyncio_websockets         | 388 ms                                                       | 384 ms: 1.01x faster                                                           |
| pycparser                  | 1.24 sec                                                     | 1.23 sec: 1.01x faster                                                         |
| logging_silent             | 97.9 ns                                                      | 97.1 ns: 1.01x faster                                                          |
| python_startup_no_site     | 8.96 ms                                                      | 8.93 ms: 1.00x faster                                                          |
| pidigits                   | 252 ms                                                       | 254 ms: 1.01x slower                                                           |
| nqueens                    | 90.7 ms                                                      | 91.4 ms: 1.01x slower                                                          |
| docutils                   | 2.83 sec                                                     | 2.85 sec: 1.01x slower                                                         |
| fannkuch                   | 363 ms                                                       | 368 ms: 1.01x slower                                                           |
| create_gc_cycles           | 2.68 ms                                                      | 2.72 ms: 1.01x slower                                                          |
| raytrace                   | 273 ms                                                       | 277 ms: 1.02x slower                                                           |
| coverage                   | 80.0 ms                                                      | 81.3 ms: 1.02x slower                                                          |
| json_dumps                 | 11.1 ms                                                      | 11.4 ms: 1.03x slower                                                          |
| mako                       | 10.4 ms                                                      | 10.8 ms: 1.05x slower                                                          |
| json_loads                 | 24.7 us                                                      | 26.0 us: 1.05x slower                                                          |
| many_optionals             | 930 us                                                       | 995 us: 1.07x slower                                                           |
| subparsers                 | 17.5 ms                                                      | 22.5 ms: 1.29x slower                                                          |
| gc_traversal               | 4.74 ms                                                      | 6.32 ms: 1.33x slower                                                          |
| bench_mp_pool              | 5.12 ms                                                      | 1.16 sec: 226.52x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.01x faster                                                                   |

Benchmark hidden because not significant (4): scimark_monte_carlo, crypto_pyaes, python_startup, pickle_pure_python
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.071x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.02x