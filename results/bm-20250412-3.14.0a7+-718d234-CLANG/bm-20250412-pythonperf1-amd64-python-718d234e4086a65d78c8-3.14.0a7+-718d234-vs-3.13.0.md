# Results vs. 3.13.0

- fork: python
- ref: 718d234e4086a65d78c8
- machine: windows-amd64
- commit hash: 718d234
- commit date: 2025-04-12
- overall geometric mean: 1.197x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7+-718d234 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 202 ms: 1.07x faster                                                        |
| docutils       | 1.53 sec                                                    | 1.54 sec: 1.00x slower                                                      |
| html5lib       | 38.2 ms                                                     | 34.1 ms: 1.12x faster                                                       |
| sphinx         | 617 ms                                                      | 596 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7+-718d234 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 161 ms: 1.86x faster                                                        |
| async_tree_io              | 513 ms                                                      | 339 ms: 1.51x faster                                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 193 ms: 1.45x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 184 ms: 1.44x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 348 ms: 1.43x faster                                                        |
| async_tree_none            | 219 ms                                                      | 155 ms: 1.42x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 148 ms: 1.35x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 308 ms: 1.23x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 315 ms: 1.22x faster                                                        |
| async_generators           | 223 ms                                                      | 184 ms: 1.21x faster                                                        |
| coroutines                 | 12.5 ms                                                     | 10.9 ms: 1.15x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.38x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7+-718d234 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 36.1 ms: 1.41x faster                                                       |
| nbody          | 66.3 ms                                                     | 51.5 ms: 1.29x faster                                                       |
| Geometric mean | (ref)                                                       | 1.22x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7+-718d234 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.5 ms: 1.77x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 66.8 ms: 1.21x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.60 ms: 1.06x faster                                                       |
| regex_dna      | 115 ms                                                      | 121 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                       | 1.21x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7+-718d234 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.01 sec: 1.35x faster                                                      |
| unpickle_pure_python | 130 us                                                      | 104 us: 1.25x faster                                                        |
| pickle_pure_python   | 186 us                                                      | 165 us: 1.13x faster                                                        |
| xml_etree_generate   | 53.5 ms                                                     | 47.6 ms: 1.12x faster                                                       |
| xml_etree_process    | 36.5 ms                                                     | 32.7 ms: 1.12x faster                                                       |
| json_loads           | 15.1 us                                                     | 13.6 us: 1.11x faster                                                       |
| json_dumps           | 6.19 ms                                                     | 5.78 ms: 1.07x faster                                                       |
| xml_etree_parse      | 92.2 ms                                                     | 90.0 ms: 1.02x faster                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 61.6 ms: 1.02x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7+-718d234 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.8 ms: 1.10x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 20.8 ms: 1.23x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.16x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7+-718d234 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 15.2 ms                                                     | 11.2 ms: 1.36x faster                                                       |
| genshi_xml      | 33.9 ms                                                     | 26.9 ms: 1.26x faster                                                       |
| mako            | 6.56 ms                                                     | 5.75 ms: 1.14x faster                                                       |
| django_template | 20.3 ms                                                     | 19.5 ms: 1.04x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.19x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7+-718d234 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 30.7 ms: 2.45x faster                                                       |
| mdp                        | 1.43 sec                                                    | 667 ms: 2.15x faster                                                        |
| asyncio_websockets         | 300 ms                                                      | 161 ms: 1.86x faster                                                        |
| regex_v8                   | 23.8 ms                                                     | 13.5 ms: 1.77x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 13.3 us: 1.73x faster                                                       |
| deepcopy                   | 223 us                                                      | 136 us: 1.65x faster                                                        |
| scimark_sor                | 76.2 ms                                                     | 47.7 ms: 1.60x faster                                                       |
| async_tree_io              | 513 ms                                                      | 339 ms: 1.51x faster                                                        |
| scimark_monte_carlo        | 40.7 ms                                                     | 27.3 ms: 1.49x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 193 ms: 1.45x faster                                                        |
| go                         | 84.7 ms                                                     | 58.5 ms: 1.45x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 184 ms: 1.44x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 348 ms: 1.43x faster                                                        |
| async_tree_none            | 219 ms                                                      | 155 ms: 1.42x faster                                                        |
| float                      | 50.8 ms                                                     | 36.1 ms: 1.41x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.46 us: 1.39x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 46.5 ms: 1.36x faster                                                       |
| genshi_text                | 15.2 ms                                                     | 11.2 ms: 1.36x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.01 sec: 1.35x faster                                                      |
| async_tree_none_tg         | 200 ms                                                      | 148 ms: 1.35x faster                                                        |
| hexiom                     | 3.84 ms                                                     | 2.85 ms: 1.35x faster                                                       |
| fannkuch                   | 252 ms                                                      | 190 ms: 1.32x faster                                                        |
| pprint_safe_repr           | 485 ms                                                      | 375 ms: 1.29x faster                                                        |
| logging_silent             | 54.6 ns                                                     | 42.4 ns: 1.29x faster                                                       |
| nbody                      | 66.3 ms                                                     | 51.5 ms: 1.29x faster                                                       |
| scimark_fft                | 175 ms                                                      | 137 ms: 1.27x faster                                                        |
| pprint_pformat             | 977 ms                                                      | 770 ms: 1.27x faster                                                        |
| richards                   | 26.3 ms                                                     | 20.8 ms: 1.26x faster                                                       |
| genshi_xml                 | 33.9 ms                                                     | 26.9 ms: 1.26x faster                                                       |
| scimark_lu                 | 56.7 ms                                                     | 45.0 ms: 1.26x faster                                                       |
| chaos                      | 37.9 ms                                                     | 30.2 ms: 1.26x faster                                                       |
| generators                 | 19.0 ms                                                     | 15.1 ms: 1.26x faster                                                       |
| comprehensions             | 10.4 us                                                     | 8.30 us: 1.25x faster                                                       |
| unpickle_pure_python       | 130 us                                                      | 104 us: 1.25x faster                                                        |
| richards_super             | 29.8 ms                                                     | 24.1 ms: 1.23x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 308 ms: 1.23x faster                                                        |
| pyflate                    | 283 ms                                                      | 231 ms: 1.23x faster                                                        |
| deltablue                  | 1.89 ms                                                     | 1.55 ms: 1.22x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.14 ms: 1.22x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 315 ms: 1.22x faster                                                        |
| async_generators           | 223 ms                                                      | 184 ms: 1.21x faster                                                        |
| regex_compile              | 80.7 ms                                                     | 66.8 ms: 1.21x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.05 ms: 1.20x faster                                                       |
| nqueens                    | 56.1 ms                                                     | 46.9 ms: 1.20x faster                                                       |
| typing_runtime_protocols   | 103 us                                                      | 86.6 us: 1.19x faster                                                       |
| json                       | 3.30 ms                                                     | 2.81 ms: 1.17x faster                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 38.9 ms: 1.17x faster                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.46 sec: 1.17x faster                                                      |
| coroutines                 | 12.5 ms                                                     | 10.9 ms: 1.15x faster                                                       |
| sympy_expand               | 286 ms                                                      | 250 ms: 1.15x faster                                                        |
| mako                       | 6.56 ms                                                     | 5.75 ms: 1.14x faster                                                       |
| sympy_str                  | 167 ms                                                      | 147 ms: 1.14x faster                                                        |
| pickle_pure_python         | 186 us                                                      | 165 us: 1.13x faster                                                        |
| xml_etree_generate         | 53.5 ms                                                     | 47.6 ms: 1.12x faster                                                       |
| html5lib                   | 38.2 ms                                                     | 34.1 ms: 1.12x faster                                                       |
| xml_etree_process          | 36.5 ms                                                     | 32.7 ms: 1.12x faster                                                       |
| sympy_integrate            | 12.3 ms                                                     | 11.0 ms: 1.12x faster                                                       |
| json_loads                 | 15.1 us                                                     | 13.6 us: 1.11x faster                                                       |
| pylint                     | 205 ms                                                      | 186 ms: 1.11x faster                                                        |
| raytrace                   | 153 ms                                                      | 139 ms: 1.10x faster                                                        |
| sympy_sum                  | 85.2 ms                                                     | 77.7 ms: 1.10x faster                                                       |
| dulwich_log                | 40.1 ms                                                     | 37.3 ms: 1.08x faster                                                       |
| meteor_contest             | 72.0 ms                                                     | 67.0 ms: 1.07x faster                                                       |
| pycparser                  | 695 ms                                                      | 648 ms: 1.07x faster                                                        |
| json_dumps                 | 6.19 ms                                                     | 5.78 ms: 1.07x faster                                                       |
| logging_simple             | 5.77 us                                                     | 5.41 us: 1.07x faster                                                       |
| 2to3                       | 215 ms                                                      | 202 ms: 1.07x faster                                                        |
| sqlite_synth               | 1.59 us                                                     | 1.49 us: 1.07x faster                                                       |
| coverage                   | 45.3 ms                                                     | 42.5 ms: 1.07x faster                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.60 ms: 1.06x faster                                                       |
| logging_format             | 6.18 us                                                     | 5.89 us: 1.05x faster                                                       |
| django_template            | 20.3 ms                                                     | 19.5 ms: 1.04x faster                                                       |
| k_core                     | 1.70 sec                                                    | 1.63 sec: 1.04x faster                                                      |
| sphinx                     | 617 ms                                                      | 596 ms: 1.04x faster                                                        |
| xml_etree_parse            | 92.2 ms                                                     | 90.0 ms: 1.02x faster                                                       |
| shortest_path              | 355 ms                                                      | 351 ms: 1.01x faster                                                        |
| docutils                   | 1.53 sec                                                    | 1.54 sec: 1.00x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 61.6 ms: 1.02x slower                                                       |
| connected_components       | 320 ms                                                      | 332 ms: 1.04x slower                                                        |
| bench_thread_pool          | 810 us                                                      | 842 us: 1.04x slower                                                        |
| regex_dna                  | 115 ms                                                      | 121 ms: 1.05x slower                                                        |
| bench_mp_pool              | 84.2 ms                                                     | 89.0 ms: 1.06x slower                                                       |
| many_optionals             | 361 us                                                      | 396 us: 1.10x slower                                                        |
| python_startup             | 24.4 ms                                                     | 26.8 ms: 1.10x slower                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.38 ms: 1.13x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 20.8 ms: 1.23x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 14.6 ms: 1.35x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.86 ms: 1.46x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.19x faster                                                                |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250412-3.14.0a7+-718d234-CLANG/bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7+-718d234.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.197x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown