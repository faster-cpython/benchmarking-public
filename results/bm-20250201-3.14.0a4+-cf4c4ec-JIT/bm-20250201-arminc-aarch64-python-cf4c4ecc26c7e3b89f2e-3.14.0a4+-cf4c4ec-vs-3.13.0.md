# Results vs. 3.13.0

- fork: python
- ref: cf4c4ecc26c7e3b89f2e
- machine: linux-aarch64
- commit hash: cf4c4ec
- commit date: 2025-02-01
- overall geometric mean: 1.036x slower
- HPT reliability: 93.42%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.30 sec: 1.11x slower                                                   |
| html5lib       | 65.6 ms                                                  | 75.6 ms: 1.15x slower                                                    |
| sphinx         | 1.20 sec                                                 | 1.25 sec: 1.05x slower                                                   |
| Geometric mean | (ref)                                                    | 1.08x slower                                                             |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 514 ms: 1.29x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 528 ms: 1.26x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 944 ms: 1.23x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 404 ms: 1.20x faster                                                     |
| async_tree_none            | 504 ms                                                   | 425 ms: 1.18x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 965 ms: 1.18x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 688 ms: 1.16x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 722 ms: 1.09x faster                                                     |
| Geometric mean             | (ref)                                                    | 1.14x faster                                                             |

Benchmark hidden because not significant (3): async_generators, asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 89.5 ms: 1.07x faster                                                    |
| Geometric mean | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.18 ms: 1.22x faster                                                    |
| regex_compile  | 134 ms                                                   | 146 ms: 1.09x slower                                                     |
| Geometric mean | (ref)                                                    | 1.02x faster                                                             |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 181 ms: 1.12x faster                                                     |
| xml_etree_iterparse | 159 ms                                                   | 147 ms: 1.08x faster                                                     |
| tomli_loads         | 2.67 sec                                                 | 2.56 sec: 1.04x faster                                                   |
| json_loads          | 32.8 us                                                  | 35.6 us: 1.08x slower                                                    |
| pickle_pure_python  | 374 us                                                   | 406 us: 1.09x slower                                                     |
| Geometric mean      | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (4): xml_etree_generate, xml_etree_process, json_dumps, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 9.05 ms: 1.03x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.03x slower                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 28.6 ms                                                  | 33.8 ms: 1.18x slower                                                    |
| django_template | 39.4 ms                                                  | 48.3 ms: 1.22x slower                                                    |
| genshi_xml      | 61.6 ms                                                  | 85.8 ms: 1.39x slower                                                    |
| Geometric mean  | (ref)                                                    | 1.19x slower                                                             |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 514 ms: 1.29x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 528 ms: 1.26x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 944 ms: 1.23x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 43.1 us: 1.23x faster                                                    |
| regex_effbot               | 5.10 ms                                                  | 4.18 ms: 1.22x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 404 ms: 1.20x faster                                                     |
| async_tree_none            | 504 ms                                                   | 425 ms: 1.18x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 965 ms: 1.18x faster                                                     |
| deepcopy                   | 479 us                                                   | 409 us: 1.17x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 688 ms: 1.16x faster                                                     |
| xml_etree_parse            | 203 ms                                                   | 181 ms: 1.12x faster                                                     |
| scimark_fft                | 463 ms                                                   | 422 ms: 1.10x faster                                                     |
| pathlib                    | 24.3 ms                                                  | 22.2 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 722 ms: 1.09x faster                                                     |
| xml_etree_iterparse        | 159 ms                                                   | 147 ms: 1.08x faster                                                     |
| float                      | 95.8 ms                                                  | 89.5 ms: 1.07x faster                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 5.70 sec: 1.05x faster                                                   |
| tomli_loads                | 2.67 sec                                                 | 2.56 sec: 1.04x faster                                                   |
| k_core                     | 2.99 sec                                                 | 2.91 sec: 1.03x faster                                                   |
| shortest_path              | 565 ms                                                   | 579 ms: 1.03x slower                                                     |
| python_startup_no_site     | 8.79 ms                                                  | 9.05 ms: 1.03x slower                                                    |
| mdp                        | 3.45 sec                                                 | 3.55 sec: 1.03x slower                                                   |
| go                         | 164 ms                                                   | 170 ms: 1.04x slower                                                     |
| pyflate                    | 582 ms                                                   | 605 ms: 1.04x slower                                                     |
| sphinx                     | 1.20 sec                                                 | 1.25 sec: 1.05x slower                                                   |
| create_gc_cycles           | 3.39 ms                                                  | 3.60 ms: 1.06x slower                                                    |
| fannkuch                   | 478 ms                                                   | 508 ms: 1.06x slower                                                     |
| sqlalchemy_imperative      | 16.1 ms                                                  | 17.1 ms: 1.06x slower                                                    |
| sqlglot_normalize          | 131 ms                                                   | 140 ms: 1.07x slower                                                     |
| sympy_sum                  | 151 ms                                                   | 162 ms: 1.07x slower                                                     |
| sympy_integrate            | 21.4 ms                                                  | 23.1 ms: 1.08x slower                                                    |
| meteor_contest             | 117 ms                                                   | 126 ms: 1.08x slower                                                     |
| sqlglot_optimize           | 65.2 ms                                                  | 70.6 ms: 1.08x slower                                                    |
| json_loads                 | 32.8 us                                                  | 35.6 us: 1.08x slower                                                    |
| pickle_pure_python         | 374 us                                                   | 406 us: 1.09x slower                                                     |
| regex_compile              | 134 ms                                                   | 146 ms: 1.09x slower                                                     |
| logging_format             | 8.10 us                                                  | 8.83 us: 1.09x slower                                                    |
| scimark_lu                 | 146 ms                                                   | 159 ms: 1.09x slower                                                     |
| sympy_expand               | 472 ms                                                   | 521 ms: 1.10x slower                                                     |
| logging_silent             | 135 ns                                                   | 149 ns: 1.10x slower                                                     |
| docutils                   | 2.96 sec                                                 | 3.30 sec: 1.11x slower                                                   |
| logging_simple             | 7.25 us                                                  | 8.08 us: 1.11x slower                                                    |
| sqlglot_parse              | 1.43 ms                                                  | 1.62 ms: 1.13x slower                                                    |
| deltablue                  | 3.97 ms                                                  | 4.51 ms: 1.14x slower                                                    |
| sympy_str                  | 265 ms                                                   | 303 ms: 1.14x slower                                                     |
| pycparser                  | 1.34 sec                                                 | 1.54 sec: 1.14x slower                                                   |
| html5lib                   | 65.6 ms                                                  | 75.6 ms: 1.15x slower                                                    |
| typing_runtime_protocols   | 197 us                                                   | 227 us: 1.15x slower                                                     |
| gc_traversal               | 5.92 ms                                                  | 6.87 ms: 1.16x slower                                                    |
| raytrace                   | 310 ms                                                   | 361 ms: 1.16x slower                                                     |
| genshi_text                | 28.6 ms                                                  | 33.8 ms: 1.18x slower                                                    |
| crypto_pyaes               | 84.9 ms                                                  | 101 ms: 1.19x slower                                                     |
| comprehensions             | 20.8 us                                                  | 25.1 us: 1.21x slower                                                    |
| django_template            | 39.4 ms                                                  | 48.3 ms: 1.22x slower                                                    |
| chaos                      | 70.7 ms                                                  | 86.7 ms: 1.23x slower                                                    |
| nqueens                    | 105 ms                                                   | 134 ms: 1.28x slower                                                     |
| many_optionals             | 626 us                                                   | 832 us: 1.33x slower                                                     |
| subparsers                 | 20.3 ms                                                  | 27.3 ms: 1.34x slower                                                    |
| pprint_safe_repr           | 962 ms                                                   | 1.30 sec: 1.35x slower                                                   |
| pprint_pformat             | 1.99 sec                                                 | 2.69 sec: 1.36x slower                                                   |
| generators                 | 40.3 ms                                                  | 55.5 ms: 1.38x slower                                                    |
| hexiom                     | 7.34 ms                                                  | 10.2 ms: 1.39x slower                                                    |
| genshi_xml                 | 61.6 ms                                                  | 85.8 ms: 1.39x slower                                                    |
| bench_mp_pool              | 8.07 ms                                                  | 1.56 sec: 193.55x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.10x slower                                                             |

Benchmark hidden because not significant (31): xml_etree_generate, spectral_norm, scimark_sor, telco, xml_etree_process, coverage, pylint, sqlalchemy_declarative, sqlite_synth, async_generators, mako, asyncio_websockets, connected_components, thrift, coroutines, regex_v8, pidigits, json_dumps, scimark_monte_carlo, bench_thread_pool, richards_super, 2to3, python_startup, deepcopy_reduce, regex_dna, nbody, richards, unpickle_pure_python, scimark_sparse_mat_mult, json, sqlglot_transpile
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (9) of results/bm-20250201-3.14.0a4+-cf4c4ec-JIT/bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.036x slower

# HPT report

- Reliability score: 93.42% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.04x