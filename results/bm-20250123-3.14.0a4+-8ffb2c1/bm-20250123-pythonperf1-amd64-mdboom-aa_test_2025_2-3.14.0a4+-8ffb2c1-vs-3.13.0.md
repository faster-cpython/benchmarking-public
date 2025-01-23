# Results vs. 3.13.0

- fork: mdboom
- ref: aa_test_2025_2
- machine: windows-amd64
- commit hash: 8ffb2c1
- commit date: 2025-01-23
- overall geometric mean: 1.022x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf1-amd64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 233 ms: 1.08x slower                                                  |
| docutils       | 1.53 sec                                                    | 1.70 sec: 1.11x slower                                                |
| html5lib       | 38.2 ms                                                     | 40.7 ms: 1.07x slower                                                 |
| sphinx         | 617 ms                                                      | 666 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                       | 1.08x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf1-amd64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 214 ms: 1.31x faster                                                  |
| async_tree_io              | 513 ms                                                      | 413 ms: 1.24x faster                                                  |
| async_tree_io_tg           | 497 ms                                                      | 404 ms: 1.23x faster                                                  |
| async_tree_none            | 219 ms                                                      | 186 ms: 1.18x faster                                                  |
| async_tree_memoization     | 265 ms                                                      | 226 ms: 1.17x faster                                                  |
| async_tree_none_tg         | 200 ms                                                      | 175 ms: 1.14x faster                                                  |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 348 ms: 1.10x faster                                                  |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 347 ms: 1.10x faster                                                  |
| async_generators           | 223 ms                                                      | 225 ms: 1.01x slower                                                  |
| coroutines                 | 12.5 ms                                                     | 15.3 ms: 1.22x slower                                                 |
| Geometric mean             | (ref)                                                       | 1.11x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf1-amd64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 51.4 ms: 1.01x slower                                                 |
| pidigits       | 146 ms                                                      | 148 ms: 1.01x slower                                                  |
| nbody          | 66.3 ms                                                     | 77.3 ms: 1.17x slower                                                 |
| Geometric mean | (ref)                                                       | 1.06x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf1-amd64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 16.5 ms: 1.45x faster                                                 |
| regex_effbot   | 1.69 ms                                                     | 1.46 ms: 1.16x faster                                                 |
| regex_dna      | 115 ms                                                      | 117 ms: 1.02x slower                                                  |
| regex_compile  | 80.7 ms                                                     | 88.2 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                       | 1.11x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf1-amd64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 88.5 ms: 1.04x faster                                                 |
| json_loads           | 15.1 us                                                     | 14.5 us: 1.04x faster                                                 |
| tomli_loads          | 1.37 sec                                                    | 1.39 sec: 1.01x slower                                                |
| xml_etree_iterparse  | 60.5 ms                                                     | 65.2 ms: 1.08x slower                                                 |
| json_dumps           | 6.19 ms                                                     | 6.82 ms: 1.10x slower                                                 |
| xml_etree_generate   | 53.5 ms                                                     | 59.4 ms: 1.11x slower                                                 |
| xml_etree_process    | 36.5 ms                                                     | 43.7 ms: 1.20x slower                                                 |
| unpickle_pure_python | 130 us                                                      | 159 us: 1.22x slower                                                  |
| pickle_pure_python   | 186 us                                                      | 239 us: 1.29x slower                                                  |
| Geometric mean       | (ref)                                                       | 1.10x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf1-amd64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 16.9 ms                                                     | 18.0 ms: 1.06x slower                                                 |
| Geometric mean         | (ref)                                                       | 1.03x slower                                                          |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf1-amd64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 35.1 ms: 1.04x slower                                                 |
| mako            | 6.56 ms                                                     | 6.89 ms: 1.05x slower                                                 |
| genshi_text     | 15.2 ms                                                     | 16.6 ms: 1.09x slower                                                 |
| django_template | 20.3 ms                                                     | 25.9 ms: 1.28x slower                                                 |
| Geometric mean  | (ref)                                                       | 1.11x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf1-amd64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 524 us: 16.17x faster                                                 |
| regex_v8                   | 23.8 ms                                                     | 16.5 ms: 1.45x faster                                                 |
| async_tree_memoization_tg  | 281 ms                                                      | 214 ms: 1.31x faster                                                  |
| async_tree_io              | 513 ms                                                      | 413 ms: 1.24x faster                                                  |
| async_tree_io_tg           | 497 ms                                                      | 404 ms: 1.23x faster                                                  |
| deepcopy                   | 223 us                                                      | 184 us: 1.21x faster                                                  |
| async_tree_none            | 219 ms                                                      | 186 ms: 1.18x faster                                                  |
| async_tree_memoization     | 265 ms                                                      | 226 ms: 1.17x faster                                                  |
| regex_effbot               | 1.69 ms                                                     | 1.46 ms: 1.16x faster                                                 |
| deepcopy_memo              | 23.1 us                                                     | 20.0 us: 1.15x faster                                                 |
| async_tree_none_tg         | 200 ms                                                      | 175 ms: 1.14x faster                                                  |
| json                       | 3.30 ms                                                     | 2.95 ms: 1.12x faster                                                 |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 348 ms: 1.10x faster                                                  |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 347 ms: 1.10x faster                                                  |
| deepcopy_reduce            | 2.02 us                                                     | 1.86 us: 1.09x faster                                                 |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.50 ms: 1.04x faster                                                 |
| xml_etree_parse            | 92.2 ms                                                     | 88.5 ms: 1.04x faster                                                 |
| json_loads                 | 15.1 us                                                     | 14.5 us: 1.04x faster                                                 |
| shortest_path              | 355 ms                                                      | 349 ms: 1.02x faster                                                  |
| tomli_loads                | 1.37 sec                                                    | 1.39 sec: 1.01x slower                                                |
| float                      | 50.8 ms                                                     | 51.4 ms: 1.01x slower                                                 |
| pidigits                   | 146 ms                                                      | 148 ms: 1.01x slower                                                  |
| async_generators           | 223 ms                                                      | 225 ms: 1.01x slower                                                  |
| k_core                     | 1.70 sec                                                    | 1.73 sec: 1.02x slower                                                |
| regex_dna                  | 115 ms                                                      | 117 ms: 1.02x slower                                                  |
| bench_thread_pool          | 810 us                                                      | 834 us: 1.03x slower                                                  |
| pathlib                    | 75.3 ms                                                     | 77.9 ms: 1.03x slower                                                 |
| genshi_xml                 | 33.9 ms                                                     | 35.1 ms: 1.04x slower                                                 |
| bench_mp_pool              | 84.2 ms                                                     | 88.0 ms: 1.04x slower                                                 |
| go                         | 84.7 ms                                                     | 88.5 ms: 1.05x slower                                                 |
| meteor_contest             | 72.0 ms                                                     | 75.5 ms: 1.05x slower                                                 |
| mako                       | 6.56 ms                                                     | 6.89 ms: 1.05x slower                                                 |
| bpe_tokeniser              | 2.87 sec                                                    | 3.02 sec: 1.05x slower                                                |
| crypto_pyaes               | 45.6 ms                                                     | 48.0 ms: 1.05x slower                                                 |
| dulwich_log                | 40.1 ms                                                     | 42.5 ms: 1.06x slower                                                 |
| pycparser                  | 695 ms                                                      | 737 ms: 1.06x slower                                                  |
| python_startup_no_site     | 16.9 ms                                                     | 18.0 ms: 1.06x slower                                                 |
| html5lib                   | 38.2 ms                                                     | 40.7 ms: 1.07x slower                                                 |
| sympy_expand               | 286 ms                                                      | 305 ms: 1.07x slower                                                  |
| fannkuch                   | 252 ms                                                      | 269 ms: 1.07x slower                                                  |
| scimark_fft                | 175 ms                                                      | 187 ms: 1.07x slower                                                  |
| sympy_sum                  | 85.2 ms                                                     | 91.3 ms: 1.07x slower                                                 |
| sympy_str                  | 167 ms                                                      | 179 ms: 1.07x slower                                                  |
| xml_etree_iterparse        | 60.5 ms                                                     | 65.2 ms: 1.08x slower                                                 |
| typing_runtime_protocols   | 103 us                                                      | 111 us: 1.08x slower                                                  |
| sphinx                     | 617 ms                                                      | 666 ms: 1.08x slower                                                  |
| 2to3                       | 215 ms                                                      | 233 ms: 1.08x slower                                                  |
| mdp                        | 1.43 sec                                                    | 1.56 sec: 1.09x slower                                                |
| genshi_text                | 15.2 ms                                                     | 16.6 ms: 1.09x slower                                                 |
| coverage                   | 45.3 ms                                                     | 49.4 ms: 1.09x slower                                                 |
| regex_compile              | 80.7 ms                                                     | 88.2 ms: 1.09x slower                                                 |
| pyflate                    | 283 ms                                                      | 310 ms: 1.09x slower                                                  |
| sqlite_synth               | 1.59 us                                                     | 1.74 us: 1.10x slower                                                 |
| json_dumps                 | 6.19 ms                                                     | 6.82 ms: 1.10x slower                                                 |
| chaos                      | 37.9 ms                                                     | 41.7 ms: 1.10x slower                                                 |
| sympy_integrate            | 12.3 ms                                                     | 13.6 ms: 1.10x slower                                                 |
| pprint_safe_repr           | 485 ms                                                      | 536 ms: 1.11x slower                                                  |
| docutils                   | 1.53 sec                                                    | 1.70 sec: 1.11x slower                                                |
| xml_etree_generate         | 53.5 ms                                                     | 59.4 ms: 1.11x slower                                                 |
| telco                      | 4.85 ms                                                     | 5.44 ms: 1.12x slower                                                 |
| pprint_pformat             | 977 ms                                                      | 1.10 sec: 1.12x slower                                                |
| sqlglot_optimize           | 32.5 ms                                                     | 36.7 ms: 1.13x slower                                                 |
| logging_simple             | 5.77 us                                                     | 6.53 us: 1.13x slower                                                 |
| logging_format             | 6.18 us                                                     | 6.99 us: 1.13x slower                                                 |
| generators                 | 19.0 ms                                                     | 21.6 ms: 1.14x slower                                                 |
| scimark_lu                 | 56.7 ms                                                     | 64.9 ms: 1.14x slower                                                 |
| nqueens                    | 56.1 ms                                                     | 64.6 ms: 1.15x slower                                                 |
| scimark_sor                | 76.2 ms                                                     | 87.8 ms: 1.15x slower                                                 |
| sqlglot_transpile          | 953 us                                                      | 1.10 ms: 1.15x slower                                                 |
| sqlglot_normalize          | 172 ms                                                      | 199 ms: 1.16x slower                                                  |
| scimark_monte_carlo        | 40.7 ms                                                     | 47.3 ms: 1.16x slower                                                 |
| sqlglot_parse              | 764 us                                                      | 890 us: 1.16x slower                                                  |
| nbody                      | 66.3 ms                                                     | 77.3 ms: 1.17x slower                                                 |
| hexiom                     | 3.84 ms                                                     | 4.54 ms: 1.18x slower                                                 |
| xml_etree_process          | 36.5 ms                                                     | 43.7 ms: 1.20x slower                                                 |
| comprehensions             | 10.4 us                                                     | 12.4 us: 1.20x slower                                                 |
| richards_super             | 29.8 ms                                                     | 35.8 ms: 1.20x slower                                                 |
| many_optionals             | 361 us                                                      | 437 us: 1.21x slower                                                  |
| richards                   | 26.3 ms                                                     | 31.8 ms: 1.21x slower                                                 |
| unpickle_pure_python       | 130 us                                                      | 159 us: 1.22x slower                                                  |
| coroutines                 | 12.5 ms                                                     | 15.3 ms: 1.22x slower                                                 |
| deltablue                  | 1.89 ms                                                     | 2.38 ms: 1.26x slower                                                 |
| django_template            | 20.3 ms                                                     | 25.9 ms: 1.28x slower                                                 |
| pickle_pure_python         | 186 us                                                      | 239 us: 1.29x slower                                                  |
| logging_silent             | 54.6 ns                                                     | 72.5 ns: 1.33x slower                                                 |
| raytrace                   | 153 ms                                                      | 209 ms: 1.37x slower                                                  |
| subparsers                 | 10.9 ms                                                     | 16.1 ms: 1.48x slower                                                 |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                          |

Benchmark hidden because not significant (7): pylint, asyncio_websockets, create_gc_cycles, python_startup, spectral_norm, connected_components, gc_traversal
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http

- Geometric mean (including insignificant results): 1.022x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: unknown