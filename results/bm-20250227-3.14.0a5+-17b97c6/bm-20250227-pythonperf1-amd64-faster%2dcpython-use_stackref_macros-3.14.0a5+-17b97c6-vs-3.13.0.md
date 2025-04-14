# Results vs. 3.13.0

- fork: faster-cpython
- ref: use_stackref_macros
- machine: windows-amd64
- commit hash: 17b97c6
- commit date: 2025-02-27
- overall geometric mean: 1.001x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250227-pythonperf1-amd64-faster%2dcpython-use_stackref_macros-3.14.0a5+-17b97c6 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 227 ms: 1.06x slower                                                                 |
| docutils       | 1.53 sec                                                    | 1.69 sec: 1.10x slower                                                               |
| html5lib       | 38.2 ms                                                     | 41.2 ms: 1.08x slower                                                                |
| sphinx         | 617 ms                                                      | 654 ms: 1.06x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.07x slower                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250227-pythonperf1-amd64-faster%2dcpython-use_stackref_macros-3.14.0a5+-17b97c6 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 216 ms: 1.30x faster                                                                 |
| async_tree_io              | 513 ms                                                      | 420 ms: 1.22x faster                                                                 |
| async_tree_io_tg           | 497 ms                                                      | 412 ms: 1.20x faster                                                                 |
| async_tree_memoization     | 265 ms                                                      | 223 ms: 1.19x faster                                                                 |
| async_tree_none            | 219 ms                                                      | 190 ms: 1.15x faster                                                                 |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 341 ms: 1.12x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 344 ms: 1.11x faster                                                                 |
| async_tree_none_tg         | 200 ms                                                      | 180 ms: 1.11x faster                                                                 |
| asyncio_websockets         | 300 ms                                                      | 308 ms: 1.03x slower                                                                 |
| async_generators           | 223 ms                                                      | 229 ms: 1.03x slower                                                                 |
| coroutines                 | 12.5 ms                                                     | 13.8 ms: 1.11x slower                                                                |
| Geometric mean             | (ref)                                                       | 1.11x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250227-pythonperf1-amd64-faster%2dcpython-use_stackref_macros-3.14.0a5+-17b97c6 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 46.8 ms: 1.09x faster                                                                |
| nbody          | 66.3 ms                                                     | 65.5 ms: 1.01x faster                                                                |
| pidigits       | 146 ms                                                      | 150 ms: 1.03x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250227-pythonperf1-amd64-faster%2dcpython-use_stackref_macros-3.14.0a5+-17b97c6 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.3 ms: 1.67x faster                                                                |
| regex_effbot   | 1.69 ms                                                     | 1.41 ms: 1.20x faster                                                                |
| regex_dna      | 115 ms                                                      | 112 ms: 1.03x faster                                                                 |
| regex_compile  | 80.7 ms                                                     | 87.2 ms: 1.08x slower                                                                |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250227-pythonperf1-amd64-faster%2dcpython-use_stackref_macros-3.14.0a5+-17b97c6 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 89.8 ms: 1.03x faster                                                                |
| tomli_loads          | 1.37 sec                                                    | 1.43 sec: 1.04x slower                                                               |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.3 ms: 1.05x slower                                                                |
| xml_etree_generate   | 53.5 ms                                                     | 57.6 ms: 1.08x slower                                                                |
| json_dumps           | 6.19 ms                                                     | 6.87 ms: 1.11x slower                                                                |
| xml_etree_process    | 36.5 ms                                                     | 41.1 ms: 1.13x slower                                                                |
| unpickle_pure_python | 130 us                                                      | 151 us: 1.16x slower                                                                 |
| pickle_pure_python   | 186 us                                                      | 230 us: 1.24x slower                                                                 |
| Geometric mean       | (ref)                                                       | 1.08x slower                                                                         |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250227-pythonperf1-amd64-faster%2dcpython-use_stackref_macros-3.14.0a5+-17b97c6 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.1 ms: 1.07x slower                                                                |
| python_startup_no_site | 16.9 ms                                                     | 19.7 ms: 1.16x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250227-pythonperf1-amd64-faster%2dcpython-use_stackref_macros-3.14.0a5+-17b97c6 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 7.07 ms: 1.08x slower                                                                |
| genshi_xml      | 33.9 ms                                                     | 38.1 ms: 1.12x slower                                                                |
| genshi_text     | 15.2 ms                                                     | 17.3 ms: 1.14x slower                                                                |
| django_template | 20.3 ms                                                     | 26.2 ms: 1.29x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.15x slower                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250227-pythonperf1-amd64-faster%2dcpython-use_stackref_macros-3.14.0a5+-17b97c6 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 528 us: 16.05x faster                                                                |
| pathlib                    | 75.3 ms                                                     | 32.1 ms: 2.34x faster                                                                |
| regex_v8                   | 23.8 ms                                                     | 14.3 ms: 1.67x faster                                                                |
| async_tree_memoization_tg  | 281 ms                                                      | 216 ms: 1.30x faster                                                                 |
| async_tree_io              | 513 ms                                                      | 420 ms: 1.22x faster                                                                 |
| deepcopy                   | 223 us                                                      | 184 us: 1.22x faster                                                                 |
| deepcopy_memo              | 23.1 us                                                     | 19.1 us: 1.21x faster                                                                |
| async_tree_io_tg           | 497 ms                                                      | 412 ms: 1.20x faster                                                                 |
| regex_effbot               | 1.69 ms                                                     | 1.41 ms: 1.20x faster                                                                |
| async_tree_memoization     | 265 ms                                                      | 223 ms: 1.19x faster                                                                 |
| async_tree_none            | 219 ms                                                      | 190 ms: 1.15x faster                                                                 |
| spectral_norm              | 63.4 ms                                                     | 56.7 ms: 1.12x faster                                                                |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 341 ms: 1.12x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 344 ms: 1.11x faster                                                                 |
| async_tree_none_tg         | 200 ms                                                      | 180 ms: 1.11x faster                                                                 |
| json                       | 3.30 ms                                                     | 3.02 ms: 1.09x faster                                                                |
| float                      | 50.8 ms                                                     | 46.8 ms: 1.09x faster                                                                |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.46 ms: 1.06x faster                                                                |
| deepcopy_reduce            | 2.02 us                                                     | 1.95 us: 1.04x faster                                                                |
| regex_dna                  | 115 ms                                                      | 112 ms: 1.03x faster                                                                 |
| xml_etree_parse            | 92.2 ms                                                     | 89.8 ms: 1.03x faster                                                                |
| nbody                      | 66.3 ms                                                     | 65.5 ms: 1.01x faster                                                                |
| telco                      | 4.85 ms                                                     | 4.88 ms: 1.01x slower                                                                |
| sqlite_synth               | 1.59 us                                                     | 1.60 us: 1.01x slower                                                                |
| shortest_path              | 355 ms                                                      | 363 ms: 1.02x slower                                                                 |
| generators                 | 19.0 ms                                                     | 19.4 ms: 1.02x slower                                                                |
| pidigits                   | 146 ms                                                      | 150 ms: 1.03x slower                                                                 |
| asyncio_websockets         | 300 ms                                                      | 308 ms: 1.03x slower                                                                 |
| k_core                     | 1.70 sec                                                    | 1.74 sec: 1.03x slower                                                               |
| async_generators           | 223 ms                                                      | 229 ms: 1.03x slower                                                                 |
| bench_mp_pool              | 84.2 ms                                                     | 86.6 ms: 1.03x slower                                                                |
| bpe_tokeniser              | 2.87 sec                                                    | 2.97 sec: 1.04x slower                                                               |
| tomli_loads                | 1.37 sec                                                    | 1.43 sec: 1.04x slower                                                               |
| connected_components       | 320 ms                                                      | 334 ms: 1.04x slower                                                                 |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.3 ms: 1.05x slower                                                                |
| mdp                        | 1.43 sec                                                    | 1.50 sec: 1.05x slower                                                               |
| scimark_fft                | 175 ms                                                      | 184 ms: 1.05x slower                                                                 |
| coverage                   | 45.3 ms                                                     | 47.6 ms: 1.05x slower                                                                |
| go                         | 84.7 ms                                                     | 89.3 ms: 1.05x slower                                                                |
| 2to3                       | 215 ms                                                      | 227 ms: 1.06x slower                                                                 |
| typing_runtime_protocols   | 103 us                                                      | 109 us: 1.06x slower                                                                 |
| scimark_lu                 | 56.7 ms                                                     | 59.9 ms: 1.06x slower                                                                |
| scimark_sor                | 76.2 ms                                                     | 80.5 ms: 1.06x slower                                                                |
| sympy_str                  | 167 ms                                                      | 177 ms: 1.06x slower                                                                 |
| sphinx                     | 617 ms                                                      | 654 ms: 1.06x slower                                                                 |
| bench_thread_pool          | 810 us                                                      | 860 us: 1.06x slower                                                                 |
| sympy_sum                  | 85.2 ms                                                     | 90.5 ms: 1.06x slower                                                                |
| meteor_contest             | 72.0 ms                                                     | 76.9 ms: 1.07x slower                                                                |
| sympy_expand               | 286 ms                                                      | 305 ms: 1.07x slower                                                                 |
| python_startup             | 24.4 ms                                                     | 26.1 ms: 1.07x slower                                                                |
| pycparser                  | 695 ms                                                      | 744 ms: 1.07x slower                                                                 |
| mako                       | 6.56 ms                                                     | 7.07 ms: 1.08x slower                                                                |
| xml_etree_generate         | 53.5 ms                                                     | 57.6 ms: 1.08x slower                                                                |
| sympy_integrate            | 12.3 ms                                                     | 13.3 ms: 1.08x slower                                                                |
| html5lib                   | 38.2 ms                                                     | 41.2 ms: 1.08x slower                                                                |
| scimark_monte_carlo        | 40.7 ms                                                     | 44.0 ms: 1.08x slower                                                                |
| regex_compile              | 80.7 ms                                                     | 87.2 ms: 1.08x slower                                                                |
| dulwich_log                | 40.1 ms                                                     | 43.4 ms: 1.08x slower                                                                |
| pyflate                    | 283 ms                                                      | 306 ms: 1.08x slower                                                                 |
| fannkuch                   | 252 ms                                                      | 273 ms: 1.08x slower                                                                 |
| logging_silent             | 54.6 ns                                                     | 59.7 ns: 1.09x slower                                                                |
| docutils                   | 1.53 sec                                                    | 1.69 sec: 1.10x slower                                                               |
| coroutines                 | 12.5 ms                                                     | 13.8 ms: 1.11x slower                                                                |
| json_dumps                 | 6.19 ms                                                     | 6.87 ms: 1.11x slower                                                                |
| sqlglot_optimize           | 32.5 ms                                                     | 36.2 ms: 1.11x slower                                                                |
| genshi_xml                 | 33.9 ms                                                     | 38.1 ms: 1.12x slower                                                                |
| crypto_pyaes               | 45.6 ms                                                     | 51.3 ms: 1.13x slower                                                                |
| logging_format             | 6.18 us                                                     | 6.95 us: 1.13x slower                                                                |
| xml_etree_process          | 36.5 ms                                                     | 41.1 ms: 1.13x slower                                                                |
| logging_simple             | 5.77 us                                                     | 6.50 us: 1.13x slower                                                                |
| pprint_safe_repr           | 485 ms                                                      | 546 ms: 1.13x slower                                                                 |
| pprint_pformat             | 977 ms                                                      | 1.10 sec: 1.13x slower                                                               |
| genshi_text                | 15.2 ms                                                     | 17.3 ms: 1.14x slower                                                                |
| hexiom                     | 3.84 ms                                                     | 4.38 ms: 1.14x slower                                                                |
| sqlglot_normalize          | 172 ms                                                      | 196 ms: 1.14x slower                                                                 |
| richards_super             | 29.8 ms                                                     | 34.1 ms: 1.15x slower                                                                |
| richards                   | 26.3 ms                                                     | 30.2 ms: 1.15x slower                                                                |
| unpickle_pure_python       | 130 us                                                      | 151 us: 1.16x slower                                                                 |
| nqueens                    | 56.1 ms                                                     | 65.0 ms: 1.16x slower                                                                |
| python_startup_no_site     | 16.9 ms                                                     | 19.7 ms: 1.16x slower                                                                |
| chaos                      | 37.9 ms                                                     | 44.1 ms: 1.17x slower                                                                |
| comprehensions             | 10.4 us                                                     | 12.1 us: 1.17x slower                                                                |
| sqlglot_transpile          | 953 us                                                      | 1.12 ms: 1.18x slower                                                                |
| sqlglot_parse              | 764 us                                                      | 910 us: 1.19x slower                                                                 |
| many_optionals             | 361 us                                                      | 440 us: 1.22x slower                                                                 |
| deltablue                  | 1.89 ms                                                     | 2.31 ms: 1.22x slower                                                                |
| pickle_pure_python         | 186 us                                                      | 230 us: 1.24x slower                                                                 |
| django_template            | 20.3 ms                                                     | 26.2 ms: 1.29x slower                                                                |
| raytrace                   | 153 ms                                                      | 204 ms: 1.33x slower                                                                 |
| subparsers                 | 10.9 ms                                                     | 16.7 ms: 1.54x slower                                                                |
| Geometric mean             | (ref)                                                       | 1.00x slower                                                                         |

Benchmark hidden because not significant (4): pylint, json_loads, create_gc_cycles, gc_traversal
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown