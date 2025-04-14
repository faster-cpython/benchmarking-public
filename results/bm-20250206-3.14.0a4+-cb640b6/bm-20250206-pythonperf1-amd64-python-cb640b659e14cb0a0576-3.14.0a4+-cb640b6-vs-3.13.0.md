# Results vs. 3.13.0

- fork: python
- ref: cb640b659e14cb0a0576
- machine: windows-amd64
- commit hash: cb640b6
- commit date: 2025-02-06
- overall geometric mean: 1.009x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.02x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250206-pythonperf1-amd64-python-cb640b659e14cb0a0576-3.14.0a4+-cb640b6 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 228 ms: 1.06x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.64 sec: 1.07x slower                                                      |
| html5lib       | 38.2 ms                                                     | 39.6 ms: 1.04x slower                                                       |
| sphinx         | 617 ms                                                      | 643 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                       | 1.05x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250206-pythonperf1-amd64-python-cb640b659e14cb0a0576-3.14.0a4+-cb640b6 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 216 ms: 1.30x faster                                                        |
| async_tree_io              | 513 ms                                                      | 417 ms: 1.23x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 405 ms: 1.23x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 220 ms: 1.20x faster                                                        |
| async_tree_none            | 219 ms                                                      | 185 ms: 1.18x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 175 ms: 1.14x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 336 ms: 1.13x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 341 ms: 1.12x faster                                                        |
| async_generators           | 223 ms                                                      | 227 ms: 1.02x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.0 ms: 1.04x slower                                                       |
| asyncio_websockets         | 300 ms                                                      | 314 ms: 1.05x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250206-pythonperf1-amd64-python-cb640b659e14cb0a0576-3.14.0a4+-cb640b6 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 45.7 ms: 1.11x faster                                                       |
| pidigits       | 146 ms                                                      | 152 ms: 1.03x slower                                                        |
| nbody          | 66.3 ms                                                     | 72.2 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                       | 1.00x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250206-pythonperf1-amd64-python-cb640b659e14cb0a0576-3.14.0a4+-cb640b6 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 15.5 ms: 1.54x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.46 ms: 1.16x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 84.7 ms: 1.05x slower                                                       |
| regex_dna      | 115 ms                                                      | 124 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250206-pythonperf1-amd64-python-cb640b659e14cb0a0576-3.14.0a4+-cb640b6 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.36 sec: 1.01x faster                                                      |
| json_loads           | 15.1 us                                                     | 15.3 us: 1.01x slower                                                       |
| xml_etree_parse      | 92.2 ms                                                     | 94.1 ms: 1.02x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 55.5 ms: 1.04x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 39.1 ms: 1.07x slower                                                       |
| unpickle_pure_python | 130 us                                                      | 140 us: 1.08x slower                                                        |
| json_dumps           | 6.19 ms                                                     | 6.78 ms: 1.09x slower                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 67.3 ms: 1.11x slower                                                       |
| pickle_pure_python   | 186 us                                                      | 214 us: 1.15x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.06x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250206-pythonperf1-amd64-python-cb640b659e14cb0a0576-3.14.0a4+-cb640b6 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.2 ms: 1.07x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 19.4 ms: 1.14x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250206-pythonperf1-amd64-python-cb640b659e14cb0a0576-3.14.0a4+-cb640b6 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 15.2 ms                                                     | 15.5 ms: 1.02x slower                                                       |
| django_template | 20.3 ms                                                     | 25.5 ms: 1.25x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.07x slower                                                                |

Benchmark hidden because not significant (2): mako, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250206-pythonperf1-amd64-python-cb640b659e14cb0a0576-3.14.0a4+-cb640b6 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 515 us: 16.44x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 15.5 ms: 1.54x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 216 ms: 1.30x faster                                                        |
| deepcopy                   | 223 us                                                      | 182 us: 1.23x faster                                                        |
| async_tree_io              | 513 ms                                                      | 417 ms: 1.23x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 405 ms: 1.23x faster                                                        |
| pathlib                    | 75.3 ms                                                     | 61.5 ms: 1.22x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 18.9 us: 1.22x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 220 ms: 1.20x faster                                                        |
| async_tree_none            | 219 ms                                                      | 185 ms: 1.18x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.46 ms: 1.16x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 175 ms: 1.14x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 336 ms: 1.13x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 341 ms: 1.12x faster                                                        |
| float                      | 50.8 ms                                                     | 45.7 ms: 1.11x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.87 us: 1.08x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 59.0 ms: 1.08x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.72 ms: 1.03x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.55 ms: 1.02x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.36 sec: 1.01x faster                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.57 us: 1.01x faster                                                       |
| json_loads                 | 15.1 us                                                     | 15.3 us: 1.01x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 15.5 ms: 1.02x slower                                                       |
| go                         | 84.7 ms                                                     | 86.1 ms: 1.02x slower                                                       |
| async_generators           | 223 ms                                                      | 227 ms: 1.02x slower                                                        |
| xml_etree_parse            | 92.2 ms                                                     | 94.1 ms: 1.02x slower                                                       |
| k_core                     | 1.70 sec                                                    | 1.74 sec: 1.02x slower                                                      |
| typing_runtime_protocols   | 103 us                                                      | 106 us: 1.03x slower                                                        |
| gc_traversal               | 1.96 ms                                                     | 2.03 ms: 1.03x slower                                                       |
| pidigits                   | 146 ms                                                      | 152 ms: 1.03x slower                                                        |
| html5lib                   | 38.2 ms                                                     | 39.6 ms: 1.04x slower                                                       |
| generators                 | 19.0 ms                                                     | 19.7 ms: 1.04x slower                                                       |
| pyflate                    | 283 ms                                                      | 294 ms: 1.04x slower                                                        |
| xml_etree_generate         | 53.5 ms                                                     | 55.5 ms: 1.04x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.0 ms: 1.04x slower                                                       |
| sphinx                     | 617 ms                                                      | 643 ms: 1.04x slower                                                        |
| sympy_expand               | 286 ms                                                      | 299 ms: 1.05x slower                                                        |
| sympy_str                  | 167 ms                                                      | 175 ms: 1.05x slower                                                        |
| meteor_contest             | 72.0 ms                                                     | 75.3 ms: 1.05x slower                                                       |
| asyncio_websockets         | 300 ms                                                      | 314 ms: 1.05x slower                                                        |
| pycparser                  | 695 ms                                                      | 728 ms: 1.05x slower                                                        |
| scimark_fft                | 175 ms                                                      | 183 ms: 1.05x slower                                                        |
| bench_thread_pool          | 810 us                                                      | 850 us: 1.05x slower                                                        |
| regex_compile              | 80.7 ms                                                     | 84.7 ms: 1.05x slower                                                       |
| coverage                   | 45.3 ms                                                     | 47.6 ms: 1.05x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 42.3 ms: 1.06x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 48.1 ms: 1.06x slower                                                       |
| comprehensions             | 10.4 us                                                     | 10.9 us: 1.06x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 90.0 ms: 1.06x slower                                                       |
| 2to3                       | 215 ms                                                      | 228 ms: 1.06x slower                                                        |
| bench_mp_pool              | 84.2 ms                                                     | 89.4 ms: 1.06x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 60.2 ms: 1.06x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.2 ms: 1.07x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 39.1 ms: 1.07x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.62 us: 1.07x slower                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 43.7 ms: 1.07x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.20 us: 1.07x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.64 sec: 1.07x slower                                                      |
| python_startup             | 24.4 ms                                                     | 26.2 ms: 1.07x slower                                                       |
| sqlglot_optimize           | 32.5 ms                                                     | 35.0 ms: 1.07x slower                                                       |
| regex_dna                  | 115 ms                                                      | 124 ms: 1.07x slower                                                        |
| logging_silent             | 54.6 ns                                                     | 58.9 ns: 1.08x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 140 us: 1.08x slower                                                        |
| fannkuch                   | 252 ms                                                      | 272 ms: 1.08x slower                                                        |
| pprint_pformat             | 977 ms                                                      | 1.06 sec: 1.09x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 528 ms: 1.09x slower                                                        |
| nbody                      | 66.3 ms                                                     | 72.2 ms: 1.09x slower                                                       |
| richards_super             | 29.8 ms                                                     | 32.5 ms: 1.09x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 6.78 ms: 1.09x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 83.5 ms: 1.10x slower                                                       |
| sqlglot_normalize          | 172 ms                                                      | 188 ms: 1.10x slower                                                        |
| chaos                      | 37.9 ms                                                     | 41.8 ms: 1.10x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.27 ms: 1.11x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 67.3 ms: 1.11x slower                                                       |
| mdp                        | 1.43 sec                                                    | 1.59 sec: 1.11x slower                                                      |
| richards                   | 26.3 ms                                                     | 29.2 ms: 1.11x slower                                                       |
| sqlglot_transpile          | 953 us                                                      | 1.06 ms: 1.12x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 63.2 ms: 1.13x slower                                                       |
| sqlglot_parse              | 764 us                                                      | 863 us: 1.13x slower                                                        |
| deltablue                  | 1.89 ms                                                     | 2.15 ms: 1.14x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 19.4 ms: 1.14x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 214 us: 1.15x slower                                                        |
| many_optionals             | 361 us                                                      | 437 us: 1.21x slower                                                        |
| django_template            | 20.3 ms                                                     | 25.5 ms: 1.25x slower                                                       |
| raytrace                   | 153 ms                                                      | 193 ms: 1.26x slower                                                        |
| subparsers                 | 10.9 ms                                                     | 16.4 ms: 1.52x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (8): json, pylint, create_gc_cycles, shortest_path, bpe_tokeniser, connected_components, mako, genshi_xml
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http

- Geometric mean (including insignificant results): 1.009x faster

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: unknown