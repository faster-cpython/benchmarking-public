# Results vs. 3.13.0

- fork: python
- ref: 359c7dde3bb074e02968
- machine: windows-amd64
- commit hash: 359c7dd
- commit date: 2025-02-16
- overall geometric mean: 1.013x faster
- HPT reliability: 98.91%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 224 ms: 1.04x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.71 sec: 1.12x slower                                                      |
| sphinx         | 617 ms                                                      | 682 ms: 1.10x slower                                                        |
| Geometric mean | (ref)                                                       | 1.07x slower                                                                |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 208 ms: 1.35x faster                                                        |
| async_tree_io              | 513 ms                                                      | 392 ms: 1.31x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 388 ms: 1.28x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 210 ms: 1.26x faster                                                        |
| async_tree_none            | 219 ms                                                      | 177 ms: 1.24x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 168 ms: 1.19x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 359 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 364 ms: 1.05x faster                                                        |
| async_generators           | 223 ms                                                      | 220 ms: 1.01x faster                                                        |
| asyncio_websockets         | 300 ms                                                      | 322 ms: 1.07x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.8 ms: 1.10x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.13x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 44.1 ms: 1.15x faster                                                       |
| nbody          | 66.3 ms                                                     | 68.3 ms: 1.03x slower                                                       |
| pidigits       | 146 ms                                                      | 154 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 16.5 ms: 1.44x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 84.4 ms: 1.05x slower                                                       |
| regex_dna      | 115 ms                                                      | 130 ms: 1.13x slower                                                        |
| regex_effbot   | 1.69 ms                                                     | 1.93 ms: 1.14x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.31 sec: 1.05x faster                                                      |
| unpickle_pure_python | 130 us                                                      | 141 us: 1.08x slower                                                        |
| xml_etree_parse      | 92.2 ms                                                     | 102 ms: 1.11x slower                                                        |
| xml_etree_iterparse  | 60.5 ms                                                     | 68.1 ms: 1.12x slower                                                       |
| pickle_pure_python   | 186 us                                                      | 209 us: 1.13x slower                                                        |
| xml_etree_generate   | 53.5 ms                                                     | 63.6 ms: 1.19x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 43.7 ms: 1.20x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 7.81 ms: 1.26x slower                                                       |
| json_loads           | 15.1 us                                                     | 19.3 us: 1.28x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.14x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.7 ms: 1.05x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 19.8 ms: 1.17x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 31.4 ms: 1.08x faster                                                       |
| genshi_text     | 15.2 ms                                                     | 14.6 ms: 1.04x faster                                                       |
| mako            | 6.56 ms                                                     | 7.57 ms: 1.15x slower                                                       |
| django_template | 20.3 ms                                                     | 24.2 ms: 1.19x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.05x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 550 us: 15.39x faster                                                       |
| pathlib                    | 75.3 ms                                                     | 29.2 ms: 2.58x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 16.5 ms: 1.44x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 208 ms: 1.35x faster                                                        |
| async_tree_io              | 513 ms                                                      | 392 ms: 1.31x faster                                                        |
| deepcopy_memo              | 23.1 us                                                     | 17.8 us: 1.30x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 388 ms: 1.28x faster                                                        |
| deepcopy                   | 223 us                                                      | 175 us: 1.28x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 210 ms: 1.26x faster                                                        |
| async_tree_none            | 219 ms                                                      | 177 ms: 1.24x faster                                                        |
| go                         | 84.7 ms                                                     | 70.8 ms: 1.20x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 168 ms: 1.19x faster                                                        |
| float                      | 50.8 ms                                                     | 44.1 ms: 1.15x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 55.8 ms: 1.14x faster                                                       |
| generators                 | 19.0 ms                                                     | 17.4 ms: 1.09x faster                                                       |
| genshi_xml                 | 33.9 ms                                                     | 31.4 ms: 1.08x faster                                                       |
| scimark_sor                | 76.2 ms                                                     | 71.6 ms: 1.07x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.90 us: 1.06x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 359 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 364 ms: 1.05x faster                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.31 sec: 1.05x faster                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 38.9 ms: 1.05x faster                                                       |
| genshi_text                | 15.2 ms                                                     | 14.6 ms: 1.04x faster                                                       |
| deltablue                  | 1.89 ms                                                     | 1.82 ms: 1.04x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.52 ms: 1.04x faster                                                       |
| async_generators           | 223 ms                                                      | 220 ms: 1.01x faster                                                        |
| meteor_contest             | 72.0 ms                                                     | 71.2 ms: 1.01x faster                                                       |
| pyflate                    | 283 ms                                                      | 281 ms: 1.01x faster                                                        |
| connected_components       | 320 ms                                                      | 323 ms: 1.01x slower                                                        |
| hexiom                     | 3.84 ms                                                     | 3.90 ms: 1.01x slower                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.63 us: 1.03x slower                                                       |
| nbody                      | 66.3 ms                                                     | 68.3 ms: 1.03x slower                                                       |
| chaos                      | 37.9 ms                                                     | 39.2 ms: 1.03x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 41.7 ms: 1.04x slower                                                       |
| 2to3                       | 215 ms                                                      | 224 ms: 1.04x slower                                                        |
| regex_compile              | 80.7 ms                                                     | 84.4 ms: 1.05x slower                                                       |
| richards                   | 26.3 ms                                                     | 27.5 ms: 1.05x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 57.3 ns: 1.05x slower                                                       |
| sympy_expand               | 286 ms                                                      | 300 ms: 1.05x slower                                                        |
| scimark_fft                | 175 ms                                                      | 184 ms: 1.05x slower                                                        |
| pidigits                   | 146 ms                                                      | 154 ms: 1.05x slower                                                        |
| python_startup             | 24.4 ms                                                     | 25.7 ms: 1.05x slower                                                       |
| sqlglot_parse              | 764 us                                                      | 806 us: 1.05x slower                                                        |
| bench_mp_pool              | 84.2 ms                                                     | 88.8 ms: 1.05x slower                                                       |
| telco                      | 4.85 ms                                                     | 5.12 ms: 1.06x slower                                                       |
| richards_super             | 29.8 ms                                                     | 31.4 ms: 1.06x slower                                                       |
| pprint_safe_repr           | 485 ms                                                      | 512 ms: 1.06x slower                                                        |
| sympy_str                  | 167 ms                                                      | 176 ms: 1.06x slower                                                        |
| bpe_tokeniser              | 2.87 sec                                                    | 3.05 sec: 1.06x slower                                                      |
| fannkuch                   | 252 ms                                                      | 267 ms: 1.06x slower                                                        |
| sqlglot_transpile          | 953 us                                                      | 1.01 ms: 1.06x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 110 us: 1.06x slower                                                        |
| logging_simple             | 5.77 us                                                     | 6.14 us: 1.06x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.58 us: 1.07x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 91.1 ms: 1.07x slower                                                       |
| asyncio_websockets         | 300 ms                                                      | 322 ms: 1.07x slower                                                        |
| bench_thread_pool          | 810 us                                                      | 873 us: 1.08x slower                                                        |
| sympy_integrate            | 12.3 ms                                                     | 13.3 ms: 1.08x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.06 sec: 1.08x slower                                                      |
| unpickle_pure_python       | 130 us                                                      | 141 us: 1.08x slower                                                        |
| sqlglot_optimize           | 32.5 ms                                                     | 35.3 ms: 1.08x slower                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.33 ms: 1.09x slower                                                       |
| json                       | 3.30 ms                                                     | 3.60 ms: 1.09x slower                                                       |
| comprehensions             | 10.4 us                                                     | 11.4 us: 1.10x slower                                                       |
| sqlglot_normalize          | 172 ms                                                      | 188 ms: 1.10x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.8 ms: 1.10x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 62.6 ms: 1.10x slower                                                       |
| sphinx                     | 617 ms                                                      | 682 ms: 1.10x slower                                                        |
| xml_etree_parse            | 92.2 ms                                                     | 102 ms: 1.11x slower                                                        |
| nqueens                    | 56.1 ms                                                     | 62.4 ms: 1.11x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.71 sec: 1.12x slower                                                      |
| raytrace                   | 153 ms                                                      | 172 ms: 1.12x slower                                                        |
| xml_etree_iterparse        | 60.5 ms                                                     | 68.1 ms: 1.12x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 209 us: 1.13x slower                                                        |
| mdp                        | 1.43 sec                                                    | 1.61 sec: 1.13x slower                                                      |
| regex_dna                  | 115 ms                                                      | 130 ms: 1.13x slower                                                        |
| crypto_pyaes               | 45.6 ms                                                     | 51.5 ms: 1.13x slower                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.93 ms: 1.14x slower                                                       |
| coverage                   | 45.3 ms                                                     | 51.9 ms: 1.14x slower                                                       |
| mako                       | 6.56 ms                                                     | 7.57 ms: 1.15x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 19.8 ms: 1.17x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 63.6 ms: 1.19x slower                                                       |
| django_template            | 20.3 ms                                                     | 24.2 ms: 1.19x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 43.7 ms: 1.20x slower                                                       |
| many_optionals             | 361 us                                                      | 446 us: 1.24x slower                                                        |
| json_dumps                 | 6.19 ms                                                     | 7.81 ms: 1.26x slower                                                       |
| json_loads                 | 15.1 us                                                     | 19.3 us: 1.28x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.89 ms: 1.47x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 16.0 ms: 1.48x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (5): pylint, shortest_path, pycparser, k_core, html5lib
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (8) of results/bm-20250216-3.14.0a5+-359c7dd-CLANG/bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.013x faster

# HPT report

- Reliability score: 98.91% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown