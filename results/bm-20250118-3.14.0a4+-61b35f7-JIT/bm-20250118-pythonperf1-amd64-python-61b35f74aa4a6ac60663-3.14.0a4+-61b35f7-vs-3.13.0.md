# Results vs. 3.13.0

- fork: python
- ref: 61b35f74aa4a6ac60663
- machine: windows-amd64
- commit hash: 61b35f7
- commit date: 2025-01-18
- overall geometric mean: 1.017x faster
- HPT reliability: 66.29%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 229 ms: 1.07x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.75 sec: 1.14x slower                                                      |
| sphinx         | 617 ms                                                      | 682 ms: 1.10x slower                                                        |
| Geometric mean | (ref)                                                       | 1.08x slower                                                                |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 215 ms: 1.31x faster                                                        |
| async_tree_io              | 513 ms                                                      | 410 ms: 1.25x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 403 ms: 1.23x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 227 ms: 1.16x faster                                                        |
| async_tree_none            | 219 ms                                                      | 190 ms: 1.15x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 175 ms: 1.15x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 346 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 349 ms: 1.09x faster                                                        |
| asyncio_websockets         | 300 ms                                                      | 310 ms: 1.03x slower                                                        |
| async_generators           | 223 ms                                                      | 248 ms: 1.11x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 15.1 ms: 1.20x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.09x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 39.2 ms: 1.30x faster                                                       |
| nbody          | 66.3 ms                                                     | 57.9 ms: 1.14x faster                                                       |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 16.7 ms: 1.43x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.41 ms: 1.20x faster                                                       |
| regex_dna      | 115 ms                                                      | 112 ms: 1.03x faster                                                        |
| regex_compile  | 80.7 ms                                                     | 81.3 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.20 sec: 1.14x faster                                                      |
| unpickle_pure_python | 130 us                                                      | 114 us: 1.14x faster                                                        |
| xml_etree_generate   | 53.5 ms                                                     | 50.6 ms: 1.06x faster                                                       |
| xml_etree_parse      | 92.2 ms                                                     | 88.4 ms: 1.04x faster                                                       |
| json_loads           | 15.1 us                                                     | 14.7 us: 1.03x faster                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 59.8 ms: 1.01x faster                                                       |
| xml_etree_process    | 36.5 ms                                                     | 37.0 ms: 1.01x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 6.48 ms: 1.05x slower                                                       |
| pickle_pure_python   | 186 us                                                      | 216 us: 1.16x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 24.1 ms: 1.01x faster                                                       |
| python_startup_no_site | 16.9 ms                                                     | 17.9 ms: 1.06x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.02x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.10 ms: 1.29x faster                                                       |
| genshi_text     | 15.2 ms                                                     | 18.7 ms: 1.23x slower                                                       |
| genshi_xml      | 33.9 ms                                                     | 45.9 ms: 1.36x slower                                                       |
| django_template | 20.3 ms                                                     | 27.6 ms: 1.36x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.15x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 570 us: 14.87x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 16.7 ms: 1.43x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 47.0 ms: 1.35x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 17.3 us: 1.33x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 215 ms: 1.31x faster                                                        |
| float                      | 50.8 ms                                                     | 39.2 ms: 1.30x faster                                                       |
| mako                       | 6.56 ms                                                     | 5.10 ms: 1.29x faster                                                       |
| async_tree_io              | 513 ms                                                      | 410 ms: 1.25x faster                                                        |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.08 ms: 1.25x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 403 ms: 1.23x faster                                                        |
| scimark_sor                | 76.2 ms                                                     | 62.5 ms: 1.22x faster                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.41 ms: 1.20x faster                                                       |
| deepcopy                   | 223 us                                                      | 188 us: 1.19x faster                                                        |
| scimark_fft                | 175 ms                                                      | 149 ms: 1.17x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 227 ms: 1.16x faster                                                        |
| async_tree_none            | 219 ms                                                      | 190 ms: 1.15x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 175 ms: 1.15x faster                                                        |
| nbody                      | 66.3 ms                                                     | 57.9 ms: 1.14x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.20 sec: 1.14x faster                                                      |
| unpickle_pure_python       | 130 us                                                      | 114 us: 1.14x faster                                                        |
| json                       | 3.30 ms                                                     | 2.96 ms: 1.12x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.38 ms: 1.11x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 346 ms: 1.11x faster                                                        |
| crypto_pyaes               | 45.6 ms                                                     | 41.3 ms: 1.10x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 349 ms: 1.09x faster                                                        |
| bpe_tokeniser              | 2.87 sec                                                    | 2.66 sec: 1.08x faster                                                      |
| fannkuch                   | 252 ms                                                      | 235 ms: 1.07x faster                                                        |
| scimark_monte_carlo        | 40.7 ms                                                     | 38.1 ms: 1.07x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.89 us: 1.07x faster                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 50.6 ms: 1.06x faster                                                       |
| pyflate                    | 283 ms                                                      | 268 ms: 1.06x faster                                                        |
| k_core                     | 1.70 sec                                                    | 1.61 sec: 1.06x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 88.4 ms: 1.04x faster                                                       |
| connected_components       | 320 ms                                                      | 309 ms: 1.04x faster                                                        |
| shortest_path              | 355 ms                                                      | 344 ms: 1.03x faster                                                        |
| regex_dna                  | 115 ms                                                      | 112 ms: 1.03x faster                                                        |
| json_loads                 | 15.1 us                                                     | 14.7 us: 1.03x faster                                                       |
| python_startup             | 24.4 ms                                                     | 24.1 ms: 1.01x faster                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 59.8 ms: 1.01x faster                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.21 ms: 1.01x faster                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.57 us: 1.01x faster                                                       |
| regex_compile              | 80.7 ms                                                     | 81.3 ms: 1.01x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 40.5 ms: 1.01x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 57.3 ms: 1.01x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 37.0 ms: 1.01x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 831 us: 1.03x slower                                                        |
| asyncio_websockets         | 300 ms                                                      | 310 ms: 1.03x slower                                                        |
| pprint_safe_repr           | 485 ms                                                      | 501 ms: 1.03x slower                                                        |
| pprint_pformat             | 977 ms                                                      | 1.01 sec: 1.03x slower                                                      |
| pycparser                  | 695 ms                                                      | 721 ms: 1.04x slower                                                        |
| meteor_contest             | 72.0 ms                                                     | 74.9 ms: 1.04x slower                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 87.7 ms: 1.04x slower                                                       |
| pathlib                    | 75.3 ms                                                     | 78.5 ms: 1.04x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 6.48 ms: 1.05x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 17.9 ms: 1.06x slower                                                       |
| sympy_expand               | 286 ms                                                      | 304 ms: 1.06x slower                                                        |
| 2to3                       | 215 ms                                                      | 229 ms: 1.07x slower                                                        |
| sympy_str                  | 167 ms                                                      | 178 ms: 1.07x slower                                                        |
| sympy_sum                  | 85.2 ms                                                     | 91.1 ms: 1.07x slower                                                       |
| chaos                      | 37.9 ms                                                     | 41.0 ms: 1.08x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 113 us: 1.09x slower                                                        |
| logging_silent             | 54.6 ns                                                     | 60.1 ns: 1.10x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.6 ms: 1.10x slower                                                       |
| sphinx                     | 617 ms                                                      | 682 ms: 1.10x slower                                                        |
| go                         | 84.7 ms                                                     | 94.2 ms: 1.11x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.87 us: 1.11x slower                                                       |
| async_generators           | 223 ms                                                      | 248 ms: 1.11x slower                                                        |
| logging_simple             | 5.77 us                                                     | 6.43 us: 1.11x slower                                                       |
| mdp                        | 1.43 sec                                                    | 1.60 sec: 1.12x slower                                                      |
| sqlglot_parse              | 764 us                                                      | 853 us: 1.12x slower                                                        |
| coverage                   | 45.3 ms                                                     | 50.6 ms: 1.12x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.75 sec: 1.14x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 64.5 ms: 1.15x slower                                                       |
| sqlglot_transpile          | 953 us                                                      | 1.10 ms: 1.15x slower                                                       |
| comprehensions             | 10.4 us                                                     | 12.0 us: 1.16x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 216 us: 1.16x slower                                                        |
| sqlglot_optimize           | 32.5 ms                                                     | 38.6 ms: 1.19x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 15.1 ms: 1.20x slower                                                       |
| sqlglot_normalize          | 172 ms                                                      | 209 ms: 1.22x slower                                                        |
| genshi_text                | 15.2 ms                                                     | 18.7 ms: 1.23x slower                                                       |
| many_optionals             | 361 us                                                      | 449 us: 1.24x slower                                                        |
| deltablue                  | 1.89 ms                                                     | 2.43 ms: 1.28x slower                                                       |
| generators                 | 19.0 ms                                                     | 25.0 ms: 1.32x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 5.08 ms: 1.32x slower                                                       |
| genshi_xml                 | 33.9 ms                                                     | 45.9 ms: 1.36x slower                                                       |
| django_template            | 20.3 ms                                                     | 27.6 ms: 1.36x slower                                                       |
| richards_super             | 29.8 ms                                                     | 40.7 ms: 1.37x slower                                                       |
| richards                   | 26.3 ms                                                     | 36.1 ms: 1.38x slower                                                       |
| raytrace                   | 153 ms                                                      | 213 ms: 1.39x slower                                                        |
| subparsers                 | 10.9 ms                                                     | 15.9 ms: 1.47x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (4): pidigits, html5lib, gc_traversal, pylint
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (8) of results/bm-20250118-3.14.0a4+-61b35f7-JIT/bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.017x faster

# HPT report

- Reliability score: 66.29% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown