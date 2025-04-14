# Results vs. 3.13.0

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: linux-aarch64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.038x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.01 sec: 1.02x slower                                                   |
| html5lib       | 65.6 ms                                                  | 62.9 ms: 1.04x faster                                                    |
| sphinx         | 1.20 sec                                                 | 1.16 sec: 1.03x faster                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                             |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 493 ms: 1.34x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 503 ms: 1.32x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 928 ms: 1.25x faster                                                     |
| async_tree_none            | 504 ms                                                   | 403 ms: 1.25x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 392 ms: 1.23x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 926 ms: 1.23x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 680 ms: 1.18x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 691 ms: 1.14x faster                                                     |
| async_generators           | 500 ms                                                   | 454 ms: 1.10x faster                                                     |
| Geometric mean             | (ref)                                                    | 1.18x faster                                                             |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 86.5 ms: 1.11x faster                                                    |
| Geometric mean | (ref)                                                    | 1.02x faster                                                             |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.14 ms: 1.23x faster                                                    |
| Geometric mean | (ref)                                                    | 1.07x faster                                                             |

Benchmark hidden because not significant (3): regex_compile, regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse | 203 ms                                                   | 185 ms: 1.09x faster                                                     |
| tomli_loads     | 2.67 sec                                                 | 2.53 sec: 1.06x faster                                                   |
| json_loads      | 32.8 us                                                  | 35.3 us: 1.08x slower                                                    |
| Geometric mean  | (ref)                                                    | 1.00x slower                                                             |

Benchmark hidden because not significant (6): xml_etree_generate, xml_etree_iterparse, xml_etree_process, unpickle_pure_python, pickle_pure_python, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 9.05 ms: 1.03x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.03x slower                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_text, mako, django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy                   | 479 us                                                   | 339 us: 1.41x faster                                                     |
| async_tree_memoization_tg  | 663 ms                                                   | 493 ms: 1.34x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 503 ms: 1.32x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 40.6 us: 1.30x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 928 ms: 1.25x faster                                                     |
| async_tree_none            | 504 ms                                                   | 403 ms: 1.25x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 392 ms: 1.23x faster                                                     |
| regex_effbot               | 5.10 ms                                                  | 4.14 ms: 1.23x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 926 ms: 1.23x faster                                                     |
| spectral_norm              | 143 ms                                                   | 119 ms: 1.20x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 680 ms: 1.18x faster                                                     |
| go                         | 164 ms                                                   | 140 ms: 1.17x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 691 ms: 1.14x faster                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 3.72 us: 1.14x faster                                                    |
| pylint                     | 345 ms                                                   | 304 ms: 1.14x faster                                                     |
| pathlib                    | 24.3 ms                                                  | 21.9 ms: 1.11x faster                                                    |
| float                      | 95.8 ms                                                  | 86.5 ms: 1.11x faster                                                    |
| telco                      | 10.5 ms                                                  | 9.46 ms: 1.11x faster                                                    |
| async_generators           | 500 ms                                                   | 454 ms: 1.10x faster                                                     |
| generators                 | 40.3 ms                                                  | 36.8 ms: 1.10x faster                                                    |
| xml_etree_parse            | 203 ms                                                   | 185 ms: 1.09x faster                                                     |
| bpe_tokeniser              | 6.02 sec                                                 | 5.58 sec: 1.08x faster                                                   |
| sqlglot_optimize           | 65.2 ms                                                  | 60.8 ms: 1.07x faster                                                    |
| scimark_fft                | 463 ms                                                   | 434 ms: 1.07x faster                                                     |
| sqlalchemy_declarative     | 154 ms                                                   | 145 ms: 1.06x faster                                                     |
| tomli_loads                | 2.67 sec                                                 | 2.53 sec: 1.06x faster                                                   |
| pyflate                    | 582 ms                                                   | 552 ms: 1.05x faster                                                     |
| pycparser                  | 1.34 sec                                                 | 1.28 sec: 1.05x faster                                                   |
| k_core                     | 2.99 sec                                                 | 2.85 sec: 1.05x faster                                                   |
| html5lib                   | 65.6 ms                                                  | 62.9 ms: 1.04x faster                                                    |
| sphinx                     | 1.20 sec                                                 | 1.16 sec: 1.03x faster                                                   |
| mdp                        | 3.45 sec                                                 | 3.35 sec: 1.03x faster                                                   |
| sympy_str                  | 265 ms                                                   | 261 ms: 1.01x faster                                                     |
| docutils                   | 2.96 sec                                                 | 3.01 sec: 1.02x slower                                                   |
| python_startup_no_site     | 8.79 ms                                                  | 9.05 ms: 1.03x slower                                                    |
| create_gc_cycles           | 3.39 ms                                                  | 3.59 ms: 1.06x slower                                                    |
| json_loads                 | 32.8 us                                                  | 35.3 us: 1.08x slower                                                    |
| gc_traversal               | 5.92 ms                                                  | 7.01 ms: 1.18x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 25.9 ms: 1.27x slower                                                    |
| many_optionals             | 626 us                                                   | 841 us: 1.34x slower                                                     |
| bench_mp_pool              | 8.07 ms                                                  | 5.97 sec: 739.52x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.03x slower                                                             |

Benchmark hidden because not significant (54): regex_compile, sympy_sum, scimark_sor, sqlalchemy_imperative, scimark_sparse_mat_mult, genshi_text, nqueens, xml_etree_generate, richards, scimark_lu, meteor_contest, sympy_expand, 2to3, sqlglot_parse, coverage, thrift, scimark_monte_carlo, connected_components, sqlglot_transpile, chaos, regex_dna, pprint_pformat, pprint_safe_repr, deltablue, richards_super, asyncio_websockets, regex_v8, typing_runtime_protocols, bench_thread_pool, coroutines, logging_format, sqlglot_normalize, mako, django_template, xml_etree_iterparse, xml_etree_process, unpickle_pure_python, logging_simple, sympy_integrate, logging_silent, sqlite_synth, shortest_path, nbody, hexiom, fannkuch, crypto_pyaes, pidigits, python_startup, comprehensions, json, raytrace, pickle_pure_python, genshi_xml, json_dumps
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (9) of results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.038x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.03x