# Results vs. 3.13.0

- fork: python
- ref: 470a0a68ebbbb4254f1a
- machine: linux-x86_64
- commit hash: 470a0a6
- commit date: 2025-01-22
- overall geometric mean: 1.061x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250122-pythonperf2-x86_64-python-470a0a68ebbbb4254f1a-3.14.0a4+-470a0a6 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 282 ms: 1.04x faster                                                         |
| docutils       | 2.83 sec                                                     | 2.89 sec: 1.02x slower                                                       |
| html5lib       | 73.5 ms                                                      | 68.0 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250122-pythonperf2-x86_64-python-470a0a68ebbbb4254f1a-3.14.0a4+-470a0a6 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 327 ms: 1.42x faster                                                         |
| async_tree_none            | 376 ms                                                       | 274 ms: 1.37x faster                                                         |
| async_tree_io              | 843 ms                                                       | 622 ms: 1.35x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 620 ms: 1.34x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 341 ms: 1.33x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 266 ms: 1.30x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 507 ms: 1.19x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 497 ms: 1.17x faster                                                         |
| async_generators           | 457 ms                                                       | 398 ms: 1.15x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.23x faster                                                                 |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250122-pythonperf2-x86_64-python-470a0a68ebbbb4254f1a-3.14.0a4+-470a0a6 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 70.5 ms: 1.15x faster                                                        |
| nbody          | 89.3 ms                                                      | 86.5 ms: 1.03x faster                                                        |
| pidigits       | 252 ms                                                       | 254 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250122-pythonperf2-x86_64-python-470a0a68ebbbb4254f1a-3.14.0a4+-470a0a6 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.18 ms: 1.15x faster                                                        |
| regex_compile  | 143 ms                                                       | 135 ms: 1.06x faster                                                         |
| regex_dna      | 247 ms                                                       | 251 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                 |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250122-pythonperf2-x86_64-python-470a0a68ebbbb4254f1a-3.14.0a4+-470a0a6 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.07 sec: 1.19x faster                                                       |
| xml_etree_parse      | 150 ms                                                       | 135 ms: 1.11x faster                                                         |
| xml_etree_iterparse  | 103 ms                                                       | 97.0 ms: 1.06x faster                                                        |
| xml_etree_generate   | 86.5 ms                                                      | 83.6 ms: 1.03x faster                                                        |
| unpickle_pure_python | 217 us                                                       | 220 us: 1.01x slower                                                         |
| xml_etree_process    | 61.2 ms                                                      | 62.0 ms: 1.01x slower                                                        |
| json_loads           | 24.7 us                                                      | 25.4 us: 1.03x slower                                                        |
| pickle_pure_python   | 323 us                                                       | 335 us: 1.04x slower                                                         |
| json_dumps           | 11.1 ms                                                      | 11.6 ms: 1.04x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.03x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250122-pythonperf2-x86_64-python-470a0a68ebbbb4254f1a-3.14.0a4+-470a0a6 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.96 ms                                                      | 8.98 ms: 1.00x slower                                                        |
| python_startup         | 15.9 ms                                                      | 16.0 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.00x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250122-pythonperf2-x86_64-python-470a0a68ebbbb4254f1a-3.14.0a4+-470a0a6 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 24.8 ms: 1.06x faster                                                        |
| genshi_xml      | 57.1 ms                                                      | 54.8 ms: 1.04x faster                                                        |
| django_template | 36.4 ms                                                      | 35.2 ms: 1.03x faster                                                        |
| mako            | 10.4 ms                                                      | 11.0 ms: 1.06x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.02x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250122-pythonperf2-x86_64-python-470a0a68ebbbb4254f1a-3.14.0a4+-470a0a6 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 327 ms: 1.42x faster                                                         |
| deepcopy                   | 392 us                                                       | 283 us: 1.38x faster                                                         |
| async_tree_none            | 376 ms                                                       | 274 ms: 1.37x faster                                                         |
| async_tree_io              | 843 ms                                                       | 622 ms: 1.35x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 620 ms: 1.34x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 341 ms: 1.33x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 266 ms: 1.30x faster                                                         |
| deepcopy_memo              | 38.6 us                                                      | 30.3 us: 1.27x faster                                                        |
| go                         | 162 ms                                                       | 128 ms: 1.27x faster                                                         |
| deepcopy_reduce            | 3.54 us                                                      | 2.93 us: 1.21x faster                                                        |
| generators                 | 33.6 ms                                                      | 28.1 ms: 1.20x faster                                                        |
| tomli_loads                | 2.46 sec                                                     | 2.07 sec: 1.19x faster                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 507 ms: 1.19x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 497 ms: 1.17x faster                                                         |
| pyflate                    | 503 ms                                                       | 431 ms: 1.17x faster                                                         |
| richards                   | 52.9 ms                                                      | 45.7 ms: 1.16x faster                                                        |
| float                      | 81.3 ms                                                      | 70.5 ms: 1.15x faster                                                        |
| regex_effbot               | 3.67 ms                                                      | 3.18 ms: 1.15x faster                                                        |
| async_generators           | 457 ms                                                       | 398 ms: 1.15x faster                                                         |
| spectral_norm              | 97.0 ms                                                      | 85.4 ms: 1.14x faster                                                        |
| richards_super             | 59.6 ms                                                      | 53.4 ms: 1.12x faster                                                        |
| xml_etree_parse            | 150 ms                                                       | 135 ms: 1.11x faster                                                         |
| scimark_fft                | 328 ms                                                       | 295 ms: 1.11x faster                                                         |
| scimark_sor                | 123 ms                                                       | 111 ms: 1.11x faster                                                         |
| pathlib                    | 17.5 ms                                                      | 15.9 ms: 1.10x faster                                                        |
| pylint                     | 347 ms                                                       | 315 ms: 1.10x faster                                                         |
| hexiom                     | 6.55 ms                                                      | 5.98 ms: 1.10x faster                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 4.65 sec: 1.09x faster                                                       |
| pprint_pformat             | 1.72 sec                                                     | 1.58 sec: 1.09x faster                                                       |
| html5lib                   | 73.5 ms                                                      | 68.0 ms: 1.08x faster                                                        |
| pprint_safe_repr           | 843 ms                                                       | 782 ms: 1.08x faster                                                         |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.44 ms: 1.08x faster                                                        |
| scimark_monte_carlo        | 66.1 ms                                                      | 61.6 ms: 1.07x faster                                                        |
| json                       | 5.69 ms                                                      | 5.31 ms: 1.07x faster                                                        |
| sqlglot_parse              | 1.40 ms                                                      | 1.31 ms: 1.07x faster                                                        |
| telco                      | 8.79 ms                                                      | 8.27 ms: 1.06x faster                                                        |
| sqlglot_transpile          | 1.79 ms                                                      | 1.69 ms: 1.06x faster                                                        |
| shortest_path              | 460 ms                                                       | 434 ms: 1.06x faster                                                         |
| xml_etree_iterparse        | 103 ms                                                       | 97.0 ms: 1.06x faster                                                        |
| regex_compile              | 143 ms                                                       | 135 ms: 1.06x faster                                                         |
| genshi_text                | 26.2 ms                                                      | 24.8 ms: 1.06x faster                                                        |
| connected_components       | 432 ms                                                       | 413 ms: 1.05x faster                                                         |
| scimark_lu                 | 98.7 ms                                                      | 94.3 ms: 1.05x faster                                                        |
| genshi_xml                 | 57.1 ms                                                      | 54.8 ms: 1.04x faster                                                        |
| thrift                     | 901 us                                                       | 865 us: 1.04x faster                                                         |
| mdp                        | 2.54 sec                                                     | 2.44 sec: 1.04x faster                                                       |
| k_core                     | 2.17 sec                                                     | 2.09 sec: 1.04x faster                                                       |
| 2to3                       | 293 ms                                                       | 282 ms: 1.04x faster                                                         |
| deltablue                  | 3.42 ms                                                      | 3.29 ms: 1.04x faster                                                        |
| meteor_contest             | 130 ms                                                       | 125 ms: 1.04x faster                                                         |
| xml_etree_generate         | 86.5 ms                                                      | 83.6 ms: 1.03x faster                                                        |
| django_template            | 36.4 ms                                                      | 35.2 ms: 1.03x faster                                                        |
| nbody                      | 89.3 ms                                                      | 86.5 ms: 1.03x faster                                                        |
| nqueens                    | 90.7 ms                                                      | 87.9 ms: 1.03x faster                                                        |
| sqlite_synth               | 2.91 us                                                      | 2.83 us: 1.03x faster                                                        |
| sympy_str                  | 298 ms                                                       | 290 ms: 1.03x faster                                                         |
| sqlalchemy_declarative     | 148 ms                                                       | 144 ms: 1.03x faster                                                         |
| sympy_expand               | 509 ms                                                       | 497 ms: 1.02x faster                                                         |
| sqlglot_normalize          | 119 ms                                                       | 117 ms: 1.02x faster                                                         |
| sympy_integrate            | 23.6 ms                                                      | 23.2 ms: 1.02x faster                                                        |
| sqlglot_optimize           | 59.3 ms                                                      | 58.3 ms: 1.02x faster                                                        |
| sympy_sum                  | 155 ms                                                       | 152 ms: 1.02x faster                                                         |
| sqlalchemy_imperative      | 18.3 ms                                                      | 18.0 ms: 1.02x faster                                                        |
| dulwich_log                | 68.2 ms                                                      | 67.2 ms: 1.01x faster                                                        |
| logging_silent             | 97.9 ns                                                      | 96.5 ns: 1.01x faster                                                        |
| coverage                   | 80.0 ms                                                      | 79.0 ms: 1.01x faster                                                        |
| python_startup_no_site     | 8.96 ms                                                      | 8.98 ms: 1.00x slower                                                        |
| python_startup             | 15.9 ms                                                      | 16.0 ms: 1.01x slower                                                        |
| logging_simple             | 6.39 us                                                      | 6.44 us: 1.01x slower                                                        |
| comprehensions             | 17.0 us                                                      | 17.2 us: 1.01x slower                                                        |
| pidigits                   | 252 ms                                                       | 254 ms: 1.01x slower                                                         |
| unpickle_pure_python       | 217 us                                                       | 220 us: 1.01x slower                                                         |
| raytrace                   | 273 ms                                                       | 276 ms: 1.01x slower                                                         |
| xml_etree_process          | 61.2 ms                                                      | 62.0 ms: 1.01x slower                                                        |
| chaos                      | 60.2 ms                                                      | 61.1 ms: 1.01x slower                                                        |
| regex_dna                  | 247 ms                                                       | 251 ms: 1.02x slower                                                         |
| docutils                   | 2.83 sec                                                     | 2.89 sec: 1.02x slower                                                       |
| crypto_pyaes               | 73.3 ms                                                      | 75.4 ms: 1.03x slower                                                        |
| logging_format             | 6.94 us                                                      | 7.14 us: 1.03x slower                                                        |
| json_loads                 | 24.7 us                                                      | 25.4 us: 1.03x slower                                                        |
| create_gc_cycles           | 2.68 ms                                                      | 2.78 ms: 1.04x slower                                                        |
| pickle_pure_python         | 323 us                                                       | 335 us: 1.04x slower                                                         |
| json_dumps                 | 11.1 ms                                                      | 11.6 ms: 1.04x slower                                                        |
| typing_runtime_protocols   | 169 us                                                       | 177 us: 1.05x slower                                                         |
| mako                       | 10.4 ms                                                      | 11.0 ms: 1.06x slower                                                        |
| many_optionals             | 930 us                                                       | 1.02 ms: 1.09x slower                                                        |
| gc_traversal               | 4.74 ms                                                      | 6.11 ms: 1.29x slower                                                        |
| subparsers                 | 17.5 ms                                                      | 22.8 ms: 1.30x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 1.63 sec: 317.76x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.00x slower                                                                 |

Benchmark hidden because not significant (7): bench_thread_pool, coroutines, asyncio_websockets, sphinx, pycparser, fannkuch, regex_v8
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.061x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.02x