# Results vs. 3.13.0

- fork: mdboom
- ref: aa_test_2025_2
- machine: linux-x86_64
- commit hash: 8ffb2c1
- commit date: 2025-01-23
- overall geometric mean: 1.100x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 309 ms: 1.16x slower                                             |
| docutils       | 2.58 sec                                               | 2.83 sec: 1.09x slower                                           |
| html5lib       | 63.4 ms                                                | 69.0 ms: 1.09x slower                                            |
| sphinx         | 1.03 sec                                               | 1.14 sec: 1.10x slower                                           |
| Geometric mean | (ref)                                                  | 1.11x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_io_tg           | 861 ms                                                 | 551 ms: 1.56x faster                                             |
| async_tree_memoization_tg  | 463 ms                                                 | 321 ms: 1.44x faster                                             |
| async_tree_io              | 838 ms                                                 | 596 ms: 1.41x faster                                             |
| async_tree_none_tg         | 319 ms                                                 | 239 ms: 1.34x faster                                             |
| async_tree_none            | 350 ms                                                 | 287 ms: 1.22x faster                                             |
| async_tree_memoization     | 437 ms                                                 | 366 ms: 1.19x faster                                             |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 480 ms: 1.13x faster                                             |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 528 ms: 1.09x faster                                             |
| async_generators           | 433 ms                                                 | 438 ms: 1.01x slower                                             |
| coroutines                 | 22.2 ms                                                | 26.7 ms: 1.20x slower                                            |
| Geometric mean             | (ref)                                                  | 1.18x faster                                                     |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 181 ms: 1.03x faster                                             |
| float          | 78.7 ms                                                | 79.1 ms: 1.01x slower                                            |
| nbody          | 87.7 ms                                                | 140 ms: 1.60x slower                                             |
| Geometric mean | (ref)                                                  | 1.16x slower                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.48 ms: 1.08x faster                                            |
| regex_v8       | 26.9 ms                                                | 25.3 ms: 1.06x faster                                            |
| regex_dna      | 220 ms                                                 | 223 ms: 1.02x slower                                             |
| regex_compile  | 132 ms                                                 | 150 ms: 1.14x slower                                             |
| Geometric mean | (ref)                                                  | 1.00x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| xml_etree_iterparse  | 101 ms                                                 | 95.2 ms: 1.06x faster                                            |
| xml_etree_parse      | 154 ms                                                 | 147 ms: 1.05x faster                                             |
| xml_etree_generate   | 86.8 ms                                                | 96.3 ms: 1.11x slower                                            |
| tomli_loads          | 2.12 sec                                               | 2.41 sec: 1.14x slower                                           |
| json_loads           | 27.2 us                                                | 31.8 us: 1.17x slower                                            |
| xml_etree_process    | 60.5 ms                                                | 72.1 ms: 1.19x slower                                            |
| pickle_pure_python   | 302 us                                                 | 380 us: 1.26x slower                                             |
| unpickle_pure_python | 213 us                                                 | 270 us: 1.27x slower                                             |
| json_dumps           | 10.1 ms                                                | 12.9 ms: 1.27x slower                                            |
| Geometric mean       | (ref)                                                  | 1.14x slower                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 15.0 ms: 1.19x slower                                            |
| python_startup_no_site | 7.00 ms                                                | 9.34 ms: 1.33x slower                                            |
| Geometric mean         | (ref)                                                  | 1.26x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_xml      | 50.5 ms                                                | 61.4 ms: 1.22x slower                                            |
| genshi_text     | 22.6 ms                                                | 29.0 ms: 1.28x slower                                            |
| django_template | 31.7 ms                                                | 41.7 ms: 1.32x slower                                            |
| mako            | 10.7 ms                                                | 16.5 ms: 1.55x slower                                            |
| Geometric mean  | (ref)                                                  | 1.34x slower                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_io_tg           | 861 ms                                                 | 551 ms: 1.56x faster                                             |
| async_tree_memoization_tg  | 463 ms                                                 | 321 ms: 1.44x faster                                             |
| create_gc_cycles           | 2.45 ms                                                | 1.70 ms: 1.44x faster                                            |
| async_tree_io              | 838 ms                                                 | 596 ms: 1.41x faster                                             |
| async_tree_none_tg         | 319 ms                                                 | 239 ms: 1.34x faster                                             |
| async_tree_none            | 350 ms                                                 | 287 ms: 1.22x faster                                             |
| async_tree_memoization     | 437 ms                                                 | 366 ms: 1.19x faster                                             |
| gc_traversal               | 4.90 ms                                                | 4.17 ms: 1.17x faster                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 480 ms: 1.13x faster                                             |
| deepcopy                   | 354 us                                                 | 318 us: 1.12x faster                                             |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 528 ms: 1.09x faster                                             |
| regex_effbot               | 3.77 ms                                                | 3.48 ms: 1.08x faster                                            |
| xml_etree_iterparse        | 101 ms                                                 | 95.2 ms: 1.06x faster                                            |
| regex_v8                   | 26.9 ms                                                | 25.3 ms: 1.06x faster                                            |
| pathlib                    | 17.4 ms                                                | 16.4 ms: 1.06x faster                                            |
| sqlite_synth               | 2.90 us                                                | 2.75 us: 1.05x faster                                            |
| xml_etree_parse            | 154 ms                                                 | 147 ms: 1.05x faster                                             |
| pidigits                   | 186 ms                                                 | 181 ms: 1.03x faster                                             |
| float                      | 78.7 ms                                                | 79.1 ms: 1.01x slower                                            |
| go                         | 141 ms                                                 | 142 ms: 1.01x slower                                             |
| async_generators           | 433 ms                                                 | 438 ms: 1.01x slower                                             |
| regex_dna                  | 220 ms                                                 | 223 ms: 1.02x slower                                             |
| deepcopy_reduce            | 3.24 us                                                | 3.30 us: 1.02x slower                                            |
| pycparser                  | 1.20 sec                                               | 1.23 sec: 1.02x slower                                           |
| k_core                     | 2.37 sec                                               | 2.46 sec: 1.04x slower                                           |
| deepcopy_memo              | 38.4 us                                                | 39.9 us: 1.04x slower                                            |
| spectral_norm              | 113 ms                                                 | 119 ms: 1.05x slower                                             |
| json                       | 5.32 ms                                                | 5.65 ms: 1.06x slower                                            |
| generators                 | 28.8 ms                                                | 30.8 ms: 1.07x slower                                            |
| bpe_tokeniser              | 4.69 sec                                               | 5.05 sec: 1.08x slower                                           |
| mdp                        | 2.54 sec                                               | 2.74 sec: 1.08x slower                                           |
| telco                      | 8.40 ms                                                | 9.10 ms: 1.08x slower                                            |
| dulwich_log                | 64.6 ms                                                | 70.1 ms: 1.08x slower                                            |
| html5lib                   | 63.4 ms                                                | 69.0 ms: 1.09x slower                                            |
| docutils                   | 2.58 sec                                               | 2.83 sec: 1.09x slower                                           |
| sphinx                     | 1.03 sec                                               | 1.14 sec: 1.10x slower                                           |
| xml_etree_generate         | 86.8 ms                                                | 96.3 ms: 1.11x slower                                            |
| sqlglot_normalize          | 108 ms                                                 | 121 ms: 1.12x slower                                             |
| pyflate                    | 470 ms                                                 | 528 ms: 1.13x slower                                             |
| richards                   | 47.5 ms                                                | 53.8 ms: 1.13x slower                                            |
| tomli_loads                | 2.12 sec                                               | 2.41 sec: 1.14x slower                                           |
| sqlglot_optimize           | 53.4 ms                                                | 60.7 ms: 1.14x slower                                            |
| regex_compile              | 132 ms                                                 | 150 ms: 1.14x slower                                             |
| richards_super             | 53.7 ms                                                | 62.3 ms: 1.16x slower                                            |
| 2to3                       | 266 ms                                                 | 309 ms: 1.16x slower                                             |
| scimark_fft                | 367 ms                                                 | 429 ms: 1.17x slower                                             |
| json_loads                 | 27.2 us                                                | 31.8 us: 1.17x slower                                            |
| scimark_sor                | 122 ms                                                 | 143 ms: 1.17x slower                                             |
| sympy_expand               | 456 ms                                                 | 536 ms: 1.17x slower                                             |
| shortest_path              | 487 ms                                                 | 572 ms: 1.18x slower                                             |
| sympy_str                  | 273 ms                                                 | 321 ms: 1.18x slower                                             |
| connected_components       | 447 ms                                                 | 529 ms: 1.18x slower                                             |
| sympy_sum                  | 150 ms                                                 | 178 ms: 1.18x slower                                             |
| python_startup             | 12.7 ms                                                | 15.0 ms: 1.19x slower                                            |
| pprint_safe_repr           | 727 ms                                                 | 865 ms: 1.19x slower                                             |
| xml_etree_process          | 60.5 ms                                                | 72.1 ms: 1.19x slower                                            |
| logging_silent             | 101 ns                                                 | 121 ns: 1.20x slower                                             |
| thrift                     | 800 us                                                 | 960 us: 1.20x slower                                             |
| coroutines                 | 22.2 ms                                                | 26.7 ms: 1.20x slower                                            |
| sympy_integrate            | 19.8 ms                                                | 23.8 ms: 1.20x slower                                            |
| pprint_pformat             | 1.48 sec                                               | 1.78 sec: 1.20x slower                                           |
| crypto_pyaes               | 74.7 ms                                                | 90.8 ms: 1.22x slower                                            |
| genshi_xml                 | 50.5 ms                                                | 61.4 ms: 1.22x slower                                            |
| logging_simple             | 5.65 us                                                | 6.90 us: 1.22x slower                                            |
| nqueens                    | 80.9 ms                                                | 99.3 ms: 1.23x slower                                            |
| meteor_contest             | 108 ms                                                 | 133 ms: 1.23x slower                                             |
| sqlglot_parse              | 1.26 ms                                                | 1.56 ms: 1.23x slower                                            |
| sqlalchemy_declarative     | 133 ms                                                 | 163 ms: 1.23x slower                                             |
| sqlalchemy_imperative      | 16.9 ms                                                | 20.8 ms: 1.23x slower                                            |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 6.24 ms: 1.24x slower                                            |
| logging_format             | 6.23 us                                                | 7.74 us: 1.24x slower                                            |
| sqlglot_transpile          | 1.57 ms                                                | 1.95 ms: 1.24x slower                                            |
| scimark_lu                 | 114 ms                                                 | 143 ms: 1.25x slower                                             |
| pickle_pure_python         | 302 us                                                 | 380 us: 1.26x slower                                             |
| comprehensions             | 16.5 us                                                | 20.9 us: 1.27x slower                                            |
| unpickle_pure_python       | 213 us                                                 | 270 us: 1.27x slower                                             |
| json_dumps                 | 10.1 ms                                                | 12.9 ms: 1.27x slower                                            |
| chaos                      | 58.0 ms                                                | 74.0 ms: 1.28x slower                                            |
| hexiom                     | 6.08 ms                                                | 7.78 ms: 1.28x slower                                            |
| genshi_text                | 22.6 ms                                                | 29.0 ms: 1.28x slower                                            |
| many_optionals             | 857 us                                                 | 1.10 ms: 1.29x slower                                            |
| coverage                   | 82.8 ms                                                | 108 ms: 1.31x slower                                             |
| fannkuch                   | 394 ms                                                 | 514 ms: 1.31x slower                                             |
| scimark_monte_carlo        | 66.8 ms                                                | 87.3 ms: 1.31x slower                                            |
| django_template            | 31.7 ms                                                | 41.7 ms: 1.32x slower                                            |
| python_startup_no_site     | 7.00 ms                                                | 9.34 ms: 1.33x slower                                            |
| typing_runtime_protocols   | 160 us                                                 | 215 us: 1.34x slower                                             |
| raytrace                   | 262 ms                                                 | 356 ms: 1.36x slower                                             |
| deltablue                  | 3.19 ms                                                | 4.68 ms: 1.47x slower                                            |
| mako                       | 10.7 ms                                                | 16.5 ms: 1.55x slower                                            |
| nbody                      | 87.7 ms                                                | 140 ms: 1.60x slower                                             |
| subparsers                 | 15.5 ms                                                | 24.8 ms: 1.60x slower                                            |
| bench_mp_pool              | 24.0 ms                                                | 89.3 ms: 3.72x slower                                            |
| bench_thread_pool          | 818 us                                                 | 3.50 ms: 4.28x slower                                            |
| Geometric mean             | (ref)                                                  | 1.14x slower                                                     |

Benchmark hidden because not significant (2): asyncio_websockets, pylint
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.100x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.09x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: 1.22x