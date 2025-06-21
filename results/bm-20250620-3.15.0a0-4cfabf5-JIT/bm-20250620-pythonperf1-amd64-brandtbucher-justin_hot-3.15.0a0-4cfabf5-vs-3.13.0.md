# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_hot
- machine: windows-amd64
- commit hash: 4cfabf5
- commit date: 2025-06-20
- overall geometric mean: 1.072x faster
- HPT reliability: 57.26%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 222 ms: 1.03x slower                                                   |
| docutils       | 1.53 sec                                                    | 1.68 sec: 1.10x slower                                                 |
| sphinx         | 617 ms                                                      | 649 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                       | 1.05x slower                                                           |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 161 ms: 1.86x faster                                                   |
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                                   |
| async_tree_io              | 513 ms                                                      | 400 ms: 1.28x faster                                                   |
| async_tree_none            | 219 ms                                                      | 172 ms: 1.27x faster                                                   |
| async_tree_io_tg           | 497 ms                                                      | 394 ms: 1.26x faster                                                   |
| async_tree_memoization     | 265 ms                                                      | 210 ms: 1.26x faster                                                   |
| async_tree_none_tg         | 200 ms                                                      | 169 ms: 1.19x faster                                                   |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 334 ms: 1.14x faster                                                   |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 347 ms: 1.10x faster                                                   |
| async_generators           | 223 ms                                                      | 248 ms: 1.11x slower                                                   |
| coroutines                 | 12.5 ms                                                     | 14.5 ms: 1.16x slower                                                  |
| Geometric mean             | (ref)                                                       | 1.20x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 56.4 ms: 1.17x faster                                                  |
| float          | 50.8 ms                                                     | 44.2 ms: 1.15x faster                                                  |
| pidigits       | 146 ms                                                      | 148 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                       | 1.10x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.2 ms: 1.67x faster                                                  |
| regex_effbot   | 1.69 ms                                                     | 1.63 ms: 1.04x faster                                                  |
| regex_compile  | 80.7 ms                                                     | 79.5 ms: 1.02x faster                                                  |
| regex_dna      | 115 ms                                                      | 121 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                       | 1.14x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.18 sec: 1.16x faster                                                 |
| unpickle_pure_python | 130 us                                                      | 112 us: 1.16x faster                                                   |
| json_loads           | 15.1 us                                                     | 14.3 us: 1.06x faster                                                  |
| xml_etree_parse      | 92.2 ms                                                     | 87.9 ms: 1.05x faster                                                  |
| xml_etree_generate   | 53.5 ms                                                     | 52.2 ms: 1.02x faster                                                  |
| xml_etree_iterparse  | 60.5 ms                                                     | 64.3 ms: 1.06x slower                                                  |
| pickle_pure_python   | 186 us                                                      | 207 us: 1.11x slower                                                   |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                           |

Benchmark hidden because not significant (2): json_dumps, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.8 ms: 1.06x slower                                                  |
| python_startup_no_site | 16.9 ms                                                     | 19.5 ms: 1.16x slower                                                  |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.65 ms: 1.16x faster                                                  |
| genshi_text     | 15.2 ms                                                     | 15.5 ms: 1.02x slower                                                  |
| django_template | 20.3 ms                                                     | 24.1 ms: 1.19x slower                                                  |
| Geometric mean  | (ref)                                                       | 1.01x slower                                                           |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 489 us: 17.30x faster                                                  |
| pathlib                    | 75.3 ms                                                     | 31.8 ms: 2.37x faster                                                  |
| asyncio_websockets         | 300 ms                                                      | 161 ms: 1.86x faster                                                   |
| mdp                        | 1.43 sec                                                    | 820 ms: 1.75x faster                                                   |
| regex_v8                   | 23.8 ms                                                     | 14.2 ms: 1.67x faster                                                  |
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                                   |
| deepcopy                   | 223 us                                                      | 171 us: 1.31x faster                                                   |
| async_tree_io              | 513 ms                                                      | 400 ms: 1.28x faster                                                   |
| async_tree_none            | 219 ms                                                      | 172 ms: 1.27x faster                                                   |
| async_tree_io_tg           | 497 ms                                                      | 394 ms: 1.26x faster                                                   |
| async_tree_memoization     | 265 ms                                                      | 210 ms: 1.26x faster                                                   |
| deepcopy_memo              | 23.1 us                                                     | 18.4 us: 1.26x faster                                                  |
| async_tree_none_tg         | 200 ms                                                      | 169 ms: 1.19x faster                                                   |
| nbody                      | 66.3 ms                                                     | 56.4 ms: 1.17x faster                                                  |
| tomli_loads                | 1.37 sec                                                    | 1.18 sec: 1.16x faster                                                 |
| mako                       | 6.56 ms                                                     | 5.65 ms: 1.16x faster                                                  |
| unpickle_pure_python       | 130 us                                                      | 112 us: 1.16x faster                                                   |
| float                      | 50.8 ms                                                     | 44.2 ms: 1.15x faster                                                  |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 334 ms: 1.14x faster                                                   |
| scimark_fft                | 175 ms                                                      | 156 ms: 1.12x faster                                                   |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.34 ms: 1.11x faster                                                  |
| telco                      | 4.85 ms                                                     | 4.35 ms: 1.11x faster                                                  |
| deepcopy_reduce            | 2.02 us                                                     | 1.82 us: 1.11x faster                                                  |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 347 ms: 1.10x faster                                                   |
| json                       | 3.30 ms                                                     | 3.00 ms: 1.10x faster                                                  |
| go                         | 84.7 ms                                                     | 78.5 ms: 1.08x faster                                                  |
| pyflate                    | 283 ms                                                      | 263 ms: 1.07x faster                                                   |
| spectral_norm              | 63.4 ms                                                     | 59.3 ms: 1.07x faster                                                  |
| bpe_tokeniser              | 2.87 sec                                                    | 2.69 sec: 1.07x faster                                                 |
| fannkuch                   | 252 ms                                                      | 236 ms: 1.07x faster                                                   |
| json_loads                 | 15.1 us                                                     | 14.3 us: 1.06x faster                                                  |
| xml_etree_parse            | 92.2 ms                                                     | 87.9 ms: 1.05x faster                                                  |
| regex_effbot               | 1.69 ms                                                     | 1.63 ms: 1.04x faster                                                  |
| k_core                     | 1.70 sec                                                    | 1.64 sec: 1.04x faster                                                 |
| sqlite_synth               | 1.59 us                                                     | 1.55 us: 1.03x faster                                                  |
| xml_etree_generate         | 53.5 ms                                                     | 52.2 ms: 1.02x faster                                                  |
| scimark_monte_carlo        | 40.7 ms                                                     | 39.9 ms: 1.02x faster                                                  |
| regex_compile              | 80.7 ms                                                     | 79.5 ms: 1.02x faster                                                  |
| scimark_sor                | 76.2 ms                                                     | 75.9 ms: 1.00x faster                                                  |
| crypto_pyaes               | 45.6 ms                                                     | 45.9 ms: 1.01x slower                                                  |
| pidigits                   | 146 ms                                                      | 148 ms: 1.01x slower                                                   |
| genshi_text                | 15.2 ms                                                     | 15.5 ms: 1.02x slower                                                  |
| meteor_contest             | 72.0 ms                                                     | 73.3 ms: 1.02x slower                                                  |
| sympy_integrate            | 12.3 ms                                                     | 12.7 ms: 1.03x slower                                                  |
| dulwich_log                | 40.1 ms                                                     | 41.3 ms: 1.03x slower                                                  |
| connected_components       | 320 ms                                                      | 329 ms: 1.03x slower                                                   |
| 2to3                       | 215 ms                                                      | 222 ms: 1.03x slower                                                   |
| sympy_str                  | 167 ms                                                      | 172 ms: 1.03x slower                                                   |
| sympy_sum                  | 85.2 ms                                                     | 88.1 ms: 1.03x slower                                                  |
| typing_runtime_protocols   | 103 us                                                      | 107 us: 1.03x slower                                                   |
| scimark_lu                 | 56.7 ms                                                     | 58.9 ms: 1.04x slower                                                  |
| generators                 | 19.0 ms                                                     | 19.7 ms: 1.04x slower                                                  |
| sympy_expand               | 286 ms                                                      | 297 ms: 1.04x slower                                                   |
| chaos                      | 37.9 ms                                                     | 39.5 ms: 1.04x slower                                                  |
| regex_dna                  | 115 ms                                                      | 121 ms: 1.05x slower                                                   |
| sphinx                     | 617 ms                                                      | 649 ms: 1.05x slower                                                   |
| nqueens                    | 56.1 ms                                                     | 59.4 ms: 1.06x slower                                                  |
| richards_super             | 29.8 ms                                                     | 31.5 ms: 1.06x slower                                                  |
| python_startup             | 24.4 ms                                                     | 25.8 ms: 1.06x slower                                                  |
| richards                   | 26.3 ms                                                     | 27.8 ms: 1.06x slower                                                  |
| xml_etree_iterparse        | 60.5 ms                                                     | 64.3 ms: 1.06x slower                                                  |
| pprint_safe_repr           | 485 ms                                                      | 518 ms: 1.07x slower                                                   |
| pprint_pformat             | 977 ms                                                      | 1.05 sec: 1.07x slower                                                 |
| hexiom                     | 3.84 ms                                                     | 4.13 ms: 1.08x slower                                                  |
| comprehensions             | 10.4 us                                                     | 11.2 us: 1.08x slower                                                  |
| create_gc_cycles           | 1.22 ms                                                     | 1.32 ms: 1.08x slower                                                  |
| coverage                   | 45.3 ms                                                     | 49.0 ms: 1.08x slower                                                  |
| docutils                   | 1.53 sec                                                    | 1.68 sec: 1.10x slower                                                 |
| gc_traversal               | 1.96 ms                                                     | 2.16 ms: 1.10x slower                                                  |
| pickle_pure_python         | 186 us                                                      | 207 us: 1.11x slower                                                   |
| logging_format             | 6.18 us                                                     | 6.86 us: 1.11x slower                                                  |
| async_generators           | 223 ms                                                      | 248 ms: 1.11x slower                                                   |
| logging_simple             | 5.77 us                                                     | 6.49 us: 1.12x slower                                                  |
| python_startup_no_site     | 16.9 ms                                                     | 19.5 ms: 1.16x slower                                                  |
| coroutines                 | 12.5 ms                                                     | 14.5 ms: 1.16x slower                                                  |
| deltablue                  | 1.89 ms                                                     | 2.23 ms: 1.18x slower                                                  |
| raytrace                   | 153 ms                                                      | 181 ms: 1.18x slower                                                   |
| django_template            | 20.3 ms                                                     | 24.1 ms: 1.19x slower                                                  |
| many_optionals             | 361 us                                                      | 449 us: 1.24x slower                                                   |
| subparsers                 | 10.9 ms                                                     | 17.2 ms: 1.58x slower                                                  |
| logging_silent             | 54.6 ns                                                     | 319 ns: 5.85x slower                                                   |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                           |

Benchmark hidden because not significant (7): pylint, json_dumps, xml_etree_process, shortest_path, html5lib, genshi_xml, pycparser
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250620-3.15.0a0-4cfabf5-JIT/bm-20250620-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-4cfabf5.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.072x faster

# HPT report

- Reliability score: 57.26% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown