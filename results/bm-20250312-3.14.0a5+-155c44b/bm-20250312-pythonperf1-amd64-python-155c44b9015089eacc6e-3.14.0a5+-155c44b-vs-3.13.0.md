# Results vs. 3.13.0

- fork: python
- ref: 155c44b9015089eacc6e
- machine: windows-amd64
- commit hash: 155c44b
- commit date: 2025-03-12
- overall geometric mean: 1.001x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-pythonperf1-amd64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 226 ms: 1.05x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.68 sec: 1.10x slower                                                      |
| html5lib       | 38.2 ms                                                     | 40.6 ms: 1.06x slower                                                       |
| sphinx         | 617 ms                                                      | 653 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                       | 1.07x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-pythonperf1-amd64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 216 ms: 1.30x faster                                                        |
| async_tree_io              | 513 ms                                                      | 424 ms: 1.21x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 222 ms: 1.19x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 420 ms: 1.18x faster                                                        |
| async_tree_none            | 219 ms                                                      | 189 ms: 1.16x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 341 ms: 1.12x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 339 ms: 1.12x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 179 ms: 1.12x faster                                                        |
| asyncio_websockets         | 300 ms                                                      | 306 ms: 1.02x slower                                                        |
| async_generators           | 223 ms                                                      | 228 ms: 1.02x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.6 ms: 1.09x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.11x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-pythonperf1-amd64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 46.1 ms: 1.10x faster                                                       |
| nbody          | 66.3 ms                                                     | 67.8 ms: 1.02x slower                                                       |
| pidigits       | 146 ms                                                      | 151 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-pythonperf1-amd64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.2 ms: 1.67x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.54 ms: 1.10x faster                                                       |
| regex_dna      | 115 ms                                                      | 119 ms: 1.03x slower                                                        |
| regex_compile  | 80.7 ms                                                     | 86.4 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-pythonperf1-amd64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.8 us: 1.02x faster                                                       |
| xml_etree_parse      | 92.2 ms                                                     | 90.8 ms: 1.02x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.44 sec: 1.05x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 64.6 ms: 1.07x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 6.92 ms: 1.12x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 60.0 ms: 1.12x slower                                                       |
| unpickle_pure_python | 130 us                                                      | 150 us: 1.15x slower                                                        |
| xml_etree_process    | 36.5 ms                                                     | 42.6 ms: 1.17x slower                                                       |
| pickle_pure_python   | 186 us                                                      | 227 us: 1.22x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-pythonperf1-amd64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.5 ms: 1.09x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 20.6 ms: 1.22x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.15x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-pythonperf1-amd64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.87 ms: 1.05x slower                                                       |
| genshi_xml      | 33.9 ms                                                     | 37.3 ms: 1.10x slower                                                       |
| genshi_text     | 15.2 ms                                                     | 17.0 ms: 1.12x slower                                                       |
| django_template | 20.3 ms                                                     | 25.7 ms: 1.26x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.13x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-pythonperf1-amd64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 520 us: 16.28x faster                                                       |
| pathlib                    | 75.3 ms                                                     | 32.1 ms: 2.35x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.2 ms: 1.67x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 216 ms: 1.30x faster                                                        |
| deepcopy                   | 223 us                                                      | 181 us: 1.23x faster                                                        |
| async_tree_io              | 513 ms                                                      | 424 ms: 1.21x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 222 ms: 1.19x faster                                                        |
| deepcopy_memo              | 23.1 us                                                     | 19.4 us: 1.19x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 420 ms: 1.18x faster                                                        |
| async_tree_none            | 219 ms                                                      | 189 ms: 1.16x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 341 ms: 1.12x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 339 ms: 1.12x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 179 ms: 1.12x faster                                                        |
| float                      | 50.8 ms                                                     | 46.1 ms: 1.10x faster                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.54 ms: 1.10x faster                                                       |
| json                       | 3.30 ms                                                     | 3.01 ms: 1.10x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 59.3 ms: 1.07x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.92 us: 1.05x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.54 ms: 1.02x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.8 us: 1.02x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 90.8 ms: 1.02x faster                                                       |
| generators                 | 19.0 ms                                                     | 19.2 ms: 1.01x slower                                                       |
| telco                      | 4.85 ms                                                     | 4.91 ms: 1.01x slower                                                       |
| k_core                     | 1.70 sec                                                    | 1.73 sec: 1.02x slower                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.62 us: 1.02x slower                                                       |
| asyncio_websockets         | 300 ms                                                      | 306 ms: 1.02x slower                                                        |
| nbody                      | 66.3 ms                                                     | 67.8 ms: 1.02x slower                                                       |
| async_generators           | 223 ms                                                      | 228 ms: 1.02x slower                                                        |
| create_gc_cycles           | 1.22 ms                                                     | 1.26 ms: 1.03x slower                                                       |
| pidigits                   | 146 ms                                                      | 151 ms: 1.03x slower                                                        |
| gc_traversal               | 1.96 ms                                                     | 2.03 ms: 1.03x slower                                                       |
| regex_dna                  | 115 ms                                                      | 119 ms: 1.03x slower                                                        |
| shortest_path              | 355 ms                                                      | 368 ms: 1.04x slower                                                        |
| scimark_fft                | 175 ms                                                      | 181 ms: 1.04x slower                                                        |
| go                         | 84.7 ms                                                     | 88.2 ms: 1.04x slower                                                       |
| mako                       | 6.56 ms                                                     | 6.87 ms: 1.05x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 89.4 ms: 1.05x slower                                                       |
| sympy_str                  | 167 ms                                                      | 175 ms: 1.05x slower                                                        |
| 2to3                       | 215 ms                                                      | 226 ms: 1.05x slower                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.44 sec: 1.05x slower                                                      |
| bench_mp_pool              | 84.2 ms                                                     | 88.5 ms: 1.05x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 42.4 ms: 1.06x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 3.04 sec: 1.06x slower                                                      |
| sphinx                     | 617 ms                                                      | 653 ms: 1.06x slower                                                        |
| scimark_lu                 | 56.7 ms                                                     | 60.0 ms: 1.06x slower                                                       |
| sympy_expand               | 286 ms                                                      | 303 ms: 1.06x slower                                                        |
| html5lib                   | 38.2 ms                                                     | 40.6 ms: 1.06x slower                                                       |
| pycparser                  | 695 ms                                                      | 740 ms: 1.06x slower                                                        |
| xml_etree_iterparse        | 60.5 ms                                                     | 64.6 ms: 1.07x slower                                                       |
| connected_components       | 320 ms                                                      | 341 ms: 1.07x slower                                                        |
| bench_thread_pool          | 810 us                                                      | 865 us: 1.07x slower                                                        |
| regex_compile              | 80.7 ms                                                     | 86.4 ms: 1.07x slower                                                       |
| coverage                   | 45.3 ms                                                     | 48.7 ms: 1.07x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 111 us: 1.07x slower                                                        |
| sympy_integrate            | 12.3 ms                                                     | 13.3 ms: 1.08x slower                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 44.1 ms: 1.08x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 59.1 ns: 1.08x slower                                                       |
| python_startup             | 24.4 ms                                                     | 26.5 ms: 1.09x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.6 ms: 1.09x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 78.3 ms: 1.09x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 83.3 ms: 1.09x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.68 sec: 1.10x slower                                                      |
| genshi_xml                 | 33.9 ms                                                     | 37.3 ms: 1.10x slower                                                       |
| mdp                        | 1.43 sec                                                    | 1.59 sec: 1.11x slower                                                      |
| pyflate                    | 283 ms                                                      | 314 ms: 1.11x slower                                                        |
| pprint_pformat             | 977 ms                                                      | 1.09 sec: 1.12x slower                                                      |
| json_dumps                 | 6.19 ms                                                     | 6.92 ms: 1.12x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 17.0 ms: 1.12x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 60.0 ms: 1.12x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 51.3 ms: 1.12x slower                                                       |
| fannkuch                   | 252 ms                                                      | 283 ms: 1.12x slower                                                        |
| hexiom                     | 3.84 ms                                                     | 4.34 ms: 1.13x slower                                                       |
| richards_super             | 29.8 ms                                                     | 33.8 ms: 1.13x slower                                                       |
| richards                   | 26.3 ms                                                     | 29.8 ms: 1.14x slower                                                       |
| comprehensions             | 10.4 us                                                     | 11.8 us: 1.14x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.62 us: 1.15x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 150 us: 1.15x slower                                                        |
| pprint_safe_repr           | 485 ms                                                      | 558 ms: 1.15x slower                                                        |
| nqueens                    | 56.1 ms                                                     | 64.8 ms: 1.15x slower                                                       |
| logging_format             | 6.18 us                                                     | 7.16 us: 1.16x slower                                                       |
| chaos                      | 37.9 ms                                                     | 43.9 ms: 1.16x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 42.6 ms: 1.17x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.25 ms: 1.19x slower                                                       |
| many_optionals             | 361 us                                                      | 435 us: 1.20x slower                                                        |
| python_startup_no_site     | 16.9 ms                                                     | 20.6 ms: 1.22x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 227 us: 1.22x slower                                                        |
| django_template            | 20.3 ms                                                     | 25.7 ms: 1.26x slower                                                       |
| raytrace                   | 153 ms                                                      | 199 ms: 1.30x slower                                                        |
| subparsers                 | 10.9 ms                                                     | 16.6 ms: 1.53x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (1): pylint
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250312-3.14.0a5+-155c44b/bm-20250312-pythonperf1-amd64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown