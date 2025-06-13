# Results vs. 3.13.0

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-x86_64
- commit hash: f603929
- commit date: 2025-06-13
- overall geometric mean: 1.121x slower
- HPT reliability: 99.92%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 331 ms: 1.13x slower                                                                |
| docutils       | 2.83 sec                                                     | 3.19 sec: 1.13x slower                                                              |
| html5lib       | 73.5 ms                                                      | 70.9 ms: 1.04x faster                                                               |
| sphinx         | 1.12 sec                                                     | 1.15 sec: 1.02x slower                                                              |
| Geometric mean | (ref)                                                        | 1.06x slower                                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 361 ms: 1.29x faster                                                                |
| async_tree_memoization     | 453 ms                                                       | 364 ms: 1.25x faster                                                                |
| async_tree_io              | 843 ms                                                       | 679 ms: 1.24x faster                                                                |
| async_tree_io_tg           | 831 ms                                                       | 683 ms: 1.22x faster                                                                |
| async_tree_none            | 376 ms                                                       | 315 ms: 1.19x faster                                                                |
| async_tree_none_tg         | 346 ms                                                       | 296 ms: 1.17x faster                                                                |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 540 ms: 1.12x faster                                                                |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 535 ms: 1.09x faster                                                                |
| asyncio_websockets         | 388 ms                                                       | 385 ms: 1.01x faster                                                                |
| async_generators           | 457 ms                                                       | 462 ms: 1.01x slower                                                                |
| coroutines                 | 21.6 ms                                                      | 22.6 ms: 1.05x slower                                                               |
| Geometric mean             | (ref)                                                        | 1.13x faster                                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| pidigits       | 252 ms                                                       | 260 ms: 1.03x slower                                                                |
| float          | 81.3 ms                                                      | 112 ms: 1.37x slower                                                                |
| nbody          | 89.3 ms                                                      | 216 ms: 2.42x slower                                                                |
| Geometric mean | (ref)                                                        | 1.51x slower                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_dna      | 247 ms                                                       | 222 ms: 1.11x faster                                                                |
| regex_v8       | 26.1 ms                                                      | 25.2 ms: 1.04x faster                                                               |
| regex_effbot   | 3.67 ms                                                      | 3.75 ms: 1.02x slower                                                               |
| regex_compile  | 143 ms                                                       | 164 ms: 1.15x slower                                                                |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| xml_etree_parse      | 150 ms                                                       | 145 ms: 1.04x faster                                                                |
| json_loads           | 24.7 us                                                      | 24.9 us: 1.01x slower                                                               |
| xml_etree_iterparse  | 103 ms                                                       | 110 ms: 1.07x slower                                                                |
| xml_etree_process    | 61.2 ms                                                      | 80.7 ms: 1.32x slower                                                               |
| xml_etree_generate   | 86.5 ms                                                      | 115 ms: 1.33x slower                                                                |
| pickle_pure_python   | 323 us                                                       | 432 us: 1.34x slower                                                                |
| tomli_loads          | 2.46 sec                                                     | 3.34 sec: 1.35x slower                                                              |
| unpickle_pure_python | 217 us                                                       | 425 us: 1.95x slower                                                                |
| Geometric mean       | (ref)                                                        | 1.23x slower                                                                        |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 15.3 ms: 1.04x faster                                                               |
| python_startup_no_site | 8.96 ms                                                      | 8.82 ms: 1.02x faster                                                               |
| Geometric mean         | (ref)                                                        | 1.03x faster                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 23.3 ms: 1.13x faster                                                               |
| django_template | 36.4 ms                                                      | 35.6 ms: 1.02x faster                                                               |
| genshi_xml      | 57.1 ms                                                      | 56.4 ms: 1.01x faster                                                               |
| mako            | 10.4 ms                                                      | 19.9 ms: 1.92x slower                                                               |
| Geometric mean  | (ref)                                                        | 1.13x slower                                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.51 sec: 1.68x faster                                                              |
| deepcopy_memo              | 38.6 us                                                      | 27.3 us: 1.41x faster                                                               |
| deepcopy                   | 392 us                                                       | 278 us: 1.41x faster                                                                |
| async_tree_memoization_tg  | 466 ms                                                       | 361 ms: 1.29x faster                                                                |
| async_tree_memoization     | 453 ms                                                       | 364 ms: 1.25x faster                                                                |
| async_tree_io              | 843 ms                                                       | 679 ms: 1.24x faster                                                                |
| async_tree_io_tg           | 831 ms                                                       | 683 ms: 1.22x faster                                                                |
| generators                 | 33.6 ms                                                      | 27.9 ms: 1.21x faster                                                               |
| deepcopy_reduce            | 3.54 us                                                      | 2.94 us: 1.21x faster                                                               |
| async_tree_none            | 376 ms                                                       | 315 ms: 1.19x faster                                                                |
| scimark_sor                | 123 ms                                                       | 104 ms: 1.19x faster                                                                |
| async_tree_none_tg         | 346 ms                                                       | 296 ms: 1.17x faster                                                                |
| genshi_text                | 26.2 ms                                                      | 23.3 ms: 1.13x faster                                                               |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 540 ms: 1.12x faster                                                                |
| regex_dna                  | 247 ms                                                       | 222 ms: 1.11x faster                                                                |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 535 ms: 1.09x faster                                                                |
| dulwich_log                | 68.2 ms                                                      | 63.6 ms: 1.07x faster                                                               |
| thrift                     | 901 us                                                       | 841 us: 1.07x faster                                                                |
| scimark_lu                 | 98.7 ms                                                      | 93.3 ms: 1.06x faster                                                               |
| json                       | 5.69 ms                                                      | 5.38 ms: 1.06x faster                                                               |
| python_startup             | 15.9 ms                                                      | 15.3 ms: 1.04x faster                                                               |
| regex_v8                   | 26.1 ms                                                      | 25.2 ms: 1.04x faster                                                               |
| html5lib                   | 73.5 ms                                                      | 70.9 ms: 1.04x faster                                                               |
| xml_etree_parse            | 150 ms                                                       | 145 ms: 1.04x faster                                                                |
| coverage                   | 80.0 ms                                                      | 77.5 ms: 1.03x faster                                                               |
| django_template            | 36.4 ms                                                      | 35.6 ms: 1.02x faster                                                               |
| python_startup_no_site     | 8.96 ms                                                      | 8.82 ms: 1.02x faster                                                               |
| genshi_xml                 | 57.1 ms                                                      | 56.4 ms: 1.01x faster                                                               |
| asyncio_websockets         | 388 ms                                                       | 385 ms: 1.01x faster                                                                |
| pathlib                    | 17.5 ms                                                      | 17.5 ms: 1.00x faster                                                               |
| logging_simple             | 6.39 us                                                      | 6.42 us: 1.00x slower                                                               |
| json_loads                 | 24.7 us                                                      | 24.9 us: 1.01x slower                                                               |
| async_generators           | 457 ms                                                       | 462 ms: 1.01x slower                                                                |
| sympy_integrate            | 23.6 ms                                                      | 23.9 ms: 1.01x slower                                                               |
| logging_format             | 6.94 us                                                      | 7.04 us: 1.01x slower                                                               |
| regex_effbot               | 3.67 ms                                                      | 3.75 ms: 1.02x slower                                                               |
| sphinx                     | 1.12 sec                                                     | 1.15 sec: 1.02x slower                                                              |
| pidigits                   | 252 ms                                                       | 260 ms: 1.03x slower                                                                |
| create_gc_cycles           | 2.68 ms                                                      | 2.80 ms: 1.04x slower                                                               |
| coroutines                 | 21.6 ms                                                      | 22.6 ms: 1.05x slower                                                               |
| sqlite_synth               | 2.91 us                                                      | 3.07 us: 1.06x slower                                                               |
| sympy_sum                  | 155 ms                                                       | 164 ms: 1.06x slower                                                                |
| xml_etree_iterparse        | 103 ms                                                       | 110 ms: 1.07x slower                                                                |
| sympy_str                  | 298 ms                                                       | 321 ms: 1.08x slower                                                                |
| richards_super             | 59.6 ms                                                      | 64.5 ms: 1.08x slower                                                               |
| chaos                      | 60.2 ms                                                      | 65.3 ms: 1.08x slower                                                               |
| k_core                     | 2.17 sec                                                     | 2.36 sec: 1.09x slower                                                              |
| richards                   | 52.9 ms                                                      | 57.9 ms: 1.09x slower                                                               |
| telco                      | 8.79 ms                                                      | 9.67 ms: 1.10x slower                                                               |
| sympy_expand               | 509 ms                                                       | 562 ms: 1.10x slower                                                                |
| 2to3                       | 293 ms                                                       | 331 ms: 1.13x slower                                                                |
| docutils                   | 2.83 sec                                                     | 3.19 sec: 1.13x slower                                                              |
| regex_compile              | 143 ms                                                       | 164 ms: 1.15x slower                                                                |
| shortest_path              | 460 ms                                                       | 532 ms: 1.16x slower                                                                |
| many_optionals             | 930 us                                                       | 1.10 ms: 1.18x slower                                                               |
| nqueens                    | 90.7 ms                                                      | 110 ms: 1.21x slower                                                                |
| connected_components       | 432 ms                                                       | 528 ms: 1.22x slower                                                                |
| raytrace                   | 273 ms                                                       | 339 ms: 1.24x slower                                                                |
| pycparser                  | 1.24 sec                                                     | 1.55 sec: 1.25x slower                                                              |
| typing_runtime_protocols   | 169 us                                                       | 215 us: 1.27x slower                                                                |
| xml_etree_process          | 61.2 ms                                                      | 80.7 ms: 1.32x slower                                                               |
| xml_etree_generate         | 86.5 ms                                                      | 115 ms: 1.33x slower                                                                |
| pickle_pure_python         | 323 us                                                       | 432 us: 1.34x slower                                                                |
| meteor_contest             | 130 ms                                                       | 174 ms: 1.34x slower                                                                |
| gc_traversal               | 4.74 ms                                                      | 6.38 ms: 1.35x slower                                                               |
| tomli_loads                | 2.46 sec                                                     | 3.34 sec: 1.35x slower                                                              |
| float                      | 81.3 ms                                                      | 112 ms: 1.37x slower                                                                |
| pyflate                    | 503 ms                                                       | 691 ms: 1.37x slower                                                                |
| bpe_tokeniser              | 5.09 sec                                                     | 7.23 sec: 1.42x slower                                                              |
| subparsers                 | 17.5 ms                                                      | 25.8 ms: 1.48x slower                                                               |
| scimark_monte_carlo        | 66.1 ms                                                      | 97.8 ms: 1.48x slower                                                               |
| go                         | 162 ms                                                       | 249 ms: 1.53x slower                                                                |
| pprint_pformat             | 1.72 sec                                                     | 2.67 sec: 1.55x slower                                                              |
| pprint_safe_repr           | 843 ms                                                       | 1.31 sec: 1.56x slower                                                              |
| crypto_pyaes               | 73.3 ms                                                      | 117 ms: 1.59x slower                                                                |
| scimark_fft                | 328 ms                                                       | 538 ms: 1.64x slower                                                                |
| hexiom                     | 6.55 ms                                                      | 11.7 ms: 1.78x slower                                                               |
| deltablue                  | 3.42 ms                                                      | 6.51 ms: 1.91x slower                                                               |
| mako                       | 10.4 ms                                                      | 19.9 ms: 1.92x slower                                                               |
| comprehensions             | 17.0 us                                                      | 33.2 us: 1.95x slower                                                               |
| unpickle_pure_python       | 217 us                                                       | 425 us: 1.95x slower                                                                |
| fannkuch                   | 363 ms                                                       | 725 ms: 2.00x slower                                                                |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 9.65 ms: 2.02x slower                                                               |
| spectral_norm              | 97.0 ms                                                      | 214 ms: 2.21x slower                                                                |
| nbody                      | 89.3 ms                                                      | 216 ms: 2.42x slower                                                                |
| logging_silent             | 97.9 ns                                                      | 501 ns: 5.11x slower                                                                |
| Geometric mean             | (ref)                                                        | 1.15x slower                                                                        |

Benchmark hidden because not significant (3): pylint, djangocms, json_dumps
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250613-3.15.0a0-f603929-PYTHON_UOPS/bm-20250613-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.121x slower

# HPT report

- Reliability score: 99.92% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.09x