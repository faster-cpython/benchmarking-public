# Results vs. 3.13.0

- fork: iritkatriel
- ref: stats
- machine: linux-x86_64
- commit hash: fb33c24
- commit date: 2025-02-21
- overall geometric mean: 1.042x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 256 ms: 1.04x faster                                         |
| docutils       | 2.58 sec                                               | 2.62 sec: 1.01x slower                                       |
| html5lib       | 63.4 ms                                                | 61.6 ms: 1.03x faster                                        |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                       |
| Geometric mean | (ref)                                                  | 1.02x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 319 ms: 1.45x faster                                         |
| async_tree_io_tg           | 861 ms                                                 | 612 ms: 1.41x faster                                         |
| async_tree_io              | 838 ms                                                 | 611 ms: 1.37x faster                                         |
| async_tree_memoization     | 437 ms                                                 | 320 ms: 1.36x faster                                         |
| async_tree_none            | 350 ms                                                 | 260 ms: 1.35x faster                                         |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 493 ms: 1.16x faster                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 476 ms: 1.14x faster                                         |
| async_generators           | 433 ms                                                 | 387 ms: 1.12x faster                                         |
| coroutines                 | 22.2 ms                                                | 23.8 ms: 1.07x slower                                        |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 78.7 ms                                                | 72.7 ms: 1.08x faster                                        |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                         |
| nbody          | 87.7 ms                                                | 97.6 ms: 1.11x slower                                        |
| Geometric mean | (ref)                                                  | 1.01x slower                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.3 ms: 1.15x faster                                        |
| regex_effbot   | 3.77 ms                                                | 3.46 ms: 1.09x faster                                        |
| regex_compile  | 132 ms                                                 | 126 ms: 1.05x faster                                         |
| Geometric mean | (ref)                                                  | 1.07x faster                                                 |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 139 ms: 1.11x faster                                         |
| tomli_loads          | 2.12 sec                                               | 1.96 sec: 1.08x faster                                       |
| xml_etree_generate   | 86.8 ms                                                | 83.9 ms: 1.04x faster                                        |
| xml_etree_iterparse  | 101 ms                                                 | 98.1 ms: 1.03x faster                                        |
| xml_etree_process    | 60.5 ms                                                | 58.7 ms: 1.03x faster                                        |
| unpickle_pure_python | 213 us                                                 | 222 us: 1.04x slower                                         |
| pickle_pure_python   | 302 us                                                 | 319 us: 1.05x slower                                         |
| json_loads           | 27.2 us                                                | 29.7 us: 1.09x slower                                        |
| json_dumps           | 10.1 ms                                                | 11.8 ms: 1.16x slower                                        |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.06 ms: 1.01x slower                                        |
| python_startup         | 12.7 ms                                                | 12.9 ms: 1.02x slower                                        |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.9 ms: 1.03x faster                                        |
| genshi_xml      | 50.5 ms                                                | 49.5 ms: 1.02x faster                                        |
| django_template | 31.7 ms                                                | 31.8 ms: 1.01x slower                                        |
| mako            | 10.7 ms                                                | 11.2 ms: 1.05x slower                                        |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 319 ms: 1.45x faster                                         |
| async_tree_io_tg           | 861 ms                                                 | 612 ms: 1.41x faster                                         |
| deepcopy                   | 354 us                                                 | 257 us: 1.38x faster                                         |
| async_tree_io              | 838 ms                                                 | 611 ms: 1.37x faster                                         |
| async_tree_memoization     | 437 ms                                                 | 320 ms: 1.36x faster                                         |
| async_tree_none            | 350 ms                                                 | 260 ms: 1.35x faster                                         |
| deepcopy_memo              | 38.4 us                                                | 30.1 us: 1.27x faster                                        |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                         |
| deepcopy_reduce            | 3.24 us                                                | 2.66 us: 1.22x faster                                        |
| go                         | 141 ms                                                 | 118 ms: 1.19x faster                                         |
| spectral_norm              | 113 ms                                                 | 97.4 ms: 1.16x faster                                        |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 493 ms: 1.16x faster                                         |
| regex_v8                   | 26.9 ms                                                | 23.3 ms: 1.15x faster                                        |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 476 ms: 1.14x faster                                         |
| pylint                     | 312 ms                                                 | 275 ms: 1.14x faster                                         |
| async_generators           | 433 ms                                                 | 387 ms: 1.12x faster                                         |
| xml_etree_parse            | 154 ms                                                 | 139 ms: 1.11x faster                                         |
| regex_effbot               | 3.77 ms                                                | 3.46 ms: 1.09x faster                                        |
| float                      | 78.7 ms                                                | 72.7 ms: 1.08x faster                                        |
| tomli_loads                | 2.12 sec                                               | 1.96 sec: 1.08x faster                                       |
| richards                   | 47.5 ms                                                | 44.4 ms: 1.07x faster                                        |
| telco                      | 8.40 ms                                                | 7.84 ms: 1.07x faster                                        |
| richards_super             | 53.7 ms                                                | 50.7 ms: 1.06x faster                                        |
| scimark_fft                | 367 ms                                                 | 348 ms: 1.05x faster                                         |
| sqlite_synth               | 2.90 us                                                | 2.76 us: 1.05x faster                                        |
| thrift                     | 800 us                                                 | 764 us: 1.05x faster                                         |
| regex_compile              | 132 ms                                                 | 126 ms: 1.05x faster                                         |
| bpe_tokeniser              | 4.69 sec                                               | 4.49 sec: 1.05x faster                                       |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.83 ms: 1.04x faster                                        |
| 2to3                       | 266 ms                                                 | 256 ms: 1.04x faster                                         |
| sqlalchemy_declarative     | 133 ms                                                 | 128 ms: 1.04x faster                                         |
| pathlib                    | 17.4 ms                                                | 16.7 ms: 1.04x faster                                        |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                       |
| xml_etree_generate         | 86.8 ms                                                | 83.9 ms: 1.04x faster                                        |
| genshi_text                | 22.6 ms                                                | 21.9 ms: 1.03x faster                                        |
| xml_etree_iterparse        | 101 ms                                                 | 98.1 ms: 1.03x faster                                        |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.4 ms: 1.03x faster                                        |
| xml_etree_process          | 60.5 ms                                                | 58.7 ms: 1.03x faster                                        |
| html5lib                   | 63.4 ms                                                | 61.6 ms: 1.03x faster                                        |
| generators                 | 28.8 ms                                                | 28.0 ms: 1.03x faster                                        |
| connected_components       | 447 ms                                                 | 436 ms: 1.03x faster                                         |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.02x faster                                       |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                         |
| gc_traversal               | 4.90 ms                                                | 4.78 ms: 1.02x faster                                        |
| deltablue                  | 3.19 ms                                                | 3.12 ms: 1.02x faster                                        |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                       |
| shortest_path              | 487 ms                                                 | 476 ms: 1.02x faster                                         |
| sympy_str                  | 273 ms                                                 | 267 ms: 1.02x faster                                         |
| genshi_xml                 | 50.5 ms                                                | 49.5 ms: 1.02x faster                                        |
| mdp                        | 2.54 sec                                               | 2.50 sec: 1.02x faster                                       |
| logging_simple             | 5.65 us                                                | 5.56 us: 1.02x faster                                        |
| dulwich_log                | 64.6 ms                                                | 64.0 ms: 1.01x faster                                        |
| sympy_integrate            | 19.8 ms                                                | 19.7 ms: 1.01x faster                                        |
| pprint_safe_repr           | 727 ms                                                 | 723 ms: 1.01x faster                                         |
| comprehensions             | 16.5 us                                                | 16.4 us: 1.01x faster                                        |
| sympy_expand               | 456 ms                                                 | 454 ms: 1.01x faster                                         |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                         |
| scimark_sor                | 122 ms                                                 | 123 ms: 1.00x slower                                         |
| django_template            | 31.7 ms                                                | 31.8 ms: 1.01x slower                                        |
| scimark_lu                 | 114 ms                                                 | 115 ms: 1.01x slower                                         |
| nqueens                    | 80.9 ms                                                | 81.6 ms: 1.01x slower                                        |
| python_startup_no_site     | 7.00 ms                                                | 7.06 ms: 1.01x slower                                        |
| create_gc_cycles           | 2.45 ms                                                | 2.48 ms: 1.01x slower                                        |
| docutils                   | 2.58 sec                                               | 2.62 sec: 1.01x slower                                       |
| scimark_monte_carlo        | 66.8 ms                                                | 67.8 ms: 1.02x slower                                        |
| python_startup             | 12.7 ms                                                | 12.9 ms: 1.02x slower                                        |
| chaos                      | 58.0 ms                                                | 59.4 ms: 1.02x slower                                        |
| hexiom                     | 6.08 ms                                                | 6.23 ms: 1.02x slower                                        |
| logging_silent             | 101 ns                                                 | 105 ns: 1.04x slower                                         |
| unpickle_pure_python       | 213 us                                                 | 222 us: 1.04x slower                                         |
| raytrace                   | 262 ms                                                 | 273 ms: 1.05x slower                                         |
| mako                       | 10.7 ms                                                | 11.2 ms: 1.05x slower                                        |
| fannkuch                   | 394 ms                                                 | 415 ms: 1.05x slower                                         |
| pickle_pure_python         | 302 us                                                 | 319 us: 1.05x slower                                         |
| bench_thread_pool          | 818 us                                                 | 867 us: 1.06x slower                                         |
| coroutines                 | 22.2 ms                                                | 23.8 ms: 1.07x slower                                        |
| json_loads                 | 27.2 us                                                | 29.7 us: 1.09x slower                                        |
| many_optionals             | 857 us                                                 | 941 us: 1.10x slower                                         |
| coverage                   | 82.8 ms                                                | 91.0 ms: 1.10x slower                                        |
| nbody                      | 87.7 ms                                                | 97.6 ms: 1.11x slower                                        |
| json_dumps                 | 10.1 ms                                                | 11.8 ms: 1.16x slower                                        |
| subparsers                 | 15.5 ms                                                | 20.7 ms: 1.34x slower                                        |
| bench_mp_pool              | 24.0 ms                                                | 83.5 ms: 3.48x slower                                        |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                 |

Benchmark hidden because not significant (9): pprint_pformat, typing_runtime_protocols, logging_format, json, asyncio_websockets, pyflate, crypto_pyaes, regex_dna, meteor_contest
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250221-3.14.0a5+-fb33c24/bm-20250221-linux-x86_64-iritkatriel-stats-3.14.0a5+-fb33c24.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.042x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.03x