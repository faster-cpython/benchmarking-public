# Results vs. 3.13.0

- fork: python
- ref: c9932a9ec8a3077933a8
- machine: windows-amd64
- commit hash: c9932a9
- commit date: 2025-03-01
- overall geometric mean: 1.010x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 223 ms: 1.04x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.66 sec: 1.08x slower                                                      |
| html5lib       | 38.2 ms                                                     | 40.4 ms: 1.06x slower                                                       |
| sphinx         | 617 ms                                                      | 643 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                       | 1.06x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 212 ms: 1.32x faster                                                        |
| async_tree_io              | 513 ms                                                      | 416 ms: 1.23x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 403 ms: 1.23x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 217 ms: 1.22x faster                                                        |
| async_tree_none            | 219 ms                                                      | 187 ms: 1.17x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 177 ms: 1.13x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 340 ms: 1.12x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 344 ms: 1.11x faster                                                        |
| async_generators           | 223 ms                                                      | 220 ms: 1.01x faster                                                        |
| asyncio_websockets         | 300 ms                                                      | 306 ms: 1.02x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.2 ms: 1.06x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.13x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 44.9 ms: 1.13x faster                                                       |
| pidigits       | 146 ms                                                      | 150 ms: 1.02x slower                                                        |
| nbody          | 66.3 ms                                                     | 68.9 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.4 ms: 1.65x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.47 ms: 1.15x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 87.6 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 90.2 ms: 1.02x faster                                                       |
| json_loads           | 15.1 us                                                     | 14.8 us: 1.02x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.43 sec: 1.04x slower                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 56.2 ms: 1.05x slower                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.8 ms: 1.05x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 40.1 ms: 1.10x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 6.85 ms: 1.11x slower                                                       |
| unpickle_pure_python | 130 us                                                      | 148 us: 1.14x slower                                                        |
| pickle_pure_python   | 186 us                                                      | 229 us: 1.23x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.0 ms: 1.03x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 19.2 ms: 1.13x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.08x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 35.8 ms: 1.06x slower                                                       |
| mako            | 6.56 ms                                                     | 6.95 ms: 1.06x slower                                                       |
| genshi_text     | 15.2 ms                                                     | 16.6 ms: 1.09x slower                                                       |
| django_template | 20.3 ms                                                     | 24.8 ms: 1.22x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.10x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 507 us: 16.70x faster                                                       |
| pathlib                    | 75.3 ms                                                     | 34.6 ms: 2.18x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.4 ms: 1.65x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 212 ms: 1.32x faster                                                        |
| async_tree_io              | 513 ms                                                      | 416 ms: 1.23x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 403 ms: 1.23x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 217 ms: 1.22x faster                                                        |
| deepcopy                   | 223 us                                                      | 186 us: 1.20x faster                                                        |
| async_tree_none            | 219 ms                                                      | 187 ms: 1.17x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.47 ms: 1.15x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 20.3 us: 1.14x faster                                                       |
| float                      | 50.8 ms                                                     | 44.9 ms: 1.13x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 177 ms: 1.13x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 340 ms: 1.12x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 344 ms: 1.11x faster                                                        |
| json                       | 3.30 ms                                                     | 2.97 ms: 1.11x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 59.1 ms: 1.07x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.95 us: 1.04x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 90.2 ms: 1.02x faster                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.55 us: 1.02x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.8 us: 1.02x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.78 ms: 1.01x faster                                                       |
| shortest_path              | 355 ms                                                      | 351 ms: 1.01x faster                                                        |
| async_generators           | 223 ms                                                      | 220 ms: 1.01x faster                                                        |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.62 ms: 1.01x slower                                                       |
| go                         | 84.7 ms                                                     | 86.1 ms: 1.02x slower                                                       |
| asyncio_websockets         | 300 ms                                                      | 306 ms: 1.02x slower                                                        |
| typing_runtime_protocols   | 103 us                                                      | 105 us: 1.02x slower                                                        |
| pidigits                   | 146 ms                                                      | 150 ms: 1.02x slower                                                        |
| bench_mp_pool              | 84.2 ms                                                     | 86.2 ms: 1.02x slower                                                       |
| python_startup             | 24.4 ms                                                     | 25.0 ms: 1.03x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.02 ms: 1.03x slower                                                       |
| generators                 | 19.0 ms                                                     | 19.5 ms: 1.03x slower                                                       |
| sympy_expand               | 286 ms                                                      | 295 ms: 1.03x slower                                                        |
| 2to3                       | 215 ms                                                      | 223 ms: 1.04x slower                                                        |
| nbody                      | 66.3 ms                                                     | 68.9 ms: 1.04x slower                                                       |
| sphinx                     | 617 ms                                                      | 643 ms: 1.04x slower                                                        |
| scimark_fft                | 175 ms                                                      | 182 ms: 1.04x slower                                                        |
| sympy_str                  | 167 ms                                                      | 174 ms: 1.04x slower                                                        |
| coverage                   | 45.3 ms                                                     | 47.3 ms: 1.04x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.43 sec: 1.04x slower                                                      |
| sympy_sum                  | 85.2 ms                                                     | 89.0 ms: 1.04x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 75.5 ms: 1.05x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 42.2 ms: 1.05x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 852 us: 1.05x slower                                                        |
| xml_etree_generate         | 53.5 ms                                                     | 56.2 ms: 1.05x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.8 ms: 1.05x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.2 ms: 1.06x slower                                                       |
| genshi_xml                 | 33.9 ms                                                     | 35.8 ms: 1.06x slower                                                       |
| html5lib                   | 38.2 ms                                                     | 40.4 ms: 1.06x slower                                                       |
| mako                       | 6.56 ms                                                     | 6.95 ms: 1.06x slower                                                       |
| pycparser                  | 695 ms                                                      | 741 ms: 1.07x slower                                                        |
| sqlglot_optimize           | 32.5 ms                                                     | 34.9 ms: 1.07x slower                                                       |
| pyflate                    | 283 ms                                                      | 304 ms: 1.08x slower                                                        |
| sympy_integrate            | 12.3 ms                                                     | 13.3 ms: 1.08x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.66 sec: 1.08x slower                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 49.5 ms: 1.08x slower                                                       |
| comprehensions             | 10.4 us                                                     | 11.2 us: 1.09x slower                                                       |
| regex_compile              | 80.7 ms                                                     | 87.6 ms: 1.09x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 16.6 ms: 1.09x slower                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 44.7 ms: 1.10x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 40.1 ms: 1.10x slower                                                       |
| fannkuch                   | 252 ms                                                      | 277 ms: 1.10x slower                                                        |
| chaos                      | 37.9 ms                                                     | 41.8 ms: 1.10x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 6.85 ms: 1.11x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 84.5 ms: 1.11x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 60.8 ns: 1.11x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 63.2 ms: 1.11x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.89 us: 1.12x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.45 us: 1.12x slower                                                       |
| mdp                        | 1.43 sec                                                    | 1.60 sec: 1.12x slower                                                      |
| sqlglot_normalize          | 172 ms                                                      | 192 ms: 1.12x slower                                                        |
| sqlglot_transpile          | 953 us                                                      | 1.07 ms: 1.12x slower                                                       |
| sqlglot_parse              | 764 us                                                      | 862 us: 1.13x slower                                                        |
| nqueens                    | 56.1 ms                                                     | 63.4 ms: 1.13x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.35 ms: 1.13x slower                                                       |
| pprint_safe_repr           | 485 ms                                                      | 549 ms: 1.13x slower                                                        |
| python_startup_no_site     | 16.9 ms                                                     | 19.2 ms: 1.13x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.11 sec: 1.14x slower                                                      |
| richards                   | 26.3 ms                                                     | 29.9 ms: 1.14x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 148 us: 1.14x slower                                                        |
| deltablue                  | 1.89 ms                                                     | 2.16 ms: 1.14x slower                                                       |
| richards_super             | 29.8 ms                                                     | 34.4 ms: 1.15x slower                                                       |
| many_optionals             | 361 us                                                      | 431 us: 1.19x slower                                                        |
| django_template            | 20.3 ms                                                     | 24.8 ms: 1.22x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 229 us: 1.23x slower                                                        |
| raytrace                   | 153 ms                                                      | 192 ms: 1.25x slower                                                        |
| subparsers                 | 10.9 ms                                                     | 15.9 ms: 1.47x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (6): pylint, create_gc_cycles, regex_dna, bpe_tokeniser, connected_components, k_core
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (8) of results/bm-20250301-3.14.0a5+-c9932a9/bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.010x faster

# HPT report

- Reliability score: 99.96% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown