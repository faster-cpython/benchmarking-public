# Results vs. 3.13.0

- fork: faster-cpython
- ref: jit_trampoline
- machine: windows-amd64
- commit hash: 14080cb
- commit date: 2025-08-19
- overall geometric mean: 1.082x faster
- HPT reliability: 89.29%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250819-pythonperf1-amd64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 219 ms: 1.02x slower                                                           |
| docutils       | 1.53 sec                                                    | 1.66 sec: 1.08x slower                                                         |
| html5lib       | 38.2 ms                                                     | 38.9 ms: 1.02x slower                                                          |
| sphinx         | 617 ms                                                      | 638 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250819-pythonperf1-amd64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 155 ms: 1.93x faster                                                           |
| async_tree_memoization_tg  | 281 ms                                                      | 207 ms: 1.35x faster                                                           |
| async_tree_io              | 513 ms                                                      | 393 ms: 1.31x faster                                                           |
| async_tree_memoization     | 265 ms                                                      | 204 ms: 1.30x faster                                                           |
| async_tree_io_tg           | 497 ms                                                      | 388 ms: 1.28x faster                                                           |
| async_tree_none            | 219 ms                                                      | 173 ms: 1.27x faster                                                           |
| async_tree_none_tg         | 200 ms                                                      | 168 ms: 1.19x faster                                                           |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 331 ms: 1.15x faster                                                           |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 336 ms: 1.14x faster                                                           |
| async_generators           | 223 ms                                                      | 247 ms: 1.11x slower                                                           |
| coroutines                 | 12.5 ms                                                     | 14.5 ms: 1.16x slower                                                          |
| Geometric mean             | (ref)                                                       | 1.22x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250819-pythonperf1-amd64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 43.6 ms: 1.17x faster                                                          |
| nbody          | 66.3 ms                                                     | 58.0 ms: 1.14x faster                                                          |
| pidigits       | 146 ms                                                      | 148 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250819-pythonperf1-amd64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.9 ms: 1.71x faster                                                          |
| regex_effbot   | 1.69 ms                                                     | 1.57 ms: 1.08x faster                                                          |
| regex_compile  | 80.7 ms                                                     | 79.2 ms: 1.02x faster                                                          |
| regex_dna      | 115 ms                                                      | 118 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250819-pythonperf1-amd64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle_pure_python | 130 us                                                      | 105 us: 1.24x faster                                                           |
| tomli_loads          | 1.37 sec                                                    | 1.12 sec: 1.22x faster                                                         |
| json_dumps           | 6.19 ms                                                     | 5.34 ms: 1.16x faster                                                          |
| json_loads           | 15.1 us                                                     | 14.0 us: 1.08x faster                                                          |
| xml_etree_generate   | 53.5 ms                                                     | 50.9 ms: 1.05x faster                                                          |
| xml_etree_parse      | 92.2 ms                                                     | 88.6 ms: 1.04x faster                                                          |
| xml_etree_process    | 36.5 ms                                                     | 36.2 ms: 1.01x faster                                                          |
| xml_etree_iterparse  | 60.5 ms                                                     | 64.5 ms: 1.07x slower                                                          |
| pickle_pure_python   | 186 us                                                      | 205 us: 1.10x slower                                                           |
| Geometric mean       | (ref)                                                       | 1.07x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250819-pythonperf1-amd64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.8 ms: 1.06x slower                                                          |
| python_startup_no_site | 16.9 ms                                                     | 19.0 ms: 1.12x slower                                                          |
| Geometric mean         | (ref)                                                       | 1.09x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250819-pythonperf1-amd64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.34 ms: 1.23x faster                                                          |
| genshi_text     | 15.2 ms                                                     | 15.7 ms: 1.03x slower                                                          |
| genshi_xml      | 33.9 ms                                                     | 35.4 ms: 1.05x slower                                                          |
| django_template | 20.3 ms                                                     | 24.2 ms: 1.19x slower                                                          |
| Geometric mean  | (ref)                                                       | 1.01x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250819-pythonperf1-amd64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 501 us: 16.88x faster                                                          |
| pathlib                    | 75.3 ms                                                     | 29.3 ms: 2.57x faster                                                          |
| asyncio_websockets         | 300 ms                                                      | 155 ms: 1.93x faster                                                           |
| mdp                        | 1.43 sec                                                    | 802 ms: 1.78x faster                                                           |
| regex_v8                   | 23.8 ms                                                     | 13.9 ms: 1.71x faster                                                          |
| async_tree_memoization_tg  | 281 ms                                                      | 207 ms: 1.35x faster                                                           |
| async_tree_io              | 513 ms                                                      | 393 ms: 1.31x faster                                                           |
| deepcopy                   | 223 us                                                      | 171 us: 1.30x faster                                                           |
| async_tree_memoization     | 265 ms                                                      | 204 ms: 1.30x faster                                                           |
| deepcopy_memo              | 23.1 us                                                     | 18.0 us: 1.28x faster                                                          |
| async_tree_io_tg           | 497 ms                                                      | 388 ms: 1.28x faster                                                           |
| async_tree_none            | 219 ms                                                      | 173 ms: 1.27x faster                                                           |
| unpickle_pure_python       | 130 us                                                      | 105 us: 1.24x faster                                                           |
| mako                       | 6.56 ms                                                     | 5.34 ms: 1.23x faster                                                          |
| tomli_loads                | 1.37 sec                                                    | 1.12 sec: 1.22x faster                                                         |
| fannkuch                   | 252 ms                                                      | 210 ms: 1.20x faster                                                           |
| telco                      | 4.85 ms                                                     | 4.06 ms: 1.20x faster                                                          |
| async_tree_none_tg         | 200 ms                                                      | 168 ms: 1.19x faster                                                           |
| float                      | 50.8 ms                                                     | 43.6 ms: 1.17x faster                                                          |
| json_dumps                 | 6.19 ms                                                     | 5.34 ms: 1.16x faster                                                          |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 331 ms: 1.15x faster                                                           |
| nbody                      | 66.3 ms                                                     | 58.0 ms: 1.14x faster                                                          |
| scimark_fft                | 175 ms                                                      | 153 ms: 1.14x faster                                                           |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.29 ms: 1.14x faster                                                          |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 336 ms: 1.14x faster                                                           |
| bpe_tokeniser              | 2.87 sec                                                    | 2.59 sec: 1.11x faster                                                         |
| pprint_safe_repr           | 485 ms                                                      | 440 ms: 1.10x faster                                                           |
| json                       | 3.30 ms                                                     | 3.00 ms: 1.10x faster                                                          |
| pprint_pformat             | 977 ms                                                      | 890 ms: 1.10x faster                                                           |
| go                         | 84.7 ms                                                     | 77.8 ms: 1.09x faster                                                          |
| pyflate                    | 283 ms                                                      | 261 ms: 1.09x faster                                                           |
| deepcopy_reduce            | 2.02 us                                                     | 1.87 us: 1.08x faster                                                          |
| json_loads                 | 15.1 us                                                     | 14.0 us: 1.08x faster                                                          |
| regex_effbot               | 1.69 ms                                                     | 1.57 ms: 1.08x faster                                                          |
| k_core                     | 1.70 sec                                                    | 1.61 sec: 1.06x faster                                                         |
| xml_etree_generate         | 53.5 ms                                                     | 50.9 ms: 1.05x faster                                                          |
| xml_etree_parse            | 92.2 ms                                                     | 88.6 ms: 1.04x faster                                                          |
| sqlite_synth               | 1.59 us                                                     | 1.54 us: 1.03x faster                                                          |
| regex_compile              | 80.7 ms                                                     | 79.2 ms: 1.02x faster                                                          |
| scimark_monte_carlo        | 40.7 ms                                                     | 40.2 ms: 1.01x faster                                                          |
| typing_runtime_protocols   | 103 us                                                      | 102 us: 1.01x faster                                                           |
| shortest_path              | 355 ms                                                      | 352 ms: 1.01x faster                                                           |
| meteor_contest             | 72.0 ms                                                     | 71.4 ms: 1.01x faster                                                          |
| xml_etree_process          | 36.5 ms                                                     | 36.2 ms: 1.01x faster                                                          |
| logging_silent             | 54.6 ns                                                     | 54.3 ns: 1.00x faster                                                          |
| dulwich_log                | 40.1 ms                                                     | 40.4 ms: 1.01x slower                                                          |
| pidigits                   | 146 ms                                                      | 148 ms: 1.01x slower                                                           |
| scimark_sor                | 76.2 ms                                                     | 76.9 ms: 1.01x slower                                                          |
| connected_components       | 320 ms                                                      | 323 ms: 1.01x slower                                                           |
| comprehensions             | 10.4 us                                                     | 10.5 us: 1.02x slower                                                          |
| 2to3                       | 215 ms                                                      | 219 ms: 1.02x slower                                                           |
| html5lib                   | 38.2 ms                                                     | 38.9 ms: 1.02x slower                                                          |
| sympy_str                  | 167 ms                                                      | 170 ms: 1.02x slower                                                           |
| sympy_sum                  | 85.2 ms                                                     | 87.2 ms: 1.02x slower                                                          |
| regex_dna                  | 115 ms                                                      | 118 ms: 1.03x slower                                                           |
| spectral_norm              | 63.4 ms                                                     | 65.3 ms: 1.03x slower                                                          |
| generators                 | 19.0 ms                                                     | 19.5 ms: 1.03x slower                                                          |
| sphinx                     | 617 ms                                                      | 638 ms: 1.03x slower                                                           |
| sympy_integrate            | 12.3 ms                                                     | 12.8 ms: 1.03x slower                                                          |
| create_gc_cycles           | 1.22 ms                                                     | 1.27 ms: 1.03x slower                                                          |
| logging_simple             | 5.77 us                                                     | 5.97 us: 1.03x slower                                                          |
| genshi_text                | 15.2 ms                                                     | 15.7 ms: 1.03x slower                                                          |
| sympy_expand               | 286 ms                                                      | 298 ms: 1.04x slower                                                           |
| logging_format             | 6.18 us                                                     | 6.45 us: 1.04x slower                                                          |
| genshi_xml                 | 33.9 ms                                                     | 35.4 ms: 1.05x slower                                                          |
| richards_super             | 29.8 ms                                                     | 31.3 ms: 1.05x slower                                                          |
| python_startup             | 24.4 ms                                                     | 25.8 ms: 1.06x slower                                                          |
| hexiom                     | 3.84 ms                                                     | 4.06 ms: 1.06x slower                                                          |
| richards                   | 26.3 ms                                                     | 27.9 ms: 1.06x slower                                                          |
| xml_etree_iterparse        | 60.5 ms                                                     | 64.5 ms: 1.07x slower                                                          |
| gc_traversal               | 1.96 ms                                                     | 2.10 ms: 1.07x slower                                                          |
| chaos                      | 37.9 ms                                                     | 40.7 ms: 1.07x slower                                                          |
| scimark_lu                 | 56.7 ms                                                     | 61.1 ms: 1.08x slower                                                          |
| nqueens                    | 56.1 ms                                                     | 60.8 ms: 1.08x slower                                                          |
| docutils                   | 1.53 sec                                                    | 1.66 sec: 1.08x slower                                                         |
| coverage                   | 45.3 ms                                                     | 50.0 ms: 1.10x slower                                                          |
| pickle_pure_python         | 186 us                                                      | 205 us: 1.10x slower                                                           |
| async_generators           | 223 ms                                                      | 247 ms: 1.11x slower                                                           |
| python_startup_no_site     | 16.9 ms                                                     | 19.0 ms: 1.12x slower                                                          |
| coroutines                 | 12.5 ms                                                     | 14.5 ms: 1.16x slower                                                          |
| deltablue                  | 1.89 ms                                                     | 2.22 ms: 1.18x slower                                                          |
| raytrace                   | 153 ms                                                      | 183 ms: 1.19x slower                                                           |
| django_template            | 20.3 ms                                                     | 24.2 ms: 1.19x slower                                                          |
| many_optionals             | 361 us                                                      | 569 us: 1.58x slower                                                           |
| subparsers                 | 10.9 ms                                                     | 30.3 ms: 2.79x slower                                                          |
| Geometric mean             | (ref)                                                       | 1.08x faster                                                                   |

Benchmark hidden because not significant (3): pylint, crypto_pyaes, pycparser
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250819-3.15.0a0-14080cb-JIT/bm-20250819-pythonperf1-amd64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.082x faster

# HPT report

- Reliability score: 89.29% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown