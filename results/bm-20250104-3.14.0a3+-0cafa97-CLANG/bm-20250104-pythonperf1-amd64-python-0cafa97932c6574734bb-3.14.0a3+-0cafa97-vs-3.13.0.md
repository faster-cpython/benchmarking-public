# Results vs. 3.13.0

- fork: python
- ref: 0cafa97932c6574734bb
- machine: windows-amd64
- commit hash: 0cafa97
- commit date: 2025-01-04
- overall geometric mean: 1.038x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 235 ms: 1.09x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.76 sec: 1.15x slower                                                      |
| html5lib       | 38.2 ms                                                     | 39.3 ms: 1.03x slower                                                       |
| sphinx         | 617 ms                                                      | 697 ms: 1.13x slower                                                        |
| Geometric mean | (ref)                                                       | 1.10x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 205 ms: 1.37x faster                                                        |
| async_tree_io              | 513 ms                                                      | 388 ms: 1.32x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 382 ms: 1.30x faster                                                        |
| async_tree_none            | 219 ms                                                      | 174 ms: 1.26x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 215 ms: 1.23x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 164 ms: 1.22x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 368 ms: 1.04x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 372 ms: 1.02x faster                                                        |
| asyncio_websockets         | 300 ms                                                      | 319 ms: 1.06x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.7 ms: 1.09x slower                                                       |
| async_generators           | 223 ms                                                      | 251 ms: 1.13x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 67.5 ms: 1.02x slower                                                       |
| float          | 50.8 ms                                                     | 52.8 ms: 1.04x slower                                                       |
| pidigits       | 146 ms                                                      | 156 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 80.7 ms                                                     | 87.9 ms: 1.09x slower                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.88 ms: 1.11x slower                                                       |
| regex_dna      | 115 ms                                                      | 130 ms: 1.13x slower                                                        |
| Geometric mean | (ref)                                                       | 1.07x slower                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.38 sec: 1.01x slower                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 103 ms: 1.12x slower                                                        |
| xml_etree_iterparse  | 60.5 ms                                                     | 69.5 ms: 1.15x slower                                                       |
| unpickle_pure_python | 130 us                                                      | 154 us: 1.18x slower                                                        |
| pickle_pure_python   | 186 us                                                      | 222 us: 1.20x slower                                                        |
| xml_etree_generate   | 53.5 ms                                                     | 66.0 ms: 1.24x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 45.7 ms: 1.25x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 7.84 ms: 1.27x slower                                                       |
| json_loads           | 15.1 us                                                     | 19.3 us: 1.28x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.18x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.6 ms: 1.05x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 18.6 ms: 1.10x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.08x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 15.2 ms                                                     | 16.0 ms: 1.05x slower                                                       |
| django_template | 20.3 ms                                                     | 24.8 ms: 1.22x slower                                                       |
| mako            | 6.56 ms                                                     | 8.22 ms: 1.25x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.13x slower                                                                |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 561 us: 15.09x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 205 ms: 1.37x faster                                                        |
| async_tree_io              | 513 ms                                                      | 388 ms: 1.32x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 382 ms: 1.30x faster                                                        |
| async_tree_none            | 219 ms                                                      | 174 ms: 1.26x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 215 ms: 1.23x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 164 ms: 1.22x faster                                                        |
| deepcopy                   | 223 us                                                      | 184 us: 1.22x faster                                                        |
| deepcopy_memo              | 23.1 us                                                     | 20.7 us: 1.11x faster                                                       |
| generators                 | 19.0 ms                                                     | 17.2 ms: 1.10x faster                                                       |
| go                         | 84.7 ms                                                     | 78.2 ms: 1.08x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.93 us: 1.05x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 368 ms: 1.04x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 372 ms: 1.02x faster                                                        |
| shortest_path              | 355 ms                                                      | 351 ms: 1.01x faster                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.38 sec: 1.01x slower                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.63 ms: 1.01x slower                                                       |
| nbody                      | 66.3 ms                                                     | 67.5 ms: 1.02x slower                                                       |
| connected_components       | 320 ms                                                      | 326 ms: 1.02x slower                                                        |
| meteor_contest             | 72.0 ms                                                     | 73.6 ms: 1.02x slower                                                       |
| html5lib                   | 38.2 ms                                                     | 39.3 ms: 1.03x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 79.2 ms: 1.04x slower                                                       |
| float                      | 50.8 ms                                                     | 52.8 ms: 1.04x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 849 us: 1.05x slower                                                        |
| pycparser                  | 695 ms                                                      | 730 ms: 1.05x slower                                                        |
| genshi_text                | 15.2 ms                                                     | 16.0 ms: 1.05x slower                                                       |
| python_startup             | 24.4 ms                                                     | 25.6 ms: 1.05x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 42.2 ms: 1.05x slower                                                       |
| pathlib                    | 75.3 ms                                                     | 79.6 ms: 1.06x slower                                                       |
| pidigits                   | 146 ms                                                      | 156 ms: 1.06x slower                                                        |
| asyncio_websockets         | 300 ms                                                      | 319 ms: 1.06x slower                                                        |
| deltablue                  | 1.89 ms                                                     | 2.02 ms: 1.07x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.20 us: 1.07x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 91.5 ms: 1.07x slower                                                       |
| sympy_expand               | 286 ms                                                      | 308 ms: 1.08x slower                                                        |
| scimark_monte_carlo        | 40.7 ms                                                     | 44.0 ms: 1.08x slower                                                       |
| telco                      | 4.85 ms                                                     | 5.24 ms: 1.08x slower                                                       |
| sympy_str                  | 167 ms                                                      | 180 ms: 1.08x slower                                                        |
| logging_format             | 6.18 us                                                     | 6.68 us: 1.08x slower                                                       |
| spectral_norm              | 63.4 ms                                                     | 68.9 ms: 1.09x slower                                                       |
| regex_compile              | 80.7 ms                                                     | 87.9 ms: 1.09x slower                                                       |
| 2to3                       | 215 ms                                                      | 235 ms: 1.09x slower                                                        |
| pprint_pformat             | 977 ms                                                      | 1.07 sec: 1.09x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 529 ms: 1.09x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.7 ms: 1.09x slower                                                       |
| json                       | 3.30 ms                                                     | 3.61 ms: 1.09x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.5 ms: 1.10x slower                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.35 ms: 1.10x slower                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.75 us: 1.10x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 18.6 ms: 1.10x slower                                                       |
| sqlglot_parse              | 764 us                                                      | 845 us: 1.10x slower                                                        |
| coverage                   | 45.3 ms                                                     | 50.1 ms: 1.11x slower                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.88 ms: 1.11x slower                                                       |
| scimark_fft                | 175 ms                                                      | 195 ms: 1.11x slower                                                        |
| pyflate                    | 283 ms                                                      | 316 ms: 1.12x slower                                                        |
| bench_mp_pool              | 84.2 ms                                                     | 93.9 ms: 1.12x slower                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 103 ms: 1.12x slower                                                        |
| typing_runtime_protocols   | 103 us                                                      | 115 us: 1.12x slower                                                        |
| sqlglot_transpile          | 953 us                                                      | 1.07 ms: 1.12x slower                                                       |
| fannkuch                   | 252 ms                                                      | 283 ms: 1.12x slower                                                        |
| sqlglot_optimize           | 32.5 ms                                                     | 36.6 ms: 1.12x slower                                                       |
| async_generators           | 223 ms                                                      | 251 ms: 1.13x slower                                                        |
| regex_dna                  | 115 ms                                                      | 130 ms: 1.13x slower                                                        |
| sphinx                     | 617 ms                                                      | 697 ms: 1.13x slower                                                        |
| nqueens                    | 56.1 ms                                                     | 63.7 ms: 1.13x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.37 ms: 1.14x slower                                                       |
| richards_super             | 29.8 ms                                                     | 33.9 ms: 1.14x slower                                                       |
| richards                   | 26.3 ms                                                     | 30.1 ms: 1.15x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 3.30 sec: 1.15x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 69.5 ms: 1.15x slower                                                       |
| sqlglot_normalize          | 172 ms                                                      | 197 ms: 1.15x slower                                                        |
| docutils                   | 1.53 sec                                                    | 1.76 sec: 1.15x slower                                                      |
| raytrace                   | 153 ms                                                      | 177 ms: 1.15x slower                                                        |
| chaos                      | 37.9 ms                                                     | 43.9 ms: 1.16x slower                                                       |
| mdp                        | 1.43 sec                                                    | 1.67 sec: 1.17x slower                                                      |
| unpickle_pure_python       | 130 us                                                      | 154 us: 1.18x slower                                                        |
| scimark_lu                 | 56.7 ms                                                     | 67.7 ms: 1.19x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 222 us: 1.20x slower                                                        |
| crypto_pyaes               | 45.6 ms                                                     | 54.8 ms: 1.20x slower                                                       |
| comprehensions             | 10.4 us                                                     | 12.5 us: 1.20x slower                                                       |
| django_template            | 20.3 ms                                                     | 24.8 ms: 1.22x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 67.3 ns: 1.23x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 66.0 ms: 1.24x slower                                                       |
| mako                       | 6.56 ms                                                     | 8.22 ms: 1.25x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 45.7 ms: 1.25x slower                                                       |
| many_optionals             | 361 us                                                      | 454 us: 1.26x slower                                                        |
| json_dumps                 | 6.19 ms                                                     | 7.84 ms: 1.27x slower                                                       |
| json_loads                 | 15.1 us                                                     | 19.3 us: 1.28x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.54 ms: 1.29x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 16.2 ms: 1.50x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                                |

Benchmark hidden because not significant (4): regex_v8, k_core, pylint, genshi_xml
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http

- Geometric mean (including insignificant results): 1.038x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown