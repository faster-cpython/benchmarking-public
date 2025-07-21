# Results vs. 3.13.0

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-x86_64
- commit hash: 53a50eb
- commit date: 2025-07-21
- overall geometric mean: 1.037x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250721-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 286 ms: 1.02x faster                                                                |
| docutils       | 2.83 sec                                                     | 2.94 sec: 1.04x slower                                                              |
| html5lib       | 73.5 ms                                                      | 66.3 ms: 1.11x faster                                                               |
| sphinx         | 1.12 sec                                                     | 1.10 sec: 1.02x faster                                                              |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250721-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 333 ms: 1.40x faster                                                                |
| async_tree_none            | 376 ms                                                       | 274 ms: 1.37x faster                                                                |
| async_tree_memoization     | 453 ms                                                       | 331 ms: 1.37x faster                                                                |
| async_tree_io              | 843 ms                                                       | 625 ms: 1.35x faster                                                                |
| async_tree_io_tg           | 831 ms                                                       | 634 ms: 1.31x faster                                                                |
| async_tree_none_tg         | 346 ms                                                       | 274 ms: 1.26x faster                                                                |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 500 ms: 1.21x faster                                                                |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 510 ms: 1.14x faster                                                                |
| async_generators           | 457 ms                                                       | 447 ms: 1.02x faster                                                                |
| asyncio_websockets         | 388 ms                                                       | 383 ms: 1.01x faster                                                                |
| coroutines                 | 21.6 ms                                                      | 22.6 ms: 1.05x slower                                                               |
| Geometric mean             | (ref)                                                        | 1.21x faster                                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250721-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 61.5 ms: 1.32x faster                                                               |
| pidigits       | 252 ms                                                       | 256 ms: 1.01x slower                                                                |
| Geometric mean | (ref)                                                        | 1.10x faster                                                                        |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250721-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_dna      | 247 ms                                                       | 227 ms: 1.09x faster                                                                |
| regex_compile  | 143 ms                                                       | 133 ms: 1.07x faster                                                                |
| regex_v8       | 26.1 ms                                                      | 24.5 ms: 1.07x faster                                                               |
| regex_effbot   | 3.67 ms                                                      | 3.58 ms: 1.03x faster                                                               |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250721-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 1.94 sec: 1.27x faster                                                              |
| xml_etree_parse      | 150 ms                                                       | 137 ms: 1.10x faster                                                                |
| xml_etree_iterparse  | 103 ms                                                       | 96.4 ms: 1.07x faster                                                               |
| unpickle_pure_python | 217 us                                                       | 204 us: 1.07x faster                                                                |
| xml_etree_process    | 61.2 ms                                                      | 58.2 ms: 1.05x faster                                                               |
| xml_etree_generate   | 86.5 ms                                                      | 83.2 ms: 1.04x faster                                                               |
| json_dumps           | 11.1 ms                                                      | 11.3 ms: 1.02x slower                                                               |
| json_loads           | 24.7 us                                                      | 25.3 us: 1.02x slower                                                               |
| pickle_pure_python   | 323 us                                                       | 338 us: 1.05x slower                                                                |
| Geometric mean       | (ref)                                                        | 1.05x faster                                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250721-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 15.2 ms: 1.04x faster                                                               |
| python_startup_no_site | 8.96 ms                                                      | 8.70 ms: 1.03x faster                                                               |
| Geometric mean         | (ref)                                                        | 1.04x faster                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250721-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 23.3 ms: 1.13x faster                                                               |
| genshi_xml      | 57.1 ms                                                      | 54.5 ms: 1.05x faster                                                               |
| django_template | 36.4 ms                                                      | 35.2 ms: 1.03x faster                                                               |
| Geometric mean  | (ref)                                                        | 1.05x faster                                                                        |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250721-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.29 sec: 1.98x faster                                                              |
| richards                   | 52.9 ms                                                      | 35.5 ms: 1.49x faster                                                               |
| richards_super             | 59.6 ms                                                      | 41.6 ms: 1.43x faster                                                               |
| deepcopy                   | 392 us                                                       | 278 us: 1.41x faster                                                                |
| async_tree_memoization_tg  | 466 ms                                                       | 333 ms: 1.40x faster                                                                |
| async_tree_none            | 376 ms                                                       | 274 ms: 1.37x faster                                                                |
| async_tree_memoization     | 453 ms                                                       | 331 ms: 1.37x faster                                                                |
| deepcopy_memo              | 38.6 us                                                      | 28.4 us: 1.36x faster                                                               |
| async_tree_io              | 843 ms                                                       | 625 ms: 1.35x faster                                                                |
| float                      | 81.3 ms                                                      | 61.5 ms: 1.32x faster                                                               |
| async_tree_io_tg           | 831 ms                                                       | 634 ms: 1.31x faster                                                                |
| go                         | 162 ms                                                       | 126 ms: 1.29x faster                                                                |
| tomli_loads                | 2.46 sec                                                     | 1.94 sec: 1.27x faster                                                              |
| async_tree_none_tg         | 346 ms                                                       | 274 ms: 1.26x faster                                                                |
| spectral_norm              | 97.0 ms                                                      | 79.4 ms: 1.22x faster                                                               |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 500 ms: 1.21x faster                                                                |
| pyflate                    | 503 ms                                                       | 423 ms: 1.19x faster                                                                |
| deltablue                  | 3.42 ms                                                      | 2.92 ms: 1.17x faster                                                               |
| deepcopy_reduce            | 3.54 us                                                      | 3.04 us: 1.17x faster                                                               |
| generators                 | 33.6 ms                                                      | 29.1 ms: 1.16x faster                                                               |
| dulwich_log                | 68.2 ms                                                      | 59.7 ms: 1.14x faster                                                               |
| scimark_sor                | 123 ms                                                       | 108 ms: 1.14x faster                                                                |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 510 ms: 1.14x faster                                                                |
| genshi_text                | 26.2 ms                                                      | 23.3 ms: 1.13x faster                                                               |
| pprint_pformat             | 1.72 sec                                                     | 1.53 sec: 1.13x faster                                                              |
| pprint_safe_repr           | 843 ms                                                       | 753 ms: 1.12x faster                                                                |
| html5lib                   | 73.5 ms                                                      | 66.3 ms: 1.11x faster                                                               |
| bpe_tokeniser              | 5.09 sec                                                     | 4.60 sec: 1.11x faster                                                              |
| xml_etree_parse            | 150 ms                                                       | 137 ms: 1.10x faster                                                                |
| regex_dna                  | 247 ms                                                       | 227 ms: 1.09x faster                                                                |
| scimark_fft                | 328 ms                                                       | 303 ms: 1.08x faster                                                                |
| thrift                     | 901 us                                                       | 837 us: 1.08x faster                                                                |
| regex_compile              | 143 ms                                                       | 133 ms: 1.07x faster                                                                |
| pylint                     | 347 ms                                                       | 323 ms: 1.07x faster                                                                |
| k_core                     | 2.17 sec                                                     | 2.02 sec: 1.07x faster                                                              |
| xml_etree_iterparse        | 103 ms                                                       | 96.4 ms: 1.07x faster                                                               |
| regex_v8                   | 26.1 ms                                                      | 24.5 ms: 1.07x faster                                                               |
| unpickle_pure_python       | 217 us                                                       | 204 us: 1.07x faster                                                                |
| json                       | 5.69 ms                                                      | 5.34 ms: 1.06x faster                                                               |
| connected_components       | 432 ms                                                       | 408 ms: 1.06x faster                                                                |
| meteor_contest             | 130 ms                                                       | 123 ms: 1.05x faster                                                                |
| xml_etree_process          | 61.2 ms                                                      | 58.2 ms: 1.05x faster                                                               |
| logging_silent             | 97.9 ns                                                      | 93.3 ns: 1.05x faster                                                               |
| sympy_integrate            | 23.6 ms                                                      | 22.4 ms: 1.05x faster                                                               |
| genshi_xml                 | 57.1 ms                                                      | 54.5 ms: 1.05x faster                                                               |
| python_startup             | 15.9 ms                                                      | 15.2 ms: 1.04x faster                                                               |
| hexiom                     | 6.55 ms                                                      | 6.28 ms: 1.04x faster                                                               |
| shortest_path              | 460 ms                                                       | 442 ms: 1.04x faster                                                                |
| xml_etree_generate         | 86.5 ms                                                      | 83.2 ms: 1.04x faster                                                               |
| sqlite_synth               | 2.91 us                                                      | 2.81 us: 1.04x faster                                                               |
| scimark_monte_carlo        | 66.1 ms                                                      | 64.0 ms: 1.03x faster                                                               |
| django_template            | 36.4 ms                                                      | 35.2 ms: 1.03x faster                                                               |
| python_startup_no_site     | 8.96 ms                                                      | 8.70 ms: 1.03x faster                                                               |
| pathlib                    | 17.5 ms                                                      | 17.1 ms: 1.03x faster                                                               |
| regex_effbot               | 3.67 ms                                                      | 3.58 ms: 1.03x faster                                                               |
| scimark_lu                 | 98.7 ms                                                      | 96.4 ms: 1.02x faster                                                               |
| 2to3                       | 293 ms                                                       | 286 ms: 1.02x faster                                                                |
| async_generators           | 457 ms                                                       | 447 ms: 1.02x faster                                                                |
| sympy_str                  | 298 ms                                                       | 292 ms: 1.02x faster                                                                |
| sphinx                     | 1.12 sec                                                     | 1.10 sec: 1.02x faster                                                              |
| sympy_expand               | 509 ms                                                       | 500 ms: 1.02x faster                                                                |
| coverage                   | 80.0 ms                                                      | 78.7 ms: 1.02x faster                                                               |
| sympy_sum                  | 155 ms                                                       | 153 ms: 1.01x faster                                                                |
| asyncio_websockets         | 388 ms                                                       | 383 ms: 1.01x faster                                                                |
| logging_simple             | 6.39 us                                                      | 6.32 us: 1.01x faster                                                               |
| logging_format             | 6.94 us                                                      | 6.87 us: 1.01x faster                                                               |
| chaos                      | 60.2 ms                                                      | 60.1 ms: 1.00x faster                                                               |
| pidigits                   | 252 ms                                                       | 256 ms: 1.01x slower                                                                |
| json_dumps                 | 11.1 ms                                                      | 11.3 ms: 1.02x slower                                                               |
| fannkuch                   | 363 ms                                                       | 370 ms: 1.02x slower                                                                |
| nqueens                    | 90.7 ms                                                      | 92.6 ms: 1.02x slower                                                               |
| json_loads                 | 24.7 us                                                      | 25.3 us: 1.02x slower                                                               |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.91 ms: 1.03x slower                                                               |
| docutils                   | 2.83 sec                                                     | 2.94 sec: 1.04x slower                                                              |
| comprehensions             | 17.0 us                                                      | 17.8 us: 1.04x slower                                                               |
| pickle_pure_python         | 323 us                                                       | 338 us: 1.05x slower                                                                |
| coroutines                 | 21.6 ms                                                      | 22.6 ms: 1.05x slower                                                               |
| create_gc_cycles           | 2.68 ms                                                      | 2.85 ms: 1.06x slower                                                               |
| raytrace                   | 273 ms                                                       | 292 ms: 1.07x slower                                                                |
| crypto_pyaes               | 73.3 ms                                                      | 79.0 ms: 1.08x slower                                                               |
| many_optionals             | 930 us                                                       | 1.23 ms: 1.32x slower                                                               |
| gc_traversal               | 4.74 ms                                                      | 6.47 ms: 1.37x slower                                                               |
| subparsers                 | 17.5 ms                                                      | 42.7 ms: 2.44x slower                                                               |
| telco                      | 8.79 ms                                                      | 160 ms: 18.20x slower                                                               |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                                        |

Benchmark hidden because not significant (5): nbody, pycparser, djangocms, typing_runtime_protocols, mako
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250721-3.15.0a0-53a50eb-JIT/bm-20250721-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.037x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.13x