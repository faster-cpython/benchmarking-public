# Results vs. 3.13.0

- fork: python
- ref: 425f60b9eb253c57bc32
- machine: windows-amd64
- commit hash: 425f60b
- commit date: 2025-03-29
- overall geometric mean: 1.011x faster
- HPT reliability: 81.72%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 224 ms: 1.04x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.72 sec: 1.12x slower                                                      |
| html5lib       | 38.2 ms                                                     | 39.5 ms: 1.03x slower                                                       |
| sphinx         | 617 ms                                                      | 667 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                       | 1.07x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 160 ms: 1.88x faster                                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 216 ms: 1.30x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 407 ms: 1.22x faster                                                        |
| async_tree_io              | 513 ms                                                      | 420 ms: 1.22x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 218 ms: 1.22x faster                                                        |
| async_tree_none            | 219 ms                                                      | 186 ms: 1.18x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 174 ms: 1.15x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 338 ms: 1.12x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 341 ms: 1.12x faster                                                        |
| coroutines                 | 12.5 ms                                                     | 13.4 ms: 1.08x slower                                                       |
| async_generators           | 223 ms                                                      | 244 ms: 1.09x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.18x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 60.9 ms: 1.09x faster                                                       |
| float          | 50.8 ms                                                     | 47.0 ms: 1.08x faster                                                       |
| pidigits       | 146 ms                                                      | 150 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.2 ms: 1.68x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.48 ms: 1.14x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 83.4 ms: 1.03x slower                                                       |
| regex_dna      | 115 ms                                                      | 120 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.25 sec: 1.10x faster                                                      |
| unpickle_pure_python | 130 us                                                      | 122 us: 1.07x faster                                                        |
| xml_etree_parse      | 92.2 ms                                                     | 87.4 ms: 1.06x faster                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 52.0 ms: 1.03x faster                                                       |
| json_loads           | 15.1 us                                                     | 15.0 us: 1.01x faster                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 62.1 ms: 1.03x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 37.8 ms: 1.03x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 6.79 ms: 1.10x slower                                                       |
| pickle_pure_python   | 186 us                                                      | 219 us: 1.18x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.7 ms: 1.06x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 20.4 ms: 1.20x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.66 ms: 1.16x faster                                                       |
| genshi_xml      | 33.9 ms                                                     | 36.5 ms: 1.08x slower                                                       |
| genshi_text     | 15.2 ms                                                     | 16.4 ms: 1.08x slower                                                       |
| django_template | 20.3 ms                                                     | 25.2 ms: 1.24x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.06x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 32.7 ms: 2.30x faster                                                       |
| asyncio_websockets         | 300 ms                                                      | 160 ms: 1.88x faster                                                        |
| mdp                        | 1.43 sec                                                    | 792 ms: 1.81x faster                                                        |
| regex_v8                   | 23.8 ms                                                     | 14.2 ms: 1.68x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 216 ms: 1.30x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 407 ms: 1.22x faster                                                        |
| async_tree_io              | 513 ms                                                      | 420 ms: 1.22x faster                                                        |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.13 ms: 1.22x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 218 ms: 1.22x faster                                                        |
| deepcopy                   | 223 us                                                      | 188 us: 1.19x faster                                                        |
| async_tree_none            | 219 ms                                                      | 186 ms: 1.18x faster                                                        |
| mako                       | 6.56 ms                                                     | 5.66 ms: 1.16x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 174 ms: 1.15x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.48 ms: 1.14x faster                                                       |
| scimark_fft                | 175 ms                                                      | 154 ms: 1.13x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 338 ms: 1.12x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 341 ms: 1.12x faster                                                        |
| deepcopy_memo              | 23.1 us                                                     | 20.9 us: 1.10x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.25 sec: 1.10x faster                                                      |
| nbody                      | 66.3 ms                                                     | 60.9 ms: 1.09x faster                                                       |
| float                      | 50.8 ms                                                     | 47.0 ms: 1.08x faster                                                       |
| pyflate                    | 283 ms                                                      | 265 ms: 1.07x faster                                                        |
| spectral_norm              | 63.4 ms                                                     | 59.4 ms: 1.07x faster                                                       |
| unpickle_pure_python       | 130 us                                                      | 122 us: 1.07x faster                                                        |
| telco                      | 4.85 ms                                                     | 4.55 ms: 1.07x faster                                                       |
| json                       | 3.30 ms                                                     | 3.10 ms: 1.06x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 87.4 ms: 1.06x faster                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.74 sec: 1.05x faster                                                      |
| generators                 | 19.0 ms                                                     | 18.3 ms: 1.04x faster                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 52.0 ms: 1.03x faster                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.55 us: 1.03x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.99 us: 1.02x faster                                                       |
| json_loads                 | 15.1 us                                                     | 15.0 us: 1.01x faster                                                       |
| go                         | 84.7 ms                                                     | 85.7 ms: 1.01x slower                                                       |
| shortest_path              | 355 ms                                                      | 360 ms: 1.01x slower                                                        |
| pidigits                   | 146 ms                                                      | 150 ms: 1.02x slower                                                        |
| connected_components       | 320 ms                                                      | 327 ms: 1.02x slower                                                        |
| create_gc_cycles           | 1.22 ms                                                     | 1.25 ms: 1.02x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 62.1 ms: 1.03x slower                                                       |
| regex_compile              | 80.7 ms                                                     | 83.4 ms: 1.03x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 37.8 ms: 1.03x slower                                                       |
| html5lib                   | 38.2 ms                                                     | 39.5 ms: 1.03x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 47.2 ms: 1.04x slower                                                       |
| regex_dna                  | 115 ms                                                      | 120 ms: 1.04x slower                                                        |
| 2to3                       | 215 ms                                                      | 224 ms: 1.04x slower                                                        |
| gc_traversal               | 1.96 ms                                                     | 2.05 ms: 1.04x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.03 sec: 1.05x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 511 ms: 1.05x slower                                                        |
| python_startup             | 24.4 ms                                                     | 25.7 ms: 1.06x slower                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 89.0 ms: 1.06x slower                                                       |
| pycparser                  | 695 ms                                                      | 738 ms: 1.06x slower                                                        |
| logging_silent             | 54.6 ns                                                     | 58.1 ns: 1.06x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 76.7 ms: 1.07x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 60.5 ms: 1.07x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 81.4 ms: 1.07x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 42.9 ms: 1.07x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.4 ms: 1.08x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 872 us: 1.08x slower                                                        |
| genshi_xml                 | 33.9 ms                                                     | 36.5 ms: 1.08x slower                                                       |
| chaos                      | 37.9 ms                                                     | 40.8 ms: 1.08x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 16.4 ms: 1.08x slower                                                       |
| sphinx                     | 617 ms                                                      | 667 ms: 1.08x slower                                                        |
| sympy_sum                  | 85.2 ms                                                     | 92.2 ms: 1.08x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 112 us: 1.08x slower                                                        |
| richards_super             | 29.8 ms                                                     | 32.4 ms: 1.09x slower                                                       |
| sympy_str                  | 167 ms                                                      | 182 ms: 1.09x slower                                                        |
| coverage                   | 45.3 ms                                                     | 49.4 ms: 1.09x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.5 ms: 1.09x slower                                                       |
| async_generators           | 223 ms                                                      | 244 ms: 1.09x slower                                                        |
| richards                   | 26.3 ms                                                     | 28.7 ms: 1.09x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 6.79 ms: 1.10x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 62.1 ms: 1.11x slower                                                       |
| sympy_expand               | 286 ms                                                      | 319 ms: 1.12x slower                                                        |
| logging_simple             | 5.77 us                                                     | 6.48 us: 1.12x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.72 sec: 1.12x slower                                                      |
| logging_format             | 6.18 us                                                     | 6.95 us: 1.12x slower                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 46.2 ms: 1.13x slower                                                       |
| raytrace                   | 153 ms                                                      | 180 ms: 1.17x slower                                                        |
| comprehensions             | 10.4 us                                                     | 12.2 us: 1.17x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 219 us: 1.18x slower                                                        |
| python_startup_no_site     | 16.9 ms                                                     | 20.4 ms: 1.20x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.73 ms: 1.23x slower                                                       |
| django_template            | 20.3 ms                                                     | 25.2 ms: 1.24x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.35 ms: 1.24x slower                                                       |
| many_optionals             | 361 us                                                      | 456 us: 1.26x slower                                                        |
| subparsers                 | 10.9 ms                                                     | 16.4 ms: 1.51x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (3): k_core, pylint, fannkuch
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250329-3.14.0a6+-425f60b-JIT/bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.011x faster

# HPT report

- Reliability score: 81.72% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown