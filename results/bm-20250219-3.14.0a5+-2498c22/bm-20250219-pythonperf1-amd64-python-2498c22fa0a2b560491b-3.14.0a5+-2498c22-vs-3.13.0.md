# Results vs. 3.13.0

- fork: python
- ref: 2498c22fa0a2b560491b
- machine: windows-amd64
- commit hash: 2498c22
- commit date: 2025-02-19
- overall geometric mean: 1.013x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250219-pythonperf1-amd64-python-2498c22fa0a2b560491b-3.14.0a5+-2498c22 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 223 ms: 1.04x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.65 sec: 1.08x slower                                                      |
| html5lib       | 38.2 ms                                                     | 39.7 ms: 1.04x slower                                                       |
| sphinx         | 617 ms                                                      | 642 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                       | 1.05x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250219-pythonperf1-amd64-python-2498c22fa0a2b560491b-3.14.0a5+-2498c22 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 214 ms: 1.31x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 403 ms: 1.23x faster                                                        |
| async_tree_io              | 513 ms                                                      | 416 ms: 1.23x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 218 ms: 1.22x faster                                                        |
| async_tree_none            | 219 ms                                                      | 187 ms: 1.17x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 176 ms: 1.14x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 337 ms: 1.13x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 341 ms: 1.12x faster                                                        |
| asyncio_websockets         | 300 ms                                                      | 309 ms: 1.03x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.2 ms: 1.06x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.13x faster                                                                |

Benchmark hidden because not significant (1): async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250219-pythonperf1-amd64-python-2498c22fa0a2b560491b-3.14.0a5+-2498c22 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 45.4 ms: 1.12x faster                                                       |
| pidigits       | 146 ms                                                      | 153 ms: 1.04x slower                                                        |
| nbody          | 66.3 ms                                                     | 71.7 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                       | 1.00x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250219-pythonperf1-amd64-python-2498c22fa0a2b560491b-3.14.0a5+-2498c22 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.4 ms: 1.66x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.46 ms: 1.16x faster                                                       |
| regex_dna      | 115 ms                                                      | 114 ms: 1.01x faster                                                        |
| regex_compile  | 80.7 ms                                                     | 85.2 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250219-pythonperf1-amd64-python-2498c22fa0a2b560491b-3.14.0a5+-2498c22 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.41 sec: 1.03x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 62.6 ms: 1.03x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 56.6 ms: 1.06x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 6.75 ms: 1.09x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 39.8 ms: 1.09x slower                                                       |
| unpickle_pure_python | 130 us                                                      | 147 us: 1.13x slower                                                        |
| pickle_pure_python   | 186 us                                                      | 224 us: 1.21x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                                |

Benchmark hidden because not significant (2): json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250219-pythonperf1-amd64-python-2498c22fa0a2b560491b-3.14.0a5+-2498c22 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 24.8 ms: 1.02x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 19.0 ms: 1.12x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.07x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250219-pythonperf1-amd64-python-2498c22fa0a2b560491b-3.14.0a5+-2498c22 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.81 ms: 1.04x slower                                                       |
| genshi_xml      | 33.9 ms                                                     | 35.5 ms: 1.05x slower                                                       |
| genshi_text     | 15.2 ms                                                     | 16.2 ms: 1.06x slower                                                       |
| django_template | 20.3 ms                                                     | 24.8 ms: 1.22x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.09x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250219-pythonperf1-amd64-python-2498c22fa0a2b560491b-3.14.0a5+-2498c22 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 498 us: 17.01x faster                                                       |
| pathlib                    | 75.3 ms                                                     | 29.5 ms: 2.56x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.4 ms: 1.66x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 214 ms: 1.31x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 403 ms: 1.23x faster                                                        |
| async_tree_io              | 513 ms                                                      | 416 ms: 1.23x faster                                                        |
| deepcopy                   | 223 us                                                      | 183 us: 1.22x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 218 ms: 1.22x faster                                                        |
| async_tree_none            | 219 ms                                                      | 187 ms: 1.17x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.46 ms: 1.16x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 20.0 us: 1.16x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 176 ms: 1.14x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 337 ms: 1.13x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 341 ms: 1.12x faster                                                        |
| float                      | 50.8 ms                                                     | 45.4 ms: 1.12x faster                                                       |
| json                       | 3.30 ms                                                     | 3.00 ms: 1.10x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.90 us: 1.07x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 61.0 ms: 1.04x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.74 ms: 1.02x faster                                                       |
| shortest_path              | 355 ms                                                      | 349 ms: 1.02x faster                                                        |
| sqlite_synth               | 1.59 us                                                     | 1.56 us: 1.01x faster                                                       |
| regex_dna                  | 115 ms                                                      | 114 ms: 1.01x faster                                                        |
| bpe_tokeniser              | 2.87 sec                                                    | 2.88 sec: 1.00x slower                                                      |
| bench_mp_pool              | 84.2 ms                                                     | 84.9 ms: 1.01x slower                                                       |
| python_startup             | 24.4 ms                                                     | 24.8 ms: 1.02x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 105 us: 1.02x slower                                                        |
| generators                 | 19.0 ms                                                     | 19.4 ms: 1.02x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 831 us: 1.03x slower                                                        |
| asyncio_websockets         | 300 ms                                                      | 309 ms: 1.03x slower                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.41 sec: 1.03x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 62.6 ms: 1.03x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 88.2 ms: 1.04x slower                                                       |
| 2to3                       | 215 ms                                                      | 223 ms: 1.04x slower                                                        |
| mako                       | 6.56 ms                                                     | 6.81 ms: 1.04x slower                                                       |
| html5lib                   | 38.2 ms                                                     | 39.7 ms: 1.04x slower                                                       |
| sphinx                     | 617 ms                                                      | 642 ms: 1.04x slower                                                        |
| sympy_expand               | 286 ms                                                      | 297 ms: 1.04x slower                                                        |
| sympy_str                  | 167 ms                                                      | 173 ms: 1.04x slower                                                        |
| dulwich_log                | 40.1 ms                                                     | 41.7 ms: 1.04x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 74.9 ms: 1.04x slower                                                       |
| pidigits                   | 146 ms                                                      | 153 ms: 1.04x slower                                                        |
| genshi_xml                 | 33.9 ms                                                     | 35.5 ms: 1.05x slower                                                       |
| regex_compile              | 80.7 ms                                                     | 85.2 ms: 1.06x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.2 ms: 1.06x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 56.6 ms: 1.06x slower                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.76 ms: 1.06x slower                                                       |
| coverage                   | 45.3 ms                                                     | 48.1 ms: 1.06x slower                                                       |
| pycparser                  | 695 ms                                                      | 739 ms: 1.06x slower                                                        |
| genshi_text                | 15.2 ms                                                     | 16.2 ms: 1.06x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 58.2 ns: 1.07x slower                                                       |
| sqlglot_optimize           | 32.5 ms                                                     | 34.7 ms: 1.07x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.2 ms: 1.07x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.65 sec: 1.08x slower                                                      |
| mdp                        | 1.43 sec                                                    | 1.54 sec: 1.08x slower                                                      |
| nbody                      | 66.3 ms                                                     | 71.7 ms: 1.08x slower                                                       |
| fannkuch                   | 252 ms                                                      | 273 ms: 1.09x slower                                                        |
| json_dumps                 | 6.19 ms                                                     | 6.75 ms: 1.09x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 39.8 ms: 1.09x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.19 ms: 1.09x slower                                                       |
| comprehensions             | 10.4 us                                                     | 11.3 us: 1.09x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 49.9 ms: 1.09x slower                                                       |
| pyflate                    | 283 ms                                                      | 310 ms: 1.10x slower                                                        |
| pprint_safe_repr           | 485 ms                                                      | 534 ms: 1.10x slower                                                        |
| chaos                      | 37.9 ms                                                     | 41.8 ms: 1.10x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.08 sec: 1.10x slower                                                      |
| sqlglot_normalize          | 172 ms                                                      | 190 ms: 1.11x slower                                                        |
| scimark_fft                | 175 ms                                                      | 194 ms: 1.11x slower                                                        |
| logging_simple             | 5.77 us                                                     | 6.42 us: 1.11x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.88 us: 1.11x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 19.0 ms: 1.12x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 85.8 ms: 1.13x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 63.4 ms: 1.13x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 147 us: 1.13x slower                                                        |
| richards                   | 26.3 ms                                                     | 29.7 ms: 1.13x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 64.2 ms: 1.13x slower                                                       |
| richards_super             | 29.8 ms                                                     | 33.8 ms: 1.14x slower                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 46.3 ms: 1.14x slower                                                       |
| sqlglot_transpile          | 953 us                                                      | 1.10 ms: 1.16x slower                                                       |
| sqlglot_parse              | 764 us                                                      | 885 us: 1.16x slower                                                        |
| deltablue                  | 1.89 ms                                                     | 2.19 ms: 1.16x slower                                                       |
| many_optionals             | 361 us                                                      | 432 us: 1.19x slower                                                        |
| pickle_pure_python         | 186 us                                                      | 224 us: 1.21x slower                                                        |
| django_template            | 20.3 ms                                                     | 24.8 ms: 1.22x slower                                                       |
| raytrace                   | 153 ms                                                      | 196 ms: 1.28x slower                                                        |
| subparsers                 | 10.9 ms                                                     | 16.3 ms: 1.50x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (9): pylint, create_gc_cycles, k_core, json_loads, go, async_generators, connected_components, gc_traversal, xml_etree_parse
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http

- Geometric mean (including insignificant results): 1.013x faster

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown