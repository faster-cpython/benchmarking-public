# Results vs. 3.13.0

- fork: python
- ref: e82c2ca2a59235bc1965
- machine: windows-amd64
- commit hash: e82c2ca
- commit date: 2025-03-15
- overall geometric mean: 1.000x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 226 ms: 1.05x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.69 sec: 1.10x slower                                                      |
| html5lib       | 38.2 ms                                                     | 40.6 ms: 1.06x slower                                                       |
| sphinx         | 617 ms                                                      | 658 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                       | 1.07x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 218 ms: 1.29x faster                                                        |
| async_tree_io              | 513 ms                                                      | 427 ms: 1.20x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 416 ms: 1.19x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 222 ms: 1.19x faster                                                        |
| async_tree_none            | 219 ms                                                      | 190 ms: 1.15x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 178 ms: 1.13x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 342 ms: 1.12x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 342 ms: 1.11x faster                                                        |
| asyncio_websockets         | 300 ms                                                      | 315 ms: 1.05x slower                                                        |
| async_generators           | 223 ms                                                      | 234 ms: 1.05x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.5 ms: 1.08x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.10x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 46.1 ms: 1.10x faster                                                       |
| pidigits       | 146 ms                                                      | 148 ms: 1.01x slower                                                        |
| nbody          | 66.3 ms                                                     | 71.7 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                       | 1.00x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.8 ms: 1.72x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.40 ms: 1.21x faster                                                       |
| regex_dna      | 115 ms                                                      | 114 ms: 1.01x faster                                                        |
| regex_compile  | 80.7 ms                                                     | 86.8 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 88.3 ms: 1.04x faster                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 64.2 ms: 1.06x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.46 sec: 1.06x slower                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 58.8 ms: 1.10x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 6.99 ms: 1.13x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 41.6 ms: 1.14x slower                                                       |
| unpickle_pure_python | 130 us                                                      | 151 us: 1.17x slower                                                        |
| pickle_pure_python   | 186 us                                                      | 227 us: 1.22x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                                |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.1 ms: 1.07x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 20.4 ms: 1.21x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.84 ms: 1.04x slower                                                       |
| genshi_xml      | 33.9 ms                                                     | 38.0 ms: 1.12x slower                                                       |
| genshi_text     | 15.2 ms                                                     | 17.5 ms: 1.15x slower                                                       |
| django_template | 20.3 ms                                                     | 26.6 ms: 1.31x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.15x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 530 us: 15.98x faster                                                       |
| pathlib                    | 75.3 ms                                                     | 32.6 ms: 2.31x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 13.8 ms: 1.72x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 218 ms: 1.29x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.40 ms: 1.21x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 19.2 us: 1.20x faster                                                       |
| async_tree_io              | 513 ms                                                      | 427 ms: 1.20x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 416 ms: 1.19x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 222 ms: 1.19x faster                                                        |
| deepcopy                   | 223 us                                                      | 188 us: 1.19x faster                                                        |
| async_tree_none            | 219 ms                                                      | 190 ms: 1.15x faster                                                        |
| spectral_norm              | 63.4 ms                                                     | 55.3 ms: 1.15x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 178 ms: 1.13x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 342 ms: 1.12x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 342 ms: 1.11x faster                                                        |
| float                      | 50.8 ms                                                     | 46.1 ms: 1.10x faster                                                       |
| json                       | 3.30 ms                                                     | 3.09 ms: 1.07x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 88.3 ms: 1.04x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.56 ms: 1.02x faster                                                       |
| regex_dna                  | 115 ms                                                      | 114 ms: 1.01x faster                                                        |
| sqlite_synth               | 1.59 us                                                     | 1.57 us: 1.01x faster                                                       |
| pidigits                   | 146 ms                                                      | 148 ms: 1.01x slower                                                        |
| telco                      | 4.85 ms                                                     | 4.92 ms: 1.02x slower                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.25 ms: 1.02x slower                                                       |
| shortest_path              | 355 ms                                                      | 365 ms: 1.03x slower                                                        |
| generators                 | 19.0 ms                                                     | 19.5 ms: 1.03x slower                                                       |
| k_core                     | 1.70 sec                                                    | 1.75 sec: 1.03x slower                                                      |
| gc_traversal               | 1.96 ms                                                     | 2.04 ms: 1.04x slower                                                       |
| mako                       | 6.56 ms                                                     | 6.84 ms: 1.04x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 3.00 sec: 1.04x slower                                                      |
| connected_components       | 320 ms                                                      | 335 ms: 1.05x slower                                                        |
| asyncio_websockets         | 300 ms                                                      | 315 ms: 1.05x slower                                                        |
| async_generators           | 223 ms                                                      | 234 ms: 1.05x slower                                                        |
| dulwich_log                | 40.1 ms                                                     | 42.2 ms: 1.05x slower                                                       |
| 2to3                       | 215 ms                                                      | 226 ms: 1.05x slower                                                        |
| scimark_fft                | 175 ms                                                      | 184 ms: 1.05x slower                                                        |
| sympy_sum                  | 85.2 ms                                                     | 90.1 ms: 1.06x slower                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 89.1 ms: 1.06x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 64.2 ms: 1.06x slower                                                       |
| coverage                   | 45.3 ms                                                     | 48.0 ms: 1.06x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.46 sec: 1.06x slower                                                      |
| pycparser                  | 695 ms                                                      | 738 ms: 1.06x slower                                                        |
| html5lib                   | 38.2 ms                                                     | 40.6 ms: 1.06x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 863 us: 1.07x slower                                                        |
| sympy_str                  | 167 ms                                                      | 178 ms: 1.07x slower                                                        |
| sphinx                     | 617 ms                                                      | 658 ms: 1.07x slower                                                        |
| python_startup             | 24.4 ms                                                     | 26.1 ms: 1.07x slower                                                       |
| sympy_expand               | 286 ms                                                      | 306 ms: 1.07x slower                                                        |
| meteor_contest             | 72.0 ms                                                     | 77.2 ms: 1.07x slower                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 43.8 ms: 1.07x slower                                                       |
| regex_compile              | 80.7 ms                                                     | 86.8 ms: 1.08x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 61.0 ms: 1.08x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.5 ms: 1.08x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.3 ms: 1.08x slower                                                       |
| go                         | 84.7 ms                                                     | 91.5 ms: 1.08x slower                                                       |
| nbody                      | 66.3 ms                                                     | 71.7 ms: 1.08x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 59.5 ns: 1.09x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 83.4 ms: 1.09x slower                                                       |
| fannkuch                   | 252 ms                                                      | 276 ms: 1.10x slower                                                        |
| crypto_pyaes               | 45.6 ms                                                     | 50.1 ms: 1.10x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 58.8 ms: 1.10x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.69 sec: 1.10x slower                                                      |
| typing_runtime_protocols   | 103 us                                                      | 114 us: 1.11x slower                                                        |
| pyflate                    | 283 ms                                                      | 314 ms: 1.11x slower                                                        |
| richards                   | 26.3 ms                                                     | 29.3 ms: 1.12x slower                                                       |
| genshi_xml                 | 33.9 ms                                                     | 38.0 ms: 1.12x slower                                                       |
| richards_super             | 29.8 ms                                                     | 33.4 ms: 1.12x slower                                                       |
| pprint_safe_repr           | 485 ms                                                      | 547 ms: 1.13x slower                                                        |
| json_dumps                 | 6.19 ms                                                     | 6.99 ms: 1.13x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.11 sec: 1.13x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 41.6 ms: 1.14x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.39 ms: 1.14x slower                                                       |
| mdp                        | 1.43 sec                                                    | 1.64 sec: 1.14x slower                                                      |
| genshi_text                | 15.2 ms                                                     | 17.5 ms: 1.15x slower                                                       |
| chaos                      | 37.9 ms                                                     | 43.7 ms: 1.15x slower                                                       |
| comprehensions             | 10.4 us                                                     | 12.1 us: 1.16x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 151 us: 1.17x slower                                                        |
| logging_simple             | 5.77 us                                                     | 6.73 us: 1.17x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 65.5 ms: 1.17x slower                                                       |
| logging_format             | 6.18 us                                                     | 7.26 us: 1.18x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.25 ms: 1.19x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 20.4 ms: 1.21x slower                                                       |
| many_optionals             | 361 us                                                      | 440 us: 1.22x slower                                                        |
| pickle_pure_python         | 186 us                                                      | 227 us: 1.22x slower                                                        |
| raytrace                   | 153 ms                                                      | 197 ms: 1.29x slower                                                        |
| django_template            | 20.3 ms                                                     | 26.6 ms: 1.31x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 16.6 ms: 1.53x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (3): pylint, deepcopy_reduce, json_loads
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250315-3.14.0a6+-e82c2ca/bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.000x faster

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown