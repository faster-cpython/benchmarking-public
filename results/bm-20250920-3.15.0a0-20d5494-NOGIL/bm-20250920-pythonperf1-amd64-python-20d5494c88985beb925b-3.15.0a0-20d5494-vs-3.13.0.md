# Results vs. 3.13.0

- fork: python
- ref: 20d5494c88985beb925b
- machine: windows-amd64
- commit hash: 20d5494
- commit date: 2025-09-20
- overall geometric mean: 1.052x slower
- HPT reliability: 99.92%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 223 ms: 1.04x slower                                                       |
| docutils       | 1.53 sec                                                    | 2.74 sec: 1.79x slower                                                     |
| html5lib       | 38.2 ms                                                     | 39.5 ms: 1.03x slower                                                      |
| sphinx         | 617 ms                                                      | 659 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                       | 1.20x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 140 ms: 2.14x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 326 ms: 1.52x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 188 ms: 1.49x faster                                                       |
| async_tree_io              | 513 ms                                                      | 347 ms: 1.48x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 147 ms: 1.36x faster                                                       |
| async_tree_none            | 219 ms                                                      | 167 ms: 1.31x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 208 ms: 1.28x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 303 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 325 ms: 1.17x faster                                                       |
| coroutines                 | 12.5 ms                                                     | 14.2 ms: 1.13x slower                                                      |
| async_generators           | 223 ms                                                      | 258 ms: 1.16x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.30x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 46.2 ms: 1.10x faster                                                      |
| pidigits       | 146 ms                                                      | 136 ms: 1.07x faster                                                       |
| nbody          | 66.3 ms                                                     | 85.1 ms: 1.28x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.1 ms: 1.82x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.60 ms: 1.06x faster                                                      |
| regex_dna      | 115 ms                                                      | 112 ms: 1.03x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 92.1 ms: 1.14x slower                                                      |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 88.1 ms: 1.05x faster                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 58.8 ms: 1.03x faster                                                      |
| json_dumps           | 6.19 ms                                                     | 6.27 ms: 1.01x slower                                                      |
| json_loads           | 15.1 us                                                     | 16.0 us: 1.06x slower                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 62.3 ms: 1.17x slower                                                      |
| unpickle_pure_python | 130 us                                                      | 156 us: 1.20x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 44.0 ms: 1.20x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 233 us: 1.25x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 2.31 sec: 1.69x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.15x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.2 ms: 1.03x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 18.8 ms: 1.11x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.07x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 40.1 ms: 1.18x slower                                                      |
| genshi_text     | 15.2 ms                                                     | 19.5 ms: 1.28x slower                                                      |
| django_template | 20.3 ms                                                     | 27.3 ms: 1.35x slower                                                      |
| mako            | 6.56 ms                                                     | 9.82 ms: 1.50x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.32x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 561 us: 15.09x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 29.6 ms: 2.55x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 140 ms: 2.14x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 13.1 ms: 1.82x faster                                                      |
| gc_traversal               | 1.96 ms                                                     | 1.14 ms: 1.72x faster                                                      |
| async_tree_io_tg           | 497 ms                                                      | 326 ms: 1.52x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 188 ms: 1.49x faster                                                       |
| async_tree_io              | 513 ms                                                      | 347 ms: 1.48x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 147 ms: 1.36x faster                                                       |
| async_tree_none            | 219 ms                                                      | 167 ms: 1.31x faster                                                       |
| mdp                        | 1.43 sec                                                    | 1.10 sec: 1.31x faster                                                     |
| async_tree_memoization     | 265 ms                                                      | 208 ms: 1.28x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 303 ms: 1.26x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 18.8 us: 1.23x faster                                                      |
| deepcopy                   | 223 us                                                      | 187 us: 1.19x faster                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.36 us: 1.17x faster                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.05 ms: 1.17x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 325 ms: 1.17x faster                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 73.4 ms: 1.15x faster                                                      |
| float                      | 50.8 ms                                                     | 46.2 ms: 1.10x faster                                                      |
| pidigits                   | 146 ms                                                      | 136 ms: 1.07x faster                                                       |
| json                       | 3.30 ms                                                     | 3.09 ms: 1.07x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.60 ms: 1.06x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 88.1 ms: 1.05x faster                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 58.8 ms: 1.03x faster                                                      |
| regex_dna                  | 115 ms                                                      | 112 ms: 1.03x faster                                                       |
| json_dumps                 | 6.19 ms                                                     | 6.27 ms: 1.01x slower                                                      |
| dulwich_log                | 40.1 ms                                                     | 41.0 ms: 1.02x slower                                                      |
| telco                      | 4.85 ms                                                     | 4.97 ms: 1.03x slower                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 2.09 us: 1.03x slower                                                      |
| python_startup             | 24.4 ms                                                     | 25.2 ms: 1.03x slower                                                      |
| html5lib                   | 38.2 ms                                                     | 39.5 ms: 1.03x slower                                                      |
| 2to3                       | 215 ms                                                      | 223 ms: 1.04x slower                                                       |
| pycparser                  | 695 ms                                                      | 722 ms: 1.04x slower                                                       |
| json_loads                 | 15.1 us                                                     | 16.0 us: 1.06x slower                                                      |
| sphinx                     | 617 ms                                                      | 659 ms: 1.07x slower                                                       |
| go                         | 84.7 ms                                                     | 91.3 ms: 1.08x slower                                                      |
| pyflate                    | 283 ms                                                      | 311 ms: 1.10x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 18.8 ms: 1.11x slower                                                      |
| sympy_expand               | 286 ms                                                      | 320 ms: 1.12x slower                                                       |
| sympy_str                  | 167 ms                                                      | 188 ms: 1.13x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 64.1 ms: 1.13x slower                                                      |
| sympy_sum                  | 85.2 ms                                                     | 96.3 ms: 1.13x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 61.8 ns: 1.13x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.2 ms: 1.13x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 14.0 ms: 1.14x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.58 us: 1.14x slower                                                      |
| regex_compile              | 80.7 ms                                                     | 92.1 ms: 1.14x slower                                                      |
| async_generators           | 223 ms                                                      | 258 ms: 1.16x slower                                                       |
| spectral_norm              | 63.4 ms                                                     | 73.6 ms: 1.16x slower                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 62.3 ms: 1.17x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 567 ms: 1.17x slower                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 3.05 ms: 1.17x slower                                                      |
| logging_format             | 6.18 us                                                     | 7.24 us: 1.17x slower                                                      |
| scimark_sor                | 76.2 ms                                                     | 89.5 ms: 1.17x slower                                                      |
| comprehensions             | 10.4 us                                                     | 12.2 us: 1.18x slower                                                      |
| genshi_xml                 | 33.9 ms                                                     | 40.1 ms: 1.18x slower                                                      |
| fannkuch                   | 252 ms                                                      | 298 ms: 1.18x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 156 us: 1.20x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.61 ms: 1.20x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 44.0 ms: 1.20x slower                                                      |
| scimark_fft                | 175 ms                                                      | 212 ms: 1.21x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 87.2 ms: 1.21x slower                                                      |
| chaos                      | 37.9 ms                                                     | 46.4 ms: 1.23x slower                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 50.0 ms: 1.23x slower                                                      |
| generators                 | 19.0 ms                                                     | 23.4 ms: 1.23x slower                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 56.9 ms: 1.25x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 233 us: 1.25x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 130 us: 1.26x slower                                                       |
| richards                   | 26.3 ms                                                     | 33.2 ms: 1.26x slower                                                      |
| genshi_text                | 15.2 ms                                                     | 19.5 ms: 1.28x slower                                                      |
| nbody                      | 66.3 ms                                                     | 85.1 ms: 1.28x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.47 ms: 1.30x slower                                                      |
| richards_super             | 29.8 ms                                                     | 38.9 ms: 1.31x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 73.6 ms: 1.31x slower                                                      |
| bench_thread_pool          | 810 us                                                      | 1.08 ms: 1.34x slower                                                      |
| django_template            | 20.3 ms                                                     | 27.3 ms: 1.35x slower                                                      |
| raytrace                   | 153 ms                                                      | 212 ms: 1.38x slower                                                       |
| coverage                   | 45.3 ms                                                     | 66.4 ms: 1.47x slower                                                      |
| mako                       | 6.56 ms                                                     | 9.82 ms: 1.50x slower                                                      |
| k_core                     | 1.70 sec                                                    | 2.61 sec: 1.54x slower                                                     |
| tomli_loads                | 1.37 sec                                                    | 2.31 sec: 1.69x slower                                                     |
| pprint_pformat             | 977 ms                                                      | 1.66 sec: 1.70x slower                                                     |
| many_optionals             | 361 us                                                      | 626 us: 1.73x slower                                                       |
| shortest_path              | 355 ms                                                      | 631 ms: 1.78x slower                                                       |
| docutils                   | 1.53 sec                                                    | 2.74 sec: 1.79x slower                                                     |
| connected_components       | 320 ms                                                      | 593 ms: 1.86x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 5.35 sec: 1.86x slower                                                     |
| subparsers                 | 10.9 ms                                                     | 35.7 ms: 3.29x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.06x slower                                                               |

Benchmark hidden because not significant (1): pylint
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250920-3.15.0a0-20d5494-NOGIL/bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.052x slower

# HPT report

- Reliability score: 99.92% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown