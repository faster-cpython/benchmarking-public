# Results vs. 3.13.0

- fork: faster-cpython
- ref: explicit_check_perio
- machine: windows-amd64
- commit hash: 494c825
- commit date: 2025-06-20
- overall geometric mean: 1.045x faster
- HPT reliability: 99.36%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 221 ms: 1.03x slower                                                                 |
| docutils       | 1.53 sec                                                    | 1.63 sec: 1.06x slower                                                               |
| sphinx         | 617 ms                                                      | 649 ms: 1.05x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                         |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 157 ms: 1.91x faster                                                                 |
| async_tree_memoization_tg  | 281 ms                                                      | 218 ms: 1.29x faster                                                                 |
| async_tree_memoization     | 265 ms                                                      | 214 ms: 1.24x faster                                                                 |
| async_tree_none            | 219 ms                                                      | 177 ms: 1.24x faster                                                                 |
| async_tree_io              | 513 ms                                                      | 415 ms: 1.24x faster                                                                 |
| async_tree_io_tg           | 497 ms                                                      | 406 ms: 1.22x faster                                                                 |
| async_tree_none_tg         | 200 ms                                                      | 174 ms: 1.15x faster                                                                 |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 333 ms: 1.14x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 347 ms: 1.10x faster                                                                 |
| async_generators           | 223 ms                                                      | 231 ms: 1.04x slower                                                                 |
| coroutines                 | 12.5 ms                                                     | 14.5 ms: 1.16x slower                                                                |
| Geometric mean             | (ref)                                                       | 1.19x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 44.5 ms: 1.14x faster                                                                |
| nbody          | 66.3 ms                                                     | 65.2 ms: 1.02x faster                                                                |
| pidigits       | 146 ms                                                      | 146 ms: 1.00x faster                                                                 |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.2 ms: 1.68x faster                                                                |
| regex_effbot   | 1.69 ms                                                     | 1.52 ms: 1.12x faster                                                                |
| regex_compile  | 80.7 ms                                                     | 82.0 ms: 1.02x slower                                                                |
| regex_dna      | 115 ms                                                      | 121 ms: 1.05x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 88.4 ms: 1.04x faster                                                                |
| json_loads           | 15.1 us                                                     | 14.6 us: 1.04x faster                                                                |
| tomli_loads          | 1.37 sec                                                    | 1.43 sec: 1.04x slower                                                               |
| unpickle_pure_python | 130 us                                                      | 138 us: 1.06x slower                                                                 |
| xml_etree_iterparse  | 60.5 ms                                                     | 64.5 ms: 1.07x slower                                                                |
| xml_etree_generate   | 53.5 ms                                                     | 57.1 ms: 1.07x slower                                                                |
| xml_etree_process    | 36.5 ms                                                     | 39.7 ms: 1.09x slower                                                                |
| pickle_pure_python   | 186 us                                                      | 219 us: 1.17x slower                                                                 |
| Geometric mean       | (ref)                                                       | 1.05x slower                                                                         |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.0 ms: 1.07x slower                                                                |
| python_startup_no_site | 16.9 ms                                                     | 19.4 ms: 1.15x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| genshi_text     | 15.2 ms                                                     | 15.7 ms: 1.03x slower                                                                |
| mako            | 6.56 ms                                                     | 6.81 ms: 1.04x slower                                                                |
| django_template | 20.3 ms                                                     | 24.4 ms: 1.20x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.07x slower                                                                         |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 501 us: 16.89x faster                                                                |
| pathlib                    | 75.3 ms                                                     | 31.8 ms: 2.37x faster                                                                |
| asyncio_websockets         | 300 ms                                                      | 157 ms: 1.91x faster                                                                 |
| mdp                        | 1.43 sec                                                    | 813 ms: 1.76x faster                                                                 |
| regex_v8                   | 23.8 ms                                                     | 14.2 ms: 1.68x faster                                                                |
| async_tree_memoization_tg  | 281 ms                                                      | 218 ms: 1.29x faster                                                                 |
| deepcopy                   | 223 us                                                      | 176 us: 1.27x faster                                                                 |
| async_tree_memoization     | 265 ms                                                      | 214 ms: 1.24x faster                                                                 |
| async_tree_none            | 219 ms                                                      | 177 ms: 1.24x faster                                                                 |
| async_tree_io              | 513 ms                                                      | 415 ms: 1.24x faster                                                                 |
| deepcopy_memo              | 23.1 us                                                     | 18.8 us: 1.23x faster                                                                |
| async_tree_io_tg           | 497 ms                                                      | 406 ms: 1.22x faster                                                                 |
| async_tree_none_tg         | 200 ms                                                      | 174 ms: 1.15x faster                                                                 |
| float                      | 50.8 ms                                                     | 44.5 ms: 1.14x faster                                                                |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 333 ms: 1.14x faster                                                                 |
| regex_effbot               | 1.69 ms                                                     | 1.52 ms: 1.12x faster                                                                |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 347 ms: 1.10x faster                                                                 |
| deepcopy_reduce            | 2.02 us                                                     | 1.85 us: 1.09x faster                                                                |
| go                         | 84.7 ms                                                     | 77.8 ms: 1.09x faster                                                                |
| json                       | 3.30 ms                                                     | 3.05 ms: 1.08x faster                                                                |
| telco                      | 4.85 ms                                                     | 4.63 ms: 1.05x faster                                                                |
| xml_etree_parse            | 92.2 ms                                                     | 88.4 ms: 1.04x faster                                                                |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.51 ms: 1.04x faster                                                                |
| json_loads                 | 15.1 us                                                     | 14.6 us: 1.04x faster                                                                |
| spectral_norm              | 63.4 ms                                                     | 62.2 ms: 1.02x faster                                                                |
| nbody                      | 66.3 ms                                                     | 65.2 ms: 1.02x faster                                                                |
| pidigits                   | 146 ms                                                      | 146 ms: 1.00x faster                                                                 |
| scimark_monte_carlo        | 40.7 ms                                                     | 41.0 ms: 1.01x slower                                                                |
| typing_runtime_protocols   | 103 us                                                      | 104 us: 1.01x slower                                                                 |
| regex_compile              | 80.7 ms                                                     | 82.0 ms: 1.02x slower                                                                |
| shortest_path              | 355 ms                                                      | 362 ms: 1.02x slower                                                                 |
| sympy_expand               | 286 ms                                                      | 292 ms: 1.02x slower                                                                 |
| sympy_integrate            | 12.3 ms                                                     | 12.7 ms: 1.03x slower                                                                |
| scimark_sor                | 76.2 ms                                                     | 78.2 ms: 1.03x slower                                                                |
| 2to3                       | 215 ms                                                      | 221 ms: 1.03x slower                                                                 |
| genshi_text                | 15.2 ms                                                     | 15.7 ms: 1.03x slower                                                                |
| pycparser                  | 695 ms                                                      | 717 ms: 1.03x slower                                                                 |
| sympy_str                  | 167 ms                                                      | 172 ms: 1.03x slower                                                                 |
| meteor_contest             | 72.0 ms                                                     | 74.4 ms: 1.03x slower                                                                |
| generators                 | 19.0 ms                                                     | 19.6 ms: 1.03x slower                                                                |
| dulwich_log                | 40.1 ms                                                     | 41.6 ms: 1.04x slower                                                                |
| connected_components       | 320 ms                                                      | 332 ms: 1.04x slower                                                                 |
| mako                       | 6.56 ms                                                     | 6.81 ms: 1.04x slower                                                                |
| async_generators           | 223 ms                                                      | 231 ms: 1.04x slower                                                                 |
| bpe_tokeniser              | 2.87 sec                                                    | 2.99 sec: 1.04x slower                                                               |
| sympy_sum                  | 85.2 ms                                                     | 88.8 ms: 1.04x slower                                                                |
| pyflate                    | 283 ms                                                      | 295 ms: 1.04x slower                                                                 |
| tomli_loads                | 1.37 sec                                                    | 1.43 sec: 1.04x slower                                                               |
| scimark_fft                | 175 ms                                                      | 183 ms: 1.05x slower                                                                 |
| sphinx                     | 617 ms                                                      | 649 ms: 1.05x slower                                                                 |
| regex_dna                  | 115 ms                                                      | 121 ms: 1.05x slower                                                                 |
| fannkuch                   | 252 ms                                                      | 265 ms: 1.05x slower                                                                 |
| scimark_lu                 | 56.7 ms                                                     | 59.9 ms: 1.06x slower                                                                |
| unpickle_pure_python       | 130 us                                                      | 138 us: 1.06x slower                                                                 |
| crypto_pyaes               | 45.6 ms                                                     | 48.5 ms: 1.06x slower                                                                |
| docutils                   | 1.53 sec                                                    | 1.63 sec: 1.06x slower                                                               |
| xml_etree_iterparse        | 60.5 ms                                                     | 64.5 ms: 1.07x slower                                                                |
| python_startup             | 24.4 ms                                                     | 26.0 ms: 1.07x slower                                                                |
| xml_etree_generate         | 53.5 ms                                                     | 57.1 ms: 1.07x slower                                                                |
| comprehensions             | 10.4 us                                                     | 11.1 us: 1.07x slower                                                                |
| chaos                      | 37.9 ms                                                     | 40.5 ms: 1.07x slower                                                                |
| richards_super             | 29.8 ms                                                     | 31.9 ms: 1.07x slower                                                                |
| richards                   | 26.3 ms                                                     | 28.2 ms: 1.07x slower                                                                |
| coverage                   | 45.3 ms                                                     | 48.7 ms: 1.07x slower                                                                |
| create_gc_cycles           | 1.22 ms                                                     | 1.32 ms: 1.08x slower                                                                |
| xml_etree_process          | 36.5 ms                                                     | 39.7 ms: 1.09x slower                                                                |
| gc_traversal               | 1.96 ms                                                     | 2.14 ms: 1.09x slower                                                                |
| hexiom                     | 3.84 ms                                                     | 4.22 ms: 1.10x slower                                                                |
| logging_simple             | 5.77 us                                                     | 6.36 us: 1.10x slower                                                                |
| logging_format             | 6.18 us                                                     | 6.81 us: 1.10x slower                                                                |
| nqueens                    | 56.1 ms                                                     | 62.1 ms: 1.11x slower                                                                |
| pprint_safe_repr           | 485 ms                                                      | 548 ms: 1.13x slower                                                                 |
| pprint_pformat             | 977 ms                                                      | 1.11 sec: 1.13x slower                                                               |
| python_startup_no_site     | 16.9 ms                                                     | 19.4 ms: 1.15x slower                                                                |
| coroutines                 | 12.5 ms                                                     | 14.5 ms: 1.16x slower                                                                |
| pickle_pure_python         | 186 us                                                      | 219 us: 1.17x slower                                                                 |
| raytrace                   | 153 ms                                                      | 183 ms: 1.19x slower                                                                 |
| django_template            | 20.3 ms                                                     | 24.4 ms: 1.20x slower                                                                |
| deltablue                  | 1.89 ms                                                     | 2.29 ms: 1.21x slower                                                                |
| many_optionals             | 361 us                                                      | 440 us: 1.22x slower                                                                 |
| subparsers                 | 10.9 ms                                                     | 17.2 ms: 1.58x slower                                                                |
| logging_silent             | 54.6 ns                                                     | 318 ns: 5.83x slower                                                                 |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                                         |

Benchmark hidden because not significant (6): pylint, sqlite_synth, html5lib, json_dumps, k_core, genshi_xml
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250620-3.15.0a0-494c825/bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.045x faster

# HPT report

- Reliability score: 99.36% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown