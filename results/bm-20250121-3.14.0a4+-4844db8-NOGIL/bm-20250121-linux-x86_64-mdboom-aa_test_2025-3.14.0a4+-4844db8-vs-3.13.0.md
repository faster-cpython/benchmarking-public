# Results vs. 3.13.0

- fork: mdboom
- ref: aa_test_2025
- machine: linux-x86_64
- commit hash: 4844db8
- commit date: 2025-01-21
- overall geometric mean: 1.103x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 312 ms: 1.17x slower                                           |
| docutils       | 2.58 sec                                               | 2.87 sec: 1.11x slower                                         |
| html5lib       | 63.4 ms                                                | 70.3 ms: 1.11x slower                                          |
| sphinx         | 1.03 sec                                               | 1.15 sec: 1.12x slower                                         |
| Geometric mean | (ref)                                                  | 1.13x slower                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_io_tg           | 861 ms                                                 | 556 ms: 1.55x faster                                           |
| async_tree_memoization_tg  | 463 ms                                                 | 326 ms: 1.42x faster                                           |
| async_tree_io              | 838 ms                                                 | 606 ms: 1.38x faster                                           |
| async_tree_none_tg         | 319 ms                                                 | 244 ms: 1.31x faster                                           |
| async_tree_none            | 350 ms                                                 | 292 ms: 1.20x faster                                           |
| async_tree_memoization     | 437 ms                                                 | 372 ms: 1.17x faster                                           |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 482 ms: 1.13x faster                                           |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 534 ms: 1.07x faster                                           |
| async_generators           | 433 ms                                                 | 443 ms: 1.02x slower                                           |
| coroutines                 | 22.2 ms                                                | 25.8 ms: 1.16x slower                                          |
| Geometric mean             | (ref)                                                  | 1.17x faster                                                   |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 181 ms: 1.03x faster                                           |
| float          | 78.7 ms                                                | 78.3 ms: 1.00x faster                                          |
| nbody          | 87.7 ms                                                | 137 ms: 1.57x slower                                           |
| Geometric mean | (ref)                                                  | 1.15x slower                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.48 ms: 1.08x faster                                          |
| regex_v8       | 26.9 ms                                                | 25.5 ms: 1.05x faster                                          |
| regex_dna      | 220 ms                                                 | 224 ms: 1.02x slower                                           |
| regex_compile  | 132 ms                                                 | 152 ms: 1.15x slower                                           |
| Geometric mean | (ref)                                                  | 1.01x slower                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| xml_etree_iterparse  | 101 ms                                                 | 95.6 ms: 1.06x faster                                          |
| xml_etree_parse      | 154 ms                                                 | 148 ms: 1.04x faster                                           |
| xml_etree_generate   | 86.8 ms                                                | 96.6 ms: 1.11x slower                                          |
| tomli_loads          | 2.12 sec                                               | 2.43 sec: 1.15x slower                                         |
| json_loads           | 27.2 us                                                | 31.8 us: 1.17x slower                                          |
| xml_etree_process    | 60.5 ms                                                | 72.5 ms: 1.20x slower                                          |
| json_dumps           | 10.1 ms                                                | 12.8 ms: 1.27x slower                                          |
| unpickle_pure_python | 213 us                                                 | 270 us: 1.27x slower                                           |
| pickle_pure_python   | 302 us                                                 | 385 us: 1.27x slower                                           |
| Geometric mean       | (ref)                                                  | 1.14x slower                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 15.1 ms: 1.19x slower                                          |
| python_startup_no_site | 7.00 ms                                                | 9.35 ms: 1.33x slower                                          |
| Geometric mean         | (ref)                                                  | 1.26x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| genshi_xml      | 50.5 ms                                                | 62.1 ms: 1.23x slower                                          |
| genshi_text     | 22.6 ms                                                | 29.5 ms: 1.31x slower                                          |
| django_template | 31.7 ms                                                | 41.6 ms: 1.31x slower                                          |
| mako            | 10.7 ms                                                | 16.4 ms: 1.54x slower                                          |
| Geometric mean  | (ref)                                                  | 1.34x slower                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_io_tg           | 861 ms                                                 | 556 ms: 1.55x faster                                           |
| async_tree_memoization_tg  | 463 ms                                                 | 326 ms: 1.42x faster                                           |
| create_gc_cycles           | 2.45 ms                                                | 1.72 ms: 1.42x faster                                          |
| async_tree_io              | 838 ms                                                 | 606 ms: 1.38x faster                                           |
| async_tree_none_tg         | 319 ms                                                 | 244 ms: 1.31x faster                                           |
| async_tree_none            | 350 ms                                                 | 292 ms: 1.20x faster                                           |
| async_tree_memoization     | 437 ms                                                 | 372 ms: 1.17x faster                                           |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 482 ms: 1.13x faster                                           |
| deepcopy                   | 354 us                                                 | 317 us: 1.12x faster                                           |
| gc_traversal               | 4.90 ms                                                | 4.45 ms: 1.10x faster                                          |
| regex_effbot               | 3.77 ms                                                | 3.48 ms: 1.08x faster                                          |
| pathlib                    | 17.4 ms                                                | 16.1 ms: 1.08x faster                                          |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 534 ms: 1.07x faster                                           |
| sqlite_synth               | 2.90 us                                                | 2.74 us: 1.06x faster                                          |
| xml_etree_iterparse        | 101 ms                                                 | 95.6 ms: 1.06x faster                                          |
| regex_v8                   | 26.9 ms                                                | 25.5 ms: 1.05x faster                                          |
| xml_etree_parse            | 154 ms                                                 | 148 ms: 1.04x faster                                           |
| pidigits                   | 186 ms                                                 | 181 ms: 1.03x faster                                           |
| float                      | 78.7 ms                                                | 78.3 ms: 1.00x faster                                          |
| deepcopy_reduce            | 3.24 us                                                | 3.27 us: 1.01x slower                                          |
| regex_dna                  | 220 ms                                                 | 224 ms: 1.02x slower                                           |
| spectral_norm              | 113 ms                                                 | 116 ms: 1.02x slower                                           |
| async_generators           | 433 ms                                                 | 443 ms: 1.02x slower                                           |
| go                         | 141 ms                                                 | 144 ms: 1.02x slower                                           |
| deepcopy_memo              | 38.4 us                                                | 39.7 us: 1.03x slower                                          |
| pycparser                  | 1.20 sec                                               | 1.24 sec: 1.03x slower                                         |
| k_core                     | 2.37 sec                                               | 2.46 sec: 1.04x slower                                         |
| json                       | 5.32 ms                                                | 5.63 ms: 1.06x slower                                          |
| mdp                        | 2.54 sec                                               | 2.75 sec: 1.08x slower                                         |
| bpe_tokeniser              | 4.69 sec                                               | 5.09 sec: 1.09x slower                                         |
| telco                      | 8.40 ms                                                | 9.14 ms: 1.09x slower                                          |
| dulwich_log                | 64.6 ms                                                | 70.4 ms: 1.09x slower                                          |
| generators                 | 28.8 ms                                                | 31.7 ms: 1.10x slower                                          |
| html5lib                   | 63.4 ms                                                | 70.3 ms: 1.11x slower                                          |
| docutils                   | 2.58 sec                                               | 2.87 sec: 1.11x slower                                         |
| xml_etree_generate         | 86.8 ms                                                | 96.6 ms: 1.11x slower                                          |
| pyflate                    | 470 ms                                                 | 523 ms: 1.11x slower                                           |
| sphinx                     | 1.03 sec                                               | 1.15 sec: 1.12x slower                                         |
| sqlglot_normalize          | 108 ms                                                 | 121 ms: 1.12x slower                                           |
| richards                   | 47.5 ms                                                | 54.2 ms: 1.14x slower                                          |
| scimark_fft                | 367 ms                                                 | 419 ms: 1.14x slower                                           |
| sqlglot_optimize           | 53.4 ms                                                | 61.0 ms: 1.14x slower                                          |
| tomli_loads                | 2.12 sec                                               | 2.43 sec: 1.15x slower                                         |
| regex_compile              | 132 ms                                                 | 152 ms: 1.15x slower                                           |
| coroutines                 | 22.2 ms                                                | 25.8 ms: 1.16x slower                                          |
| logging_silent             | 101 ns                                                 | 117 ns: 1.16x slower                                           |
| scimark_sor                | 122 ms                                                 | 142 ms: 1.16x slower                                           |
| richards_super             | 53.7 ms                                                | 62.8 ms: 1.17x slower                                          |
| sympy_expand               | 456 ms                                                 | 534 ms: 1.17x slower                                           |
| json_loads                 | 27.2 us                                                | 31.8 us: 1.17x slower                                          |
| shortest_path              | 487 ms                                                 | 571 ms: 1.17x slower                                           |
| 2to3                       | 266 ms                                                 | 312 ms: 1.17x slower                                           |
| sympy_str                  | 273 ms                                                 | 322 ms: 1.18x slower                                           |
| connected_components       | 447 ms                                                 | 528 ms: 1.18x slower                                           |
| python_startup             | 12.7 ms                                                | 15.1 ms: 1.19x slower                                          |
| sympy_sum                  | 150 ms                                                 | 180 ms: 1.19x slower                                           |
| pprint_safe_repr           | 727 ms                                                 | 869 ms: 1.20x slower                                           |
| xml_etree_process          | 60.5 ms                                                | 72.5 ms: 1.20x slower                                          |
| pprint_pformat             | 1.48 sec                                               | 1.79 sec: 1.21x slower                                         |
| thrift                     | 800 us                                                 | 968 us: 1.21x slower                                           |
| sympy_integrate            | 19.8 ms                                                | 24.1 ms: 1.21x slower                                          |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 6.12 ms: 1.22x slower                                          |
| crypto_pyaes               | 74.7 ms                                                | 91.3 ms: 1.22x slower                                          |
| nqueens                    | 80.9 ms                                                | 99.1 ms: 1.23x slower                                          |
| logging_simple             | 5.65 us                                                | 6.93 us: 1.23x slower                                          |
| scimark_lu                 | 114 ms                                                 | 140 ms: 1.23x slower                                           |
| genshi_xml                 | 50.5 ms                                                | 62.1 ms: 1.23x slower                                          |
| sqlglot_parse              | 1.26 ms                                                | 1.56 ms: 1.23x slower                                          |
| meteor_contest             | 108 ms                                                 | 134 ms: 1.24x slower                                           |
| sqlalchemy_declarative     | 133 ms                                                 | 165 ms: 1.24x slower                                           |
| sqlalchemy_imperative      | 16.9 ms                                                | 21.1 ms: 1.25x slower                                          |
| logging_format             | 6.23 us                                                | 7.78 us: 1.25x slower                                          |
| sqlglot_transpile          | 1.57 ms                                                | 1.96 ms: 1.25x slower                                          |
| json_dumps                 | 10.1 ms                                                | 12.8 ms: 1.27x slower                                          |
| unpickle_pure_python       | 213 us                                                 | 270 us: 1.27x slower                                           |
| comprehensions             | 16.5 us                                                | 20.9 us: 1.27x slower                                          |
| pickle_pure_python         | 302 us                                                 | 385 us: 1.27x slower                                           |
| fannkuch                   | 394 ms                                                 | 507 ms: 1.29x slower                                           |
| many_optionals             | 857 us                                                 | 1.10 ms: 1.29x slower                                          |
| hexiom                     | 6.08 ms                                                | 7.83 ms: 1.29x slower                                          |
| coverage                   | 82.8 ms                                                | 107 ms: 1.29x slower                                           |
| chaos                      | 58.0 ms                                                | 75.0 ms: 1.29x slower                                          |
| genshi_text                | 22.6 ms                                                | 29.5 ms: 1.31x slower                                          |
| django_template            | 31.7 ms                                                | 41.6 ms: 1.31x slower                                          |
| scimark_monte_carlo        | 66.8 ms                                                | 87.8 ms: 1.31x slower                                          |
| python_startup_no_site     | 7.00 ms                                                | 9.35 ms: 1.33x slower                                          |
| typing_runtime_protocols   | 160 us                                                 | 215 us: 1.34x slower                                           |
| raytrace                   | 262 ms                                                 | 356 ms: 1.36x slower                                           |
| deltablue                  | 3.19 ms                                                | 4.70 ms: 1.47x slower                                          |
| mako                       | 10.7 ms                                                | 16.4 ms: 1.54x slower                                          |
| nbody                      | 87.7 ms                                                | 137 ms: 1.57x slower                                           |
| subparsers                 | 15.5 ms                                                | 24.8 ms: 1.61x slower                                          |
| bench_mp_pool              | 24.0 ms                                                | 89.6 ms: 3.74x slower                                          |
| bench_thread_pool          | 818 us                                                 | 3.49 ms: 4.27x slower                                          |
| Geometric mean             | (ref)                                                  | 1.14x slower                                                   |

Benchmark hidden because not significant (2): asyncio_websockets, pylint
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.103x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.09x
- 95% likely to have a slowdown of 1.09x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: 1.22x