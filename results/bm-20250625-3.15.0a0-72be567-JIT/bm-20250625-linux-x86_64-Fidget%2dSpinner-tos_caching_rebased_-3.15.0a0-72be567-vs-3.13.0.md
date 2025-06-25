# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: tos_caching_rebased_
- machine: linux-x86_64
- commit hash: 72be567
- commit date: 2025-06-25
- overall geometric mean: 1.056x faster
- HPT reliability: 99.95%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250625-linux-x86_64-Fidget%2dSpinner-tos_caching_rebased_-3.15.0a0-72be567 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 260 ms: 1.02x faster                                                            |
| docutils       | 2.58 sec                                               | 2.65 sec: 1.02x slower                                                          |
| html5lib       | 63.4 ms                                                | 61.7 ms: 1.03x faster                                                           |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250625-linux-x86_64-Fidget%2dSpinner-tos_caching_rebased_-3.15.0a0-72be567 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                                            |
| async_tree_io_tg           | 861 ms                                                 | 615 ms: 1.40x faster                                                            |
| async_tree_io              | 838 ms                                                 | 600 ms: 1.40x faster                                                            |
| async_tree_memoization     | 437 ms                                                 | 316 ms: 1.38x faster                                                            |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                            |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                                            |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 493 ms: 1.16x faster                                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 487 ms: 1.12x faster                                                            |
| async_generators           | 433 ms                                                 | 431 ms: 1.01x faster                                                            |
| coroutines                 | 22.2 ms                                                | 24.6 ms: 1.11x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250625-linux-x86_64-Fidget%2dSpinner-tos_caching_rebased_-3.15.0a0-72be567 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 65.3 ms: 1.20x faster                                                           |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                            |
| nbody          | 87.7 ms                                                | 90.2 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250625-linux-x86_64-Fidget%2dSpinner-tos_caching_rebased_-3.15.0a0-72be567 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.4 ms: 1.15x faster                                                           |
| regex_effbot   | 3.77 ms                                                | 3.32 ms: 1.14x faster                                                           |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                                            |
| regex_dna      | 220 ms                                                 | 214 ms: 1.03x faster                                                            |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250625-linux-x86_64-Fidget%2dSpinner-tos_caching_rebased_-3.15.0a0-72be567 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.84 sec: 1.15x faster                                                          |
| xml_etree_parse      | 154 ms                                                 | 140 ms: 1.10x faster                                                            |
| xml_etree_process    | 60.5 ms                                                | 55.7 ms: 1.09x faster                                                           |
| xml_etree_generate   | 86.8 ms                                                | 80.8 ms: 1.08x faster                                                           |
| unpickle_pure_python | 213 us                                                 | 201 us: 1.06x faster                                                            |
| xml_etree_iterparse  | 101 ms                                                 | 99.5 ms: 1.02x faster                                                           |
| pickle_pure_python   | 302 us                                                 | 320 us: 1.06x slower                                                            |
| json_loads           | 27.2 us                                                | 28.8 us: 1.06x slower                                                           |
| json_dumps           | 10.1 ms                                                | 11.0 ms: 1.08x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250625-linux-x86_64-Fidget%2dSpinner-tos_caching_rebased_-3.15.0a0-72be567 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.1 ms: 1.04x faster                                                           |
| python_startup_no_site | 7.00 ms                                                | 6.93 ms: 1.01x faster                                                           |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250625-linux-x86_64-Fidget%2dSpinner-tos_caching_rebased_-3.15.0a0-72be567 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.4 ms: 1.06x faster                                                           |
| genshi_xml      | 50.5 ms                                                | 49.8 ms: 1.01x faster                                                           |
| mako            | 10.7 ms                                                | 10.6 ms: 1.01x faster                                                           |
| django_template | 31.7 ms                                                | 32.2 ms: 1.02x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250625-linux-x86_64-Fidget%2dSpinner-tos_caching_rebased_-3.15.0a0-72be567 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.24 sec: 2.05x faster                                                          |
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                                            |
| richards                   | 47.5 ms                                                | 33.4 ms: 1.42x faster                                                           |
| async_tree_io_tg           | 861 ms                                                 | 615 ms: 1.40x faster                                                            |
| async_tree_io              | 838 ms                                                 | 600 ms: 1.40x faster                                                            |
| async_tree_memoization     | 437 ms                                                 | 316 ms: 1.38x faster                                                            |
| deepcopy                   | 354 us                                                 | 259 us: 1.37x faster                                                            |
| richards_super             | 53.7 ms                                                | 39.2 ms: 1.37x faster                                                           |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                            |
| deepcopy_memo              | 38.4 us                                                | 29.3 us: 1.31x faster                                                           |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                                            |
| spectral_norm              | 113 ms                                                 | 93.8 ms: 1.21x faster                                                           |
| float                      | 78.7 ms                                                | 65.3 ms: 1.20x faster                                                           |
| deepcopy_reduce            | 3.24 us                                                | 2.73 us: 1.19x faster                                                           |
| scimark_fft                | 367 ms                                                 | 315 ms: 1.16x faster                                                            |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 493 ms: 1.16x faster                                                            |
| go                         | 141 ms                                                 | 121 ms: 1.16x faster                                                            |
| pyflate                    | 470 ms                                                 | 407 ms: 1.15x faster                                                            |
| regex_v8                   | 26.9 ms                                                | 23.4 ms: 1.15x faster                                                           |
| tomli_loads                | 2.12 sec                                               | 1.84 sec: 1.15x faster                                                          |
| regex_effbot               | 3.77 ms                                                | 3.32 ms: 1.14x faster                                                           |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 487 ms: 1.12x faster                                                            |
| pylint                     | 312 ms                                                 | 282 ms: 1.10x faster                                                            |
| xml_etree_parse            | 154 ms                                                 | 140 ms: 1.10x faster                                                            |
| dulwich_log                | 64.6 ms                                                | 59.2 ms: 1.09x faster                                                           |
| telco                      | 8.40 ms                                                | 7.71 ms: 1.09x faster                                                           |
| xml_etree_process          | 60.5 ms                                                | 55.7 ms: 1.09x faster                                                           |
| bpe_tokeniser              | 4.69 sec                                               | 4.36 sec: 1.08x faster                                                          |
| xml_etree_generate         | 86.8 ms                                                | 80.8 ms: 1.08x faster                                                           |
| unpickle_pure_python       | 213 us                                                 | 201 us: 1.06x faster                                                            |
| genshi_text                | 22.6 ms                                                | 21.4 ms: 1.06x faster                                                           |
| python_startup             | 12.7 ms                                                | 12.1 ms: 1.04x faster                                                           |
| pycparser                  | 1.20 sec                                               | 1.15 sec: 1.04x faster                                                          |
| sqlite_synth               | 2.90 us                                                | 2.79 us: 1.04x faster                                                           |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                                            |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.04x faster                                                          |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.03x faster                                                            |
| deltablue                  | 3.19 ms                                                | 3.10 ms: 1.03x faster                                                           |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.03x faster                                                            |
| html5lib                   | 63.4 ms                                                | 61.7 ms: 1.03x faster                                                           |
| regex_dna                  | 220 ms                                                 | 214 ms: 1.03x faster                                                            |
| sympy_integrate            | 19.8 ms                                                | 19.3 ms: 1.03x faster                                                           |
| thrift                     | 800 us                                                 | 781 us: 1.02x faster                                                            |
| 2to3                       | 266 ms                                                 | 260 ms: 1.02x faster                                                            |
| scimark_monte_carlo        | 66.8 ms                                                | 65.5 ms: 1.02x faster                                                           |
| pathlib                    | 17.4 ms                                                | 17.1 ms: 1.02x faster                                                           |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.94 ms: 1.02x faster                                                           |
| xml_etree_iterparse        | 101 ms                                                 | 99.5 ms: 1.02x faster                                                           |
| genshi_xml                 | 50.5 ms                                                | 49.8 ms: 1.01x faster                                                           |
| python_startup_no_site     | 7.00 ms                                                | 6.93 ms: 1.01x faster                                                           |
| mako                       | 10.7 ms                                                | 10.6 ms: 1.01x faster                                                           |
| async_generators           | 433 ms                                                 | 431 ms: 1.01x faster                                                            |
| gc_traversal               | 4.90 ms                                                | 4.93 ms: 1.01x slower                                                           |
| crypto_pyaes               | 74.7 ms                                                | 75.3 ms: 1.01x slower                                                           |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                                            |
| shortest_path              | 487 ms                                                 | 493 ms: 1.01x slower                                                            |
| connected_components       | 447 ms                                                 | 455 ms: 1.02x slower                                                            |
| django_template            | 31.7 ms                                                | 32.2 ms: 1.02x slower                                                           |
| nqueens                    | 80.9 ms                                                | 82.6 ms: 1.02x slower                                                           |
| docutils                   | 2.58 sec                                               | 2.65 sec: 1.02x slower                                                          |
| sympy_expand               | 456 ms                                                 | 468 ms: 1.03x slower                                                            |
| nbody                      | 87.7 ms                                                | 90.2 ms: 1.03x slower                                                           |
| scimark_lu                 | 114 ms                                                 | 118 ms: 1.03x slower                                                            |
| comprehensions             | 16.5 us                                                | 17.1 us: 1.04x slower                                                           |
| chaos                      | 58.0 ms                                                | 61.1 ms: 1.05x slower                                                           |
| raytrace                   | 262 ms                                                 | 275 ms: 1.05x slower                                                            |
| create_gc_cycles           | 2.45 ms                                                | 2.58 ms: 1.06x slower                                                           |
| coverage                   | 82.8 ms                                                | 87.5 ms: 1.06x slower                                                           |
| pickle_pure_python         | 302 us                                                 | 320 us: 1.06x slower                                                            |
| typing_runtime_protocols   | 160 us                                                 | 170 us: 1.06x slower                                                            |
| json_loads                 | 27.2 us                                                | 28.8 us: 1.06x slower                                                           |
| hexiom                     | 6.08 ms                                                | 6.48 ms: 1.07x slower                                                           |
| logging_simple             | 5.65 us                                                | 6.05 us: 1.07x slower                                                           |
| generators                 | 28.8 ms                                                | 30.9 ms: 1.07x slower                                                           |
| json_dumps                 | 10.1 ms                                                | 11.0 ms: 1.08x slower                                                           |
| logging_format             | 6.23 us                                                | 6.77 us: 1.09x slower                                                           |
| coroutines                 | 22.2 ms                                                | 24.6 ms: 1.11x slower                                                           |
| pprint_pformat             | 1.48 sec                                               | 1.67 sec: 1.13x slower                                                          |
| pprint_safe_repr           | 727 ms                                                 | 826 ms: 1.14x slower                                                            |
| many_optionals             | 857 us                                                 | 977 us: 1.14x slower                                                            |
| subparsers                 | 15.5 ms                                                | 23.6 ms: 1.53x slower                                                           |
| logging_silent             | 101 ns                                                 | 476 ns: 4.71x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                                    |

Benchmark hidden because not significant (7): sphinx, sympy_str, json, sympy_sum, fannkuch, asyncio_websockets, djangocms
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250625-3.15.0a0-72be567-JIT/bm-20250625-linux-x86_64-Fidget%2dSpinner-tos_caching_rebased_-3.15.0a0-72be567.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.056x faster

# HPT report

- Reliability score: 99.95% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x