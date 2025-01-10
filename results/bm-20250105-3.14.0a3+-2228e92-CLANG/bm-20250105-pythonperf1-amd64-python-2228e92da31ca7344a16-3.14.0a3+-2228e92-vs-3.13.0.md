# Results vs. 3.13.0

- fork: python
- ref: 2228e92da31ca7344a16
- machine: windows-amd64
- commit hash: 2228e92
- commit date: 2025-01-05
- overall geometric mean: 1.059x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 239 ms: 1.11x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.79 sec: 1.17x slower                                                      |
| html5lib       | 38.2 ms                                                     | 39.8 ms: 1.04x slower                                                       |
| sphinx         | 617 ms                                                      | 706 ms: 1.14x slower                                                        |
| Geometric mean | (ref)                                                       | 1.12x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 205 ms: 1.37x faster                                                        |
| async_tree_io              | 513 ms                                                      | 401 ms: 1.28x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 391 ms: 1.27x faster                                                        |
| async_tree_none            | 219 ms                                                      | 177 ms: 1.24x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 218 ms: 1.22x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 166 ms: 1.21x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 373 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 373 ms: 1.02x faster                                                        |
| asyncio_websockets         | 300 ms                                                      | 326 ms: 1.09x slower                                                        |
| async_generators           | 223 ms                                                      | 254 ms: 1.14x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 14.6 ms: 1.17x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.10x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 68.8 ms: 1.04x slower                                                       |
| pidigits       | 146 ms                                                      | 155 ms: 1.06x slower                                                        |
| float          | 50.8 ms                                                     | 55.1 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                       | 1.06x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 80.7 ms                                                     | 91.0 ms: 1.13x slower                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.98 ms: 1.17x slower                                                       |
| regex_dna      | 115 ms                                                      | 142 ms: 1.23x slower                                                        |
| Geometric mean | (ref)                                                       | 1.16x slower                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.40 sec: 1.02x slower                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 102 ms: 1.10x slower                                                        |
| xml_etree_iterparse  | 60.5 ms                                                     | 71.0 ms: 1.17x slower                                                       |
| unpickle_pure_python | 130 us                                                      | 159 us: 1.22x slower                                                        |
| pickle_pure_python   | 186 us                                                      | 228 us: 1.22x slower                                                        |
| json_dumps           | 6.19 ms                                                     | 7.79 ms: 1.26x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 67.6 ms: 1.26x slower                                                       |
| json_loads           | 15.1 us                                                     | 19.6 us: 1.30x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 47.3 ms: 1.30x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.20x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.6 ms: 1.05x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 19.0 ms: 1.12x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.08x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 15.2 ms                                                     | 16.2 ms: 1.07x slower                                                       |
| django_template | 20.3 ms                                                     | 25.7 ms: 1.27x slower                                                       |
| mako            | 6.56 ms                                                     | 8.55 ms: 1.30x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.15x slower                                                                |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 565 us: 14.97x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 205 ms: 1.37x faster                                                        |
| async_tree_io              | 513 ms                                                      | 401 ms: 1.28x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 391 ms: 1.27x faster                                                        |
| async_tree_none            | 219 ms                                                      | 177 ms: 1.24x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 218 ms: 1.22x faster                                                        |
| deepcopy                   | 223 us                                                      | 185 us: 1.21x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 166 ms: 1.21x faster                                                        |
| generators                 | 19.0 ms                                                     | 17.3 ms: 1.10x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 21.7 us: 1.06x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.95 us: 1.04x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 373 ms: 1.03x faster                                                        |
| go                         | 84.7 ms                                                     | 82.7 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 373 ms: 1.02x faster                                                        |
| shortest_path              | 355 ms                                                      | 352 ms: 1.01x faster                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.40 sec: 1.02x slower                                                      |
| connected_components       | 320 ms                                                      | 329 ms: 1.03x slower                                                        |
| nbody                      | 66.3 ms                                                     | 68.8 ms: 1.04x slower                                                       |
| html5lib                   | 38.2 ms                                                     | 39.8 ms: 1.04x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 75.4 ms: 1.05x slower                                                       |
| python_startup             | 24.4 ms                                                     | 25.6 ms: 1.05x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 42.3 ms: 1.05x slower                                                       |
| pidigits                   | 146 ms                                                      | 155 ms: 1.06x slower                                                        |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.76 ms: 1.06x slower                                                       |
| pathlib                    | 75.3 ms                                                     | 79.8 ms: 1.06x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 16.2 ms: 1.07x slower                                                       |
| telco                      | 4.85 ms                                                     | 5.18 ms: 1.07x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 92.0 ms: 1.08x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 82.5 ms: 1.08x slower                                                       |
| pycparser                  | 695 ms                                                      | 753 ms: 1.08x slower                                                        |
| float                      | 50.8 ms                                                     | 55.1 ms: 1.08x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 878 us: 1.08x slower                                                        |
| sqlite_synth               | 1.59 us                                                     | 1.72 us: 1.09x slower                                                       |
| asyncio_websockets         | 300 ms                                                      | 326 ms: 1.09x slower                                                        |
| sympy_str                  | 167 ms                                                      | 182 ms: 1.09x slower                                                        |
| sympy_expand               | 286 ms                                                      | 314 ms: 1.10x slower                                                        |
| xml_etree_parse            | 92.2 ms                                                     | 102 ms: 1.10x slower                                                        |
| logging_format             | 6.18 us                                                     | 6.82 us: 1.10x slower                                                       |
| scimark_fft                | 175 ms                                                      | 194 ms: 1.11x slower                                                        |
| logging_simple             | 5.77 us                                                     | 6.41 us: 1.11x slower                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.36 ms: 1.11x slower                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 93.5 ms: 1.11x slower                                                       |
| 2to3                       | 215 ms                                                      | 239 ms: 1.11x slower                                                        |
| json                       | 3.30 ms                                                     | 3.67 ms: 1.11x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.7 ms: 1.11x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 115 us: 1.12x slower                                                        |
| python_startup_no_site     | 16.9 ms                                                     | 19.0 ms: 1.12x slower                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 45.7 ms: 1.12x slower                                                       |
| regex_compile              | 80.7 ms                                                     | 91.0 ms: 1.13x slower                                                       |
| pprint_safe_repr           | 485 ms                                                      | 549 ms: 1.13x slower                                                        |
| deltablue                  | 1.89 ms                                                     | 2.15 ms: 1.13x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.11 sec: 1.14x slower                                                      |
| sqlglot_optimize           | 32.5 ms                                                     | 37.0 ms: 1.14x slower                                                       |
| sqlglot_parse              | 764 us                                                      | 871 us: 1.14x slower                                                        |
| async_generators           | 223 ms                                                      | 254 ms: 1.14x slower                                                        |
| sphinx                     | 617 ms                                                      | 706 ms: 1.14x slower                                                        |
| spectral_norm              | 63.4 ms                                                     | 73.1 ms: 1.15x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 64.8 ms: 1.15x slower                                                       |
| fannkuch                   | 252 ms                                                      | 291 ms: 1.16x slower                                                        |
| sqlglot_transpile          | 953 us                                                      | 1.10 ms: 1.16x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 3.34 sec: 1.16x slower                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.98 ms: 1.17x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.6 ms: 1.17x slower                                                       |
| coverage                   | 45.3 ms                                                     | 53.1 ms: 1.17x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.79 sec: 1.17x slower                                                      |
| mdp                        | 1.43 sec                                                    | 1.68 sec: 1.17x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 71.0 ms: 1.17x slower                                                       |
| pyflate                    | 283 ms                                                      | 332 ms: 1.17x slower                                                        |
| sqlglot_normalize          | 172 ms                                                      | 201 ms: 1.17x slower                                                        |
| richards_super             | 29.8 ms                                                     | 35.3 ms: 1.18x slower                                                       |
| raytrace                   | 153 ms                                                      | 182 ms: 1.18x slower                                                        |
| richards                   | 26.3 ms                                                     | 31.1 ms: 1.19x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.59 ms: 1.19x slower                                                       |
| chaos                      | 37.9 ms                                                     | 45.2 ms: 1.19x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 159 us: 1.22x slower                                                        |
| pickle_pure_python         | 186 us                                                      | 228 us: 1.22x slower                                                        |
| regex_dna                  | 115 ms                                                      | 142 ms: 1.23x slower                                                        |
| comprehensions             | 10.4 us                                                     | 12.9 us: 1.24x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 7.79 ms: 1.26x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 57.7 ms: 1.26x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 67.6 ms: 1.26x slower                                                       |
| django_template            | 20.3 ms                                                     | 25.7 ms: 1.27x slower                                                       |
| many_optionals             | 361 us                                                      | 460 us: 1.27x slower                                                        |
| scimark_lu                 | 56.7 ms                                                     | 72.3 ms: 1.28x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 70.2 ns: 1.29x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.54 ms: 1.29x slower                                                       |
| json_loads                 | 15.1 us                                                     | 19.6 us: 1.30x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 47.3 ms: 1.30x slower                                                       |
| mako                       | 6.56 ms                                                     | 8.55 ms: 1.30x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 16.5 ms: 1.52x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.07x slower                                                                |

Benchmark hidden because not significant (4): k_core, pylint, genshi_xml, regex_v8
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http

- Geometric mean (including insignificant results): 1.059x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.09x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: unknown