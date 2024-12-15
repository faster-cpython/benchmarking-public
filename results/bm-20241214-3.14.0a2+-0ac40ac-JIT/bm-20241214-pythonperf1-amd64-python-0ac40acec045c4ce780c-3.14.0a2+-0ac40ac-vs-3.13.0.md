# Results vs. 3.13.0

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: windows-amd64
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.030x faster
- HPT reliability: 62.09%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 219 ms: 1.02x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.72 sec: 1.13x slower                                                      |
| html5lib       | 38.2 ms                                                     | 39.2 ms: 1.03x slower                                                       |
| sphinx         | 617 ms                                                      | 671 ms: 1.09x slower                                                        |
| Geometric mean | (ref)                                                       | 1.06x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 215 ms: 1.30x faster                                                        |
| async_tree_io              | 513 ms                                                      | 405 ms: 1.27x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 400 ms: 1.24x faster                                                        |
| async_tree_none            | 219 ms                                                      | 185 ms: 1.19x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 224 ms: 1.18x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 170 ms: 1.18x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 355 ms: 1.08x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 362 ms: 1.05x faster                                                        |
| asyncio_websockets         | 300 ms                                                      | 308 ms: 1.03x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.3 ms: 1.06x slower                                                       |
| async_generators           | 223 ms                                                      | 249 ms: 1.12x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.11x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 54.6 ms: 1.21x faster                                                       |
| float          | 50.8 ms                                                     | 43.8 ms: 1.16x faster                                                       |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.69 ms                                                     | 1.45 ms: 1.17x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 79.6 ms: 1.01x faster                                                       |
| regex_dna      | 115 ms                                                      | 116 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 130 us                                                      | 112 us: 1.16x faster                                                        |
| tomli_loads          | 1.37 sec                                                    | 1.21 sec: 1.13x faster                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 49.9 ms: 1.07x faster                                                       |
| xml_etree_parse      | 92.2 ms                                                     | 86.4 ms: 1.07x faster                                                       |
| json_loads           | 15.1 us                                                     | 14.2 us: 1.06x faster                                                       |
| xml_etree_process    | 36.5 ms                                                     | 35.3 ms: 1.03x faster                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 59.1 ms: 1.02x faster                                                       |
| json_dumps           | 6.19 ms                                                     | 6.30 ms: 1.02x slower                                                       |
| pickle_pure_python   | 186 us                                                      | 205 us: 1.10x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 23.3 ms: 1.05x faster                                                       |
| python_startup_no_site | 16.9 ms                                                     | 17.2 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.04 ms: 1.30x faster                                                       |
| genshi_text     | 15.2 ms                                                     | 18.5 ms: 1.21x slower                                                       |
| django_template | 20.3 ms                                                     | 27.0 ms: 1.33x slower                                                       |
| genshi_xml      | 33.9 ms                                                     | 46.9 ms: 1.38x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.14x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 516 us: 16.42x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 16.1 us: 1.43x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 46.9 ms: 1.35x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 215 ms: 1.30x faster                                                        |
| mako                       | 6.56 ms                                                     | 5.04 ms: 1.30x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.00 ms: 1.30x faster                                                       |
| async_tree_io              | 513 ms                                                      | 405 ms: 1.27x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 400 ms: 1.24x faster                                                        |
| scimark_fft                | 175 ms                                                      | 142 ms: 1.23x faster                                                        |
| scimark_sor                | 76.2 ms                                                     | 62.6 ms: 1.22x faster                                                       |
| nbody                      | 66.3 ms                                                     | 54.6 ms: 1.21x faster                                                       |
| deepcopy                   | 223 us                                                      | 186 us: 1.20x faster                                                        |
| async_tree_none            | 219 ms                                                      | 185 ms: 1.19x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 224 ms: 1.18x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 170 ms: 1.18x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.45 ms: 1.17x faster                                                       |
| unpickle_pure_python       | 130 us                                                      | 112 us: 1.16x faster                                                        |
| json                       | 3.30 ms                                                     | 2.84 ms: 1.16x faster                                                       |
| float                      | 50.8 ms                                                     | 43.8 ms: 1.16x faster                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 35.8 ms: 1.14x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.21 sec: 1.13x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.34 ms: 1.12x faster                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 41.0 ms: 1.11x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.83 us: 1.11x faster                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.62 sec: 1.10x faster                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 355 ms: 1.08x faster                                                        |
| k_core                     | 1.70 sec                                                    | 1.57 sec: 1.08x faster                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 49.9 ms: 1.07x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 86.4 ms: 1.07x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.2 us: 1.06x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 362 ms: 1.05x faster                                                        |
| python_startup             | 24.4 ms                                                     | 23.3 ms: 1.05x faster                                                       |
| connected_components       | 320 ms                                                      | 310 ms: 1.03x faster                                                        |
| xml_etree_process          | 36.5 ms                                                     | 35.3 ms: 1.03x faster                                                       |
| shortest_path              | 355 ms                                                      | 344 ms: 1.03x faster                                                        |
| bench_mp_pool              | 84.2 ms                                                     | 82.1 ms: 1.03x faster                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 59.1 ms: 1.02x faster                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.56 us: 1.02x faster                                                       |
| pprint_pformat             | 977 ms                                                      | 962 ms: 1.02x faster                                                        |
| regex_compile              | 80.7 ms                                                     | 79.6 ms: 1.01x faster                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.21 ms: 1.01x faster                                                       |
| coverage                   | 45.3 ms                                                     | 44.7 ms: 1.01x faster                                                       |
| fannkuch                   | 252 ms                                                      | 253 ms: 1.01x slower                                                        |
| pprint_safe_repr           | 485 ms                                                      | 489 ms: 1.01x slower                                                        |
| regex_dna                  | 115 ms                                                      | 116 ms: 1.01x slower                                                        |
| dulwich_log                | 40.1 ms                                                     | 40.6 ms: 1.01x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 6.30 ms: 1.02x slower                                                       |
| 2to3                       | 215 ms                                                      | 219 ms: 1.02x slower                                                        |
| python_startup_no_site     | 16.9 ms                                                     | 17.2 ms: 1.02x slower                                                       |
| html5lib                   | 38.2 ms                                                     | 39.2 ms: 1.03x slower                                                       |
| asyncio_websockets         | 300 ms                                                      | 308 ms: 1.03x slower                                                        |
| pycparser                  | 695 ms                                                      | 722 ms: 1.04x slower                                                        |
| go                         | 84.7 ms                                                     | 88.1 ms: 1.04x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 75.1 ms: 1.04x slower                                                       |
| sympy_str                  | 167 ms                                                      | 175 ms: 1.05x slower                                                        |
| sympy_expand               | 286 ms                                                      | 301 ms: 1.05x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.3 ms: 1.06x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 90.5 ms: 1.06x slower                                                       |
| mdp                        | 1.43 sec                                                    | 1.55 sec: 1.08x slower                                                      |
| logging_format             | 6.18 us                                                     | 6.70 us: 1.08x slower                                                       |
| sphinx                     | 617 ms                                                      | 671 ms: 1.09x slower                                                        |
| sqlglot_parse              | 764 us                                                      | 833 us: 1.09x slower                                                        |
| logging_simple             | 5.77 us                                                     | 6.29 us: 1.09x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.5 ms: 1.09x slower                                                       |
| chaos                      | 37.9 ms                                                     | 41.5 ms: 1.10x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 205 us: 1.10x slower                                                        |
| typing_runtime_protocols   | 103 us                                                      | 114 us: 1.10x slower                                                        |
| async_generators           | 223 ms                                                      | 249 ms: 1.12x slower                                                        |
| sqlglot_transpile          | 953 us                                                      | 1.07 ms: 1.13x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.72 sec: 1.13x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 64.0 ms: 1.14x slower                                                       |
| comprehensions             | 10.4 us                                                     | 11.8 us: 1.14x slower                                                       |
| sqlglot_optimize           | 32.5 ms                                                     | 37.2 ms: 1.14x slower                                                       |
| sqlglot_normalize          | 172 ms                                                      | 202 ms: 1.18x slower                                                        |
| deltablue                  | 1.89 ms                                                     | 2.26 ms: 1.20x slower                                                       |
| generators                 | 19.0 ms                                                     | 22.8 ms: 1.20x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 18.5 ms: 1.21x slower                                                       |
| many_optionals             | 361 us                                                      | 453 us: 1.25x slower                                                        |
| richards_super             | 29.8 ms                                                     | 38.0 ms: 1.27x slower                                                       |
| richards                   | 26.3 ms                                                     | 33.7 ms: 1.28x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.95 ms: 1.29x slower                                                       |
| django_template            | 20.3 ms                                                     | 27.0 ms: 1.33x slower                                                       |
| raytrace                   | 153 ms                                                      | 209 ms: 1.36x slower                                                        |
| genshi_xml                 | 33.9 ms                                                     | 46.9 ms: 1.38x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 16.1 ms: 1.48x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (9): regex_v8, pyflate, pidigits, scimark_lu, gc_traversal, logging_silent, pathlib, bench_thread_pool, pylint
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of results/bm-20241214-3.14.0a2+-0ac40ac-JIT/bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json: mypy2

- Geometric mean (including insignificant results): 1.030x faster

# HPT report

- Reliability score: 62.09% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown