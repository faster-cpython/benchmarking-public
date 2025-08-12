# Results vs. 3.13.0

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-x86_64
- commit hash: 6041480
- commit date: 2025-08-11
- overall geometric mean: 1.046x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250811-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 287 ms: 1.02x faster                                                                |
| docutils       | 2.83 sec                                                     | 2.91 sec: 1.03x slower                                                              |
| html5lib       | 73.5 ms                                                      | 67.3 ms: 1.09x faster                                                               |
| sphinx         | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                              |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250811-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 331 ms: 1.41x faster                                                                |
| async_tree_memoization     | 453 ms                                                       | 329 ms: 1.38x faster                                                                |
| async_tree_io              | 843 ms                                                       | 619 ms: 1.36x faster                                                                |
| async_tree_none            | 376 ms                                                       | 280 ms: 1.34x faster                                                                |
| async_tree_io_tg           | 831 ms                                                       | 630 ms: 1.32x faster                                                                |
| async_tree_none_tg         | 346 ms                                                       | 268 ms: 1.29x faster                                                                |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 501 ms: 1.21x faster                                                                |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 504 ms: 1.15x faster                                                                |
| async_generators           | 457 ms                                                       | 442 ms: 1.03x faster                                                                |
| asyncio_websockets         | 388 ms                                                       | 384 ms: 1.01x faster                                                                |
| coroutines                 | 21.6 ms                                                      | 22.5 ms: 1.04x slower                                                               |
| Geometric mean             | (ref)                                                        | 1.21x faster                                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250811-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 60.5 ms: 1.34x faster                                                               |
| nbody          | 89.3 ms                                                      | 86.4 ms: 1.03x faster                                                               |
| pidigits       | 252 ms                                                       | 255 ms: 1.01x slower                                                                |
| Geometric mean | (ref)                                                        | 1.11x faster                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250811-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_v8       | 26.1 ms                                                      | 23.5 ms: 1.11x faster                                                               |
| regex_dna      | 247 ms                                                       | 226 ms: 1.09x faster                                                                |
| regex_compile  | 143 ms                                                       | 134 ms: 1.07x faster                                                                |
| regex_effbot   | 3.67 ms                                                      | 3.69 ms: 1.01x slower                                                               |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250811-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 1.92 sec: 1.28x faster                                                              |
| xml_etree_process    | 61.2 ms                                                      | 55.2 ms: 1.11x faster                                                               |
| unpickle_pure_python | 217 us                                                       | 199 us: 1.10x faster                                                                |
| json_dumps           | 11.1 ms                                                      | 10.2 ms: 1.10x faster                                                               |
| xml_etree_generate   | 86.5 ms                                                      | 79.5 ms: 1.09x faster                                                               |
| xml_etree_parse      | 150 ms                                                       | 140 ms: 1.07x faster                                                                |
| xml_etree_iterparse  | 103 ms                                                       | 98.2 ms: 1.05x faster                                                               |
| json_loads           | 24.7 us                                                      | 25.3 us: 1.03x slower                                                               |
| pickle_pure_python   | 323 us                                                       | 333 us: 1.03x slower                                                                |
| Geometric mean       | (ref)                                                        | 1.08x faster                                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250811-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 15.4 ms: 1.03x faster                                                               |
| python_startup_no_site | 8.96 ms                                                      | 8.81 ms: 1.02x faster                                                               |
| Geometric mean         | (ref)                                                        | 1.03x faster                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250811-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 23.1 ms: 1.13x faster                                                               |
| mako            | 10.4 ms                                                      | 9.87 ms: 1.05x faster                                                               |
| genshi_xml      | 57.1 ms                                                      | 54.6 ms: 1.04x faster                                                               |
| django_template | 36.4 ms                                                      | 35.5 ms: 1.03x faster                                                               |
| Geometric mean  | (ref)                                                        | 1.06x faster                                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250811-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.30 sec: 1.95x faster                                                              |
| richards                   | 52.9 ms                                                      | 34.3 ms: 1.54x faster                                                               |
| richards_super             | 59.6 ms                                                      | 39.8 ms: 1.50x faster                                                               |
| deepcopy                   | 392 us                                                       | 276 us: 1.42x faster                                                                |
| async_tree_memoization_tg  | 466 ms                                                       | 331 ms: 1.41x faster                                                                |
| deepcopy_memo              | 38.6 us                                                      | 27.7 us: 1.39x faster                                                               |
| async_tree_memoization     | 453 ms                                                       | 329 ms: 1.38x faster                                                                |
| async_tree_io              | 843 ms                                                       | 619 ms: 1.36x faster                                                                |
| async_tree_none            | 376 ms                                                       | 280 ms: 1.34x faster                                                                |
| float                      | 81.3 ms                                                      | 60.5 ms: 1.34x faster                                                               |
| go                         | 162 ms                                                       | 122 ms: 1.33x faster                                                                |
| async_tree_io_tg           | 831 ms                                                       | 630 ms: 1.32x faster                                                                |
| async_tree_none_tg         | 346 ms                                                       | 268 ms: 1.29x faster                                                                |
| tomli_loads                | 2.46 sec                                                     | 1.92 sec: 1.28x faster                                                              |
| pyflate                    | 503 ms                                                       | 414 ms: 1.21x faster                                                                |
| scimark_sor                | 123 ms                                                       | 102 ms: 1.21x faster                                                                |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 501 ms: 1.21x faster                                                                |
| spectral_norm              | 97.0 ms                                                      | 80.6 ms: 1.20x faster                                                               |
| deltablue                  | 3.42 ms                                                      | 2.86 ms: 1.19x faster                                                               |
| deepcopy_reduce            | 3.54 us                                                      | 2.97 us: 1.19x faster                                                               |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 504 ms: 1.15x faster                                                                |
| pprint_pformat             | 1.72 sec                                                     | 1.49 sec: 1.15x faster                                                              |
| dulwich_log                | 68.2 ms                                                      | 59.8 ms: 1.14x faster                                                               |
| generators                 | 33.6 ms                                                      | 29.5 ms: 1.14x faster                                                               |
| pprint_safe_repr           | 843 ms                                                       | 742 ms: 1.14x faster                                                                |
| genshi_text                | 26.2 ms                                                      | 23.1 ms: 1.13x faster                                                               |
| bpe_tokeniser              | 5.09 sec                                                     | 4.57 sec: 1.11x faster                                                              |
| regex_v8                   | 26.1 ms                                                      | 23.5 ms: 1.11x faster                                                               |
| xml_etree_process          | 61.2 ms                                                      | 55.2 ms: 1.11x faster                                                               |
| unpickle_pure_python       | 217 us                                                       | 199 us: 1.10x faster                                                                |
| json_dumps                 | 11.1 ms                                                      | 10.2 ms: 1.10x faster                                                               |
| regex_dna                  | 247 ms                                                       | 226 ms: 1.09x faster                                                                |
| html5lib                   | 73.5 ms                                                      | 67.3 ms: 1.09x faster                                                               |
| xml_etree_generate         | 86.5 ms                                                      | 79.5 ms: 1.09x faster                                                               |
| scimark_fft                | 328 ms                                                       | 302 ms: 1.08x faster                                                                |
| k_core                     | 2.17 sec                                                     | 2.02 sec: 1.07x faster                                                              |
| meteor_contest             | 130 ms                                                       | 121 ms: 1.07x faster                                                                |
| pylint                     | 347 ms                                                       | 323 ms: 1.07x faster                                                                |
| hexiom                     | 6.55 ms                                                      | 6.12 ms: 1.07x faster                                                               |
| xml_etree_parse            | 150 ms                                                       | 140 ms: 1.07x faster                                                                |
| logging_silent             | 97.9 ns                                                      | 91.5 ns: 1.07x faster                                                               |
| regex_compile              | 143 ms                                                       | 134 ms: 1.07x faster                                                                |
| thrift                     | 901 us                                                       | 844 us: 1.07x faster                                                                |
| pathlib                    | 17.5 ms                                                      | 16.5 ms: 1.06x faster                                                               |
| connected_components       | 432 ms                                                       | 408 ms: 1.06x faster                                                                |
| logging_simple             | 6.39 us                                                      | 6.04 us: 1.06x faster                                                               |
| mako                       | 10.4 ms                                                      | 9.87 ms: 1.05x faster                                                               |
| sympy_integrate            | 23.6 ms                                                      | 22.5 ms: 1.05x faster                                                               |
| xml_etree_iterparse        | 103 ms                                                       | 98.2 ms: 1.05x faster                                                               |
| genshi_xml                 | 57.1 ms                                                      | 54.6 ms: 1.04x faster                                                               |
| shortest_path              | 460 ms                                                       | 442 ms: 1.04x faster                                                                |
| json                       | 5.69 ms                                                      | 5.48 ms: 1.04x faster                                                               |
| logging_format             | 6.94 us                                                      | 6.70 us: 1.04x faster                                                               |
| scimark_lu                 | 98.7 ms                                                      | 95.3 ms: 1.04x faster                                                               |
| sqlite_synth               | 2.91 us                                                      | 2.81 us: 1.03x faster                                                               |
| python_startup             | 15.9 ms                                                      | 15.4 ms: 1.03x faster                                                               |
| nbody                      | 89.3 ms                                                      | 86.4 ms: 1.03x faster                                                               |
| async_generators           | 457 ms                                                       | 442 ms: 1.03x faster                                                                |
| sphinx                     | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                              |
| scimark_monte_carlo        | 66.1 ms                                                      | 64.4 ms: 1.03x faster                                                               |
| django_template            | 36.4 ms                                                      | 35.5 ms: 1.03x faster                                                               |
| sympy_expand               | 509 ms                                                       | 497 ms: 1.02x faster                                                                |
| sympy_str                  | 298 ms                                                       | 291 ms: 1.02x faster                                                                |
| chaos                      | 60.2 ms                                                      | 58.9 ms: 1.02x faster                                                               |
| sympy_sum                  | 155 ms                                                       | 151 ms: 1.02x faster                                                                |
| 2to3                       | 293 ms                                                       | 287 ms: 1.02x faster                                                                |
| python_startup_no_site     | 8.96 ms                                                      | 8.81 ms: 1.02x faster                                                               |
| coverage                   | 80.0 ms                                                      | 78.9 ms: 1.01x faster                                                               |
| asyncio_websockets         | 388 ms                                                       | 384 ms: 1.01x faster                                                                |
| regex_effbot               | 3.67 ms                                                      | 3.69 ms: 1.01x slower                                                               |
| fannkuch                   | 363 ms                                                       | 367 ms: 1.01x slower                                                                |
| typing_runtime_protocols   | 169 us                                                       | 171 us: 1.01x slower                                                                |
| pidigits                   | 252 ms                                                       | 255 ms: 1.01x slower                                                                |
| nqueens                    | 90.7 ms                                                      | 92.2 ms: 1.02x slower                                                               |
| comprehensions             | 17.0 us                                                      | 17.4 us: 1.02x slower                                                               |
| json_loads                 | 24.7 us                                                      | 25.3 us: 1.03x slower                                                               |
| pickle_pure_python         | 323 us                                                       | 333 us: 1.03x slower                                                                |
| docutils                   | 2.83 sec                                                     | 2.91 sec: 1.03x slower                                                              |
| raytrace                   | 273 ms                                                       | 283 ms: 1.04x slower                                                                |
| coroutines                 | 21.6 ms                                                      | 22.5 ms: 1.04x slower                                                               |
| crypto_pyaes               | 73.3 ms                                                      | 77.3 ms: 1.06x slower                                                               |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 5.09 ms: 1.07x slower                                                               |
| create_gc_cycles           | 2.68 ms                                                      | 2.87 ms: 1.07x slower                                                               |
| many_optionals             | 930 us                                                       | 1.23 ms: 1.32x slower                                                               |
| gc_traversal               | 4.74 ms                                                      | 6.47 ms: 1.36x slower                                                               |
| subparsers                 | 17.5 ms                                                      | 42.9 ms: 2.46x slower                                                               |
| telco                      | 8.79 ms                                                      | 161 ms: 18.27x slower                                                               |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                                        |

Benchmark hidden because not significant (2): djangocms, pycparser
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250811-3.15.0a0-6041480-JIT/bm-20250811-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.046x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.12x