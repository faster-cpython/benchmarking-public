# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_oz
- machine: windows-amd64
- commit hash: 6448067
- commit date: 2025-06-28
- overall geometric mean: 1.083x faster
- HPT reliability: 81.42%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 218 ms: 1.01x slower                                               |
| docutils       | 1.53 sec                                                    | 1.64 sec: 1.07x slower                                             |
| sphinx         | 617 ms                                                      | 639 ms: 1.03x slower                                               |
| Geometric mean | (ref)                                                       | 1.03x slower                                                       |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 156 ms: 1.93x faster                                               |
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                               |
| async_tree_io              | 513 ms                                                      | 391 ms: 1.31x faster                                               |
| async_tree_none            | 219 ms                                                      | 170 ms: 1.29x faster                                               |
| async_tree_memoization     | 265 ms                                                      | 207 ms: 1.28x faster                                               |
| async_tree_io_tg           | 497 ms                                                      | 392 ms: 1.27x faster                                               |
| async_tree_none_tg         | 200 ms                                                      | 169 ms: 1.18x faster                                               |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 332 ms: 1.15x faster                                               |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 342 ms: 1.12x faster                                               |
| async_generators           | 223 ms                                                      | 248 ms: 1.11x slower                                               |
| coroutines                 | 12.5 ms                                                     | 14.5 ms: 1.16x slower                                              |
| Geometric mean             | (ref)                                                       | 1.21x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 56.2 ms: 1.18x faster                                              |
| float          | 50.8 ms                                                     | 44.9 ms: 1.13x faster                                              |
| Geometric mean | (ref)                                                       | 1.10x faster                                                       |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.4 ms: 1.78x faster                                              |
| regex_effbot   | 1.69 ms                                                     | 1.54 ms: 1.10x faster                                              |
| regex_compile  | 80.7 ms                                                     | 78.5 ms: 1.03x faster                                              |
| regex_dna      | 115 ms                                                      | 117 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                       | 1.19x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| unpickle_pure_python | 130 us                                                      | 110 us: 1.18x faster                                               |
| tomli_loads          | 1.37 sec                                                    | 1.24 sec: 1.11x faster                                             |
| xml_etree_parse      | 92.2 ms                                                     | 86.5 ms: 1.07x faster                                              |
| xml_etree_generate   | 53.5 ms                                                     | 50.3 ms: 1.06x faster                                              |
| xml_etree_process    | 36.5 ms                                                     | 35.5 ms: 1.03x faster                                              |
| json_loads           | 15.1 us                                                     | 14.7 us: 1.03x faster                                              |
| xml_etree_iterparse  | 60.5 ms                                                     | 62.3 ms: 1.03x slower                                              |
| pickle_pure_python   | 186 us                                                      | 207 us: 1.11x slower                                               |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                       |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.0 ms: 1.06x slower                                              |
| python_startup_no_site | 16.9 ms                                                     | 19.1 ms: 1.13x slower                                              |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.57 ms: 1.18x faster                                              |
| genshi_text     | 15.2 ms                                                     | 15.5 ms: 1.02x slower                                              |
| django_template | 20.3 ms                                                     | 24.4 ms: 1.20x slower                                              |
| Geometric mean  | (ref)                                                       | 1.01x slower                                                       |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 496 us: 17.07x faster                                              |
| pathlib                    | 75.3 ms                                                     | 28.7 ms: 2.63x faster                                              |
| asyncio_websockets         | 300 ms                                                      | 156 ms: 1.93x faster                                               |
| mdp                        | 1.43 sec                                                    | 795 ms: 1.80x faster                                               |
| regex_v8                   | 23.8 ms                                                     | 13.4 ms: 1.78x faster                                              |
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                               |
| deepcopy_memo              | 23.1 us                                                     | 17.6 us: 1.31x faster                                              |
| deepcopy                   | 223 us                                                      | 170 us: 1.31x faster                                               |
| async_tree_io              | 513 ms                                                      | 391 ms: 1.31x faster                                               |
| async_tree_none            | 219 ms                                                      | 170 ms: 1.29x faster                                               |
| async_tree_memoization     | 265 ms                                                      | 207 ms: 1.28x faster                                               |
| async_tree_io_tg           | 497 ms                                                      | 392 ms: 1.27x faster                                               |
| async_tree_none_tg         | 200 ms                                                      | 169 ms: 1.18x faster                                               |
| unpickle_pure_python       | 130 us                                                      | 110 us: 1.18x faster                                               |
| nbody                      | 66.3 ms                                                     | 56.2 ms: 1.18x faster                                              |
| mako                       | 6.56 ms                                                     | 5.57 ms: 1.18x faster                                              |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.23 ms: 1.17x faster                                              |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 332 ms: 1.15x faster                                               |
| float                      | 50.8 ms                                                     | 44.9 ms: 1.13x faster                                              |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 342 ms: 1.12x faster                                               |
| telco                      | 4.85 ms                                                     | 4.36 ms: 1.11x faster                                              |
| tomli_loads                | 1.37 sec                                                    | 1.24 sec: 1.11x faster                                             |
| regex_effbot               | 1.69 ms                                                     | 1.54 ms: 1.10x faster                                              |
| deepcopy_reduce            | 2.02 us                                                     | 1.84 us: 1.10x faster                                              |
| pyflate                    | 283 ms                                                      | 258 ms: 1.10x faster                                               |
| go                         | 84.7 ms                                                     | 77.8 ms: 1.09x faster                                              |
| scimark_fft                | 175 ms                                                      | 161 ms: 1.08x faster                                               |
| xml_etree_parse            | 92.2 ms                                                     | 86.5 ms: 1.07x faster                                              |
| xml_etree_generate         | 53.5 ms                                                     | 50.3 ms: 1.06x faster                                              |
| bpe_tokeniser              | 2.87 sec                                                    | 2.71 sec: 1.06x faster                                             |
| pprint_safe_repr           | 485 ms                                                      | 460 ms: 1.05x faster                                               |
| k_core                     | 1.70 sec                                                    | 1.61 sec: 1.05x faster                                             |
| fannkuch                   | 252 ms                                                      | 242 ms: 1.04x faster                                               |
| pprint_pformat             | 977 ms                                                      | 941 ms: 1.04x faster                                               |
| xml_etree_process          | 36.5 ms                                                     | 35.5 ms: 1.03x faster                                              |
| regex_compile              | 80.7 ms                                                     | 78.5 ms: 1.03x faster                                              |
| json_loads                 | 15.1 us                                                     | 14.7 us: 1.03x faster                                              |
| sqlite_synth               | 1.59 us                                                     | 1.56 us: 1.02x faster                                              |
| meteor_contest             | 72.0 ms                                                     | 71.0 ms: 1.01x faster                                              |
| dulwich_log                | 40.1 ms                                                     | 40.3 ms: 1.01x slower                                              |
| connected_components       | 320 ms                                                      | 323 ms: 1.01x slower                                               |
| 2to3                       | 215 ms                                                      | 218 ms: 1.01x slower                                               |
| regex_dna                  | 115 ms                                                      | 117 ms: 1.01x slower                                               |
| sympy_str                  | 167 ms                                                      | 169 ms: 1.02x slower                                               |
| typing_runtime_protocols   | 103 us                                                      | 105 us: 1.02x slower                                               |
| spectral_norm              | 63.4 ms                                                     | 64.5 ms: 1.02x slower                                              |
| genshi_text                | 15.2 ms                                                     | 15.5 ms: 1.02x slower                                              |
| sympy_sum                  | 85.2 ms                                                     | 86.9 ms: 1.02x slower                                              |
| sympy_expand               | 286 ms                                                      | 292 ms: 1.02x slower                                               |
| scimark_monte_carlo        | 40.7 ms                                                     | 41.7 ms: 1.02x slower                                              |
| sympy_integrate            | 12.3 ms                                                     | 12.6 ms: 1.03x slower                                              |
| crypto_pyaes               | 45.6 ms                                                     | 46.7 ms: 1.03x slower                                              |
| richards                   | 26.3 ms                                                     | 27.0 ms: 1.03x slower                                              |
| generators                 | 19.0 ms                                                     | 19.5 ms: 1.03x slower                                              |
| xml_etree_iterparse        | 60.5 ms                                                     | 62.3 ms: 1.03x slower                                              |
| richards_super             | 29.8 ms                                                     | 30.7 ms: 1.03x slower                                              |
| scimark_lu                 | 56.7 ms                                                     | 58.6 ms: 1.03x slower                                              |
| sphinx                     | 617 ms                                                      | 639 ms: 1.03x slower                                               |
| scimark_sor                | 76.2 ms                                                     | 79.2 ms: 1.04x slower                                              |
| create_gc_cycles           | 1.22 ms                                                     | 1.30 ms: 1.06x slower                                              |
| gc_traversal               | 1.96 ms                                                     | 2.09 ms: 1.06x slower                                              |
| comprehensions             | 10.4 us                                                     | 11.0 us: 1.06x slower                                              |
| python_startup             | 24.4 ms                                                     | 26.0 ms: 1.06x slower                                              |
| docutils                   | 1.53 sec                                                    | 1.64 sec: 1.07x slower                                             |
| logging_simple             | 5.77 us                                                     | 6.23 us: 1.08x slower                                              |
| nqueens                    | 56.1 ms                                                     | 60.8 ms: 1.08x slower                                              |
| hexiom                     | 3.84 ms                                                     | 4.17 ms: 1.09x slower                                              |
| logging_format             | 6.18 us                                                     | 6.71 us: 1.09x slower                                              |
| chaos                      | 37.9 ms                                                     | 41.2 ms: 1.09x slower                                              |
| coverage                   | 45.3 ms                                                     | 49.7 ms: 1.10x slower                                              |
| pickle_pure_python         | 186 us                                                      | 207 us: 1.11x slower                                               |
| async_generators           | 223 ms                                                      | 248 ms: 1.11x slower                                               |
| python_startup_no_site     | 16.9 ms                                                     | 19.1 ms: 1.13x slower                                              |
| coroutines                 | 12.5 ms                                                     | 14.5 ms: 1.16x slower                                              |
| raytrace                   | 153 ms                                                      | 178 ms: 1.16x slower                                               |
| deltablue                  | 1.89 ms                                                     | 2.21 ms: 1.17x slower                                              |
| django_template            | 20.3 ms                                                     | 24.4 ms: 1.20x slower                                              |
| many_optionals             | 361 us                                                      | 447 us: 1.24x slower                                               |
| subparsers                 | 10.9 ms                                                     | 17.0 ms: 1.57x slower                                              |
| Geometric mean             | (ref)                                                       | 1.08x faster                                                       |

Benchmark hidden because not significant (9): pylint, json, html5lib, pycparser, json_dumps, shortest_path, pidigits, logging_silent, genshi_xml
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250628-3.15.0a0-6448067-JIT/bm-20250628-pythonperf1-amd64-brandtbucher-jit_oz-3.15.0a0-6448067.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.083x faster

# HPT report

- Reliability score: 81.42% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown