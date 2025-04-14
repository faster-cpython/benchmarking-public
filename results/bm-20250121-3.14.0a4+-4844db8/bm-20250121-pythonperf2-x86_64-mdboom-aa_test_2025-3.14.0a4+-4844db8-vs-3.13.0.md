# Results vs. 3.13.0

- fork: mdboom
- ref: aa_test_2025
- machine: linux-x86_64
- commit hash: 4844db8
- commit date: 2025-01-21
- overall geometric mean: 1.062x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 282 ms: 1.04x faster                                                 |
| docutils       | 2.83 sec                                                     | 2.88 sec: 1.02x slower                                               |
| html5lib       | 73.5 ms                                                      | 66.5 ms: 1.10x faster                                                |
| Geometric mean | (ref)                                                        | 1.03x faster                                                         |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 325 ms: 1.43x faster                                                 |
| async_tree_none            | 376 ms                                                       | 275 ms: 1.37x faster                                                 |
| async_tree_io              | 843 ms                                                       | 626 ms: 1.35x faster                                                 |
| async_tree_io_tg           | 831 ms                                                       | 621 ms: 1.34x faster                                                 |
| async_tree_memoization     | 453 ms                                                       | 340 ms: 1.33x faster                                                 |
| async_tree_none_tg         | 346 ms                                                       | 266 ms: 1.30x faster                                                 |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 507 ms: 1.19x faster                                                 |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 497 ms: 1.17x faster                                                 |
| async_generators           | 457 ms                                                       | 410 ms: 1.11x faster                                                 |
| coroutines                 | 21.6 ms                                                      | 21.0 ms: 1.03x faster                                                |
| Geometric mean             | (ref)                                                        | 1.23x faster                                                         |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 69.5 ms: 1.17x faster                                                |
| nbody          | 89.3 ms                                                      | 87.1 ms: 1.03x faster                                                |
| pidigits       | 252 ms                                                       | 254 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                        | 1.06x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.11 ms: 1.18x faster                                                |
| regex_compile  | 143 ms                                                       | 135 ms: 1.06x faster                                                 |
| regex_dna      | 247 ms                                                       | 236 ms: 1.05x faster                                                 |
| Geometric mean | (ref)                                                        | 1.07x faster                                                         |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.08 sec: 1.18x faster                                               |
| xml_etree_parse      | 150 ms                                                       | 137 ms: 1.10x faster                                                 |
| xml_etree_iterparse  | 103 ms                                                       | 96.2 ms: 1.07x faster                                                |
| xml_etree_generate   | 86.5 ms                                                      | 83.2 ms: 1.04x faster                                                |
| xml_etree_process    | 61.2 ms                                                      | 60.7 ms: 1.01x faster                                                |
| unpickle_pure_python | 217 us                                                       | 219 us: 1.01x slower                                                 |
| json_loads           | 24.7 us                                                      | 25.5 us: 1.03x slower                                                |
| json_dumps           | 11.1 ms                                                      | 11.5 ms: 1.04x slower                                                |
| pickle_pure_python   | 323 us                                                       | 339 us: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                        | 1.03x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 8.96 ms                                                      | 9.01 ms: 1.01x slower                                                |
| python_startup         | 15.9 ms                                                      | 16.1 ms: 1.01x slower                                                |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 24.9 ms: 1.05x faster                                                |
| genshi_xml      | 57.1 ms                                                      | 54.6 ms: 1.05x faster                                                |
| django_template | 36.4 ms                                                      | 36.0 ms: 1.01x faster                                                |
| mako            | 10.4 ms                                                      | 11.0 ms: 1.06x slower                                                |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 325 ms: 1.43x faster                                                 |
| deepcopy                   | 392 us                                                       | 283 us: 1.38x faster                                                 |
| async_tree_none            | 376 ms                                                       | 275 ms: 1.37x faster                                                 |
| async_tree_io              | 843 ms                                                       | 626 ms: 1.35x faster                                                 |
| async_tree_io_tg           | 831 ms                                                       | 621 ms: 1.34x faster                                                 |
| async_tree_memoization     | 453 ms                                                       | 340 ms: 1.33x faster                                                 |
| async_tree_none_tg         | 346 ms                                                       | 266 ms: 1.30x faster                                                 |
| go                         | 162 ms                                                       | 126 ms: 1.29x faster                                                 |
| deepcopy_memo              | 38.6 us                                                      | 30.3 us: 1.28x faster                                                |
| deepcopy_reduce            | 3.54 us                                                      | 2.95 us: 1.20x faster                                                |
| generators                 | 33.6 ms                                                      | 28.1 ms: 1.20x faster                                                |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 507 ms: 1.19x faster                                                 |
| tomli_loads                | 2.46 sec                                                     | 2.08 sec: 1.18x faster                                               |
| regex_effbot               | 3.67 ms                                                      | 3.11 ms: 1.18x faster                                                |
| float                      | 81.3 ms                                                      | 69.5 ms: 1.17x faster                                                |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 497 ms: 1.17x faster                                                 |
| richards                   | 52.9 ms                                                      | 45.5 ms: 1.16x faster                                                |
| spectral_norm              | 97.0 ms                                                      | 83.7 ms: 1.16x faster                                                |
| richards_super             | 59.6 ms                                                      | 52.6 ms: 1.13x faster                                                |
| pyflate                    | 503 ms                                                       | 446 ms: 1.13x faster                                                 |
| async_generators           | 457 ms                                                       | 410 ms: 1.11x faster                                                 |
| scimark_sor                | 123 ms                                                       | 111 ms: 1.11x faster                                                 |
| html5lib                   | 73.5 ms                                                      | 66.5 ms: 1.10x faster                                                |
| telco                      | 8.79 ms                                                      | 7.99 ms: 1.10x faster                                                |
| pathlib                    | 17.5 ms                                                      | 16.0 ms: 1.10x faster                                                |
| pylint                     | 347 ms                                                       | 316 ms: 1.10x faster                                                 |
| xml_etree_parse            | 150 ms                                                       | 137 ms: 1.10x faster                                                 |
| hexiom                     | 6.55 ms                                                      | 6.00 ms: 1.09x faster                                                |
| scimark_fft                | 328 ms                                                       | 301 ms: 1.09x faster                                                 |
| bpe_tokeniser              | 5.09 sec                                                     | 4.69 sec: 1.09x faster                                               |
| pprint_pformat             | 1.72 sec                                                     | 1.59 sec: 1.08x faster                                               |
| pprint_safe_repr           | 843 ms                                                       | 779 ms: 1.08x faster                                                 |
| coverage                   | 80.0 ms                                                      | 74.1 ms: 1.08x faster                                                |
| sqlglot_parse              | 1.40 ms                                                      | 1.31 ms: 1.07x faster                                                |
| xml_etree_iterparse        | 103 ms                                                       | 96.2 ms: 1.07x faster                                                |
| json                       | 5.69 ms                                                      | 5.36 ms: 1.06x faster                                                |
| sqlglot_transpile          | 1.79 ms                                                      | 1.69 ms: 1.06x faster                                                |
| regex_compile              | 143 ms                                                       | 135 ms: 1.06x faster                                                 |
| scimark_monte_carlo        | 66.1 ms                                                      | 62.6 ms: 1.06x faster                                                |
| genshi_text                | 26.2 ms                                                      | 24.9 ms: 1.05x faster                                                |
| regex_dna                  | 247 ms                                                       | 236 ms: 1.05x faster                                                 |
| genshi_xml                 | 57.1 ms                                                      | 54.6 ms: 1.05x faster                                                |
| mdp                        | 2.54 sec                                                     | 2.44 sec: 1.04x faster                                               |
| connected_components       | 432 ms                                                       | 415 ms: 1.04x faster                                                 |
| xml_etree_generate         | 86.5 ms                                                      | 83.2 ms: 1.04x faster                                                |
| thrift                     | 901 us                                                       | 866 us: 1.04x faster                                                 |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.59 ms: 1.04x faster                                                |
| 2to3                       | 293 ms                                                       | 282 ms: 1.04x faster                                                 |
| k_core                     | 2.17 sec                                                     | 2.09 sec: 1.04x faster                                               |
| shortest_path              | 460 ms                                                       | 445 ms: 1.03x faster                                                 |
| sympy_str                  | 298 ms                                                       | 289 ms: 1.03x faster                                                 |
| dulwich_log                | 68.2 ms                                                      | 66.1 ms: 1.03x faster                                                |
| sqlglot_normalize          | 119 ms                                                       | 116 ms: 1.03x faster                                                 |
| sqlglot_optimize           | 59.3 ms                                                      | 57.7 ms: 1.03x faster                                                |
| coroutines                 | 21.6 ms                                                      | 21.0 ms: 1.03x faster                                                |
| nbody                      | 89.3 ms                                                      | 87.1 ms: 1.03x faster                                                |
| sympy_expand               | 509 ms                                                       | 497 ms: 1.03x faster                                                 |
| scimark_lu                 | 98.7 ms                                                      | 96.3 ms: 1.02x faster                                                |
| pycparser                  | 1.24 sec                                                     | 1.21 sec: 1.02x faster                                               |
| sqlite_synth               | 2.91 us                                                      | 2.84 us: 1.02x faster                                                |
| sympy_sum                  | 155 ms                                                       | 151 ms: 1.02x faster                                                 |
| meteor_contest             | 130 ms                                                       | 127 ms: 1.02x faster                                                 |
| fannkuch                   | 363 ms                                                       | 356 ms: 1.02x faster                                                 |
| raytrace                   | 273 ms                                                       | 267 ms: 1.02x faster                                                 |
| sqlalchemy_declarative     | 148 ms                                                       | 146 ms: 1.02x faster                                                 |
| sympy_integrate            | 23.6 ms                                                      | 23.1 ms: 1.02x faster                                                |
| deltablue                  | 3.42 ms                                                      | 3.36 ms: 1.02x faster                                                |
| sqlalchemy_imperative      | 18.3 ms                                                      | 18.0 ms: 1.02x faster                                                |
| chaos                      | 60.2 ms                                                      | 59.5 ms: 1.01x faster                                                |
| django_template            | 36.4 ms                                                      | 36.0 ms: 1.01x faster                                                |
| nqueens                    | 90.7 ms                                                      | 89.8 ms: 1.01x faster                                                |
| xml_etree_process          | 61.2 ms                                                      | 60.7 ms: 1.01x faster                                                |
| logging_silent             | 97.9 ns                                                      | 97.1 ns: 1.01x faster                                                |
| python_startup_no_site     | 8.96 ms                                                      | 9.01 ms: 1.01x slower                                                |
| pidigits                   | 252 ms                                                       | 254 ms: 1.01x slower                                                 |
| unpickle_pure_python       | 217 us                                                       | 219 us: 1.01x slower                                                 |
| crypto_pyaes               | 73.3 ms                                                      | 73.9 ms: 1.01x slower                                                |
| python_startup             | 15.9 ms                                                      | 16.1 ms: 1.01x slower                                                |
| docutils                   | 2.83 sec                                                     | 2.88 sec: 1.02x slower                                               |
| create_gc_cycles           | 2.68 ms                                                      | 2.75 ms: 1.02x slower                                                |
| comprehensions             | 17.0 us                                                      | 17.5 us: 1.03x slower                                                |
| json_loads                 | 24.7 us                                                      | 25.5 us: 1.03x slower                                                |
| json_dumps                 | 11.1 ms                                                      | 11.5 ms: 1.04x slower                                                |
| logging_simple             | 6.39 us                                                      | 6.69 us: 1.05x slower                                                |
| pickle_pure_python         | 323 us                                                       | 339 us: 1.05x slower                                                 |
| logging_format             | 6.94 us                                                      | 7.28 us: 1.05x slower                                                |
| mako                       | 10.4 ms                                                      | 11.0 ms: 1.06x slower                                                |
| typing_runtime_protocols   | 169 us                                                       | 183 us: 1.08x slower                                                 |
| many_optionals             | 930 us                                                       | 1.01 ms: 1.09x slower                                                |
| subparsers                 | 17.5 ms                                                      | 22.7 ms: 1.30x slower                                                |
| gc_traversal               | 4.74 ms                                                      | 6.36 ms: 1.34x slower                                                |
| bench_mp_pool              | 5.12 ms                                                      | 1.87 sec: 365.02x slower                                             |
| Geometric mean             | (ref)                                                        | 1.00x slower                                                         |

Benchmark hidden because not significant (4): bench_thread_pool, sphinx, asyncio_websockets, regex_v8
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.062x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.02x