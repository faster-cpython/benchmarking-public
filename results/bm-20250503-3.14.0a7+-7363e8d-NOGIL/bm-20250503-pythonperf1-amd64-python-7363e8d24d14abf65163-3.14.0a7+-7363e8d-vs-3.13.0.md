# Results vs. 3.13.0

- fork: python
- ref: 7363e8d24d14abf65163
- machine: windows-amd64
- commit hash: 7363e8d
- commit date: 2025-05-03
- overall geometric mean: 1.041x slower
- HPT reliability: 99.95%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 227 ms: 1.06x slower                                                        |
| docutils       | 1.53 sec                                                    | 2.98 sec: 1.94x slower                                                      |
| html5lib       | 38.2 ms                                                     | 39.8 ms: 1.04x slower                                                       |
| sphinx         | 617 ms                                                      | 736 ms: 1.19x slower                                                        |
| Geometric mean | (ref)                                                       | 1.26x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 144 ms: 2.08x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 330 ms: 1.51x faster                                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 190 ms: 1.48x faster                                                        |
| async_tree_io              | 513 ms                                                      | 354 ms: 1.45x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 147 ms: 1.36x faster                                                        |
| async_tree_none            | 219 ms                                                      | 169 ms: 1.29x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 209 ms: 1.26x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 310 ms: 1.23x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 332 ms: 1.15x faster                                                        |
| coroutines                 | 12.5 ms                                                     | 13.2 ms: 1.06x slower                                                       |
| async_generators           | 223 ms                                                      | 264 ms: 1.19x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.29x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 45.3 ms: 1.12x faster                                                       |
| pidigits       | 146 ms                                                      | 139 ms: 1.05x faster                                                        |
| nbody          | 66.3 ms                                                     | 78.9 ms: 1.19x slower                                                       |
| Geometric mean | (ref)                                                       | 1.00x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.1 ms: 1.81x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.57 ms: 1.08x faster                                                       |
| regex_dna      | 115 ms                                                      | 113 ms: 1.02x faster                                                        |
| regex_compile  | 80.7 ms                                                     | 90.8 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 60.5 ms                                                     | 58.4 ms: 1.04x faster                                                       |
| xml_etree_parse      | 92.2 ms                                                     | 90.6 ms: 1.02x faster                                                       |
| json_loads           | 15.1 us                                                     | 17.0 us: 1.13x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 60.7 ms: 1.13x slower                                                       |
| unpickle_pure_python | 130 us                                                      | 148 us: 1.14x slower                                                        |
| json_dumps           | 6.19 ms                                                     | 7.22 ms: 1.17x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 43.3 ms: 1.19x slower                                                       |
| pickle_pure_python   | 186 us                                                      | 223 us: 1.20x slower                                                        |
| tomli_loads          | 1.37 sec                                                    | 2.59 sec: 1.89x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.18x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.8 ms: 1.06x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 19.5 ms: 1.15x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 37.9 ms: 1.12x slower                                                       |
| genshi_text     | 15.2 ms                                                     | 18.7 ms: 1.23x slower                                                       |
| django_template | 20.3 ms                                                     | 26.2 ms: 1.29x slower                                                       |
| mako            | 6.56 ms                                                     | 9.76 ms: 1.49x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.27x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 573 us: 14.77x faster                                                       |
| pathlib                    | 75.3 ms                                                     | 32.2 ms: 2.34x faster                                                       |
| asyncio_websockets         | 300 ms                                                      | 144 ms: 2.08x faster                                                        |
| regex_v8                   | 23.8 ms                                                     | 13.1 ms: 1.81x faster                                                       |
| gc_traversal               | 1.96 ms                                                     | 1.14 ms: 1.72x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 330 ms: 1.51x faster                                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 190 ms: 1.48x faster                                                        |
| async_tree_io              | 513 ms                                                      | 354 ms: 1.45x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 147 ms: 1.36x faster                                                        |
| mdp                        | 1.43 sec                                                    | 1.08 sec: 1.32x faster                                                      |
| async_tree_none            | 219 ms                                                      | 169 ms: 1.29x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 209 ms: 1.26x faster                                                        |
| create_gc_cycles           | 1.22 ms                                                     | 982 us: 1.25x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 310 ms: 1.23x faster                                                        |
| deepcopy                   | 223 us                                                      | 192 us: 1.16x faster                                                        |
| sqlite_synth               | 1.59 us                                                     | 1.37 us: 1.16x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 332 ms: 1.15x faster                                                        |
| float                      | 50.8 ms                                                     | 45.3 ms: 1.12x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 20.7 us: 1.11x faster                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 76.7 ms: 1.10x faster                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.57 ms: 1.08x faster                                                       |
| pidigits                   | 146 ms                                                      | 139 ms: 1.05x faster                                                        |
| xml_etree_iterparse        | 60.5 ms                                                     | 58.4 ms: 1.04x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 90.6 ms: 1.02x faster                                                       |
| regex_dna                  | 115 ms                                                      | 113 ms: 1.02x faster                                                        |
| deepcopy_reduce            | 2.02 us                                                     | 2.04 us: 1.01x slower                                                       |
| pycparser                  | 695 ms                                                      | 719 ms: 1.03x slower                                                        |
| html5lib                   | 38.2 ms                                                     | 39.8 ms: 1.04x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.2 ms: 1.06x slower                                                       |
| 2to3                       | 215 ms                                                      | 227 ms: 1.06x slower                                                        |
| dulwich_log                | 40.1 ms                                                     | 42.4 ms: 1.06x slower                                                       |
| python_startup             | 24.4 ms                                                     | 25.8 ms: 1.06x slower                                                       |
| telco                      | 4.85 ms                                                     | 5.17 ms: 1.07x slower                                                       |
| spectral_norm              | 63.4 ms                                                     | 68.5 ms: 1.08x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 59.5 ns: 1.09x slower                                                       |
| go                         | 84.7 ms                                                     | 92.6 ms: 1.09x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 62.2 ms: 1.10x slower                                                       |
| sympy_expand               | 286 ms                                                      | 315 ms: 1.10x slower                                                        |
| logging_simple             | 5.77 us                                                     | 6.41 us: 1.11x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 94.8 ms: 1.11x slower                                                       |
| sympy_str                  | 167 ms                                                      | 186 ms: 1.12x slower                                                        |
| logging_format             | 6.18 us                                                     | 6.89 us: 1.12x slower                                                       |
| genshi_xml                 | 33.9 ms                                                     | 37.9 ms: 1.12x slower                                                       |
| scimark_fft                | 175 ms                                                      | 196 ms: 1.12x slower                                                        |
| pyflate                    | 283 ms                                                      | 318 ms: 1.12x slower                                                        |
| regex_compile              | 80.7 ms                                                     | 90.8 ms: 1.13x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 85.8 ms: 1.13x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.9 ms: 1.13x slower                                                       |
| json_loads                 | 15.1 us                                                     | 17.0 us: 1.13x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 60.7 ms: 1.13x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 148 us: 1.14x slower                                                        |
| chaos                      | 37.9 ms                                                     | 43.2 ms: 1.14x slower                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.98 ms: 1.14x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 19.5 ms: 1.15x slower                                                       |
| generators                 | 19.0 ms                                                     | 22.1 ms: 1.16x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 7.22 ms: 1.17x slower                                                       |
| fannkuch                   | 252 ms                                                      | 295 ms: 1.17x slower                                                        |
| pprint_safe_repr           | 485 ms                                                      | 569 ms: 1.17x slower                                                        |
| hexiom                     | 3.84 ms                                                     | 4.52 ms: 1.18x slower                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 48.3 ms: 1.18x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 43.3 ms: 1.19x slower                                                       |
| async_generators           | 223 ms                                                      | 264 ms: 1.19x slower                                                        |
| nbody                      | 66.3 ms                                                     | 78.9 ms: 1.19x slower                                                       |
| sphinx                     | 617 ms                                                      | 736 ms: 1.19x slower                                                        |
| pickle_pure_python         | 186 us                                                      | 223 us: 1.20x slower                                                        |
| richards                   | 26.3 ms                                                     | 32.2 ms: 1.23x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 18.7 ms: 1.23x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 69.2 ms: 1.23x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 88.8 ms: 1.23x slower                                                       |
| comprehensions             | 10.4 us                                                     | 12.8 us: 1.23x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.36 ms: 1.25x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 57.1 ms: 1.25x slower                                                       |
| richards_super             | 29.8 ms                                                     | 37.5 ms: 1.26x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 130 us: 1.26x slower                                                        |
| many_optionals             | 361 us                                                      | 465 us: 1.29x slower                                                        |
| django_template            | 20.3 ms                                                     | 26.2 ms: 1.29x slower                                                       |
| raytrace                   | 153 ms                                                      | 203 ms: 1.32x slower                                                        |
| bench_thread_pool          | 810 us                                                      | 1.10 ms: 1.36x slower                                                       |
| coverage                   | 45.3 ms                                                     | 67.2 ms: 1.48x slower                                                       |
| mako                       | 6.56 ms                                                     | 9.76 ms: 1.49x slower                                                       |
| k_core                     | 1.70 sec                                                    | 2.71 sec: 1.60x slower                                                      |
| subparsers                 | 10.9 ms                                                     | 18.1 ms: 1.66x slower                                                       |
| shortest_path              | 355 ms                                                      | 667 ms: 1.88x slower                                                        |
| tomli_loads                | 1.37 sec                                                    | 2.59 sec: 1.89x slower                                                      |
| pprint_pformat             | 977 ms                                                      | 1.85 sec: 1.89x slower                                                      |
| bpe_tokeniser              | 2.87 sec                                                    | 5.46 sec: 1.90x slower                                                      |
| docutils                   | 1.53 sec                                                    | 2.98 sec: 1.94x slower                                                      |
| connected_components       | 320 ms                                                      | 632 ms: 1.97x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.05x slower                                                                |

Benchmark hidden because not significant (2): json, pylint
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250503-3.14.0a7+-7363e8d-NOGIL/bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.041x slower

# HPT report

- Reliability score: 99.95% likely to be slow
- 90% likely to have a slowdown of 1.09x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown