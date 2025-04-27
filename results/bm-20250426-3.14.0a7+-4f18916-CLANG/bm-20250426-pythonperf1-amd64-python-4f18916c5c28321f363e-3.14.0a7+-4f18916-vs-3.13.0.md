# Results vs. 3.13.0

- fork: python
- ref: 4f18916c5c28321f363e
- machine: windows-amd64
- commit hash: 4f18916
- commit date: 2025-04-26
- overall geometric mean: 1.193x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 201 ms: 1.07x faster                                                        |
| docutils       | 1.53 sec                                                    | 1.54 sec: 1.01x slower                                                      |
| html5lib       | 38.2 ms                                                     | 34.6 ms: 1.10x faster                                                       |
| sphinx         | 617 ms                                                      | 592 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 164 ms: 1.83x faster                                                        |
| async_tree_io              | 513 ms                                                      | 345 ms: 1.49x faster                                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 194 ms: 1.45x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 184 ms: 1.44x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 352 ms: 1.41x faster                                                        |
| async_tree_none            | 219 ms                                                      | 156 ms: 1.40x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 149 ms: 1.34x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 313 ms: 1.21x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 318 ms: 1.20x faster                                                        |
| async_generators           | 223 ms                                                      | 187 ms: 1.19x faster                                                        |
| coroutines                 | 12.5 ms                                                     | 11.0 ms: 1.14x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.36x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 35.9 ms: 1.41x faster                                                       |
| nbody          | 66.3 ms                                                     | 54.1 ms: 1.23x faster                                                       |
| pidigits       | 146 ms                                                      | 146 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                       | 1.20x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 12.7 ms: 1.88x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 67.2 ms: 1.20x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.50 ms: 1.13x faster                                                       |
| regex_dna      | 115 ms                                                      | 119 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                       | 1.25x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.03 sec: 1.33x faster                                                      |
| unpickle_pure_python | 130 us                                                      | 102 us: 1.27x faster                                                        |
| xml_etree_generate   | 53.5 ms                                                     | 46.9 ms: 1.14x faster                                                       |
| pickle_pure_python   | 186 us                                                      | 164 us: 1.13x faster                                                        |
| xml_etree_process    | 36.5 ms                                                     | 32.7 ms: 1.12x faster                                                       |
| json_loads           | 15.1 us                                                     | 14.0 us: 1.08x faster                                                       |
| json_dumps           | 6.19 ms                                                     | 5.87 ms: 1.06x faster                                                       |
| xml_etree_parse      | 92.2 ms                                                     | 90.4 ms: 1.02x faster                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 68.1 ms: 1.13x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.11x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 27.9 ms: 1.14x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 20.8 ms: 1.23x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.18x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 15.2 ms                                                     | 11.2 ms: 1.36x faster                                                       |
| genshi_xml      | 33.9 ms                                                     | 26.6 ms: 1.27x faster                                                       |
| mako            | 6.56 ms                                                     | 5.98 ms: 1.10x faster                                                       |
| django_template | 20.3 ms                                                     | 19.8 ms: 1.02x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.18x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 31.0 ms: 2.43x faster                                                       |
| mdp                        | 1.43 sec                                                    | 672 ms: 2.13x faster                                                        |
| regex_v8                   | 23.8 ms                                                     | 12.7 ms: 1.88x faster                                                       |
| asyncio_websockets         | 300 ms                                                      | 164 ms: 1.83x faster                                                        |
| deepcopy_memo              | 23.1 us                                                     | 13.0 us: 1.77x faster                                                       |
| deepcopy                   | 223 us                                                      | 135 us: 1.66x faster                                                        |
| scimark_sor                | 76.2 ms                                                     | 47.2 ms: 1.61x faster                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 26.8 ms: 1.52x faster                                                       |
| async_tree_io              | 513 ms                                                      | 345 ms: 1.49x faster                                                        |
| go                         | 84.7 ms                                                     | 58.1 ms: 1.46x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 194 ms: 1.45x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 184 ms: 1.44x faster                                                        |
| float                      | 50.8 ms                                                     | 35.9 ms: 1.41x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 352 ms: 1.41x faster                                                        |
| deepcopy_reduce            | 2.02 us                                                     | 1.44 us: 1.41x faster                                                       |
| async_tree_none            | 219 ms                                                      | 156 ms: 1.40x faster                                                        |
| spectral_norm              | 63.4 ms                                                     | 46.2 ms: 1.37x faster                                                       |
| genshi_text                | 15.2 ms                                                     | 11.2 ms: 1.36x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 149 ms: 1.34x faster                                                        |
| hexiom                     | 3.84 ms                                                     | 2.87 ms: 1.34x faster                                                       |
| logging_silent             | 54.6 ns                                                     | 40.9 ns: 1.33x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.03 sec: 1.33x faster                                                      |
| fannkuch                   | 252 ms                                                      | 194 ms: 1.29x faster                                                        |
| genshi_xml                 | 33.9 ms                                                     | 26.6 ms: 1.27x faster                                                       |
| unpickle_pure_python       | 130 us                                                      | 102 us: 1.27x faster                                                        |
| generators                 | 19.0 ms                                                     | 15.0 ms: 1.27x faster                                                       |
| richards                   | 26.3 ms                                                     | 21.0 ms: 1.25x faster                                                       |
| pyflate                    | 283 ms                                                      | 228 ms: 1.24x faster                                                        |
| deltablue                  | 1.89 ms                                                     | 1.53 ms: 1.24x faster                                                       |
| chaos                      | 37.9 ms                                                     | 30.7 ms: 1.24x faster                                                       |
| richards_super             | 29.8 ms                                                     | 24.1 ms: 1.23x faster                                                       |
| scimark_fft                | 175 ms                                                      | 142 ms: 1.23x faster                                                        |
| pprint_pformat             | 977 ms                                                      | 793 ms: 1.23x faster                                                        |
| pprint_safe_repr           | 485 ms                                                      | 394 ms: 1.23x faster                                                        |
| comprehensions             | 10.4 us                                                     | 8.45 us: 1.23x faster                                                       |
| nbody                      | 66.3 ms                                                     | 54.1 ms: 1.23x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 313 ms: 1.21x faster                                                        |
| nqueens                    | 56.1 ms                                                     | 46.2 ms: 1.21x faster                                                       |
| scimark_lu                 | 56.7 ms                                                     | 46.8 ms: 1.21x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.15 ms: 1.21x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 318 ms: 1.20x faster                                                        |
| regex_compile              | 80.7 ms                                                     | 67.2 ms: 1.20x faster                                                       |
| async_generators           | 223 ms                                                      | 187 ms: 1.19x faster                                                        |
| telco                      | 4.85 ms                                                     | 4.08 ms: 1.19x faster                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.44 sec: 1.17x faster                                                      |
| typing_runtime_protocols   | 103 us                                                      | 88.9 us: 1.16x faster                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 39.3 ms: 1.16x faster                                                       |
| json                       | 3.30 ms                                                     | 2.88 ms: 1.15x faster                                                       |
| sympy_str                  | 167 ms                                                      | 146 ms: 1.14x faster                                                        |
| xml_etree_generate         | 53.5 ms                                                     | 46.9 ms: 1.14x faster                                                       |
| coroutines                 | 12.5 ms                                                     | 11.0 ms: 1.14x faster                                                       |
| sympy_expand               | 286 ms                                                      | 252 ms: 1.13x faster                                                        |
| pickle_pure_python         | 186 us                                                      | 164 us: 1.13x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.50 ms: 1.13x faster                                                       |
| sympy_integrate            | 12.3 ms                                                     | 10.9 ms: 1.13x faster                                                       |
| xml_etree_process          | 36.5 ms                                                     | 32.7 ms: 1.12x faster                                                       |
| meteor_contest             | 72.0 ms                                                     | 64.6 ms: 1.11x faster                                                       |
| pylint                     | 205 ms                                                      | 186 ms: 1.11x faster                                                        |
| pycparser                  | 695 ms                                                      | 630 ms: 1.10x faster                                                        |
| html5lib                   | 38.2 ms                                                     | 34.6 ms: 1.10x faster                                                       |
| raytrace                   | 153 ms                                                      | 139 ms: 1.10x faster                                                        |
| sympy_sum                  | 85.2 ms                                                     | 77.5 ms: 1.10x faster                                                       |
| mako                       | 6.56 ms                                                     | 5.98 ms: 1.10x faster                                                       |
| coverage                   | 45.3 ms                                                     | 41.5 ms: 1.09x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.0 us: 1.08x faster                                                       |
| 2to3                       | 215 ms                                                      | 201 ms: 1.07x faster                                                        |
| sqlite_synth               | 1.59 us                                                     | 1.49 us: 1.06x faster                                                       |
| json_dumps                 | 6.19 ms                                                     | 5.87 ms: 1.06x faster                                                       |
| dulwich_log                | 40.1 ms                                                     | 38.4 ms: 1.04x faster                                                       |
| k_core                     | 1.70 sec                                                    | 1.63 sec: 1.04x faster                                                      |
| sphinx                     | 617 ms                                                      | 592 ms: 1.04x faster                                                        |
| logging_simple             | 5.77 us                                                     | 5.54 us: 1.04x faster                                                       |
| logging_format             | 6.18 us                                                     | 5.93 us: 1.04x faster                                                       |
| django_template            | 20.3 ms                                                     | 19.8 ms: 1.02x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 90.4 ms: 1.02x faster                                                       |
| shortest_path              | 355 ms                                                      | 352 ms: 1.01x faster                                                        |
| pidigits                   | 146 ms                                                      | 146 ms: 1.00x faster                                                        |
| docutils                   | 1.53 sec                                                    | 1.54 sec: 1.01x slower                                                      |
| connected_components       | 320 ms                                                      | 329 ms: 1.03x slower                                                        |
| regex_dna                  | 115 ms                                                      | 119 ms: 1.04x slower                                                        |
| bench_mp_pool              | 84.2 ms                                                     | 89.5 ms: 1.06x slower                                                       |
| many_optionals             | 361 us                                                      | 399 us: 1.10x slower                                                        |
| create_gc_cycles           | 1.22 ms                                                     | 1.37 ms: 1.12x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 68.1 ms: 1.13x slower                                                       |
| python_startup             | 24.4 ms                                                     | 27.9 ms: 1.14x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 20.8 ms: 1.23x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 14.6 ms: 1.35x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.80 ms: 1.43x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.19x faster                                                                |

Benchmark hidden because not significant (1): bench_thread_pool
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250426-3.14.0a7+-4f18916-CLANG/bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.193x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown