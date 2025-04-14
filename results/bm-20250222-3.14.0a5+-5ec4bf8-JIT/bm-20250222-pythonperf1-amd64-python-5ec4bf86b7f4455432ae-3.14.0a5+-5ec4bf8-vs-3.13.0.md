# Results vs. 3.13.0

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: windows-amd64
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.032x faster
- HPT reliability: 87.55%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 221 ms: 1.03x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.71 sec: 1.12x slower                                                      |
| html5lib       | 38.2 ms                                                     | 39.9 ms: 1.04x slower                                                       |
| sphinx         | 617 ms                                                      | 654 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                       | 1.06x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 214 ms: 1.31x faster                                                        |
| async_tree_io              | 513 ms                                                      | 414 ms: 1.24x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 215 ms: 1.23x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 404 ms: 1.23x faster                                                        |
| async_tree_none            | 219 ms                                                      | 183 ms: 1.20x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 173 ms: 1.16x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 342 ms: 1.12x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 341 ms: 1.12x faster                                                        |
| asyncio_websockets         | 300 ms                                                      | 315 ms: 1.05x slower                                                        |
| async_generators           | 223 ms                                                      | 234 ms: 1.05x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.3 ms: 1.06x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 60.0 ms: 1.10x faster                                                       |
| float          | 50.8 ms                                                     | 48.0 ms: 1.06x faster                                                       |
| pidigits       | 146 ms                                                      | 154 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                       | 1.04x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.1 ms: 1.69x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.41 ms: 1.20x faster                                                       |
| regex_dna      | 115 ms                                                      | 113 ms: 1.02x faster                                                        |
| regex_compile  | 80.7 ms                                                     | 83.4 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.19x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.20 sec: 1.14x faster                                                      |
| unpickle_pure_python | 130 us                                                      | 116 us: 1.12x faster                                                        |
| xml_etree_generate   | 53.5 ms                                                     | 50.7 ms: 1.05x faster                                                       |
| xml_etree_parse      | 92.2 ms                                                     | 89.9 ms: 1.02x faster                                                       |
| json_loads           | 15.1 us                                                     | 14.8 us: 1.02x faster                                                       |
| xml_etree_process    | 36.5 ms                                                     | 36.7 ms: 1.00x slower                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.6 ms: 1.05x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 6.70 ms: 1.08x slower                                                       |
| pickle_pure_python   | 186 us                                                      | 213 us: 1.15x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 24.6 ms: 1.01x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 19.0 ms: 1.12x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.07x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.25 ms: 1.25x faster                                                       |
| genshi_text     | 15.2 ms                                                     | 16.4 ms: 1.08x slower                                                       |
| genshi_xml      | 33.9 ms                                                     | 36.9 ms: 1.09x slower                                                       |
| django_template | 20.3 ms                                                     | 25.5 ms: 1.25x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.04x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 509 us: 16.62x faster                                                       |
| pathlib                    | 75.3 ms                                                     | 29.7 ms: 2.53x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.1 ms: 1.69x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 214 ms: 1.31x faster                                                        |
| mako                       | 6.56 ms                                                     | 5.25 ms: 1.25x faster                                                       |
| async_tree_io              | 513 ms                                                      | 414 ms: 1.24x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 215 ms: 1.23x faster                                                        |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.11 ms: 1.23x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 404 ms: 1.23x faster                                                        |
| deepcopy                   | 223 us                                                      | 185 us: 1.21x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.41 ms: 1.20x faster                                                       |
| async_tree_none            | 219 ms                                                      | 183 ms: 1.20x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 173 ms: 1.16x faster                                                        |
| scimark_fft                | 175 ms                                                      | 152 ms: 1.15x faster                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.20 sec: 1.14x faster                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 342 ms: 1.12x faster                                                        |
| unpickle_pure_python       | 130 us                                                      | 116 us: 1.12x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 341 ms: 1.12x faster                                                        |
| deepcopy_memo              | 23.1 us                                                     | 20.7 us: 1.11x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.39 ms: 1.11x faster                                                       |
| nbody                      | 66.3 ms                                                     | 60.0 ms: 1.10x faster                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.61 sec: 1.10x faster                                                      |
| json                       | 3.30 ms                                                     | 3.00 ms: 1.10x faster                                                       |
| float                      | 50.8 ms                                                     | 48.0 ms: 1.06x faster                                                       |
| fannkuch                   | 252 ms                                                      | 238 ms: 1.06x faster                                                        |
| xml_etree_generate         | 53.5 ms                                                     | 50.7 ms: 1.05x faster                                                       |
| k_core                     | 1.70 sec                                                    | 1.61 sec: 1.05x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.93 us: 1.05x faster                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.53 us: 1.04x faster                                                       |
| connected_components       | 320 ms                                                      | 312 ms: 1.03x faster                                                        |
| xml_etree_parse            | 92.2 ms                                                     | 89.9 ms: 1.02x faster                                                       |
| shortest_path              | 355 ms                                                      | 347 ms: 1.02x faster                                                        |
| regex_dna                  | 115 ms                                                      | 113 ms: 1.02x faster                                                        |
| json_loads                 | 15.1 us                                                     | 14.8 us: 1.02x faster                                                       |
| pyflate                    | 283 ms                                                      | 278 ms: 1.02x faster                                                        |
| xml_etree_process          | 36.5 ms                                                     | 36.7 ms: 1.00x slower                                                       |
| python_startup             | 24.4 ms                                                     | 24.6 ms: 1.01x slower                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 85.2 ms: 1.01x slower                                                       |
| pprint_safe_repr           | 485 ms                                                      | 493 ms: 1.02x slower                                                        |
| pprint_pformat             | 977 ms                                                      | 999 ms: 1.02x slower                                                        |
| 2to3                       | 215 ms                                                      | 221 ms: 1.03x slower                                                        |
| spectral_norm              | 63.4 ms                                                     | 65.3 ms: 1.03x slower                                                       |
| regex_compile              | 80.7 ms                                                     | 83.4 ms: 1.03x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 74.6 ms: 1.04x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 47.4 ms: 1.04x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 843 us: 1.04x slower                                                        |
| generators                 | 19.0 ms                                                     | 19.8 ms: 1.04x slower                                                       |
| html5lib                   | 38.2 ms                                                     | 39.9 ms: 1.04x slower                                                       |
| pidigits                   | 146 ms                                                      | 154 ms: 1.05x slower                                                        |
| dulwich_log                | 40.1 ms                                                     | 42.1 ms: 1.05x slower                                                       |
| asyncio_websockets         | 300 ms                                                      | 315 ms: 1.05x slower                                                        |
| async_generators           | 223 ms                                                      | 234 ms: 1.05x slower                                                        |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.6 ms: 1.05x slower                                                       |
| coverage                   | 45.3 ms                                                     | 47.6 ms: 1.05x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 89.7 ms: 1.05x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 109 us: 1.05x slower                                                        |
| go                         | 84.7 ms                                                     | 89.5 ms: 1.06x slower                                                       |
| comprehensions             | 10.4 us                                                     | 11.0 us: 1.06x slower                                                       |
| pycparser                  | 695 ms                                                      | 735 ms: 1.06x slower                                                        |
| sympy_str                  | 167 ms                                                      | 177 ms: 1.06x slower                                                        |
| sphinx                     | 617 ms                                                      | 654 ms: 1.06x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.3 ms: 1.06x slower                                                       |
| sympy_expand               | 286 ms                                                      | 306 ms: 1.07x slower                                                        |
| genshi_text                | 15.2 ms                                                     | 16.4 ms: 1.08x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 6.70 ms: 1.08x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.4 ms: 1.08x slower                                                       |
| sqlglot_parse              | 764 us                                                      | 831 us: 1.09x slower                                                        |
| nqueens                    | 56.1 ms                                                     | 61.1 ms: 1.09x slower                                                       |
| genshi_xml                 | 33.9 ms                                                     | 36.9 ms: 1.09x slower                                                       |
| mdp                        | 1.43 sec                                                    | 1.56 sec: 1.09x slower                                                      |
| sqlglot_transpile          | 953 us                                                      | 1.06 ms: 1.11x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.41 us: 1.11x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.71 sec: 1.12x slower                                                      |
| sqlglot_optimize           | 32.5 ms                                                     | 36.3 ms: 1.12x slower                                                       |
| chaos                      | 37.9 ms                                                     | 42.4 ms: 1.12x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.92 us: 1.12x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 19.0 ms: 1.12x slower                                                       |
| sqlglot_normalize          | 172 ms                                                      | 195 ms: 1.14x slower                                                        |
| richards_super             | 29.8 ms                                                     | 34.1 ms: 1.15x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 213 us: 1.15x slower                                                        |
| scimark_lu                 | 56.7 ms                                                     | 65.1 ms: 1.15x slower                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 47.1 ms: 1.16x slower                                                       |
| richards                   | 26.3 ms                                                     | 30.5 ms: 1.16x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.48 ms: 1.17x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 90.1 ms: 1.18x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 64.7 ns: 1.19x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.25 ms: 1.19x slower                                                       |
| many_optionals             | 361 us                                                      | 446 us: 1.23x slower                                                        |
| raytrace                   | 153 ms                                                      | 192 ms: 1.25x slower                                                        |
| django_template            | 20.3 ms                                                     | 25.5 ms: 1.25x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 16.3 ms: 1.50x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (3): pylint, create_gc_cycles, gc_traversal
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (8) of results/bm-20250222-3.14.0a5+-5ec4bf8-JIT/bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.032x faster

# HPT report

- Reliability score: 87.55% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown