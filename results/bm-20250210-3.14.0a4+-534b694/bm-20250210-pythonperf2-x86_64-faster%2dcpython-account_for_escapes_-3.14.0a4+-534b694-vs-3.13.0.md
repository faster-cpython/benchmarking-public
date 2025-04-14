# Results vs. 3.13.0

- fork: faster-cpython
- ref: account_for_escapes_
- machine: linux-x86_64
- commit hash: 534b694
- commit date: 2025-02-10
- overall geometric mean: 1.060x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-534b694 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 283 ms: 1.03x faster                                                                   |
| docutils       | 2.83 sec                                                     | 2.87 sec: 1.02x slower                                                                 |
| html5lib       | 73.5 ms                                                      | 68.0 ms: 1.08x faster                                                                  |
| sphinx         | 1.12 sec                                                     | 1.10 sec: 1.02x faster                                                                 |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-534b694 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 338 ms: 1.38x faster                                                                   |
| async_tree_io              | 843 ms                                                       | 649 ms: 1.30x faster                                                                   |
| async_tree_none            | 376 ms                                                       | 290 ms: 1.30x faster                                                                   |
| async_tree_memoization     | 453 ms                                                       | 354 ms: 1.28x faster                                                                   |
| async_tree_io_tg           | 831 ms                                                       | 650 ms: 1.28x faster                                                                   |
| async_tree_none_tg         | 346 ms                                                       | 278 ms: 1.25x faster                                                                   |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 521 ms: 1.16x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 508 ms: 1.15x faster                                                                   |
| async_generators           | 457 ms                                                       | 413 ms: 1.11x faster                                                                   |
| coroutines                 | 21.6 ms                                                      | 21.1 ms: 1.02x faster                                                                  |
| Geometric mean             | (ref)                                                        | 1.20x faster                                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-534b694 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 70.3 ms: 1.16x faster                                                                  |
| pidigits       | 252 ms                                                       | 255 ms: 1.01x slower                                                                   |
| nbody          | 89.3 ms                                                      | 90.8 ms: 1.02x slower                                                                  |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-534b694 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.15 ms: 1.17x faster                                                                  |
| regex_compile  | 143 ms                                                       | 135 ms: 1.06x faster                                                                   |
| regex_dna      | 247 ms                                                       | 242 ms: 1.02x faster                                                                   |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                           |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-534b694 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.08 sec: 1.18x faster                                                                 |
| xml_etree_parse      | 150 ms                                                       | 134 ms: 1.12x faster                                                                   |
| xml_etree_iterparse  | 103 ms                                                       | 94.8 ms: 1.08x faster                                                                  |
| xml_etree_generate   | 86.5 ms                                                      | 83.7 ms: 1.03x faster                                                                  |
| unpickle_pure_python | 217 us                                                       | 212 us: 1.02x faster                                                                   |
| xml_etree_process    | 61.2 ms                                                      | 60.0 ms: 1.02x faster                                                                  |
| pickle_pure_python   | 323 us                                                       | 330 us: 1.02x slower                                                                   |
| json_dumps           | 11.1 ms                                                      | 11.7 ms: 1.05x slower                                                                  |
| json_loads           | 24.7 us                                                      | 26.7 us: 1.08x slower                                                                  |
| Geometric mean       | (ref)                                                        | 1.03x faster                                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-534b694 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.96 ms                                                      | 9.00 ms: 1.01x slower                                                                  |
| python_startup         | 15.9 ms                                                      | 16.0 ms: 1.01x slower                                                                  |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-534b694 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 23.9 ms: 1.10x faster                                                                  |
| genshi_xml      | 57.1 ms                                                      | 55.4 ms: 1.03x faster                                                                  |
| django_template | 36.4 ms                                                      | 35.8 ms: 1.01x faster                                                                  |
| mako            | 10.4 ms                                                      | 11.0 ms: 1.06x slower                                                                  |
| Geometric mean  | (ref)                                                        | 1.02x faster                                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-534b694 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| deepcopy                   | 392 us                                                       | 280 us: 1.40x faster                                                                   |
| async_tree_memoization_tg  | 466 ms                                                       | 338 ms: 1.38x faster                                                                   |
| deepcopy_memo              | 38.6 us                                                      | 29.1 us: 1.33x faster                                                                  |
| async_tree_io              | 843 ms                                                       | 649 ms: 1.30x faster                                                                   |
| async_tree_none            | 376 ms                                                       | 290 ms: 1.30x faster                                                                   |
| go                         | 162 ms                                                       | 127 ms: 1.28x faster                                                                   |
| async_tree_memoization     | 453 ms                                                       | 354 ms: 1.28x faster                                                                   |
| async_tree_io_tg           | 831 ms                                                       | 650 ms: 1.28x faster                                                                   |
| async_tree_none_tg         | 346 ms                                                       | 278 ms: 1.25x faster                                                                   |
| deepcopy_reduce            | 3.54 us                                                      | 2.92 us: 1.21x faster                                                                  |
| tomli_loads                | 2.46 sec                                                     | 2.08 sec: 1.18x faster                                                                 |
| pyflate                    | 503 ms                                                       | 426 ms: 1.18x faster                                                                   |
| regex_effbot               | 3.67 ms                                                      | 3.15 ms: 1.17x faster                                                                  |
| richards                   | 52.9 ms                                                      | 45.4 ms: 1.17x faster                                                                  |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 521 ms: 1.16x faster                                                                   |
| spectral_norm              | 97.0 ms                                                      | 83.7 ms: 1.16x faster                                                                  |
| float                      | 81.3 ms                                                      | 70.3 ms: 1.16x faster                                                                  |
| generators                 | 33.6 ms                                                      | 29.3 ms: 1.15x faster                                                                  |
| richards_super             | 59.6 ms                                                      | 51.9 ms: 1.15x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 508 ms: 1.15x faster                                                                   |
| scimark_sor                | 123 ms                                                       | 108 ms: 1.15x faster                                                                   |
| telco                      | 8.79 ms                                                      | 7.76 ms: 1.13x faster                                                                  |
| xml_etree_parse            | 150 ms                                                       | 134 ms: 1.12x faster                                                                   |
| bpe_tokeniser              | 5.09 sec                                                     | 4.55 sec: 1.12x faster                                                                 |
| pylint                     | 347 ms                                                       | 313 ms: 1.11x faster                                                                   |
| async_generators           | 457 ms                                                       | 413 ms: 1.11x faster                                                                   |
| genshi_text                | 26.2 ms                                                      | 23.9 ms: 1.10x faster                                                                  |
| xml_etree_iterparse        | 103 ms                                                       | 94.8 ms: 1.08x faster                                                                  |
| html5lib                   | 73.5 ms                                                      | 68.0 ms: 1.08x faster                                                                  |
| pprint_safe_repr           | 843 ms                                                       | 780 ms: 1.08x faster                                                                   |
| pathlib                    | 17.5 ms                                                      | 16.3 ms: 1.08x faster                                                                  |
| pprint_pformat             | 1.72 sec                                                     | 1.60 sec: 1.07x faster                                                                 |
| thrift                     | 901 us                                                       | 841 us: 1.07x faster                                                                   |
| scimark_fft                | 328 ms                                                       | 306 ms: 1.07x faster                                                                   |
| hexiom                     | 6.55 ms                                                      | 6.16 ms: 1.06x faster                                                                  |
| regex_compile              | 143 ms                                                       | 135 ms: 1.06x faster                                                                   |
| meteor_contest             | 130 ms                                                       | 123 ms: 1.05x faster                                                                   |
| json                       | 5.69 ms                                                      | 5.43 ms: 1.05x faster                                                                  |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.56 ms: 1.05x faster                                                                  |
| scimark_monte_carlo        | 66.1 ms                                                      | 63.3 ms: 1.05x faster                                                                  |
| scimark_lu                 | 98.7 ms                                                      | 94.5 ms: 1.04x faster                                                                  |
| sqlalchemy_declarative     | 148 ms                                                       | 142 ms: 1.04x faster                                                                   |
| connected_components       | 432 ms                                                       | 416 ms: 1.04x faster                                                                   |
| k_core                     | 2.17 sec                                                     | 2.09 sec: 1.04x faster                                                                 |
| sqlite_synth               | 2.91 us                                                      | 2.80 us: 1.04x faster                                                                  |
| xml_etree_generate         | 86.5 ms                                                      | 83.7 ms: 1.03x faster                                                                  |
| sqlglot_optimize           | 59.3 ms                                                      | 57.3 ms: 1.03x faster                                                                  |
| 2to3                       | 293 ms                                                       | 283 ms: 1.03x faster                                                                   |
| shortest_path              | 460 ms                                                       | 446 ms: 1.03x faster                                                                   |
| sqlalchemy_imperative      | 18.3 ms                                                      | 17.7 ms: 1.03x faster                                                                  |
| sympy_expand               | 509 ms                                                       | 494 ms: 1.03x faster                                                                   |
| sympy_str                  | 298 ms                                                       | 290 ms: 1.03x faster                                                                   |
| genshi_xml                 | 57.1 ms                                                      | 55.4 ms: 1.03x faster                                                                  |
| sqlglot_parse              | 1.40 ms                                                      | 1.36 ms: 1.03x faster                                                                  |
| sqlglot_normalize          | 119 ms                                                       | 116 ms: 1.03x faster                                                                   |
| unpickle_pure_python       | 217 us                                                       | 212 us: 1.02x faster                                                                   |
| sympy_integrate            | 23.6 ms                                                      | 23.0 ms: 1.02x faster                                                                  |
| sqlglot_transpile          | 1.79 ms                                                      | 1.75 ms: 1.02x faster                                                                  |
| logging_simple             | 6.39 us                                                      | 6.26 us: 1.02x faster                                                                  |
| coroutines                 | 21.6 ms                                                      | 21.1 ms: 1.02x faster                                                                  |
| xml_etree_process          | 61.2 ms                                                      | 60.0 ms: 1.02x faster                                                                  |
| deltablue                  | 3.42 ms                                                      | 3.35 ms: 1.02x faster                                                                  |
| regex_dna                  | 247 ms                                                       | 242 ms: 1.02x faster                                                                   |
| sphinx                     | 1.12 sec                                                     | 1.10 sec: 1.02x faster                                                                 |
| dulwich_log                | 68.2 ms                                                      | 67.0 ms: 1.02x faster                                                                  |
| mdp                        | 2.54 sec                                                     | 2.50 sec: 1.02x faster                                                                 |
| sympy_sum                  | 155 ms                                                       | 152 ms: 1.02x faster                                                                   |
| coverage                   | 80.0 ms                                                      | 78.8 ms: 1.02x faster                                                                  |
| django_template            | 36.4 ms                                                      | 35.8 ms: 1.01x faster                                                                  |
| pycparser                  | 1.24 sec                                                     | 1.23 sec: 1.01x faster                                                                 |
| nqueens                    | 90.7 ms                                                      | 89.6 ms: 1.01x faster                                                                  |
| logging_silent             | 97.9 ns                                                      | 96.9 ns: 1.01x faster                                                                  |
| python_startup_no_site     | 8.96 ms                                                      | 9.00 ms: 1.01x slower                                                                  |
| fannkuch                   | 363 ms                                                       | 365 ms: 1.01x slower                                                                   |
| python_startup             | 15.9 ms                                                      | 16.0 ms: 1.01x slower                                                                  |
| crypto_pyaes               | 73.3 ms                                                      | 73.9 ms: 1.01x slower                                                                  |
| raytrace                   | 273 ms                                                       | 275 ms: 1.01x slower                                                                   |
| pidigits                   | 252 ms                                                       | 255 ms: 1.01x slower                                                                   |
| docutils                   | 2.83 sec                                                     | 2.87 sec: 1.02x slower                                                                 |
| nbody                      | 89.3 ms                                                      | 90.8 ms: 1.02x slower                                                                  |
| pickle_pure_python         | 323 us                                                       | 330 us: 1.02x slower                                                                   |
| create_gc_cycles           | 2.68 ms                                                      | 2.77 ms: 1.03x slower                                                                  |
| json_dumps                 | 11.1 ms                                                      | 11.7 ms: 1.05x slower                                                                  |
| mako                       | 10.4 ms                                                      | 11.0 ms: 1.06x slower                                                                  |
| many_optionals             | 930 us                                                       | 1.01 ms: 1.08x slower                                                                  |
| json_loads                 | 24.7 us                                                      | 26.7 us: 1.08x slower                                                                  |
| subparsers                 | 17.5 ms                                                      | 22.8 ms: 1.31x slower                                                                  |
| gc_traversal               | 4.74 ms                                                      | 6.35 ms: 1.34x slower                                                                  |
| bench_mp_pool              | 5.12 ms                                                      | 1.32 sec: 258.20x slower                                                               |
| Geometric mean             | (ref)                                                        | 1.00x slower                                                                           |

Benchmark hidden because not significant (7): asyncio_websockets, chaos, logging_format, comprehensions, typing_runtime_protocols, bench_thread_pool, regex_v8
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.060x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.02x