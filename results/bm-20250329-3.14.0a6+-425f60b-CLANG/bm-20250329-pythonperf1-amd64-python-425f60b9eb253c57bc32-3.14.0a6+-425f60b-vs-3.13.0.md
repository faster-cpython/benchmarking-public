# Results vs. 3.13.0

- fork: python
- ref: 425f60b9eb253c57bc32
- machine: windows-amd64
- commit hash: 425f60b
- commit date: 2025-03-29
- overall geometric mean: 1.179x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 203 ms: 1.06x faster                                                        |
| html5lib       | 38.2 ms                                                     | 35.4 ms: 1.08x faster                                                       |
| sphinx         | 617 ms                                                      | 595 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                       | 1.04x faster                                                                |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 159 ms: 1.88x faster                                                        |
| async_tree_io              | 513 ms                                                      | 350 ms: 1.47x faster                                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 198 ms: 1.42x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 350 ms: 1.42x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 189 ms: 1.40x faster                                                        |
| async_tree_none            | 219 ms                                                      | 157 ms: 1.40x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 151 ms: 1.32x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 312 ms: 1.22x faster                                                        |
| async_generators           | 223 ms                                                      | 183 ms: 1.22x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 317 ms: 1.21x faster                                                        |
| coroutines                 | 12.5 ms                                                     | 10.7 ms: 1.17x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.36x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 48.0 ms: 1.38x faster                                                       |
| float          | 50.8 ms                                                     | 36.9 ms: 1.38x faster                                                       |
| pidigits       | 146 ms                                                      | 145 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                       | 1.24x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 12.4 ms: 1.92x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 69.1 ms: 1.17x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.50 ms: 1.13x faster                                                       |
| regex_dna      | 115 ms                                                      | 117 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                       | 1.25x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.09 sec: 1.26x faster                                                      |
| unpickle_pure_python | 130 us                                                      | 106 us: 1.22x faster                                                        |
| json_dumps           | 6.19 ms                                                     | 5.50 ms: 1.13x faster                                                       |
| json_loads           | 15.1 us                                                     | 13.8 us: 1.09x faster                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 49.0 ms: 1.09x faster                                                       |
| xml_etree_process    | 36.5 ms                                                     | 34.2 ms: 1.07x faster                                                       |
| pickle_pure_python   | 186 us                                                      | 174 us: 1.07x faster                                                        |
| xml_etree_parse      | 92.2 ms                                                     | 91.0 ms: 1.01x faster                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 61.6 ms: 1.02x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.10x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.6 ms: 1.09x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 20.3 ms: 1.20x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 15.2 ms                                                     | 12.3 ms: 1.24x faster                                                       |
| genshi_xml      | 33.9 ms                                                     | 29.8 ms: 1.14x faster                                                       |
| mako            | 6.56 ms                                                     | 5.80 ms: 1.13x faster                                                       |
| django_template | 20.3 ms                                                     | 20.5 ms: 1.01x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.12x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 31.2 ms: 2.42x faster                                                       |
| mdp                        | 1.43 sec                                                    | 671 ms: 2.13x faster                                                        |
| regex_v8                   | 23.8 ms                                                     | 12.4 ms: 1.92x faster                                                       |
| asyncio_websockets         | 300 ms                                                      | 159 ms: 1.88x faster                                                        |
| deepcopy_memo              | 23.1 us                                                     | 14.0 us: 1.65x faster                                                       |
| deepcopy                   | 223 us                                                      | 143 us: 1.56x faster                                                        |
| scimark_sor                | 76.2 ms                                                     | 50.0 ms: 1.52x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 42.8 ms: 1.48x faster                                                       |
| async_tree_io              | 513 ms                                                      | 350 ms: 1.47x faster                                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 198 ms: 1.42x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 350 ms: 1.42x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 189 ms: 1.40x faster                                                        |
| async_tree_none            | 219 ms                                                      | 157 ms: 1.40x faster                                                        |
| scimark_monte_carlo        | 40.7 ms                                                     | 29.1 ms: 1.40x faster                                                       |
| go                         | 84.7 ms                                                     | 60.7 ms: 1.39x faster                                                       |
| nbody                      | 66.3 ms                                                     | 48.0 ms: 1.38x faster                                                       |
| float                      | 50.8 ms                                                     | 36.9 ms: 1.38x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 151 ms: 1.32x faster                                                        |
| logging_silent             | 54.6 ns                                                     | 41.8 ns: 1.31x faster                                                       |
| scimark_lu                 | 56.7 ms                                                     | 43.5 ms: 1.30x faster                                                       |
| hexiom                     | 3.84 ms                                                     | 2.96 ms: 1.30x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.01 ms: 1.30x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.57 us: 1.29x faster                                                       |
| fannkuch                   | 252 ms                                                      | 196 ms: 1.29x faster                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.09 sec: 1.26x faster                                                      |
| scimark_fft                | 175 ms                                                      | 139 ms: 1.26x faster                                                        |
| generators                 | 19.0 ms                                                     | 15.3 ms: 1.24x faster                                                       |
| genshi_text                | 15.2 ms                                                     | 12.3 ms: 1.24x faster                                                       |
| pyflate                    | 283 ms                                                      | 229 ms: 1.23x faster                                                        |
| unpickle_pure_python       | 130 us                                                      | 106 us: 1.22x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 312 ms: 1.22x faster                                                        |
| async_generators           | 223 ms                                                      | 183 ms: 1.22x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 317 ms: 1.21x faster                                                        |
| comprehensions             | 10.4 us                                                     | 8.60 us: 1.21x faster                                                       |
| chaos                      | 37.9 ms                                                     | 31.4 ms: 1.20x faster                                                       |
| pprint_safe_repr           | 485 ms                                                      | 405 ms: 1.20x faster                                                        |
| json                       | 3.30 ms                                                     | 2.78 ms: 1.19x faster                                                       |
| richards                   | 26.3 ms                                                     | 22.2 ms: 1.18x faster                                                       |
| pprint_pformat             | 977 ms                                                      | 828 ms: 1.18x faster                                                        |
| typing_runtime_protocols   | 103 us                                                      | 87.6 us: 1.18x faster                                                       |
| coroutines                 | 12.5 ms                                                     | 10.7 ms: 1.17x faster                                                       |
| regex_compile              | 80.7 ms                                                     | 69.1 ms: 1.17x faster                                                       |
| deltablue                  | 1.89 ms                                                     | 1.62 ms: 1.16x faster                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 39.2 ms: 1.16x faster                                                       |
| nqueens                    | 56.1 ms                                                     | 48.4 ms: 1.16x faster                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.48 sec: 1.16x faster                                                      |
| richards_super             | 29.8 ms                                                     | 25.7 ms: 1.16x faster                                                       |
| genshi_xml                 | 33.9 ms                                                     | 29.8 ms: 1.14x faster                                                       |
| mako                       | 6.56 ms                                                     | 5.80 ms: 1.13x faster                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.50 ms: 1.13x faster                                                       |
| json_dumps                 | 6.19 ms                                                     | 5.50 ms: 1.13x faster                                                       |
| sympy_str                  | 167 ms                                                      | 149 ms: 1.12x faster                                                        |
| telco                      | 4.85 ms                                                     | 4.33 ms: 1.12x faster                                                       |
| sympy_expand               | 286 ms                                                      | 257 ms: 1.11x faster                                                        |
| pylint                     | 205 ms                                                      | 185 ms: 1.11x faster                                                        |
| meteor_contest             | 72.0 ms                                                     | 65.9 ms: 1.09x faster                                                       |
| json_loads                 | 15.1 us                                                     | 13.8 us: 1.09x faster                                                       |
| raytrace                   | 153 ms                                                      | 140 ms: 1.09x faster                                                        |
| xml_etree_generate         | 53.5 ms                                                     | 49.0 ms: 1.09x faster                                                       |
| sympy_integrate            | 12.3 ms                                                     | 11.3 ms: 1.09x faster                                                       |
| sympy_sum                  | 85.2 ms                                                     | 78.7 ms: 1.08x faster                                                       |
| html5lib                   | 38.2 ms                                                     | 35.4 ms: 1.08x faster                                                       |
| pycparser                  | 695 ms                                                      | 645 ms: 1.08x faster                                                        |
| xml_etree_process          | 36.5 ms                                                     | 34.2 ms: 1.07x faster                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.49 us: 1.07x faster                                                       |
| pickle_pure_python         | 186 us                                                      | 174 us: 1.07x faster                                                        |
| 2to3                       | 215 ms                                                      | 203 ms: 1.06x faster                                                        |
| dulwich_log                | 40.1 ms                                                     | 38.2 ms: 1.05x faster                                                       |
| sphinx                     | 617 ms                                                      | 595 ms: 1.04x faster                                                        |
| k_core                     | 1.70 sec                                                    | 1.64 sec: 1.03x faster                                                      |
| logging_simple             | 5.77 us                                                     | 5.62 us: 1.03x faster                                                       |
| logging_format             | 6.18 us                                                     | 6.04 us: 1.02x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 91.0 ms: 1.01x faster                                                       |
| shortest_path              | 355 ms                                                      | 351 ms: 1.01x faster                                                        |
| pidigits                   | 146 ms                                                      | 145 ms: 1.01x faster                                                        |
| django_template            | 20.3 ms                                                     | 20.5 ms: 1.01x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 61.6 ms: 1.02x slower                                                       |
| regex_dna                  | 115 ms                                                      | 117 ms: 1.02x slower                                                        |
| connected_components       | 320 ms                                                      | 330 ms: 1.03x slower                                                        |
| coverage                   | 45.3 ms                                                     | 47.0 ms: 1.04x slower                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 88.8 ms: 1.05x slower                                                       |
| python_startup             | 24.4 ms                                                     | 26.6 ms: 1.09x slower                                                       |
| many_optionals             | 361 us                                                      | 399 us: 1.10x slower                                                        |
| create_gc_cycles           | 1.22 ms                                                     | 1.36 ms: 1.11x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 20.3 ms: 1.20x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 15.0 ms: 1.38x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.73 ms: 1.39x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.18x faster                                                                |

Benchmark hidden because not significant (2): docutils, bench_thread_pool
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250329-3.14.0a6+-425f60b-CLANG/bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.179x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown