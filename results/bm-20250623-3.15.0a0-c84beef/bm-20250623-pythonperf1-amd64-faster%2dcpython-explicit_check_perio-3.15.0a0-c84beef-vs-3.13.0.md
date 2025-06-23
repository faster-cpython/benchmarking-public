# Results vs. 3.13.0

- fork: faster-cpython
- ref: explicit_check_perio
- machine: windows-amd64
- commit hash: c84beef
- commit date: 2025-06-23
- overall geometric mean: 1.028x faster
- HPT reliability: 99.51%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 226 ms: 1.05x slower                                                                 |
| docutils       | 1.53 sec                                                    | 1.65 sec: 1.08x slower                                                               |
| html5lib       | 38.2 ms                                                     | 40.7 ms: 1.07x slower                                                                |
| sphinx         | 617 ms                                                      | 655 ms: 1.06x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.06x slower                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 157 ms: 1.91x faster                                                                 |
| async_tree_memoization_tg  | 281 ms                                                      | 226 ms: 1.24x faster                                                                 |
| async_tree_io              | 513 ms                                                      | 424 ms: 1.21x faster                                                                 |
| async_tree_io_tg           | 497 ms                                                      | 418 ms: 1.19x faster                                                                 |
| async_tree_none            | 219 ms                                                      | 188 ms: 1.17x faster                                                                 |
| async_tree_memoization     | 265 ms                                                      | 228 ms: 1.16x faster                                                                 |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 345 ms: 1.10x faster                                                                 |
| async_tree_none_tg         | 200 ms                                                      | 183 ms: 1.09x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 351 ms: 1.09x faster                                                                 |
| async_generators           | 223 ms                                                      | 235 ms: 1.06x slower                                                                 |
| coroutines                 | 12.5 ms                                                     | 14.4 ms: 1.16x slower                                                                |
| Geometric mean             | (ref)                                                       | 1.16x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 46.1 ms: 1.10x faster                                                                |
| nbody          | 66.3 ms                                                     | 65.2 ms: 1.02x faster                                                                |
| Geometric mean | (ref)                                                       | 1.04x faster                                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.0 ms: 1.71x faster                                                                |
| regex_effbot   | 1.69 ms                                                     | 1.59 ms: 1.07x faster                                                                |
| regex_compile  | 80.7 ms                                                     | 84.1 ms: 1.04x slower                                                                |
| regex_dna      | 115 ms                                                      | 121 ms: 1.05x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.13x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.4 us: 1.05x faster                                                                |
| xml_etree_parse      | 92.2 ms                                                     | 88.2 ms: 1.05x faster                                                                |
| json_dumps           | 6.19 ms                                                     | 6.27 ms: 1.01x slower                                                                |
| tomli_loads          | 1.37 sec                                                    | 1.41 sec: 1.03x slower                                                               |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.1 ms: 1.04x slower                                                                |
| xml_etree_generate   | 53.5 ms                                                     | 56.4 ms: 1.06x slower                                                                |
| unpickle_pure_python | 130 us                                                      | 142 us: 1.09x slower                                                                 |
| xml_etree_process    | 36.5 ms                                                     | 40.1 ms: 1.10x slower                                                                |
| pickle_pure_python   | 186 us                                                      | 222 us: 1.19x slower                                                                 |
| Geometric mean       | (ref)                                                       | 1.05x slower                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.0 ms: 1.07x slower                                                                |
| python_startup_no_site | 16.9 ms                                                     | 19.5 ms: 1.15x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.78 ms: 1.03x slower                                                                |
| genshi_text     | 15.2 ms                                                     | 16.5 ms: 1.08x slower                                                                |
| genshi_xml      | 33.9 ms                                                     | 37.5 ms: 1.11x slower                                                                |
| django_template | 20.3 ms                                                     | 25.1 ms: 1.24x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.11x slower                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 495 us: 17.09x faster                                                                |
| pathlib                    | 75.3 ms                                                     | 31.6 ms: 2.38x faster                                                                |
| asyncio_websockets         | 300 ms                                                      | 157 ms: 1.91x faster                                                                 |
| mdp                        | 1.43 sec                                                    | 835 ms: 1.71x faster                                                                 |
| regex_v8                   | 23.8 ms                                                     | 14.0 ms: 1.71x faster                                                                |
| deepcopy                   | 223 us                                                      | 178 us: 1.25x faster                                                                 |
| async_tree_memoization_tg  | 281 ms                                                      | 226 ms: 1.24x faster                                                                 |
| deepcopy_memo              | 23.1 us                                                     | 18.9 us: 1.22x faster                                                                |
| async_tree_io              | 513 ms                                                      | 424 ms: 1.21x faster                                                                 |
| async_tree_io_tg           | 497 ms                                                      | 418 ms: 1.19x faster                                                                 |
| async_tree_none            | 219 ms                                                      | 188 ms: 1.17x faster                                                                 |
| async_tree_memoization     | 265 ms                                                      | 228 ms: 1.16x faster                                                                 |
| float                      | 50.8 ms                                                     | 46.1 ms: 1.10x faster                                                                |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 345 ms: 1.10x faster                                                                 |
| json                       | 3.30 ms                                                     | 3.01 ms: 1.10x faster                                                                |
| async_tree_none_tg         | 200 ms                                                      | 183 ms: 1.09x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 351 ms: 1.09x faster                                                                 |
| go                         | 84.7 ms                                                     | 79.3 ms: 1.07x faster                                                                |
| regex_effbot               | 1.69 ms                                                     | 1.59 ms: 1.07x faster                                                                |
| deepcopy_reduce            | 2.02 us                                                     | 1.90 us: 1.06x faster                                                                |
| telco                      | 4.85 ms                                                     | 4.60 ms: 1.06x faster                                                                |
| json_loads                 | 15.1 us                                                     | 14.4 us: 1.05x faster                                                                |
| xml_etree_parse            | 92.2 ms                                                     | 88.2 ms: 1.05x faster                                                                |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.53 ms: 1.03x faster                                                                |
| spectral_norm              | 63.4 ms                                                     | 62.1 ms: 1.02x faster                                                                |
| nbody                      | 66.3 ms                                                     | 65.2 ms: 1.02x faster                                                                |
| scimark_sor                | 76.2 ms                                                     | 75.2 ms: 1.01x faster                                                                |
| json_dumps                 | 6.19 ms                                                     | 6.27 ms: 1.01x slower                                                                |
| scimark_monte_carlo        | 40.7 ms                                                     | 41.5 ms: 1.02x slower                                                                |
| shortest_path              | 355 ms                                                      | 365 ms: 1.03x slower                                                                 |
| tomli_loads                | 1.37 sec                                                    | 1.41 sec: 1.03x slower                                                               |
| fannkuch                   | 252 ms                                                      | 259 ms: 1.03x slower                                                                 |
| mako                       | 6.56 ms                                                     | 6.78 ms: 1.03x slower                                                                |
| typing_runtime_protocols   | 103 us                                                      | 107 us: 1.04x slower                                                                 |
| meteor_contest             | 72.0 ms                                                     | 74.9 ms: 1.04x slower                                                                |
| pyflate                    | 283 ms                                                      | 295 ms: 1.04x slower                                                                 |
| regex_compile              | 80.7 ms                                                     | 84.1 ms: 1.04x slower                                                                |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.1 ms: 1.04x slower                                                                |
| connected_components       | 320 ms                                                      | 334 ms: 1.04x slower                                                                 |
| sympy_integrate            | 12.3 ms                                                     | 12.9 ms: 1.05x slower                                                                |
| 2to3                       | 215 ms                                                      | 226 ms: 1.05x slower                                                                 |
| regex_dna                  | 115 ms                                                      | 121 ms: 1.05x slower                                                                 |
| bpe_tokeniser              | 2.87 sec                                                    | 3.03 sec: 1.05x slower                                                               |
| dulwich_log                | 40.1 ms                                                     | 42.3 ms: 1.05x slower                                                                |
| async_generators           | 223 ms                                                      | 235 ms: 1.06x slower                                                                 |
| xml_etree_generate         | 53.5 ms                                                     | 56.4 ms: 1.06x slower                                                                |
| sympy_expand               | 286 ms                                                      | 302 ms: 1.06x slower                                                                 |
| sympy_str                  | 167 ms                                                      | 176 ms: 1.06x slower                                                                 |
| scimark_fft                | 175 ms                                                      | 185 ms: 1.06x slower                                                                 |
| sphinx                     | 617 ms                                                      | 655 ms: 1.06x slower                                                                 |
| scimark_lu                 | 56.7 ms                                                     | 60.1 ms: 1.06x slower                                                                |
| pycparser                  | 695 ms                                                      | 739 ms: 1.06x slower                                                                 |
| html5lib                   | 38.2 ms                                                     | 40.7 ms: 1.07x slower                                                                |
| comprehensions             | 10.4 us                                                     | 11.0 us: 1.07x slower                                                                |
| sympy_sum                  | 85.2 ms                                                     | 90.8 ms: 1.07x slower                                                                |
| python_startup             | 24.4 ms                                                     | 26.0 ms: 1.07x slower                                                                |
| generators                 | 19.0 ms                                                     | 20.5 ms: 1.08x slower                                                                |
| docutils                   | 1.53 sec                                                    | 1.65 sec: 1.08x slower                                                               |
| chaos                      | 37.9 ms                                                     | 41.0 ms: 1.08x slower                                                                |
| genshi_text                | 15.2 ms                                                     | 16.5 ms: 1.08x slower                                                                |
| create_gc_cycles           | 1.22 ms                                                     | 1.33 ms: 1.08x slower                                                                |
| richards                   | 26.3 ms                                                     | 28.5 ms: 1.09x slower                                                                |
| gc_traversal               | 1.96 ms                                                     | 2.14 ms: 1.09x slower                                                                |
| crypto_pyaes               | 45.6 ms                                                     | 49.8 ms: 1.09x slower                                                                |
| unpickle_pure_python       | 130 us                                                      | 142 us: 1.09x slower                                                                 |
| richards_super             | 29.8 ms                                                     | 32.6 ms: 1.10x slower                                                                |
| coverage                   | 45.3 ms                                                     | 49.7 ms: 1.10x slower                                                                |
| xml_etree_process          | 36.5 ms                                                     | 40.1 ms: 1.10x slower                                                                |
| hexiom                     | 3.84 ms                                                     | 4.25 ms: 1.10x slower                                                                |
| genshi_xml                 | 33.9 ms                                                     | 37.5 ms: 1.11x slower                                                                |
| logging_simple             | 5.77 us                                                     | 6.62 us: 1.15x slower                                                                |
| nqueens                    | 56.1 ms                                                     | 64.7 ms: 1.15x slower                                                                |
| python_startup_no_site     | 16.9 ms                                                     | 19.5 ms: 1.15x slower                                                                |
| coroutines                 | 12.5 ms                                                     | 14.4 ms: 1.16x slower                                                                |
| logging_format             | 6.18 us                                                     | 7.14 us: 1.16x slower                                                                |
| pprint_safe_repr           | 485 ms                                                      | 566 ms: 1.17x slower                                                                 |
| deltablue                  | 1.89 ms                                                     | 2.24 ms: 1.18x slower                                                                |
| pickle_pure_python         | 186 us                                                      | 222 us: 1.19x slower                                                                 |
| pprint_pformat             | 977 ms                                                      | 1.17 sec: 1.20x slower                                                               |
| raytrace                   | 153 ms                                                      | 189 ms: 1.23x slower                                                                 |
| django_template            | 20.3 ms                                                     | 25.1 ms: 1.24x slower                                                                |
| many_optionals             | 361 us                                                      | 452 us: 1.25x slower                                                                 |
| subparsers                 | 10.9 ms                                                     | 17.5 ms: 1.61x slower                                                                |
| logging_silent             | 54.6 ns                                                     | 323 ns: 5.91x slower                                                                 |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                                         |

Benchmark hidden because not significant (4): pylint, sqlite_synth, pidigits, k_core
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250623-3.15.0a0-c84beef/bm-20250623-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.028x faster

# HPT report

- Reliability score: 99.51% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown