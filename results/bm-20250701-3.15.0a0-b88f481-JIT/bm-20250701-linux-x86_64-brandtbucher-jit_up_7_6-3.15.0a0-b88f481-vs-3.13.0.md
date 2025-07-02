# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_up_7_6
- machine: linux-x86_64
- commit hash: b88f481
- commit date: 2025-07-01
- overall geometric mean: 1.065x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_6-3.15.0a0-b88f481 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 265 ms: 1.00x faster                                              |
| docutils       | 2.58 sec                                               | 2.67 sec: 1.03x slower                                            |
| html5lib       | 63.4 ms                                                | 62.0 ms: 1.02x faster                                             |
| Geometric mean | (ref)                                                  | 1.00x faster                                                      |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_6-3.15.0a0-b88f481 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 311 ms: 1.49x faster                                              |
| async_tree_memoization     | 437 ms                                                 | 313 ms: 1.39x faster                                              |
| async_tree_io              | 838 ms                                                 | 603 ms: 1.39x faster                                              |
| async_tree_io_tg           | 861 ms                                                 | 637 ms: 1.35x faster                                              |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                              |
| async_tree_none_tg         | 319 ms                                                 | 248 ms: 1.29x faster                                              |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 492 ms: 1.17x faster                                              |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 483 ms: 1.12x faster                                              |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                              |
| coroutines                 | 22.2 ms                                                | 25.0 ms: 1.13x slower                                             |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                      |

Benchmark hidden because not significant (1): async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_6-3.15.0a0-b88f481 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 78.7 ms                                                | 65.7 ms: 1.20x faster                                             |
| pidigits       | 186 ms                                                 | 196 ms: 1.05x slower                                              |
| nbody          | 87.7 ms                                                | 93.0 ms: 1.06x slower                                             |
| Geometric mean | (ref)                                                  | 1.02x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_6-3.15.0a0-b88f481 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 22.5 ms: 1.20x faster                                             |
| regex_effbot   | 3.77 ms                                                | 3.32 ms: 1.14x faster                                             |
| regex_dna      | 220 ms                                                 | 202 ms: 1.09x faster                                              |
| regex_compile  | 132 ms                                                 | 129 ms: 1.02x faster                                              |
| Geometric mean | (ref)                                                  | 1.11x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_6-3.15.0a0-b88f481 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.84 sec: 1.15x faster                                            |
| xml_etree_parse      | 154 ms                                                 | 139 ms: 1.11x faster                                              |
| unpickle_pure_python | 213 us                                                 | 196 us: 1.09x faster                                              |
| xml_etree_process    | 60.5 ms                                                | 55.8 ms: 1.08x faster                                             |
| xml_etree_generate   | 86.8 ms                                                | 80.4 ms: 1.08x faster                                             |
| xml_etree_iterparse  | 101 ms                                                 | 98.2 ms: 1.03x faster                                             |
| json_loads           | 27.2 us                                                | 28.3 us: 1.04x slower                                             |
| pickle_pure_python   | 302 us                                                 | 321 us: 1.06x slower                                              |
| json_dumps           | 10.1 ms                                                | 11.0 ms: 1.09x slower                                             |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_6-3.15.0a0-b88f481 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                             |
| python_startup_no_site | 7.00 ms                                                | 6.94 ms: 1.01x faster                                             |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_6-3.15.0a0-b88f481 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.5 ms: 1.05x faster                                             |
| mako            | 10.7 ms                                                | 10.5 ms: 1.01x faster                                             |
| django_template | 31.7 ms                                                | 32.7 ms: 1.03x slower                                             |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                      |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_6-3.15.0a0-b88f481 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.23 sec: 2.07x faster                                            |
| richards                   | 47.5 ms                                                | 31.3 ms: 1.52x faster                                             |
| async_tree_memoization_tg  | 463 ms                                                 | 311 ms: 1.49x faster                                              |
| richards_super             | 53.7 ms                                                | 36.2 ms: 1.48x faster                                             |
| async_tree_memoization     | 437 ms                                                 | 313 ms: 1.39x faster                                              |
| async_tree_io              | 838 ms                                                 | 603 ms: 1.39x faster                                              |
| deepcopy                   | 354 us                                                 | 259 us: 1.37x faster                                              |
| async_tree_io_tg           | 861 ms                                                 | 637 ms: 1.35x faster                                              |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                              |
| deepcopy_memo              | 38.4 us                                                | 29.7 us: 1.29x faster                                             |
| async_tree_none_tg         | 319 ms                                                 | 248 ms: 1.29x faster                                              |
| go                         | 141 ms                                                 | 114 ms: 1.24x faster                                              |
| spectral_norm              | 113 ms                                                 | 92.2 ms: 1.23x faster                                             |
| float                      | 78.7 ms                                                | 65.7 ms: 1.20x faster                                             |
| regex_v8                   | 26.9 ms                                                | 22.5 ms: 1.20x faster                                             |
| deepcopy_reduce            | 3.24 us                                                | 2.75 us: 1.18x faster                                             |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 492 ms: 1.17x faster                                              |
| scimark_fft                | 367 ms                                                 | 315 ms: 1.17x faster                                              |
| pyflate                    | 470 ms                                                 | 406 ms: 1.16x faster                                              |
| tomli_loads                | 2.12 sec                                               | 1.84 sec: 1.15x faster                                            |
| regex_effbot               | 3.77 ms                                                | 3.32 ms: 1.14x faster                                             |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 483 ms: 1.12x faster                                              |
| xml_etree_parse            | 154 ms                                                 | 139 ms: 1.11x faster                                              |
| telco                      | 8.40 ms                                                | 7.63 ms: 1.10x faster                                             |
| regex_dna                  | 220 ms                                                 | 202 ms: 1.09x faster                                              |
| unpickle_pure_python       | 213 us                                                 | 196 us: 1.09x faster                                              |
| xml_etree_process          | 60.5 ms                                                | 55.8 ms: 1.08x faster                                             |
| dulwich_log                | 64.6 ms                                                | 59.7 ms: 1.08x faster                                             |
| pylint                     | 312 ms                                                 | 288 ms: 1.08x faster                                              |
| xml_etree_generate         | 86.8 ms                                                | 80.4 ms: 1.08x faster                                             |
| bpe_tokeniser              | 4.69 sec                                               | 4.40 sec: 1.07x faster                                            |
| pycparser                  | 1.20 sec                                               | 1.13 sec: 1.07x faster                                            |
| genshi_text                | 22.6 ms                                                | 21.5 ms: 1.05x faster                                             |
| deltablue                  | 3.19 ms                                                | 3.05 ms: 1.05x faster                                             |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.82 ms: 1.04x faster                                             |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                             |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                            |
| scimark_sor                | 122 ms                                                 | 118 ms: 1.04x faster                                              |
| xml_etree_iterparse        | 101 ms                                                 | 98.2 ms: 1.03x faster                                             |
| thrift                     | 800 us                                                 | 777 us: 1.03x faster                                              |
| sqlite_synth               | 2.90 us                                                | 2.82 us: 1.03x faster                                             |
| regex_compile              | 132 ms                                                 | 129 ms: 1.02x faster                                              |
| html5lib                   | 63.4 ms                                                | 62.0 ms: 1.02x faster                                             |
| pprint_pformat             | 1.48 sec                                               | 1.45 sec: 1.02x faster                                            |
| json                       | 5.32 ms                                                | 5.24 ms: 1.02x faster                                             |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                              |
| mako                       | 10.7 ms                                                | 10.5 ms: 1.01x faster                                             |
| pathlib                    | 17.4 ms                                                | 17.2 ms: 1.01x faster                                             |
| python_startup_no_site     | 7.00 ms                                                | 6.94 ms: 1.01x faster                                             |
| logging_simple             | 5.65 us                                                | 5.61 us: 1.01x faster                                             |
| fannkuch                   | 394 ms                                                 | 391 ms: 1.01x faster                                              |
| comprehensions             | 16.5 us                                                | 16.4 us: 1.01x faster                                             |
| sympy_integrate            | 19.8 ms                                                | 19.8 ms: 1.00x faster                                             |
| 2to3                       | 266 ms                                                 | 265 ms: 1.00x faster                                              |
| gc_traversal               | 4.90 ms                                                | 4.91 ms: 1.00x slower                                             |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                              |
| nqueens                    | 80.9 ms                                                | 81.5 ms: 1.01x slower                                             |
| connected_components       | 447 ms                                                 | 453 ms: 1.01x slower                                              |
| sympy_sum                  | 150 ms                                                 | 154 ms: 1.02x slower                                              |
| logging_silent             | 101 ns                                                 | 103 ns: 1.02x slower                                              |
| hexiom                     | 6.08 ms                                                | 6.22 ms: 1.02x slower                                             |
| sympy_expand               | 456 ms                                                 | 467 ms: 1.02x slower                                              |
| scimark_lu                 | 114 ms                                                 | 118 ms: 1.03x slower                                              |
| django_template            | 31.7 ms                                                | 32.7 ms: 1.03x slower                                             |
| djangocms                  | 22.3 us                                                | 23.0 us: 1.03x slower                                             |
| docutils                   | 2.58 sec                                               | 2.67 sec: 1.03x slower                                            |
| raytrace                   | 262 ms                                                 | 271 ms: 1.04x slower                                              |
| json_loads                 | 27.2 us                                                | 28.3 us: 1.04x slower                                             |
| chaos                      | 58.0 ms                                                | 60.4 ms: 1.04x slower                                             |
| typing_runtime_protocols   | 160 us                                                 | 167 us: 1.05x slower                                              |
| pidigits                   | 186 ms                                                 | 196 ms: 1.05x slower                                              |
| generators                 | 28.8 ms                                                | 30.4 ms: 1.06x slower                                             |
| pickle_pure_python         | 302 us                                                 | 321 us: 1.06x slower                                              |
| nbody                      | 87.7 ms                                                | 93.0 ms: 1.06x slower                                             |
| create_gc_cycles           | 2.45 ms                                                | 2.60 ms: 1.06x slower                                             |
| coverage                   | 82.8 ms                                                | 88.5 ms: 1.07x slower                                             |
| json_dumps                 | 10.1 ms                                                | 11.0 ms: 1.09x slower                                             |
| coroutines                 | 22.2 ms                                                | 25.0 ms: 1.13x slower                                             |
| many_optionals             | 857 us                                                 | 999 us: 1.17x slower                                              |
| subparsers                 | 15.5 ms                                                | 23.5 ms: 1.52x slower                                             |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                      |

Benchmark hidden because not significant (9): crypto_pyaes, sphinx, pprint_safe_repr, scimark_monte_carlo, genshi_xml, async_generators, logging_format, sympy_str, shortest_path
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250701-3.15.0a0-b88f481-JIT/bm-20250701-linux-x86_64-brandtbucher-jit_up_7_6-3.15.0a0-b88f481.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.065x faster

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x