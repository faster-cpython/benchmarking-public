# Results vs. 3.13.0

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: windows-amd64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.010x faster
- HPT reliability: 99.76%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 227 ms: 1.05x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.65 sec: 1.07x slower                                                      |
| html5lib       | 38.2 ms                                                     | 39.0 ms: 1.02x slower                                                       |
| sphinx         | 617 ms                                                      | 643 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                       | 1.05x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 218 ms: 1.29x faster                                                        |
| async_tree_io              | 513 ms                                                      | 416 ms: 1.23x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 224 ms: 1.18x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 428 ms: 1.16x faster                                                        |
| async_tree_none            | 219 ms                                                      | 190 ms: 1.15x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 339 ms: 1.12x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 179 ms: 1.12x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 345 ms: 1.11x faster                                                        |
| async_generators           | 223 ms                                                      | 222 ms: 1.00x faster                                                        |
| asyncio_websockets         | 300 ms                                                      | 312 ms: 1.04x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.3 ms: 1.06x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.11x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 45.1 ms: 1.13x faster                                                       |
| pidigits       | 146 ms                                                      | 151 ms: 1.03x slower                                                        |
| nbody          | 66.3 ms                                                     | 69.1 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.3 ms: 1.66x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.40 ms: 1.21x faster                                                       |
| regex_dna      | 115 ms                                                      | 112 ms: 1.03x faster                                                        |
| regex_compile  | 80.7 ms                                                     | 84.1 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.19x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 90.4 ms: 1.02x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.35 sec: 1.01x faster                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 62.9 ms: 1.04x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 56.5 ms: 1.06x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 6.67 ms: 1.08x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 39.6 ms: 1.08x slower                                                       |
| unpickle_pure_python | 130 us                                                      | 142 us: 1.09x slower                                                        |
| pickle_pure_python   | 186 us                                                      | 217 us: 1.17x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.05x slower                                                                |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.2 ms: 1.07x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 19.6 ms: 1.16x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.69 ms: 1.02x slower                                                       |
| genshi_text     | 15.2 ms                                                     | 15.8 ms: 1.04x slower                                                       |
| django_template | 20.3 ms                                                     | 25.9 ms: 1.28x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.08x slower                                                                |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 515 us: 16.43x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.3 ms: 1.66x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 218 ms: 1.29x faster                                                        |
| async_tree_io              | 513 ms                                                      | 416 ms: 1.23x faster                                                        |
| deepcopy                   | 223 us                                                      | 183 us: 1.22x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.40 ms: 1.21x faster                                                       |
| pathlib                    | 75.3 ms                                                     | 62.4 ms: 1.21x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 19.4 us: 1.19x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 224 ms: 1.18x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 428 ms: 1.16x faster                                                        |
| async_tree_none            | 219 ms                                                      | 190 ms: 1.15x faster                                                        |
| float                      | 50.8 ms                                                     | 45.1 ms: 1.13x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 339 ms: 1.12x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 179 ms: 1.12x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 345 ms: 1.11x faster                                                        |
| json                       | 3.30 ms                                                     | 3.02 ms: 1.09x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 58.2 ms: 1.09x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.90 us: 1.06x faster                                                       |
| regex_dna                  | 115 ms                                                      | 112 ms: 1.03x faster                                                        |
| xml_etree_parse            | 92.2 ms                                                     | 90.4 ms: 1.02x faster                                                       |
| shortest_path              | 355 ms                                                      | 349 ms: 1.02x faster                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.35 sec: 1.01x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.79 ms: 1.01x faster                                                       |
| async_generators           | 223 ms                                                      | 222 ms: 1.00x faster                                                        |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.62 ms: 1.01x slower                                                       |
| go                         | 84.7 ms                                                     | 85.4 ms: 1.01x slower                                                       |
| k_core                     | 1.70 sec                                                    | 1.72 sec: 1.01x slower                                                      |
| mako                       | 6.56 ms                                                     | 6.69 ms: 1.02x slower                                                       |
| html5lib                   | 38.2 ms                                                     | 39.0 ms: 1.02x slower                                                       |
| mdp                        | 1.43 sec                                                    | 1.46 sec: 1.02x slower                                                      |
| typing_runtime_protocols   | 103 us                                                      | 106 us: 1.03x slower                                                        |
| crypto_pyaes               | 45.6 ms                                                     | 46.9 ms: 1.03x slower                                                       |
| pidigits                   | 146 ms                                                      | 151 ms: 1.03x slower                                                        |
| genshi_text                | 15.2 ms                                                     | 15.8 ms: 1.04x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.04 ms: 1.04x slower                                                       |
| asyncio_websockets         | 300 ms                                                      | 312 ms: 1.04x slower                                                        |
| xml_etree_iterparse        | 60.5 ms                                                     | 62.9 ms: 1.04x slower                                                       |
| fannkuch                   | 252 ms                                                      | 262 ms: 1.04x slower                                                        |
| sympy_str                  | 167 ms                                                      | 174 ms: 1.04x slower                                                        |
| regex_compile              | 80.7 ms                                                     | 84.1 ms: 1.04x slower                                                       |
| sphinx                     | 617 ms                                                      | 643 ms: 1.04x slower                                                        |
| pycparser                  | 695 ms                                                      | 725 ms: 1.04x slower                                                        |
| nbody                      | 66.3 ms                                                     | 69.1 ms: 1.04x slower                                                       |
| generators                 | 19.0 ms                                                     | 19.8 ms: 1.04x slower                                                       |
| sympy_expand               | 286 ms                                                      | 299 ms: 1.05x slower                                                        |
| logging_silent             | 54.6 ns                                                     | 57.2 ns: 1.05x slower                                                       |
| scimark_fft                | 175 ms                                                      | 183 ms: 1.05x slower                                                        |
| sympy_sum                  | 85.2 ms                                                     | 89.4 ms: 1.05x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 42.2 ms: 1.05x slower                                                       |
| 2to3                       | 215 ms                                                      | 227 ms: 1.05x slower                                                        |
| meteor_contest             | 72.0 ms                                                     | 76.0 ms: 1.06x slower                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.67 us: 1.06x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 56.5 ms: 1.06x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 858 us: 1.06x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.3 ms: 1.06x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.1 ms: 1.07x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 60.7 ms: 1.07x slower                                                       |
| coverage                   | 45.3 ms                                                     | 48.5 ms: 1.07x slower                                                       |
| pyflate                    | 283 ms                                                      | 303 ms: 1.07x slower                                                        |
| python_startup             | 24.4 ms                                                     | 26.2 ms: 1.07x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.65 sec: 1.07x slower                                                      |
| bench_mp_pool              | 84.2 ms                                                     | 90.8 ms: 1.08x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 6.67 ms: 1.08x slower                                                       |
| sqlglot_optimize           | 32.5 ms                                                     | 35.2 ms: 1.08x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 39.6 ms: 1.08x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.06 sec: 1.09x slower                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 44.3 ms: 1.09x slower                                                       |
| pprint_safe_repr           | 485 ms                                                      | 527 ms: 1.09x slower                                                        |
| unpickle_pure_python       | 130 us                                                      | 142 us: 1.09x slower                                                        |
| richards                   | 26.3 ms                                                     | 28.7 ms: 1.09x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.32 us: 1.09x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.77 us: 1.10x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.23 ms: 1.10x slower                                                       |
| sqlglot_normalize          | 172 ms                                                      | 189 ms: 1.10x slower                                                        |
| richards_super             | 29.8 ms                                                     | 32.9 ms: 1.10x slower                                                       |
| chaos                      | 37.9 ms                                                     | 41.9 ms: 1.11x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 62.6 ms: 1.11x slower                                                       |
| comprehensions             | 10.4 us                                                     | 11.6 us: 1.12x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 85.4 ms: 1.12x slower                                                       |
| sqlglot_transpile          | 953 us                                                      | 1.07 ms: 1.13x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.15 ms: 1.14x slower                                                       |
| sqlglot_parse              | 764 us                                                      | 875 us: 1.14x slower                                                        |
| python_startup_no_site     | 16.9 ms                                                     | 19.6 ms: 1.16x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 217 us: 1.17x slower                                                        |
| many_optionals             | 361 us                                                      | 437 us: 1.21x slower                                                        |
| django_template            | 20.3 ms                                                     | 25.9 ms: 1.28x slower                                                       |
| raytrace                   | 153 ms                                                      | 198 ms: 1.29x slower                                                        |
| subparsers                 | 10.9 ms                                                     | 16.4 ms: 1.52x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (6): pylint, connected_components, create_gc_cycles, bpe_tokeniser, json_loads, genshi_xml
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (8) of results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.010x faster

# HPT report

- Reliability score: 99.76% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown