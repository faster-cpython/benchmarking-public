# Results vs. 3.13.0

- fork: python
- ref: c9932a9ec8a3077933a8
- machine: windows-amd64
- commit hash: c9932a9
- commit date: 2025-03-01
- overall geometric mean: 1.030x faster
- HPT reliability: 90.62%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 225 ms: 1.05x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.71 sec: 1.11x slower                                                      |
| html5lib       | 38.2 ms                                                     | 40.2 ms: 1.05x slower                                                       |
| sphinx         | 617 ms                                                      | 659 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                       | 1.07x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 212 ms: 1.32x faster                                                        |
| async_tree_io              | 513 ms                                                      | 417 ms: 1.23x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 404 ms: 1.23x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 218 ms: 1.22x faster                                                        |
| async_tree_none            | 219 ms                                                      | 185 ms: 1.18x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 171 ms: 1.17x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 340 ms: 1.12x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 346 ms: 1.10x faster                                                        |
| asyncio_websockets         | 300 ms                                                      | 319 ms: 1.06x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.3 ms: 1.06x slower                                                       |
| async_generators           | 223 ms                                                      | 251 ms: 1.13x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.11x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 60.0 ms: 1.10x faster                                                       |
| float          | 50.8 ms                                                     | 47.1 ms: 1.08x faster                                                       |
| pidigits       | 146 ms                                                      | 152 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 15.2 ms: 1.57x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.47 ms: 1.16x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 83.7 ms: 1.04x slower                                                       |
| regex_dna      | 115 ms                                                      | 125 ms: 1.09x slower                                                        |
| Geometric mean | (ref)                                                       | 1.13x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 130 us                                                      | 114 us: 1.15x faster                                                        |
| tomli_loads          | 1.37 sec                                                    | 1.22 sec: 1.13x faster                                                      |
| json_loads           | 15.1 us                                                     | 14.6 us: 1.04x faster                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 51.6 ms: 1.03x faster                                                       |
| xml_etree_parse      | 92.2 ms                                                     | 91.2 ms: 1.01x faster                                                       |
| xml_etree_process    | 36.5 ms                                                     | 36.8 ms: 1.01x slower                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 62.0 ms: 1.03x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 6.93 ms: 1.12x slower                                                       |
| pickle_pure_python   | 186 us                                                      | 219 us: 1.18x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.00x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.9 ms: 1.06x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 19.5 ms: 1.16x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.34 ms: 1.23x faster                                                       |
| genshi_xml      | 33.9 ms                                                     | 35.3 ms: 1.04x slower                                                       |
| genshi_text     | 15.2 ms                                                     | 16.3 ms: 1.07x slower                                                       |
| django_template | 20.3 ms                                                     | 25.8 ms: 1.27x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.04x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 521 us: 16.25x faster                                                       |
| pathlib                    | 75.3 ms                                                     | 31.9 ms: 2.36x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 15.2 ms: 1.57x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 212 ms: 1.32x faster                                                        |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.09 ms: 1.25x faster                                                       |
| async_tree_io              | 513 ms                                                      | 417 ms: 1.23x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 404 ms: 1.23x faster                                                        |
| mako                       | 6.56 ms                                                     | 5.34 ms: 1.23x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 218 ms: 1.22x faster                                                        |
| deepcopy                   | 223 us                                                      | 184 us: 1.21x faster                                                        |
| async_tree_none            | 219 ms                                                      | 185 ms: 1.18x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 171 ms: 1.17x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.47 ms: 1.16x faster                                                       |
| scimark_fft                | 175 ms                                                      | 152 ms: 1.15x faster                                                        |
| deepcopy_memo              | 23.1 us                                                     | 20.1 us: 1.15x faster                                                       |
| unpickle_pure_python       | 130 us                                                      | 114 us: 1.15x faster                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.22 sec: 1.13x faster                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 340 ms: 1.12x faster                                                        |
| telco                      | 4.85 ms                                                     | 4.32 ms: 1.12x faster                                                       |
| json                       | 3.30 ms                                                     | 2.95 ms: 1.12x faster                                                       |
| nbody                      | 66.3 ms                                                     | 60.0 ms: 1.10x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 346 ms: 1.10x faster                                                        |
| bpe_tokeniser              | 2.87 sec                                                    | 2.62 sec: 1.10x faster                                                      |
| float                      | 50.8 ms                                                     | 47.1 ms: 1.08x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.92 us: 1.06x faster                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.53 us: 1.04x faster                                                       |
| k_core                     | 1.70 sec                                                    | 1.63 sec: 1.04x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.6 us: 1.04x faster                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 51.6 ms: 1.03x faster                                                       |
| pyflate                    | 283 ms                                                      | 274 ms: 1.03x faster                                                        |
| fannkuch                   | 252 ms                                                      | 245 ms: 1.03x faster                                                        |
| shortest_path              | 355 ms                                                      | 350 ms: 1.01x faster                                                        |
| spectral_norm              | 63.4 ms                                                     | 62.6 ms: 1.01x faster                                                       |
| connected_components       | 320 ms                                                      | 316 ms: 1.01x faster                                                        |
| xml_etree_parse            | 92.2 ms                                                     | 91.2 ms: 1.01x faster                                                       |
| xml_etree_process          | 36.5 ms                                                     | 36.8 ms: 1.01x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 999 ms: 1.02x slower                                                        |
| generators                 | 19.0 ms                                                     | 19.4 ms: 1.02x slower                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 86.3 ms: 1.02x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 62.0 ms: 1.03x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 74.0 ms: 1.03x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 47.0 ms: 1.03x slower                                                       |
| go                         | 84.7 ms                                                     | 87.4 ms: 1.03x slower                                                       |
| pidigits                   | 146 ms                                                      | 152 ms: 1.03x slower                                                        |
| regex_compile              | 80.7 ms                                                     | 83.7 ms: 1.04x slower                                                       |
| pprint_safe_repr           | 485 ms                                                      | 504 ms: 1.04x slower                                                        |
| genshi_xml                 | 33.9 ms                                                     | 35.3 ms: 1.04x slower                                                       |
| mdp                        | 1.43 sec                                                    | 1.49 sec: 1.04x slower                                                      |
| sympy_sum                  | 85.2 ms                                                     | 89.0 ms: 1.05x slower                                                       |
| 2to3                       | 215 ms                                                      | 225 ms: 1.05x slower                                                        |
| bench_thread_pool          | 810 us                                                      | 848 us: 1.05x slower                                                        |
| typing_runtime_protocols   | 103 us                                                      | 108 us: 1.05x slower                                                        |
| sympy_str                  | 167 ms                                                      | 175 ms: 1.05x slower                                                        |
| pycparser                  | 695 ms                                                      | 730 ms: 1.05x slower                                                        |
| html5lib                   | 38.2 ms                                                     | 40.2 ms: 1.05x slower                                                       |
| sympy_expand               | 286 ms                                                      | 303 ms: 1.06x slower                                                        |
| python_startup             | 24.4 ms                                                     | 25.9 ms: 1.06x slower                                                       |
| asyncio_websockets         | 300 ms                                                      | 319 ms: 1.06x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.3 ms: 1.06x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 59.8 ms: 1.07x slower                                                       |
| coverage                   | 45.3 ms                                                     | 48.3 ms: 1.07x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 42.7 ms: 1.07x slower                                                       |
| sphinx                     | 617 ms                                                      | 659 ms: 1.07x slower                                                        |
| comprehensions             | 10.4 us                                                     | 11.1 us: 1.07x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 16.3 ms: 1.07x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.3 ms: 1.08x slower                                                       |
| regex_dna                  | 115 ms                                                      | 125 ms: 1.09x slower                                                        |
| sqlglot_parse              | 764 us                                                      | 841 us: 1.10x slower                                                        |
| scimark_sor                | 76.2 ms                                                     | 84.5 ms: 1.11x slower                                                       |
| chaos                      | 37.9 ms                                                     | 42.1 ms: 1.11x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.71 sec: 1.11x slower                                                      |
| json_dumps                 | 6.19 ms                                                     | 6.93 ms: 1.12x slower                                                       |
| sqlglot_transpile          | 953 us                                                      | 1.07 ms: 1.12x slower                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 45.7 ms: 1.12x slower                                                       |
| sqlglot_optimize           | 32.5 ms                                                     | 36.6 ms: 1.12x slower                                                       |
| async_generators           | 223 ms                                                      | 251 ms: 1.13x slower                                                        |
| logging_format             | 6.18 us                                                     | 7.01 us: 1.13x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.57 us: 1.14x slower                                                       |
| richards                   | 26.3 ms                                                     | 29.9 ms: 1.14x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 64.8 ms: 1.14x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.39 ms: 1.14x slower                                                       |
| richards_super             | 29.8 ms                                                     | 34.1 ms: 1.15x slower                                                       |
| sqlglot_normalize          | 172 ms                                                      | 197 ms: 1.15x slower                                                        |
| python_startup_no_site     | 16.9 ms                                                     | 19.5 ms: 1.16x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 63.7 ns: 1.17x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 219 us: 1.18x slower                                                        |
| deltablue                  | 1.89 ms                                                     | 2.25 ms: 1.19x slower                                                       |
| many_optionals             | 361 us                                                      | 452 us: 1.25x slower                                                        |
| raytrace                   | 153 ms                                                      | 193 ms: 1.26x slower                                                        |
| django_template            | 20.3 ms                                                     | 25.8 ms: 1.27x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 15.8 ms: 1.46x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (3): pylint, create_gc_cycles, gc_traversal
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (8) of results/bm-20250301-3.14.0a5+-c9932a9-JIT/bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.030x faster

# HPT report

- Reliability score: 90.62% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown