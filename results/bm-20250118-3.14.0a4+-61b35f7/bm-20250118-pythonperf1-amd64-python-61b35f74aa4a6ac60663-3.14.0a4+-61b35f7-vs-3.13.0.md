# Results vs. 3.13.0

- fork: python
- ref: 61b35f74aa4a6ac60663
- machine: windows-amd64
- commit hash: 61b35f7
- commit date: 2025-01-18
- overall geometric mean: 1.054x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 237 ms: 1.10x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.70 sec: 1.11x slower                                                      |
| html5lib       | 38.2 ms                                                     | 41.1 ms: 1.08x slower                                                       |
| sphinx         | 617 ms                                                      | 668 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                       | 1.09x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 220 ms: 1.27x faster                                                        |
| async_tree_io              | 513 ms                                                      | 432 ms: 1.19x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 421 ms: 1.18x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 236 ms: 1.12x faster                                                        |
| async_tree_none            | 219 ms                                                      | 196 ms: 1.12x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 181 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 351 ms: 1.09x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 356 ms: 1.07x faster                                                        |
| async_generators           | 223 ms                                                      | 237 ms: 1.07x slower                                                        |
| asyncio_websockets         | 300 ms                                                      | 321 ms: 1.07x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 16.2 ms: 1.30x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.06x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 146 ms                                                      | 147 ms: 1.00x slower                                                        |
| float          | 50.8 ms                                                     | 53.1 ms: 1.04x slower                                                       |
| nbody          | 66.3 ms                                                     | 80.9 ms: 1.22x slower                                                       |
| Geometric mean | (ref)                                                       | 1.09x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 16.1 ms: 1.48x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.53 ms: 1.11x faster                                                       |
| regex_dna      | 115 ms                                                      | 117 ms: 1.02x slower                                                        |
| regex_compile  | 80.7 ms                                                     | 93.6 ms: 1.16x slower                                                       |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 88.8 ms: 1.04x faster                                                       |
| json_loads           | 15.1 us                                                     | 14.9 us: 1.02x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.49 sec: 1.09x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 66.2 ms: 1.09x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 7.00 ms: 1.13x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 63.3 ms: 1.18x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 45.3 ms: 1.24x slower                                                       |
| unpickle_pure_python | 130 us                                                      | 164 us: 1.26x slower                                                        |
| pickle_pure_python   | 186 us                                                      | 240 us: 1.29x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.13x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 24.2 ms: 1.01x faster                                                       |
| python_startup_no_site | 16.9 ms                                                     | 18.0 ms: 1.06x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 36.5 ms: 1.08x slower                                                       |
| mako            | 6.56 ms                                                     | 7.26 ms: 1.11x slower                                                       |
| genshi_text     | 15.2 ms                                                     | 17.0 ms: 1.12x slower                                                       |
| django_template | 20.3 ms                                                     | 27.3 ms: 1.34x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.16x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 538 us: 15.75x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 16.1 ms: 1.48x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 220 ms: 1.27x faster                                                        |
| async_tree_io              | 513 ms                                                      | 432 ms: 1.19x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 421 ms: 1.18x faster                                                        |
| deepcopy                   | 223 us                                                      | 196 us: 1.14x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 236 ms: 1.12x faster                                                        |
| async_tree_none            | 219 ms                                                      | 196 ms: 1.12x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.53 ms: 1.11x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 181 ms: 1.11x faster                                                        |
| json                       | 3.30 ms                                                     | 3.01 ms: 1.10x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 351 ms: 1.09x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 356 ms: 1.07x faster                                                        |
| xml_etree_parse            | 92.2 ms                                                     | 88.8 ms: 1.04x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.95 us: 1.04x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 22.5 us: 1.03x faster                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.20 ms: 1.02x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.9 us: 1.02x faster                                                       |
| python_startup             | 24.4 ms                                                     | 24.2 ms: 1.01x faster                                                       |
| pidigits                   | 146 ms                                                      | 147 ms: 1.00x slower                                                        |
| shortest_path              | 355 ms                                                      | 357 ms: 1.01x slower                                                        |
| spectral_norm              | 63.4 ms                                                     | 64.1 ms: 1.01x slower                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.61 us: 1.01x slower                                                       |
| regex_dna                  | 115 ms                                                      | 117 ms: 1.02x slower                                                        |
| connected_components       | 320 ms                                                      | 326 ms: 1.02x slower                                                        |
| k_core                     | 1.70 sec                                                    | 1.73 sec: 1.02x slower                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.66 ms: 1.02x slower                                                       |
| pathlib                    | 75.3 ms                                                     | 78.1 ms: 1.04x slower                                                       |
| float                      | 50.8 ms                                                     | 53.1 ms: 1.04x slower                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 88.2 ms: 1.05x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 852 us: 1.05x slower                                                        |
| python_startup_no_site     | 16.9 ms                                                     | 18.0 ms: 1.06x slower                                                       |
| async_generators           | 223 ms                                                      | 237 ms: 1.07x slower                                                        |
| asyncio_websockets         | 300 ms                                                      | 321 ms: 1.07x slower                                                        |
| sympy_sum                  | 85.2 ms                                                     | 91.2 ms: 1.07x slower                                                       |
| genshi_xml                 | 33.9 ms                                                     | 36.5 ms: 1.08x slower                                                       |
| html5lib                   | 38.2 ms                                                     | 41.1 ms: 1.08x slower                                                       |
| sympy_expand               | 286 ms                                                      | 309 ms: 1.08x slower                                                        |
| sphinx                     | 617 ms                                                      | 668 ms: 1.08x slower                                                        |
| dulwich_log                | 40.1 ms                                                     | 43.4 ms: 1.08x slower                                                       |
| sympy_str                  | 167 ms                                                      | 181 ms: 1.08x slower                                                        |
| meteor_contest             | 72.0 ms                                                     | 77.9 ms: 1.08x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 3.12 sec: 1.08x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.49 sec: 1.09x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 66.2 ms: 1.09x slower                                                       |
| coverage                   | 45.3 ms                                                     | 49.7 ms: 1.10x slower                                                       |
| pycparser                  | 695 ms                                                      | 764 ms: 1.10x slower                                                        |
| 2to3                       | 215 ms                                                      | 237 ms: 1.10x slower                                                        |
| mako                       | 6.56 ms                                                     | 7.26 ms: 1.11x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 50.7 ms: 1.11x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.70 sec: 1.11x slower                                                      |
| genshi_text                | 15.2 ms                                                     | 17.0 ms: 1.12x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.8 ms: 1.12x slower                                                       |
| scimark_fft                | 175 ms                                                      | 197 ms: 1.12x slower                                                        |
| json_dumps                 | 6.19 ms                                                     | 7.00 ms: 1.13x slower                                                       |
| go                         | 84.7 ms                                                     | 96.0 ms: 1.13x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 117 us: 1.13x slower                                                        |
| logging_simple             | 5.77 us                                                     | 6.61 us: 1.14x slower                                                       |
| fannkuch                   | 252 ms                                                      | 288 ms: 1.14x slower                                                        |
| pyflate                    | 283 ms                                                      | 326 ms: 1.15x slower                                                        |
| logging_format             | 6.18 us                                                     | 7.12 us: 1.15x slower                                                       |
| mdp                        | 1.43 sec                                                    | 1.65 sec: 1.15x slower                                                      |
| sqlglot_optimize           | 32.5 ms                                                     | 37.6 ms: 1.16x slower                                                       |
| regex_compile              | 80.7 ms                                                     | 93.6 ms: 1.16x slower                                                       |
| chaos                      | 37.9 ms                                                     | 44.1 ms: 1.16x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.15 sec: 1.18x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 573 ms: 1.18x slower                                                        |
| xml_etree_generate         | 53.5 ms                                                     | 63.3 ms: 1.18x slower                                                       |
| sqlglot_normalize          | 172 ms                                                      | 204 ms: 1.19x slower                                                        |
| scimark_lu                 | 56.7 ms                                                     | 69.0 ms: 1.22x slower                                                       |
| sqlglot_transpile          | 953 us                                                      | 1.16 ms: 1.22x slower                                                       |
| nbody                      | 66.3 ms                                                     | 80.9 ms: 1.22x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 68.7 ms: 1.22x slower                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 49.9 ms: 1.23x slower                                                       |
| generators                 | 19.0 ms                                                     | 23.5 ms: 1.24x slower                                                       |
| sqlglot_parse              | 764 us                                                      | 946 us: 1.24x slower                                                        |
| xml_etree_process          | 36.5 ms                                                     | 45.3 ms: 1.24x slower                                                       |
| many_optionals             | 361 us                                                      | 452 us: 1.25x slower                                                        |
| unpickle_pure_python       | 130 us                                                      | 164 us: 1.26x slower                                                        |
| comprehensions             | 10.4 us                                                     | 13.1 us: 1.27x slower                                                       |
| richards                   | 26.3 ms                                                     | 33.3 ms: 1.27x slower                                                       |
| richards_super             | 29.8 ms                                                     | 37.8 ms: 1.27x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.92 ms: 1.28x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 240 us: 1.29x slower                                                        |
| scimark_sor                | 76.2 ms                                                     | 98.3 ms: 1.29x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 16.2 ms: 1.30x slower                                                       |
| django_template            | 20.3 ms                                                     | 27.3 ms: 1.34x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.58 ms: 1.36x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 75.3 ns: 1.38x slower                                                       |
| raytrace                   | 153 ms                                                      | 215 ms: 1.40x slower                                                        |
| subparsers                 | 10.9 ms                                                     | 16.7 ms: 1.54x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.06x slower                                                                |

Benchmark hidden because not significant (3): pylint, telco, gc_traversal
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (8) of results/bm-20250118-3.14.0a4+-61b35f7/bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.054x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown