# Results vs. 3.13.0

- fork: python
- ref: d783d7b51d31db568de6
- machine: windows-amd64
- commit hash: d783d7b
- commit date: 2025-03-18
- overall geometric mean: 1.002x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-pythonperf1-amd64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 227 ms: 1.06x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.71 sec: 1.12x slower                                                      |
| html5lib       | 38.2 ms                                                     | 41.3 ms: 1.08x slower                                                       |
| sphinx         | 617 ms                                                      | 660 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                       | 1.08x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-pythonperf1-amd64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 219 ms: 1.28x faster                                                        |
| async_tree_io              | 513 ms                                                      | 429 ms: 1.19x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 418 ms: 1.19x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 224 ms: 1.18x faster                                                        |
| async_tree_none            | 219 ms                                                      | 190 ms: 1.15x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 181 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 346 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 346 ms: 1.10x faster                                                        |
| asyncio_websockets         | 300 ms                                                      | 308 ms: 1.03x slower                                                        |
| async_generators           | 223 ms                                                      | 229 ms: 1.03x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.6 ms: 1.09x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.10x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-pythonperf1-amd64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 46.5 ms: 1.09x faster                                                       |
| nbody          | 66.3 ms                                                     | 67.0 ms: 1.01x slower                                                       |
| pidigits       | 146 ms                                                      | 149 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-pythonperf1-amd64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.8 ms: 1.73x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.45 ms: 1.17x faster                                                       |
| regex_dna      | 115 ms                                                      | 117 ms: 1.02x slower                                                        |
| regex_compile  | 80.7 ms                                                     | 89.0 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-pythonperf1-amd64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 88.7 ms: 1.04x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.44 sec: 1.05x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.7 ms: 1.05x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 59.2 ms: 1.11x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 6.93 ms: 1.12x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 42.1 ms: 1.15x slower                                                       |
| unpickle_pure_python | 130 us                                                      | 152 us: 1.17x slower                                                        |
| pickle_pure_python   | 186 us                                                      | 228 us: 1.23x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                                |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-pythonperf1-amd64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.4 ms: 1.08x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 20.4 ms: 1.21x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-pythonperf1-amd64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.73 ms: 1.02x slower                                                       |
| genshi_xml      | 33.9 ms                                                     | 38.5 ms: 1.14x slower                                                       |
| genshi_text     | 15.2 ms                                                     | 17.4 ms: 1.14x slower                                                       |
| django_template | 20.3 ms                                                     | 26.7 ms: 1.32x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.15x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-pythonperf1-amd64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 522 us: 16.21x faster                                                       |
| pathlib                    | 75.3 ms                                                     | 32.7 ms: 2.31x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 13.8 ms: 1.73x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 219 ms: 1.28x faster                                                        |
| deepcopy_memo              | 23.1 us                                                     | 19.1 us: 1.21x faster                                                       |
| deepcopy                   | 223 us                                                      | 187 us: 1.20x faster                                                        |
| async_tree_io              | 513 ms                                                      | 429 ms: 1.19x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 418 ms: 1.19x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 224 ms: 1.18x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.45 ms: 1.17x faster                                                       |
| async_tree_none            | 219 ms                                                      | 190 ms: 1.15x faster                                                        |
| spectral_norm              | 63.4 ms                                                     | 57.2 ms: 1.11x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 181 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 346 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 346 ms: 1.10x faster                                                        |
| float                      | 50.8 ms                                                     | 46.5 ms: 1.09x faster                                                       |
| json                       | 3.30 ms                                                     | 3.06 ms: 1.08x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 88.7 ms: 1.04x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.53 ms: 1.03x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 2.00 us: 1.01x faster                                                       |
| nbody                      | 66.3 ms                                                     | 67.0 ms: 1.01x slower                                                       |
| pidigits                   | 146 ms                                                      | 149 ms: 1.01x slower                                                        |
| regex_dna                  | 115 ms                                                      | 117 ms: 1.02x slower                                                        |
| create_gc_cycles           | 1.22 ms                                                     | 1.25 ms: 1.02x slower                                                       |
| telco                      | 4.85 ms                                                     | 4.96 ms: 1.02x slower                                                       |
| mako                       | 6.56 ms                                                     | 6.73 ms: 1.02x slower                                                       |
| asyncio_websockets         | 300 ms                                                      | 308 ms: 1.03x slower                                                        |
| shortest_path              | 355 ms                                                      | 365 ms: 1.03x slower                                                        |
| async_generators           | 223 ms                                                      | 229 ms: 1.03x slower                                                        |
| generators                 | 19.0 ms                                                     | 19.6 ms: 1.03x slower                                                       |
| connected_components       | 320 ms                                                      | 333 ms: 1.04x slower                                                        |
| sqlite_synth               | 1.59 us                                                     | 1.65 us: 1.04x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 3.00 sec: 1.05x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.44 sec: 1.05x slower                                                      |
| gc_traversal               | 1.96 ms                                                     | 2.06 ms: 1.05x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.7 ms: 1.05x slower                                                       |
| scimark_fft                | 175 ms                                                      | 184 ms: 1.05x slower                                                        |
| bench_mp_pool              | 84.2 ms                                                     | 88.8 ms: 1.05x slower                                                       |
| 2to3                       | 215 ms                                                      | 227 ms: 1.06x slower                                                        |
| coverage                   | 45.3 ms                                                     | 48.4 ms: 1.07x slower                                                       |
| go                         | 84.7 ms                                                     | 90.4 ms: 1.07x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 76.9 ms: 1.07x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 91.0 ms: 1.07x slower                                                       |
| sphinx                     | 617 ms                                                      | 660 ms: 1.07x slower                                                        |
| sympy_str                  | 167 ms                                                      | 178 ms: 1.07x slower                                                        |
| scimark_lu                 | 56.7 ms                                                     | 60.9 ms: 1.07x slower                                                       |
| sympy_expand               | 286 ms                                                      | 307 ms: 1.07x slower                                                        |
| scimark_sor                | 76.2 ms                                                     | 81.9 ms: 1.07x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 111 us: 1.07x slower                                                        |
| logging_silent             | 54.6 ns                                                     | 58.9 ns: 1.08x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 49.3 ms: 1.08x slower                                                       |
| python_startup             | 24.4 ms                                                     | 26.4 ms: 1.08x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.4 ms: 1.08x slower                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 44.1 ms: 1.08x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 878 us: 1.08x slower                                                        |
| html5lib                   | 38.2 ms                                                     | 41.3 ms: 1.08x slower                                                       |
| pycparser                  | 695 ms                                                      | 754 ms: 1.08x slower                                                        |
| dulwich_log                | 40.1 ms                                                     | 43.5 ms: 1.09x slower                                                       |
| fannkuch                   | 252 ms                                                      | 273 ms: 1.09x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.6 ms: 1.09x slower                                                       |
| regex_compile              | 80.7 ms                                                     | 89.0 ms: 1.10x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 59.2 ms: 1.11x slower                                                       |
| pyflate                    | 283 ms                                                      | 314 ms: 1.11x slower                                                        |
| richards                   | 26.3 ms                                                     | 29.3 ms: 1.12x slower                                                       |
| richards_super             | 29.8 ms                                                     | 33.3 ms: 1.12x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.71 sec: 1.12x slower                                                      |
| json_dumps                 | 6.19 ms                                                     | 6.93 ms: 1.12x slower                                                       |
| pprint_safe_repr           | 485 ms                                                      | 545 ms: 1.12x slower                                                        |
| mdp                        | 1.43 sec                                                    | 1.62 sec: 1.13x slower                                                      |
| pprint_pformat             | 977 ms                                                      | 1.10 sec: 1.13x slower                                                      |
| genshi_xml                 | 33.9 ms                                                     | 38.5 ms: 1.14x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 17.4 ms: 1.14x slower                                                       |
| chaos                      | 37.9 ms                                                     | 43.4 ms: 1.15x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 42.1 ms: 1.15x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.46 ms: 1.16x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 65.2 ms: 1.16x slower                                                       |
| comprehensions             | 10.4 us                                                     | 12.1 us: 1.16x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 152 us: 1.17x slower                                                        |
| logging_simple             | 5.77 us                                                     | 6.82 us: 1.18x slower                                                       |
| logging_format             | 6.18 us                                                     | 7.36 us: 1.19x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.27 ms: 1.20x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 20.4 ms: 1.21x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 228 us: 1.23x slower                                                        |
| many_optionals             | 361 us                                                      | 444 us: 1.23x slower                                                        |
| raytrace                   | 153 ms                                                      | 199 ms: 1.30x slower                                                        |
| django_template            | 20.3 ms                                                     | 26.7 ms: 1.32x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 16.8 ms: 1.55x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (3): pylint, json_loads, k_core
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250318-3.14.0a6+-d783d7b/bm-20250318-pythonperf1-amd64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown