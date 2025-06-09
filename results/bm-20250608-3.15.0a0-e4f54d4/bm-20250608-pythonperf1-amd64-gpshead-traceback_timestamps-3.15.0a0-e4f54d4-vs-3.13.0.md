# Results vs. 3.13.0

- fork: gpshead
- ref: traceback_timestamps
- machine: windows-amd64
- commit hash: e4f54d4
- commit date: 2025-06-08
- overall geometric mean: 1.025x slower
- HPT reliability: 97.63%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-pythonperf1-amd64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 222 ms: 1.03x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.62 sec: 1.06x slower                                                      |
| html5lib       | 38.2 ms                                                     | 39.0 ms: 1.02x slower                                                       |
| sphinx         | 617 ms                                                      | 638 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-pythonperf1-amd64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 158 ms: 1.90x faster                                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 208 ms: 1.35x faster                                                        |
| async_tree_io              | 513 ms                                                      | 389 ms: 1.32x faster                                                        |
| async_tree_none            | 219 ms                                                      | 170 ms: 1.29x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 206 ms: 1.29x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 392 ms: 1.27x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 171 ms: 1.17x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 331 ms: 1.15x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 338 ms: 1.13x faster                                                        |
| async_generators           | 223 ms                                                      | 232 ms: 1.04x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.9 ms: 1.11x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.23x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-pythonperf1-amd64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 44.0 ms: 1.15x faster                                                       |
| nbody          | 66.3 ms                                                     | 62.8 ms: 1.05x faster                                                       |
| pidigits       | 146 ms                                                      | 149 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-pythonperf1-amd64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.9 ms: 1.71x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.53 ms: 1.11x faster                                                       |
| regex_dna      | 115 ms                                                      | 121 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-pythonperf1-amd64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.1 us: 1.07x faster                                                       |
| xml_etree_parse      | 92.2 ms                                                     | 89.7 ms: 1.03x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.39 sec: 1.01x slower                                                      |
| json_dumps           | 6.19 ms                                                     | 6.31 ms: 1.02x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 55.6 ms: 1.04x slower                                                       |
| unpickle_pure_python | 130 us                                                      | 137 us: 1.05x slower                                                        |
| xml_etree_process    | 36.5 ms                                                     | 39.0 ms: 1.07x slower                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 64.8 ms: 1.07x slower                                                       |
| pickle_pure_python   | 186 us                                                      | 212 us: 1.14x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-pythonperf1-amd64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.2 ms: 1.08x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 19.6 ms: 1.16x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-pythonperf1-amd64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 15.2 ms                                                     | 15.4 ms: 1.01x slower                                                       |
| mako            | 6.56 ms                                                     | 6.65 ms: 1.01x slower                                                       |
| django_template | 20.3 ms                                                     | 24.0 ms: 1.18x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.05x slower                                                                |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-pythonperf1-amd64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 32.4 ms: 2.32x faster                                                       |
| asyncio_websockets         | 300 ms                                                      | 158 ms: 1.90x faster                                                        |
| mdp                        | 1.43 sec                                                    | 801 ms: 1.79x faster                                                        |
| regex_v8                   | 23.8 ms                                                     | 13.9 ms: 1.71x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 208 ms: 1.35x faster                                                        |
| async_tree_io              | 513 ms                                                      | 389 ms: 1.32x faster                                                        |
| deepcopy                   | 223 us                                                      | 171 us: 1.31x faster                                                        |
| async_tree_none            | 219 ms                                                      | 170 ms: 1.29x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 206 ms: 1.29x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 392 ms: 1.27x faster                                                        |
| deepcopy_memo              | 23.1 us                                                     | 18.3 us: 1.26x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 171 ms: 1.17x faster                                                        |
| float                      | 50.8 ms                                                     | 44.0 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 331 ms: 1.15x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 338 ms: 1.13x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.53 ms: 1.11x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.84 us: 1.10x faster                                                       |
| go                         | 84.7 ms                                                     | 77.3 ms: 1.10x faster                                                       |
| json                       | 3.30 ms                                                     | 3.03 ms: 1.09x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.1 us: 1.07x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.57 ms: 1.06x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 60.1 ms: 1.06x faster                                                       |
| nbody                      | 66.3 ms                                                     | 62.8 ms: 1.05x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 89.7 ms: 1.03x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.55 ms: 1.02x faster                                                       |
| scimark_sor                | 76.2 ms                                                     | 75.2 ms: 1.01x faster                                                       |
| sympy_str                  | 167 ms                                                      | 168 ms: 1.01x slower                                                        |
| genshi_text                | 15.2 ms                                                     | 15.4 ms: 1.01x slower                                                       |
| mako                       | 6.56 ms                                                     | 6.65 ms: 1.01x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 57.4 ms: 1.01x slower                                                       |
| pidigits                   | 146 ms                                                      | 149 ms: 1.01x slower                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.39 sec: 1.01x slower                                                      |
| pyflate                    | 283 ms                                                      | 287 ms: 1.01x slower                                                        |
| fannkuch                   | 252 ms                                                      | 256 ms: 1.02x slower                                                        |
| scimark_monte_carlo        | 40.7 ms                                                     | 41.5 ms: 1.02x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 6.31 ms: 1.02x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 73.4 ms: 1.02x slower                                                       |
| scimark_fft                | 175 ms                                                      | 178 ms: 1.02x slower                                                        |
| html5lib                   | 38.2 ms                                                     | 39.0 ms: 1.02x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 40.9 ms: 1.02x slower                                                       |
| generators                 | 19.0 ms                                                     | 19.5 ms: 1.03x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 87.4 ms: 1.03x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.95 sec: 1.03x slower                                                      |
| shortest_path              | 355 ms                                                      | 365 ms: 1.03x slower                                                        |
| 2to3                       | 215 ms                                                      | 222 ms: 1.03x slower                                                        |
| sqlite_synth               | 1.59 us                                                     | 1.64 us: 1.03x slower                                                       |
| sphinx                     | 617 ms                                                      | 638 ms: 1.03x slower                                                        |
| xml_etree_generate         | 53.5 ms                                                     | 55.6 ms: 1.04x slower                                                       |
| async_generators           | 223 ms                                                      | 232 ms: 1.04x slower                                                        |
| crypto_pyaes               | 45.6 ms                                                     | 47.6 ms: 1.04x slower                                                       |
| comprehensions             | 10.4 us                                                     | 10.9 us: 1.05x slower                                                       |
| regex_dna                  | 115 ms                                                      | 121 ms: 1.05x slower                                                        |
| unpickle_pure_python       | 130 us                                                      | 137 us: 1.05x slower                                                        |
| chaos                      | 37.9 ms                                                     | 39.8 ms: 1.05x slower                                                       |
| connected_components       | 320 ms                                                      | 337 ms: 1.05x slower                                                        |
| richards                   | 26.3 ms                                                     | 27.7 ms: 1.06x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.62 sec: 1.06x slower                                                      |
| richards_super             | 29.8 ms                                                     | 31.5 ms: 1.06x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 39.0 ms: 1.07x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 64.8 ms: 1.07x slower                                                       |
| python_startup             | 24.4 ms                                                     | 26.2 ms: 1.08x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.14 ms: 1.08x slower                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.32 ms: 1.08x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.31 us: 1.09x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 61.6 ms: 1.10x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.79 us: 1.10x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.17 ms: 1.11x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.9 ms: 1.11x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 212 us: 1.14x slower                                                        |
| pprint_safe_repr           | 485 ms                                                      | 554 ms: 1.14x slower                                                        |
| pprint_pformat             | 977 ms                                                      | 1.12 sec: 1.15x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 19.6 ms: 1.16x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.23 ms: 1.18x slower                                                       |
| django_template            | 20.3 ms                                                     | 24.0 ms: 1.18x slower                                                       |
| raytrace                   | 153 ms                                                      | 183 ms: 1.20x slower                                                        |
| many_optionals             | 361 us                                                      | 435 us: 1.20x slower                                                        |
| subparsers                 | 10.9 ms                                                     | 16.8 ms: 1.55x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 324 ns: 5.93x slower                                                        |
| coverage                   | 45.3 ms                                                     | 291 ms: 6.42x slower                                                        |
| thrift                     | 8.47 ms                                                     | 93.6 ms: 11.05x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                                |

Benchmark hidden because not significant (8): pylint, k_core, typing_runtime_protocols, regex_compile, sympy_expand, sympy_integrate, pycparser, genshi_xml
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250608-3.15.0a0-e4f54d4/bm-20250608-pythonperf1-amd64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.025x slower

# HPT report

- Reliability score: 97.63% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown