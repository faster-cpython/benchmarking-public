# Results vs. 3.13.0

- fork: brandtbucher
- ref: unbox
- machine: linux-x86_64
- commit hash: 07c4777
- commit date: 2025-04-03
- overall geometric mean: 1.034x faster
- HPT reliability: 92.31%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-brandtbucher-unbox-3.14.0a6+-07c4777 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 260 ms: 1.02x faster                                          |
| docutils       | 2.58 sec                                               | 2.62 sec: 1.01x slower                                        |
| html5lib       | 63.4 ms                                                | 62.7 ms: 1.01x faster                                         |
| Geometric mean | (ref)                                                  | 1.01x faster                                                  |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-brandtbucher-unbox-3.14.0a6+-07c4777 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 323 ms: 1.43x faster                                          |
| async_tree_io_tg           | 861 ms                                                 | 633 ms: 1.36x faster                                          |
| async_tree_memoization     | 437 ms                                                 | 322 ms: 1.36x faster                                          |
| async_tree_io              | 838 ms                                                 | 631 ms: 1.33x faster                                          |
| async_tree_none            | 350 ms                                                 | 265 ms: 1.32x faster                                          |
| async_tree_none_tg         | 319 ms                                                 | 254 ms: 1.26x faster                                          |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 489 ms: 1.17x faster                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 479 ms: 1.13x faster                                          |
| async_generators           | 433 ms                                                 | 394 ms: 1.10x faster                                          |
| coroutines                 | 22.2 ms                                                | 21.2 ms: 1.05x faster                                         |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                  |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-brandtbucher-unbox-3.14.0a6+-07c4777 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 78.7 ms                                                | 74.1 ms: 1.06x faster                                         |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                          |
| nbody          | 87.7 ms                                                | 100 ms: 1.14x slower                                          |
| Geometric mean | (ref)                                                  | 1.03x slower                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-brandtbucher-unbox-3.14.0a6+-07c4777 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 22.7 ms: 1.18x faster                                         |
| regex_effbot   | 3.77 ms                                                | 3.25 ms: 1.16x faster                                         |
| regex_compile  | 132 ms                                                 | 131 ms: 1.01x faster                                          |
| Geometric mean | (ref)                                                  | 1.08x faster                                                  |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-brandtbucher-unbox-3.14.0a6+-07c4777 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.86 sec: 1.14x faster                                        |
| xml_etree_parse      | 154 ms                                                 | 142 ms: 1.09x faster                                          |
| xml_etree_generate   | 86.8 ms                                                | 85.2 ms: 1.02x faster                                         |
| xml_etree_iterparse  | 101 ms                                                 | 99.5 ms: 1.02x faster                                         |
| xml_etree_process    | 60.5 ms                                                | 59.8 ms: 1.01x faster                                         |
| unpickle_pure_python | 213 us                                                 | 222 us: 1.04x slower                                          |
| pickle_pure_python   | 302 us                                                 | 323 us: 1.07x slower                                          |
| json_dumps           | 10.1 ms                                                | 11.3 ms: 1.12x slower                                         |
| json_loads           | 27.2 us                                                | 34.2 us: 1.26x slower                                         |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-brandtbucher-unbox-3.14.0a6+-07c4777 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.04x slower                                         |
| python_startup_no_site | 7.00 ms                                                | 8.20 ms: 1.17x slower                                         |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-brandtbucher-unbox-3.14.0a6+-07c4777 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.9 ms: 1.03x faster                                         |
| genshi_xml      | 50.5 ms                                                | 50.2 ms: 1.01x faster                                         |
| django_template | 31.7 ms                                                | 32.4 ms: 1.02x slower                                         |
| mako            | 10.7 ms                                                | 11.6 ms: 1.09x slower                                         |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-brandtbucher-unbox-3.14.0a6+-07c4777 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.25 sec: 2.04x faster                                        |
| async_tree_memoization_tg  | 463 ms                                                 | 323 ms: 1.43x faster                                          |
| deepcopy                   | 354 us                                                 | 260 us: 1.36x faster                                          |
| async_tree_io_tg           | 861 ms                                                 | 633 ms: 1.36x faster                                          |
| async_tree_memoization     | 437 ms                                                 | 322 ms: 1.36x faster                                          |
| async_tree_io              | 838 ms                                                 | 631 ms: 1.33x faster                                          |
| async_tree_none            | 350 ms                                                 | 265 ms: 1.32x faster                                          |
| deepcopy_memo              | 38.4 us                                                | 30.4 us: 1.26x faster                                         |
| async_tree_none_tg         | 319 ms                                                 | 254 ms: 1.26x faster                                          |
| spectral_norm              | 113 ms                                                 | 92.5 ms: 1.23x faster                                         |
| deepcopy_reduce            | 3.24 us                                                | 2.71 us: 1.20x faster                                         |
| regex_v8                   | 26.9 ms                                                | 22.7 ms: 1.18x faster                                         |
| go                         | 141 ms                                                 | 120 ms: 1.18x faster                                          |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 489 ms: 1.17x faster                                          |
| regex_effbot               | 3.77 ms                                                | 3.25 ms: 1.16x faster                                         |
| tomli_loads                | 2.12 sec                                               | 1.86 sec: 1.14x faster                                        |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 479 ms: 1.13x faster                                          |
| pylint                     | 312 ms                                                 | 281 ms: 1.11x faster                                          |
| async_generators           | 433 ms                                                 | 394 ms: 1.10x faster                                          |
| dulwich_log                | 64.6 ms                                                | 59.4 ms: 1.09x faster                                         |
| xml_etree_parse            | 154 ms                                                 | 142 ms: 1.09x faster                                          |
| float                      | 78.7 ms                                                | 74.1 ms: 1.06x faster                                         |
| telco                      | 8.40 ms                                                | 7.94 ms: 1.06x faster                                         |
| bpe_tokeniser              | 4.69 sec                                               | 4.45 sec: 1.05x faster                                        |
| richards                   | 47.5 ms                                                | 45.3 ms: 1.05x faster                                         |
| coroutines                 | 22.2 ms                                                | 21.2 ms: 1.05x faster                                         |
| pathlib                    | 17.4 ms                                                | 16.7 ms: 1.04x faster                                         |
| richards_super             | 53.7 ms                                                | 51.6 ms: 1.04x faster                                         |
| scimark_sor                | 122 ms                                                 | 118 ms: 1.04x faster                                          |
| logging_silent             | 101 ns                                                 | 97.6 ns: 1.04x faster                                         |
| genshi_text                | 22.6 ms                                                | 21.9 ms: 1.03x faster                                         |
| k_core                     | 2.37 sec                                               | 2.31 sec: 1.02x faster                                        |
| 2to3                       | 266 ms                                                 | 260 ms: 1.02x faster                                          |
| sqlite_synth               | 2.90 us                                                | 2.84 us: 1.02x faster                                         |
| xml_etree_generate         | 86.8 ms                                                | 85.2 ms: 1.02x faster                                         |
| pyflate                    | 470 ms                                                 | 461 ms: 1.02x faster                                          |
| xml_etree_iterparse        | 101 ms                                                 | 99.5 ms: 1.02x faster                                         |
| xml_etree_process          | 60.5 ms                                                | 59.8 ms: 1.01x faster                                         |
| html5lib                   | 63.4 ms                                                | 62.7 ms: 1.01x faster                                         |
| chaos                      | 58.0 ms                                                | 57.5 ms: 1.01x faster                                         |
| regex_compile              | 132 ms                                                 | 131 ms: 1.01x faster                                          |
| sqlalchemy_declarative     | 133 ms                                                 | 132 ms: 1.01x faster                                          |
| genshi_xml                 | 50.5 ms                                                | 50.2 ms: 1.01x faster                                         |
| sympy_integrate            | 19.8 ms                                                | 19.8 ms: 1.00x faster                                         |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                          |
| gc_traversal               | 4.90 ms                                                | 4.91 ms: 1.00x slower                                         |
| meteor_contest             | 108 ms                                                 | 109 ms: 1.00x slower                                          |
| sympy_sum                  | 150 ms                                                 | 151 ms: 1.00x slower                                          |
| generators                 | 28.8 ms                                                | 28.9 ms: 1.01x slower                                         |
| hexiom                     | 6.08 ms                                                | 6.13 ms: 1.01x slower                                         |
| shortest_path              | 487 ms                                                 | 493 ms: 1.01x slower                                          |
| docutils                   | 2.58 sec                                               | 2.62 sec: 1.01x slower                                        |
| connected_components       | 447 ms                                                 | 453 ms: 1.01x slower                                          |
| create_gc_cycles           | 2.45 ms                                                | 2.49 ms: 1.01x slower                                         |
| scimark_monte_carlo        | 66.8 ms                                                | 68.2 ms: 1.02x slower                                         |
| deltablue                  | 3.19 ms                                                | 3.26 ms: 1.02x slower                                         |
| django_template            | 31.7 ms                                                | 32.4 ms: 1.02x slower                                         |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.15 ms: 1.02x slower                                         |
| coverage                   | 82.8 ms                                                | 84.7 ms: 1.02x slower                                         |
| typing_runtime_protocols   | 160 us                                                 | 164 us: 1.02x slower                                          |
| sympy_expand               | 456 ms                                                 | 470 ms: 1.03x slower                                          |
| nqueens                    | 80.9 ms                                                | 83.5 ms: 1.03x slower                                         |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.04x slower                                         |
| raytrace                   | 262 ms                                                 | 272 ms: 1.04x slower                                          |
| comprehensions             | 16.5 us                                                | 17.2 us: 1.04x slower                                         |
| unpickle_pure_python       | 213 us                                                 | 222 us: 1.04x slower                                          |
| scimark_fft                | 367 ms                                                 | 384 ms: 1.05x slower                                          |
| pickle_pure_python         | 302 us                                                 | 323 us: 1.07x slower                                          |
| pprint_safe_repr           | 727 ms                                                 | 782 ms: 1.08x slower                                          |
| pprint_pformat             | 1.48 sec                                               | 1.59 sec: 1.08x slower                                        |
| scimark_lu                 | 114 ms                                                 | 124 ms: 1.08x slower                                          |
| bench_thread_pool          | 818 us                                                 | 885 us: 1.08x slower                                          |
| mako                       | 10.7 ms                                                | 11.6 ms: 1.09x slower                                         |
| crypto_pyaes               | 74.7 ms                                                | 82.1 ms: 1.10x slower                                         |
| json                       | 5.32 ms                                                | 5.86 ms: 1.10x slower                                         |
| fannkuch                   | 394 ms                                                 | 435 ms: 1.10x slower                                          |
| json_dumps                 | 10.1 ms                                                | 11.3 ms: 1.12x slower                                         |
| many_optionals             | 857 us                                                 | 958 us: 1.12x slower                                          |
| nbody                      | 87.7 ms                                                | 100 ms: 1.14x slower                                          |
| python_startup_no_site     | 7.00 ms                                                | 8.20 ms: 1.17x slower                                         |
| json_loads                 | 27.2 us                                                | 34.2 us: 1.26x slower                                         |
| subparsers                 | 15.5 ms                                                | 21.2 ms: 1.37x slower                                         |
| bench_mp_pool              | 24.0 ms                                                | 83.6 ms: 3.49x slower                                         |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                  |

Benchmark hidden because not significant (8): sphinx, logging_format, logging_simple, regex_dna, asyncio_websockets, pycparser, sympy_str, sqlalchemy_imperative
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250403-3.14.0a6+-07c4777/bm-20250403-linux-x86_64-brandtbucher-unbox-3.14.0a6+-07c4777.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.034x faster

# HPT report

- Reliability score: 92.31% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x