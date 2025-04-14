# Results vs. 3.13.0

- fork: faster-cpython
- ref: close_escapes_2
- machine: windows-amd64
- commit hash: fa5c6fd
- commit date: 2025-01-28
- overall geometric mean: 1.027x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250128-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 231 ms: 1.07x slower                                                             |
| docutils       | 1.53 sec                                                    | 1.69 sec: 1.10x slower                                                           |
| html5lib       | 38.2 ms                                                     | 39.5 ms: 1.04x slower                                                            |
| sphinx         | 617 ms                                                      | 657 ms: 1.06x slower                                                             |
| Geometric mean | (ref)                                                       | 1.07x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250128-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 221 ms: 1.27x faster                                                             |
| async_tree_io              | 513 ms                                                      | 432 ms: 1.19x faster                                                             |
| async_tree_io_tg           | 497 ms                                                      | 422 ms: 1.18x faster                                                             |
| async_tree_memoization     | 265 ms                                                      | 228 ms: 1.16x faster                                                             |
| async_tree_none            | 219 ms                                                      | 195 ms: 1.12x faster                                                             |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 345 ms: 1.11x faster                                                             |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 347 ms: 1.10x faster                                                             |
| async_tree_none_tg         | 200 ms                                                      | 187 ms: 1.07x faster                                                             |
| async_generators           | 223 ms                                                      | 226 ms: 1.02x slower                                                             |
| coroutines                 | 12.5 ms                                                     | 14.7 ms: 1.17x slower                                                            |
| Geometric mean             | (ref)                                                       | 1.09x faster                                                                     |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250128-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 146 ms                                                      | 148 ms: 1.01x slower                                                             |
| float          | 50.8 ms                                                     | 51.9 ms: 1.02x slower                                                            |
| nbody          | 66.3 ms                                                     | 78.2 ms: 1.18x slower                                                            |
| Geometric mean | (ref)                                                       | 1.07x slower                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250128-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 16.3 ms: 1.46x faster                                                            |
| regex_effbot   | 1.69 ms                                                     | 1.48 ms: 1.14x faster                                                            |
| regex_dna      | 115 ms                                                      | 116 ms: 1.01x slower                                                             |
| regex_compile  | 80.7 ms                                                     | 89.3 ms: 1.11x slower                                                            |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250128-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 88.0 ms: 1.05x faster                                                            |
| json_loads           | 15.1 us                                                     | 15.4 us: 1.02x slower                                                            |
| tomli_loads          | 1.37 sec                                                    | 1.45 sec: 1.06x slower                                                           |
| xml_etree_iterparse  | 60.5 ms                                                     | 64.1 ms: 1.06x slower                                                            |
| xml_etree_generate   | 53.5 ms                                                     | 58.5 ms: 1.09x slower                                                            |
| json_dumps           | 6.19 ms                                                     | 6.77 ms: 1.09x slower                                                            |
| xml_etree_process    | 36.5 ms                                                     | 41.4 ms: 1.13x slower                                                            |
| unpickle_pure_python | 130 us                                                      | 155 us: 1.19x slower                                                             |
| pickle_pure_python   | 186 us                                                      | 236 us: 1.27x slower                                                             |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250128-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 16.9 ms                                                     | 18.1 ms: 1.07x slower                                                            |
| Geometric mean         | (ref)                                                       | 1.03x slower                                                                     |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250128-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.77 ms: 1.03x slower                                                            |
| genshi_text     | 15.2 ms                                                     | 16.3 ms: 1.07x slower                                                            |
| django_template | 20.3 ms                                                     | 25.9 ms: 1.28x slower                                                            |
| Geometric mean  | (ref)                                                       | 1.10x slower                                                                     |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250128-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 520 us: 16.29x faster                                                            |
| regex_v8                   | 23.8 ms                                                     | 16.3 ms: 1.46x faster                                                            |
| async_tree_memoization_tg  | 281 ms                                                      | 221 ms: 1.27x faster                                                             |
| deepcopy                   | 223 us                                                      | 185 us: 1.21x faster                                                             |
| async_tree_io              | 513 ms                                                      | 432 ms: 1.19x faster                                                             |
| async_tree_io_tg           | 497 ms                                                      | 422 ms: 1.18x faster                                                             |
| async_tree_memoization     | 265 ms                                                      | 228 ms: 1.16x faster                                                             |
| regex_effbot               | 1.69 ms                                                     | 1.48 ms: 1.14x faster                                                            |
| async_tree_none            | 219 ms                                                      | 195 ms: 1.12x faster                                                             |
| deepcopy_memo              | 23.1 us                                                     | 20.8 us: 1.11x faster                                                            |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 345 ms: 1.11x faster                                                             |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 347 ms: 1.10x faster                                                             |
| deepcopy_reduce            | 2.02 us                                                     | 1.86 us: 1.09x faster                                                            |
| json                       | 3.30 ms                                                     | 3.04 ms: 1.09x faster                                                            |
| async_tree_none_tg         | 200 ms                                                      | 187 ms: 1.07x faster                                                             |
| xml_etree_parse            | 92.2 ms                                                     | 88.0 ms: 1.05x faster                                                            |
| telco                      | 4.85 ms                                                     | 4.79 ms: 1.01x faster                                                            |
| sqlite_synth               | 1.59 us                                                     | 1.57 us: 1.01x faster                                                            |
| create_gc_cycles           | 1.22 ms                                                     | 1.21 ms: 1.01x faster                                                            |
| regex_dna                  | 115 ms                                                      | 116 ms: 1.01x slower                                                             |
| pidigits                   | 146 ms                                                      | 148 ms: 1.01x slower                                                             |
| async_generators           | 223 ms                                                      | 226 ms: 1.02x slower                                                             |
| k_core                     | 1.70 sec                                                    | 1.73 sec: 1.02x slower                                                           |
| float                      | 50.8 ms                                                     | 51.9 ms: 1.02x slower                                                            |
| json_loads                 | 15.1 us                                                     | 15.4 us: 1.02x slower                                                            |
| bench_thread_pool          | 810 us                                                      | 836 us: 1.03x slower                                                             |
| mako                       | 6.56 ms                                                     | 6.77 ms: 1.03x slower                                                            |
| sympy_sum                  | 85.2 ms                                                     | 88.0 ms: 1.03x slower                                                            |
| pathlib                    | 75.3 ms                                                     | 78.0 ms: 1.04x slower                                                            |
| html5lib                   | 38.2 ms                                                     | 39.5 ms: 1.04x slower                                                            |
| spectral_norm              | 63.4 ms                                                     | 66.2 ms: 1.04x slower                                                            |
| sympy_expand               | 286 ms                                                      | 299 ms: 1.05x slower                                                             |
| meteor_contest             | 72.0 ms                                                     | 75.4 ms: 1.05x slower                                                            |
| bench_mp_pool              | 84.2 ms                                                     | 88.5 ms: 1.05x slower                                                            |
| tomli_loads                | 1.37 sec                                                    | 1.45 sec: 1.06x slower                                                           |
| mdp                        | 1.43 sec                                                    | 1.51 sec: 1.06x slower                                                           |
| sympy_str                  | 167 ms                                                      | 177 ms: 1.06x slower                                                             |
| xml_etree_iterparse        | 60.5 ms                                                     | 64.1 ms: 1.06x slower                                                            |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.76 ms: 1.06x slower                                                            |
| pycparser                  | 695 ms                                                      | 737 ms: 1.06x slower                                                             |
| bpe_tokeniser              | 2.87 sec                                                    | 3.05 sec: 1.06x slower                                                           |
| dulwich_log                | 40.1 ms                                                     | 42.7 ms: 1.06x slower                                                            |
| sphinx                     | 617 ms                                                      | 657 ms: 1.06x slower                                                             |
| crypto_pyaes               | 45.6 ms                                                     | 48.6 ms: 1.07x slower                                                            |
| genshi_text                | 15.2 ms                                                     | 16.3 ms: 1.07x slower                                                            |
| python_startup_no_site     | 16.9 ms                                                     | 18.1 ms: 1.07x slower                                                            |
| 2to3                       | 215 ms                                                      | 231 ms: 1.07x slower                                                             |
| sympy_integrate            | 12.3 ms                                                     | 13.3 ms: 1.08x slower                                                            |
| typing_runtime_protocols   | 103 us                                                      | 112 us: 1.08x slower                                                             |
| coverage                   | 45.3 ms                                                     | 49.3 ms: 1.09x slower                                                            |
| scimark_fft                | 175 ms                                                      | 191 ms: 1.09x slower                                                             |
| xml_etree_generate         | 53.5 ms                                                     | 58.5 ms: 1.09x slower                                                            |
| json_dumps                 | 6.19 ms                                                     | 6.77 ms: 1.09x slower                                                            |
| docutils                   | 1.53 sec                                                    | 1.69 sec: 1.10x slower                                                           |
| generators                 | 19.0 ms                                                     | 21.0 ms: 1.10x slower                                                            |
| logging_format             | 6.18 us                                                     | 6.82 us: 1.10x slower                                                            |
| go                         | 84.7 ms                                                     | 93.6 ms: 1.11x slower                                                            |
| regex_compile              | 80.7 ms                                                     | 89.3 ms: 1.11x slower                                                            |
| logging_simple             | 5.77 us                                                     | 6.41 us: 1.11x slower                                                            |
| pyflate                    | 283 ms                                                      | 316 ms: 1.11x slower                                                             |
| pprint_pformat             | 977 ms                                                      | 1.09 sec: 1.12x slower                                                           |
| sqlglot_optimize           | 32.5 ms                                                     | 36.6 ms: 1.12x slower                                                            |
| xml_etree_process          | 36.5 ms                                                     | 41.4 ms: 1.13x slower                                                            |
| pprint_safe_repr           | 485 ms                                                      | 551 ms: 1.14x slower                                                             |
| sqlglot_transpile          | 953 us                                                      | 1.09 ms: 1.14x slower                                                            |
| fannkuch                   | 252 ms                                                      | 289 ms: 1.15x slower                                                             |
| chaos                      | 37.9 ms                                                     | 43.5 ms: 1.15x slower                                                            |
| sqlglot_parse              | 764 us                                                      | 882 us: 1.15x slower                                                             |
| sqlglot_normalize          | 172 ms                                                      | 200 ms: 1.17x slower                                                             |
| coroutines                 | 12.5 ms                                                     | 14.7 ms: 1.17x slower                                                            |
| nqueens                    | 56.1 ms                                                     | 66.1 ms: 1.18x slower                                                            |
| nbody                      | 66.3 ms                                                     | 78.2 ms: 1.18x slower                                                            |
| unpickle_pure_python       | 130 us                                                      | 155 us: 1.19x slower                                                             |
| scimark_monte_carlo        | 40.7 ms                                                     | 48.8 ms: 1.20x slower                                                            |
| many_optionals             | 361 us                                                      | 439 us: 1.21x slower                                                             |
| scimark_sor                | 76.2 ms                                                     | 94.7 ms: 1.24x slower                                                            |
| hexiom                     | 3.84 ms                                                     | 4.79 ms: 1.25x slower                                                            |
| richards_super             | 29.8 ms                                                     | 37.4 ms: 1.25x slower                                                            |
| comprehensions             | 10.4 us                                                     | 13.0 us: 1.26x slower                                                            |
| scimark_lu                 | 56.7 ms                                                     | 71.5 ms: 1.26x slower                                                            |
| richards                   | 26.3 ms                                                     | 33.1 ms: 1.26x slower                                                            |
| pickle_pure_python         | 186 us                                                      | 236 us: 1.27x slower                                                             |
| django_template            | 20.3 ms                                                     | 25.9 ms: 1.28x slower                                                            |
| logging_silent             | 54.6 ns                                                     | 69.9 ns: 1.28x slower                                                            |
| deltablue                  | 1.89 ms                                                     | 2.48 ms: 1.31x slower                                                            |
| raytrace                   | 153 ms                                                      | 206 ms: 1.34x slower                                                             |
| subparsers                 | 10.9 ms                                                     | 16.0 ms: 1.47x slower                                                            |
| Geometric mean             | (ref)                                                       | 1.03x slower                                                                     |

Benchmark hidden because not significant (7): pylint, python_startup, connected_components, shortest_path, asyncio_websockets, gc_traversal, genshi_xml
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http

- Geometric mean (including insignificant results): 1.027x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown