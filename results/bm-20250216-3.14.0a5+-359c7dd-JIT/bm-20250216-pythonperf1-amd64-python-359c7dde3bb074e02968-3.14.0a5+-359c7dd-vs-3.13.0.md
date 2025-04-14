# Results vs. 3.13.0

- fork: python
- ref: 359c7dde3bb074e02968
- machine: windows-amd64
- commit hash: 359c7dd
- commit date: 2025-02-16
- overall geometric mean: 1.036x faster
- HPT reliability: 82.32%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 219 ms: 1.02x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.69 sec: 1.10x slower                                                      |
| html5lib       | 38.2 ms                                                     | 39.8 ms: 1.04x slower                                                       |
| sphinx         | 617 ms                                                      | 647 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                       | 1.05x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 218 ms: 1.29x faster                                                        |
| async_tree_io              | 513 ms                                                      | 415 ms: 1.24x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 413 ms: 1.20x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 222 ms: 1.19x faster                                                        |
| async_tree_none            | 219 ms                                                      | 186 ms: 1.18x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 177 ms: 1.13x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 347 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 347 ms: 1.10x faster                                                        |
| asyncio_websockets         | 300 ms                                                      | 308 ms: 1.03x slower                                                        |
| async_generators           | 223 ms                                                      | 234 ms: 1.05x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.9 ms: 1.11x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.11x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 44.8 ms: 1.14x faster                                                       |
| nbody          | 66.3 ms                                                     | 59.8 ms: 1.11x faster                                                       |
| pidigits       | 146 ms                                                      | 150 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.5 ms: 1.65x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.45 ms: 1.17x faster                                                       |
| regex_dna      | 115 ms                                                      | 114 ms: 1.01x faster                                                        |
| regex_compile  | 80.7 ms                                                     | 82.7 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.21 sec: 1.13x faster                                                      |
| unpickle_pure_python | 130 us                                                      | 118 us: 1.10x faster                                                        |
| xml_etree_generate   | 53.5 ms                                                     | 51.5 ms: 1.04x faster                                                       |
| xml_etree_parse      | 92.2 ms                                                     | 89.1 ms: 1.04x faster                                                       |
| json_loads           | 15.1 us                                                     | 14.8 us: 1.02x faster                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 61.1 ms: 1.01x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 37.0 ms: 1.01x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 6.55 ms: 1.06x slower                                                       |
| pickle_pure_python   | 186 us                                                      | 209 us: 1.13x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.9 ms                                                     | 18.6 ms: 1.10x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.05x slower                                                                |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.34 ms: 1.23x faster                                                       |
| genshi_text     | 15.2 ms                                                     | 16.8 ms: 1.10x slower                                                       |
| genshi_xml      | 33.9 ms                                                     | 39.1 ms: 1.15x slower                                                       |
| django_template | 20.3 ms                                                     | 26.0 ms: 1.28x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.07x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 506 us: 16.72x faster                                                       |
| pathlib                    | 75.3 ms                                                     | 29.1 ms: 2.59x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.5 ms: 1.65x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 218 ms: 1.29x faster                                                        |
| async_tree_io              | 513 ms                                                      | 415 ms: 1.24x faster                                                        |
| mako                       | 6.56 ms                                                     | 5.34 ms: 1.23x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 19.0 us: 1.21x faster                                                       |
| deepcopy                   | 223 us                                                      | 184 us: 1.21x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 413 ms: 1.20x faster                                                        |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.17 ms: 1.20x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 222 ms: 1.19x faster                                                        |
| async_tree_none            | 219 ms                                                      | 186 ms: 1.18x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.45 ms: 1.17x faster                                                       |
| scimark_fft                | 175 ms                                                      | 153 ms: 1.14x faster                                                        |
| float                      | 50.8 ms                                                     | 44.8 ms: 1.14x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.21 sec: 1.13x faster                                                      |
| async_tree_none_tg         | 200 ms                                                      | 177 ms: 1.13x faster                                                        |
| nbody                      | 66.3 ms                                                     | 59.8 ms: 1.11x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 347 ms: 1.10x faster                                                        |
| bpe_tokeniser              | 2.87 sec                                                    | 2.61 sec: 1.10x faster                                                      |
| unpickle_pure_python       | 130 us                                                      | 118 us: 1.10x faster                                                        |
| json                       | 3.30 ms                                                     | 3.01 ms: 1.10x faster                                                       |
| fannkuch                   | 252 ms                                                      | 230 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 347 ms: 1.10x faster                                                        |
| telco                      | 4.85 ms                                                     | 4.47 ms: 1.09x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 59.6 ms: 1.06x faster                                                       |
| pyflate                    | 283 ms                                                      | 271 ms: 1.04x faster                                                        |
| sqlite_synth               | 1.59 us                                                     | 1.52 us: 1.04x faster                                                       |
| k_core                     | 1.70 sec                                                    | 1.63 sec: 1.04x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.94 us: 1.04x faster                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 51.5 ms: 1.04x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 89.1 ms: 1.04x faster                                                       |
| shortest_path              | 355 ms                                                      | 347 ms: 1.02x faster                                                        |
| json_loads                 | 15.1 us                                                     | 14.8 us: 1.02x faster                                                       |
| connected_components       | 320 ms                                                      | 315 ms: 1.02x faster                                                        |
| regex_dna                  | 115 ms                                                      | 114 ms: 1.01x faster                                                        |
| bench_mp_pool              | 84.2 ms                                                     | 83.9 ms: 1.00x faster                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 61.1 ms: 1.01x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 37.0 ms: 1.01x slower                                                       |
| 2to3                       | 215 ms                                                      | 219 ms: 1.02x slower                                                        |
| go                         | 84.7 ms                                                     | 86.2 ms: 1.02x slower                                                       |
| pidigits                   | 146 ms                                                      | 150 ms: 1.02x slower                                                        |
| meteor_contest             | 72.0 ms                                                     | 73.7 ms: 1.02x slower                                                       |
| regex_compile              | 80.7 ms                                                     | 82.7 ms: 1.02x slower                                                       |
| asyncio_websockets         | 300 ms                                                      | 308 ms: 1.03x slower                                                        |
| crypto_pyaes               | 45.6 ms                                                     | 46.9 ms: 1.03x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 843 us: 1.04x slower                                                        |
| dulwich_log                | 40.1 ms                                                     | 41.8 ms: 1.04x slower                                                       |
| html5lib                   | 38.2 ms                                                     | 39.8 ms: 1.04x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 89.1 ms: 1.05x slower                                                       |
| sphinx                     | 617 ms                                                      | 647 ms: 1.05x slower                                                        |
| coverage                   | 45.3 ms                                                     | 47.5 ms: 1.05x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 58.9 ms: 1.05x slower                                                       |
| async_generators           | 223 ms                                                      | 234 ms: 1.05x slower                                                        |
| pycparser                  | 695 ms                                                      | 732 ms: 1.05x slower                                                        |
| pprint_pformat             | 977 ms                                                      | 1.03 sec: 1.06x slower                                                      |
| sympy_str                  | 167 ms                                                      | 176 ms: 1.06x slower                                                        |
| json_dumps                 | 6.19 ms                                                     | 6.55 ms: 1.06x slower                                                       |
| generators                 | 19.0 ms                                                     | 20.1 ms: 1.06x slower                                                       |
| comprehensions             | 10.4 us                                                     | 11.1 us: 1.07x slower                                                       |
| mdp                        | 1.43 sec                                                    | 1.54 sec: 1.07x slower                                                      |
| sympy_expand               | 286 ms                                                      | 307 ms: 1.07x slower                                                        |
| sympy_integrate            | 12.3 ms                                                     | 13.3 ms: 1.08x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 111 us: 1.08x slower                                                        |
| logging_silent             | 54.6 ns                                                     | 59.0 ns: 1.08x slower                                                       |
| pprint_safe_repr           | 485 ms                                                      | 529 ms: 1.09x slower                                                        |
| scimark_monte_carlo        | 40.7 ms                                                     | 44.6 ms: 1.09x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 18.6 ms: 1.10x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 16.8 ms: 1.10x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.37 us: 1.10x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.69 sec: 1.10x slower                                                      |
| logging_format             | 6.18 us                                                     | 6.83 us: 1.11x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 84.3 ms: 1.11x slower                                                       |
| richards_super             | 29.8 ms                                                     | 33.0 ms: 1.11x slower                                                       |
| richards                   | 26.3 ms                                                     | 29.1 ms: 1.11x slower                                                       |
| chaos                      | 37.9 ms                                                     | 42.0 ms: 1.11x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 63.0 ms: 1.11x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.9 ms: 1.11x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.28 ms: 1.11x slower                                                       |
| sqlglot_parse              | 764 us                                                      | 854 us: 1.12x slower                                                        |
| pickle_pure_python         | 186 us                                                      | 209 us: 1.13x slower                                                        |
| sqlglot_transpile          | 953 us                                                      | 1.08 ms: 1.13x slower                                                       |
| sqlglot_optimize           | 32.5 ms                                                     | 36.8 ms: 1.13x slower                                                       |
| genshi_xml                 | 33.9 ms                                                     | 39.1 ms: 1.15x slower                                                       |
| sqlglot_normalize          | 172 ms                                                      | 199 ms: 1.16x slower                                                        |
| deltablue                  | 1.89 ms                                                     | 2.23 ms: 1.18x slower                                                       |
| many_optionals             | 361 us                                                      | 453 us: 1.25x slower                                                        |
| raytrace                   | 153 ms                                                      | 194 ms: 1.27x slower                                                        |
| django_template            | 20.3 ms                                                     | 26.0 ms: 1.28x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 16.2 ms: 1.50x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (4): pylint, python_startup, create_gc_cycles, gc_traversal
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (8) of results/bm-20250216-3.14.0a5+-359c7dd-JIT/bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.036x faster

# HPT report

- Reliability score: 82.32% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown