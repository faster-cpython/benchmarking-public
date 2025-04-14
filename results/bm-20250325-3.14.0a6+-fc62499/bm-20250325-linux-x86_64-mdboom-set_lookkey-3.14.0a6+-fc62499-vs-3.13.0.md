# Results vs. 3.13.0

- fork: mdboom
- ref: set_lookkey
- machine: linux-x86_64
- commit hash: fc62499
- commit date: 2025-03-25
- overall geometric mean: 1.036x faster
- HPT reliability: 99.69%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250325-linux-x86_64-mdboom-set_lookkey-3.14.0a6+-fc62499 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 257 ms: 1.03x faster                                          |
| docutils       | 2.58 sec                                               | 2.62 sec: 1.01x slower                                        |
| html5lib       | 63.4 ms                                                | 61.7 ms: 1.03x faster                                         |
| sphinx         | 1.03 sec                                               | 1.02 sec: 1.02x faster                                        |
| Geometric mean | (ref)                                                  | 1.02x faster                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250325-linux-x86_64-mdboom-set_lookkey-3.14.0a6+-fc62499 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 309 ms: 1.50x faster                                          |
| async_tree_io_tg           | 861 ms                                                 | 611 ms: 1.41x faster                                          |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                          |
| async_tree_io              | 838 ms                                                 | 610 ms: 1.37x faster                                          |
| async_tree_none            | 350 ms                                                 | 257 ms: 1.36x faster                                          |
| async_tree_none_tg         | 319 ms                                                 | 247 ms: 1.29x faster                                          |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 489 ms: 1.17x faster                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 472 ms: 1.15x faster                                          |
| async_generators           | 433 ms                                                 | 398 ms: 1.09x faster                                          |
| coroutines                 | 22.2 ms                                                | 24.2 ms: 1.09x slower                                         |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                  |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250325-linux-x86_64-mdboom-set_lookkey-3.14.0a6+-fc62499 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 78.7 ms                                                | 70.0 ms: 1.12x faster                                         |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                          |
| nbody          | 87.7 ms                                                | 99.9 ms: 1.14x slower                                         |
| Geometric mean | (ref)                                                  | 1.00x slower                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250325-linux-x86_64-mdboom-set_lookkey-3.14.0a6+-fc62499 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.30 ms: 1.14x faster                                         |
| regex_v8       | 26.9 ms                                                | 24.0 ms: 1.12x faster                                         |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                          |
| Geometric mean | (ref)                                                  | 1.08x faster                                                  |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250325-linux-x86_64-mdboom-set_lookkey-3.14.0a6+-fc62499 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 140 ms: 1.10x faster                                          |
| tomli_loads          | 2.12 sec                                               | 2.02 sec: 1.05x faster                                        |
| xml_etree_generate   | 86.8 ms                                                | 84.2 ms: 1.03x faster                                         |
| xml_etree_process    | 60.5 ms                                                | 58.7 ms: 1.03x faster                                         |
| xml_etree_iterparse  | 101 ms                                                 | 98.8 ms: 1.02x faster                                         |
| unpickle_pure_python | 213 us                                                 | 221 us: 1.04x slower                                          |
| pickle_pure_python   | 302 us                                                 | 315 us: 1.04x slower                                          |
| json_loads           | 27.2 us                                                | 30.0 us: 1.10x slower                                         |
| json_dumps           | 10.1 ms                                                | 11.5 ms: 1.13x slower                                         |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250325-linux-x86_64-mdboom-set_lookkey-3.14.0a6+-fc62499 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.2 ms: 1.04x slower                                         |
| python_startup_no_site | 7.00 ms                                                | 8.22 ms: 1.17x slower                                         |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250325-linux-x86_64-mdboom-set_lookkey-3.14.0a6+-fc62499 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.2 ms: 1.07x faster                                         |
| genshi_xml      | 50.5 ms                                                | 49.2 ms: 1.02x faster                                         |
| django_template | 31.7 ms                                                | 31.4 ms: 1.01x faster                                         |
| mako            | 10.7 ms                                                | 11.2 ms: 1.05x slower                                         |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250325-linux-x86_64-mdboom-set_lookkey-3.14.0a6+-fc62499 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 309 ms: 1.50x faster                                          |
| async_tree_io_tg           | 861 ms                                                 | 611 ms: 1.41x faster                                          |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                          |
| deepcopy                   | 354 us                                                 | 256 us: 1.38x faster                                          |
| async_tree_io              | 838 ms                                                 | 610 ms: 1.37x faster                                          |
| async_tree_none            | 350 ms                                                 | 257 ms: 1.36x faster                                          |
| deepcopy_memo              | 38.4 us                                                | 29.6 us: 1.30x faster                                         |
| async_tree_none_tg         | 319 ms                                                 | 247 ms: 1.29x faster                                          |
| go                         | 141 ms                                                 | 114 ms: 1.23x faster                                          |
| deepcopy_reduce            | 3.24 us                                                | 2.70 us: 1.20x faster                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 489 ms: 1.17x faster                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 472 ms: 1.15x faster                                          |
| regex_effbot               | 3.77 ms                                                | 3.30 ms: 1.14x faster                                         |
| float                      | 78.7 ms                                                | 70.0 ms: 1.12x faster                                         |
| regex_v8                   | 26.9 ms                                                | 24.0 ms: 1.12x faster                                         |
| pylint                     | 312 ms                                                 | 279 ms: 1.12x faster                                          |
| spectral_norm              | 113 ms                                                 | 102 ms: 1.11x faster                                          |
| xml_etree_parse            | 154 ms                                                 | 140 ms: 1.10x faster                                          |
| richards                   | 47.5 ms                                                | 43.6 ms: 1.09x faster                                         |
| async_generators           | 433 ms                                                 | 398 ms: 1.09x faster                                          |
| logging_silent             | 101 ns                                                 | 93.0 ns: 1.09x faster                                         |
| richards_super             | 53.7 ms                                                | 49.9 ms: 1.08x faster                                         |
| dulwich_log                | 64.6 ms                                                | 60.1 ms: 1.08x faster                                         |
| telco                      | 8.40 ms                                                | 7.84 ms: 1.07x faster                                         |
| genshi_text                | 22.6 ms                                                | 21.2 ms: 1.07x faster                                         |
| pycparser                  | 1.20 sec                                               | 1.13 sec: 1.06x faster                                        |
| sqlite_synth               | 2.90 us                                                | 2.77 us: 1.05x faster                                         |
| tomli_loads                | 2.12 sec                                               | 2.02 sec: 1.05x faster                                        |
| pathlib                    | 17.4 ms                                                | 16.6 ms: 1.05x faster                                         |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                          |
| thrift                     | 800 us                                                 | 770 us: 1.04x faster                                          |
| deltablue                  | 3.19 ms                                                | 3.08 ms: 1.04x faster                                         |
| 2to3                       | 266 ms                                                 | 257 ms: 1.03x faster                                          |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.03x faster                                        |
| xml_etree_generate         | 86.8 ms                                                | 84.2 ms: 1.03x faster                                         |
| xml_etree_process          | 60.5 ms                                                | 58.7 ms: 1.03x faster                                         |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.89 ms: 1.03x faster                                         |
| html5lib                   | 63.4 ms                                                | 61.7 ms: 1.03x faster                                         |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.03x faster                                          |
| genshi_xml                 | 50.5 ms                                                | 49.2 ms: 1.02x faster                                         |
| scimark_fft                | 367 ms                                                 | 358 ms: 1.02x faster                                          |
| xml_etree_iterparse        | 101 ms                                                 | 98.8 ms: 1.02x faster                                         |
| sphinx                     | 1.03 sec                                               | 1.02 sec: 1.02x faster                                        |
| bpe_tokeniser              | 4.69 sec                                               | 4.62 sec: 1.01x faster                                        |
| sympy_str                  | 273 ms                                                 | 269 ms: 1.01x faster                                          |
| mdp                        | 2.54 sec                                               | 2.51 sec: 1.01x faster                                        |
| logging_simple             | 5.65 us                                                | 5.60 us: 1.01x faster                                         |
| django_template            | 31.7 ms                                                | 31.4 ms: 1.01x faster                                         |
| sqlalchemy_declarative     | 133 ms                                                 | 132 ms: 1.01x faster                                          |
| sympy_integrate            | 19.8 ms                                                | 19.7 ms: 1.01x faster                                         |
| typing_runtime_protocols   | 160 us                                                 | 159 us: 1.01x faster                                          |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                          |
| generators                 | 28.8 ms                                                | 28.9 ms: 1.00x slower                                         |
| comprehensions             | 16.5 us                                                | 16.6 us: 1.01x slower                                         |
| logging_format             | 6.23 us                                                | 6.28 us: 1.01x slower                                         |
| sympy_sum                  | 150 ms                                                 | 152 ms: 1.01x slower                                          |
| pprint_pformat             | 1.48 sec                                               | 1.49 sec: 1.01x slower                                        |
| meteor_contest             | 108 ms                                                 | 110 ms: 1.01x slower                                          |
| raytrace                   | 262 ms                                                 | 265 ms: 1.01x slower                                          |
| scimark_lu                 | 114 ms                                                 | 116 ms: 1.01x slower                                          |
| docutils                   | 2.58 sec                                               | 2.62 sec: 1.01x slower                                        |
| shortest_path              | 487 ms                                                 | 494 ms: 1.02x slower                                          |
| create_gc_cycles           | 2.45 ms                                                | 2.49 ms: 1.02x slower                                         |
| gc_traversal               | 4.90 ms                                                | 4.99 ms: 1.02x slower                                         |
| scimark_monte_carlo        | 66.8 ms                                                | 68.2 ms: 1.02x slower                                         |
| connected_components       | 447 ms                                                 | 457 ms: 1.02x slower                                          |
| chaos                      | 58.0 ms                                                | 59.6 ms: 1.03x slower                                         |
| crypto_pyaes               | 74.7 ms                                                | 77.3 ms: 1.04x slower                                         |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.5 ms: 1.04x slower                                         |
| unpickle_pure_python       | 213 us                                                 | 221 us: 1.04x slower                                          |
| nqueens                    | 80.9 ms                                                | 84.2 ms: 1.04x slower                                         |
| hexiom                     | 6.08 ms                                                | 6.33 ms: 1.04x slower                                         |
| pickle_pure_python         | 302 us                                                 | 315 us: 1.04x slower                                          |
| python_startup             | 12.7 ms                                                | 13.2 ms: 1.04x slower                                         |
| mako                       | 10.7 ms                                                | 11.2 ms: 1.05x slower                                         |
| bench_thread_pool          | 818 us                                                 | 880 us: 1.08x slower                                          |
| coroutines                 | 22.2 ms                                                | 24.2 ms: 1.09x slower                                         |
| json_loads                 | 27.2 us                                                | 30.0 us: 1.10x slower                                         |
| fannkuch                   | 394 ms                                                 | 437 ms: 1.11x slower                                          |
| coverage                   | 82.8 ms                                                | 92.4 ms: 1.12x slower                                         |
| many_optionals             | 857 us                                                 | 968 us: 1.13x slower                                          |
| json_dumps                 | 10.1 ms                                                | 11.5 ms: 1.13x slower                                         |
| nbody                      | 87.7 ms                                                | 99.9 ms: 1.14x slower                                         |
| python_startup_no_site     | 7.00 ms                                                | 8.22 ms: 1.17x slower                                         |
| subparsers                 | 15.5 ms                                                | 20.8 ms: 1.34x slower                                         |
| bench_mp_pool              | 24.0 ms                                                | 84.1 ms: 3.51x slower                                         |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                  |

Benchmark hidden because not significant (6): regex_dna, sympy_expand, pyflate, pprint_safe_repr, asyncio_websockets, json
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250325-3.14.0a6+-fc62499/bm-20250325-linux-x86_64-mdboom-set_lookkey-3.14.0a6+-fc62499.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.036x faster

# HPT report

- Reliability score: 99.69% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.03x