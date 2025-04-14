# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_mcmodel_again
- machine: linux-x86_64
- commit hash: b13591a
- commit date: 2025-03-04
- overall geometric mean: 1.043x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250304-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a5+-b13591a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 260 ms: 1.02x faster                                                         |
| docutils       | 2.58 sec                                               | 2.66 sec: 1.03x slower                                                       |
| html5lib       | 63.4 ms                                                | 62.3 ms: 1.02x faster                                                        |
| sphinx         | 1.03 sec                                               | 1.02 sec: 1.01x faster                                                       |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250304-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a5+-b13591a |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                         |
| async_tree_io              | 838 ms                                                 | 610 ms: 1.37x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 627 ms: 1.37x faster                                                         |
| async_tree_none            | 350 ms                                                 | 264 ms: 1.33x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 332 ms: 1.32x faster                                                         |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 494 ms: 1.16x faster                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 485 ms: 1.12x faster                                                         |
| async_generators           | 433 ms                                                 | 414 ms: 1.05x faster                                                         |
| coroutines                 | 22.2 ms                                                | 23.9 ms: 1.08x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250304-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a5+-b13591a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 69.0 ms: 1.14x faster                                                        |
| nbody          | 87.7 ms                                                | 86.7 ms: 1.01x faster                                                        |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250304-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a5+-b13591a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.46 ms: 1.09x faster                                                        |
| regex_v8       | 26.9 ms                                                | 25.6 ms: 1.05x faster                                                        |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                                         |
| regex_dna      | 220 ms                                                 | 225 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250304-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a5+-b13591a |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.88 sec: 1.13x faster                                                       |
| xml_etree_generate   | 86.8 ms                                                | 79.1 ms: 1.10x faster                                                        |
| xml_etree_process    | 60.5 ms                                                | 55.2 ms: 1.10x faster                                                        |
| xml_etree_parse      | 154 ms                                                 | 146 ms: 1.06x faster                                                         |
| unpickle_pure_python | 213 us                                                 | 206 us: 1.04x faster                                                         |
| xml_etree_iterparse  | 101 ms                                                 | 99.0 ms: 1.02x faster                                                        |
| pickle_pure_python   | 302 us                                                 | 325 us: 1.07x slower                                                         |
| json_loads           | 27.2 us                                                | 29.8 us: 1.10x slower                                                        |
| json_dumps           | 10.1 ms                                                | 11.3 ms: 1.12x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250304-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a5+-b13591a |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.12 ms: 1.02x slower                                                        |
| python_startup         | 12.7 ms                                                | 12.9 ms: 1.02x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250304-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a5+-b13591a |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.9 ms: 1.03x faster                                                        |
| mako            | 10.7 ms                                                | 10.5 ms: 1.02x faster                                                        |
| genshi_xml      | 50.5 ms                                                | 49.8 ms: 1.01x faster                                                        |
| django_template | 31.7 ms                                                | 31.8 ms: 1.00x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250304-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a5+-b13591a |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                         |
| async_tree_io              | 838 ms                                                 | 610 ms: 1.37x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 627 ms: 1.37x faster                                                         |
| deepcopy                   | 354 us                                                 | 259 us: 1.37x faster                                                         |
| async_tree_none            | 350 ms                                                 | 264 ms: 1.33x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 332 ms: 1.32x faster                                                         |
| deepcopy_memo              | 38.4 us                                                | 29.4 us: 1.30x faster                                                        |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                                         |
| deepcopy_reduce            | 3.24 us                                                | 2.70 us: 1.20x faster                                                        |
| go                         | 141 ms                                                 | 118 ms: 1.19x faster                                                         |
| spectral_norm              | 113 ms                                                 | 95.4 ms: 1.19x faster                                                        |
| scimark_fft                | 367 ms                                                 | 310 ms: 1.18x faster                                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 494 ms: 1.16x faster                                                         |
| float                      | 78.7 ms                                                | 69.0 ms: 1.14x faster                                                        |
| tomli_loads                | 2.12 sec                                               | 1.88 sec: 1.13x faster                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 485 ms: 1.12x faster                                                         |
| pylint                     | 312 ms                                                 | 279 ms: 1.12x faster                                                         |
| xml_etree_generate         | 86.8 ms                                                | 79.1 ms: 1.10x faster                                                        |
| xml_etree_process          | 60.5 ms                                                | 55.2 ms: 1.10x faster                                                        |
| telco                      | 8.40 ms                                                | 7.69 ms: 1.09x faster                                                        |
| regex_effbot               | 3.77 ms                                                | 3.46 ms: 1.09x faster                                                        |
| richards                   | 47.5 ms                                                | 43.9 ms: 1.08x faster                                                        |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.69 ms: 1.07x faster                                                        |
| richards_super             | 53.7 ms                                                | 50.5 ms: 1.07x faster                                                        |
| sqlite_synth               | 2.90 us                                                | 2.73 us: 1.06x faster                                                        |
| xml_etree_parse            | 154 ms                                                 | 146 ms: 1.06x faster                                                         |
| gc_traversal               | 4.90 ms                                                | 4.63 ms: 1.06x faster                                                        |
| pyflate                    | 470 ms                                                 | 445 ms: 1.05x faster                                                         |
| thrift                     | 800 us                                                 | 761 us: 1.05x faster                                                         |
| bpe_tokeniser              | 4.69 sec                                               | 4.47 sec: 1.05x faster                                                       |
| regex_v8                   | 26.9 ms                                                | 25.6 ms: 1.05x faster                                                        |
| async_generators           | 433 ms                                                 | 414 ms: 1.05x faster                                                         |
| k_core                     | 2.37 sec                                               | 2.27 sec: 1.04x faster                                                       |
| unpickle_pure_python       | 213 us                                                 | 206 us: 1.04x faster                                                         |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                                         |
| shortest_path              | 487 ms                                                 | 470 ms: 1.03x faster                                                         |
| genshi_text                | 22.6 ms                                                | 21.9 ms: 1.03x faster                                                        |
| pathlib                    | 17.4 ms                                                | 16.8 ms: 1.03x faster                                                        |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.03x faster                                                       |
| connected_components       | 447 ms                                                 | 434 ms: 1.03x faster                                                         |
| logging_simple             | 5.65 us                                                | 5.49 us: 1.03x faster                                                        |
| generators                 | 28.8 ms                                                | 28.1 ms: 1.03x faster                                                        |
| 2to3                       | 266 ms                                                 | 260 ms: 1.02x faster                                                         |
| sqlalchemy_declarative     | 133 ms                                                 | 130 ms: 1.02x faster                                                         |
| xml_etree_iterparse        | 101 ms                                                 | 99.0 ms: 1.02x faster                                                        |
| sqlglot_normalize          | 108 ms                                                 | 106 ms: 1.02x faster                                                         |
| mdp                        | 2.54 sec                                               | 2.49 sec: 1.02x faster                                                       |
| html5lib                   | 63.4 ms                                                | 62.3 ms: 1.02x faster                                                        |
| mako                       | 10.7 ms                                                | 10.5 ms: 1.02x faster                                                        |
| sphinx                     | 1.03 sec                                               | 1.02 sec: 1.01x faster                                                       |
| genshi_xml                 | 50.5 ms                                                | 49.8 ms: 1.01x faster                                                        |
| logging_format             | 6.23 us                                                | 6.15 us: 1.01x faster                                                        |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.7 ms: 1.01x faster                                                        |
| nbody                      | 87.7 ms                                                | 86.7 ms: 1.01x faster                                                        |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                                         |
| crypto_pyaes               | 74.7 ms                                                | 74.0 ms: 1.01x faster                                                        |
| create_gc_cycles           | 2.45 ms                                                | 2.43 ms: 1.01x faster                                                        |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| sqlglot_optimize           | 53.4 ms                                                | 53.2 ms: 1.00x faster                                                        |
| django_template            | 31.7 ms                                                | 31.8 ms: 1.00x slower                                                        |
| typing_runtime_protocols   | 160 us                                                 | 161 us: 1.01x slower                                                         |
| scimark_sor                | 122 ms                                                 | 123 ms: 1.01x slower                                                         |
| sqlglot_transpile          | 1.57 ms                                                | 1.59 ms: 1.01x slower                                                        |
| sqlglot_parse              | 1.26 ms                                                | 1.28 ms: 1.01x slower                                                        |
| scimark_monte_carlo        | 66.8 ms                                                | 67.8 ms: 1.01x slower                                                        |
| sympy_integrate            | 19.8 ms                                                | 20.1 ms: 1.02x slower                                                        |
| python_startup_no_site     | 7.00 ms                                                | 7.12 ms: 1.02x slower                                                        |
| scimark_lu                 | 114 ms                                                 | 116 ms: 1.02x slower                                                         |
| chaos                      | 58.0 ms                                                | 59.2 ms: 1.02x slower                                                        |
| python_startup             | 12.7 ms                                                | 12.9 ms: 1.02x slower                                                        |
| regex_dna                  | 220 ms                                                 | 225 ms: 1.02x slower                                                         |
| fannkuch                   | 394 ms                                                 | 404 ms: 1.03x slower                                                         |
| coverage                   | 82.8 ms                                                | 85.2 ms: 1.03x slower                                                        |
| sympy_expand               | 456 ms                                                 | 469 ms: 1.03x slower                                                         |
| docutils                   | 2.58 sec                                               | 2.66 sec: 1.03x slower                                                       |
| deltablue                  | 3.19 ms                                                | 3.30 ms: 1.03x slower                                                        |
| dulwich_log                | 64.6 ms                                                | 66.8 ms: 1.03x slower                                                        |
| raytrace                   | 262 ms                                                 | 272 ms: 1.04x slower                                                         |
| hexiom                     | 6.08 ms                                                | 6.36 ms: 1.05x slower                                                        |
| logging_silent             | 101 ns                                                 | 107 ns: 1.06x slower                                                         |
| comprehensions             | 16.5 us                                                | 17.6 us: 1.07x slower                                                        |
| bench_thread_pool          | 818 us                                                 | 874 us: 1.07x slower                                                         |
| pickle_pure_python         | 302 us                                                 | 325 us: 1.07x slower                                                         |
| coroutines                 | 22.2 ms                                                | 23.9 ms: 1.08x slower                                                        |
| json_loads                 | 27.2 us                                                | 29.8 us: 1.10x slower                                                        |
| json_dumps                 | 10.1 ms                                                | 11.3 ms: 1.12x slower                                                        |
| many_optionals             | 857 us                                                 | 965 us: 1.13x slower                                                         |
| subparsers                 | 15.5 ms                                                | 20.8 ms: 1.34x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 81.8 ms: 3.41x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                 |

Benchmark hidden because not significant (7): json, sympy_sum, pprint_safe_repr, nqueens, pprint_pformat, asyncio_websockets, sympy_str
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.043x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x