# Results vs. 3.13.0

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: windows-amd64
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.018x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 223 ms: 1.04x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.66 sec: 1.08x slower                                                      |
| html5lib       | 38.2 ms                                                     | 40.6 ms: 1.06x slower                                                       |
| sphinx         | 617 ms                                                      | 652 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                       | 1.06x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 215 ms: 1.30x faster                                                        |
| async_tree_io              | 513 ms                                                      | 415 ms: 1.24x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 411 ms: 1.21x faster                                                        |
| async_tree_none            | 219 ms                                                      | 184 ms: 1.19x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 227 ms: 1.16x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 175 ms: 1.14x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 356 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 356 ms: 1.07x faster                                                        |
| asyncio_websockets         | 300 ms                                                      | 312 ms: 1.04x slower                                                        |
| async_generators           | 223 ms                                                      | 238 ms: 1.07x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.4 ms: 1.07x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.10x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 146 ms                                                      | 148 ms: 1.01x slower                                                        |
| float          | 50.8 ms                                                     | 54.4 ms: 1.07x slower                                                       |
| nbody          | 66.3 ms                                                     | 79.5 ms: 1.20x slower                                                       |
| Geometric mean | (ref)                                                       | 1.09x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.69 ms                                                     | 1.40 ms: 1.21x faster                                                       |
| regex_dna      | 115 ms                                                      | 111 ms: 1.03x faster                                                        |
| regex_compile  | 80.7 ms                                                     | 89.2 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 87.8 ms: 1.05x faster                                                       |
| json_loads           | 15.1 us                                                     | 14.4 us: 1.05x faster                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.0 ms: 1.04x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 57.5 ms: 1.07x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 6.73 ms: 1.09x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.54 sec: 1.12x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 41.3 ms: 1.13x slower                                                       |
| unpickle_pure_python | 130 us                                                      | 147 us: 1.13x slower                                                        |
| pickle_pure_python   | 186 us                                                      | 222 us: 1.19x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 23.2 ms: 1.05x faster                                                       |
| python_startup_no_site | 16.9 ms                                                     | 17.4 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.76 ms: 1.03x slower                                                       |
| genshi_xml      | 33.9 ms                                                     | 37.1 ms: 1.10x slower                                                       |
| genshi_text     | 15.2 ms                                                     | 17.2 ms: 1.13x slower                                                       |
| django_template | 20.3 ms                                                     | 24.9 ms: 1.23x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.12x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 522 us: 16.23x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 215 ms: 1.30x faster                                                        |
| async_tree_io              | 513 ms                                                      | 415 ms: 1.24x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.40 ms: 1.21x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 411 ms: 1.21x faster                                                        |
| deepcopy                   | 223 us                                                      | 187 us: 1.20x faster                                                        |
| async_tree_none            | 219 ms                                                      | 184 ms: 1.19x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 227 ms: 1.16x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 175 ms: 1.14x faster                                                        |
| json                       | 3.30 ms                                                     | 2.96 ms: 1.11x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 21.1 us: 1.09x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 356 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 356 ms: 1.07x faster                                                        |
| deepcopy_reduce            | 2.02 us                                                     | 1.92 us: 1.05x faster                                                       |
| python_startup             | 24.4 ms                                                     | 23.2 ms: 1.05x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 87.8 ms: 1.05x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.4 us: 1.05x faster                                                       |
| regex_dna                  | 115 ms                                                      | 111 ms: 1.03x faster                                                        |
| bench_mp_pool              | 84.2 ms                                                     | 81.9 ms: 1.03x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 62.0 ms: 1.02x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.76 ms: 1.02x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.57 ms: 1.01x faster                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.21 ms: 1.01x faster                                                       |
| pidigits                   | 146 ms                                                      | 148 ms: 1.01x slower                                                        |
| shortest_path              | 355 ms                                                      | 360 ms: 1.01x slower                                                        |
| sqlite_synth               | 1.59 us                                                     | 1.61 us: 1.01x slower                                                       |
| connected_components       | 320 ms                                                      | 327 ms: 1.02x slower                                                        |
| python_startup_no_site     | 16.9 ms                                                     | 17.4 ms: 1.03x slower                                                       |
| mako                       | 6.56 ms                                                     | 6.76 ms: 1.03x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.97 sec: 1.03x slower                                                      |
| 2to3                       | 215 ms                                                      | 223 ms: 1.04x slower                                                        |
| go                         | 84.7 ms                                                     | 88.0 ms: 1.04x slower                                                       |
| asyncio_websockets         | 300 ms                                                      | 312 ms: 1.04x slower                                                        |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.0 ms: 1.04x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 89.2 ms: 1.05x slower                                                       |
| sympy_str                  | 167 ms                                                      | 176 ms: 1.05x slower                                                        |
| sphinx                     | 617 ms                                                      | 652 ms: 1.06x slower                                                        |
| sympy_expand               | 286 ms                                                      | 302 ms: 1.06x slower                                                        |
| coverage                   | 45.3 ms                                                     | 48.0 ms: 1.06x slower                                                       |
| pycparser                  | 695 ms                                                      | 737 ms: 1.06x slower                                                        |
| html5lib                   | 38.2 ms                                                     | 40.6 ms: 1.06x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 42.9 ms: 1.07x slower                                                       |
| async_generators           | 223 ms                                                      | 238 ms: 1.07x slower                                                        |
| float                      | 50.8 ms                                                     | 54.4 ms: 1.07x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.4 ms: 1.07x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 57.5 ms: 1.07x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 77.5 ms: 1.08x slower                                                       |
| fannkuch                   | 252 ms                                                      | 271 ms: 1.08x slower                                                        |
| scimark_fft                | 175 ms                                                      | 189 ms: 1.08x slower                                                        |
| sympy_integrate            | 12.3 ms                                                     | 13.3 ms: 1.08x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.66 sec: 1.08x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 61.5 ms: 1.08x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 49.4 ms: 1.08x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 6.73 ms: 1.09x slower                                                       |
| genshi_xml                 | 33.9 ms                                                     | 37.1 ms: 1.10x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 114 us: 1.10x slower                                                        |
| sqlglot_optimize           | 32.5 ms                                                     | 35.9 ms: 1.10x slower                                                       |
| regex_compile              | 80.7 ms                                                     | 89.2 ms: 1.10x slower                                                       |
| pyflate                    | 283 ms                                                      | 313 ms: 1.10x slower                                                        |
| logging_format             | 6.18 us                                                     | 6.86 us: 1.11x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.42 us: 1.11x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 60.8 ns: 1.11x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 62.8 ms: 1.12x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.31 ms: 1.12x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.54 sec: 1.12x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 41.3 ms: 1.13x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 17.2 ms: 1.13x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 147 us: 1.13x slower                                                        |
| sqlglot_normalize          | 172 ms                                                      | 195 ms: 1.14x slower                                                        |
| pprint_pformat             | 977 ms                                                      | 1.11 sec: 1.14x slower                                                      |
| scimark_sor                | 76.2 ms                                                     | 87.1 ms: 1.14x slower                                                       |
| pprint_safe_repr           | 485 ms                                                      | 556 ms: 1.15x slower                                                        |
| comprehensions             | 10.4 us                                                     | 12.0 us: 1.15x slower                                                       |
| chaos                      | 37.9 ms                                                     | 43.9 ms: 1.16x slower                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 47.2 ms: 1.16x slower                                                       |
| sqlglot_transpile          | 953 us                                                      | 1.11 ms: 1.16x slower                                                       |
| sqlglot_parse              | 764 us                                                      | 891 us: 1.17x slower                                                        |
| generators                 | 19.0 ms                                                     | 22.2 ms: 1.17x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 222 us: 1.19x slower                                                        |
| deltablue                  | 1.89 ms                                                     | 2.26 ms: 1.19x slower                                                       |
| nbody                      | 66.3 ms                                                     | 79.5 ms: 1.20x slower                                                       |
| richards_super             | 29.8 ms                                                     | 36.2 ms: 1.22x slower                                                       |
| richards                   | 26.3 ms                                                     | 32.0 ms: 1.22x slower                                                       |
| many_optionals             | 361 us                                                      | 441 us: 1.22x slower                                                        |
| django_template            | 20.3 ms                                                     | 24.9 ms: 1.23x slower                                                       |
| raytrace                   | 153 ms                                                      | 191 ms: 1.25x slower                                                        |
| subparsers                 | 10.9 ms                                                     | 16.1 ms: 1.48x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                                |

Benchmark hidden because not significant (7): pylint, k_core, mdp, pathlib, gc_traversal, bench_thread_pool, regex_v8
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json: mypy2

- Geometric mean (including insignificant results): 1.018x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown