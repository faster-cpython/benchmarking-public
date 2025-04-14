# Results vs. 3.13.0

- fork: python
- ref: 6226edc48baa888b413f
- machine: linux-x86_64
- commit hash: 6226edc
- commit date: 2025-03-24
- overall geometric mean: 1.045x slower
- HPT reliability: 99.69%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.24x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250324-pythonperf2-x86_64-python-6226edc48baa888b413f-3.14.0a6+-6226edc |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 326 ms: 1.11x slower                                                         |
| docutils       | 2.83 sec                                                     | 2.91 sec: 1.03x slower                                                       |
| html5lib       | 73.5 ms                                                      | 72.8 ms: 1.01x faster                                                        |
| sphinx         | 1.12 sec                                                     | 1.17 sec: 1.04x slower                                                       |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250324-pythonperf2-x86_64-python-6226edc48baa888b413f-3.14.0a6+-6226edc |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 307 ms: 1.52x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 549 ms: 1.51x faster                                                         |
| async_tree_io              | 843 ms                                                       | 579 ms: 1.45x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 243 ms: 1.42x faster                                                         |
| async_tree_none            | 376 ms                                                       | 278 ms: 1.35x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 337 ms: 1.34x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 474 ms: 1.23x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 510 ms: 1.18x faster                                                         |
| asyncio_websockets         | 388 ms                                                       | 375 ms: 1.03x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 21.2 ms: 1.02x faster                                                        |
| async_generators           | 457 ms                                                       | 495 ms: 1.08x slower                                                         |
| Geometric mean             | (ref)                                                        | 1.26x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250324-pythonperf2-x86_64-python-6226edc48baa888b413f-3.14.0a6+-6226edc |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 77.0 ms: 1.06x faster                                                        |
| pidigits       | 252 ms                                                       | 249 ms: 1.01x faster                                                         |
| nbody          | 89.3 ms                                                      | 133 ms: 1.49x slower                                                         |
| Geometric mean | (ref)                                                        | 1.12x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250324-pythonperf2-x86_64-python-6226edc48baa888b413f-3.14.0a6+-6226edc |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.12 ms: 1.18x faster                                                        |
| regex_v8       | 26.1 ms                                                      | 25.2 ms: 1.04x faster                                                        |
| regex_dna      | 247 ms                                                       | 246 ms: 1.00x faster                                                         |
| regex_compile  | 143 ms                                                       | 161 ms: 1.13x slower                                                         |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250324-pythonperf2-x86_64-python-6226edc48baa888b413f-3.14.0a6+-6226edc |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 89.7 ms: 1.15x faster                                                        |
| xml_etree_parse      | 150 ms                                                       | 137 ms: 1.09x faster                                                         |
| tomli_loads          | 2.46 sec                                                     | 2.39 sec: 1.03x faster                                                       |
| unpickle_pure_python | 217 us                                                       | 244 us: 1.12x slower                                                         |
| xml_etree_generate   | 86.5 ms                                                      | 97.5 ms: 1.13x slower                                                        |
| pickle_pure_python   | 323 us                                                       | 367 us: 1.14x slower                                                         |
| xml_etree_process    | 61.2 ms                                                      | 70.0 ms: 1.14x slower                                                        |
| json_loads           | 24.7 us                                                      | 29.2 us: 1.18x slower                                                        |
| json_dumps           | 11.1 ms                                                      | 13.3 ms: 1.20x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.07x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250324-pythonperf2-x86_64-python-6226edc48baa888b413f-3.14.0a6+-6226edc |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 19.4 ms: 1.22x slower                                                        |
| python_startup_no_site | 8.96 ms                                                      | 13.8 ms: 1.54x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.37x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250324-pythonperf2-x86_64-python-6226edc48baa888b413f-3.14.0a6+-6226edc |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 57.1 ms                                                      | 62.8 ms: 1.10x slower                                                        |
| genshi_text     | 26.2 ms                                                      | 30.2 ms: 1.15x slower                                                        |
| django_template | 36.4 ms                                                      | 45.7 ms: 1.26x slower                                                        |
| mako            | 10.4 ms                                                      | 17.7 ms: 1.70x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.28x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250324-pythonperf2-x86_64-python-6226edc48baa888b413f-3.14.0a6+-6226edc |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| gc_traversal               | 4.74 ms                                                      | 2.10 ms: 2.25x faster                                                        |
| async_tree_memoization_tg  | 466 ms                                                       | 307 ms: 1.52x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 549 ms: 1.51x faster                                                         |
| async_tree_io              | 843 ms                                                       | 579 ms: 1.45x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 243 ms: 1.42x faster                                                         |
| create_gc_cycles           | 2.68 ms                                                      | 1.94 ms: 1.39x faster                                                        |
| async_tree_none            | 376 ms                                                       | 278 ms: 1.35x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 337 ms: 1.34x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 474 ms: 1.23x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 510 ms: 1.18x faster                                                         |
| deepcopy                   | 392 us                                                       | 333 us: 1.18x faster                                                         |
| regex_effbot               | 3.67 ms                                                      | 3.12 ms: 1.18x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 89.7 ms: 1.15x faster                                                        |
| sqlite_synth               | 2.91 us                                                      | 2.60 us: 1.12x faster                                                        |
| generators                 | 33.6 ms                                                      | 30.6 ms: 1.10x faster                                                        |
| xml_etree_parse            | 150 ms                                                       | 137 ms: 1.09x faster                                                         |
| deepcopy_memo              | 38.6 us                                                      | 36.2 us: 1.07x faster                                                        |
| go                         | 162 ms                                                       | 153 ms: 1.06x faster                                                         |
| float                      | 81.3 ms                                                      | 77.0 ms: 1.06x faster                                                        |
| dulwich_log                | 68.2 ms                                                      | 64.6 ms: 1.06x faster                                                        |
| regex_v8                   | 26.1 ms                                                      | 25.2 ms: 1.04x faster                                                        |
| asyncio_websockets         | 388 ms                                                       | 375 ms: 1.03x faster                                                         |
| tomli_loads                | 2.46 sec                                                     | 2.39 sec: 1.03x faster                                                       |
| scimark_sor                | 123 ms                                                       | 120 ms: 1.03x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 21.2 ms: 1.02x faster                                                        |
| pyflate                    | 503 ms                                                       | 495 ms: 1.02x faster                                                         |
| pidigits                   | 252 ms                                                       | 249 ms: 1.01x faster                                                         |
| html5lib                   | 73.5 ms                                                      | 72.8 ms: 1.01x faster                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 3.51 us: 1.01x faster                                                        |
| pathlib                    | 17.5 ms                                                      | 17.5 ms: 1.00x faster                                                        |
| regex_dna                  | 247 ms                                                       | 246 ms: 1.00x faster                                                         |
| spectral_norm              | 97.0 ms                                                      | 97.3 ms: 1.00x slower                                                        |
| pycparser                  | 1.24 sec                                                     | 1.25 sec: 1.01x slower                                                       |
| logging_silent             | 97.9 ns                                                      | 101 ns: 1.03x slower                                                         |
| docutils                   | 2.83 sec                                                     | 2.91 sec: 1.03x slower                                                       |
| bpe_tokeniser              | 5.09 sec                                                     | 5.31 sec: 1.04x slower                                                       |
| sphinx                     | 1.12 sec                                                     | 1.17 sec: 1.04x slower                                                       |
| scimark_fft                | 328 ms                                                       | 347 ms: 1.06x slower                                                         |
| pprint_safe_repr           | 843 ms                                                       | 904 ms: 1.07x slower                                                         |
| thrift                     | 901 us                                                       | 966 us: 1.07x slower                                                         |
| telco                      | 8.79 ms                                                      | 9.51 ms: 1.08x slower                                                        |
| richards                   | 52.9 ms                                                      | 57.3 ms: 1.08x slower                                                        |
| pprint_pformat             | 1.72 sec                                                     | 1.86 sec: 1.08x slower                                                       |
| async_generators           | 457 ms                                                       | 495 ms: 1.08x slower                                                         |
| mdp                        | 2.54 sec                                                     | 2.80 sec: 1.10x slower                                                       |
| genshi_xml                 | 57.1 ms                                                      | 62.8 ms: 1.10x slower                                                        |
| k_core                     | 2.17 sec                                                     | 2.39 sec: 1.10x slower                                                       |
| sympy_expand               | 509 ms                                                       | 564 ms: 1.11x slower                                                         |
| 2to3                       | 293 ms                                                       | 326 ms: 1.11x slower                                                         |
| sympy_str                  | 298 ms                                                       | 334 ms: 1.12x slower                                                         |
| richards_super             | 59.6 ms                                                      | 66.8 ms: 1.12x slower                                                        |
| unpickle_pure_python       | 217 us                                                       | 244 us: 1.12x slower                                                         |
| xml_etree_generate         | 86.5 ms                                                      | 97.5 ms: 1.13x slower                                                        |
| regex_compile              | 143 ms                                                       | 161 ms: 1.13x slower                                                         |
| sympy_integrate            | 23.6 ms                                                      | 26.6 ms: 1.13x slower                                                        |
| sympy_sum                  | 155 ms                                                       | 175 ms: 1.13x slower                                                         |
| sqlalchemy_imperative      | 18.3 ms                                                      | 20.7 ms: 1.13x slower                                                        |
| logging_simple             | 6.39 us                                                      | 7.24 us: 1.13x slower                                                        |
| hexiom                     | 6.55 ms                                                      | 7.44 ms: 1.14x slower                                                        |
| pickle_pure_python         | 323 us                                                       | 367 us: 1.14x slower                                                         |
| xml_etree_process          | 61.2 ms                                                      | 70.0 ms: 1.14x slower                                                        |
| chaos                      | 60.2 ms                                                      | 69.2 ms: 1.15x slower                                                        |
| genshi_text                | 26.2 ms                                                      | 30.2 ms: 1.15x slower                                                        |
| shortest_path              | 460 ms                                                       | 531 ms: 1.15x slower                                                         |
| connected_components       | 432 ms                                                       | 502 ms: 1.16x slower                                                         |
| logging_format             | 6.94 us                                                      | 8.07 us: 1.16x slower                                                        |
| sqlalchemy_declarative     | 148 ms                                                       | 173 ms: 1.16x slower                                                         |
| json_loads                 | 24.7 us                                                      | 29.2 us: 1.18x slower                                                        |
| deltablue                  | 3.42 ms                                                      | 4.05 ms: 1.18x slower                                                        |
| comprehensions             | 17.0 us                                                      | 20.2 us: 1.19x slower                                                        |
| meteor_contest             | 130 ms                                                       | 154 ms: 1.19x slower                                                         |
| many_optionals             | 930 us                                                       | 1.11 ms: 1.19x slower                                                        |
| json_dumps                 | 11.1 ms                                                      | 13.3 ms: 1.20x slower                                                        |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 5.73 ms: 1.20x slower                                                        |
| raytrace                   | 273 ms                                                       | 328 ms: 1.20x slower                                                         |
| nqueens                    | 90.7 ms                                                      | 110 ms: 1.21x slower                                                         |
| python_startup             | 15.9 ms                                                      | 19.4 ms: 1.22x slower                                                        |
| crypto_pyaes               | 73.3 ms                                                      | 91.9 ms: 1.25x slower                                                        |
| scimark_lu                 | 98.7 ms                                                      | 124 ms: 1.25x slower                                                         |
| django_template            | 36.4 ms                                                      | 45.7 ms: 1.26x slower                                                        |
| typing_runtime_protocols   | 169 us                                                       | 214 us: 1.27x slower                                                         |
| fannkuch                   | 363 ms                                                       | 473 ms: 1.30x slower                                                         |
| scimark_monte_carlo        | 66.1 ms                                                      | 86.7 ms: 1.31x slower                                                        |
| subparsers                 | 17.5 ms                                                      | 25.2 ms: 1.44x slower                                                        |
| nbody                      | 89.3 ms                                                      | 133 ms: 1.49x slower                                                         |
| coverage                   | 80.0 ms                                                      | 121 ms: 1.51x slower                                                         |
| bench_thread_pool          | 942 us                                                       | 1.44 ms: 1.53x slower                                                        |
| python_startup_no_site     | 8.96 ms                                                      | 13.8 ms: 1.54x slower                                                        |
| mako                       | 10.4 ms                                                      | 17.7 ms: 1.70x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 50.4 ms: 9.84x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.08x slower                                                                 |

Benchmark hidden because not significant (2): json, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250324-3.14.0a6+-6226edc-NOGIL/bm-20250324-pythonperf2-x86_64-python-6226edc48baa888b413f-3.14.0a6+-6226edc.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.045x slower

# HPT report

- Reliability score: 99.69% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.24x