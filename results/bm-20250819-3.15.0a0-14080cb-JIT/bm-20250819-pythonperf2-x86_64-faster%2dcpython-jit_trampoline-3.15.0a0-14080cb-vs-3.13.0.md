# Results vs. 3.13.0

- fork: faster-cpython
- ref: jit_trampoline
- machine: linux-x86_64
- commit hash: 14080cb
- commit date: 2025-08-19
- overall geometric mean: 1.044x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250819-pythonperf2-x86_64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 286 ms: 1.02x faster                                                            |
| docutils       | 2.83 sec                                                     | 2.91 sec: 1.03x slower                                                          |
| html5lib       | 73.5 ms                                                      | 68.1 ms: 1.08x faster                                                           |
| sphinx         | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                          |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250819-pythonperf2-x86_64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 332 ms: 1.40x faster                                                            |
| async_tree_none            | 376 ms                                                       | 270 ms: 1.39x faster                                                            |
| async_tree_memoization     | 453 ms                                                       | 327 ms: 1.39x faster                                                            |
| async_tree_io              | 843 ms                                                       | 617 ms: 1.37x faster                                                            |
| async_tree_io_tg           | 831 ms                                                       | 628 ms: 1.32x faster                                                            |
| async_tree_none_tg         | 346 ms                                                       | 272 ms: 1.27x faster                                                            |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 499 ms: 1.21x faster                                                            |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 511 ms: 1.14x faster                                                            |
| async_generators           | 457 ms                                                       | 443 ms: 1.03x faster                                                            |
| asyncio_websockets         | 388 ms                                                       | 384 ms: 1.01x faster                                                            |
| coroutines                 | 21.6 ms                                                      | 22.4 ms: 1.04x slower                                                           |
| Geometric mean             | (ref)                                                        | 1.22x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250819-pythonperf2-x86_64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 64.0 ms: 1.27x faster                                                           |
| pidigits       | 252 ms                                                       | 255 ms: 1.01x slower                                                            |
| nbody          | 89.3 ms                                                      | 106 ms: 1.18x slower                                                            |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250819-pythonperf2-x86_64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 26.1 ms                                                      | 23.3 ms: 1.12x faster                                                           |
| regex_dna      | 247 ms                                                       | 228 ms: 1.08x faster                                                            |
| regex_compile  | 143 ms                                                       | 133 ms: 1.07x faster                                                            |
| regex_effbot   | 3.67 ms                                                      | 3.58 ms: 1.03x faster                                                           |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250819-pythonperf2-x86_64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 1.92 sec: 1.28x faster                                                          |
| unpickle_pure_python | 217 us                                                       | 191 us: 1.14x faster                                                            |
| xml_etree_process    | 61.2 ms                                                      | 55.0 ms: 1.11x faster                                                           |
| json_dumps           | 11.1 ms                                                      | 10.0 ms: 1.11x faster                                                           |
| xml_etree_generate   | 86.5 ms                                                      | 78.4 ms: 1.10x faster                                                           |
| xml_etree_parse      | 150 ms                                                       | 143 ms: 1.05x faster                                                            |
| xml_etree_iterparse  | 103 ms                                                       | 98.0 ms: 1.05x faster                                                           |
| pickle_pure_python   | 323 us                                                       | 328 us: 1.02x slower                                                            |
| json_loads           | 24.7 us                                                      | 25.1 us: 1.02x slower                                                           |
| Geometric mean       | (ref)                                                        | 1.09x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250819-pythonperf2-x86_64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 15.4 ms: 1.03x faster                                                           |
| python_startup_no_site | 8.96 ms                                                      | 8.83 ms: 1.01x faster                                                           |
| Geometric mean         | (ref)                                                        | 1.02x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250819-pythonperf2-x86_64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 23.4 ms: 1.12x faster                                                           |
| mako            | 10.4 ms                                                      | 9.79 ms: 1.06x faster                                                           |
| django_template | 36.4 ms                                                      | 35.0 ms: 1.04x faster                                                           |
| genshi_xml      | 57.1 ms                                                      | 56.6 ms: 1.01x faster                                                           |
| Geometric mean  | (ref)                                                        | 1.06x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250819-pythonperf2-x86_64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.30 sec: 1.95x faster                                                          |
| richards                   | 52.9 ms                                                      | 34.2 ms: 1.55x faster                                                           |
| richards_super             | 59.6 ms                                                      | 39.3 ms: 1.52x faster                                                           |
| async_tree_memoization_tg  | 466 ms                                                       | 332 ms: 1.40x faster                                                            |
| deepcopy                   | 392 us                                                       | 280 us: 1.40x faster                                                            |
| async_tree_none            | 376 ms                                                       | 270 ms: 1.39x faster                                                            |
| async_tree_memoization     | 453 ms                                                       | 327 ms: 1.39x faster                                                            |
| deepcopy_memo              | 38.6 us                                                      | 27.9 us: 1.38x faster                                                           |
| async_tree_io              | 843 ms                                                       | 617 ms: 1.37x faster                                                            |
| async_tree_io_tg           | 831 ms                                                       | 628 ms: 1.32x faster                                                            |
| go                         | 162 ms                                                       | 124 ms: 1.31x faster                                                            |
| tomli_loads                | 2.46 sec                                                     | 1.92 sec: 1.28x faster                                                          |
| async_tree_none_tg         | 346 ms                                                       | 272 ms: 1.27x faster                                                            |
| float                      | 81.3 ms                                                      | 64.0 ms: 1.27x faster                                                           |
| spectral_norm              | 97.0 ms                                                      | 77.6 ms: 1.25x faster                                                           |
| scimark_sor                | 123 ms                                                       | 101 ms: 1.22x faster                                                            |
| pyflate                    | 503 ms                                                       | 414 ms: 1.22x faster                                                            |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 499 ms: 1.21x faster                                                            |
| deltablue                  | 3.42 ms                                                      | 2.86 ms: 1.19x faster                                                           |
| deepcopy_reduce            | 3.54 us                                                      | 3.03 us: 1.17x faster                                                           |
| pprint_pformat             | 1.72 sec                                                     | 1.48 sec: 1.16x faster                                                          |
| dulwich_log                | 68.2 ms                                                      | 59.2 ms: 1.15x faster                                                           |
| pprint_safe_repr           | 843 ms                                                       | 737 ms: 1.14x faster                                                            |
| unpickle_pure_python       | 217 us                                                       | 191 us: 1.14x faster                                                            |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 511 ms: 1.14x faster                                                            |
| bpe_tokeniser              | 5.09 sec                                                     | 4.51 sec: 1.13x faster                                                          |
| regex_v8                   | 26.1 ms                                                      | 23.3 ms: 1.12x faster                                                           |
| genshi_text                | 26.2 ms                                                      | 23.4 ms: 1.12x faster                                                           |
| xml_etree_process          | 61.2 ms                                                      | 55.0 ms: 1.11x faster                                                           |
| generators                 | 33.6 ms                                                      | 30.3 ms: 1.11x faster                                                           |
| json_dumps                 | 11.1 ms                                                      | 10.0 ms: 1.11x faster                                                           |
| xml_etree_generate         | 86.5 ms                                                      | 78.4 ms: 1.10x faster                                                           |
| scimark_fft                | 328 ms                                                       | 299 ms: 1.10x faster                                                            |
| regex_dna                  | 247 ms                                                       | 228 ms: 1.08x faster                                                            |
| hexiom                     | 6.55 ms                                                      | 6.06 ms: 1.08x faster                                                           |
| logging_simple             | 6.39 us                                                      | 5.92 us: 1.08x faster                                                           |
| html5lib                   | 73.5 ms                                                      | 68.1 ms: 1.08x faster                                                           |
| meteor_contest             | 130 ms                                                       | 120 ms: 1.08x faster                                                            |
| k_core                     | 2.17 sec                                                     | 2.02 sec: 1.08x faster                                                          |
| thrift                     | 901 us                                                       | 842 us: 1.07x faster                                                            |
| regex_compile              | 143 ms                                                       | 133 ms: 1.07x faster                                                            |
| logging_silent             | 97.9 ns                                                      | 91.8 ns: 1.07x faster                                                           |
| pylint                     | 347 ms                                                       | 326 ms: 1.06x faster                                                            |
| logging_format             | 6.94 us                                                      | 6.52 us: 1.06x faster                                                           |
| scimark_monte_carlo        | 66.1 ms                                                      | 62.2 ms: 1.06x faster                                                           |
| connected_components       | 432 ms                                                       | 407 ms: 1.06x faster                                                            |
| mako                       | 10.4 ms                                                      | 9.79 ms: 1.06x faster                                                           |
| xml_etree_parse            | 150 ms                                                       | 143 ms: 1.05x faster                                                            |
| sympy_integrate            | 23.6 ms                                                      | 22.4 ms: 1.05x faster                                                           |
| xml_etree_iterparse        | 103 ms                                                       | 98.0 ms: 1.05x faster                                                           |
| pathlib                    | 17.5 ms                                                      | 16.8 ms: 1.04x faster                                                           |
| shortest_path              | 460 ms                                                       | 441 ms: 1.04x faster                                                            |
| json                       | 5.69 ms                                                      | 5.47 ms: 1.04x faster                                                           |
| django_template            | 36.4 ms                                                      | 35.0 ms: 1.04x faster                                                           |
| python_startup             | 15.9 ms                                                      | 15.4 ms: 1.03x faster                                                           |
| async_generators           | 457 ms                                                       | 443 ms: 1.03x faster                                                            |
| sqlite_synth               | 2.91 us                                                      | 2.82 us: 1.03x faster                                                           |
| sphinx                     | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                          |
| regex_effbot               | 3.67 ms                                                      | 3.58 ms: 1.03x faster                                                           |
| 2to3                       | 293 ms                                                       | 286 ms: 1.02x faster                                                            |
| sympy_sum                  | 155 ms                                                       | 152 ms: 1.02x faster                                                            |
| sympy_str                  | 298 ms                                                       | 292 ms: 1.02x faster                                                            |
| chaos                      | 60.2 ms                                                      | 59.1 ms: 1.02x faster                                                           |
| sympy_expand               | 509 ms                                                       | 502 ms: 1.01x faster                                                            |
| python_startup_no_site     | 8.96 ms                                                      | 8.83 ms: 1.01x faster                                                           |
| asyncio_websockets         | 388 ms                                                       | 384 ms: 1.01x faster                                                            |
| genshi_xml                 | 57.1 ms                                                      | 56.6 ms: 1.01x faster                                                           |
| comprehensions             | 17.0 us                                                      | 17.1 us: 1.00x slower                                                           |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.79 ms: 1.00x slower                                                           |
| typing_runtime_protocols   | 169 us                                                       | 170 us: 1.01x slower                                                            |
| pidigits                   | 252 ms                                                       | 255 ms: 1.01x slower                                                            |
| fannkuch                   | 363 ms                                                       | 367 ms: 1.01x slower                                                            |
| nqueens                    | 90.7 ms                                                      | 91.8 ms: 1.01x slower                                                           |
| pickle_pure_python         | 323 us                                                       | 328 us: 1.02x slower                                                            |
| json_loads                 | 24.7 us                                                      | 25.1 us: 1.02x slower                                                           |
| docutils                   | 2.83 sec                                                     | 2.91 sec: 1.03x slower                                                          |
| raytrace                   | 273 ms                                                       | 281 ms: 1.03x slower                                                            |
| coroutines                 | 21.6 ms                                                      | 22.4 ms: 1.04x slower                                                           |
| crypto_pyaes               | 73.3 ms                                                      | 77.0 ms: 1.05x slower                                                           |
| coverage                   | 80.0 ms                                                      | 86.3 ms: 1.08x slower                                                           |
| create_gc_cycles           | 2.68 ms                                                      | 2.92 ms: 1.09x slower                                                           |
| nbody                      | 89.3 ms                                                      | 106 ms: 1.18x slower                                                            |
| many_optionals             | 930 us                                                       | 1.23 ms: 1.32x slower                                                           |
| gc_traversal               | 4.74 ms                                                      | 6.65 ms: 1.40x slower                                                           |
| subparsers                 | 17.5 ms                                                      | 42.5 ms: 2.43x slower                                                           |
| telco                      | 8.79 ms                                                      | 160 ms: 18.24x slower                                                           |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                                    |

Benchmark hidden because not significant (3): scimark_lu, djangocms, pycparser
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250819-3.15.0a0-14080cb-JIT/bm-20250819-pythonperf2-x86_64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.044x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.12x