# Results vs. 3.13.0

- fork: python
- ref: c9932a9ec8a3077933a8
- machine: windows-amd64
- commit hash: c9932a9
- commit date: 2025-03-01
- overall geometric mean: 1.018x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 232 ms: 1.08x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.75 sec: 1.15x slower                                                      |
| html5lib       | 38.2 ms                                                     | 40.0 ms: 1.05x slower                                                       |
| sphinx         | 617 ms                                                      | 691 ms: 1.12x slower                                                        |
| Geometric mean | (ref)                                                       | 1.10x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 208 ms: 1.35x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 209 ms: 1.27x faster                                                        |
| async_tree_io              | 513 ms                                                      | 406 ms: 1.26x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 397 ms: 1.25x faster                                                        |
| async_tree_none            | 219 ms                                                      | 178 ms: 1.23x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 172 ms: 1.16x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 361 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 366 ms: 1.05x faster                                                        |
| async_generators           | 223 ms                                                      | 225 ms: 1.01x slower                                                        |
| asyncio_websockets         | 300 ms                                                      | 310 ms: 1.03x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.1 ms: 1.05x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.13x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 46.3 ms: 1.10x faster                                                       |
| nbody          | 66.3 ms                                                     | 67.7 ms: 1.02x slower                                                       |
| pidigits       | 146 ms                                                      | 155 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 17.1 ms: 1.40x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 86.9 ms: 1.08x slower                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.87 ms: 1.10x slower                                                       |
| regex_dna      | 115 ms                                                      | 129 ms: 1.12x slower                                                        |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.35 sec: 1.02x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 104 ms: 1.13x slower                                                        |
| xml_etree_iterparse  | 60.5 ms                                                     | 70.0 ms: 1.16x slower                                                       |
| unpickle_pure_python | 130 us                                                      | 151 us: 1.16x slower                                                        |
| pickle_pure_python   | 186 us                                                      | 220 us: 1.18x slower                                                        |
| xml_etree_generate   | 53.5 ms                                                     | 65.8 ms: 1.23x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 46.1 ms: 1.26x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 7.88 ms: 1.27x slower                                                       |
| json_loads           | 15.1 us                                                     | 20.5 us: 1.35x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.19x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 27.4 ms: 1.13x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 20.4 ms: 1.21x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.17x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 32.5 ms: 1.04x faster                                                       |
| genshi_text     | 15.2 ms                                                     | 15.0 ms: 1.02x faster                                                       |
| django_template | 20.3 ms                                                     | 25.1 ms: 1.24x slower                                                       |
| mako            | 6.56 ms                                                     | 8.33 ms: 1.27x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.10x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 552 us: 15.35x faster                                                       |
| pathlib                    | 75.3 ms                                                     | 31.6 ms: 2.38x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 17.1 ms: 1.40x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 208 ms: 1.35x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 209 ms: 1.27x faster                                                        |
| async_tree_io              | 513 ms                                                      | 406 ms: 1.26x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 397 ms: 1.25x faster                                                        |
| async_tree_none            | 219 ms                                                      | 178 ms: 1.23x faster                                                        |
| deepcopy                   | 223 us                                                      | 182 us: 1.23x faster                                                        |
| deepcopy_memo              | 23.1 us                                                     | 19.3 us: 1.20x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 172 ms: 1.16x faster                                                        |
| generators                 | 19.0 ms                                                     | 17.3 ms: 1.10x faster                                                       |
| float                      | 50.8 ms                                                     | 46.3 ms: 1.10x faster                                                       |
| go                         | 84.7 ms                                                     | 77.2 ms: 1.10x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 361 ms: 1.05x faster                                                        |
| deepcopy_reduce            | 2.02 us                                                     | 1.93 us: 1.05x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 366 ms: 1.05x faster                                                        |
| genshi_xml                 | 33.9 ms                                                     | 32.5 ms: 1.04x faster                                                       |
| scimark_sor                | 76.2 ms                                                     | 74.6 ms: 1.02x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.35 sec: 1.02x faster                                                      |
| genshi_text                | 15.2 ms                                                     | 15.0 ms: 1.02x faster                                                       |
| shortest_path              | 355 ms                                                      | 354 ms: 1.00x faster                                                        |
| async_generators           | 223 ms                                                      | 225 ms: 1.01x slower                                                        |
| sqlite_synth               | 1.59 us                                                     | 1.61 us: 1.02x slower                                                       |
| connected_components       | 320 ms                                                      | 326 ms: 1.02x slower                                                        |
| nbody                      | 66.3 ms                                                     | 67.7 ms: 1.02x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 74.1 ms: 1.03x slower                                                       |
| pycparser                  | 695 ms                                                      | 716 ms: 1.03x slower                                                        |
| asyncio_websockets         | 300 ms                                                      | 310 ms: 1.03x slower                                                        |
| scimark_monte_carlo        | 40.7 ms                                                     | 42.6 ms: 1.04x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 1.98 ms: 1.04x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.1 ms: 1.05x slower                                                       |
| html5lib                   | 38.2 ms                                                     | 40.0 ms: 1.05x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 42.2 ms: 1.05x slower                                                       |
| pidigits                   | 146 ms                                                      | 155 ms: 1.06x slower                                                        |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.76 ms: 1.06x slower                                                       |
| sympy_str                  | 167 ms                                                      | 178 ms: 1.06x slower                                                        |
| sympy_expand               | 286 ms                                                      | 304 ms: 1.06x slower                                                        |
| pyflate                    | 283 ms                                                      | 302 ms: 1.07x slower                                                        |
| sympy_sum                  | 85.2 ms                                                     | 91.6 ms: 1.08x slower                                                       |
| regex_compile              | 80.7 ms                                                     | 86.9 ms: 1.08x slower                                                       |
| telco                      | 4.85 ms                                                     | 5.23 ms: 1.08x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.15 ms: 1.08x slower                                                       |
| 2to3                       | 215 ms                                                      | 232 ms: 1.08x slower                                                        |
| typing_runtime_protocols   | 103 us                                                      | 112 us: 1.08x slower                                                        |
| bench_mp_pool              | 84.2 ms                                                     | 91.5 ms: 1.09x slower                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.33 ms: 1.09x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.4 ms: 1.09x slower                                                       |
| sqlglot_parse              | 764 us                                                      | 833 us: 1.09x slower                                                        |
| chaos                      | 37.9 ms                                                     | 41.3 ms: 1.09x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.75 us: 1.09x slower                                                       |
| pprint_safe_repr           | 485 ms                                                      | 531 ms: 1.10x slower                                                        |
| bench_thread_pool          | 810 us                                                      | 889 us: 1.10x slower                                                        |
| logging_simple             | 5.77 us                                                     | 6.34 us: 1.10x slower                                                       |
| sqlglot_transpile          | 953 us                                                      | 1.05 ms: 1.10x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.08 sec: 1.10x slower                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.87 ms: 1.10x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 3.20 sec: 1.11x slower                                                      |
| regex_dna                  | 115 ms                                                      | 129 ms: 1.12x slower                                                        |
| sphinx                     | 617 ms                                                      | 691 ms: 1.12x slower                                                        |
| richards                   | 26.3 ms                                                     | 29.4 ms: 1.12x slower                                                       |
| sqlglot_optimize           | 32.5 ms                                                     | 36.5 ms: 1.12x slower                                                       |
| scimark_fft                | 175 ms                                                      | 197 ms: 1.13x slower                                                        |
| python_startup             | 24.4 ms                                                     | 27.4 ms: 1.13x slower                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 104 ms: 1.13x slower                                                        |
| json                       | 3.30 ms                                                     | 3.73 ms: 1.13x slower                                                       |
| richards_super             | 29.8 ms                                                     | 33.6 ms: 1.13x slower                                                       |
| sqlglot_normalize          | 172 ms                                                      | 194 ms: 1.13x slower                                                        |
| nqueens                    | 56.1 ms                                                     | 64.0 ms: 1.14x slower                                                       |
| fannkuch                   | 252 ms                                                      | 287 ms: 1.14x slower                                                        |
| docutils                   | 1.53 sec                                                    | 1.75 sec: 1.15x slower                                                      |
| raytrace                   | 153 ms                                                      | 176 ms: 1.15x slower                                                        |
| crypto_pyaes               | 45.6 ms                                                     | 52.3 ms: 1.15x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 70.0 ms: 1.16x slower                                                       |
| mdp                        | 1.43 sec                                                    | 1.66 sec: 1.16x slower                                                      |
| unpickle_pure_python       | 130 us                                                      | 151 us: 1.16x slower                                                        |
| comprehensions             | 10.4 us                                                     | 12.1 us: 1.17x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 63.9 ns: 1.17x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 220 us: 1.18x slower                                                        |
| coverage                   | 45.3 ms                                                     | 53.9 ms: 1.19x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 67.7 ms: 1.19x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 20.4 ms: 1.21x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 65.8 ms: 1.23x slower                                                       |
| django_template            | 20.3 ms                                                     | 25.1 ms: 1.24x slower                                                       |
| many_optionals             | 361 us                                                      | 447 us: 1.24x slower                                                        |
| xml_etree_process          | 36.5 ms                                                     | 46.1 ms: 1.26x slower                                                       |
| mako                       | 6.56 ms                                                     | 8.33 ms: 1.27x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 7.88 ms: 1.27x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.65 ms: 1.35x slower                                                       |
| json_loads                 | 15.1 us                                                     | 20.5 us: 1.35x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 16.3 ms: 1.51x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                                |

Benchmark hidden because not significant (3): pylint, spectral_norm, k_core
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (8) of results/bm-20250301-3.14.0a5+-c9932a9-CLANG/bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.018x slower

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: unknown