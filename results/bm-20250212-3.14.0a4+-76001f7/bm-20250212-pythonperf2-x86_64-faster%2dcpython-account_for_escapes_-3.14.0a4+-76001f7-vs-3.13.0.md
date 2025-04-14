# Results vs. 3.13.0

- fork: faster-cpython
- ref: account_for_escapes_
- machine: linux-x86_64
- commit hash: 76001f7
- commit date: 2025-02-12
- overall geometric mean: 1.054x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-76001f7 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 283 ms: 1.03x faster                                                                   |
| docutils       | 2.83 sec                                                     | 2.87 sec: 1.01x slower                                                                 |
| html5lib       | 73.5 ms                                                      | 67.4 ms: 1.09x faster                                                                  |
| sphinx         | 1.12 sec                                                     | 1.10 sec: 1.02x faster                                                                 |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-76001f7 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 341 ms: 1.37x faster                                                                   |
| async_tree_none            | 376 ms                                                       | 292 ms: 1.29x faster                                                                   |
| async_tree_io              | 843 ms                                                       | 656 ms: 1.29x faster                                                                   |
| async_tree_memoization     | 453 ms                                                       | 355 ms: 1.28x faster                                                                   |
| async_tree_io_tg           | 831 ms                                                       | 656 ms: 1.27x faster                                                                   |
| async_tree_none_tg         | 346 ms                                                       | 282 ms: 1.23x faster                                                                   |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 522 ms: 1.16x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 511 ms: 1.14x faster                                                                   |
| async_generators           | 457 ms                                                       | 408 ms: 1.12x faster                                                                   |
| asyncio_websockets         | 388 ms                                                       | 383 ms: 1.01x faster                                                                   |
| coroutines                 | 21.6 ms                                                      | 21.4 ms: 1.01x faster                                                                  |
| Geometric mean             | (ref)                                                        | 1.19x faster                                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-76001f7 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 70.1 ms: 1.16x faster                                                                  |
| pidigits       | 252 ms                                                       | 255 ms: 1.01x slower                                                                   |
| nbody          | 89.3 ms                                                      | 91.7 ms: 1.03x slower                                                                  |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-76001f7 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.08 ms: 1.19x faster                                                                  |
| regex_compile  | 143 ms                                                       | 135 ms: 1.05x faster                                                                   |
| regex_dna      | 247 ms                                                       | 238 ms: 1.04x faster                                                                   |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                           |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-76001f7 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.04 sec: 1.20x faster                                                                 |
| xml_etree_parse      | 150 ms                                                       | 140 ms: 1.07x faster                                                                   |
| xml_etree_iterparse  | 103 ms                                                       | 97.7 ms: 1.05x faster                                                                  |
| xml_etree_generate   | 86.5 ms                                                      | 84.2 ms: 1.03x faster                                                                  |
| unpickle_pure_python | 217 us                                                       | 213 us: 1.02x faster                                                                   |
| xml_etree_process    | 61.2 ms                                                      | 59.9 ms: 1.02x faster                                                                  |
| pickle_pure_python   | 323 us                                                       | 332 us: 1.03x slower                                                                   |
| json_dumps           | 11.1 ms                                                      | 11.7 ms: 1.05x slower                                                                  |
| json_loads           | 24.7 us                                                      | 26.4 us: 1.07x slower                                                                  |
| Geometric mean       | (ref)                                                        | 1.03x faster                                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-76001f7 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.96 ms                                                      | 9.03 ms: 1.01x slower                                                                  |
| python_startup         | 15.9 ms                                                      | 16.0 ms: 1.01x slower                                                                  |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-76001f7 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 24.1 ms: 1.09x faster                                                                  |
| genshi_xml      | 57.1 ms                                                      | 54.6 ms: 1.04x faster                                                                  |
| django_template | 36.4 ms                                                      | 35.7 ms: 1.02x faster                                                                  |
| mako            | 10.4 ms                                                      | 10.8 ms: 1.05x slower                                                                  |
| Geometric mean  | (ref)                                                        | 1.03x faster                                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-76001f7 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 341 ms: 1.37x faster                                                                   |
| deepcopy                   | 392 us                                                       | 293 us: 1.34x faster                                                                   |
| go                         | 162 ms                                                       | 126 ms: 1.29x faster                                                                   |
| async_tree_none            | 376 ms                                                       | 292 ms: 1.29x faster                                                                   |
| async_tree_io              | 843 ms                                                       | 656 ms: 1.29x faster                                                                   |
| async_tree_memoization     | 453 ms                                                       | 355 ms: 1.28x faster                                                                   |
| deepcopy_memo              | 38.6 us                                                      | 30.4 us: 1.27x faster                                                                  |
| async_tree_io_tg           | 831 ms                                                       | 656 ms: 1.27x faster                                                                   |
| async_tree_none_tg         | 346 ms                                                       | 282 ms: 1.23x faster                                                                   |
| tomli_loads                | 2.46 sec                                                     | 2.04 sec: 1.20x faster                                                                 |
| regex_effbot               | 3.67 ms                                                      | 3.08 ms: 1.19x faster                                                                  |
| deepcopy_reduce            | 3.54 us                                                      | 2.98 us: 1.19x faster                                                                  |
| float                      | 81.3 ms                                                      | 70.1 ms: 1.16x faster                                                                  |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 522 ms: 1.16x faster                                                                   |
| spectral_norm              | 97.0 ms                                                      | 84.1 ms: 1.15x faster                                                                  |
| pyflate                    | 503 ms                                                       | 439 ms: 1.15x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 511 ms: 1.14x faster                                                                   |
| generators                 | 33.6 ms                                                      | 29.8 ms: 1.13x faster                                                                  |
| richards_super             | 59.6 ms                                                      | 52.8 ms: 1.13x faster                                                                  |
| richards                   | 52.9 ms                                                      | 47.0 ms: 1.13x faster                                                                  |
| scimark_sor                | 123 ms                                                       | 110 ms: 1.12x faster                                                                   |
| async_generators           | 457 ms                                                       | 408 ms: 1.12x faster                                                                   |
| telco                      | 8.79 ms                                                      | 7.88 ms: 1.12x faster                                                                  |
| bpe_tokeniser              | 5.09 sec                                                     | 4.61 sec: 1.10x faster                                                                 |
| pylint                     | 347 ms                                                       | 316 ms: 1.10x faster                                                                   |
| scimark_monte_carlo        | 66.1 ms                                                      | 60.5 ms: 1.09x faster                                                                  |
| html5lib                   | 73.5 ms                                                      | 67.4 ms: 1.09x faster                                                                  |
| genshi_text                | 26.2 ms                                                      | 24.1 ms: 1.09x faster                                                                  |
| pathlib                    | 17.5 ms                                                      | 16.3 ms: 1.08x faster                                                                  |
| xml_etree_parse            | 150 ms                                                       | 140 ms: 1.07x faster                                                                   |
| hexiom                     | 6.55 ms                                                      | 6.16 ms: 1.06x faster                                                                  |
| pprint_safe_repr           | 843 ms                                                       | 795 ms: 1.06x faster                                                                   |
| scimark_fft                | 328 ms                                                       | 310 ms: 1.06x faster                                                                   |
| scimark_lu                 | 98.7 ms                                                      | 93.5 ms: 1.06x faster                                                                  |
| regex_compile              | 143 ms                                                       | 135 ms: 1.05x faster                                                                   |
| pprint_pformat             | 1.72 sec                                                     | 1.63 sec: 1.05x faster                                                                 |
| connected_components       | 432 ms                                                       | 411 ms: 1.05x faster                                                                   |
| xml_etree_iterparse        | 103 ms                                                       | 97.7 ms: 1.05x faster                                                                  |
| thrift                     | 901 us                                                       | 856 us: 1.05x faster                                                                   |
| json                       | 5.69 ms                                                      | 5.41 ms: 1.05x faster                                                                  |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.56 ms: 1.05x faster                                                                  |
| genshi_xml                 | 57.1 ms                                                      | 54.6 ms: 1.04x faster                                                                  |
| sqlalchemy_declarative     | 148 ms                                                       | 143 ms: 1.04x faster                                                                   |
| sympy_expand               | 509 ms                                                       | 491 ms: 1.04x faster                                                                   |
| regex_dna                  | 247 ms                                                       | 238 ms: 1.04x faster                                                                   |
| k_core                     | 2.17 sec                                                     | 2.09 sec: 1.04x faster                                                                 |
| shortest_path              | 460 ms                                                       | 445 ms: 1.03x faster                                                                   |
| 2to3                       | 293 ms                                                       | 283 ms: 1.03x faster                                                                   |
| sympy_str                  | 298 ms                                                       | 289 ms: 1.03x faster                                                                   |
| sqlite_synth               | 2.91 us                                                      | 2.82 us: 1.03x faster                                                                  |
| xml_etree_generate         | 86.5 ms                                                      | 84.2 ms: 1.03x faster                                                                  |
| sqlglot_optimize           | 59.3 ms                                                      | 57.7 ms: 1.03x faster                                                                  |
| sympy_sum                  | 155 ms                                                       | 151 ms: 1.03x faster                                                                   |
| meteor_contest             | 130 ms                                                       | 126 ms: 1.03x faster                                                                   |
| deltablue                  | 3.42 ms                                                      | 3.34 ms: 1.02x faster                                                                  |
| unpickle_pure_python       | 217 us                                                       | 213 us: 1.02x faster                                                                   |
| sphinx                     | 1.12 sec                                                     | 1.10 sec: 1.02x faster                                                                 |
| dulwich_log                | 68.2 ms                                                      | 66.7 ms: 1.02x faster                                                                  |
| mdp                        | 2.54 sec                                                     | 2.49 sec: 1.02x faster                                                                 |
| sqlalchemy_imperative      | 18.3 ms                                                      | 17.9 ms: 1.02x faster                                                                  |
| sympy_integrate            | 23.6 ms                                                      | 23.1 ms: 1.02x faster                                                                  |
| xml_etree_process          | 61.2 ms                                                      | 59.9 ms: 1.02x faster                                                                  |
| django_template            | 36.4 ms                                                      | 35.7 ms: 1.02x faster                                                                  |
| logging_silent             | 97.9 ns                                                      | 96.3 ns: 1.02x faster                                                                  |
| sqlglot_normalize          | 119 ms                                                       | 118 ms: 1.01x faster                                                                   |
| asyncio_websockets         | 388 ms                                                       | 383 ms: 1.01x faster                                                                   |
| sqlglot_parse              | 1.40 ms                                                      | 1.38 ms: 1.01x faster                                                                  |
| chaos                      | 60.2 ms                                                      | 59.4 ms: 1.01x faster                                                                  |
| coverage                   | 80.0 ms                                                      | 78.9 ms: 1.01x faster                                                                  |
| sqlglot_transpile          | 1.79 ms                                                      | 1.77 ms: 1.01x faster                                                                  |
| coroutines                 | 21.6 ms                                                      | 21.4 ms: 1.01x faster                                                                  |
| python_startup_no_site     | 8.96 ms                                                      | 9.03 ms: 1.01x slower                                                                  |
| python_startup             | 15.9 ms                                                      | 16.0 ms: 1.01x slower                                                                  |
| pidigits                   | 252 ms                                                       | 255 ms: 1.01x slower                                                                   |
| comprehensions             | 17.0 us                                                      | 17.3 us: 1.01x slower                                                                  |
| docutils                   | 2.83 sec                                                     | 2.87 sec: 1.01x slower                                                                 |
| fannkuch                   | 363 ms                                                       | 368 ms: 1.01x slower                                                                   |
| logging_simple             | 6.39 us                                                      | 6.54 us: 1.02x slower                                                                  |
| pycparser                  | 1.24 sec                                                     | 1.27 sec: 1.02x slower                                                                 |
| raytrace                   | 273 ms                                                       | 280 ms: 1.03x slower                                                                   |
| nbody                      | 89.3 ms                                                      | 91.7 ms: 1.03x slower                                                                  |
| pickle_pure_python         | 323 us                                                       | 332 us: 1.03x slower                                                                   |
| logging_format             | 6.94 us                                                      | 7.15 us: 1.03x slower                                                                  |
| mako                       | 10.4 ms                                                      | 10.8 ms: 1.05x slower                                                                  |
| create_gc_cycles           | 2.68 ms                                                      | 2.81 ms: 1.05x slower                                                                  |
| json_dumps                 | 11.1 ms                                                      | 11.7 ms: 1.05x slower                                                                  |
| json_loads                 | 24.7 us                                                      | 26.4 us: 1.07x slower                                                                  |
| many_optionals             | 930 us                                                       | 1.01 ms: 1.08x slower                                                                  |
| subparsers                 | 17.5 ms                                                      | 22.9 ms: 1.31x slower                                                                  |
| gc_traversal               | 4.74 ms                                                      | 6.52 ms: 1.38x slower                                                                  |
| bench_mp_pool              | 5.12 ms                                                      | 1.15 sec: 223.82x slower                                                               |
| Geometric mean             | (ref)                                                        | 1.00x slower                                                                           |

Benchmark hidden because not significant (5): regex_v8, bench_thread_pool, crypto_pyaes, nqueens, typing_runtime_protocols
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.054x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.02x