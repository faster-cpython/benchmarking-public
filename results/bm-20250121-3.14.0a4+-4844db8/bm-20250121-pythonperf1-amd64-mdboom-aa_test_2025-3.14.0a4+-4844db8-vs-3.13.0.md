# Results vs. 3.13.0

- fork: mdboom
- ref: aa_test_2025
- machine: windows-amd64
- commit hash: 4844db8
- commit date: 2025-01-21
- overall geometric mean: 1.023x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-pythonperf1-amd64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 232 ms: 1.08x slower                                                |
| docutils       | 1.53 sec                                                    | 1.69 sec: 1.10x slower                                              |
| html5lib       | 38.2 ms                                                     | 40.6 ms: 1.06x slower                                               |
| sphinx         | 617 ms                                                      | 662 ms: 1.07x slower                                                |
| Geometric mean | (ref)                                                       | 1.08x slower                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-pythonperf1-amd64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 213 ms: 1.32x faster                                                |
| async_tree_io              | 513 ms                                                      | 414 ms: 1.24x faster                                                |
| async_tree_io_tg           | 497 ms                                                      | 402 ms: 1.24x faster                                                |
| async_tree_none            | 219 ms                                                      | 186 ms: 1.18x faster                                                |
| async_tree_memoization     | 265 ms                                                      | 226 ms: 1.17x faster                                                |
| async_tree_none_tg         | 200 ms                                                      | 174 ms: 1.15x faster                                                |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 346 ms: 1.11x faster                                                |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 348 ms: 1.09x faster                                                |
| asyncio_websockets         | 300 ms                                                      | 284 ms: 1.06x faster                                                |
| async_generators           | 223 ms                                                      | 231 ms: 1.04x slower                                                |
| coroutines                 | 12.5 ms                                                     | 14.8 ms: 1.18x slower                                               |
| Geometric mean             | (ref)                                                       | 1.12x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-pythonperf1-amd64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 146 ms                                                      | 146 ms: 1.00x faster                                                |
| float          | 50.8 ms                                                     | 51.6 ms: 1.02x slower                                               |
| nbody          | 66.3 ms                                                     | 74.5 ms: 1.12x slower                                               |
| Geometric mean | (ref)                                                       | 1.04x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-pythonperf1-amd64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.8 ms: 1.61x faster                                               |
| regex_effbot   | 1.69 ms                                                     | 1.47 ms: 1.15x faster                                               |
| regex_compile  | 80.7 ms                                                     | 87.9 ms: 1.09x slower                                               |
| Geometric mean | (ref)                                                       | 1.14x faster                                                        |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-pythonperf1-amd64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.4 us: 1.05x faster                                               |
| xml_etree_parse      | 92.2 ms                                                     | 89.4 ms: 1.03x faster                                               |
| tomli_loads          | 1.37 sec                                                    | 1.40 sec: 1.02x slower                                              |
| xml_etree_iterparse  | 60.5 ms                                                     | 65.0 ms: 1.07x slower                                               |
| json_dumps           | 6.19 ms                                                     | 6.89 ms: 1.11x slower                                               |
| xml_etree_generate   | 53.5 ms                                                     | 60.3 ms: 1.13x slower                                               |
| xml_etree_process    | 36.5 ms                                                     | 43.3 ms: 1.19x slower                                               |
| unpickle_pure_python | 130 us                                                      | 162 us: 1.24x slower                                                |
| pickle_pure_python   | 186 us                                                      | 238 us: 1.28x slower                                                |
| Geometric mean       | (ref)                                                       | 1.10x slower                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-pythonperf1-amd64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 16.9 ms                                                     | 18.2 ms: 1.07x slower                                               |
| Geometric mean         | (ref)                                                       | 1.04x slower                                                        |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-pythonperf1-amd64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 35.7 ms: 1.05x slower                                               |
| mako            | 6.56 ms                                                     | 6.97 ms: 1.06x slower                                               |
| genshi_text     | 15.2 ms                                                     | 16.5 ms: 1.09x slower                                               |
| django_template | 20.3 ms                                                     | 25.9 ms: 1.28x slower                                               |
| Geometric mean  | (ref)                                                       | 1.12x slower                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-pythonperf1-amd64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 519 us: 16.31x faster                                               |
| regex_v8                   | 23.8 ms                                                     | 14.8 ms: 1.61x faster                                               |
| async_tree_memoization_tg  | 281 ms                                                      | 213 ms: 1.32x faster                                                |
| async_tree_io              | 513 ms                                                      | 414 ms: 1.24x faster                                                |
| async_tree_io_tg           | 497 ms                                                      | 402 ms: 1.24x faster                                                |
| deepcopy                   | 223 us                                                      | 189 us: 1.18x faster                                                |
| async_tree_none            | 219 ms                                                      | 186 ms: 1.18x faster                                                |
| async_tree_memoization     | 265 ms                                                      | 226 ms: 1.17x faster                                                |
| regex_effbot               | 1.69 ms                                                     | 1.47 ms: 1.15x faster                                               |
| async_tree_none_tg         | 200 ms                                                      | 174 ms: 1.15x faster                                                |
| deepcopy_memo              | 23.1 us                                                     | 20.3 us: 1.14x faster                                               |
| json                       | 3.30 ms                                                     | 2.93 ms: 1.13x faster                                               |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 346 ms: 1.11x faster                                                |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 348 ms: 1.09x faster                                                |
| deepcopy_reduce            | 2.02 us                                                     | 1.89 us: 1.07x faster                                               |
| asyncio_websockets         | 300 ms                                                      | 284 ms: 1.06x faster                                                |
| json_loads                 | 15.1 us                                                     | 14.4 us: 1.05x faster                                               |
| xml_etree_parse            | 92.2 ms                                                     | 89.4 ms: 1.03x faster                                               |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.56 ms: 1.02x faster                                               |
| create_gc_cycles           | 1.22 ms                                                     | 1.21 ms: 1.01x faster                                               |
| telco                      | 4.85 ms                                                     | 4.81 ms: 1.01x faster                                               |
| pidigits                   | 146 ms                                                      | 146 ms: 1.00x faster                                                |
| spectral_norm              | 63.4 ms                                                     | 63.7 ms: 1.00x slower                                               |
| sqlite_synth               | 1.59 us                                                     | 1.60 us: 1.01x slower                                               |
| float                      | 50.8 ms                                                     | 51.6 ms: 1.02x slower                                               |
| tomli_loads                | 1.37 sec                                                    | 1.40 sec: 1.02x slower                                              |
| async_generators           | 223 ms                                                      | 231 ms: 1.04x slower                                                |
| pathlib                    | 75.3 ms                                                     | 78.3 ms: 1.04x slower                                               |
| go                         | 84.7 ms                                                     | 88.3 ms: 1.04x slower                                               |
| bench_mp_pool              | 84.2 ms                                                     | 88.2 ms: 1.05x slower                                               |
| genshi_xml                 | 33.9 ms                                                     | 35.7 ms: 1.05x slower                                               |
| meteor_contest             | 72.0 ms                                                     | 76.0 ms: 1.06x slower                                               |
| bench_thread_pool          | 810 us                                                      | 856 us: 1.06x slower                                                |
| bpe_tokeniser              | 2.87 sec                                                    | 3.04 sec: 1.06x slower                                              |
| pycparser                  | 695 ms                                                      | 736 ms: 1.06x slower                                                |
| mako                       | 6.56 ms                                                     | 6.97 ms: 1.06x slower                                               |
| dulwich_log                | 40.1 ms                                                     | 42.6 ms: 1.06x slower                                               |
| html5lib                   | 38.2 ms                                                     | 40.6 ms: 1.06x slower                                               |
| coverage                   | 45.3 ms                                                     | 48.3 ms: 1.07x slower                                               |
| crypto_pyaes               | 45.6 ms                                                     | 48.7 ms: 1.07x slower                                               |
| sympy_sum                  | 85.2 ms                                                     | 91.2 ms: 1.07x slower                                               |
| sphinx                     | 617 ms                                                      | 662 ms: 1.07x slower                                                |
| python_startup_no_site     | 16.9 ms                                                     | 18.2 ms: 1.07x slower                                               |
| xml_etree_iterparse        | 60.5 ms                                                     | 65.0 ms: 1.07x slower                                               |
| 2to3                       | 215 ms                                                      | 232 ms: 1.08x slower                                                |
| sympy_str                  | 167 ms                                                      | 180 ms: 1.08x slower                                                |
| sympy_expand               | 286 ms                                                      | 310 ms: 1.08x slower                                                |
| genshi_text                | 15.2 ms                                                     | 16.5 ms: 1.09x slower                                               |
| regex_compile              | 80.7 ms                                                     | 87.9 ms: 1.09x slower                                               |
| mdp                        | 1.43 sec                                                    | 1.56 sec: 1.09x slower                                              |
| fannkuch                   | 252 ms                                                      | 277 ms: 1.10x slower                                                |
| sympy_integrate            | 12.3 ms                                                     | 13.6 ms: 1.10x slower                                               |
| logging_format             | 6.18 us                                                     | 6.81 us: 1.10x slower                                               |
| docutils                   | 1.53 sec                                                    | 1.69 sec: 1.10x slower                                              |
| pyflate                    | 283 ms                                                      | 312 ms: 1.10x slower                                                |
| pprint_safe_repr           | 485 ms                                                      | 535 ms: 1.10x slower                                                |
| json_dumps                 | 6.19 ms                                                     | 6.89 ms: 1.11x slower                                               |
| logging_simple             | 5.77 us                                                     | 6.43 us: 1.11x slower                                               |
| sqlglot_optimize           | 32.5 ms                                                     | 36.3 ms: 1.12x slower                                               |
| typing_runtime_protocols   | 103 us                                                      | 115 us: 1.12x slower                                                |
| pprint_pformat             | 977 ms                                                      | 1.09 sec: 1.12x slower                                              |
| nbody                      | 66.3 ms                                                     | 74.5 ms: 1.12x slower                                               |
| xml_etree_generate         | 53.5 ms                                                     | 60.3 ms: 1.13x slower                                               |
| scimark_fft                | 175 ms                                                      | 198 ms: 1.13x slower                                                |
| generators                 | 19.0 ms                                                     | 21.5 ms: 1.13x slower                                               |
| chaos                      | 37.9 ms                                                     | 42.9 ms: 1.13x slower                                               |
| sqlglot_normalize          | 172 ms                                                      | 197 ms: 1.15x slower                                                |
| sqlglot_transpile          | 953 us                                                      | 1.10 ms: 1.16x slower                                               |
| nqueens                    | 56.1 ms                                                     | 65.2 ms: 1.16x slower                                               |
| sqlglot_parse              | 764 us                                                      | 891 us: 1.17x slower                                                |
| scimark_sor                | 76.2 ms                                                     | 89.6 ms: 1.18x slower                                               |
| coroutines                 | 12.5 ms                                                     | 14.8 ms: 1.18x slower                                               |
| xml_etree_process          | 36.5 ms                                                     | 43.3 ms: 1.19x slower                                               |
| hexiom                     | 3.84 ms                                                     | 4.60 ms: 1.20x slower                                               |
| many_optionals             | 361 us                                                      | 437 us: 1.21x slower                                                |
| comprehensions             | 10.4 us                                                     | 12.6 us: 1.21x slower                                               |
| richards_super             | 29.8 ms                                                     | 36.3 ms: 1.22x slower                                               |
| scimark_monte_carlo        | 40.7 ms                                                     | 49.9 ms: 1.23x slower                                               |
| scimark_lu                 | 56.7 ms                                                     | 69.8 ms: 1.23x slower                                               |
| richards                   | 26.3 ms                                                     | 32.3 ms: 1.23x slower                                               |
| unpickle_pure_python       | 130 us                                                      | 162 us: 1.24x slower                                                |
| deltablue                  | 1.89 ms                                                     | 2.37 ms: 1.25x slower                                               |
| django_template            | 20.3 ms                                                     | 25.9 ms: 1.28x slower                                               |
| pickle_pure_python         | 186 us                                                      | 238 us: 1.28x slower                                                |
| logging_silent             | 54.6 ns                                                     | 69.9 ns: 1.28x slower                                               |
| raytrace                   | 153 ms                                                      | 214 ms: 1.39x slower                                                |
| subparsers                 | 10.9 ms                                                     | 16.0 ms: 1.47x slower                                               |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                        |

Benchmark hidden because not significant (7): pylint, connected_components, shortest_path, regex_dna, python_startup, k_core, gc_traversal
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http

- Geometric mean (including insignificant results): 1.023x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown