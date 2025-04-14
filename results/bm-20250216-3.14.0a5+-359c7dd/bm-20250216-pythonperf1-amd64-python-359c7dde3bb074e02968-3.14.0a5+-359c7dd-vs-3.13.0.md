# Results vs. 3.13.0

- fork: python
- ref: 359c7dde3bb074e02968
- machine: windows-amd64
- commit hash: 359c7dd
- commit date: 2025-02-16
- overall geometric mean: 1.005x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 223 ms: 1.04x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.65 sec: 1.08x slower                                                      |
| html5lib       | 38.2 ms                                                     | 39.5 ms: 1.03x slower                                                       |
| sphinx         | 617 ms                                                      | 640 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                       | 1.05x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 221 ms: 1.27x faster                                                        |
| async_tree_io              | 513 ms                                                      | 416 ms: 1.23x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 224 ms: 1.18x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 421 ms: 1.18x faster                                                        |
| async_tree_none            | 219 ms                                                      | 190 ms: 1.15x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 179 ms: 1.12x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 345 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 343 ms: 1.11x faster                                                        |
| asyncio_websockets         | 300 ms                                                      | 314 ms: 1.05x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.6 ms: 1.09x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.11x faster                                                                |

Benchmark hidden because not significant (1): async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 46.8 ms: 1.09x faster                                                       |
| pidigits       | 146 ms                                                      | 150 ms: 1.02x slower                                                        |
| nbody          | 66.3 ms                                                     | 68.9 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.3 ms: 1.67x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.42 ms: 1.19x faster                                                       |
| regex_dna      | 115 ms                                                      | 114 ms: 1.01x faster                                                        |
| regex_compile  | 80.7 ms                                                     | 86.0 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 89.6 ms: 1.03x faster                                                       |
| json_loads           | 15.1 us                                                     | 15.7 us: 1.04x slower                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.1 ms: 1.04x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.45 sec: 1.06x slower                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 56.8 ms: 1.06x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 6.68 ms: 1.08x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 40.0 ms: 1.10x slower                                                       |
| unpickle_pure_python | 130 us                                                      | 149 us: 1.15x slower                                                        |
| pickle_pure_python   | 186 us                                                      | 224 us: 1.20x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.08x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 24.6 ms: 1.01x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 18.7 ms: 1.10x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.05x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 35.3 ms: 1.04x slower                                                       |
| mako            | 6.56 ms                                                     | 6.89 ms: 1.05x slower                                                       |
| genshi_text     | 15.2 ms                                                     | 16.3 ms: 1.07x slower                                                       |
| django_template | 20.3 ms                                                     | 24.9 ms: 1.23x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.09x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 516 us: 16.41x faster                                                       |
| pathlib                    | 75.3 ms                                                     | 29.1 ms: 2.59x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.3 ms: 1.67x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 221 ms: 1.27x faster                                                        |
| async_tree_io              | 513 ms                                                      | 416 ms: 1.23x faster                                                        |
| deepcopy                   | 223 us                                                      | 187 us: 1.19x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.42 ms: 1.19x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 224 ms: 1.18x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 421 ms: 1.18x faster                                                        |
| async_tree_none            | 219 ms                                                      | 190 ms: 1.15x faster                                                        |
| deepcopy_memo              | 23.1 us                                                     | 20.6 us: 1.12x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 179 ms: 1.12x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 345 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 343 ms: 1.11x faster                                                        |
| float                      | 50.8 ms                                                     | 46.8 ms: 1.09x faster                                                       |
| json                       | 3.30 ms                                                     | 3.09 ms: 1.07x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.92 us: 1.06x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 60.7 ms: 1.04x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.69 ms: 1.03x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 89.6 ms: 1.03x faster                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.56 us: 1.01x faster                                                       |
| regex_dna                  | 115 ms                                                      | 114 ms: 1.01x faster                                                        |
| shortest_path              | 355 ms                                                      | 352 ms: 1.01x faster                                                        |
| bench_mp_pool              | 84.2 ms                                                     | 83.5 ms: 1.01x faster                                                       |
| connected_components       | 320 ms                                                      | 322 ms: 1.01x slower                                                        |
| python_startup             | 24.4 ms                                                     | 24.6 ms: 1.01x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.92 sec: 1.02x slower                                                      |
| pidigits                   | 146 ms                                                      | 150 ms: 1.02x slower                                                        |
| bench_thread_pool          | 810 us                                                      | 832 us: 1.03x slower                                                        |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.68 ms: 1.03x slower                                                       |
| generators                 | 19.0 ms                                                     | 19.6 ms: 1.03x slower                                                       |
| html5lib                   | 38.2 ms                                                     | 39.5 ms: 1.03x slower                                                       |
| 2to3                       | 215 ms                                                      | 223 ms: 1.04x slower                                                        |
| sphinx                     | 617 ms                                                      | 640 ms: 1.04x slower                                                        |
| dulwich_log                | 40.1 ms                                                     | 41.6 ms: 1.04x slower                                                       |
| nbody                      | 66.3 ms                                                     | 68.9 ms: 1.04x slower                                                       |
| genshi_xml                 | 33.9 ms                                                     | 35.3 ms: 1.04x slower                                                       |
| json_loads                 | 15.1 us                                                     | 15.7 us: 1.04x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.1 ms: 1.04x slower                                                       |
| asyncio_websockets         | 300 ms                                                      | 314 ms: 1.05x slower                                                        |
| pycparser                  | 695 ms                                                      | 728 ms: 1.05x slower                                                        |
| mako                       | 6.56 ms                                                     | 6.89 ms: 1.05x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 75.7 ms: 1.05x slower                                                       |
| sympy_str                  | 167 ms                                                      | 176 ms: 1.05x slower                                                        |
| sympy_sum                  | 85.2 ms                                                     | 89.9 ms: 1.06x slower                                                       |
| sympy_expand               | 286 ms                                                      | 302 ms: 1.06x slower                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.45 sec: 1.06x slower                                                      |
| coverage                   | 45.3 ms                                                     | 48.1 ms: 1.06x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 56.8 ms: 1.06x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 48.5 ms: 1.06x slower                                                       |
| regex_compile              | 80.7 ms                                                     | 86.0 ms: 1.07x slower                                                       |
| go                         | 84.7 ms                                                     | 90.3 ms: 1.07x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 110 us: 1.07x slower                                                        |
| genshi_text                | 15.2 ms                                                     | 16.3 ms: 1.07x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.65 sec: 1.08x slower                                                      |
| json_dumps                 | 6.19 ms                                                     | 6.68 ms: 1.08x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.3 ms: 1.08x slower                                                       |
| mdp                        | 1.43 sec                                                    | 1.55 sec: 1.08x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 13.6 ms: 1.09x slower                                                       |
| scimark_fft                | 175 ms                                                      | 190 ms: 1.09x slower                                                        |
| comprehensions             | 10.4 us                                                     | 11.3 us: 1.09x slower                                                       |
| sqlglot_optimize           | 32.5 ms                                                     | 35.5 ms: 1.09x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 61.2 ms: 1.09x slower                                                       |
| pyflate                    | 283 ms                                                      | 309 ms: 1.09x slower                                                        |
| logging_simple             | 5.77 us                                                     | 6.33 us: 1.10x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 40.0 ms: 1.10x slower                                                       |
| fannkuch                   | 252 ms                                                      | 276 ms: 1.10x slower                                                        |
| python_startup_no_site     | 16.9 ms                                                     | 18.7 ms: 1.10x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.84 us: 1.11x slower                                                       |
| sqlglot_normalize          | 172 ms                                                      | 191 ms: 1.12x slower                                                        |
| hexiom                     | 3.84 ms                                                     | 4.30 ms: 1.12x slower                                                       |
| chaos                      | 37.9 ms                                                     | 42.5 ms: 1.12x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 64.0 ms: 1.13x slower                                                       |
| pprint_safe_repr           | 485 ms                                                      | 549 ms: 1.13x slower                                                        |
| scimark_monte_carlo        | 40.7 ms                                                     | 46.4 ms: 1.14x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.12 sec: 1.14x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 62.5 ns: 1.15x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 149 us: 1.15x slower                                                        |
| sqlglot_transpile          | 953 us                                                      | 1.10 ms: 1.15x slower                                                       |
| richards                   | 26.3 ms                                                     | 30.3 ms: 1.15x slower                                                       |
| sqlglot_parse              | 764 us                                                      | 888 us: 1.16x slower                                                        |
| richards_super             | 29.8 ms                                                     | 34.7 ms: 1.17x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.24 ms: 1.19x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 90.7 ms: 1.19x slower                                                       |
| many_optionals             | 361 us                                                      | 431 us: 1.19x slower                                                        |
| pickle_pure_python         | 186 us                                                      | 224 us: 1.20x slower                                                        |
| django_template            | 20.3 ms                                                     | 24.9 ms: 1.23x slower                                                       |
| raytrace                   | 153 ms                                                      | 197 ms: 1.29x slower                                                        |
| subparsers                 | 10.9 ms                                                     | 16.0 ms: 1.48x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (5): pylint, create_gc_cycles, k_core, async_generators, gc_traversal
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (8) of results/bm-20250216-3.14.0a5+-359c7dd/bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.005x faster

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown