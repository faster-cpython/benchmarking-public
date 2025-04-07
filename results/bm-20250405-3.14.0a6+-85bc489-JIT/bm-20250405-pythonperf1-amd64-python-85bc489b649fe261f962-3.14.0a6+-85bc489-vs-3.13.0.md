# Results vs. 3.13.0

- fork: python
- ref: 85bc489b649fe261f962
- machine: windows-amd64
- commit hash: 85bc489
- commit date: 2025-04-05
- overall geometric mean: 1.037x faster
- HPT reliability: 72.07%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 222 ms: 1.03x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.70 sec: 1.11x slower                                                      |
| html5lib       | 38.2 ms                                                     | 38.9 ms: 1.02x slower                                                       |
| sphinx         | 617 ms                                                      | 653 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                       | 1.06x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 160 ms: 1.87x faster                                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 207 ms: 1.35x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 204 ms: 1.30x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 393 ms: 1.26x faster                                                        |
| async_tree_io              | 513 ms                                                      | 408 ms: 1.26x faster                                                        |
| async_tree_none            | 219 ms                                                      | 179 ms: 1.22x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 168 ms: 1.19x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 330 ms: 1.15x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 336 ms: 1.14x faster                                                        |
| async_generators           | 223 ms                                                      | 248 ms: 1.11x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 14.2 ms: 1.14x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.21x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 43.3 ms: 1.17x faster                                                       |
| nbody          | 66.3 ms                                                     | 57.0 ms: 1.16x faster                                                       |
| pidigits       | 146 ms                                                      | 148 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.2 ms: 1.67x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.47 ms: 1.15x faster                                                       |
| regex_dna      | 115 ms                                                      | 116 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.19 sec: 1.15x faster                                                      |
| unpickle_pure_python | 130 us                                                      | 119 us: 1.09x faster                                                        |
| xml_etree_generate   | 53.5 ms                                                     | 51.4 ms: 1.04x faster                                                       |
| xml_etree_process    | 36.5 ms                                                     | 36.9 ms: 1.01x slower                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.2 ms: 1.04x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 6.76 ms: 1.09x slower                                                       |
| pickle_pure_python   | 186 us                                                      | 208 us: 1.12x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.00x faster                                                                |

Benchmark hidden because not significant (2): xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.3 ms: 1.08x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 20.5 ms: 1.21x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.67 ms: 1.16x faster                                                       |
| genshi_text     | 15.2 ms                                                     | 15.3 ms: 1.01x slower                                                       |
| genshi_xml      | 33.9 ms                                                     | 35.3 ms: 1.04x slower                                                       |
| django_template | 20.3 ms                                                     | 25.1 ms: 1.24x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.03x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 32.3 ms: 2.33x faster                                                       |
| asyncio_websockets         | 300 ms                                                      | 160 ms: 1.87x faster                                                        |
| mdp                        | 1.43 sec                                                    | 797 ms: 1.80x faster                                                        |
| regex_v8                   | 23.8 ms                                                     | 14.2 ms: 1.67x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 207 ms: 1.35x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 204 ms: 1.30x faster                                                        |
| deepcopy                   | 223 us                                                      | 177 us: 1.26x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 393 ms: 1.26x faster                                                        |
| async_tree_io              | 513 ms                                                      | 408 ms: 1.26x faster                                                        |
| deepcopy_memo              | 23.1 us                                                     | 18.4 us: 1.26x faster                                                       |
| async_tree_none            | 219 ms                                                      | 179 ms: 1.22x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 168 ms: 1.19x faster                                                        |
| float                      | 50.8 ms                                                     | 43.3 ms: 1.17x faster                                                       |
| nbody                      | 66.3 ms                                                     | 57.0 ms: 1.16x faster                                                       |
| mako                       | 6.56 ms                                                     | 5.67 ms: 1.16x faster                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.47 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 330 ms: 1.15x faster                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.19 sec: 1.15x faster                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 336 ms: 1.14x faster                                                        |
| spectral_norm              | 63.4 ms                                                     | 56.5 ms: 1.12x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.32 ms: 1.12x faster                                                       |
| scimark_fft                | 175 ms                                                      | 157 ms: 1.12x faster                                                        |
| telco                      | 4.85 ms                                                     | 4.35 ms: 1.11x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.85 us: 1.09x faster                                                       |
| unpickle_pure_python       | 130 us                                                      | 119 us: 1.09x faster                                                        |
| pyflate                    | 283 ms                                                      | 262 ms: 1.08x faster                                                        |
| bpe_tokeniser              | 2.87 sec                                                    | 2.70 sec: 1.06x faster                                                      |
| fannkuch                   | 252 ms                                                      | 238 ms: 1.06x faster                                                        |
| go                         | 84.7 ms                                                     | 80.3 ms: 1.06x faster                                                       |
| k_core                     | 1.70 sec                                                    | 1.62 sec: 1.05x faster                                                      |
| json                       | 3.30 ms                                                     | 3.15 ms: 1.05x faster                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 51.4 ms: 1.04x faster                                                       |
| scimark_sor                | 76.2 ms                                                     | 74.2 ms: 1.03x faster                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.55 us: 1.02x faster                                                       |
| pprint_pformat             | 977 ms                                                      | 963 ms: 1.01x faster                                                        |
| scimark_monte_carlo        | 40.7 ms                                                     | 40.5 ms: 1.01x faster                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 45.8 ms: 1.00x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 15.3 ms: 1.01x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 55.0 ns: 1.01x slower                                                       |
| pidigits                   | 146 ms                                                      | 148 ms: 1.01x slower                                                        |
| regex_dna                  | 115 ms                                                      | 116 ms: 1.01x slower                                                        |
| xml_etree_process          | 36.5 ms                                                     | 36.9 ms: 1.01x slower                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.24 ms: 1.01x slower                                                       |
| generators                 | 19.0 ms                                                     | 19.2 ms: 1.01x slower                                                       |
| html5lib                   | 38.2 ms                                                     | 38.9 ms: 1.02x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 58.3 ms: 1.03x slower                                                       |
| chaos                      | 37.9 ms                                                     | 39.0 ms: 1.03x slower                                                       |
| 2to3                       | 215 ms                                                      | 222 ms: 1.03x slower                                                        |
| meteor_contest             | 72.0 ms                                                     | 74.5 ms: 1.04x slower                                                       |
| genshi_xml                 | 33.9 ms                                                     | 35.3 ms: 1.04x slower                                                       |
| richards                   | 26.3 ms                                                     | 27.4 ms: 1.04x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.2 ms: 1.04x slower                                                       |
| sympy_str                  | 167 ms                                                      | 175 ms: 1.05x slower                                                        |
| bench_mp_pool              | 84.2 ms                                                     | 88.3 ms: 1.05x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 855 us: 1.06x slower                                                        |
| sympy_sum                  | 85.2 ms                                                     | 89.9 ms: 1.06x slower                                                       |
| sphinx                     | 617 ms                                                      | 653 ms: 1.06x slower                                                        |
| richards_super             | 29.8 ms                                                     | 31.5 ms: 1.06x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.1 ms: 1.06x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 42.7 ms: 1.07x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.09 ms: 1.07x slower                                                       |
| sympy_expand               | 286 ms                                                      | 305 ms: 1.07x slower                                                        |
| hexiom                     | 3.84 ms                                                     | 4.12 ms: 1.07x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.21 us: 1.07x slower                                                       |
| python_startup             | 24.4 ms                                                     | 26.3 ms: 1.08x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 60.8 ms: 1.08x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 112 us: 1.08x slower                                                        |
| logging_format             | 6.18 us                                                     | 6.74 us: 1.09x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 6.76 ms: 1.09x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.70 sec: 1.11x slower                                                      |
| raytrace                   | 153 ms                                                      | 171 ms: 1.11x slower                                                        |
| async_generators           | 223 ms                                                      | 248 ms: 1.11x slower                                                        |
| pickle_pure_python         | 186 us                                                      | 208 us: 1.12x slower                                                        |
| coverage                   | 45.3 ms                                                     | 51.1 ms: 1.13x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.2 ms: 1.14x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.16 ms: 1.14x slower                                                       |
| comprehensions             | 10.4 us                                                     | 12.0 us: 1.16x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 20.5 ms: 1.21x slower                                                       |
| django_template            | 20.3 ms                                                     | 25.1 ms: 1.24x slower                                                       |
| many_optionals             | 361 us                                                      | 458 us: 1.27x slower                                                        |
| subparsers                 | 10.9 ms                                                     | 16.1 ms: 1.48x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (8): pylint, pprint_safe_repr, regex_compile, xml_etree_parse, shortest_path, json_loads, connected_components, pycparser
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250405-3.14.0a6+-85bc489-JIT/bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.037x faster

# HPT report

- Reliability score: 72.07% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown