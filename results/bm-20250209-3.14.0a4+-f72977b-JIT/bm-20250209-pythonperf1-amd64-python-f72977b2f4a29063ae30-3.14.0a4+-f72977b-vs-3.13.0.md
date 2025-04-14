# Results vs. 3.13.0

- fork: python
- ref: f72977b2f4a29063ae30
- machine: windows-amd64
- commit hash: f72977b
- commit date: 2025-02-09
- overall geometric mean: 1.035x faster
- HPT reliability: 65.70%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250209-pythonperf1-amd64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 223 ms: 1.04x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.72 sec: 1.12x slower                                                      |
| html5lib       | 38.2 ms                                                     | 39.8 ms: 1.04x slower                                                       |
| sphinx         | 617 ms                                                      | 646 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                       | 1.06x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250209-pythonperf1-amd64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 217 ms: 1.30x faster                                                        |
| async_tree_io              | 513 ms                                                      | 408 ms: 1.26x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 403 ms: 1.23x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 220 ms: 1.20x faster                                                        |
| async_tree_none            | 219 ms                                                      | 183 ms: 1.20x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 174 ms: 1.15x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 337 ms: 1.13x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 342 ms: 1.12x faster                                                        |
| coroutines                 | 12.5 ms                                                     | 13.1 ms: 1.05x slower                                                       |
| async_generators           | 223 ms                                                      | 238 ms: 1.07x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.13x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250209-pythonperf1-amd64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 59.4 ms: 1.11x faster                                                       |
| float          | 50.8 ms                                                     | 46.0 ms: 1.11x faster                                                       |
| pidigits       | 146 ms                                                      | 151 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250209-pythonperf1-amd64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.7 ms: 1.62x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.42 ms: 1.19x faster                                                       |
| regex_dna      | 115 ms                                                      | 113 ms: 1.02x faster                                                        |
| regex_compile  | 80.7 ms                                                     | 81.8 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250209-pythonperf1-amd64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 130 us                                                      | 113 us: 1.15x faster                                                        |
| tomli_loads          | 1.37 sec                                                    | 1.19 sec: 1.15x faster                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 49.7 ms: 1.08x faster                                                       |
| xml_etree_parse      | 92.2 ms                                                     | 88.7 ms: 1.04x faster                                                       |
| xml_etree_process    | 36.5 ms                                                     | 35.8 ms: 1.02x faster                                                       |
| json_dumps           | 6.19 ms                                                     | 6.57 ms: 1.06x slower                                                       |
| pickle_pure_python   | 186 us                                                      | 208 us: 1.12x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (2): xml_etree_iterparse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250209-pythonperf1-amd64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.3 ms: 1.04x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 19.2 ms: 1.13x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.08x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250209-pythonperf1-amd64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.25 ms: 1.25x faster                                                       |
| genshi_xml      | 33.9 ms                                                     | 35.3 ms: 1.04x slower                                                       |
| genshi_text     | 15.2 ms                                                     | 15.9 ms: 1.05x slower                                                       |
| django_template | 20.3 ms                                                     | 25.3 ms: 1.25x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.02x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250209-pythonperf1-amd64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 513 us: 16.49x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.7 ms: 1.62x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 217 ms: 1.30x faster                                                        |
| pathlib                    | 75.3 ms                                                     | 58.1 ms: 1.30x faster                                                       |
| async_tree_io              | 513 ms                                                      | 408 ms: 1.26x faster                                                        |
| mako                       | 6.56 ms                                                     | 5.25 ms: 1.25x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.10 ms: 1.24x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 403 ms: 1.23x faster                                                        |
| deepcopy                   | 223 us                                                      | 184 us: 1.22x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 220 ms: 1.20x faster                                                        |
| async_tree_none            | 219 ms                                                      | 183 ms: 1.20x faster                                                        |
| scimark_fft                | 175 ms                                                      | 147 ms: 1.19x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.42 ms: 1.19x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 174 ms: 1.15x faster                                                        |
| unpickle_pure_python       | 130 us                                                      | 113 us: 1.15x faster                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.19 sec: 1.15x faster                                                      |
| deepcopy_memo              | 23.1 us                                                     | 20.2 us: 1.14x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 337 ms: 1.13x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 342 ms: 1.12x faster                                                        |
| nbody                      | 66.3 ms                                                     | 59.4 ms: 1.11x faster                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.58 sec: 1.11x faster                                                      |
| float                      | 50.8 ms                                                     | 46.0 ms: 1.11x faster                                                       |
| fannkuch                   | 252 ms                                                      | 228 ms: 1.10x faster                                                        |
| spectral_norm              | 63.4 ms                                                     | 58.4 ms: 1.09x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.49 ms: 1.08x faster                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 49.7 ms: 1.08x faster                                                       |
| json                       | 3.30 ms                                                     | 3.14 ms: 1.05x faster                                                       |
| k_core                     | 1.70 sec                                                    | 1.62 sec: 1.05x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 88.7 ms: 1.04x faster                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.53 us: 1.04x faster                                                       |
| pyflate                    | 283 ms                                                      | 273 ms: 1.04x faster                                                        |
| shortest_path              | 355 ms                                                      | 344 ms: 1.03x faster                                                        |
| connected_components       | 320 ms                                                      | 311 ms: 1.03x faster                                                        |
| deepcopy_reduce            | 2.02 us                                                     | 1.97 us: 1.03x faster                                                       |
| regex_dna                  | 115 ms                                                      | 113 ms: 1.02x faster                                                        |
| xml_etree_process          | 36.5 ms                                                     | 35.8 ms: 1.02x faster                                                       |
| pprint_pformat             | 977 ms                                                      | 987 ms: 1.01x slower                                                        |
| regex_compile              | 80.7 ms                                                     | 81.8 ms: 1.01x slower                                                       |
| go                         | 84.7 ms                                                     | 85.9 ms: 1.01x slower                                                       |
| pidigits                   | 146 ms                                                      | 151 ms: 1.03x slower                                                        |
| dulwich_log                | 40.1 ms                                                     | 41.5 ms: 1.04x slower                                                       |
| 2to3                       | 215 ms                                                      | 223 ms: 1.04x slower                                                        |
| python_startup             | 24.4 ms                                                     | 25.3 ms: 1.04x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 841 us: 1.04x slower                                                        |
| genshi_xml                 | 33.9 ms                                                     | 35.3 ms: 1.04x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 74.9 ms: 1.04x slower                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 87.7 ms: 1.04x slower                                                       |
| pprint_safe_repr           | 485 ms                                                      | 505 ms: 1.04x slower                                                        |
| html5lib                   | 38.2 ms                                                     | 39.8 ms: 1.04x slower                                                       |
| coverage                   | 45.3 ms                                                     | 47.4 ms: 1.05x slower                                                       |
| generators                 | 19.0 ms                                                     | 19.8 ms: 1.05x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 15.9 ms: 1.05x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.1 ms: 1.05x slower                                                       |
| sphinx                     | 617 ms                                                      | 646 ms: 1.05x slower                                                        |
| sympy_sum                  | 85.2 ms                                                     | 89.5 ms: 1.05x slower                                                       |
| sympy_str                  | 167 ms                                                      | 175 ms: 1.05x slower                                                        |
| json_dumps                 | 6.19 ms                                                     | 6.57 ms: 1.06x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 58.0 ns: 1.06x slower                                                       |
| sympy_expand               | 286 ms                                                      | 304 ms: 1.06x slower                                                        |
| scimark_lu                 | 56.7 ms                                                     | 60.6 ms: 1.07x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 110 us: 1.07x slower                                                        |
| comprehensions             | 10.4 us                                                     | 11.1 us: 1.07x slower                                                       |
| async_generators           | 223 ms                                                      | 238 ms: 1.07x slower                                                        |
| scimark_monte_carlo        | 40.7 ms                                                     | 43.9 ms: 1.08x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.68 us: 1.08x slower                                                       |
| richards                   | 26.3 ms                                                     | 28.5 ms: 1.08x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.27 us: 1.09x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 61.1 ms: 1.09x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.4 ms: 1.09x slower                                                       |
| chaos                      | 37.9 ms                                                     | 41.4 ms: 1.09x slower                                                       |
| sqlglot_parse              | 764 us                                                      | 838 us: 1.10x slower                                                        |
| scimark_sor                | 76.2 ms                                                     | 83.6 ms: 1.10x slower                                                       |
| richards_super             | 29.8 ms                                                     | 32.7 ms: 1.10x slower                                                       |
| mdp                        | 1.43 sec                                                    | 1.59 sec: 1.11x slower                                                      |
| sqlglot_transpile          | 953 us                                                      | 1.06 ms: 1.12x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 208 us: 1.12x slower                                                        |
| docutils                   | 1.53 sec                                                    | 1.72 sec: 1.12x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 19.2 ms: 1.13x slower                                                       |
| sqlglot_optimize           | 32.5 ms                                                     | 37.0 ms: 1.14x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.38 ms: 1.14x slower                                                       |
| sqlglot_normalize          | 172 ms                                                      | 200 ms: 1.17x slower                                                        |
| deltablue                  | 1.89 ms                                                     | 2.29 ms: 1.21x slower                                                       |
| django_template            | 20.3 ms                                                     | 25.3 ms: 1.25x slower                                                       |
| many_optionals             | 361 us                                                      | 452 us: 1.25x slower                                                        |
| raytrace                   | 153 ms                                                      | 196 ms: 1.28x slower                                                        |
| subparsers                 | 10.9 ms                                                     | 15.9 ms: 1.47x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (8): pylint, create_gc_cycles, xml_etree_iterparse, asyncio_websockets, crypto_pyaes, gc_traversal, json_loads, pycparser
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http

- Geometric mean (including insignificant results): 1.035x faster

# HPT report

- Reliability score: 65.70% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown