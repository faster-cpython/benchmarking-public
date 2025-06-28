# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_o2
- machine: windows-amd64
- commit hash: f528bf3
- commit date: 2025-06-28
- overall geometric mean: 1.082x faster
- HPT reliability: 82.66%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 222 ms: 1.03x slower                                               |
| docutils       | 1.53 sec                                                    | 1.66 sec: 1.08x slower                                             |
| sphinx         | 617 ms                                                      | 648 ms: 1.05x slower                                               |
| Geometric mean | (ref)                                                       | 1.04x slower                                                       |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 157 ms: 1.91x faster                                               |
| async_tree_memoization_tg  | 281 ms                                                      | 213 ms: 1.32x faster                                               |
| async_tree_io              | 513 ms                                                      | 397 ms: 1.29x faster                                               |
| async_tree_none            | 219 ms                                                      | 170 ms: 1.29x faster                                               |
| async_tree_io_tg           | 497 ms                                                      | 388 ms: 1.28x faster                                               |
| async_tree_memoization     | 265 ms                                                      | 208 ms: 1.27x faster                                               |
| async_tree_none_tg         | 200 ms                                                      | 168 ms: 1.19x faster                                               |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 334 ms: 1.14x faster                                               |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 344 ms: 1.11x faster                                               |
| async_generators           | 223 ms                                                      | 245 ms: 1.10x slower                                               |
| coroutines                 | 12.5 ms                                                     | 14.1 ms: 1.13x slower                                              |
| Geometric mean             | (ref)                                                       | 1.21x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 55.1 ms: 1.20x faster                                              |
| float          | 50.8 ms                                                     | 45.0 ms: 1.13x faster                                              |
| pidigits       | 146 ms                                                      | 146 ms: 1.00x faster                                               |
| Geometric mean | (ref)                                                       | 1.11x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.3 ms: 1.67x faster                                              |
| regex_effbot   | 1.69 ms                                                     | 1.57 ms: 1.08x faster                                              |
| regex_compile  | 80.7 ms                                                     | 78.5 ms: 1.03x faster                                              |
| regex_dna      | 115 ms                                                      | 121 ms: 1.05x slower                                               |
| Geometric mean | (ref)                                                       | 1.15x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| unpickle_pure_python | 130 us                                                      | 108 us: 1.20x faster                                               |
| tomli_loads          | 1.37 sec                                                    | 1.16 sec: 1.18x faster                                             |
| xml_etree_generate   | 53.5 ms                                                     | 50.4 ms: 1.06x faster                                              |
| json_loads           | 15.1 us                                                     | 14.3 us: 1.05x faster                                              |
| xml_etree_parse      | 92.2 ms                                                     | 88.2 ms: 1.05x faster                                              |
| xml_etree_process    | 36.5 ms                                                     | 36.1 ms: 1.01x faster                                              |
| xml_etree_iterparse  | 60.5 ms                                                     | 64.6 ms: 1.07x slower                                              |
| pickle_pure_python   | 186 us                                                      | 205 us: 1.10x slower                                               |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                       |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.7 ms: 1.06x slower                                              |
| python_startup_no_site | 16.9 ms                                                     | 19.5 ms: 1.15x slower                                              |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.46 ms: 1.20x faster                                              |
| genshi_text     | 15.2 ms                                                     | 15.6 ms: 1.03x slower                                              |
| django_template | 20.3 ms                                                     | 24.2 ms: 1.19x slower                                              |
| Geometric mean  | (ref)                                                       | 1.01x slower                                                       |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 499 us: 16.95x faster                                              |
| pathlib                    | 75.3 ms                                                     | 32.1 ms: 2.34x faster                                              |
| asyncio_websockets         | 300 ms                                                      | 157 ms: 1.91x faster                                               |
| mdp                        | 1.43 sec                                                    | 802 ms: 1.79x faster                                               |
| regex_v8                   | 23.8 ms                                                     | 14.3 ms: 1.67x faster                                              |
| async_tree_memoization_tg  | 281 ms                                                      | 213 ms: 1.32x faster                                               |
| deepcopy                   | 223 us                                                      | 172 us: 1.30x faster                                               |
| async_tree_io              | 513 ms                                                      | 397 ms: 1.29x faster                                               |
| async_tree_none            | 219 ms                                                      | 170 ms: 1.29x faster                                               |
| async_tree_io_tg           | 497 ms                                                      | 388 ms: 1.28x faster                                               |
| deepcopy_memo              | 23.1 us                                                     | 18.1 us: 1.27x faster                                              |
| async_tree_memoization     | 265 ms                                                      | 208 ms: 1.27x faster                                               |
| mako                       | 6.56 ms                                                     | 5.46 ms: 1.20x faster                                              |
| unpickle_pure_python       | 130 us                                                      | 108 us: 1.20x faster                                               |
| nbody                      | 66.3 ms                                                     | 55.1 ms: 1.20x faster                                              |
| async_tree_none_tg         | 200 ms                                                      | 168 ms: 1.19x faster                                               |
| tomli_loads                | 1.37 sec                                                    | 1.16 sec: 1.18x faster                                             |
| fannkuch                   | 252 ms                                                      | 214 ms: 1.18x faster                                               |
| scimark_fft                | 175 ms                                                      | 151 ms: 1.16x faster                                               |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.26 ms: 1.15x faster                                              |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 334 ms: 1.14x faster                                               |
| telco                      | 4.85 ms                                                     | 4.29 ms: 1.13x faster                                              |
| float                      | 50.8 ms                                                     | 45.0 ms: 1.13x faster                                              |
| bpe_tokeniser              | 2.87 sec                                                    | 2.57 sec: 1.12x faster                                             |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 344 ms: 1.11x faster                                               |
| pyflate                    | 283 ms                                                      | 259 ms: 1.09x faster                                               |
| go                         | 84.7 ms                                                     | 77.7 ms: 1.09x faster                                              |
| deepcopy_reduce            | 2.02 us                                                     | 1.86 us: 1.09x faster                                              |
| pprint_safe_repr           | 485 ms                                                      | 447 ms: 1.09x faster                                               |
| regex_effbot               | 1.69 ms                                                     | 1.57 ms: 1.08x faster                                              |
| xml_etree_generate         | 53.5 ms                                                     | 50.4 ms: 1.06x faster                                              |
| pprint_pformat             | 977 ms                                                      | 925 ms: 1.06x faster                                               |
| json_loads                 | 15.1 us                                                     | 14.3 us: 1.05x faster                                              |
| xml_etree_parse            | 92.2 ms                                                     | 88.2 ms: 1.05x faster                                              |
| k_core                     | 1.70 sec                                                    | 1.64 sec: 1.03x faster                                             |
| regex_compile              | 80.7 ms                                                     | 78.5 ms: 1.03x faster                                              |
| sqlite_synth               | 1.59 us                                                     | 1.56 us: 1.01x faster                                              |
| xml_etree_process          | 36.5 ms                                                     | 36.1 ms: 1.01x faster                                              |
| logging_silent             | 54.6 ns                                                     | 54.1 ns: 1.01x faster                                              |
| pidigits                   | 146 ms                                                      | 146 ms: 1.00x faster                                               |
| typing_runtime_protocols   | 103 us                                                      | 104 us: 1.01x slower                                               |
| scimark_monte_carlo        | 40.7 ms                                                     | 41.2 ms: 1.01x slower                                              |
| spectral_norm              | 63.4 ms                                                     | 64.1 ms: 1.01x slower                                              |
| shortest_path              | 355 ms                                                      | 361 ms: 1.02x slower                                               |
| sympy_str                  | 167 ms                                                      | 170 ms: 1.02x slower                                               |
| sympy_expand               | 286 ms                                                      | 292 ms: 1.02x slower                                               |
| genshi_text                | 15.2 ms                                                     | 15.6 ms: 1.03x slower                                              |
| sympy_integrate            | 12.3 ms                                                     | 12.7 ms: 1.03x slower                                              |
| comprehensions             | 10.4 us                                                     | 10.7 us: 1.03x slower                                              |
| 2to3                       | 215 ms                                                      | 222 ms: 1.03x slower                                               |
| connected_components       | 320 ms                                                      | 330 ms: 1.03x slower                                               |
| sympy_sum                  | 85.2 ms                                                     | 87.9 ms: 1.03x slower                                              |
| generators                 | 19.0 ms                                                     | 19.6 ms: 1.03x slower                                              |
| dulwich_log                | 40.1 ms                                                     | 41.5 ms: 1.03x slower                                              |
| scimark_sor                | 76.2 ms                                                     | 79.9 ms: 1.05x slower                                              |
| sphinx                     | 617 ms                                                      | 648 ms: 1.05x slower                                               |
| richards                   | 26.3 ms                                                     | 27.6 ms: 1.05x slower                                              |
| regex_dna                  | 115 ms                                                      | 121 ms: 1.05x slower                                               |
| python_startup             | 24.4 ms                                                     | 25.7 ms: 1.06x slower                                              |
| logging_simple             | 5.77 us                                                     | 6.11 us: 1.06x slower                                              |
| nqueens                    | 56.1 ms                                                     | 59.5 ms: 1.06x slower                                              |
| logging_format             | 6.18 us                                                     | 6.57 us: 1.06x slower                                              |
| richards_super             | 29.8 ms                                                     | 31.7 ms: 1.07x slower                                              |
| scimark_lu                 | 56.7 ms                                                     | 60.4 ms: 1.07x slower                                              |
| xml_etree_iterparse        | 60.5 ms                                                     | 64.6 ms: 1.07x slower                                              |
| create_gc_cycles           | 1.22 ms                                                     | 1.32 ms: 1.08x slower                                              |
| chaos                      | 37.9 ms                                                     | 41.0 ms: 1.08x slower                                              |
| docutils                   | 1.53 sec                                                    | 1.66 sec: 1.08x slower                                             |
| gc_traversal               | 1.96 ms                                                     | 2.14 ms: 1.09x slower                                              |
| hexiom                     | 3.84 ms                                                     | 4.19 ms: 1.09x slower                                              |
| async_generators           | 223 ms                                                      | 245 ms: 1.10x slower                                               |
| pickle_pure_python         | 186 us                                                      | 205 us: 1.10x slower                                               |
| coverage                   | 45.3 ms                                                     | 50.1 ms: 1.11x slower                                              |
| coroutines                 | 12.5 ms                                                     | 14.1 ms: 1.13x slower                                              |
| python_startup_no_site     | 16.9 ms                                                     | 19.5 ms: 1.15x slower                                              |
| deltablue                  | 1.89 ms                                                     | 2.19 ms: 1.16x slower                                              |
| raytrace                   | 153 ms                                                      | 181 ms: 1.18x slower                                               |
| django_template            | 20.3 ms                                                     | 24.2 ms: 1.19x slower                                              |
| many_optionals             | 361 us                                                      | 449 us: 1.24x slower                                               |
| subparsers                 | 10.9 ms                                                     | 17.0 ms: 1.57x slower                                              |
| Geometric mean             | (ref)                                                       | 1.08x faster                                                       |

Benchmark hidden because not significant (8): pylint, json, meteor_contest, pycparser, crypto_pyaes, json_dumps, html5lib, genshi_xml
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250628-3.15.0a0-f528bf3-JIT/bm-20250628-pythonperf1-amd64-brandtbucher-jit_o2-3.15.0a0-f528bf3.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.082x faster

# HPT report

- Reliability score: 82.66% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown