# Results vs. 3.13.0

- fork: python
- ref: 425f60b9eb253c57bc32
- machine: windows-amd64
- commit hash: 425f60b
- commit date: 2025-03-29
- overall geometric mean: 1.013x faster
- HPT reliability: 99.36%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 220 ms: 1.02x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.65 sec: 1.08x slower                                                      |
| html5lib       | 38.2 ms                                                     | 39.0 ms: 1.02x slower                                                       |
| sphinx         | 617 ms                                                      | 653 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                       | 1.05x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 158 ms: 1.90x faster                                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 215 ms: 1.31x faster                                                        |
| async_tree_io              | 513 ms                                                      | 416 ms: 1.23x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 216 ms: 1.23x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 407 ms: 1.22x faster                                                        |
| async_tree_none            | 219 ms                                                      | 185 ms: 1.18x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 176 ms: 1.14x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 337 ms: 1.13x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 342 ms: 1.12x faster                                                        |
| coroutines                 | 12.5 ms                                                     | 13.4 ms: 1.07x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.20x faster                                                                |

Benchmark hidden because not significant (1): async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 44.7 ms: 1.14x faster                                                       |
| nbody          | 66.3 ms                                                     | 64.2 ms: 1.03x faster                                                       |
| pidigits       | 146 ms                                                      | 149 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.4 ms: 1.78x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.39 ms: 1.22x faster                                                       |
| regex_dna      | 115 ms                                                      | 114 ms: 1.01x faster                                                        |
| regex_compile  | 80.7 ms                                                     | 82.3 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.21x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 87.6 ms: 1.05x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.41 sec: 1.03x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 64.1 ms: 1.06x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 57.2 ms: 1.07x slower                                                       |
| unpickle_pure_python | 130 us                                                      | 140 us: 1.08x slower                                                        |
| json_dumps           | 6.19 ms                                                     | 6.78 ms: 1.10x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 40.9 ms: 1.12x slower                                                       |
| pickle_pure_python   | 186 us                                                      | 216 us: 1.16x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.06x slower                                                                |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.8 ms: 1.06x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 20.4 ms: 1.21x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.71 ms: 1.02x slower                                                       |
| genshi_text     | 15.2 ms                                                     | 15.8 ms: 1.04x slower                                                       |
| django_template | 20.3 ms                                                     | 25.4 ms: 1.25x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.08x slower                                                                |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 32.5 ms: 2.32x faster                                                       |
| asyncio_websockets         | 300 ms                                                      | 158 ms: 1.90x faster                                                        |
| mdp                        | 1.43 sec                                                    | 799 ms: 1.79x faster                                                        |
| regex_v8                   | 23.8 ms                                                     | 13.4 ms: 1.78x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 215 ms: 1.31x faster                                                        |
| deepcopy                   | 223 us                                                      | 180 us: 1.24x faster                                                        |
| async_tree_io              | 513 ms                                                      | 416 ms: 1.23x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 216 ms: 1.23x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 407 ms: 1.22x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.39 ms: 1.22x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 19.1 us: 1.21x faster                                                       |
| async_tree_none            | 219 ms                                                      | 185 ms: 1.18x faster                                                        |
| spectral_norm              | 63.4 ms                                                     | 55.1 ms: 1.15x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 176 ms: 1.14x faster                                                        |
| float                      | 50.8 ms                                                     | 44.7 ms: 1.14x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 337 ms: 1.13x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 342 ms: 1.12x faster                                                        |
| deepcopy_reduce            | 2.02 us                                                     | 1.88 us: 1.08x faster                                                       |
| json                       | 3.30 ms                                                     | 3.09 ms: 1.07x faster                                                       |
| generators                 | 19.0 ms                                                     | 17.9 ms: 1.06x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 87.6 ms: 1.05x faster                                                       |
| go                         | 84.7 ms                                                     | 80.8 ms: 1.05x faster                                                       |
| nbody                      | 66.3 ms                                                     | 64.2 ms: 1.03x faster                                                       |
| regex_dna                  | 115 ms                                                      | 114 ms: 1.01x faster                                                        |
| telco                      | 4.85 ms                                                     | 4.87 ms: 1.00x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 76.7 ms: 1.01x slower                                                       |
| regex_compile              | 80.7 ms                                                     | 82.3 ms: 1.02x slower                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.25 ms: 1.02x slower                                                       |
| pidigits                   | 146 ms                                                      | 149 ms: 1.02x slower                                                        |
| bpe_tokeniser              | 2.87 sec                                                    | 2.93 sec: 1.02x slower                                                      |
| mako                       | 6.56 ms                                                     | 6.71 ms: 1.02x slower                                                       |
| html5lib                   | 38.2 ms                                                     | 39.0 ms: 1.02x slower                                                       |
| 2to3                       | 215 ms                                                      | 220 ms: 1.02x slower                                                        |
| pyflate                    | 283 ms                                                      | 291 ms: 1.03x slower                                                        |
| shortest_path              | 355 ms                                                      | 366 ms: 1.03x slower                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.41 sec: 1.03x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 56.3 ns: 1.03x slower                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.69 ms: 1.03x slower                                                       |
| fannkuch                   | 252 ms                                                      | 260 ms: 1.03x slower                                                        |
| genshi_text                | 15.2 ms                                                     | 15.8 ms: 1.04x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 47.3 ms: 1.04x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 107 us: 1.04x slower                                                        |
| sympy_integrate            | 12.3 ms                                                     | 12.9 ms: 1.04x slower                                                       |
| pycparser                  | 695 ms                                                      | 728 ms: 1.05x slower                                                        |
| connected_components       | 320 ms                                                      | 336 ms: 1.05x slower                                                        |
| dulwich_log                | 40.1 ms                                                     | 42.1 ms: 1.05x slower                                                       |
| sympy_str                  | 167 ms                                                      | 175 ms: 1.05x slower                                                        |
| sympy_sum                  | 85.2 ms                                                     | 89.6 ms: 1.05x slower                                                       |
| sympy_expand               | 286 ms                                                      | 301 ms: 1.05x slower                                                        |
| bench_mp_pool              | 84.2 ms                                                     | 88.9 ms: 1.05x slower                                                       |
| scimark_fft                | 175 ms                                                      | 185 ms: 1.06x slower                                                        |
| richards_super             | 29.8 ms                                                     | 31.5 ms: 1.06x slower                                                       |
| sphinx                     | 617 ms                                                      | 653 ms: 1.06x slower                                                        |
| gc_traversal               | 1.96 ms                                                     | 2.08 ms: 1.06x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 76.2 ms: 1.06x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 64.1 ms: 1.06x slower                                                       |
| python_startup             | 24.4 ms                                                     | 25.8 ms: 1.06x slower                                                       |
| richards                   | 26.3 ms                                                     | 27.8 ms: 1.06x slower                                                       |
| chaos                      | 37.9 ms                                                     | 40.2 ms: 1.06x slower                                                       |
| coverage                   | 45.3 ms                                                     | 48.3 ms: 1.07x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 864 us: 1.07x slower                                                        |
| scimark_monte_carlo        | 40.7 ms                                                     | 43.5 ms: 1.07x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 57.2 ms: 1.07x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.4 ms: 1.07x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.12 ms: 1.07x slower                                                       |
| pprint_safe_repr           | 485 ms                                                      | 521 ms: 1.08x slower                                                        |
| unpickle_pure_python       | 130 us                                                      | 140 us: 1.08x slower                                                        |
| docutils                   | 1.53 sec                                                    | 1.65 sec: 1.08x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 61.6 ms: 1.09x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.07 sec: 1.09x slower                                                      |
| json_dumps                 | 6.19 ms                                                     | 6.78 ms: 1.10x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.39 us: 1.11x slower                                                       |
| comprehensions             | 10.4 us                                                     | 11.5 us: 1.11x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.88 us: 1.11x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 40.9 ms: 1.12x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.12 ms: 1.12x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 63.5 ms: 1.13x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 216 us: 1.16x slower                                                        |
| raytrace                   | 153 ms                                                      | 181 ms: 1.18x slower                                                        |
| many_optionals             | 361 us                                                      | 432 us: 1.20x slower                                                        |
| python_startup_no_site     | 16.9 ms                                                     | 20.4 ms: 1.21x slower                                                       |
| django_template            | 20.3 ms                                                     | 25.4 ms: 1.25x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 15.9 ms: 1.47x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (6): pylint, sqlite_synth, json_loads, async_generators, k_core, genshi_xml
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250329-3.14.0a6+-425f60b/bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.013x faster

# HPT report

- Reliability score: 99.36% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown