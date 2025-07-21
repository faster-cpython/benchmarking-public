# Results vs. 3.13.0

- fork: python
- ref: 800d37feca2e0ea33439
- machine: windows-amd64
- commit hash: 800d37f
- commit date: 2025-07-19
- overall geometric mean: 1.061x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.07x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 231 ms: 1.08x slower                                                       |
| docutils       | 1.53 sec                                                    | 2.87 sec: 1.87x slower                                                     |
| html5lib       | 38.2 ms                                                     | 40.6 ms: 1.06x slower                                                      |
| sphinx         | 617 ms                                                      | 689 ms: 1.12x slower                                                       |
| Geometric mean | (ref)                                                       | 1.24x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 143 ms: 2.09x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 328 ms: 1.52x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 189 ms: 1.48x faster                                                       |
| async_tree_io              | 513 ms                                                      | 352 ms: 1.46x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 148 ms: 1.36x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 209 ms: 1.27x faster                                                       |
| async_tree_none            | 219 ms                                                      | 174 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 311 ms: 1.23x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 333 ms: 1.14x faster                                                       |
| coroutines                 | 12.5 ms                                                     | 14.8 ms: 1.18x slower                                                      |
| async_generators           | 223 ms                                                      | 275 ms: 1.23x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.27x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 46.6 ms: 1.09x faster                                                      |
| pidigits       | 146 ms                                                      | 138 ms: 1.06x faster                                                       |
| nbody          | 66.3 ms                                                     | 81.0 ms: 1.22x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.5 ms: 1.77x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.68 ms: 1.01x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 94.6 ms: 1.17x slower                                                      |
| Geometric mean | (ref)                                                       | 1.11x faster                                                               |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 89.4 ms: 1.03x faster                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 59.1 ms: 1.02x faster                                                      |
| json_loads           | 15.1 us                                                     | 15.8 us: 1.04x slower                                                      |
| json_dumps           | 6.19 ms                                                     | 6.69 ms: 1.08x slower                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 63.0 ms: 1.18x slower                                                      |
| unpickle_pure_python | 130 us                                                      | 156 us: 1.20x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 45.2 ms: 1.24x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 239 us: 1.29x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 2.66 sec: 1.94x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.19x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.8 ms: 1.06x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.3 ms: 1.14x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 42.7 ms: 1.26x slower                                                      |
| genshi_text     | 15.2 ms                                                     | 20.3 ms: 1.33x slower                                                      |
| django_template | 20.3 ms                                                     | 27.3 ms: 1.35x slower                                                      |
| mako            | 6.56 ms                                                     | 9.63 ms: 1.47x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.35x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 566 us: 14.95x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 30.5 ms: 2.47x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 143 ms: 2.09x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 13.5 ms: 1.77x faster                                                      |
| gc_traversal               | 1.96 ms                                                     | 1.15 ms: 1.71x faster                                                      |
| async_tree_io_tg           | 497 ms                                                      | 328 ms: 1.52x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 189 ms: 1.48x faster                                                       |
| async_tree_io              | 513 ms                                                      | 352 ms: 1.46x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 148 ms: 1.36x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 209 ms: 1.27x faster                                                       |
| async_tree_none            | 219 ms                                                      | 174 ms: 1.26x faster                                                       |
| mdp                        | 1.43 sec                                                    | 1.15 sec: 1.25x faster                                                     |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 311 ms: 1.23x faster                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.33 us: 1.19x faster                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.04 ms: 1.18x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 333 ms: 1.14x faster                                                       |
| deepcopy                   | 223 us                                                      | 203 us: 1.10x faster                                                       |
| float                      | 50.8 ms                                                     | 46.6 ms: 1.09x faster                                                      |
| deepcopy_memo              | 23.1 us                                                     | 21.4 us: 1.08x faster                                                      |
| json                       | 3.30 ms                                                     | 3.08 ms: 1.07x faster                                                      |
| bench_mp_pool              | 84.2 ms                                                     | 79.1 ms: 1.06x faster                                                      |
| pidigits                   | 146 ms                                                      | 138 ms: 1.06x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 89.4 ms: 1.03x faster                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 59.1 ms: 1.02x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.68 ms: 1.01x faster                                                      |
| dulwich_log                | 40.1 ms                                                     | 41.6 ms: 1.04x slower                                                      |
| json_loads                 | 15.1 us                                                     | 15.8 us: 1.04x slower                                                      |
| pycparser                  | 695 ms                                                      | 731 ms: 1.05x slower                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 2.13 us: 1.05x slower                                                      |
| python_startup             | 24.4 ms                                                     | 25.8 ms: 1.06x slower                                                      |
| html5lib                   | 38.2 ms                                                     | 40.6 ms: 1.06x slower                                                      |
| 2to3                       | 215 ms                                                      | 231 ms: 1.08x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 6.69 ms: 1.08x slower                                                      |
| telco                      | 4.85 ms                                                     | 5.39 ms: 1.11x slower                                                      |
| pyflate                    | 283 ms                                                      | 315 ms: 1.11x slower                                                       |
| go                         | 84.7 ms                                                     | 94.5 ms: 1.12x slower                                                      |
| sphinx                     | 617 ms                                                      | 689 ms: 1.12x slower                                                       |
| sympy_expand               | 286 ms                                                      | 320 ms: 1.12x slower                                                       |
| sympy_str                  | 167 ms                                                      | 188 ms: 1.12x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 61.8 ns: 1.13x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 14.0 ms: 1.14x slower                                                      |
| sympy_sum                  | 85.2 ms                                                     | 97.1 ms: 1.14x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 19.3 ms: 1.14x slower                                                      |
| comprehensions             | 10.4 us                                                     | 11.9 us: 1.15x slower                                                      |
| spectral_norm              | 63.4 ms                                                     | 73.6 ms: 1.16x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 66.2 ms: 1.17x slower                                                      |
| regex_compile              | 80.7 ms                                                     | 94.6 ms: 1.17x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 571 ms: 1.18x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.80 us: 1.18x slower                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 63.0 ms: 1.18x slower                                                      |
| scimark_sor                | 76.2 ms                                                     | 90.0 ms: 1.18x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.8 ms: 1.18x slower                                                      |
| logging_format             | 6.18 us                                                     | 7.33 us: 1.19x slower                                                      |
| generators                 | 19.0 ms                                                     | 22.6 ms: 1.19x slower                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 3.11 ms: 1.20x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.61 ms: 1.20x slower                                                      |
| unpickle_pure_python       | 130 us                                                      | 156 us: 1.20x slower                                                       |
| fannkuch                   | 252 ms                                                      | 307 ms: 1.22x slower                                                       |
| nbody                      | 66.3 ms                                                     | 81.0 ms: 1.22x slower                                                      |
| chaos                      | 37.9 ms                                                     | 46.4 ms: 1.22x slower                                                      |
| meteor_contest             | 72.0 ms                                                     | 88.2 ms: 1.23x slower                                                      |
| async_generators           | 223 ms                                                      | 275 ms: 1.23x slower                                                       |
| scimark_fft                | 175 ms                                                      | 216 ms: 1.24x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 45.2 ms: 1.24x slower                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 50.8 ms: 1.25x slower                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 57.4 ms: 1.26x slower                                                      |
| genshi_xml                 | 33.9 ms                                                     | 42.7 ms: 1.26x slower                                                      |
| typing_runtime_protocols   | 103 us                                                      | 130 us: 1.26x slower                                                       |
| richards                   | 26.3 ms                                                     | 33.6 ms: 1.28x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 239 us: 1.29x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.44 ms: 1.29x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 73.1 ms: 1.30x slower                                                      |
| many_optionals             | 361 us                                                      | 472 us: 1.31x slower                                                       |
| richards_super             | 29.8 ms                                                     | 39.1 ms: 1.31x slower                                                      |
| genshi_text                | 15.2 ms                                                     | 20.3 ms: 1.33x slower                                                      |
| bench_thread_pool          | 810 us                                                      | 1.09 ms: 1.34x slower                                                      |
| django_template            | 20.3 ms                                                     | 27.3 ms: 1.35x slower                                                      |
| raytrace                   | 153 ms                                                      | 209 ms: 1.37x slower                                                       |
| mako                       | 6.56 ms                                                     | 9.63 ms: 1.47x slower                                                      |
| coverage                   | 45.3 ms                                                     | 68.3 ms: 1.51x slower                                                      |
| k_core                     | 1.70 sec                                                    | 2.69 sec: 1.58x slower                                                     |
| pprint_pformat             | 977 ms                                                      | 1.72 sec: 1.76x slower                                                     |
| subparsers                 | 10.9 ms                                                     | 19.2 ms: 1.77x slower                                                      |
| shortest_path              | 355 ms                                                      | 651 ms: 1.83x slower                                                       |
| docutils                   | 1.53 sec                                                    | 2.87 sec: 1.87x slower                                                     |
| bpe_tokeniser              | 2.87 sec                                                    | 5.49 sec: 1.91x slower                                                     |
| tomli_loads                | 1.37 sec                                                    | 2.66 sec: 1.94x slower                                                     |
| connected_components       | 320 ms                                                      | 622 ms: 1.94x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.07x slower                                                               |

Benchmark hidden because not significant (2): regex_dna, pylint
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250719-3.15.0a0-800d37f-NOGIL/bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.061x slower

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.10x
- 95% likely to have a slowdown of 1.09x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: unknown