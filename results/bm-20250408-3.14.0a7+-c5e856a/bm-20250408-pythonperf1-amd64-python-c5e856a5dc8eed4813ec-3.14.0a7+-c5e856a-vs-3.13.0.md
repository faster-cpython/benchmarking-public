# Results vs. 3.13.0

- fork: python
- ref: c5e856a5dc8eed4813ec
- machine: windows-amd64
- commit hash: c5e856a
- commit date: 2025-04-08
- overall geometric mean: 1.042x faster
- HPT reliability: 55.84%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-pythonperf1-amd64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 217 ms: 1.01x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.63 sec: 1.06x slower                                                      |
| sphinx         | 617 ms                                                      | 637 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-pythonperf1-amd64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 156 ms: 1.93x faster                                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 209 ms: 1.35x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 205 ms: 1.29x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 395 ms: 1.26x faster                                                        |
| async_tree_io              | 513 ms                                                      | 409 ms: 1.25x faster                                                        |
| async_tree_none            | 219 ms                                                      | 178 ms: 1.23x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 170 ms: 1.18x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 327 ms: 1.16x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 337 ms: 1.14x faster                                                        |
| async_generators           | 223 ms                                                      | 228 ms: 1.02x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.3 ms: 1.07x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.22x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-pythonperf1-amd64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 42.4 ms: 1.20x faster                                                       |
| nbody          | 66.3 ms                                                     | 61.9 ms: 1.07x faster                                                       |
| pidigits       | 146 ms                                                      | 148 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-pythonperf1-amd64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.1 ms: 1.69x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.43 ms: 1.18x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 79.2 ms: 1.02x faster                                                       |
| regex_dna      | 115 ms                                                      | 117 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                       | 1.19x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-pythonperf1-amd64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 89.7 ms: 1.03x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.34 sec: 1.02x faster                                                      |
| json_loads           | 15.1 us                                                     | 14.9 us: 1.01x faster                                                       |
| unpickle_pure_python | 130 us                                                      | 134 us: 1.03x slower                                                        |
| xml_etree_generate   | 53.5 ms                                                     | 55.4 ms: 1.04x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 6.45 ms: 1.04x slower                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.6 ms: 1.05x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 39.0 ms: 1.07x slower                                                       |
| pickle_pure_python   | 186 us                                                      | 210 us: 1.13x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-pythonperf1-amd64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.2 ms: 1.03x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 19.5 ms: 1.16x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.09x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-pythonperf1-amd64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.31 ms: 1.04x faster                                                       |
| genshi_text     | 15.2 ms                                                     | 15.4 ms: 1.01x slower                                                       |
| django_template | 20.3 ms                                                     | 24.6 ms: 1.21x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.04x slower                                                                |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-pythonperf1-amd64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 28.5 ms: 2.64x faster                                                       |
| asyncio_websockets         | 300 ms                                                      | 156 ms: 1.93x faster                                                        |
| mdp                        | 1.43 sec                                                    | 772 ms: 1.85x faster                                                        |
| regex_v8                   | 23.8 ms                                                     | 14.1 ms: 1.69x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 209 ms: 1.35x faster                                                        |
| deepcopy                   | 223 us                                                      | 167 us: 1.34x faster                                                        |
| deepcopy_memo              | 23.1 us                                                     | 17.8 us: 1.30x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 205 ms: 1.29x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 395 ms: 1.26x faster                                                        |
| async_tree_io              | 513 ms                                                      | 409 ms: 1.25x faster                                                        |
| async_tree_none            | 219 ms                                                      | 178 ms: 1.23x faster                                                        |
| float                      | 50.8 ms                                                     | 42.4 ms: 1.20x faster                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.43 ms: 1.18x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 170 ms: 1.18x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 327 ms: 1.16x faster                                                        |
| deepcopy_reduce            | 2.02 us                                                     | 1.78 us: 1.14x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 337 ms: 1.14x faster                                                        |
| spectral_norm              | 63.4 ms                                                     | 56.2 ms: 1.13x faster                                                       |
| go                         | 84.7 ms                                                     | 76.4 ms: 1.11x faster                                                       |
| nbody                      | 66.3 ms                                                     | 61.9 ms: 1.07x faster                                                       |
| json                       | 3.30 ms                                                     | 3.08 ms: 1.07x faster                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 38.2 ms: 1.07x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.56 ms: 1.06x faster                                                       |
| scimark_sor                | 76.2 ms                                                     | 72.2 ms: 1.06x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.49 ms: 1.05x faster                                                       |
| mako                       | 6.56 ms                                                     | 6.31 ms: 1.04x faster                                                       |
| fannkuch                   | 252 ms                                                      | 245 ms: 1.03x faster                                                        |
| xml_etree_parse            | 92.2 ms                                                     | 89.7 ms: 1.03x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.34 sec: 1.02x faster                                                      |
| regex_compile              | 80.7 ms                                                     | 79.2 ms: 1.02x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.9 us: 1.01x faster                                                       |
| shortest_path              | 355 ms                                                      | 352 ms: 1.01x faster                                                        |
| sqlite_synth               | 1.59 us                                                     | 1.57 us: 1.01x faster                                                       |
| scimark_fft                | 175 ms                                                      | 174 ms: 1.01x faster                                                        |
| bpe_tokeniser              | 2.87 sec                                                    | 2.86 sec: 1.00x faster                                                      |
| pprint_safe_repr           | 485 ms                                                      | 487 ms: 1.01x slower                                                        |
| pyflate                    | 283 ms                                                      | 285 ms: 1.01x slower                                                        |
| 2to3                       | 215 ms                                                      | 217 ms: 1.01x slower                                                        |
| pidigits                   | 146 ms                                                      | 148 ms: 1.01x slower                                                        |
| connected_components       | 320 ms                                                      | 323 ms: 1.01x slower                                                        |
| typing_runtime_protocols   | 103 us                                                      | 104 us: 1.01x slower                                                        |
| logging_silent             | 54.6 ns                                                     | 55.3 ns: 1.01x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 15.4 ms: 1.01x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 12.5 ms: 1.01x slower                                                       |
| regex_dna                  | 115 ms                                                      | 117 ms: 1.02x slower                                                        |
| pprint_pformat             | 977 ms                                                      | 997 ms: 1.02x slower                                                        |
| async_generators           | 223 ms                                                      | 228 ms: 1.02x slower                                                        |
| dulwich_log                | 40.1 ms                                                     | 41.1 ms: 1.02x slower                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 86.3 ms: 1.03x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.01 ms: 1.03x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 134 us: 1.03x slower                                                        |
| bench_thread_pool          | 810 us                                                      | 834 us: 1.03x slower                                                        |
| sphinx                     | 617 ms                                                      | 637 ms: 1.03x slower                                                        |
| sympy_str                  | 167 ms                                                      | 172 ms: 1.03x slower                                                        |
| richards                   | 26.3 ms                                                     | 27.1 ms: 1.03x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 3.97 ms: 1.03x slower                                                       |
| python_startup             | 24.4 ms                                                     | 25.2 ms: 1.03x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 55.4 ms: 1.04x slower                                                       |
| sympy_expand               | 286 ms                                                      | 296 ms: 1.04x slower                                                        |
| richards_super             | 29.8 ms                                                     | 30.9 ms: 1.04x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 59.0 ms: 1.04x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 6.45 ms: 1.04x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 89.0 ms: 1.04x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.6 ms: 1.05x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.63 sec: 1.06x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.15 us: 1.07x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.3 ms: 1.07x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 39.0 ms: 1.07x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 60.2 ms: 1.07x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.67 us: 1.08x slower                                                       |
| comprehensions             | 10.4 us                                                     | 11.4 us: 1.10x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.10 ms: 1.11x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 210 us: 1.13x slower                                                        |
| coverage                   | 45.3 ms                                                     | 51.2 ms: 1.13x slower                                                       |
| raytrace                   | 153 ms                                                      | 175 ms: 1.14x slower                                                        |
| python_startup_no_site     | 16.9 ms                                                     | 19.5 ms: 1.16x slower                                                       |
| many_optionals             | 361 us                                                      | 428 us: 1.18x slower                                                        |
| django_template            | 20.3 ms                                                     | 24.6 ms: 1.21x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 15.9 ms: 1.46x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                                |

Benchmark hidden because not significant (10): pylint, k_core, create_gc_cycles, html5lib, chaos, genshi_xml, crypto_pyaes, generators, meteor_contest, pycparser
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250408-3.14.0a7+-c5e856a/bm-20250408-pythonperf1-amd64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.042x faster

# HPT report

- Reliability score: 55.84% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown