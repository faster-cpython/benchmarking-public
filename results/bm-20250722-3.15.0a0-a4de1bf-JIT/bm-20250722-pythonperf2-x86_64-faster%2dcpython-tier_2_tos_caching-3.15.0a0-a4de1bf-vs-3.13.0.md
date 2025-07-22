# Results vs. 3.13.0

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-x86_64
- commit hash: a4de1bf
- commit date: 2025-07-22
- overall geometric mean: 1.040x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 285 ms: 1.03x faster                                                                |
| docutils       | 2.83 sec                                                     | 2.93 sec: 1.04x slower                                                              |
| html5lib       | 73.5 ms                                                      | 67.0 ms: 1.10x faster                                                               |
| sphinx         | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                              |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 331 ms: 1.41x faster                                                                |
| async_tree_memoization     | 453 ms                                                       | 327 ms: 1.38x faster                                                                |
| async_tree_none            | 376 ms                                                       | 272 ms: 1.38x faster                                                                |
| async_tree_io              | 843 ms                                                       | 623 ms: 1.35x faster                                                                |
| async_tree_io_tg           | 831 ms                                                       | 633 ms: 1.31x faster                                                                |
| async_tree_none_tg         | 346 ms                                                       | 273 ms: 1.27x faster                                                                |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 504 ms: 1.20x faster                                                                |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 511 ms: 1.14x faster                                                                |
| async_generators           | 457 ms                                                       | 443 ms: 1.03x faster                                                                |
| asyncio_websockets         | 388 ms                                                       | 384 ms: 1.01x faster                                                                |
| coroutines                 | 21.6 ms                                                      | 22.3 ms: 1.03x slower                                                               |
| Geometric mean             | (ref)                                                        | 1.21x faster                                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 61.7 ms: 1.32x faster                                                               |
| nbody          | 89.3 ms                                                      | 84.4 ms: 1.06x faster                                                               |
| pidigits       | 252 ms                                                       | 256 ms: 1.01x slower                                                                |
| Geometric mean | (ref)                                                        | 1.11x faster                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_dna      | 247 ms                                                       | 223 ms: 1.11x faster                                                                |
| regex_v8       | 26.1 ms                                                      | 23.8 ms: 1.10x faster                                                               |
| regex_compile  | 143 ms                                                       | 133 ms: 1.07x faster                                                                |
| regex_effbot   | 3.67 ms                                                      | 3.60 ms: 1.02x faster                                                               |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 1.94 sec: 1.27x faster                                                              |
| unpickle_pure_python | 217 us                                                       | 199 us: 1.09x faster                                                                |
| xml_etree_process    | 61.2 ms                                                      | 56.4 ms: 1.08x faster                                                               |
| xml_etree_generate   | 86.5 ms                                                      | 80.2 ms: 1.08x faster                                                               |
| xml_etree_parse      | 150 ms                                                       | 140 ms: 1.07x faster                                                                |
| xml_etree_iterparse  | 103 ms                                                       | 97.9 ms: 1.05x faster                                                               |
| json_loads           | 24.7 us                                                      | 25.5 us: 1.03x slower                                                               |
| pickle_pure_python   | 323 us                                                       | 335 us: 1.04x slower                                                                |
| Geometric mean       | (ref)                                                        | 1.06x faster                                                                        |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 15.3 ms: 1.04x faster                                                               |
| python_startup_no_site | 8.96 ms                                                      | 8.72 ms: 1.03x faster                                                               |
| Geometric mean         | (ref)                                                        | 1.03x faster                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 23.6 ms: 1.11x faster                                                               |
| genshi_xml      | 57.1 ms                                                      | 54.6 ms: 1.04x faster                                                               |
| django_template | 36.4 ms                                                      | 35.0 ms: 1.04x faster                                                               |
| mako            | 10.4 ms                                                      | 10.3 ms: 1.01x faster                                                               |
| Geometric mean  | (ref)                                                        | 1.05x faster                                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.29 sec: 1.96x faster                                                              |
| richards                   | 52.9 ms                                                      | 35.4 ms: 1.50x faster                                                               |
| richards_super             | 59.6 ms                                                      | 41.6 ms: 1.43x faster                                                               |
| async_tree_memoization_tg  | 466 ms                                                       | 331 ms: 1.41x faster                                                                |
| deepcopy                   | 392 us                                                       | 279 us: 1.40x faster                                                                |
| async_tree_memoization     | 453 ms                                                       | 327 ms: 1.38x faster                                                                |
| async_tree_none            | 376 ms                                                       | 272 ms: 1.38x faster                                                                |
| deepcopy_memo              | 38.6 us                                                      | 28.1 us: 1.38x faster                                                               |
| async_tree_io              | 843 ms                                                       | 623 ms: 1.35x faster                                                                |
| float                      | 81.3 ms                                                      | 61.7 ms: 1.32x faster                                                               |
| async_tree_io_tg           | 831 ms                                                       | 633 ms: 1.31x faster                                                                |
| go                         | 162 ms                                                       | 124 ms: 1.31x faster                                                                |
| tomli_loads                | 2.46 sec                                                     | 1.94 sec: 1.27x faster                                                              |
| async_tree_none_tg         | 346 ms                                                       | 273 ms: 1.27x faster                                                                |
| pyflate                    | 503 ms                                                       | 417 ms: 1.21x faster                                                                |
| spectral_norm              | 97.0 ms                                                      | 80.9 ms: 1.20x faster                                                               |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 504 ms: 1.20x faster                                                                |
| scimark_sor                | 123 ms                                                       | 104 ms: 1.19x faster                                                                |
| dulwich_log                | 68.2 ms                                                      | 58.3 ms: 1.17x faster                                                               |
| deepcopy_reduce            | 3.54 us                                                      | 3.03 us: 1.17x faster                                                               |
| deltablue                  | 3.42 ms                                                      | 2.93 ms: 1.17x faster                                                               |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 511 ms: 1.14x faster                                                                |
| pprint_pformat             | 1.72 sec                                                     | 1.52 sec: 1.13x faster                                                              |
| pprint_safe_repr           | 843 ms                                                       | 753 ms: 1.12x faster                                                                |
| generators                 | 33.6 ms                                                      | 30.2 ms: 1.11x faster                                                               |
| genshi_text                | 26.2 ms                                                      | 23.6 ms: 1.11x faster                                                               |
| regex_dna                  | 247 ms                                                       | 223 ms: 1.11x faster                                                                |
| html5lib                   | 73.5 ms                                                      | 67.0 ms: 1.10x faster                                                               |
| regex_v8                   | 26.1 ms                                                      | 23.8 ms: 1.10x faster                                                               |
| unpickle_pure_python       | 217 us                                                       | 199 us: 1.09x faster                                                                |
| bpe_tokeniser              | 5.09 sec                                                     | 4.66 sec: 1.09x faster                                                              |
| xml_etree_process          | 61.2 ms                                                      | 56.4 ms: 1.08x faster                                                               |
| k_core                     | 2.17 sec                                                     | 2.01 sec: 1.08x faster                                                              |
| xml_etree_generate         | 86.5 ms                                                      | 80.2 ms: 1.08x faster                                                               |
| regex_compile              | 143 ms                                                       | 133 ms: 1.07x faster                                                                |
| xml_etree_parse            | 150 ms                                                       | 140 ms: 1.07x faster                                                                |
| thrift                     | 901 us                                                       | 841 us: 1.07x faster                                                                |
| pylint                     | 347 ms                                                       | 324 ms: 1.07x faster                                                                |
| json                       | 5.69 ms                                                      | 5.34 ms: 1.06x faster                                                               |
| connected_components       | 432 ms                                                       | 407 ms: 1.06x faster                                                                |
| meteor_contest             | 130 ms                                                       | 122 ms: 1.06x faster                                                                |
| scimark_monte_carlo        | 66.1 ms                                                      | 62.4 ms: 1.06x faster                                                               |
| hexiom                     | 6.55 ms                                                      | 6.18 ms: 1.06x faster                                                               |
| nbody                      | 89.3 ms                                                      | 84.4 ms: 1.06x faster                                                               |
| sympy_integrate            | 23.6 ms                                                      | 22.4 ms: 1.05x faster                                                               |
| xml_etree_iterparse        | 103 ms                                                       | 97.9 ms: 1.05x faster                                                               |
| logging_silent             | 97.9 ns                                                      | 93.4 ns: 1.05x faster                                                               |
| genshi_xml                 | 57.1 ms                                                      | 54.6 ms: 1.04x faster                                                               |
| logging_simple             | 6.39 us                                                      | 6.12 us: 1.04x faster                                                               |
| scimark_fft                | 328 ms                                                       | 314 ms: 1.04x faster                                                                |
| python_startup             | 15.9 ms                                                      | 15.3 ms: 1.04x faster                                                               |
| django_template            | 36.4 ms                                                      | 35.0 ms: 1.04x faster                                                               |
| shortest_path              | 460 ms                                                       | 443 ms: 1.04x faster                                                                |
| logging_format             | 6.94 us                                                      | 6.69 us: 1.04x faster                                                               |
| sympy_expand               | 509 ms                                                       | 493 ms: 1.03x faster                                                                |
| async_generators           | 457 ms                                                       | 443 ms: 1.03x faster                                                                |
| sympy_str                  | 298 ms                                                       | 289 ms: 1.03x faster                                                                |
| sqlite_synth               | 2.91 us                                                      | 2.82 us: 1.03x faster                                                               |
| pathlib                    | 17.5 ms                                                      | 17.1 ms: 1.03x faster                                                               |
| 2to3                       | 293 ms                                                       | 285 ms: 1.03x faster                                                                |
| python_startup_no_site     | 8.96 ms                                                      | 8.72 ms: 1.03x faster                                                               |
| coverage                   | 80.0 ms                                                      | 77.9 ms: 1.03x faster                                                               |
| sphinx                     | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                              |
| sympy_sum                  | 155 ms                                                       | 151 ms: 1.02x faster                                                                |
| scimark_lu                 | 98.7 ms                                                      | 96.6 ms: 1.02x faster                                                               |
| regex_effbot               | 3.67 ms                                                      | 3.60 ms: 1.02x faster                                                               |
| chaos                      | 60.2 ms                                                      | 59.1 ms: 1.02x faster                                                               |
| asyncio_websockets         | 388 ms                                                       | 384 ms: 1.01x faster                                                                |
| pycparser                  | 1.24 sec                                                     | 1.23 sec: 1.01x faster                                                              |
| mako                       | 10.4 ms                                                      | 10.3 ms: 1.01x faster                                                               |
| pidigits                   | 252 ms                                                       | 256 ms: 1.01x slower                                                                |
| fannkuch                   | 363 ms                                                       | 372 ms: 1.02x slower                                                                |
| comprehensions             | 17.0 us                                                      | 17.5 us: 1.03x slower                                                               |
| coroutines                 | 21.6 ms                                                      | 22.3 ms: 1.03x slower                                                               |
| json_loads                 | 24.7 us                                                      | 25.5 us: 1.03x slower                                                               |
| docutils                   | 2.83 sec                                                     | 2.93 sec: 1.04x slower                                                              |
| typing_runtime_protocols   | 169 us                                                       | 175 us: 1.04x slower                                                                |
| pickle_pure_python         | 323 us                                                       | 335 us: 1.04x slower                                                                |
| nqueens                    | 90.7 ms                                                      | 94.4 ms: 1.04x slower                                                               |
| crypto_pyaes               | 73.3 ms                                                      | 77.2 ms: 1.05x slower                                                               |
| raytrace                   | 273 ms                                                       | 288 ms: 1.06x slower                                                                |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 5.07 ms: 1.06x slower                                                               |
| create_gc_cycles           | 2.68 ms                                                      | 2.91 ms: 1.09x slower                                                               |
| many_optionals             | 930 us                                                       | 1.22 ms: 1.31x slower                                                               |
| gc_traversal               | 4.74 ms                                                      | 6.58 ms: 1.39x slower                                                               |
| subparsers                 | 17.5 ms                                                      | 43.2 ms: 2.47x slower                                                               |
| telco                      | 8.79 ms                                                      | 163 ms: 18.55x slower                                                               |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                                        |

Benchmark hidden because not significant (2): djangocms, json_dumps
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250722-3.15.0a0-a4de1bf-JIT/bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.040x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.13x