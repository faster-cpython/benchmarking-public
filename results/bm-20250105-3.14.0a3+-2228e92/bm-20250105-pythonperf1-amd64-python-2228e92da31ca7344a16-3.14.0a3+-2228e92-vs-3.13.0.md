# Results vs. 3.13.0

- fork: python
- ref: 2228e92da31ca7344a16
- machine: windows-amd64
- commit hash: 2228e92
- commit date: 2025-01-05
- overall geometric mean: 1.011x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 224 ms: 1.04x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.67 sec: 1.09x slower                                                      |
| html5lib       | 38.2 ms                                                     | 40.2 ms: 1.05x slower                                                       |
| sphinx         | 617 ms                                                      | 649 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                       | 1.06x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 210 ms: 1.34x faster                                                        |
| async_tree_io              | 513 ms                                                      | 404 ms: 1.27x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 401 ms: 1.24x faster                                                        |
| async_tree_none            | 219 ms                                                      | 182 ms: 1.21x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 224 ms: 1.18x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 172 ms: 1.16x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 347 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 350 ms: 1.09x faster                                                        |
| asyncio_websockets         | 300 ms                                                      | 310 ms: 1.03x slower                                                        |
| async_generators           | 223 ms                                                      | 238 ms: 1.07x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.4 ms: 1.07x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 53.0 ms: 1.04x slower                                                       |
| nbody          | 66.3 ms                                                     | 77.0 ms: 1.16x slower                                                       |
| Geometric mean | (ref)                                                       | 1.07x slower                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.69 ms                                                     | 1.47 ms: 1.15x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 87.5 ms: 1.08x slower                                                       |
| regex_dna      | 115 ms                                                      | 127 ms: 1.10x slower                                                        |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 87.5 ms: 1.05x faster                                                       |
| json_loads           | 15.1 us                                                     | 14.5 us: 1.04x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.39 sec: 1.02x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 62.7 ms: 1.04x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 57.4 ms: 1.07x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 6.70 ms: 1.08x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 40.2 ms: 1.10x slower                                                       |
| unpickle_pure_python | 130 us                                                      | 148 us: 1.14x slower                                                        |
| pickle_pure_python   | 186 us                                                      | 221 us: 1.19x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.06x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 23.1 ms: 1.05x faster                                                       |
| python_startup_no_site | 16.9 ms                                                     | 17.2 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.87 ms: 1.05x slower                                                       |
| genshi_text     | 15.2 ms                                                     | 16.7 ms: 1.10x slower                                                       |
| django_template | 20.3 ms                                                     | 24.8 ms: 1.22x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.09x slower                                                                |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 524 us: 16.14x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 210 ms: 1.34x faster                                                        |
| async_tree_io              | 513 ms                                                      | 404 ms: 1.27x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 401 ms: 1.24x faster                                                        |
| deepcopy                   | 223 us                                                      | 184 us: 1.21x faster                                                        |
| async_tree_none            | 219 ms                                                      | 182 ms: 1.21x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 224 ms: 1.18x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 172 ms: 1.16x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.47 ms: 1.15x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 20.8 us: 1.11x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 347 ms: 1.10x faster                                                        |
| json                       | 3.30 ms                                                     | 3.01 ms: 1.10x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 350 ms: 1.09x faster                                                        |
| deepcopy_reduce            | 2.02 us                                                     | 1.89 us: 1.07x faster                                                       |
| python_startup             | 24.4 ms                                                     | 23.1 ms: 1.05x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 87.5 ms: 1.05x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.5 us: 1.04x faster                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 82.5 ms: 1.02x faster                                                       |
| shortest_path              | 355 ms                                                      | 349 ms: 1.02x faster                                                        |
| create_gc_cycles           | 1.22 ms                                                     | 1.21 ms: 1.01x faster                                                       |
| connected_components       | 320 ms                                                      | 316 ms: 1.01x faster                                                        |
| telco                      | 4.85 ms                                                     | 4.82 ms: 1.01x faster                                                       |
| mdp                        | 1.43 sec                                                    | 1.43 sec: 1.00x faster                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.60 ms: 1.00x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 64.1 ms: 1.01x slower                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.61 us: 1.01x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.39 sec: 1.02x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 17.2 ms: 1.02x slower                                                       |
| pathlib                    | 75.3 ms                                                     | 76.6 ms: 1.02x slower                                                       |
| coverage                   | 45.3 ms                                                     | 46.5 ms: 1.03x slower                                                       |
| go                         | 84.7 ms                                                     | 87.2 ms: 1.03x slower                                                       |
| asyncio_websockets         | 300 ms                                                      | 310 ms: 1.03x slower                                                        |
| xml_etree_iterparse        | 60.5 ms                                                     | 62.7 ms: 1.04x slower                                                       |
| 2to3                       | 215 ms                                                      | 224 ms: 1.04x slower                                                        |
| float                      | 50.8 ms                                                     | 53.0 ms: 1.04x slower                                                       |
| mako                       | 6.56 ms                                                     | 6.87 ms: 1.05x slower                                                       |
| sphinx                     | 617 ms                                                      | 649 ms: 1.05x slower                                                        |
| html5lib                   | 38.2 ms                                                     | 40.2 ms: 1.05x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 3.03 sec: 1.05x slower                                                      |
| fannkuch                   | 252 ms                                                      | 266 ms: 1.06x slower                                                        |
| crypto_pyaes               | 45.6 ms                                                     | 48.2 ms: 1.06x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 90.2 ms: 1.06x slower                                                       |
| sympy_str                  | 167 ms                                                      | 177 ms: 1.06x slower                                                        |
| dulwich_log                | 40.1 ms                                                     | 42.7 ms: 1.07x slower                                                       |
| sympy_expand               | 286 ms                                                      | 305 ms: 1.07x slower                                                        |
| pycparser                  | 695 ms                                                      | 742 ms: 1.07x slower                                                        |
| meteor_contest             | 72.0 ms                                                     | 77.0 ms: 1.07x slower                                                       |
| async_generators           | 223 ms                                                      | 238 ms: 1.07x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.4 ms: 1.07x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 57.4 ms: 1.07x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 6.70 ms: 1.08x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.4 ms: 1.08x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 61.5 ms: 1.08x slower                                                       |
| regex_compile              | 80.7 ms                                                     | 87.5 ms: 1.08x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 112 us: 1.09x slower                                                        |
| docutils                   | 1.53 sec                                                    | 1.67 sec: 1.09x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 531 ms: 1.10x slower                                                        |
| genshi_text                | 15.2 ms                                                     | 16.7 ms: 1.10x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.07 sec: 1.10x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 40.2 ms: 1.10x slower                                                       |
| sqlglot_optimize           | 32.5 ms                                                     | 35.9 ms: 1.10x slower                                                       |
| regex_dna                  | 115 ms                                                      | 127 ms: 1.10x slower                                                        |
| scimark_fft                | 175 ms                                                      | 193 ms: 1.10x slower                                                        |
| logging_simple             | 5.77 us                                                     | 6.38 us: 1.11x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 62.2 ms: 1.11x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.27 ms: 1.11x slower                                                       |
| generators                 | 19.0 ms                                                     | 21.1 ms: 1.11x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.89 us: 1.12x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 61.6 ns: 1.13x slower                                                       |
| richards                   | 26.3 ms                                                     | 29.7 ms: 1.13x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 148 us: 1.14x slower                                                        |
| sqlglot_normalize          | 172 ms                                                      | 196 ms: 1.14x slower                                                        |
| richards_super             | 29.8 ms                                                     | 34.1 ms: 1.14x slower                                                       |
| chaos                      | 37.9 ms                                                     | 43.5 ms: 1.15x slower                                                       |
| comprehensions             | 10.4 us                                                     | 11.9 us: 1.15x slower                                                       |
| pyflate                    | 283 ms                                                      | 326 ms: 1.15x slower                                                        |
| sqlglot_transpile          | 953 us                                                      | 1.11 ms: 1.16x slower                                                       |
| nbody                      | 66.3 ms                                                     | 77.0 ms: 1.16x slower                                                       |
| sqlglot_parse              | 764 us                                                      | 889 us: 1.16x slower                                                        |
| scimark_monte_carlo        | 40.7 ms                                                     | 47.8 ms: 1.17x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 90.3 ms: 1.19x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 221 us: 1.19x slower                                                        |
| deltablue                  | 1.89 ms                                                     | 2.26 ms: 1.19x slower                                                       |
| many_optionals             | 361 us                                                      | 437 us: 1.21x slower                                                        |
| django_template            | 20.3 ms                                                     | 24.8 ms: 1.22x slower                                                       |
| raytrace                   | 153 ms                                                      | 193 ms: 1.26x slower                                                        |
| subparsers                 | 10.9 ms                                                     | 16.2 ms: 1.50x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (7): pylint, k_core, pidigits, gc_traversal, bench_thread_pool, genshi_xml, regex_v8
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of results/bm-20250105-3.14.0a3+-2228e92/bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92.json: mypy2

- Geometric mean (including insignificant results): 1.011x slower

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: unknown