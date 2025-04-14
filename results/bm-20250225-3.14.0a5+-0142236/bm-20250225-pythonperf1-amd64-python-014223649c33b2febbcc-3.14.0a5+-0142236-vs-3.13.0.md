# Results vs. 3.13.0

- fork: python
- ref: 014223649c33b2febbcc
- machine: windows-amd64
- commit hash: 0142236
- commit date: 2025-02-25
- overall geometric mean: 1.017x faster
- HPT reliability: 99.89%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-pythonperf1-amd64-python-014223649c33b2febbcc-3.14.0a5+-0142236 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 223 ms: 1.04x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.66 sec: 1.08x slower                                                      |
| html5lib       | 38.2 ms                                                     | 40.0 ms: 1.05x slower                                                       |
| sphinx         | 617 ms                                                      | 642 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                       | 1.05x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-pythonperf1-amd64-python-014223649c33b2febbcc-3.14.0a5+-0142236 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 209 ms: 1.34x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 402 ms: 1.24x faster                                                        |
| async_tree_io              | 513 ms                                                      | 417 ms: 1.23x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 219 ms: 1.21x faster                                                        |
| async_tree_none            | 219 ms                                                      | 190 ms: 1.15x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 175 ms: 1.14x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 343 ms: 1.12x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 342 ms: 1.11x faster                                                        |
| async_generators           | 223 ms                                                      | 219 ms: 1.02x faster                                                        |
| coroutines                 | 12.5 ms                                                     | 13.0 ms: 1.04x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.13x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-pythonperf1-amd64-python-014223649c33b2febbcc-3.14.0a5+-0142236 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 45.3 ms: 1.12x faster                                                       |
| pidigits       | 146 ms                                                      | 150 ms: 1.03x slower                                                        |
| nbody          | 66.3 ms                                                     | 69.2 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-pythonperf1-amd64-python-014223649c33b2febbcc-3.14.0a5+-0142236 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.2 ms: 1.67x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.42 ms: 1.19x faster                                                       |
| regex_dna      | 115 ms                                                      | 114 ms: 1.01x faster                                                        |
| regex_compile  | 80.7 ms                                                     | 85.6 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-pythonperf1-amd64-python-014223649c33b2febbcc-3.14.0a5+-0142236 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 89.1 ms: 1.03x faster                                                       |
| json_loads           | 15.1 us                                                     | 14.7 us: 1.03x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.41 sec: 1.03x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 62.5 ms: 1.03x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 56.1 ms: 1.05x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 6.66 ms: 1.08x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 39.9 ms: 1.09x slower                                                       |
| unpickle_pure_python | 130 us                                                      | 145 us: 1.12x slower                                                        |
| pickle_pure_python   | 186 us                                                      | 227 us: 1.22x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.06x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-pythonperf1-amd64-python-014223649c33b2febbcc-3.14.0a5+-0142236 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.1 ms: 1.03x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 19.0 ms: 1.12x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.08x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-pythonperf1-amd64-python-014223649c33b2febbcc-3.14.0a5+-0142236 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.75 ms: 1.03x slower                                                       |
| genshi_xml      | 33.9 ms                                                     | 35.7 ms: 1.05x slower                                                       |
| genshi_text     | 15.2 ms                                                     | 16.3 ms: 1.07x slower                                                       |
| django_template | 20.3 ms                                                     | 25.2 ms: 1.24x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.10x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-pythonperf1-amd64-python-014223649c33b2febbcc-3.14.0a5+-0142236 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 514 us: 16.46x faster                                                       |
| pathlib                    | 75.3 ms                                                     | 30.2 ms: 2.49x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.2 ms: 1.67x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 209 ms: 1.34x faster                                                        |
| deepcopy                   | 223 us                                                      | 181 us: 1.24x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 402 ms: 1.24x faster                                                        |
| async_tree_io              | 513 ms                                                      | 417 ms: 1.23x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 219 ms: 1.21x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.42 ms: 1.19x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 19.9 us: 1.16x faster                                                       |
| async_tree_none            | 219 ms                                                      | 190 ms: 1.15x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 175 ms: 1.14x faster                                                        |
| json                       | 3.30 ms                                                     | 2.94 ms: 1.12x faster                                                       |
| float                      | 50.8 ms                                                     | 45.3 ms: 1.12x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 343 ms: 1.12x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 342 ms: 1.11x faster                                                        |
| spectral_norm              | 63.4 ms                                                     | 58.4 ms: 1.09x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.92 us: 1.06x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.67 ms: 1.04x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 89.1 ms: 1.03x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.7 us: 1.03x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.55 ms: 1.02x faster                                                       |
| async_generators           | 223 ms                                                      | 219 ms: 1.02x faster                                                        |
| create_gc_cycles           | 1.22 ms                                                     | 1.21 ms: 1.01x faster                                                       |
| regex_dna                  | 115 ms                                                      | 114 ms: 1.01x faster                                                        |
| sqlite_synth               | 1.59 us                                                     | 1.57 us: 1.01x faster                                                       |
| shortest_path              | 355 ms                                                      | 354 ms: 1.00x faster                                                        |
| bpe_tokeniser              | 2.87 sec                                                    | 2.86 sec: 1.00x faster                                                      |
| bench_mp_pool              | 84.2 ms                                                     | 84.8 ms: 1.01x slower                                                       |
| connected_components       | 320 ms                                                      | 323 ms: 1.01x slower                                                        |
| go                         | 84.7 ms                                                     | 85.5 ms: 1.01x slower                                                       |
| coverage                   | 45.3 ms                                                     | 46.1 ms: 1.02x slower                                                       |
| k_core                     | 1.70 sec                                                    | 1.73 sec: 1.02x slower                                                      |
| generators                 | 19.0 ms                                                     | 19.4 ms: 1.02x slower                                                       |
| pidigits                   | 146 ms                                                      | 150 ms: 1.03x slower                                                        |
| typing_runtime_protocols   | 103 us                                                      | 106 us: 1.03x slower                                                        |
| mako                       | 6.56 ms                                                     | 6.75 ms: 1.03x slower                                                       |
| python_startup             | 24.4 ms                                                     | 25.1 ms: 1.03x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.41 sec: 1.03x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 62.5 ms: 1.03x slower                                                       |
| 2to3                       | 215 ms                                                      | 223 ms: 1.04x slower                                                        |
| sphinx                     | 617 ms                                                      | 642 ms: 1.04x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.0 ms: 1.04x slower                                                       |
| nbody                      | 66.3 ms                                                     | 69.2 ms: 1.04x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 41.9 ms: 1.05x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 89.2 ms: 1.05x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 849 us: 1.05x slower                                                        |
| sympy_str                  | 167 ms                                                      | 175 ms: 1.05x slower                                                        |
| html5lib                   | 38.2 ms                                                     | 40.0 ms: 1.05x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 56.1 ms: 1.05x slower                                                       |
| sympy_expand               | 286 ms                                                      | 300 ms: 1.05x slower                                                        |
| meteor_contest             | 72.0 ms                                                     | 75.8 ms: 1.05x slower                                                       |
| genshi_xml                 | 33.9 ms                                                     | 35.7 ms: 1.05x slower                                                       |
| regex_compile              | 80.7 ms                                                     | 85.6 ms: 1.06x slower                                                       |
| scimark_fft                | 175 ms                                                      | 186 ms: 1.06x slower                                                        |
| crypto_pyaes               | 45.6 ms                                                     | 48.5 ms: 1.06x slower                                                       |
| pyflate                    | 283 ms                                                      | 303 ms: 1.07x slower                                                        |
| genshi_text                | 15.2 ms                                                     | 16.3 ms: 1.07x slower                                                       |
| pycparser                  | 695 ms                                                      | 746 ms: 1.07x slower                                                        |
| fannkuch                   | 252 ms                                                      | 270 ms: 1.07x slower                                                        |
| sqlglot_optimize           | 32.5 ms                                                     | 34.9 ms: 1.07x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 6.66 ms: 1.08x slower                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 43.9 ms: 1.08x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.3 ms: 1.08x slower                                                       |
| mdp                        | 1.43 sec                                                    | 1.55 sec: 1.08x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.66 sec: 1.08x slower                                                      |
| scimark_sor                | 76.2 ms                                                     | 82.7 ms: 1.09x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 39.9 ms: 1.09x slower                                                       |
| comprehensions             | 10.4 us                                                     | 11.4 us: 1.10x slower                                                       |
| chaos                      | 37.9 ms                                                     | 41.7 ms: 1.10x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 62.6 ms: 1.10x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.86 us: 1.11x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 60.7 ns: 1.11x slower                                                       |
| sqlglot_normalize          | 172 ms                                                      | 191 ms: 1.11x slower                                                        |
| richards                   | 26.3 ms                                                     | 29.3 ms: 1.12x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 145 us: 1.12x slower                                                        |
| logging_simple             | 5.77 us                                                     | 6.48 us: 1.12x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 19.0 ms: 1.12x slower                                                       |
| sqlglot_transpile          | 953 us                                                      | 1.07 ms: 1.12x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 63.2 ms: 1.13x slower                                                       |
| richards_super             | 29.8 ms                                                     | 33.6 ms: 1.13x slower                                                       |
| sqlglot_parse              | 764 us                                                      | 865 us: 1.13x slower                                                        |
| pprint_pformat             | 977 ms                                                      | 1.11 sec: 1.13x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.37 ms: 1.14x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.16 ms: 1.14x slower                                                       |
| pprint_safe_repr           | 485 ms                                                      | 557 ms: 1.15x slower                                                        |
| many_optionals             | 361 us                                                      | 435 us: 1.20x slower                                                        |
| pickle_pure_python         | 186 us                                                      | 227 us: 1.22x slower                                                        |
| django_template            | 20.3 ms                                                     | 25.2 ms: 1.24x slower                                                       |
| raytrace                   | 153 ms                                                      | 191 ms: 1.24x slower                                                        |
| subparsers                 | 10.9 ms                                                     | 16.2 ms: 1.50x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (3): pylint, asyncio_websockets, gc_traversal
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http

- Geometric mean (including insignificant results): 1.017x faster

# HPT report

- Reliability score: 99.89% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown