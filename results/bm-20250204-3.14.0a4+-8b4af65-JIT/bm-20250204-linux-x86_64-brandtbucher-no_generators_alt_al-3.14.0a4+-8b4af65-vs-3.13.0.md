# Results vs. 3.13.0

- fork: brandtbucher
- ref: no_generators_alt_al
- machine: linux-x86_64
- commit hash: 8b4af65
- commit date: 2025-02-04
- overall geometric mean: 1.046x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-8b4af65 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 258 ms: 1.03x faster                                                         |
| docutils       | 2.58 sec                                               | 2.69 sec: 1.04x slower                                                       |
| html5lib       | 63.4 ms                                                | 62.7 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-8b4af65 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 618 ms: 1.39x faster                                                         |
| async_tree_io              | 838 ms                                                 | 627 ms: 1.34x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 330 ms: 1.32x faster                                                         |
| async_tree_none            | 350 ms                                                 | 270 ms: 1.30x faster                                                         |
| async_tree_none_tg         | 319 ms                                                 | 255 ms: 1.25x faster                                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 496 ms: 1.16x faster                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 479 ms: 1.13x faster                                                         |
| async_generators           | 433 ms                                                 | 405 ms: 1.07x faster                                                         |
| coroutines                 | 22.2 ms                                                | 22.5 ms: 1.01x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-8b4af65 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 67.6 ms: 1.16x faster                                                        |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| nbody          | 87.7 ms                                                | 90.8 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-8b4af65 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 2.99 ms: 1.26x faster                                                        |
| regex_v8       | 26.9 ms                                                | 23.8 ms: 1.13x faster                                                        |
| regex_dna      | 220 ms                                                 | 195 ms: 1.13x faster                                                         |
| regex_compile  | 132 ms                                                 | 129 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                  | 1.13x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-8b4af65 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.81 sec: 1.17x faster                                                       |
| xml_etree_parse      | 154 ms                                                 | 138 ms: 1.12x faster                                                         |
| xml_etree_generate   | 86.8 ms                                                | 77.7 ms: 1.12x faster                                                        |
| xml_etree_process    | 60.5 ms                                                | 55.0 ms: 1.10x faster                                                        |
| xml_etree_iterparse  | 101 ms                                                 | 95.6 ms: 1.06x faster                                                        |
| unpickle_pure_python | 213 us                                                 | 202 us: 1.06x faster                                                         |
| pickle_pure_python   | 302 us                                                 | 320 us: 1.06x slower                                                         |
| json_loads           | 27.2 us                                                | 28.7 us: 1.06x slower                                                        |
| json_dumps           | 10.1 ms                                                | 11.3 ms: 1.11x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-8b4af65 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.02 ms: 1.00x slower                                                        |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-8b4af65 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 20.9 ms: 1.08x faster                                                        |
| mako            | 10.7 ms                                                | 9.98 ms: 1.07x faster                                                        |
| genshi_xml      | 50.5 ms                                                | 49.1 ms: 1.03x faster                                                        |
| django_template | 31.7 ms                                                | 33.1 ms: 1.04x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-8b4af65 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 618 ms: 1.39x faster                                                         |
| async_tree_io              | 838 ms                                                 | 627 ms: 1.34x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 330 ms: 1.32x faster                                                         |
| deepcopy                   | 354 us                                                 | 271 us: 1.31x faster                                                         |
| async_tree_none            | 350 ms                                                 | 270 ms: 1.30x faster                                                         |
| regex_effbot               | 3.77 ms                                                | 2.99 ms: 1.26x faster                                                        |
| deepcopy_memo              | 38.4 us                                                | 30.5 us: 1.26x faster                                                        |
| async_tree_none_tg         | 319 ms                                                 | 255 ms: 1.25x faster                                                         |
| spectral_norm              | 113 ms                                                 | 95.2 ms: 1.19x faster                                                        |
| scimark_fft                | 367 ms                                                 | 310 ms: 1.18x faster                                                         |
| deepcopy_reduce            | 3.24 us                                                | 2.76 us: 1.17x faster                                                        |
| tomli_loads                | 2.12 sec                                               | 1.81 sec: 1.17x faster                                                       |
| float                      | 78.7 ms                                                | 67.6 ms: 1.16x faster                                                        |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 496 ms: 1.16x faster                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 479 ms: 1.13x faster                                                         |
| regex_v8                   | 26.9 ms                                                | 23.8 ms: 1.13x faster                                                        |
| regex_dna                  | 220 ms                                                 | 195 ms: 1.13x faster                                                         |
| xml_etree_parse            | 154 ms                                                 | 138 ms: 1.12x faster                                                         |
| xml_etree_generate         | 86.8 ms                                                | 77.7 ms: 1.12x faster                                                        |
| pylint                     | 312 ms                                                 | 280 ms: 1.11x faster                                                         |
| go                         | 141 ms                                                 | 126 ms: 1.11x faster                                                         |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.55 ms: 1.11x faster                                                        |
| telco                      | 8.40 ms                                                | 7.61 ms: 1.10x faster                                                        |
| xml_etree_process          | 60.5 ms                                                | 55.0 ms: 1.10x faster                                                        |
| pathlib                    | 17.4 ms                                                | 16.0 ms: 1.09x faster                                                        |
| richards                   | 47.5 ms                                                | 43.9 ms: 1.08x faster                                                        |
| genshi_text                | 22.6 ms                                                | 20.9 ms: 1.08x faster                                                        |
| richards_super             | 53.7 ms                                                | 50.1 ms: 1.07x faster                                                        |
| mako                       | 10.7 ms                                                | 9.98 ms: 1.07x faster                                                        |
| bpe_tokeniser              | 4.69 sec                                               | 4.38 sec: 1.07x faster                                                       |
| async_generators           | 433 ms                                                 | 405 ms: 1.07x faster                                                         |
| scimark_sor                | 122 ms                                                 | 115 ms: 1.07x faster                                                         |
| sqlite_synth               | 2.90 us                                                | 2.73 us: 1.06x faster                                                        |
| scimark_monte_carlo        | 66.8 ms                                                | 62.8 ms: 1.06x faster                                                        |
| xml_etree_iterparse        | 101 ms                                                 | 95.6 ms: 1.06x faster                                                        |
| unpickle_pure_python       | 213 us                                                 | 202 us: 1.06x faster                                                         |
| crypto_pyaes               | 74.7 ms                                                | 71.0 ms: 1.05x faster                                                        |
| pyflate                    | 470 ms                                                 | 454 ms: 1.03x faster                                                         |
| 2to3                       | 266 ms                                                 | 258 ms: 1.03x faster                                                         |
| k_core                     | 2.37 sec                                               | 2.30 sec: 1.03x faster                                                       |
| genshi_xml                 | 50.5 ms                                                | 49.1 ms: 1.03x faster                                                        |
| json                       | 5.32 ms                                                | 5.19 ms: 1.03x faster                                                        |
| sqlglot_normalize          | 108 ms                                                 | 105 ms: 1.02x faster                                                         |
| mdp                        | 2.54 sec                                               | 2.49 sec: 1.02x faster                                                       |
| regex_compile              | 132 ms                                                 | 129 ms: 1.02x faster                                                         |
| thrift                     | 800 us                                                 | 785 us: 1.02x faster                                                         |
| nqueens                    | 80.9 ms                                                | 79.6 ms: 1.02x faster                                                        |
| connected_components       | 447 ms                                                 | 440 ms: 1.02x faster                                                         |
| generators                 | 28.8 ms                                                | 28.4 ms: 1.01x faster                                                        |
| html5lib                   | 63.4 ms                                                | 62.7 ms: 1.01x faster                                                        |
| fannkuch                   | 394 ms                                                 | 390 ms: 1.01x faster                                                         |
| shortest_path              | 487 ms                                                 | 482 ms: 1.01x faster                                                         |
| sqlalchemy_declarative     | 133 ms                                                 | 132 ms: 1.01x faster                                                         |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| python_startup_no_site     | 7.00 ms                                                | 7.02 ms: 1.00x slower                                                        |
| create_gc_cycles           | 2.45 ms                                                | 2.46 ms: 1.00x slower                                                        |
| gc_traversal               | 4.90 ms                                                | 4.93 ms: 1.01x slower                                                        |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                        |
| sympy_sum                  | 150 ms                                                 | 152 ms: 1.01x slower                                                         |
| coroutines                 | 22.2 ms                                                | 22.5 ms: 1.01x slower                                                        |
| sympy_str                  | 273 ms                                                 | 277 ms: 1.02x slower                                                         |
| sqlglot_parse              | 1.26 ms                                                | 1.29 ms: 1.02x slower                                                        |
| logging_simple             | 5.65 us                                                | 5.76 us: 1.02x slower                                                        |
| sqlglot_transpile          | 1.57 ms                                                | 1.60 ms: 1.02x slower                                                        |
| comprehensions             | 16.5 us                                                | 16.9 us: 1.02x slower                                                        |
| pprint_safe_repr           | 727 ms                                                 | 745 ms: 1.03x slower                                                         |
| dulwich_log                | 64.6 ms                                                | 66.3 ms: 1.03x slower                                                        |
| typing_runtime_protocols   | 160 us                                                 | 165 us: 1.03x slower                                                         |
| chaos                      | 58.0 ms                                                | 59.8 ms: 1.03x slower                                                        |
| pprint_pformat             | 1.48 sec                                               | 1.53 sec: 1.03x slower                                                       |
| sympy_integrate            | 19.8 ms                                                | 20.5 ms: 1.03x slower                                                        |
| sympy_expand               | 456 ms                                                 | 472 ms: 1.03x slower                                                         |
| logging_format             | 6.23 us                                                | 6.46 us: 1.04x slower                                                        |
| nbody                      | 87.7 ms                                                | 90.8 ms: 1.04x slower                                                        |
| docutils                   | 2.58 sec                                               | 2.69 sec: 1.04x slower                                                       |
| django_template            | 31.7 ms                                                | 33.1 ms: 1.04x slower                                                        |
| pickle_pure_python         | 302 us                                                 | 320 us: 1.06x slower                                                         |
| json_loads                 | 27.2 us                                                | 28.7 us: 1.06x slower                                                        |
| bench_thread_pool          | 818 us                                                 | 874 us: 1.07x slower                                                         |
| coverage                   | 82.8 ms                                                | 89.6 ms: 1.08x slower                                                        |
| logging_silent             | 101 ns                                                 | 110 ns: 1.09x slower                                                         |
| deltablue                  | 3.19 ms                                                | 3.50 ms: 1.09x slower                                                        |
| raytrace                   | 262 ms                                                 | 287 ms: 1.10x slower                                                         |
| json_dumps                 | 10.1 ms                                                | 11.3 ms: 1.11x slower                                                        |
| many_optionals             | 857 us                                                 | 963 us: 1.12x slower                                                         |
| hexiom                     | 6.08 ms                                                | 7.26 ms: 1.19x slower                                                        |
| subparsers                 | 15.5 ms                                                | 20.6 ms: 1.34x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 80.3 ms: 3.35x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                 |

Benchmark hidden because not significant (7): sphinx, pycparser, meteor_contest, sqlalchemy_imperative, sqlglot_optimize, scimark_lu, asyncio_websockets
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.046x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x