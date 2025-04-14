# Results vs. 3.13.0

- fork: python
- ref: 425f60b9eb253c57bc32
- machine: windows-amd64
- commit hash: 425f60b
- commit date: 2025-03-29
- overall geometric mean: 1.084x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.09x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 235 ms: 1.09x slower                                                        |
| docutils       | 1.53 sec                                                    | 2.99 sec: 1.95x slower                                                      |
| html5lib       | 38.2 ms                                                     | 42.5 ms: 1.11x slower                                                       |
| sphinx         | 617 ms                                                      | 765 ms: 1.24x slower                                                        |
| Geometric mean | (ref)                                                       | 1.31x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 143 ms: 2.09x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 354 ms: 1.40x faster                                                        |
| async_tree_io              | 513 ms                                                      | 378 ms: 1.36x faster                                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 207 ms: 1.35x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 164 ms: 1.22x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 315 ms: 1.21x faster                                                        |
| async_tree_none            | 219 ms                                                      | 181 ms: 1.21x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 228 ms: 1.16x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 339 ms: 1.12x faster                                                        |
| coroutines                 | 12.5 ms                                                     | 13.2 ms: 1.06x slower                                                       |
| async_generators           | 223 ms                                                      | 250 ms: 1.12x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.24x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 146 ms                                                      | 138 ms: 1.06x faster                                                        |
| float          | 50.8 ms                                                     | 48.1 ms: 1.06x faster                                                       |
| nbody          | 66.3 ms                                                     | 92.0 ms: 1.39x slower                                                       |
| Geometric mean | (ref)                                                       | 1.07x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.1 ms: 1.83x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.45 ms: 1.17x faster                                                       |
| regex_dna      | 115 ms                                                      | 111 ms: 1.03x faster                                                        |
| regex_compile  | 80.7 ms                                                     | 97.2 ms: 1.20x slower                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 90.1 ms: 1.02x faster                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 59.6 ms: 1.02x faster                                                       |
| json_loads           | 15.1 us                                                     | 17.4 us: 1.15x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 63.6 ms: 1.19x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 7.62 ms: 1.23x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 45.9 ms: 1.26x slower                                                       |
| unpickle_pure_python | 130 us                                                      | 165 us: 1.27x slower                                                        |
| pickle_pure_python   | 186 us                                                      | 238 us: 1.28x slower                                                        |
| tomli_loads          | 1.37 sec                                                    | 2.89 sec: 2.11x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.24x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 27.3 ms: 1.12x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 21.0 ms: 1.24x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.18x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 39.1 ms: 1.15x slower                                                       |
| genshi_text     | 15.2 ms                                                     | 19.3 ms: 1.27x slower                                                       |
| django_template | 20.3 ms                                                     | 27.5 ms: 1.36x slower                                                       |
| mako            | 6.56 ms                                                     | 9.96 ms: 1.52x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.32x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 586 us: 14.44x faster                                                       |
| pathlib                    | 75.3 ms                                                     | 32.1 ms: 2.35x faster                                                       |
| asyncio_websockets         | 300 ms                                                      | 143 ms: 2.09x faster                                                        |
| regex_v8                   | 23.8 ms                                                     | 13.1 ms: 1.83x faster                                                       |
| gc_traversal               | 1.96 ms                                                     | 1.15 ms: 1.71x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 354 ms: 1.40x faster                                                        |
| async_tree_io              | 513 ms                                                      | 378 ms: 1.36x faster                                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 207 ms: 1.35x faster                                                        |
| create_gc_cycles           | 1.22 ms                                                     | 967 us: 1.27x faster                                                        |
| mdp                        | 1.43 sec                                                    | 1.14 sec: 1.26x faster                                                      |
| async_tree_none_tg         | 200 ms                                                      | 164 ms: 1.22x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 315 ms: 1.21x faster                                                        |
| async_tree_none            | 219 ms                                                      | 181 ms: 1.21x faster                                                        |
| sqlite_synth               | 1.59 us                                                     | 1.33 us: 1.19x faster                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.45 ms: 1.17x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 228 ms: 1.16x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 339 ms: 1.12x faster                                                        |
| bench_mp_pool              | 84.2 ms                                                     | 76.9 ms: 1.10x faster                                                       |
| deepcopy                   | 223 us                                                      | 211 us: 1.06x faster                                                        |
| pidigits                   | 146 ms                                                      | 138 ms: 1.06x faster                                                        |
| float                      | 50.8 ms                                                     | 48.1 ms: 1.06x faster                                                       |
| regex_dna                  | 115 ms                                                      | 111 ms: 1.03x faster                                                        |
| xml_etree_parse            | 92.2 ms                                                     | 90.1 ms: 1.02x faster                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 59.6 ms: 1.02x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 23.8 us: 1.03x slower                                                       |
| pycparser                  | 695 ms                                                      | 728 ms: 1.05x slower                                                        |
| pylint                     | 205 ms                                                      | 216 ms: 1.05x slower                                                        |
| dulwich_log                | 40.1 ms                                                     | 42.3 ms: 1.06x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.2 ms: 1.06x slower                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 2.19 us: 1.08x slower                                                       |
| 2to3                       | 215 ms                                                      | 235 ms: 1.09x slower                                                        |
| spectral_norm              | 63.4 ms                                                     | 70.2 ms: 1.11x slower                                                       |
| html5lib                   | 38.2 ms                                                     | 42.5 ms: 1.11x slower                                                       |
| generators                 | 19.0 ms                                                     | 21.2 ms: 1.11x slower                                                       |
| python_startup             | 24.4 ms                                                     | 27.3 ms: 1.12x slower                                                       |
| async_generators           | 223 ms                                                      | 250 ms: 1.12x slower                                                        |
| json_loads                 | 15.1 us                                                     | 17.4 us: 1.15x slower                                                       |
| genshi_xml                 | 33.9 ms                                                     | 39.1 ms: 1.15x slower                                                       |
| telco                      | 4.85 ms                                                     | 5.60 ms: 1.15x slower                                                       |
| sympy_expand               | 286 ms                                                      | 333 ms: 1.17x slower                                                        |
| sympy_str                  | 167 ms                                                      | 195 ms: 1.17x slower                                                        |
| pyflate                    | 283 ms                                                      | 333 ms: 1.18x slower                                                        |
| logging_silent             | 54.6 ns                                                     | 64.3 ns: 1.18x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 101 ms: 1.18x slower                                                        |
| scimark_lu                 | 56.7 ms                                                     | 67.1 ms: 1.18x slower                                                       |
| go                         | 84.7 ms                                                     | 100 ms: 1.19x slower                                                        |
| xml_etree_generate         | 53.5 ms                                                     | 63.6 ms: 1.19x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.89 us: 1.19x slower                                                       |
| logging_format             | 6.18 us                                                     | 7.41 us: 1.20x slower                                                       |
| regex_compile              | 80.7 ms                                                     | 97.2 ms: 1.20x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 14.9 ms: 1.20x slower                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 3.17 ms: 1.22x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 93.2 ms: 1.22x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 7.62 ms: 1.23x slower                                                       |
| sphinx                     | 617 ms                                                      | 765 ms: 1.24x slower                                                        |
| python_startup_no_site     | 16.9 ms                                                     | 21.0 ms: 1.24x slower                                                       |
| scimark_fft                | 175 ms                                                      | 217 ms: 1.24x slower                                                        |
| meteor_contest             | 72.0 ms                                                     | 89.4 ms: 1.24x slower                                                       |
| pprint_safe_repr           | 485 ms                                                      | 604 ms: 1.25x slower                                                        |
| hexiom                     | 3.84 ms                                                     | 4.81 ms: 1.25x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 45.9 ms: 1.26x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 165 us: 1.27x slower                                                        |
| genshi_text                | 15.2 ms                                                     | 19.3 ms: 1.27x slower                                                       |
| chaos                      | 37.9 ms                                                     | 48.4 ms: 1.28x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 238 us: 1.28x slower                                                        |
| typing_runtime_protocols   | 103 us                                                      | 133 us: 1.29x slower                                                        |
| crypto_pyaes               | 45.6 ms                                                     | 59.3 ms: 1.30x slower                                                       |
| richards                   | 26.3 ms                                                     | 34.2 ms: 1.30x slower                                                       |
| fannkuch                   | 252 ms                                                      | 328 ms: 1.31x slower                                                        |
| many_optionals             | 361 us                                                      | 472 us: 1.31x slower                                                        |
| deltablue                  | 1.89 ms                                                     | 2.51 ms: 1.33x slower                                                       |
| comprehensions             | 10.4 us                                                     | 13.8 us: 1.33x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 75.3 ms: 1.34x slower                                                       |
| richards_super             | 29.8 ms                                                     | 40.3 ms: 1.35x slower                                                       |
| django_template            | 20.3 ms                                                     | 27.5 ms: 1.36x slower                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 55.6 ms: 1.36x slower                                                       |
| nbody                      | 66.3 ms                                                     | 92.0 ms: 1.39x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 1.13 ms: 1.40x slower                                                       |
| raytrace                   | 153 ms                                                      | 217 ms: 1.42x slower                                                        |
| coverage                   | 45.3 ms                                                     | 67.2 ms: 1.48x slower                                                       |
| mako                       | 6.56 ms                                                     | 9.96 ms: 1.52x slower                                                       |
| k_core                     | 1.70 sec                                                    | 2.73 sec: 1.61x slower                                                      |
| subparsers                 | 10.9 ms                                                     | 17.7 ms: 1.63x slower                                                       |
| shortest_path              | 355 ms                                                      | 683 ms: 1.92x slower                                                        |
| docutils                   | 1.53 sec                                                    | 2.99 sec: 1.95x slower                                                      |
| bpe_tokeniser              | 2.87 sec                                                    | 5.70 sec: 1.98x slower                                                      |
| connected_components       | 320 ms                                                      | 646 ms: 2.02x slower                                                        |
| pprint_pformat             | 977 ms                                                      | 1.98 sec: 2.02x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 2.89 sec: 2.11x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.10x slower                                                                |

Benchmark hidden because not significant (1): json
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250329-3.14.0a6+-425f60b-NOGIL/bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.084x slower

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.13x
- 95% likely to have a slowdown of 1.11x
- 99% likely to have a slowdown of 1.09x

# Memory
- memory change: unknown