# Results vs. 3.13.0

- fork: brandtbucher
- ref: nojit
- machine: windows-amd64
- commit hash: f098037
- commit date: 2025-01-07
- overall geometric mean: 1.001x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 222 ms: 1.03x slower                                               |
| docutils       | 1.53 sec                                                    | 1.66 sec: 1.08x slower                                             |
| html5lib       | 38.2 ms                                                     | 37.1 ms: 1.03x faster                                              |
| sphinx         | 617 ms                                                      | 641 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                       | 1.03x slower                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 210 ms: 1.34x faster                                               |
| async_tree_io              | 513 ms                                                      | 409 ms: 1.25x faster                                               |
| async_tree_io_tg           | 497 ms                                                      | 402 ms: 1.24x faster                                               |
| async_tree_none            | 219 ms                                                      | 185 ms: 1.18x faster                                               |
| async_tree_none_tg         | 200 ms                                                      | 170 ms: 1.18x faster                                               |
| async_tree_memoization     | 265 ms                                                      | 226 ms: 1.17x faster                                               |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 347 ms: 1.10x faster                                               |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 349 ms: 1.09x faster                                               |
| async_generators           | 223 ms                                                      | 236 ms: 1.06x slower                                               |
| coroutines                 | 12.5 ms                                                     | 13.3 ms: 1.06x slower                                              |
| Geometric mean             | (ref)                                                       | 1.12x faster                                                       |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 51.2 ms: 1.01x slower                                              |
| pidigits       | 146 ms                                                      | 148 ms: 1.01x slower                                               |
| nbody          | 66.3 ms                                                     | 73.5 ms: 1.11x slower                                              |
| Geometric mean | (ref)                                                       | 1.04x slower                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 15.6 ms: 1.53x faster                                              |
| regex_effbot   | 1.69 ms                                                     | 1.45 ms: 1.17x faster                                              |
| regex_compile  | 80.7 ms                                                     | 82.9 ms: 1.03x slower                                              |
| regex_dna      | 115 ms                                                      | 124 ms: 1.07x slower                                               |
| Geometric mean | (ref)                                                       | 1.13x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.5 us: 1.04x faster                                              |
| xml_etree_parse      | 92.2 ms                                                     | 88.6 ms: 1.04x faster                                              |
| tomli_loads          | 1.37 sec                                                    | 1.41 sec: 1.03x slower                                             |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.8 ms: 1.05x slower                                              |
| xml_etree_generate   | 53.5 ms                                                     | 57.0 ms: 1.07x slower                                              |
| json_dumps           | 6.19 ms                                                     | 6.80 ms: 1.10x slower                                              |
| unpickle_pure_python | 130 us                                                      | 144 us: 1.11x slower                                               |
| xml_etree_process    | 36.5 ms                                                     | 40.6 ms: 1.11x slower                                              |
| pickle_pure_python   | 186 us                                                      | 220 us: 1.18x slower                                               |
| Geometric mean       | (ref)                                                       | 1.06x slower                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 23.4 ms: 1.04x faster                                              |
| python_startup_no_site | 16.9 ms                                                     | 17.3 ms: 1.02x slower                                              |
| Geometric mean         | (ref)                                                       | 1.01x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.71 ms: 1.02x slower                                              |
| genshi_xml      | 33.9 ms                                                     | 34.9 ms: 1.03x slower                                              |
| genshi_text     | 15.2 ms                                                     | 16.9 ms: 1.11x slower                                              |
| django_template | 20.3 ms                                                     | 25.5 ms: 1.25x slower                                              |
| Geometric mean  | (ref)                                                       | 1.10x slower                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 514 us: 16.47x faster                                              |
| regex_v8                   | 23.8 ms                                                     | 15.6 ms: 1.53x faster                                              |
| async_tree_memoization_tg  | 281 ms                                                      | 210 ms: 1.34x faster                                               |
| async_tree_io              | 513 ms                                                      | 409 ms: 1.25x faster                                               |
| async_tree_io_tg           | 497 ms                                                      | 402 ms: 1.24x faster                                               |
| deepcopy                   | 223 us                                                      | 187 us: 1.20x faster                                               |
| async_tree_none            | 219 ms                                                      | 185 ms: 1.18x faster                                               |
| async_tree_none_tg         | 200 ms                                                      | 170 ms: 1.18x faster                                               |
| async_tree_memoization     | 265 ms                                                      | 226 ms: 1.17x faster                                               |
| regex_effbot               | 1.69 ms                                                     | 1.45 ms: 1.17x faster                                              |
| deepcopy_memo              | 23.1 us                                                     | 20.4 us: 1.13x faster                                              |
| json                       | 3.30 ms                                                     | 2.97 ms: 1.11x faster                                              |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 347 ms: 1.10x faster                                               |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 349 ms: 1.09x faster                                               |
| spectral_norm              | 63.4 ms                                                     | 59.1 ms: 1.07x faster                                              |
| deepcopy_reduce            | 2.02 us                                                     | 1.89 us: 1.07x faster                                              |
| json_loads                 | 15.1 us                                                     | 14.5 us: 1.04x faster                                              |
| python_startup             | 24.4 ms                                                     | 23.4 ms: 1.04x faster                                              |
| xml_etree_parse            | 92.2 ms                                                     | 88.6 ms: 1.04x faster                                              |
| dulwich_log                | 40.1 ms                                                     | 39.0 ms: 1.03x faster                                              |
| html5lib                   | 38.2 ms                                                     | 37.1 ms: 1.03x faster                                              |
| bench_mp_pool              | 84.2 ms                                                     | 82.1 ms: 1.03x faster                                              |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.54 ms: 1.02x faster                                              |
| create_gc_cycles           | 1.22 ms                                                     | 1.20 ms: 1.02x faster                                              |
| telco                      | 4.85 ms                                                     | 4.78 ms: 1.01x faster                                              |
| scimark_lu                 | 56.7 ms                                                     | 57.0 ms: 1.01x slower                                              |
| connected_components       | 320 ms                                                      | 322 ms: 1.01x slower                                               |
| float                      | 50.8 ms                                                     | 51.2 ms: 1.01x slower                                              |
| go                         | 84.7 ms                                                     | 85.3 ms: 1.01x slower                                              |
| sympy_expand               | 286 ms                                                      | 288 ms: 1.01x slower                                               |
| pidigits                   | 146 ms                                                      | 148 ms: 1.01x slower                                               |
| pathlib                    | 75.3 ms                                                     | 76.0 ms: 1.01x slower                                              |
| python_startup_no_site     | 16.9 ms                                                     | 17.3 ms: 1.02x slower                                              |
| mako                       | 6.56 ms                                                     | 6.71 ms: 1.02x slower                                              |
| sympy_str                  | 167 ms                                                      | 171 ms: 1.02x slower                                               |
| bench_thread_pool          | 810 us                                                      | 829 us: 1.02x slower                                               |
| regex_compile              | 80.7 ms                                                     | 82.9 ms: 1.03x slower                                              |
| tomli_loads                | 1.37 sec                                                    | 1.41 sec: 1.03x slower                                             |
| genshi_xml                 | 33.9 ms                                                     | 34.9 ms: 1.03x slower                                              |
| 2to3                       | 215 ms                                                      | 222 ms: 1.03x slower                                               |
| coverage                   | 45.3 ms                                                     | 46.8 ms: 1.03x slower                                              |
| sympy_sum                  | 85.2 ms                                                     | 88.4 ms: 1.04x slower                                              |
| sphinx                     | 617 ms                                                      | 641 ms: 1.04x slower                                               |
| bpe_tokeniser              | 2.87 sec                                                    | 3.00 sec: 1.04x slower                                             |
| mdp                        | 1.43 sec                                                    | 1.50 sec: 1.05x slower                                             |
| sqlite_synth               | 1.59 us                                                     | 1.66 us: 1.05x slower                                              |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.8 ms: 1.05x slower                                              |
| crypto_pyaes               | 45.6 ms                                                     | 48.2 ms: 1.06x slower                                              |
| async_generators           | 223 ms                                                      | 236 ms: 1.06x slower                                               |
| scimark_fft                | 175 ms                                                      | 185 ms: 1.06x slower                                               |
| coroutines                 | 12.5 ms                                                     | 13.3 ms: 1.06x slower                                              |
| xml_etree_generate         | 53.5 ms                                                     | 57.0 ms: 1.07x slower                                              |
| regex_dna                  | 115 ms                                                      | 124 ms: 1.07x slower                                               |
| pycparser                  | 695 ms                                                      | 747 ms: 1.07x slower                                               |
| meteor_contest             | 72.0 ms                                                     | 77.5 ms: 1.08x slower                                              |
| fannkuch                   | 252 ms                                                      | 271 ms: 1.08x slower                                               |
| docutils                   | 1.53 sec                                                    | 1.66 sec: 1.08x slower                                             |
| sympy_integrate            | 12.3 ms                                                     | 13.4 ms: 1.08x slower                                              |
| typing_runtime_protocols   | 103 us                                                      | 113 us: 1.09x slower                                               |
| scimark_monte_carlo        | 40.7 ms                                                     | 44.5 ms: 1.09x slower                                              |
| sqlglot_optimize           | 32.5 ms                                                     | 35.6 ms: 1.09x slower                                              |
| json_dumps                 | 6.19 ms                                                     | 6.80 ms: 1.10x slower                                              |
| logging_simple             | 5.77 us                                                     | 6.37 us: 1.10x slower                                              |
| unpickle_pure_python       | 130 us                                                      | 144 us: 1.11x slower                                               |
| logging_format             | 6.18 us                                                     | 6.83 us: 1.11x slower                                              |
| nbody                      | 66.3 ms                                                     | 73.5 ms: 1.11x slower                                              |
| pprint_pformat             | 977 ms                                                      | 1.09 sec: 1.11x slower                                             |
| xml_etree_process          | 36.5 ms                                                     | 40.6 ms: 1.11x slower                                              |
| genshi_text                | 15.2 ms                                                     | 16.9 ms: 1.11x slower                                              |
| pprint_safe_repr           | 485 ms                                                      | 542 ms: 1.12x slower                                               |
| hexiom                     | 3.84 ms                                                     | 4.33 ms: 1.13x slower                                              |
| pyflate                    | 283 ms                                                      | 319 ms: 1.13x slower                                               |
| logging_silent             | 54.6 ns                                                     | 61.7 ns: 1.13x slower                                              |
| chaos                      | 37.9 ms                                                     | 42.8 ms: 1.13x slower                                              |
| nqueens                    | 56.1 ms                                                     | 63.8 ms: 1.14x slower                                              |
| sqlglot_normalize          | 172 ms                                                      | 196 ms: 1.14x slower                                               |
| sqlglot_parse              | 764 us                                                      | 877 us: 1.15x slower                                               |
| generators                 | 19.0 ms                                                     | 21.9 ms: 1.16x slower                                              |
| sqlglot_transpile          | 953 us                                                      | 1.10 ms: 1.16x slower                                              |
| scimark_sor                | 76.2 ms                                                     | 88.9 ms: 1.17x slower                                              |
| deltablue                  | 1.89 ms                                                     | 2.23 ms: 1.18x slower                                              |
| richards                   | 26.3 ms                                                     | 31.1 ms: 1.18x slower                                              |
| pickle_pure_python         | 186 us                                                      | 220 us: 1.18x slower                                               |
| richards_super             | 29.8 ms                                                     | 35.3 ms: 1.18x slower                                              |
| comprehensions             | 10.4 us                                                     | 12.3 us: 1.19x slower                                              |
| many_optionals             | 361 us                                                      | 433 us: 1.20x slower                                               |
| raytrace                   | 153 ms                                                      | 188 ms: 1.23x slower                                               |
| django_template            | 20.3 ms                                                     | 25.5 ms: 1.25x slower                                              |
| subparsers                 | 10.9 ms                                                     | 16.5 ms: 1.52x slower                                              |
| Geometric mean             | (ref)                                                       | 1.00x slower                                                       |

Benchmark hidden because not significant (5): pylint, shortest_path, k_core, gc_traversal, asyncio_websockets
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of results/bm-20250107-3.14.0a3+-f098037/bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037.json: mypy2

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown