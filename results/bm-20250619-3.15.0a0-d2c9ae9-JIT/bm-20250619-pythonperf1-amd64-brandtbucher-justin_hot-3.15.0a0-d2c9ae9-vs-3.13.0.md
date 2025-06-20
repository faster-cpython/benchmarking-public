# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_hot
- machine: windows-amd64
- commit hash: d2c9ae9
- commit date: 2025-06-19
- overall geometric mean: 1.074x faster
- HPT reliability: 58.10%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 221 ms: 1.03x slower                                                   |
| docutils       | 1.53 sec                                                    | 1.66 sec: 1.08x slower                                                 |
| sphinx         | 617 ms                                                      | 644 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                       | 1.04x slower                                                           |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 160 ms: 1.87x faster                                                   |
| async_tree_memoization_tg  | 281 ms                                                      | 210 ms: 1.34x faster                                                   |
| async_tree_io              | 513 ms                                                      | 398 ms: 1.29x faster                                                   |
| async_tree_none            | 219 ms                                                      | 171 ms: 1.28x faster                                                   |
| async_tree_memoization     | 265 ms                                                      | 207 ms: 1.28x faster                                                   |
| async_tree_io_tg           | 497 ms                                                      | 390 ms: 1.27x faster                                                   |
| async_tree_none_tg         | 200 ms                                                      | 169 ms: 1.18x faster                                                   |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 333 ms: 1.14x faster                                                   |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 342 ms: 1.12x faster                                                   |
| async_generators           | 223 ms                                                      | 243 ms: 1.09x slower                                                   |
| coroutines                 | 12.5 ms                                                     | 14.3 ms: 1.15x slower                                                  |
| Geometric mean             | (ref)                                                       | 1.21x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 44.0 ms: 1.15x faster                                                  |
| nbody          | 66.3 ms                                                     | 62.4 ms: 1.06x faster                                                  |
| pidigits       | 146 ms                                                      | 149 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                       | 1.06x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.4 ms: 1.65x faster                                                  |
| regex_effbot   | 1.69 ms                                                     | 1.63 ms: 1.04x faster                                                  |
| regex_compile  | 80.7 ms                                                     | 78.9 ms: 1.02x faster                                                  |
| regex_dna      | 115 ms                                                      | 120 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                       | 1.14x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.16 sec: 1.19x faster                                                 |
| unpickle_pure_python | 130 us                                                      | 114 us: 1.14x faster                                                   |
| xml_etree_generate   | 53.5 ms                                                     | 50.7 ms: 1.05x faster                                                  |
| xml_etree_parse      | 92.2 ms                                                     | 88.1 ms: 1.05x faster                                                  |
| json_loads           | 15.1 us                                                     | 14.6 us: 1.04x faster                                                  |
| xml_etree_iterparse  | 60.5 ms                                                     | 62.8 ms: 1.04x slower                                                  |
| json_dumps           | 6.19 ms                                                     | 6.47 ms: 1.04x slower                                                  |
| pickle_pure_python   | 186 us                                                      | 205 us: 1.10x slower                                                   |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                           |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.8 ms: 1.06x slower                                                  |
| python_startup_no_site | 16.9 ms                                                     | 19.3 ms: 1.14x slower                                                  |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.47 ms: 1.20x faster                                                  |
| genshi_text     | 15.2 ms                                                     | 15.7 ms: 1.03x slower                                                  |
| genshi_xml      | 33.9 ms                                                     | 35.1 ms: 1.04x slower                                                  |
| django_template | 20.3 ms                                                     | 24.0 ms: 1.18x slower                                                  |
| Geometric mean  | (ref)                                                       | 1.01x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 492 us: 17.21x faster                                                  |
| pathlib                    | 75.3 ms                                                     | 31.8 ms: 2.37x faster                                                  |
| asyncio_websockets         | 300 ms                                                      | 160 ms: 1.87x faster                                                   |
| mdp                        | 1.43 sec                                                    | 795 ms: 1.80x faster                                                   |
| regex_v8                   | 23.8 ms                                                     | 14.4 ms: 1.65x faster                                                  |
| async_tree_memoization_tg  | 281 ms                                                      | 210 ms: 1.34x faster                                                   |
| deepcopy                   | 223 us                                                      | 169 us: 1.32x faster                                                   |
| async_tree_io              | 513 ms                                                      | 398 ms: 1.29x faster                                                   |
| async_tree_none            | 219 ms                                                      | 171 ms: 1.28x faster                                                   |
| async_tree_memoization     | 265 ms                                                      | 207 ms: 1.28x faster                                                   |
| async_tree_io_tg           | 497 ms                                                      | 390 ms: 1.27x faster                                                   |
| deepcopy_memo              | 23.1 us                                                     | 18.2 us: 1.27x faster                                                  |
| mako                       | 6.56 ms                                                     | 5.47 ms: 1.20x faster                                                  |
| tomli_loads                | 1.37 sec                                                    | 1.16 sec: 1.19x faster                                                 |
| async_tree_none_tg         | 200 ms                                                      | 169 ms: 1.18x faster                                                   |
| float                      | 50.8 ms                                                     | 44.0 ms: 1.15x faster                                                  |
| unpickle_pure_python       | 130 us                                                      | 114 us: 1.14x faster                                                   |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 333 ms: 1.14x faster                                                   |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.29 ms: 1.14x faster                                                  |
| deepcopy_reduce            | 2.02 us                                                     | 1.79 us: 1.13x faster                                                  |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 342 ms: 1.12x faster                                                   |
| telco                      | 4.85 ms                                                     | 4.41 ms: 1.10x faster                                                  |
| go                         | 84.7 ms                                                     | 77.5 ms: 1.09x faster                                                  |
| bpe_tokeniser              | 2.87 sec                                                    | 2.63 sec: 1.09x faster                                                 |
| scimark_fft                | 175 ms                                                      | 161 ms: 1.09x faster                                                   |
| fannkuch                   | 252 ms                                                      | 232 ms: 1.08x faster                                                   |
| json                       | 3.30 ms                                                     | 3.07 ms: 1.08x faster                                                  |
| pyflate                    | 283 ms                                                      | 263 ms: 1.07x faster                                                   |
| nbody                      | 66.3 ms                                                     | 62.4 ms: 1.06x faster                                                  |
| xml_etree_generate         | 53.5 ms                                                     | 50.7 ms: 1.05x faster                                                  |
| xml_etree_parse            | 92.2 ms                                                     | 88.1 ms: 1.05x faster                                                  |
| regex_effbot               | 1.69 ms                                                     | 1.63 ms: 1.04x faster                                                  |
| json_loads                 | 15.1 us                                                     | 14.6 us: 1.04x faster                                                  |
| k_core                     | 1.70 sec                                                    | 1.64 sec: 1.03x faster                                                 |
| spectral_norm              | 63.4 ms                                                     | 61.7 ms: 1.03x faster                                                  |
| regex_compile              | 80.7 ms                                                     | 78.9 ms: 1.02x faster                                                  |
| sqlite_synth               | 1.59 us                                                     | 1.56 us: 1.02x faster                                                  |
| scimark_monte_carlo        | 40.7 ms                                                     | 40.2 ms: 1.01x faster                                                  |
| scimark_sor                | 76.2 ms                                                     | 77.0 ms: 1.01x slower                                                  |
| shortest_path              | 355 ms                                                      | 359 ms: 1.01x slower                                                   |
| pidigits                   | 146 ms                                                      | 149 ms: 1.02x slower                                                   |
| crypto_pyaes               | 45.6 ms                                                     | 46.5 ms: 1.02x slower                                                  |
| connected_components       | 320 ms                                                      | 328 ms: 1.03x slower                                                   |
| sympy_sum                  | 85.2 ms                                                     | 87.5 ms: 1.03x slower                                                  |
| 2to3                       | 215 ms                                                      | 221 ms: 1.03x slower                                                   |
| genshi_text                | 15.2 ms                                                     | 15.7 ms: 1.03x slower                                                  |
| generators                 | 19.0 ms                                                     | 19.6 ms: 1.03x slower                                                  |
| sympy_str                  | 167 ms                                                      | 172 ms: 1.03x slower                                                   |
| richards_super             | 29.8 ms                                                     | 30.7 ms: 1.03x slower                                                  |
| dulwich_log                | 40.1 ms                                                     | 41.5 ms: 1.03x slower                                                  |
| richards                   | 26.3 ms                                                     | 27.2 ms: 1.03x slower                                                  |
| genshi_xml                 | 33.9 ms                                                     | 35.1 ms: 1.04x slower                                                  |
| xml_etree_iterparse        | 60.5 ms                                                     | 62.8 ms: 1.04x slower                                                  |
| sympy_expand               | 286 ms                                                      | 297 ms: 1.04x slower                                                   |
| scimark_lu                 | 56.7 ms                                                     | 58.9 ms: 1.04x slower                                                  |
| sympy_integrate            | 12.3 ms                                                     | 12.8 ms: 1.04x slower                                                  |
| nqueens                    | 56.1 ms                                                     | 58.4 ms: 1.04x slower                                                  |
| comprehensions             | 10.4 us                                                     | 10.8 us: 1.04x slower                                                  |
| sphinx                     | 617 ms                                                      | 644 ms: 1.04x slower                                                   |
| regex_dna                  | 115 ms                                                      | 120 ms: 1.04x slower                                                   |
| json_dumps                 | 6.19 ms                                                     | 6.47 ms: 1.04x slower                                                  |
| pprint_safe_repr           | 485 ms                                                      | 507 ms: 1.05x slower                                                   |
| python_startup             | 24.4 ms                                                     | 25.8 ms: 1.06x slower                                                  |
| pprint_pformat             | 977 ms                                                      | 1.03 sec: 1.06x slower                                                 |
| chaos                      | 37.9 ms                                                     | 40.4 ms: 1.07x slower                                                  |
| hexiom                     | 3.84 ms                                                     | 4.12 ms: 1.07x slower                                                  |
| create_gc_cycles           | 1.22 ms                                                     | 1.32 ms: 1.08x slower                                                  |
| logging_format             | 6.18 us                                                     | 6.64 us: 1.08x slower                                                  |
| docutils                   | 1.53 sec                                                    | 1.66 sec: 1.08x slower                                                 |
| logging_simple             | 5.77 us                                                     | 6.27 us: 1.09x slower                                                  |
| async_generators           | 223 ms                                                      | 243 ms: 1.09x slower                                                   |
| pickle_pure_python         | 186 us                                                      | 205 us: 1.10x slower                                                   |
| gc_traversal               | 1.96 ms                                                     | 2.17 ms: 1.10x slower                                                  |
| coverage                   | 45.3 ms                                                     | 50.2 ms: 1.11x slower                                                  |
| python_startup_no_site     | 16.9 ms                                                     | 19.3 ms: 1.14x slower                                                  |
| coroutines                 | 12.5 ms                                                     | 14.3 ms: 1.15x slower                                                  |
| django_template            | 20.3 ms                                                     | 24.0 ms: 1.18x slower                                                  |
| deltablue                  | 1.89 ms                                                     | 2.24 ms: 1.19x slower                                                  |
| raytrace                   | 153 ms                                                      | 182 ms: 1.19x slower                                                   |
| many_optionals             | 361 us                                                      | 448 us: 1.24x slower                                                   |
| subparsers                 | 10.9 ms                                                     | 17.1 ms: 1.57x slower                                                  |
| logging_silent             | 54.6 ns                                                     | 314 ns: 5.75x slower                                                   |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                           |

Benchmark hidden because not significant (6): pylint, meteor_contest, xml_etree_process, typing_runtime_protocols, html5lib, pycparser
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250619-3.15.0a0-d2c9ae9-JIT/bm-20250619-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.074x faster

# HPT report

- Reliability score: 58.10% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown