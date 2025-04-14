# Results vs. 3.13.0

- fork: faster-cpython
- ref: account_for_escapes_
- machine: linux-x86_64
- commit hash: de9adc3
- commit date: 2025-02-06
- overall geometric mean: 1.055x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-de9adc3 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 286 ms: 1.02x faster                                                                   |
| docutils       | 2.83 sec                                                     | 2.87 sec: 1.01x slower                                                                 |
| html5lib       | 73.5 ms                                                      | 67.6 ms: 1.09x faster                                                                  |
| sphinx         | 1.12 sec                                                     | 1.10 sec: 1.02x faster                                                                 |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-de9adc3 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 340 ms: 1.37x faster                                                                   |
| async_tree_none            | 376 ms                                                       | 290 ms: 1.30x faster                                                                   |
| async_tree_memoization     | 453 ms                                                       | 353 ms: 1.28x faster                                                                   |
| async_tree_io              | 843 ms                                                       | 658 ms: 1.28x faster                                                                   |
| async_tree_io_tg           | 831 ms                                                       | 655 ms: 1.27x faster                                                                   |
| async_tree_none_tg         | 346 ms                                                       | 279 ms: 1.24x faster                                                                   |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 523 ms: 1.16x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 510 ms: 1.14x faster                                                                   |
| async_generators           | 457 ms                                                       | 405 ms: 1.13x faster                                                                   |
| coroutines                 | 21.6 ms                                                      | 21.1 ms: 1.02x faster                                                                  |
| asyncio_websockets         | 388 ms                                                       | 385 ms: 1.01x faster                                                                   |
| Geometric mean             | (ref)                                                        | 1.19x faster                                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-de9adc3 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 70.3 ms: 1.16x faster                                                                  |
| pidigits       | 252 ms                                                       | 254 ms: 1.01x slower                                                                   |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                           |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-de9adc3 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.11 ms: 1.18x faster                                                                  |
| regex_dna      | 247 ms                                                       | 231 ms: 1.07x faster                                                                   |
| regex_compile  | 143 ms                                                       | 135 ms: 1.06x faster                                                                   |
| regex_v8       | 26.1 ms                                                      | 25.2 ms: 1.04x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-de9adc3 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.09 sec: 1.18x faster                                                                 |
| xml_etree_parse      | 150 ms                                                       | 139 ms: 1.08x faster                                                                   |
| xml_etree_iterparse  | 103 ms                                                       | 98.7 ms: 1.04x faster                                                                  |
| xml_etree_generate   | 86.5 ms                                                      | 83.9 ms: 1.03x faster                                                                  |
| unpickle_pure_python | 217 us                                                       | 211 us: 1.03x faster                                                                   |
| xml_etree_process    | 61.2 ms                                                      | 60.2 ms: 1.02x faster                                                                  |
| pickle_pure_python   | 323 us                                                       | 329 us: 1.02x slower                                                                   |
| json_dumps           | 11.1 ms                                                      | 11.8 ms: 1.06x slower                                                                  |
| json_loads           | 24.7 us                                                      | 26.5 us: 1.07x slower                                                                  |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-de9adc3 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.96 ms                                                      | 9.01 ms: 1.01x slower                                                                  |
| python_startup         | 15.9 ms                                                      | 16.2 ms: 1.02x slower                                                                  |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-de9adc3 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 24.7 ms: 1.06x faster                                                                  |
| django_template | 36.4 ms                                                      | 35.9 ms: 1.01x faster                                                                  |
| genshi_xml      | 57.1 ms                                                      | 57.9 ms: 1.02x slower                                                                  |
| mako            | 10.4 ms                                                      | 10.7 ms: 1.03x slower                                                                  |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-de9adc3 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 340 ms: 1.37x faster                                                                   |
| deepcopy                   | 392 us                                                       | 288 us: 1.36x faster                                                                   |
| async_tree_none            | 376 ms                                                       | 290 ms: 1.30x faster                                                                   |
| async_tree_memoization     | 453 ms                                                       | 353 ms: 1.28x faster                                                                   |
| async_tree_io              | 843 ms                                                       | 658 ms: 1.28x faster                                                                   |
| go                         | 162 ms                                                       | 127 ms: 1.27x faster                                                                   |
| async_tree_io_tg           | 831 ms                                                       | 655 ms: 1.27x faster                                                                   |
| deepcopy_memo              | 38.6 us                                                      | 30.5 us: 1.27x faster                                                                  |
| async_tree_none_tg         | 346 ms                                                       | 279 ms: 1.24x faster                                                                   |
| deepcopy_reduce            | 3.54 us                                                      | 2.95 us: 1.20x faster                                                                  |
| regex_effbot               | 3.67 ms                                                      | 3.11 ms: 1.18x faster                                                                  |
| tomli_loads                | 2.46 sec                                                     | 2.09 sec: 1.18x faster                                                                 |
| spectral_norm              | 97.0 ms                                                      | 83.1 ms: 1.17x faster                                                                  |
| float                      | 81.3 ms                                                      | 70.3 ms: 1.16x faster                                                                  |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 523 ms: 1.16x faster                                                                   |
| generators                 | 33.6 ms                                                      | 29.2 ms: 1.15x faster                                                                  |
| pyflate                    | 503 ms                                                       | 439 ms: 1.15x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 510 ms: 1.14x faster                                                                   |
| async_generators           | 457 ms                                                       | 405 ms: 1.13x faster                                                                   |
| richards                   | 52.9 ms                                                      | 47.0 ms: 1.13x faster                                                                  |
| richards_super             | 59.6 ms                                                      | 52.9 ms: 1.13x faster                                                                  |
| pathlib                    | 17.5 ms                                                      | 15.8 ms: 1.11x faster                                                                  |
| scimark_sor                | 123 ms                                                       | 111 ms: 1.11x faster                                                                   |
| bpe_tokeniser              | 5.09 sec                                                     | 4.59 sec: 1.11x faster                                                                 |
| pylint                     | 347 ms                                                       | 317 ms: 1.09x faster                                                                   |
| html5lib                   | 73.5 ms                                                      | 67.6 ms: 1.09x faster                                                                  |
| xml_etree_parse            | 150 ms                                                       | 139 ms: 1.08x faster                                                                   |
| telco                      | 8.79 ms                                                      | 8.11 ms: 1.08x faster                                                                  |
| regex_dna                  | 247 ms                                                       | 231 ms: 1.07x faster                                                                   |
| hexiom                     | 6.55 ms                                                      | 6.16 ms: 1.06x faster                                                                  |
| pprint_safe_repr           | 843 ms                                                       | 792 ms: 1.06x faster                                                                   |
| genshi_text                | 26.2 ms                                                      | 24.7 ms: 1.06x faster                                                                  |
| regex_compile              | 143 ms                                                       | 135 ms: 1.06x faster                                                                   |
| pprint_pformat             | 1.72 sec                                                     | 1.64 sec: 1.05x faster                                                                 |
| scimark_lu                 | 98.7 ms                                                      | 94.1 ms: 1.05x faster                                                                  |
| scimark_fft                | 328 ms                                                       | 313 ms: 1.05x faster                                                                   |
| meteor_contest             | 130 ms                                                       | 124 ms: 1.04x faster                                                                   |
| xml_etree_iterparse        | 103 ms                                                       | 98.7 ms: 1.04x faster                                                                  |
| connected_components       | 432 ms                                                       | 415 ms: 1.04x faster                                                                   |
| sqlite_synth               | 2.91 us                                                      | 2.80 us: 1.04x faster                                                                  |
| json                       | 5.69 ms                                                      | 5.49 ms: 1.04x faster                                                                  |
| thrift                     | 901 us                                                       | 870 us: 1.04x faster                                                                   |
| regex_v8                   | 26.1 ms                                                      | 25.2 ms: 1.04x faster                                                                  |
| sqlalchemy_declarative     | 148 ms                                                       | 143 ms: 1.04x faster                                                                   |
| shortest_path              | 460 ms                                                       | 445 ms: 1.03x faster                                                                   |
| sqlglot_parse              | 1.40 ms                                                      | 1.35 ms: 1.03x faster                                                                  |
| k_core                     | 2.17 sec                                                     | 2.10 sec: 1.03x faster                                                                 |
| mdp                        | 2.54 sec                                                     | 2.46 sec: 1.03x faster                                                                 |
| coverage                   | 80.0 ms                                                      | 77.5 ms: 1.03x faster                                                                  |
| xml_etree_generate         | 86.5 ms                                                      | 83.9 ms: 1.03x faster                                                                  |
| sqlglot_optimize           | 59.3 ms                                                      | 57.5 ms: 1.03x faster                                                                  |
| logging_simple             | 6.39 us                                                      | 6.20 us: 1.03x faster                                                                  |
| sqlalchemy_imperative      | 18.3 ms                                                      | 17.8 ms: 1.03x faster                                                                  |
| unpickle_pure_python       | 217 us                                                       | 211 us: 1.03x faster                                                                   |
| sqlglot_transpile          | 1.79 ms                                                      | 1.74 ms: 1.03x faster                                                                  |
| deltablue                  | 3.42 ms                                                      | 3.33 ms: 1.03x faster                                                                  |
| sqlglot_normalize          | 119 ms                                                       | 116 ms: 1.03x faster                                                                   |
| sympy_str                  | 298 ms                                                       | 291 ms: 1.02x faster                                                                   |
| sympy_expand               | 509 ms                                                       | 497 ms: 1.02x faster                                                                   |
| 2to3                       | 293 ms                                                       | 286 ms: 1.02x faster                                                                   |
| sphinx                     | 1.12 sec                                                     | 1.10 sec: 1.02x faster                                                                 |
| coroutines                 | 21.6 ms                                                      | 21.1 ms: 1.02x faster                                                                  |
| sympy_sum                  | 155 ms                                                       | 152 ms: 1.02x faster                                                                   |
| sympy_integrate            | 23.6 ms                                                      | 23.1 ms: 1.02x faster                                                                  |
| nqueens                    | 90.7 ms                                                      | 88.9 ms: 1.02x faster                                                                  |
| dulwich_log                | 68.2 ms                                                      | 67.0 ms: 1.02x faster                                                                  |
| xml_etree_process          | 61.2 ms                                                      | 60.2 ms: 1.02x faster                                                                  |
| scimark_monte_carlo        | 66.1 ms                                                      | 65.4 ms: 1.01x faster                                                                  |
| django_template            | 36.4 ms                                                      | 35.9 ms: 1.01x faster                                                                  |
| logging_silent             | 97.9 ns                                                      | 96.9 ns: 1.01x faster                                                                  |
| logging_format             | 6.94 us                                                      | 6.87 us: 1.01x faster                                                                  |
| asyncio_websockets         | 388 ms                                                       | 385 ms: 1.01x faster                                                                   |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.76 ms: 1.00x faster                                                                  |
| python_startup_no_site     | 8.96 ms                                                      | 9.01 ms: 1.01x slower                                                                  |
| fannkuch                   | 363 ms                                                       | 366 ms: 1.01x slower                                                                   |
| pidigits                   | 252 ms                                                       | 254 ms: 1.01x slower                                                                   |
| comprehensions             | 17.0 us                                                      | 17.2 us: 1.01x slower                                                                  |
| pycparser                  | 1.24 sec                                                     | 1.26 sec: 1.01x slower                                                                 |
| docutils                   | 2.83 sec                                                     | 2.87 sec: 1.01x slower                                                                 |
| genshi_xml                 | 57.1 ms                                                      | 57.9 ms: 1.02x slower                                                                  |
| raytrace                   | 273 ms                                                       | 277 ms: 1.02x slower                                                                   |
| python_startup             | 15.9 ms                                                      | 16.2 ms: 1.02x slower                                                                  |
| pickle_pure_python         | 323 us                                                       | 329 us: 1.02x slower                                                                   |
| create_gc_cycles           | 2.68 ms                                                      | 2.76 ms: 1.03x slower                                                                  |
| crypto_pyaes               | 73.3 ms                                                      | 75.4 ms: 1.03x slower                                                                  |
| mako                       | 10.4 ms                                                      | 10.7 ms: 1.03x slower                                                                  |
| json_dumps                 | 11.1 ms                                                      | 11.8 ms: 1.06x slower                                                                  |
| json_loads                 | 24.7 us                                                      | 26.5 us: 1.07x slower                                                                  |
| many_optionals             | 930 us                                                       | 1.00 ms: 1.08x slower                                                                  |
| subparsers                 | 17.5 ms                                                      | 22.9 ms: 1.31x slower                                                                  |
| gc_traversal               | 4.74 ms                                                      | 6.38 ms: 1.34x slower                                                                  |
| bench_mp_pool              | 5.12 ms                                                      | 1.64 sec: 319.26x slower                                                               |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                                           |

Benchmark hidden because not significant (4): chaos, typing_runtime_protocols, bench_thread_pool, nbody
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.055x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.02x