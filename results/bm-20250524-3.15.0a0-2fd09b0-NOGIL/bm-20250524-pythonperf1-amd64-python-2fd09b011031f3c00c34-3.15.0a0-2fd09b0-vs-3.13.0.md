# Results vs. 3.13.0

- fork: python
- ref: 2fd09b011031f3c00c34
- machine: windows-amd64
- commit hash: 2fd09b0
- commit date: 2025-05-24
- overall geometric mean: 1.058x slower
- HPT reliability: 99.96%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 226 ms: 1.05x slower                                                       |
| docutils       | 1.53 sec                                                    | 2.93 sec: 1.91x slower                                                     |
| html5lib       | 38.2 ms                                                     | 40.7 ms: 1.06x slower                                                      |
| sphinx         | 617 ms                                                      | 677 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                       | 1.24x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 143 ms: 2.10x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 330 ms: 1.50x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 191 ms: 1.47x faster                                                       |
| async_tree_io              | 513 ms                                                      | 351 ms: 1.46x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 148 ms: 1.36x faster                                                       |
| async_tree_none            | 219 ms                                                      | 172 ms: 1.28x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 212 ms: 1.25x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 310 ms: 1.23x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 331 ms: 1.15x faster                                                       |
| coroutines                 | 12.5 ms                                                     | 13.3 ms: 1.06x slower                                                      |
| async_generators           | 223 ms                                                      | 273 ms: 1.22x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.29x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 46.2 ms: 1.10x faster                                                      |
| pidigits       | 146 ms                                                      | 135 ms: 1.08x faster                                                       |
| nbody          | 66.3 ms                                                     | 81.6 ms: 1.23x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.3 ms: 1.80x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.54 ms: 1.10x faster                                                      |
| regex_dna      | 115 ms                                                      | 114 ms: 1.01x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 95.8 ms: 1.19x slower                                                      |
| Geometric mean | (ref)                                                       | 1.14x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 60.5 ms                                                     | 57.4 ms: 1.06x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 90.3 ms: 1.02x faster                                                      |
| json_dumps           | 6.19 ms                                                     | 6.72 ms: 1.09x slower                                                      |
| json_loads           | 15.1 us                                                     | 16.8 us: 1.11x slower                                                      |
| unpickle_pure_python | 130 us                                                      | 153 us: 1.18x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 63.6 ms: 1.19x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 45.1 ms: 1.24x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 232 us: 1.25x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 2.68 sec: 1.95x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.19x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.9 ms                                                     | 18.4 ms: 1.09x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 40.4 ms: 1.19x slower                                                      |
| genshi_text     | 15.2 ms                                                     | 19.5 ms: 1.28x slower                                                      |
| django_template | 20.3 ms                                                     | 27.5 ms: 1.35x slower                                                      |
| mako            | 6.56 ms                                                     | 9.66 ms: 1.47x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.32x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 571 us: 14.82x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 29.8 ms: 2.52x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 143 ms: 2.10x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 13.3 ms: 1.80x faster                                                      |
| gc_traversal               | 1.96 ms                                                     | 1.17 ms: 1.67x faster                                                      |
| async_tree_io_tg           | 497 ms                                                      | 330 ms: 1.50x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 191 ms: 1.47x faster                                                       |
| async_tree_io              | 513 ms                                                      | 351 ms: 1.46x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 148 ms: 1.36x faster                                                       |
| async_tree_none            | 219 ms                                                      | 172 ms: 1.28x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 212 ms: 1.25x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 310 ms: 1.23x faster                                                       |
| mdp                        | 1.43 sec                                                    | 1.17 sec: 1.22x faster                                                     |
| create_gc_cycles           | 1.22 ms                                                     | 1.00 ms: 1.22x faster                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.33 us: 1.19x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 331 ms: 1.15x faster                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 75.7 ms: 1.11x faster                                                      |
| float                      | 50.8 ms                                                     | 46.2 ms: 1.10x faster                                                      |
| deepcopy                   | 223 us                                                      | 203 us: 1.10x faster                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.54 ms: 1.10x faster                                                      |
| pidigits                   | 146 ms                                                      | 135 ms: 1.08x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 21.8 us: 1.06x faster                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 57.4 ms: 1.06x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 90.3 ms: 1.02x faster                                                      |
| regex_dna                  | 115 ms                                                      | 114 ms: 1.01x faster                                                       |
| dulwich_log                | 40.1 ms                                                     | 41.3 ms: 1.03x slower                                                      |
| pycparser                  | 695 ms                                                      | 725 ms: 1.04x slower                                                       |
| 2to3                       | 215 ms                                                      | 226 ms: 1.05x slower                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 2.14 us: 1.06x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 13.3 ms: 1.06x slower                                                      |
| html5lib                   | 38.2 ms                                                     | 40.7 ms: 1.06x slower                                                      |
| json_dumps                 | 6.19 ms                                                     | 6.72 ms: 1.09x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 18.4 ms: 1.09x slower                                                      |
| spectral_norm              | 63.4 ms                                                     | 69.2 ms: 1.09x slower                                                      |
| telco                      | 4.85 ms                                                     | 5.32 ms: 1.10x slower                                                      |
| sphinx                     | 617 ms                                                      | 677 ms: 1.10x slower                                                       |
| go                         | 84.7 ms                                                     | 93.4 ms: 1.10x slower                                                      |
| json_loads                 | 15.1 us                                                     | 16.8 us: 1.11x slower                                                      |
| pyflate                    | 283 ms                                                      | 320 ms: 1.13x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 86.4 ms: 1.13x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 64.6 ms: 1.14x slower                                                      |
| sympy_expand               | 286 ms                                                      | 326 ms: 1.14x slower                                                       |
| sympy_str                  | 167 ms                                                      | 190 ms: 1.14x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 97.4 ms: 1.14x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 14.2 ms: 1.15x slower                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 3.04 ms: 1.17x slower                                                      |
| generators                 | 19.0 ms                                                     | 22.2 ms: 1.17x slower                                                      |
| fannkuch                   | 252 ms                                                      | 296 ms: 1.18x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 153 us: 1.18x slower                                                       |
| regex_compile              | 80.7 ms                                                     | 95.8 ms: 1.19x slower                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 63.6 ms: 1.19x slower                                                      |
| genshi_xml                 | 33.9 ms                                                     | 40.4 ms: 1.19x slower                                                      |
| scimark_fft                | 175 ms                                                      | 209 ms: 1.20x slower                                                       |
| chaos                      | 37.9 ms                                                     | 45.4 ms: 1.20x slower                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 55.5 ms: 1.22x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.69 ms: 1.22x slower                                                      |
| async_generators           | 223 ms                                                      | 273 ms: 1.22x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 88.3 ms: 1.23x slower                                                      |
| logging_format             | 6.18 us                                                     | 7.60 us: 1.23x slower                                                      |
| nbody                      | 66.3 ms                                                     | 81.6 ms: 1.23x slower                                                      |
| logging_simple             | 5.77 us                                                     | 7.12 us: 1.23x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 45.1 ms: 1.24x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 232 us: 1.25x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 70.8 ms: 1.26x slower                                                      |
| comprehensions             | 10.4 us                                                     | 13.1 us: 1.26x slower                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 51.4 ms: 1.26x slower                                                      |
| genshi_text                | 15.2 ms                                                     | 19.5 ms: 1.28x slower                                                      |
| richards                   | 26.3 ms                                                     | 33.8 ms: 1.29x slower                                                      |
| typing_runtime_protocols   | 103 us                                                      | 133 us: 1.29x slower                                                       |
| pprint_safe_repr           | 485 ms                                                      | 628 ms: 1.30x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.46 ms: 1.30x slower                                                      |
| richards_super             | 29.8 ms                                                     | 39.7 ms: 1.33x slower                                                      |
| many_optionals             | 361 us                                                      | 482 us: 1.33x slower                                                       |
| django_template            | 20.3 ms                                                     | 27.5 ms: 1.35x slower                                                      |
| bench_thread_pool          | 810 us                                                      | 1.12 ms: 1.38x slower                                                      |
| raytrace                   | 153 ms                                                      | 214 ms: 1.40x slower                                                       |
| mako                       | 6.56 ms                                                     | 9.66 ms: 1.47x slower                                                      |
| coverage                   | 45.3 ms                                                     | 66.7 ms: 1.47x slower                                                      |
| k_core                     | 1.70 sec                                                    | 2.67 sec: 1.57x slower                                                     |
| subparsers                 | 10.9 ms                                                     | 19.3 ms: 1.78x slower                                                      |
| shortest_path              | 355 ms                                                      | 642 ms: 1.81x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 5.44 sec: 1.89x slower                                                     |
| docutils                   | 1.53 sec                                                    | 2.93 sec: 1.91x slower                                                     |
| connected_components       | 320 ms                                                      | 615 ms: 1.92x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 2.68 sec: 1.95x slower                                                     |
| pprint_pformat             | 977 ms                                                      | 2.13 sec: 2.18x slower                                                     |
| logging_silent             | 54.6 ns                                                     | 371 ns: 6.81x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.09x slower                                                               |

Benchmark hidden because not significant (3): json, pylint, python_startup
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250524-3.15.0a0-2fd09b0-NOGIL/bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.058x slower

# HPT report

- Reliability score: 99.96% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown