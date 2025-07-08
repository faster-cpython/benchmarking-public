# Results vs. 3.13.0

- fork: faster-cpython
- ref: fast_side_exits
- machine: linux-x86_64
- commit hash: 73832b2
- commit date: 2025-07-08
- overall geometric mean: 1.047x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250708-pythonperf2-x86_64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 286 ms: 1.02x faster                                                             |
| docutils       | 2.83 sec                                                     | 2.91 sec: 1.03x slower                                                           |
| html5lib       | 73.5 ms                                                      | 66.8 ms: 1.10x faster                                                            |
| sphinx         | 1.12 sec                                                     | 1.10 sec: 1.02x faster                                                           |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250708-pythonperf2-x86_64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 333 ms: 1.40x faster                                                             |
| async_tree_memoization     | 453 ms                                                       | 331 ms: 1.37x faster                                                             |
| async_tree_none            | 376 ms                                                       | 275 ms: 1.37x faster                                                             |
| async_tree_io              | 843 ms                                                       | 624 ms: 1.35x faster                                                             |
| async_tree_io_tg           | 831 ms                                                       | 632 ms: 1.31x faster                                                             |
| async_tree_none_tg         | 346 ms                                                       | 273 ms: 1.27x faster                                                             |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 503 ms: 1.20x faster                                                             |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 510 ms: 1.14x faster                                                             |
| async_generators           | 457 ms                                                       | 444 ms: 1.03x faster                                                             |
| coroutines                 | 21.6 ms                                                      | 22.3 ms: 1.03x slower                                                            |
| Geometric mean             | (ref)                                                        | 1.21x faster                                                                     |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250708-pythonperf2-x86_64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 63.6 ms: 1.28x faster                                                            |
| pidigits       | 252 ms                                                       | 255 ms: 1.01x slower                                                             |
| nbody          | 89.3 ms                                                      | 99.7 ms: 1.12x slower                                                            |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250708-pythonperf2-x86_64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_v8       | 26.1 ms                                                      | 23.6 ms: 1.11x faster                                                            |
| regex_dna      | 247 ms                                                       | 225 ms: 1.09x faster                                                             |
| regex_compile  | 143 ms                                                       | 133 ms: 1.07x faster                                                             |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                     |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250708-pythonperf2-x86_64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 1.94 sec: 1.27x faster                                                           |
| xml_etree_parse      | 150 ms                                                       | 134 ms: 1.12x faster                                                             |
| xml_etree_process    | 61.2 ms                                                      | 55.4 ms: 1.10x faster                                                            |
| unpickle_pure_python | 217 us                                                       | 198 us: 1.10x faster                                                             |
| xml_etree_generate   | 86.5 ms                                                      | 78.9 ms: 1.10x faster                                                            |
| xml_etree_iterparse  | 103 ms                                                       | 96.9 ms: 1.06x faster                                                            |
| json_loads           | 24.7 us                                                      | 25.2 us: 1.02x slower                                                            |
| pickle_pure_python   | 323 us                                                       | 338 us: 1.05x slower                                                             |
| Geometric mean       | (ref)                                                        | 1.07x faster                                                                     |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250708-pythonperf2-x86_64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 15.4 ms: 1.04x faster                                                            |
| python_startup_no_site | 8.96 ms                                                      | 8.86 ms: 1.01x faster                                                            |
| Geometric mean         | (ref)                                                        | 1.02x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250708-pythonperf2-x86_64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 23.2 ms: 1.13x faster                                                            |
| genshi_xml      | 57.1 ms                                                      | 54.2 ms: 1.05x faster                                                            |
| mako            | 10.4 ms                                                      | 10.1 ms: 1.03x faster                                                            |
| django_template | 36.4 ms                                                      | 35.4 ms: 1.03x faster                                                            |
| Geometric mean  | (ref)                                                        | 1.06x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250708-pythonperf2-x86_64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.29 sec: 1.97x faster                                                           |
| richards                   | 52.9 ms                                                      | 34.5 ms: 1.53x faster                                                            |
| richards_super             | 59.6 ms                                                      | 40.3 ms: 1.48x faster                                                            |
| async_tree_memoization_tg  | 466 ms                                                       | 333 ms: 1.40x faster                                                             |
| deepcopy                   | 392 us                                                       | 281 us: 1.39x faster                                                             |
| deepcopy_memo              | 38.6 us                                                      | 28.1 us: 1.38x faster                                                            |
| async_tree_memoization     | 453 ms                                                       | 331 ms: 1.37x faster                                                             |
| async_tree_none            | 376 ms                                                       | 275 ms: 1.37x faster                                                             |
| async_tree_io              | 843 ms                                                       | 624 ms: 1.35x faster                                                             |
| async_tree_io_tg           | 831 ms                                                       | 632 ms: 1.31x faster                                                             |
| float                      | 81.3 ms                                                      | 63.6 ms: 1.28x faster                                                            |
| go                         | 162 ms                                                       | 127 ms: 1.28x faster                                                             |
| tomli_loads                | 2.46 sec                                                     | 1.94 sec: 1.27x faster                                                           |
| async_tree_none_tg         | 346 ms                                                       | 273 ms: 1.27x faster                                                             |
| pyflate                    | 503 ms                                                       | 405 ms: 1.24x faster                                                             |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 503 ms: 1.20x faster                                                             |
| spectral_norm              | 97.0 ms                                                      | 81.3 ms: 1.19x faster                                                            |
| generators                 | 33.6 ms                                                      | 28.2 ms: 1.19x faster                                                            |
| deltablue                  | 3.42 ms                                                      | 2.89 ms: 1.18x faster                                                            |
| deepcopy_reduce            | 3.54 us                                                      | 3.02 us: 1.17x faster                                                            |
| scimark_sor                | 123 ms                                                       | 105 ms: 1.17x faster                                                             |
| dulwich_log                | 68.2 ms                                                      | 59.8 ms: 1.14x faster                                                            |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 510 ms: 1.14x faster                                                             |
| genshi_text                | 26.2 ms                                                      | 23.2 ms: 1.13x faster                                                            |
| xml_etree_parse            | 150 ms                                                       | 134 ms: 1.12x faster                                                             |
| pprint_pformat             | 1.72 sec                                                     | 1.54 sec: 1.11x faster                                                           |
| bpe_tokeniser              | 5.09 sec                                                     | 4.57 sec: 1.11x faster                                                           |
| regex_v8                   | 26.1 ms                                                      | 23.6 ms: 1.11x faster                                                            |
| xml_etree_process          | 61.2 ms                                                      | 55.4 ms: 1.10x faster                                                            |
| pprint_safe_repr           | 843 ms                                                       | 766 ms: 1.10x faster                                                             |
| html5lib                   | 73.5 ms                                                      | 66.8 ms: 1.10x faster                                                            |
| unpickle_pure_python       | 217 us                                                       | 198 us: 1.10x faster                                                             |
| xml_etree_generate         | 86.5 ms                                                      | 78.9 ms: 1.10x faster                                                            |
| regex_dna                  | 247 ms                                                       | 225 ms: 1.09x faster                                                             |
| scimark_fft                | 328 ms                                                       | 303 ms: 1.08x faster                                                             |
| k_core                     | 2.17 sec                                                     | 2.00 sec: 1.08x faster                                                           |
| thrift                     | 901 us                                                       | 835 us: 1.08x faster                                                             |
| meteor_contest             | 130 ms                                                       | 121 ms: 1.07x faster                                                             |
| regex_compile              | 143 ms                                                       | 133 ms: 1.07x faster                                                             |
| hexiom                     | 6.55 ms                                                      | 6.13 ms: 1.07x faster                                                            |
| pylint                     | 347 ms                                                       | 325 ms: 1.07x faster                                                             |
| json                       | 5.69 ms                                                      | 5.35 ms: 1.06x faster                                                            |
| xml_etree_iterparse        | 103 ms                                                       | 96.9 ms: 1.06x faster                                                            |
| connected_components       | 432 ms                                                       | 408 ms: 1.06x faster                                                             |
| genshi_xml                 | 57.1 ms                                                      | 54.2 ms: 1.05x faster                                                            |
| sympy_integrate            | 23.6 ms                                                      | 22.4 ms: 1.05x faster                                                            |
| logging_silent             | 97.9 ns                                                      | 93.3 ns: 1.05x faster                                                            |
| scimark_monte_carlo        | 66.1 ms                                                      | 63.3 ms: 1.05x faster                                                            |
| logging_simple             | 6.39 us                                                      | 6.15 us: 1.04x faster                                                            |
| shortest_path              | 460 ms                                                       | 443 ms: 1.04x faster                                                             |
| python_startup             | 15.9 ms                                                      | 15.4 ms: 1.04x faster                                                            |
| pathlib                    | 17.5 ms                                                      | 17.0 ms: 1.03x faster                                                            |
| async_generators           | 457 ms                                                       | 444 ms: 1.03x faster                                                             |
| mako                       | 10.4 ms                                                      | 10.1 ms: 1.03x faster                                                            |
| sympy_str                  | 298 ms                                                       | 290 ms: 1.03x faster                                                             |
| django_template            | 36.4 ms                                                      | 35.4 ms: 1.03x faster                                                            |
| sympy_sum                  | 155 ms                                                       | 151 ms: 1.03x faster                                                             |
| sympy_expand               | 509 ms                                                       | 497 ms: 1.02x faster                                                             |
| sphinx                     | 1.12 sec                                                     | 1.10 sec: 1.02x faster                                                           |
| logging_format             | 6.94 us                                                      | 6.79 us: 1.02x faster                                                            |
| 2to3                       | 293 ms                                                       | 286 ms: 1.02x faster                                                             |
| python_startup_no_site     | 8.96 ms                                                      | 8.86 ms: 1.01x faster                                                            |
| chaos                      | 60.2 ms                                                      | 60.4 ms: 1.00x slower                                                            |
| coverage                   | 80.0 ms                                                      | 80.3 ms: 1.00x slower                                                            |
| pidigits                   | 252 ms                                                       | 255 ms: 1.01x slower                                                             |
| nqueens                    | 90.7 ms                                                      | 92.5 ms: 1.02x slower                                                            |
| json_loads                 | 24.7 us                                                      | 25.2 us: 1.02x slower                                                            |
| scimark_lu                 | 98.7 ms                                                      | 101 ms: 1.02x slower                                                             |
| comprehensions             | 17.0 us                                                      | 17.5 us: 1.03x slower                                                            |
| typing_runtime_protocols   | 169 us                                                       | 174 us: 1.03x slower                                                             |
| docutils                   | 2.83 sec                                                     | 2.91 sec: 1.03x slower                                                           |
| coroutines                 | 21.6 ms                                                      | 22.3 ms: 1.03x slower                                                            |
| pickle_pure_python         | 323 us                                                       | 338 us: 1.05x slower                                                             |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 5.00 ms: 1.05x slower                                                            |
| fannkuch                   | 363 ms                                                       | 383 ms: 1.05x slower                                                             |
| crypto_pyaes               | 73.3 ms                                                      | 77.6 ms: 1.06x slower                                                            |
| create_gc_cycles           | 2.68 ms                                                      | 2.84 ms: 1.06x slower                                                            |
| raytrace                   | 273 ms                                                       | 294 ms: 1.08x slower                                                             |
| nbody                      | 89.3 ms                                                      | 99.7 ms: 1.12x slower                                                            |
| many_optionals             | 930 us                                                       | 1.04 ms: 1.12x slower                                                            |
| gc_traversal               | 4.74 ms                                                      | 6.48 ms: 1.37x slower                                                            |
| subparsers                 | 17.5 ms                                                      | 25.1 ms: 1.44x slower                                                            |
| telco                      | 8.79 ms                                                      | 160 ms: 18.24x slower                                                            |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                                     |

Benchmark hidden because not significant (5): djangocms, asyncio_websockets, json_dumps, regex_effbot, sqlite_synth
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, pycparser, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250708-3.15.0a0-73832b2-JIT/bm-20250708-pythonperf2-x86_64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.047x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.12x