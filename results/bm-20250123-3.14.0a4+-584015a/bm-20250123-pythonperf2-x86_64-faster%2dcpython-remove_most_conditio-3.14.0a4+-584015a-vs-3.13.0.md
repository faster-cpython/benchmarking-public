# Results vs. 3.13.0

- fork: faster-cpython
- ref: remove_most_conditio
- machine: linux-x86_64
- commit hash: 584015a
- commit date: 2025-01-23
- overall geometric mean: 1.058x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 283 ms: 1.03x faster                                                                   |
| docutils       | 2.83 sec                                                     | 2.92 sec: 1.03x slower                                                                 |
| html5lib       | 73.5 ms                                                      | 66.4 ms: 1.11x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                           |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 336 ms: 1.39x faster                                                                   |
| async_tree_none            | 376 ms                                                       | 288 ms: 1.30x faster                                                                   |
| async_tree_io              | 843 ms                                                       | 653 ms: 1.29x faster                                                                   |
| async_tree_io_tg           | 831 ms                                                       | 645 ms: 1.29x faster                                                                   |
| async_tree_memoization     | 453 ms                                                       | 351 ms: 1.29x faster                                                                   |
| async_tree_none_tg         | 346 ms                                                       | 279 ms: 1.24x faster                                                                   |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 517 ms: 1.17x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 505 ms: 1.15x faster                                                                   |
| async_generators           | 457 ms                                                       | 400 ms: 1.14x faster                                                                   |
| coroutines                 | 21.6 ms                                                      | 20.6 ms: 1.05x faster                                                                  |
| asyncio_websockets         | 388 ms                                                       | 384 ms: 1.01x faster                                                                   |
| Geometric mean             | (ref)                                                        | 1.21x faster                                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 69.3 ms: 1.17x faster                                                                  |
| nbody          | 89.3 ms                                                      | 86.6 ms: 1.03x faster                                                                  |
| pidigits       | 252 ms                                                       | 253 ms: 1.00x slower                                                                   |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.12 ms: 1.17x faster                                                                  |
| regex_compile  | 143 ms                                                       | 134 ms: 1.06x faster                                                                   |
| regex_v8       | 26.1 ms                                                      | 25.3 ms: 1.03x faster                                                                  |
| regex_dna      | 247 ms                                                       | 244 ms: 1.01x faster                                                                   |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.05 sec: 1.20x faster                                                                 |
| xml_etree_parse      | 150 ms                                                       | 134 ms: 1.12x faster                                                                   |
| unpickle_pure_python | 217 us                                                       | 208 us: 1.04x faster                                                                   |
| xml_etree_process    | 61.2 ms                                                      | 59.2 ms: 1.03x faster                                                                  |
| xml_etree_generate   | 86.5 ms                                                      | 84.1 ms: 1.03x faster                                                                  |
| xml_etree_iterparse  | 103 ms                                                       | 104 ms: 1.01x slower                                                                   |
| json_loads           | 24.7 us                                                      | 25.2 us: 1.02x slower                                                                  |
| json_dumps           | 11.1 ms                                                      | 11.7 ms: 1.05x slower                                                                  |
| Geometric mean       | (ref)                                                        | 1.04x faster                                                                           |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.96 ms                                                      | 8.98 ms: 1.00x slower                                                                  |
| python_startup         | 15.9 ms                                                      | 16.0 ms: 1.01x slower                                                                  |
| Geometric mean         | (ref)                                                        | 1.00x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 23.3 ms: 1.13x faster                                                                  |
| genshi_xml      | 57.1 ms                                                      | 52.3 ms: 1.09x faster                                                                  |
| django_template | 36.4 ms                                                      | 37.0 ms: 1.02x slower                                                                  |
| mako            | 10.4 ms                                                      | 10.9 ms: 1.05x slower                                                                  |
| Geometric mean  | (ref)                                                        | 1.04x faster                                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| deepcopy                   | 392 us                                                       | 280 us: 1.40x faster                                                                   |
| async_tree_memoization_tg  | 466 ms                                                       | 336 ms: 1.39x faster                                                                   |
| async_tree_none            | 376 ms                                                       | 288 ms: 1.30x faster                                                                   |
| async_tree_io              | 843 ms                                                       | 653 ms: 1.29x faster                                                                   |
| async_tree_io_tg           | 831 ms                                                       | 645 ms: 1.29x faster                                                                   |
| async_tree_memoization     | 453 ms                                                       | 351 ms: 1.29x faster                                                                   |
| deepcopy_memo              | 38.6 us                                                      | 30.4 us: 1.27x faster                                                                  |
| go                         | 162 ms                                                       | 130 ms: 1.25x faster                                                                   |
| async_tree_none_tg         | 346 ms                                                       | 279 ms: 1.24x faster                                                                   |
| deepcopy_reduce            | 3.54 us                                                      | 2.90 us: 1.22x faster                                                                  |
| tomli_loads                | 2.46 sec                                                     | 2.05 sec: 1.20x faster                                                                 |
| generators                 | 33.6 ms                                                      | 28.2 ms: 1.19x faster                                                                  |
| regex_effbot               | 3.67 ms                                                      | 3.12 ms: 1.17x faster                                                                  |
| float                      | 81.3 ms                                                      | 69.3 ms: 1.17x faster                                                                  |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 517 ms: 1.17x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 505 ms: 1.15x faster                                                                   |
| spectral_norm              | 97.0 ms                                                      | 84.3 ms: 1.15x faster                                                                  |
| pyflate                    | 503 ms                                                       | 438 ms: 1.15x faster                                                                   |
| telco                      | 8.79 ms                                                      | 7.66 ms: 1.15x faster                                                                  |
| async_generators           | 457 ms                                                       | 400 ms: 1.14x faster                                                                   |
| genshi_text                | 26.2 ms                                                      | 23.3 ms: 1.13x faster                                                                  |
| scimark_sor                | 123 ms                                                       | 110 ms: 1.12x faster                                                                   |
| xml_etree_parse            | 150 ms                                                       | 134 ms: 1.12x faster                                                                   |
| hexiom                     | 6.55 ms                                                      | 5.91 ms: 1.11x faster                                                                  |
| pathlib                    | 17.5 ms                                                      | 15.8 ms: 1.11x faster                                                                  |
| html5lib                   | 73.5 ms                                                      | 66.4 ms: 1.11x faster                                                                  |
| pprint_pformat             | 1.72 sec                                                     | 1.57 sec: 1.10x faster                                                                 |
| genshi_xml                 | 57.1 ms                                                      | 52.3 ms: 1.09x faster                                                                  |
| bpe_tokeniser              | 5.09 sec                                                     | 4.69 sec: 1.09x faster                                                                 |
| pylint                     | 347 ms                                                       | 322 ms: 1.08x faster                                                                   |
| pprint_safe_repr           | 843 ms                                                       | 782 ms: 1.08x faster                                                                   |
| scimark_fft                | 328 ms                                                       | 305 ms: 1.08x faster                                                                   |
| json                       | 5.69 ms                                                      | 5.34 ms: 1.06x faster                                                                  |
| regex_compile              | 143 ms                                                       | 134 ms: 1.06x faster                                                                   |
| sqlglot_parse              | 1.40 ms                                                      | 1.33 ms: 1.06x faster                                                                  |
| scimark_monte_carlo        | 66.1 ms                                                      | 62.8 ms: 1.05x faster                                                                  |
| mdp                        | 2.54 sec                                                     | 2.43 sec: 1.05x faster                                                                 |
| scimark_lu                 | 98.7 ms                                                      | 94.3 ms: 1.05x faster                                                                  |
| coroutines                 | 21.6 ms                                                      | 20.6 ms: 1.05x faster                                                                  |
| sqlglot_transpile          | 1.79 ms                                                      | 1.71 ms: 1.04x faster                                                                  |
| unpickle_pure_python       | 217 us                                                       | 208 us: 1.04x faster                                                                   |
| k_core                     | 2.17 sec                                                     | 2.08 sec: 1.04x faster                                                                 |
| sqlalchemy_declarative     | 148 ms                                                       | 143 ms: 1.04x faster                                                                   |
| sympy_expand               | 509 ms                                                       | 490 ms: 1.04x faster                                                                   |
| sqlite_synth               | 2.91 us                                                      | 2.80 us: 1.04x faster                                                                  |
| dulwich_log                | 68.2 ms                                                      | 65.7 ms: 1.04x faster                                                                  |
| sympy_str                  | 298 ms                                                       | 288 ms: 1.04x faster                                                                   |
| connected_components       | 432 ms                                                       | 418 ms: 1.03x faster                                                                   |
| 2to3                       | 293 ms                                                       | 283 ms: 1.03x faster                                                                   |
| sqlalchemy_imperative      | 18.3 ms                                                      | 17.7 ms: 1.03x faster                                                                  |
| xml_etree_process          | 61.2 ms                                                      | 59.2 ms: 1.03x faster                                                                  |
| regex_v8                   | 26.1 ms                                                      | 25.3 ms: 1.03x faster                                                                  |
| nbody                      | 89.3 ms                                                      | 86.6 ms: 1.03x faster                                                                  |
| shortest_path              | 460 ms                                                       | 446 ms: 1.03x faster                                                                   |
| sqlglot_optimize           | 59.3 ms                                                      | 57.5 ms: 1.03x faster                                                                  |
| sqlglot_normalize          | 119 ms                                                       | 116 ms: 1.03x faster                                                                   |
| coverage                   | 80.0 ms                                                      | 77.7 ms: 1.03x faster                                                                  |
| xml_etree_generate         | 86.5 ms                                                      | 84.1 ms: 1.03x faster                                                                  |
| meteor_contest             | 130 ms                                                       | 126 ms: 1.03x faster                                                                   |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.66 ms: 1.03x faster                                                                  |
| chaos                      | 60.2 ms                                                      | 58.8 ms: 1.02x faster                                                                  |
| thrift                     | 901 us                                                       | 880 us: 1.02x faster                                                                   |
| nqueens                    | 90.7 ms                                                      | 88.8 ms: 1.02x faster                                                                  |
| sympy_sum                  | 155 ms                                                       | 152 ms: 1.02x faster                                                                   |
| sympy_integrate            | 23.6 ms                                                      | 23.1 ms: 1.02x faster                                                                  |
| logging_simple             | 6.39 us                                                      | 6.28 us: 1.02x faster                                                                  |
| regex_dna                  | 247 ms                                                       | 244 ms: 1.01x faster                                                                   |
| logging_format             | 6.94 us                                                      | 6.86 us: 1.01x faster                                                                  |
| asyncio_websockets         | 388 ms                                                       | 384 ms: 1.01x faster                                                                   |
| crypto_pyaes               | 73.3 ms                                                      | 72.6 ms: 1.01x faster                                                                  |
| logging_silent             | 97.9 ns                                                      | 97.4 ns: 1.01x faster                                                                  |
| pidigits                   | 252 ms                                                       | 253 ms: 1.00x slower                                                                   |
| python_startup_no_site     | 8.96 ms                                                      | 8.98 ms: 1.00x slower                                                                  |
| python_startup             | 15.9 ms                                                      | 16.0 ms: 1.01x slower                                                                  |
| fannkuch                   | 363 ms                                                       | 366 ms: 1.01x slower                                                                   |
| xml_etree_iterparse        | 103 ms                                                       | 104 ms: 1.01x slower                                                                   |
| django_template            | 36.4 ms                                                      | 37.0 ms: 1.02x slower                                                                  |
| json_loads                 | 24.7 us                                                      | 25.2 us: 1.02x slower                                                                  |
| docutils                   | 2.83 sec                                                     | 2.92 sec: 1.03x slower                                                                 |
| create_gc_cycles           | 2.68 ms                                                      | 2.79 ms: 1.04x slower                                                                  |
| comprehensions             | 17.0 us                                                      | 17.7 us: 1.04x slower                                                                  |
| richards                   | 52.9 ms                                                      | 55.3 ms: 1.04x slower                                                                  |
| richards_super             | 59.6 ms                                                      | 62.3 ms: 1.05x slower                                                                  |
| mako                       | 10.4 ms                                                      | 10.9 ms: 1.05x slower                                                                  |
| json_dumps                 | 11.1 ms                                                      | 11.7 ms: 1.05x slower                                                                  |
| many_optionals             | 930 us                                                       | 1.02 ms: 1.10x slower                                                                  |
| subparsers                 | 17.5 ms                                                      | 23.1 ms: 1.32x slower                                                                  |
| gc_traversal               | 4.74 ms                                                      | 6.41 ms: 1.35x slower                                                                  |
| bench_mp_pool              | 5.12 ms                                                      | 2.02 sec: 393.79x slower                                                               |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                                           |

Benchmark hidden because not significant (7): bench_thread_pool, typing_runtime_protocols, raytrace, pickle_pure_python, pycparser, sphinx, deltablue
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.058x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.02x