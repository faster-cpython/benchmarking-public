# Results vs. 3.13.0

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-x86_64
- commit hash: 6a85f95
- commit date: 2025-08-13
- overall geometric mean: 1.046x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250813-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 287 ms: 1.02x faster                                                                |
| docutils       | 2.83 sec                                                     | 2.92 sec: 1.03x slower                                                              |
| html5lib       | 73.5 ms                                                      | 68.5 ms: 1.07x faster                                                               |
| sphinx         | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                              |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250813-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 331 ms: 1.41x faster                                                                |
| async_tree_memoization     | 453 ms                                                       | 328 ms: 1.38x faster                                                                |
| async_tree_io              | 843 ms                                                       | 623 ms: 1.35x faster                                                                |
| async_tree_none            | 376 ms                                                       | 283 ms: 1.33x faster                                                                |
| async_tree_io_tg           | 831 ms                                                       | 634 ms: 1.31x faster                                                                |
| async_tree_none_tg         | 346 ms                                                       | 272 ms: 1.27x faster                                                                |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 504 ms: 1.20x faster                                                                |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 506 ms: 1.15x faster                                                                |
| async_generators           | 457 ms                                                       | 448 ms: 1.02x faster                                                                |
| coroutines                 | 21.6 ms                                                      | 22.5 ms: 1.04x slower                                                               |
| Geometric mean             | (ref)                                                        | 1.21x faster                                                                        |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250813-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 61.7 ms: 1.32x faster                                                               |
| nbody          | 89.3 ms                                                      | 86.6 ms: 1.03x faster                                                               |
| pidigits       | 252 ms                                                       | 255 ms: 1.01x slower                                                                |
| Geometric mean | (ref)                                                        | 1.10x faster                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250813-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_v8       | 26.1 ms                                                      | 23.3 ms: 1.12x faster                                                               |
| regex_dna      | 247 ms                                                       | 223 ms: 1.10x faster                                                                |
| regex_compile  | 143 ms                                                       | 133 ms: 1.08x faster                                                                |
| regex_effbot   | 3.67 ms                                                      | 3.71 ms: 1.01x slower                                                               |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250813-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 1.91 sec: 1.29x faster                                                              |
| unpickle_pure_python | 217 us                                                       | 195 us: 1.12x faster                                                                |
| xml_etree_process    | 61.2 ms                                                      | 55.2 ms: 1.11x faster                                                               |
| json_dumps           | 11.1 ms                                                      | 10.3 ms: 1.08x faster                                                               |
| xml_etree_generate   | 86.5 ms                                                      | 80.8 ms: 1.07x faster                                                               |
| xml_etree_parse      | 150 ms                                                       | 144 ms: 1.04x faster                                                                |
| xml_etree_iterparse  | 103 ms                                                       | 99.5 ms: 1.03x faster                                                               |
| pickle_pure_python   | 323 us                                                       | 335 us: 1.04x slower                                                                |
| json_loads           | 24.7 us                                                      | 25.9 us: 1.05x slower                                                               |
| Geometric mean       | (ref)                                                        | 1.07x faster                                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250813-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 15.5 ms: 1.03x faster                                                               |
| python_startup_no_site | 8.96 ms                                                      | 8.86 ms: 1.01x faster                                                               |
| Geometric mean         | (ref)                                                        | 1.02x faster                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250813-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 23.1 ms: 1.13x faster                                                               |
| mako            | 10.4 ms                                                      | 9.73 ms: 1.07x faster                                                               |
| genshi_xml      | 57.1 ms                                                      | 54.5 ms: 1.05x faster                                                               |
| django_template | 36.4 ms                                                      | 35.3 ms: 1.03x faster                                                               |
| Geometric mean  | (ref)                                                        | 1.07x faster                                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250813-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.29 sec: 1.97x faster                                                              |
| richards                   | 52.9 ms                                                      | 33.6 ms: 1.58x faster                                                               |
| richards_super             | 59.6 ms                                                      | 39.1 ms: 1.52x faster                                                               |
| deepcopy                   | 392 us                                                       | 276 us: 1.42x faster                                                                |
| async_tree_memoization_tg  | 466 ms                                                       | 331 ms: 1.41x faster                                                                |
| deepcopy_memo              | 38.6 us                                                      | 27.6 us: 1.40x faster                                                               |
| async_tree_memoization     | 453 ms                                                       | 328 ms: 1.38x faster                                                                |
| async_tree_io              | 843 ms                                                       | 623 ms: 1.35x faster                                                                |
| async_tree_none            | 376 ms                                                       | 283 ms: 1.33x faster                                                                |
| go                         | 162 ms                                                       | 122 ms: 1.33x faster                                                                |
| float                      | 81.3 ms                                                      | 61.7 ms: 1.32x faster                                                               |
| async_tree_io_tg           | 831 ms                                                       | 634 ms: 1.31x faster                                                                |
| tomli_loads                | 2.46 sec                                                     | 1.91 sec: 1.29x faster                                                              |
| pyflate                    | 503 ms                                                       | 393 ms: 1.28x faster                                                                |
| async_tree_none_tg         | 346 ms                                                       | 272 ms: 1.27x faster                                                                |
| spectral_norm              | 97.0 ms                                                      | 78.0 ms: 1.24x faster                                                               |
| scimark_sor                | 123 ms                                                       | 102 ms: 1.21x faster                                                                |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 504 ms: 1.20x faster                                                                |
| deltablue                  | 3.42 ms                                                      | 2.86 ms: 1.19x faster                                                               |
| deepcopy_reduce            | 3.54 us                                                      | 2.98 us: 1.19x faster                                                               |
| pprint_pformat             | 1.72 sec                                                     | 1.48 sec: 1.16x faster                                                              |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 506 ms: 1.15x faster                                                                |
| dulwich_log                | 68.2 ms                                                      | 59.4 ms: 1.15x faster                                                               |
| pprint_safe_repr           | 843 ms                                                       | 739 ms: 1.14x faster                                                                |
| genshi_text                | 26.2 ms                                                      | 23.1 ms: 1.13x faster                                                               |
| regex_v8                   | 26.1 ms                                                      | 23.3 ms: 1.12x faster                                                               |
| bpe_tokeniser              | 5.09 sec                                                     | 4.54 sec: 1.12x faster                                                              |
| unpickle_pure_python       | 217 us                                                       | 195 us: 1.12x faster                                                                |
| generators                 | 33.6 ms                                                      | 30.2 ms: 1.11x faster                                                               |
| xml_etree_process          | 61.2 ms                                                      | 55.2 ms: 1.11x faster                                                               |
| regex_dna                  | 247 ms                                                       | 223 ms: 1.10x faster                                                                |
| hexiom                     | 6.55 ms                                                      | 6.00 ms: 1.09x faster                                                               |
| json_dumps                 | 11.1 ms                                                      | 10.3 ms: 1.08x faster                                                               |
| k_core                     | 2.17 sec                                                     | 2.00 sec: 1.08x faster                                                              |
| meteor_contest             | 130 ms                                                       | 120 ms: 1.08x faster                                                                |
| regex_compile              | 143 ms                                                       | 133 ms: 1.08x faster                                                                |
| scimark_fft                | 328 ms                                                       | 305 ms: 1.07x faster                                                                |
| html5lib                   | 73.5 ms                                                      | 68.5 ms: 1.07x faster                                                               |
| xml_etree_generate         | 86.5 ms                                                      | 80.8 ms: 1.07x faster                                                               |
| pylint                     | 347 ms                                                       | 324 ms: 1.07x faster                                                                |
| mako                       | 10.4 ms                                                      | 9.73 ms: 1.07x faster                                                               |
| logging_simple             | 6.39 us                                                      | 6.02 us: 1.06x faster                                                               |
| connected_components       | 432 ms                                                       | 407 ms: 1.06x faster                                                                |
| thrift                     | 901 us                                                       | 850 us: 1.06x faster                                                                |
| logging_silent             | 97.9 ns                                                      | 93.0 ns: 1.05x faster                                                               |
| sympy_integrate            | 23.6 ms                                                      | 22.5 ms: 1.05x faster                                                               |
| genshi_xml                 | 57.1 ms                                                      | 54.5 ms: 1.05x faster                                                               |
| logging_format             | 6.94 us                                                      | 6.64 us: 1.05x faster                                                               |
| scimark_monte_carlo        | 66.1 ms                                                      | 63.3 ms: 1.04x faster                                                               |
| xml_etree_parse            | 150 ms                                                       | 144 ms: 1.04x faster                                                                |
| pathlib                    | 17.5 ms                                                      | 16.9 ms: 1.04x faster                                                               |
| shortest_path              | 460 ms                                                       | 443 ms: 1.04x faster                                                                |
| sqlite_synth               | 2.91 us                                                      | 2.80 us: 1.04x faster                                                               |
| xml_etree_iterparse        | 103 ms                                                       | 99.5 ms: 1.03x faster                                                               |
| nbody                      | 89.3 ms                                                      | 86.6 ms: 1.03x faster                                                               |
| django_template            | 36.4 ms                                                      | 35.3 ms: 1.03x faster                                                               |
| scimark_lu                 | 98.7 ms                                                      | 95.8 ms: 1.03x faster                                                               |
| chaos                      | 60.2 ms                                                      | 58.5 ms: 1.03x faster                                                               |
| python_startup             | 15.9 ms                                                      | 15.5 ms: 1.03x faster                                                               |
| sphinx                     | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                              |
| json                       | 5.69 ms                                                      | 5.54 ms: 1.03x faster                                                               |
| sympy_str                  | 298 ms                                                       | 291 ms: 1.02x faster                                                                |
| sympy_expand               | 509 ms                                                       | 499 ms: 1.02x faster                                                                |
| async_generators           | 457 ms                                                       | 448 ms: 1.02x faster                                                                |
| 2to3                       | 293 ms                                                       | 287 ms: 1.02x faster                                                                |
| sympy_sum                  | 155 ms                                                       | 152 ms: 1.02x faster                                                                |
| python_startup_no_site     | 8.96 ms                                                      | 8.86 ms: 1.01x faster                                                               |
| fannkuch                   | 363 ms                                                       | 362 ms: 1.00x faster                                                                |
| regex_effbot               | 3.67 ms                                                      | 3.71 ms: 1.01x slower                                                               |
| pidigits                   | 252 ms                                                       | 255 ms: 1.01x slower                                                                |
| typing_runtime_protocols   | 169 us                                                       | 172 us: 1.02x slower                                                                |
| raytrace                   | 273 ms                                                       | 279 ms: 1.02x slower                                                                |
| comprehensions             | 17.0 us                                                      | 17.5 us: 1.03x slower                                                               |
| nqueens                    | 90.7 ms                                                      | 93.4 ms: 1.03x slower                                                               |
| docutils                   | 2.83 sec                                                     | 2.92 sec: 1.03x slower                                                              |
| pickle_pure_python         | 323 us                                                       | 335 us: 1.04x slower                                                                |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.95 ms: 1.04x slower                                                               |
| coroutines                 | 21.6 ms                                                      | 22.5 ms: 1.04x slower                                                               |
| crypto_pyaes               | 73.3 ms                                                      | 76.7 ms: 1.05x slower                                                               |
| coverage                   | 80.0 ms                                                      | 83.8 ms: 1.05x slower                                                               |
| json_loads                 | 24.7 us                                                      | 25.9 us: 1.05x slower                                                               |
| create_gc_cycles           | 2.68 ms                                                      | 2.90 ms: 1.08x slower                                                               |
| many_optionals             | 930 us                                                       | 1.23 ms: 1.33x slower                                                               |
| gc_traversal               | 4.74 ms                                                      | 6.32 ms: 1.33x slower                                                               |
| subparsers                 | 17.5 ms                                                      | 43.2 ms: 2.47x slower                                                               |
| telco                      | 8.79 ms                                                      | 160 ms: 18.25x slower                                                               |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                                        |

Benchmark hidden because not significant (3): asyncio_websockets, djangocms, pycparser
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250813-3.15.0a0-6a85f95-JIT/bm-20250813-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.046x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.12x