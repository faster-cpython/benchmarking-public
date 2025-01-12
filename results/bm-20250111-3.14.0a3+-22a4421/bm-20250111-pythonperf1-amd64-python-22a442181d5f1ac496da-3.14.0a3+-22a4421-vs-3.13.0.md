# Results vs. 3.13.0

- fork: python
- ref: 22a442181d5f1ac496da
- machine: windows-amd64
- commit hash: 22a4421
- commit date: 2025-01-11
- overall geometric mean: 1.004x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 224 ms: 1.04x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.67 sec: 1.09x slower                                                      |
| html5lib       | 38.2 ms                                                     | 39.3 ms: 1.03x slower                                                       |
| sphinx         | 617 ms                                                      | 647 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                       | 1.05x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 212 ms: 1.32x faster                                                        |
| async_tree_io              | 513 ms                                                      | 411 ms: 1.25x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 400 ms: 1.24x faster                                                        |
| async_tree_none            | 219 ms                                                      | 188 ms: 1.16x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 228 ms: 1.16x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 173 ms: 1.16x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 345 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 348 ms: 1.09x faster                                                        |
| async_generators           | 223 ms                                                      | 232 ms: 1.04x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.4 ms: 1.07x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.12x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 49.6 ms: 1.02x faster                                                       |
| pidigits       | 146 ms                                                      | 147 ms: 1.00x slower                                                        |
| nbody          | 66.3 ms                                                     | 72.7 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.5 ms: 1.64x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.42 ms: 1.19x faster                                                       |
| regex_dna      | 115 ms                                                      | 112 ms: 1.02x faster                                                        |
| regex_compile  | 80.7 ms                                                     | 85.1 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 89.5 ms: 1.03x faster                                                       |
| json_loads           | 15.1 us                                                     | 14.7 us: 1.03x faster                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 61.4 ms: 1.02x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 56.5 ms: 1.06x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 6.63 ms: 1.07x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 39.8 ms: 1.09x slower                                                       |
| unpickle_pure_python | 130 us                                                      | 143 us: 1.10x slower                                                        |
| pickle_pure_python   | 186 us                                                      | 219 us: 1.18x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.05x slower                                                                |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 23.6 ms: 1.03x faster                                                       |
| python_startup_no_site | 16.9 ms                                                     | 17.2 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.65 ms: 1.01x slower                                                       |
| genshi_xml      | 33.9 ms                                                     | 35.1 ms: 1.04x slower                                                       |
| genshi_text     | 15.2 ms                                                     | 16.1 ms: 1.06x slower                                                       |
| django_template | 20.3 ms                                                     | 25.1 ms: 1.24x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.08x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 520 us: 16.29x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.5 ms: 1.64x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 212 ms: 1.32x faster                                                        |
| async_tree_io              | 513 ms                                                      | 411 ms: 1.25x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 400 ms: 1.24x faster                                                        |
| deepcopy                   | 223 us                                                      | 180 us: 1.24x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.42 ms: 1.19x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 19.8 us: 1.16x faster                                                       |
| async_tree_none            | 219 ms                                                      | 188 ms: 1.16x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 228 ms: 1.16x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 173 ms: 1.16x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 345 ms: 1.11x faster                                                        |
| deepcopy_reduce            | 2.02 us                                                     | 1.85 us: 1.09x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 348 ms: 1.09x faster                                                        |
| python_startup             | 24.4 ms                                                     | 23.6 ms: 1.03x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 61.5 ms: 1.03x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 89.5 ms: 1.03x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.7 us: 1.03x faster                                                       |
| float                      | 50.8 ms                                                     | 49.6 ms: 1.02x faster                                                       |
| regex_dna                  | 115 ms                                                      | 112 ms: 1.02x faster                                                        |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.56 ms: 1.02x faster                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 83.2 ms: 1.01x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.81 ms: 1.01x faster                                                       |
| go                         | 84.7 ms                                                     | 84.1 ms: 1.01x faster                                                       |
| pidigits                   | 146 ms                                                      | 147 ms: 1.00x slower                                                        |
| sqlite_synth               | 1.59 us                                                     | 1.60 us: 1.01x slower                                                       |
| connected_components       | 320 ms                                                      | 322 ms: 1.01x slower                                                        |
| mako                       | 6.56 ms                                                     | 6.65 ms: 1.01x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 61.4 ms: 1.02x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 17.2 ms: 1.02x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.94 sec: 1.02x slower                                                      |
| html5lib                   | 38.2 ms                                                     | 39.3 ms: 1.03x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 47.1 ms: 1.03x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 58.6 ms: 1.03x slower                                                       |
| coverage                   | 45.3 ms                                                     | 46.9 ms: 1.03x slower                                                       |
| genshi_xml                 | 33.9 ms                                                     | 35.1 ms: 1.04x slower                                                       |
| fannkuch                   | 252 ms                                                      | 262 ms: 1.04x slower                                                        |
| pycparser                  | 695 ms                                                      | 723 ms: 1.04x slower                                                        |
| 2to3                       | 215 ms                                                      | 224 ms: 1.04x slower                                                        |
| mdp                        | 1.43 sec                                                    | 1.49 sec: 1.04x slower                                                      |
| async_generators           | 223 ms                                                      | 232 ms: 1.04x slower                                                        |
| sphinx                     | 617 ms                                                      | 647 ms: 1.05x slower                                                        |
| sympy_sum                  | 85.2 ms                                                     | 89.4 ms: 1.05x slower                                                       |
| sympy_str                  | 167 ms                                                      | 176 ms: 1.05x slower                                                        |
| dulwich_log                | 40.1 ms                                                     | 42.3 ms: 1.05x slower                                                       |
| regex_compile              | 80.7 ms                                                     | 85.1 ms: 1.05x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 16.1 ms: 1.06x slower                                                       |
| scimark_fft                | 175 ms                                                      | 185 ms: 1.06x slower                                                        |
| pathlib                    | 75.3 ms                                                     | 79.6 ms: 1.06x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 56.5 ms: 1.06x slower                                                       |
| sympy_expand               | 286 ms                                                      | 302 ms: 1.06x slower                                                        |
| json_dumps                 | 6.19 ms                                                     | 6.63 ms: 1.07x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.2 ms: 1.07x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.4 ms: 1.07x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 77.4 ms: 1.07x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.67 us: 1.08x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.27 us: 1.09x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 39.8 ms: 1.09x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 83.1 ms: 1.09x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.07 sec: 1.09x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.67 sec: 1.09x slower                                                      |
| sqlglot_optimize           | 32.5 ms                                                     | 35.6 ms: 1.09x slower                                                       |
| pprint_safe_repr           | 485 ms                                                      | 531 ms: 1.10x slower                                                        |
| nbody                      | 66.3 ms                                                     | 72.7 ms: 1.10x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 143 us: 1.10x slower                                                        |
| nqueens                    | 56.1 ms                                                     | 61.8 ms: 1.10x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 114 us: 1.11x slower                                                        |
| hexiom                     | 3.84 ms                                                     | 4.25 ms: 1.11x slower                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 45.1 ms: 1.11x slower                                                       |
| chaos                      | 37.9 ms                                                     | 42.3 ms: 1.12x slower                                                       |
| pyflate                    | 283 ms                                                      | 317 ms: 1.12x slower                                                        |
| logging_silent             | 54.6 ns                                                     | 61.1 ns: 1.12x slower                                                       |
| sqlglot_normalize          | 172 ms                                                      | 193 ms: 1.13x slower                                                        |
| sqlglot_parse              | 764 us                                                      | 862 us: 1.13x slower                                                        |
| generators                 | 19.0 ms                                                     | 21.4 ms: 1.13x slower                                                       |
| comprehensions             | 10.4 us                                                     | 11.8 us: 1.13x slower                                                       |
| sqlglot_transpile          | 953 us                                                      | 1.08 ms: 1.14x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.22 ms: 1.17x slower                                                       |
| richards_super             | 29.8 ms                                                     | 34.9 ms: 1.17x slower                                                       |
| richards                   | 26.3 ms                                                     | 30.9 ms: 1.18x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 219 us: 1.18x slower                                                        |
| many_optionals             | 361 us                                                      | 438 us: 1.21x slower                                                        |
| django_template            | 20.3 ms                                                     | 25.1 ms: 1.24x slower                                                       |
| raytrace                   | 153 ms                                                      | 192 ms: 1.25x slower                                                        |
| subparsers                 | 10.9 ms                                                     | 16.0 ms: 1.47x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.00x faster                                                                |

Benchmark hidden because not significant (9): pylint, json, k_core, shortest_path, create_gc_cycles, tomli_loads, asyncio_websockets, gc_traversal, bench_thread_pool
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (8) of results/bm-20250111-3.14.0a3+-22a4421/bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.004x faster

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown