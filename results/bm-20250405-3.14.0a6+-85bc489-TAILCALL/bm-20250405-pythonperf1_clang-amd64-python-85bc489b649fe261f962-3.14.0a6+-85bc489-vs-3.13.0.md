# Results vs. 3.13.0

- fork: python
- ref: 85bc489b649fe261f962
- machine: windows-amd64
- commit hash: 85bc489
- commit date: 2025-04-05
- overall geometric mean: 1.201x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 202 ms: 1.06x faster                                                        |
| html5lib       | 38.2 ms                                                     | 33.3 ms: 1.15x faster                                                       |
| sphinx         | 617 ms                                                      | 589 ms: 1.05x faster                                                        |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 165 ms: 1.82x faster                                                        |
| async_tree_io              | 513 ms                                                      | 339 ms: 1.51x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 183 ms: 1.45x faster                                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 194 ms: 1.45x faster                                                        |
| async_tree_none            | 219 ms                                                      | 153 ms: 1.43x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 347 ms: 1.43x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 147 ms: 1.36x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 308 ms: 1.24x faster                                                        |
| async_generators           | 223 ms                                                      | 183 ms: 1.22x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 315 ms: 1.22x faster                                                        |
| coroutines                 | 12.5 ms                                                     | 10.8 ms: 1.15x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.38x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 35.8 ms: 1.42x faster                                                       |
| nbody          | 66.3 ms                                                     | 51.9 ms: 1.28x faster                                                       |
| pidigits       | 146 ms                                                      | 145 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                       | 1.22x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.2 ms: 1.80x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 67.6 ms: 1.19x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.59 ms: 1.06x faster                                                       |
| regex_dna      | 115 ms                                                      | 121 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                       | 1.22x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.01 sec: 1.36x faster                                                      |
| unpickle_pure_python | 130 us                                                      | 105 us: 1.23x faster                                                        |
| xml_etree_generate   | 53.5 ms                                                     | 46.9 ms: 1.14x faster                                                       |
| pickle_pure_python   | 186 us                                                      | 164 us: 1.13x faster                                                        |
| xml_etree_process    | 36.5 ms                                                     | 32.4 ms: 1.13x faster                                                       |
| json_loads           | 15.1 us                                                     | 13.6 us: 1.11x faster                                                       |
| json_dumps           | 6.19 ms                                                     | 5.59 ms: 1.11x faster                                                       |
| xml_etree_parse      | 92.2 ms                                                     | 89.5 ms: 1.03x faster                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 61.1 ms: 1.01x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.13x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.6 ms: 1.09x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 20.9 ms: 1.24x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.16x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 15.2 ms                                                     | 11.3 ms: 1.34x faster                                                       |
| genshi_xml      | 33.9 ms                                                     | 27.3 ms: 1.24x faster                                                       |
| mako            | 6.56 ms                                                     | 5.72 ms: 1.15x faster                                                       |
| django_template | 20.3 ms                                                     | 19.4 ms: 1.05x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.19x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 30.7 ms: 2.45x faster                                                       |
| mdp                        | 1.43 sec                                                    | 661 ms: 2.17x faster                                                        |
| asyncio_websockets         | 300 ms                                                      | 165 ms: 1.82x faster                                                        |
| regex_v8                   | 23.8 ms                                                     | 13.2 ms: 1.80x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 13.0 us: 1.77x faster                                                       |
| deepcopy                   | 223 us                                                      | 133 us: 1.68x faster                                                        |
| scimark_sor                | 76.2 ms                                                     | 47.1 ms: 1.62x faster                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 26.9 ms: 1.52x faster                                                       |
| async_tree_io              | 513 ms                                                      | 339 ms: 1.51x faster                                                        |
| go                         | 84.7 ms                                                     | 57.9 ms: 1.46x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 183 ms: 1.45x faster                                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 194 ms: 1.45x faster                                                        |
| deepcopy_reduce            | 2.02 us                                                     | 1.41 us: 1.44x faster                                                       |
| async_tree_none            | 219 ms                                                      | 153 ms: 1.43x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 347 ms: 1.43x faster                                                        |
| float                      | 50.8 ms                                                     | 35.8 ms: 1.42x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 46.5 ms: 1.36x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 147 ms: 1.36x faster                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.01 sec: 1.36x faster                                                      |
| genshi_text                | 15.2 ms                                                     | 11.3 ms: 1.34x faster                                                       |
| hexiom                     | 3.84 ms                                                     | 2.88 ms: 1.33x faster                                                       |
| fannkuch                   | 252 ms                                                      | 190 ms: 1.32x faster                                                        |
| logging_silent             | 54.6 ns                                                     | 41.9 ns: 1.30x faster                                                       |
| pprint_safe_repr           | 485 ms                                                      | 379 ms: 1.28x faster                                                        |
| nbody                      | 66.3 ms                                                     | 51.9 ms: 1.28x faster                                                       |
| richards                   | 26.3 ms                                                     | 20.7 ms: 1.27x faster                                                       |
| scimark_fft                | 175 ms                                                      | 138 ms: 1.27x faster                                                        |
| scimark_lu                 | 56.7 ms                                                     | 45.2 ms: 1.25x faster                                                       |
| deltablue                  | 1.89 ms                                                     | 1.51 ms: 1.25x faster                                                       |
| generators                 | 19.0 ms                                                     | 15.2 ms: 1.25x faster                                                       |
| richards_super             | 29.8 ms                                                     | 23.9 ms: 1.25x faster                                                       |
| pprint_pformat             | 977 ms                                                      | 785 ms: 1.24x faster                                                        |
| genshi_xml                 | 33.9 ms                                                     | 27.3 ms: 1.24x faster                                                       |
| comprehensions             | 10.4 us                                                     | 8.35 us: 1.24x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 308 ms: 1.24x faster                                                        |
| unpickle_pure_python       | 130 us                                                      | 105 us: 1.23x faster                                                        |
| typing_runtime_protocols   | 103 us                                                      | 84.1 us: 1.23x faster                                                       |
| async_generators           | 223 ms                                                      | 183 ms: 1.22x faster                                                        |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.14 ms: 1.22x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 315 ms: 1.22x faster                                                        |
| pyflate                    | 283 ms                                                      | 233 ms: 1.21x faster                                                        |
| telco                      | 4.85 ms                                                     | 4.00 ms: 1.21x faster                                                       |
| chaos                      | 37.9 ms                                                     | 31.2 ms: 1.21x faster                                                       |
| regex_compile              | 80.7 ms                                                     | 67.6 ms: 1.19x faster                                                       |
| nqueens                    | 56.1 ms                                                     | 47.8 ms: 1.17x faster                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 39.2 ms: 1.16x faster                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.47 sec: 1.16x faster                                                      |
| coroutines                 | 12.5 ms                                                     | 10.8 ms: 1.15x faster                                                       |
| mako                       | 6.56 ms                                                     | 5.72 ms: 1.15x faster                                                       |
| html5lib                   | 38.2 ms                                                     | 33.3 ms: 1.15x faster                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 46.9 ms: 1.14x faster                                                       |
| sympy_str                  | 167 ms                                                      | 147 ms: 1.13x faster                                                        |
| pickle_pure_python         | 186 us                                                      | 164 us: 1.13x faster                                                        |
| sympy_expand               | 286 ms                                                      | 252 ms: 1.13x faster                                                        |
| xml_etree_process          | 36.5 ms                                                     | 32.4 ms: 1.13x faster                                                       |
| pylint                     | 205 ms                                                      | 183 ms: 1.12x faster                                                        |
| coverage                   | 45.3 ms                                                     | 40.5 ms: 1.12x faster                                                       |
| sympy_integrate            | 12.3 ms                                                     | 11.1 ms: 1.11x faster                                                       |
| json_loads                 | 15.1 us                                                     | 13.6 us: 1.11x faster                                                       |
| json_dumps                 | 6.19 ms                                                     | 5.59 ms: 1.11x faster                                                       |
| sympy_sum                  | 85.2 ms                                                     | 77.9 ms: 1.09x faster                                                       |
| meteor_contest             | 72.0 ms                                                     | 66.2 ms: 1.09x faster                                                       |
| pycparser                  | 695 ms                                                      | 641 ms: 1.08x faster                                                        |
| logging_format             | 6.18 us                                                     | 5.73 us: 1.08x faster                                                       |
| raytrace                   | 153 ms                                                      | 143 ms: 1.07x faster                                                        |
| logging_simple             | 5.77 us                                                     | 5.38 us: 1.07x faster                                                       |
| json                       | 3.30 ms                                                     | 3.08 ms: 1.07x faster                                                       |
| dulwich_log                | 40.1 ms                                                     | 37.6 ms: 1.07x faster                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.59 ms: 1.06x faster                                                       |
| 2to3                       | 215 ms                                                      | 202 ms: 1.06x faster                                                        |
| k_core                     | 1.70 sec                                                    | 1.60 sec: 1.06x faster                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.50 us: 1.06x faster                                                       |
| django_template            | 20.3 ms                                                     | 19.4 ms: 1.05x faster                                                       |
| sphinx                     | 617 ms                                                      | 589 ms: 1.05x faster                                                        |
| xml_etree_parse            | 92.2 ms                                                     | 89.5 ms: 1.03x faster                                                       |
| shortest_path              | 355 ms                                                      | 345 ms: 1.03x faster                                                        |
| pidigits                   | 146 ms                                                      | 145 ms: 1.01x faster                                                        |
| xml_etree_iterparse        | 60.5 ms                                                     | 61.1 ms: 1.01x slower                                                       |
| connected_components       | 320 ms                                                      | 325 ms: 1.02x slower                                                        |
| bench_mp_pool              | 84.2 ms                                                     | 87.9 ms: 1.04x slower                                                       |
| regex_dna                  | 115 ms                                                      | 121 ms: 1.05x slower                                                        |
| many_optionals             | 361 us                                                      | 392 us: 1.08x slower                                                        |
| python_startup             | 24.4 ms                                                     | 26.6 ms: 1.09x slower                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.38 ms: 1.13x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 20.9 ms: 1.24x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 14.4 ms: 1.33x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.81 ms: 1.43x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.20x faster                                                                |

Benchmark hidden because not significant (2): docutils, bench_thread_pool
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250405-3.14.0a6+-85bc489-CLANG/bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.201x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown