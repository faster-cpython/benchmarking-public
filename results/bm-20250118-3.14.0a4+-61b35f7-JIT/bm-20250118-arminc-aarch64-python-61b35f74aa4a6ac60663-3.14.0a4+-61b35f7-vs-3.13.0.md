# Results vs. 3.13.0

- fork: python
- ref: 61b35f74aa4a6ac60663
- machine: linux-aarch64
- commit hash: 61b35f7
- commit date: 2025-01-18
- overall geometric mean: 1.031x slower
- HPT reliability: 96.97%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 329 ms: 1.05x slower                                                     |
| docutils       | 2.96 sec                                                 | 3.24 sec: 1.09x slower                                                   |
| html5lib       | 65.6 ms                                                  | 70.5 ms: 1.07x slower                                                    |
| sphinx         | 1.20 sec                                                 | 1.26 sec: 1.05x slower                                                   |
| Geometric mean | (ref)                                                    | 1.07x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 481 ms: 1.38x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 519 ms: 1.28x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 915 ms: 1.27x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 389 ms: 1.24x faster                                                     |
| async_tree_none            | 504 ms                                                   | 406 ms: 1.24x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 921 ms: 1.24x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 681 ms: 1.18x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 701 ms: 1.13x faster                                                     |
| Geometric mean             | (ref)                                                    | 1.17x faster                                                             |

Benchmark hidden because not significant (3): coroutines, async_generators, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 88.5 ms: 1.08x faster                                                    |
| Geometric mean | (ref)                                                    | 1.00x faster                                                             |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.02 ms: 1.27x faster                                                    |
| regex_dna      | 263 ms                                                   | 254 ms: 1.03x faster                                                     |
| regex_compile  | 134 ms                                                   | 144 ms: 1.08x slower                                                     |
| Geometric mean | (ref)                                                    | 1.05x faster                                                             |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 182 ms: 1.11x faster                                                     |
| xml_etree_iterparse | 159 ms                                                   | 147 ms: 1.08x faster                                                     |
| tomli_loads         | 2.67 sec                                                 | 2.56 sec: 1.04x faster                                                   |
| pickle_pure_python  | 374 us                                                   | 405 us: 1.08x slower                                                     |
| json_dumps          | 14.2 ms                                                  | 15.8 ms: 1.11x slower                                                    |
| Geometric mean      | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (4): xml_etree_generate, xml_etree_process, unpickle_pure_python, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 9.10 ms: 1.04x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.03x slower                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 28.6 ms                                                  | 33.7 ms: 1.18x slower                                                    |
| django_template | 39.4 ms                                                  | 48.8 ms: 1.24x slower                                                    |
| genshi_xml      | 61.6 ms                                                  | 87.0 ms: 1.41x slower                                                    |
| Geometric mean  | (ref)                                                    | 1.20x slower                                                             |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 481 ms: 1.38x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 519 ms: 1.28x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 915 ms: 1.27x faster                                                     |
| regex_effbot               | 5.10 ms                                                  | 4.02 ms: 1.27x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 389 ms: 1.24x faster                                                     |
| async_tree_none            | 504 ms                                                   | 406 ms: 1.24x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 921 ms: 1.24x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 43.2 us: 1.23x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 681 ms: 1.18x faster                                                     |
| deepcopy                   | 479 us                                                   | 411 us: 1.16x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 701 ms: 1.13x faster                                                     |
| xml_etree_parse            | 203 ms                                                   | 182 ms: 1.11x faster                                                     |
| xml_etree_iterparse        | 159 ms                                                   | 147 ms: 1.08x faster                                                     |
| float                      | 95.8 ms                                                  | 88.5 ms: 1.08x faster                                                    |
| pathlib                    | 24.3 ms                                                  | 22.7 ms: 1.07x faster                                                    |
| scimark_fft                | 463 ms                                                   | 432 ms: 1.07x faster                                                     |
| spectral_norm              | 143 ms                                                   | 135 ms: 1.06x faster                                                     |
| scimark_sor                | 164 ms                                                   | 157 ms: 1.05x faster                                                     |
| bpe_tokeniser              | 6.02 sec                                                 | 5.77 sec: 1.04x faster                                                   |
| tomli_loads                | 2.67 sec                                                 | 2.56 sec: 1.04x faster                                                   |
| regex_dna                  | 263 ms                                                   | 254 ms: 1.03x faster                                                     |
| shortest_path              | 565 ms                                                   | 579 ms: 1.02x slower                                                     |
| richards                   | 54.5 ms                                                  | 56.3 ms: 1.03x slower                                                    |
| python_startup_no_site     | 8.79 ms                                                  | 9.10 ms: 1.04x slower                                                    |
| mdp                        | 3.45 sec                                                 | 3.59 sec: 1.04x slower                                                   |
| sphinx                     | 1.20 sec                                                 | 1.26 sec: 1.05x slower                                                   |
| richards_super             | 60.8 ms                                                  | 63.8 ms: 1.05x slower                                                    |
| 2to3                       | 313 ms                                                   | 329 ms: 1.05x slower                                                     |
| pyflate                    | 582 ms                                                   | 624 ms: 1.07x slower                                                     |
| sympy_sum                  | 151 ms                                                   | 162 ms: 1.07x slower                                                     |
| scimark_lu                 | 146 ms                                                   | 157 ms: 1.07x slower                                                     |
| html5lib                   | 65.6 ms                                                  | 70.5 ms: 1.07x slower                                                    |
| sympy_integrate            | 21.4 ms                                                  | 23.0 ms: 1.07x slower                                                    |
| create_gc_cycles           | 3.39 ms                                                  | 3.65 ms: 1.08x slower                                                    |
| sqlglot_optimize           | 65.2 ms                                                  | 70.2 ms: 1.08x slower                                                    |
| fannkuch                   | 478 ms                                                   | 515 ms: 1.08x slower                                                     |
| regex_compile              | 134 ms                                                   | 144 ms: 1.08x slower                                                     |
| sqlglot_normalize          | 131 ms                                                   | 142 ms: 1.08x slower                                                     |
| pickle_pure_python         | 374 us                                                   | 405 us: 1.08x slower                                                     |
| meteor_contest             | 117 ms                                                   | 127 ms: 1.09x slower                                                     |
| docutils                   | 2.96 sec                                                 | 3.24 sec: 1.09x slower                                                   |
| logging_format             | 8.10 us                                                  | 8.91 us: 1.10x slower                                                    |
| deltablue                  | 3.97 ms                                                  | 4.38 ms: 1.10x slower                                                    |
| crypto_pyaes               | 84.9 ms                                                  | 94.0 ms: 1.11x slower                                                    |
| json_dumps                 | 14.2 ms                                                  | 15.8 ms: 1.11x slower                                                    |
| sympy_expand               | 472 ms                                                   | 526 ms: 1.11x slower                                                     |
| logging_silent             | 135 ns                                                   | 150 ns: 1.11x slower                                                     |
| raytrace                   | 310 ms                                                   | 347 ms: 1.12x slower                                                     |
| typing_runtime_protocols   | 197 us                                                   | 222 us: 1.12x slower                                                     |
| logging_simple             | 7.25 us                                                  | 8.19 us: 1.13x slower                                                    |
| sympy_str                  | 265 ms                                                   | 301 ms: 1.13x slower                                                     |
| sqlglot_parse              | 1.43 ms                                                  | 1.63 ms: 1.13x slower                                                    |
| pycparser                  | 1.34 sec                                                 | 1.54 sec: 1.14x slower                                                   |
| go                         | 164 ms                                                   | 188 ms: 1.14x slower                                                     |
| chaos                      | 70.7 ms                                                  | 82.3 ms: 1.16x slower                                                    |
| gc_traversal               | 5.92 ms                                                  | 7.00 ms: 1.18x slower                                                    |
| genshi_text                | 28.6 ms                                                  | 33.7 ms: 1.18x slower                                                    |
| comprehensions             | 20.8 us                                                  | 24.8 us: 1.19x slower                                                    |
| nqueens                    | 105 ms                                                   | 126 ms: 1.20x slower                                                     |
| django_template            | 39.4 ms                                                  | 48.8 ms: 1.24x slower                                                    |
| hexiom                     | 7.34 ms                                                  | 9.71 ms: 1.32x slower                                                    |
| pprint_pformat             | 1.99 sec                                                 | 2.65 sec: 1.34x slower                                                   |
| pprint_safe_repr           | 962 ms                                                   | 1.29 sec: 1.34x slower                                                   |
| subparsers                 | 20.3 ms                                                  | 27.6 ms: 1.35x slower                                                    |
| many_optionals             | 626 us                                                   | 861 us: 1.37x slower                                                     |
| generators                 | 40.3 ms                                                  | 55.5 ms: 1.38x slower                                                    |
| genshi_xml                 | 61.6 ms                                                  | 87.0 ms: 1.41x slower                                                    |
| bench_mp_pool              | 8.07 ms                                                  | 2.21 sec: 274.13x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.10x slower                                                             |

Benchmark hidden because not significant (27): xml_etree_generate, telco, thrift, coverage, coroutines, sqlite_synth, async_generators, xml_etree_process, k_core, scimark_monte_carlo, sqlalchemy_declarative, unpickle_pure_python, asyncio_websockets, scimark_sparse_mat_mult, deepcopy_reduce, mako, regex_v8, pylint, connected_components, json_loads, python_startup, pidigits, json, nbody, bench_thread_pool, sqlalchemy_imperative, sqlglot_transpile
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (9) of results/bm-20250118-3.14.0a4+-61b35f7-JIT/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.031x slower

# HPT report

- Reliability score: 96.97% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.04x