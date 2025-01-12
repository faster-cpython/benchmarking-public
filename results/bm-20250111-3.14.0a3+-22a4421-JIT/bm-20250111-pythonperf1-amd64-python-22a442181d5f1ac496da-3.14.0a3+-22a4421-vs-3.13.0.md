# Results vs. 3.13.0

- fork: python
- ref: 22a442181d5f1ac496da
- machine: windows-amd64
- commit hash: 22a4421
- commit date: 2025-01-11
- overall geometric mean: 1.035x faster
- HPT reliability: 69.04%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 225 ms: 1.04x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.74 sec: 1.14x slower                                                      |
| html5lib       | 38.2 ms                                                     | 39.3 ms: 1.03x slower                                                       |
| sphinx         | 617 ms                                                      | 667 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                       | 1.07x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 216 ms: 1.30x faster                                                        |
| async_tree_io              | 513 ms                                                      | 405 ms: 1.27x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 398 ms: 1.25x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 224 ms: 1.18x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 170 ms: 1.18x faster                                                        |
| async_tree_none            | 219 ms                                                      | 187 ms: 1.17x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 344 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 351 ms: 1.08x faster                                                        |
| coroutines                 | 12.5 ms                                                     | 13.5 ms: 1.08x slower                                                       |
| async_generators           | 223 ms                                                      | 261 ms: 1.17x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.11x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 39.3 ms: 1.29x faster                                                       |
| nbody          | 66.3 ms                                                     | 53.9 ms: 1.23x faster                                                       |
| pidigits       | 146 ms                                                      | 147 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 15.0 ms: 1.59x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.48 ms: 1.15x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 79.5 ms: 1.02x faster                                                       |
| regex_dna      | 115 ms                                                      | 116 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 130 us                                                      | 108 us: 1.21x faster                                                        |
| tomli_loads          | 1.37 sec                                                    | 1.19 sec: 1.15x faster                                                      |
| json_loads           | 15.1 us                                                     | 14.3 us: 1.05x faster                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 51.2 ms: 1.04x faster                                                       |
| xml_etree_parse      | 92.2 ms                                                     | 88.5 ms: 1.04x faster                                                       |
| xml_etree_process    | 36.5 ms                                                     | 36.2 ms: 1.01x faster                                                       |
| json_dumps           | 6.19 ms                                                     | 6.28 ms: 1.01x slower                                                       |
| pickle_pure_python   | 186 us                                                      | 208 us: 1.12x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 23.6 ms: 1.03x faster                                                       |
| python_startup_no_site | 16.9 ms                                                     | 17.3 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.08 ms: 1.29x faster                                                       |
| genshi_text     | 15.2 ms                                                     | 18.3 ms: 1.20x slower                                                       |
| django_template | 20.3 ms                                                     | 27.5 ms: 1.36x slower                                                       |
| genshi_xml      | 33.9 ms                                                     | 46.0 ms: 1.36x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.14x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 529 us: 16.00x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 15.0 ms: 1.59x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 16.3 us: 1.41x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 216 ms: 1.30x faster                                                        |
| float                      | 50.8 ms                                                     | 39.3 ms: 1.29x faster                                                       |
| mako                       | 6.56 ms                                                     | 5.08 ms: 1.29x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.04 ms: 1.28x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 49.8 ms: 1.27x faster                                                       |
| async_tree_io              | 513 ms                                                      | 405 ms: 1.27x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 398 ms: 1.25x faster                                                        |
| scimark_sor                | 76.2 ms                                                     | 61.3 ms: 1.24x faster                                                       |
| nbody                      | 66.3 ms                                                     | 53.9 ms: 1.23x faster                                                       |
| scimark_fft                | 175 ms                                                      | 143 ms: 1.22x faster                                                        |
| unpickle_pure_python       | 130 us                                                      | 108 us: 1.21x faster                                                        |
| deepcopy                   | 223 us                                                      | 188 us: 1.19x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 224 ms: 1.18x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 170 ms: 1.18x faster                                                        |
| async_tree_none            | 219 ms                                                      | 187 ms: 1.17x faster                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.19 sec: 1.15x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.48 ms: 1.15x faster                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 36.4 ms: 1.12x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.35 ms: 1.11x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 344 ms: 1.11x faster                                                        |
| json                       | 3.30 ms                                                     | 2.98 ms: 1.11x faster                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 41.2 ms: 1.11x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.83 us: 1.10x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 351 ms: 1.08x faster                                                        |
| bpe_tokeniser              | 2.87 sec                                                    | 2.66 sec: 1.08x faster                                                      |
| scimark_lu                 | 56.7 ms                                                     | 53.0 ms: 1.07x faster                                                       |
| k_core                     | 1.70 sec                                                    | 1.61 sec: 1.06x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.3 us: 1.05x faster                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 51.2 ms: 1.04x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 88.5 ms: 1.04x faster                                                       |
| python_startup             | 24.4 ms                                                     | 23.6 ms: 1.03x faster                                                       |
| pprint_pformat             | 977 ms                                                      | 948 ms: 1.03x faster                                                        |
| pyflate                    | 283 ms                                                      | 276 ms: 1.02x faster                                                        |
| shortest_path              | 355 ms                                                      | 347 ms: 1.02x faster                                                        |
| connected_components       | 320 ms                                                      | 313 ms: 1.02x faster                                                        |
| fannkuch                   | 252 ms                                                      | 247 ms: 1.02x faster                                                        |
| pprint_safe_repr           | 485 ms                                                      | 476 ms: 1.02x faster                                                        |
| regex_compile              | 80.7 ms                                                     | 79.5 ms: 1.02x faster                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.57 us: 1.01x faster                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 83.5 ms: 1.01x faster                                                       |
| xml_etree_process          | 36.5 ms                                                     | 36.2 ms: 1.01x faster                                                       |
| pidigits                   | 146 ms                                                      | 147 ms: 1.00x slower                                                        |
| regex_dna                  | 115 ms                                                      | 116 ms: 1.01x slower                                                        |
| dulwich_log                | 40.1 ms                                                     | 40.6 ms: 1.01x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 6.28 ms: 1.01x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 17.3 ms: 1.02x slower                                                       |
| html5lib                   | 38.2 ms                                                     | 39.3 ms: 1.03x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 74.2 ms: 1.03x slower                                                       |
| mdp                        | 1.43 sec                                                    | 1.49 sec: 1.04x slower                                                      |
| sympy_str                  | 167 ms                                                      | 174 ms: 1.04x slower                                                        |
| sympy_expand               | 286 ms                                                      | 297 ms: 1.04x slower                                                        |
| bench_thread_pool          | 810 us                                                      | 844 us: 1.04x slower                                                        |
| logging_silent             | 54.6 ns                                                     | 57.0 ns: 1.04x slower                                                       |
| 2to3                       | 215 ms                                                      | 225 ms: 1.04x slower                                                        |
| coverage                   | 45.3 ms                                                     | 47.7 ms: 1.05x slower                                                       |
| pycparser                  | 695 ms                                                      | 734 ms: 1.06x slower                                                        |
| go                         | 84.7 ms                                                     | 89.8 ms: 1.06x slower                                                       |
| pathlib                    | 75.3 ms                                                     | 79.9 ms: 1.06x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 90.5 ms: 1.06x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.62 us: 1.07x slower                                                       |
| sqlglot_parse              | 764 us                                                      | 820 us: 1.07x slower                                                        |
| logging_simple             | 5.77 us                                                     | 6.21 us: 1.08x slower                                                       |
| sphinx                     | 617 ms                                                      | 667 ms: 1.08x slower                                                        |
| chaos                      | 37.9 ms                                                     | 41.0 ms: 1.08x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.5 ms: 1.08x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.4 ms: 1.09x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 114 us: 1.11x slower                                                        |
| sqlglot_transpile          | 953 us                                                      | 1.06 ms: 1.11x slower                                                       |
| comprehensions             | 10.4 us                                                     | 11.6 us: 1.12x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 208 us: 1.12x slower                                                        |
| nqueens                    | 56.1 ms                                                     | 63.5 ms: 1.13x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.74 sec: 1.14x slower                                                      |
| sqlglot_optimize           | 32.5 ms                                                     | 37.1 ms: 1.14x slower                                                       |
| async_generators           | 223 ms                                                      | 261 ms: 1.17x slower                                                        |
| sqlglot_normalize          | 172 ms                                                      | 202 ms: 1.18x slower                                                        |
| genshi_text                | 15.2 ms                                                     | 18.3 ms: 1.20x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.28 ms: 1.20x slower                                                       |
| generators                 | 19.0 ms                                                     | 23.7 ms: 1.25x slower                                                       |
| many_optionals             | 361 us                                                      | 453 us: 1.25x slower                                                        |
| richards_super             | 29.8 ms                                                     | 37.9 ms: 1.27x slower                                                       |
| richards                   | 26.3 ms                                                     | 33.6 ms: 1.28x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 5.00 ms: 1.30x slower                                                       |
| raytrace                   | 153 ms                                                      | 200 ms: 1.31x slower                                                        |
| django_template            | 20.3 ms                                                     | 27.5 ms: 1.36x slower                                                       |
| genshi_xml                 | 33.9 ms                                                     | 46.0 ms: 1.36x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 15.9 ms: 1.46x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (5): create_gc_cycles, xml_etree_iterparse, asyncio_websockets, gc_traversal, pylint
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (8) of results/bm-20250111-3.14.0a3+-22a4421-JIT/bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.035x faster

# HPT report

- Reliability score: 69.04% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown