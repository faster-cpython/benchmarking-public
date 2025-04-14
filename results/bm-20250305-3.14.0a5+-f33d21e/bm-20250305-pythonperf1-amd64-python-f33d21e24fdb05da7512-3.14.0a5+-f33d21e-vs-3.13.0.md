# Results vs. 3.13.0

- fork: python
- ref: f33d21e24fdb05da7512
- machine: windows-amd64
- commit hash: f33d21e
- commit date: 2025-03-05
- overall geometric mean: 1.005x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250305-pythonperf1-amd64-python-f33d21e24fdb05da7512-3.14.0a5+-f33d21e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 225 ms: 1.04x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.68 sec: 1.10x slower                                                      |
| html5lib       | 38.2 ms                                                     | 40.0 ms: 1.05x slower                                                       |
| sphinx         | 617 ms                                                      | 653 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                       | 1.06x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250305-pythonperf1-amd64-python-f33d21e24fdb05da7512-3.14.0a5+-f33d21e |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 217 ms: 1.29x faster                                                        |
| async_tree_io              | 513 ms                                                      | 421 ms: 1.22x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 411 ms: 1.21x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 220 ms: 1.20x faster                                                        |
| async_tree_none            | 219 ms                                                      | 187 ms: 1.17x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 179 ms: 1.12x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 345 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 348 ms: 1.10x faster                                                        |
| async_generators           | 223 ms                                                      | 226 ms: 1.01x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.8 ms: 1.10x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.11x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250305-pythonperf1-amd64-python-f33d21e24fdb05da7512-3.14.0a5+-f33d21e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 47.2 ms: 1.08x faster                                                       |
| pidigits       | 146 ms                                                      | 151 ms: 1.03x slower                                                        |
| nbody          | 66.3 ms                                                     | 73.4 ms: 1.11x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250305-pythonperf1-amd64-python-f33d21e24fdb05da7512-3.14.0a5+-f33d21e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.7 ms: 1.62x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.41 ms: 1.20x faster                                                       |
| regex_dna      | 115 ms                                                      | 113 ms: 1.02x faster                                                        |
| regex_compile  | 80.7 ms                                                     | 88.9 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250305-pythonperf1-amd64-python-f33d21e24fdb05da7512-3.14.0a5+-f33d21e |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.6 us: 1.03x faster                                                       |
| xml_etree_parse      | 92.2 ms                                                     | 91.0 ms: 1.01x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.44 sec: 1.05x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.8 ms: 1.05x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 58.0 ms: 1.09x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 6.81 ms: 1.10x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 40.7 ms: 1.12x slower                                                       |
| unpickle_pure_python | 130 us                                                      | 152 us: 1.17x slower                                                        |
| pickle_pure_python   | 186 us                                                      | 229 us: 1.23x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.08x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250305-pythonperf1-amd64-python-f33d21e24fdb05da7512-3.14.0a5+-f33d21e |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.1 ms: 1.03x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 19.0 ms: 1.13x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.08x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250305-pythonperf1-amd64-python-f33d21e24fdb05da7512-3.14.0a5+-f33d21e |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.96 ms: 1.06x slower                                                       |
| genshi_xml      | 33.9 ms                                                     | 36.2 ms: 1.07x slower                                                       |
| genshi_text     | 15.2 ms                                                     | 16.5 ms: 1.08x slower                                                       |
| django_template | 20.3 ms                                                     | 24.9 ms: 1.23x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.11x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250305-pythonperf1-amd64-python-f33d21e24fdb05da7512-3.14.0a5+-f33d21e |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 513 us: 16.50x faster                                                       |
| pathlib                    | 75.3 ms                                                     | 32.0 ms: 2.35x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.7 ms: 1.62x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 217 ms: 1.29x faster                                                        |
| async_tree_io              | 513 ms                                                      | 421 ms: 1.22x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 411 ms: 1.21x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.41 ms: 1.20x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 220 ms: 1.20x faster                                                        |
| deepcopy                   | 223 us                                                      | 187 us: 1.19x faster                                                        |
| async_tree_none            | 219 ms                                                      | 187 ms: 1.17x faster                                                        |
| json                       | 3.30 ms                                                     | 2.95 ms: 1.12x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 179 ms: 1.12x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 345 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 348 ms: 1.10x faster                                                        |
| deepcopy_memo              | 23.1 us                                                     | 21.0 us: 1.10x faster                                                       |
| float                      | 50.8 ms                                                     | 47.2 ms: 1.08x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.93 us: 1.05x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.6 us: 1.03x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 61.5 ms: 1.03x faster                                                       |
| regex_dna                  | 115 ms                                                      | 113 ms: 1.02x faster                                                        |
| telco                      | 4.85 ms                                                     | 4.78 ms: 1.01x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 91.0 ms: 1.01x faster                                                       |
| shortest_path              | 355 ms                                                      | 358 ms: 1.01x slower                                                        |
| async_generators           | 223 ms                                                      | 226 ms: 1.01x slower                                                        |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.64 ms: 1.01x slower                                                       |
| k_core                     | 1.70 sec                                                    | 1.74 sec: 1.03x slower                                                      |
| connected_components       | 320 ms                                                      | 328 ms: 1.03x slower                                                        |
| bench_mp_pool              | 84.2 ms                                                     | 86.6 ms: 1.03x slower                                                       |
| python_startup             | 24.4 ms                                                     | 25.1 ms: 1.03x slower                                                       |
| pidigits                   | 146 ms                                                      | 151 ms: 1.03x slower                                                        |
| gc_traversal               | 1.96 ms                                                     | 2.03 ms: 1.04x slower                                                       |
| generators                 | 19.0 ms                                                     | 19.7 ms: 1.04x slower                                                       |
| mdp                        | 1.43 sec                                                    | 1.49 sec: 1.04x slower                                                      |
| bpe_tokeniser              | 2.87 sec                                                    | 3.00 sec: 1.04x slower                                                      |
| 2to3                       | 215 ms                                                      | 225 ms: 1.04x slower                                                        |
| typing_runtime_protocols   | 103 us                                                      | 108 us: 1.05x slower                                                        |
| go                         | 84.7 ms                                                     | 88.6 ms: 1.05x slower                                                       |
| html5lib                   | 38.2 ms                                                     | 40.0 ms: 1.05x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 850 us: 1.05x slower                                                        |
| sympy_expand               | 286 ms                                                      | 300 ms: 1.05x slower                                                        |
| coverage                   | 45.3 ms                                                     | 47.7 ms: 1.05x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.44 sec: 1.05x slower                                                      |
| sympy_str                  | 167 ms                                                      | 176 ms: 1.05x slower                                                        |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.8 ms: 1.05x slower                                                       |
| sphinx                     | 617 ms                                                      | 653 ms: 1.06x slower                                                        |
| sympy_sum                  | 85.2 ms                                                     | 90.1 ms: 1.06x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 42.5 ms: 1.06x slower                                                       |
| mako                       | 6.56 ms                                                     | 6.96 ms: 1.06x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 76.5 ms: 1.06x slower                                                       |
| genshi_xml                 | 33.9 ms                                                     | 36.2 ms: 1.07x slower                                                       |
| pycparser                  | 695 ms                                                      | 746 ms: 1.07x slower                                                        |
| genshi_text                | 15.2 ms                                                     | 16.5 ms: 1.08x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 58.0 ms: 1.09x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.4 ms: 1.09x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 49.9 ms: 1.09x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.68 sec: 1.10x slower                                                      |
| sqlglot_optimize           | 32.5 ms                                                     | 35.7 ms: 1.10x slower                                                       |
| scimark_fft                | 175 ms                                                      | 192 ms: 1.10x slower                                                        |
| json_dumps                 | 6.19 ms                                                     | 6.81 ms: 1.10x slower                                                       |
| regex_compile              | 80.7 ms                                                     | 88.9 ms: 1.10x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.8 ms: 1.10x slower                                                       |
| nbody                      | 66.3 ms                                                     | 73.4 ms: 1.11x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 40.7 ms: 1.12x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.47 us: 1.12x slower                                                       |
| comprehensions             | 10.4 us                                                     | 11.6 us: 1.12x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 19.0 ms: 1.13x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 63.2 ms: 1.13x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.98 us: 1.13x slower                                                       |
| pyflate                    | 283 ms                                                      | 320 ms: 1.13x slower                                                        |
| sqlglot_normalize          | 172 ms                                                      | 194 ms: 1.13x slower                                                        |
| logging_silent             | 54.6 ns                                                     | 61.9 ns: 1.13x slower                                                       |
| chaos                      | 37.9 ms                                                     | 43.0 ms: 1.14x slower                                                       |
| fannkuch                   | 252 ms                                                      | 286 ms: 1.14x slower                                                        |
| sqlglot_transpile          | 953 us                                                      | 1.11 ms: 1.16x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.48 ms: 1.17x slower                                                       |
| sqlglot_parse              | 764 us                                                      | 891 us: 1.17x slower                                                        |
| richards                   | 26.3 ms                                                     | 30.7 ms: 1.17x slower                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 47.8 ms: 1.17x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 152 us: 1.17x slower                                                        |
| scimark_sor                | 76.2 ms                                                     | 89.9 ms: 1.18x slower                                                       |
| richards_super             | 29.8 ms                                                     | 35.3 ms: 1.18x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.16 sec: 1.18x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 577 ms: 1.19x slower                                                        |
| scimark_lu                 | 56.7 ms                                                     | 67.7 ms: 1.19x slower                                                       |
| many_optionals             | 361 us                                                      | 433 us: 1.20x slower                                                        |
| deltablue                  | 1.89 ms                                                     | 2.29 ms: 1.21x slower                                                       |
| django_template            | 20.3 ms                                                     | 24.9 ms: 1.23x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 229 us: 1.23x slower                                                        |
| raytrace                   | 153 ms                                                      | 195 ms: 1.27x slower                                                        |
| subparsers                 | 10.9 ms                                                     | 16.3 ms: 1.51x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (4): pylint, sqlite_synth, create_gc_cycles, asyncio_websockets
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http

- Geometric mean (including insignificant results): 1.005x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown