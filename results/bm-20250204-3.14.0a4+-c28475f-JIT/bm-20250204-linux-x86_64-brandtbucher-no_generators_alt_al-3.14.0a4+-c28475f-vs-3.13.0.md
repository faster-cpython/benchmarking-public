# Results vs. 3.13.0

- fork: brandtbucher
- ref: no_generators_alt_al
- machine: linux-x86_64
- commit hash: c28475f
- commit date: 2025-02-04
- overall geometric mean: 1.041x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-c28475f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 258 ms: 1.03x faster                                                         |
| docutils       | 2.58 sec                                               | 2.69 sec: 1.04x slower                                                       |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-c28475f |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 619 ms: 1.39x faster                                                         |
| async_tree_io              | 838 ms                                                 | 627 ms: 1.34x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 328 ms: 1.33x faster                                                         |
| async_tree_none            | 350 ms                                                 | 269 ms: 1.30x faster                                                         |
| async_tree_none_tg         | 319 ms                                                 | 255 ms: 1.25x faster                                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 494 ms: 1.16x faster                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 478 ms: 1.14x faster                                                         |
| async_generators           | 433 ms                                                 | 405 ms: 1.07x faster                                                         |
| coroutines                 | 22.2 ms                                                | 23.9 ms: 1.07x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-c28475f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 67.2 ms: 1.17x faster                                                        |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| nbody          | 87.7 ms                                                | 90.6 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-c28475f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.31 ms: 1.14x faster                                                        |
| regex_v8       | 26.9 ms                                                | 23.9 ms: 1.12x faster                                                        |
| regex_dna      | 220 ms                                                 | 212 ms: 1.04x faster                                                         |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-c28475f |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.84 sec: 1.15x faster                                                       |
| xml_etree_parse      | 154 ms                                                 | 139 ms: 1.11x faster                                                         |
| xml_etree_generate   | 86.8 ms                                                | 78.6 ms: 1.10x faster                                                        |
| xml_etree_process    | 60.5 ms                                                | 55.3 ms: 1.09x faster                                                        |
| xml_etree_iterparse  | 101 ms                                                 | 94.6 ms: 1.07x faster                                                        |
| unpickle_pure_python | 213 us                                                 | 201 us: 1.06x faster                                                         |
| pickle_pure_python   | 302 us                                                 | 315 us: 1.04x slower                                                         |
| json_loads           | 27.2 us                                                | 29.4 us: 1.08x slower                                                        |
| json_dumps           | 10.1 ms                                                | 11.3 ms: 1.11x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-c28475f |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.07 ms: 1.01x slower                                                        |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-c28475f |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.4 ms: 1.06x faster                                                        |
| mako            | 10.7 ms                                                | 10.1 ms: 1.06x faster                                                        |
| genshi_xml      | 50.5 ms                                                | 49.2 ms: 1.03x faster                                                        |
| django_template | 31.7 ms                                                | 33.2 ms: 1.05x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-c28475f |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 619 ms: 1.39x faster                                                         |
| async_tree_io              | 838 ms                                                 | 627 ms: 1.34x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 328 ms: 1.33x faster                                                         |
| deepcopy                   | 354 us                                                 | 270 us: 1.31x faster                                                         |
| async_tree_none            | 350 ms                                                 | 269 ms: 1.30x faster                                                         |
| deepcopy_memo              | 38.4 us                                                | 30.6 us: 1.25x faster                                                        |
| async_tree_none_tg         | 319 ms                                                 | 255 ms: 1.25x faster                                                         |
| scimark_fft                | 367 ms                                                 | 309 ms: 1.19x faster                                                         |
| spectral_norm              | 113 ms                                                 | 96.5 ms: 1.17x faster                                                        |
| float                      | 78.7 ms                                                | 67.2 ms: 1.17x faster                                                        |
| deepcopy_reduce            | 3.24 us                                                | 2.78 us: 1.17x faster                                                        |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 494 ms: 1.16x faster                                                         |
| tomli_loads                | 2.12 sec                                               | 1.84 sec: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 478 ms: 1.14x faster                                                         |
| regex_effbot               | 3.77 ms                                                | 3.31 ms: 1.14x faster                                                        |
| regex_v8                   | 26.9 ms                                                | 23.9 ms: 1.12x faster                                                        |
| pylint                     | 312 ms                                                 | 279 ms: 1.12x faster                                                         |
| go                         | 141 ms                                                 | 126 ms: 1.11x faster                                                         |
| xml_etree_parse            | 154 ms                                                 | 139 ms: 1.11x faster                                                         |
| xml_etree_generate         | 86.8 ms                                                | 78.6 ms: 1.10x faster                                                        |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.59 ms: 1.10x faster                                                        |
| xml_etree_process          | 60.5 ms                                                | 55.3 ms: 1.09x faster                                                        |
| richards                   | 47.5 ms                                                | 43.6 ms: 1.09x faster                                                        |
| telco                      | 8.40 ms                                                | 7.74 ms: 1.08x faster                                                        |
| scimark_sor                | 122 ms                                                 | 113 ms: 1.08x faster                                                         |
| richards_super             | 53.7 ms                                                | 50.0 ms: 1.08x faster                                                        |
| bpe_tokeniser              | 4.69 sec                                               | 4.37 sec: 1.07x faster                                                       |
| pathlib                    | 17.4 ms                                                | 16.2 ms: 1.07x faster                                                        |
| xml_etree_iterparse        | 101 ms                                                 | 94.6 ms: 1.07x faster                                                        |
| async_generators           | 433 ms                                                 | 405 ms: 1.07x faster                                                         |
| scimark_monte_carlo        | 66.8 ms                                                | 62.6 ms: 1.07x faster                                                        |
| crypto_pyaes               | 74.7 ms                                                | 70.0 ms: 1.07x faster                                                        |
| unpickle_pure_python       | 213 us                                                 | 201 us: 1.06x faster                                                         |
| sqlite_synth               | 2.90 us                                                | 2.74 us: 1.06x faster                                                        |
| genshi_text                | 22.6 ms                                                | 21.4 ms: 1.06x faster                                                        |
| mako                       | 10.7 ms                                                | 10.1 ms: 1.06x faster                                                        |
| pyflate                    | 470 ms                                                 | 448 ms: 1.05x faster                                                         |
| pycparser                  | 1.20 sec                                               | 1.15 sec: 1.05x faster                                                       |
| thrift                     | 800 us                                                 | 766 us: 1.04x faster                                                         |
| regex_dna                  | 220 ms                                                 | 212 ms: 1.04x faster                                                         |
| k_core                     | 2.37 sec                                               | 2.30 sec: 1.03x faster                                                       |
| 2to3                       | 266 ms                                                 | 258 ms: 1.03x faster                                                         |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                                         |
| genshi_xml                 | 50.5 ms                                                | 49.2 ms: 1.03x faster                                                        |
| connected_components       | 447 ms                                                 | 437 ms: 1.02x faster                                                         |
| json                       | 5.32 ms                                                | 5.21 ms: 1.02x faster                                                        |
| sqlalchemy_declarative     | 133 ms                                                 | 130 ms: 1.02x faster                                                         |
| shortest_path              | 487 ms                                                 | 478 ms: 1.02x faster                                                         |
| fannkuch                   | 394 ms                                                 | 388 ms: 1.02x faster                                                         |
| sqlglot_normalize          | 108 ms                                                 | 106 ms: 1.01x faster                                                         |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.8 ms: 1.01x faster                                                        |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| sqlglot_optimize           | 53.4 ms                                                | 53.6 ms: 1.00x slower                                                        |
| generators                 | 28.8 ms                                                | 28.9 ms: 1.00x slower                                                        |
| chaos                      | 58.0 ms                                                | 58.6 ms: 1.01x slower                                                        |
| python_startup_no_site     | 7.00 ms                                                | 7.07 ms: 1.01x slower                                                        |
| create_gc_cycles           | 2.45 ms                                                | 2.47 ms: 1.01x slower                                                        |
| pprint_pformat             | 1.48 sec                                               | 1.50 sec: 1.01x slower                                                       |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                        |
| sqlglot_parse              | 1.26 ms                                                | 1.28 ms: 1.01x slower                                                        |
| pprint_safe_repr           | 727 ms                                                 | 738 ms: 1.02x slower                                                         |
| dulwich_log                | 64.6 ms                                                | 65.6 ms: 1.02x slower                                                        |
| logging_format             | 6.23 us                                                | 6.35 us: 1.02x slower                                                        |
| sqlglot_transpile          | 1.57 ms                                                | 1.60 ms: 1.02x slower                                                        |
| typing_runtime_protocols   | 160 us                                                 | 164 us: 1.02x slower                                                         |
| sympy_str                  | 273 ms                                                 | 279 ms: 1.02x slower                                                         |
| sympy_sum                  | 150 ms                                                 | 154 ms: 1.03x slower                                                         |
| gc_traversal               | 4.90 ms                                                | 5.04 ms: 1.03x slower                                                        |
| nbody                      | 87.7 ms                                                | 90.6 ms: 1.03x slower                                                        |
| logging_simple             | 5.65 us                                                | 5.85 us: 1.03x slower                                                        |
| sympy_expand               | 456 ms                                                 | 472 ms: 1.03x slower                                                         |
| comprehensions             | 16.5 us                                                | 17.1 us: 1.03x slower                                                        |
| sympy_integrate            | 19.8 ms                                                | 20.6 ms: 1.04x slower                                                        |
| docutils                   | 2.58 sec                                               | 2.69 sec: 1.04x slower                                                       |
| pickle_pure_python         | 302 us                                                 | 315 us: 1.04x slower                                                         |
| django_template            | 31.7 ms                                                | 33.2 ms: 1.05x slower                                                        |
| coroutines                 | 22.2 ms                                                | 23.9 ms: 1.07x slower                                                        |
| json_loads                 | 27.2 us                                                | 29.4 us: 1.08x slower                                                        |
| bench_thread_pool          | 818 us                                                 | 887 us: 1.08x slower                                                         |
| coverage                   | 82.8 ms                                                | 90.6 ms: 1.09x slower                                                        |
| raytrace                   | 262 ms                                                 | 287 ms: 1.10x slower                                                         |
| deltablue                  | 3.19 ms                                                | 3.52 ms: 1.10x slower                                                        |
| logging_silent             | 101 ns                                                 | 111 ns: 1.10x slower                                                         |
| nqueens                    | 80.9 ms                                                | 89.6 ms: 1.11x slower                                                        |
| json_dumps                 | 10.1 ms                                                | 11.3 ms: 1.11x slower                                                        |
| many_optionals             | 857 us                                                 | 956 us: 1.12x slower                                                         |
| hexiom                     | 6.08 ms                                                | 7.39 ms: 1.22x slower                                                        |
| subparsers                 | 15.5 ms                                                | 20.5 ms: 1.33x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 80.6 ms: 3.36x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                 |

Benchmark hidden because not significant (6): scimark_lu, meteor_contest, sphinx, html5lib, asyncio_websockets, mdp
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.041x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x