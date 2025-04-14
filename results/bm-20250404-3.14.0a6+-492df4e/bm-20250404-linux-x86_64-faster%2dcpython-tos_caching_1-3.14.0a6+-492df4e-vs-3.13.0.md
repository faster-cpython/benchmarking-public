# Results vs. 3.13.0

- fork: faster-cpython
- ref: tos_caching_1
- machine: linux-x86_64
- commit hash: 492df4e
- commit date: 2025-04-04
- overall geometric mean: 1.053x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250404-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 248 ms: 1.07x faster                                                      |
| docutils       | 2.58 sec                                               | 2.59 sec: 1.00x slower                                                    |
| html5lib       | 63.4 ms                                                | 62.1 ms: 1.02x faster                                                     |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                    |
| Geometric mean | (ref)                                                  | 1.03x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250404-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 321 ms: 1.44x faster                                                      |
| async_tree_io_tg           | 861 ms                                                 | 617 ms: 1.39x faster                                                      |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                                      |
| async_tree_io              | 838 ms                                                 | 620 ms: 1.35x faster                                                      |
| async_tree_none            | 350 ms                                                 | 263 ms: 1.33x faster                                                      |
| async_tree_none_tg         | 319 ms                                                 | 254 ms: 1.26x faster                                                      |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 481 ms: 1.19x faster                                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 476 ms: 1.14x faster                                                      |
| async_generators           | 433 ms                                                 | 395 ms: 1.10x faster                                                      |
| coroutines                 | 22.2 ms                                                | 24.2 ms: 1.09x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                              |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250404-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 67.4 ms: 1.17x faster                                                     |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                      |
| nbody          | 87.7 ms                                                | 91.6 ms: 1.05x slower                                                     |
| Geometric mean | (ref)                                                  | 1.04x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250404-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.3 ms: 1.15x faster                                                     |
| regex_effbot   | 3.77 ms                                                | 3.35 ms: 1.12x faster                                                     |
| regex_compile  | 132 ms                                                 | 126 ms: 1.04x faster                                                      |
| regex_dna      | 220 ms                                                 | 216 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.08x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250404-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.09x faster                                                      |
| tomli_loads          | 2.12 sec                                               | 1.94 sec: 1.09x faster                                                    |
| xml_etree_generate   | 86.8 ms                                                | 84.9 ms: 1.02x faster                                                     |
| xml_etree_iterparse  | 101 ms                                                 | 99.0 ms: 1.02x faster                                                     |
| xml_etree_process    | 60.5 ms                                                | 59.7 ms: 1.01x faster                                                     |
| unpickle_pure_python | 213 us                                                 | 221 us: 1.04x slower                                                      |
| pickle_pure_python   | 302 us                                                 | 316 us: 1.04x slower                                                      |
| json_loads           | 27.2 us                                                | 29.7 us: 1.09x slower                                                     |
| json_dumps           | 10.1 ms                                                | 11.6 ms: 1.15x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250404-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.04x slower                                                     |
| python_startup_no_site | 7.00 ms                                                | 8.18 ms: 1.17x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250404-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.2 ms: 1.06x faster                                                     |
| genshi_xml      | 50.5 ms                                                | 49.6 ms: 1.02x faster                                                     |
| django_template | 31.7 ms                                                | 32.1 ms: 1.01x slower                                                     |
| mako            | 10.7 ms                                                | 11.5 ms: 1.08x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250404-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.22 sec: 2.09x faster                                                    |
| async_tree_memoization_tg  | 463 ms                                                 | 321 ms: 1.44x faster                                                      |
| deepcopy                   | 354 us                                                 | 253 us: 1.40x faster                                                      |
| async_tree_io_tg           | 861 ms                                                 | 617 ms: 1.39x faster                                                      |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                                      |
| async_tree_io              | 838 ms                                                 | 620 ms: 1.35x faster                                                      |
| async_tree_none            | 350 ms                                                 | 263 ms: 1.33x faster                                                      |
| deepcopy_memo              | 38.4 us                                                | 30.1 us: 1.28x faster                                                     |
| async_tree_none_tg         | 319 ms                                                 | 254 ms: 1.26x faster                                                      |
| go                         | 141 ms                                                 | 113 ms: 1.24x faster                                                      |
| deepcopy_reduce            | 3.24 us                                                | 2.66 us: 1.22x faster                                                     |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 481 ms: 1.19x faster                                                      |
| float                      | 78.7 ms                                                | 67.4 ms: 1.17x faster                                                     |
| regex_v8                   | 26.9 ms                                                | 23.3 ms: 1.15x faster                                                     |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 476 ms: 1.14x faster                                                      |
| pylint                     | 312 ms                                                 | 276 ms: 1.13x faster                                                      |
| regex_effbot               | 3.77 ms                                                | 3.35 ms: 1.12x faster                                                     |
| async_generators           | 433 ms                                                 | 395 ms: 1.10x faster                                                      |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                                      |
| tomli_loads                | 2.12 sec                                               | 1.94 sec: 1.09x faster                                                    |
| dulwich_log                | 64.6 ms                                                | 59.1 ms: 1.09x faster                                                     |
| telco                      | 8.40 ms                                                | 7.75 ms: 1.08x faster                                                     |
| richards                   | 47.5 ms                                                | 44.0 ms: 1.08x faster                                                     |
| spectral_norm              | 113 ms                                                 | 105 ms: 1.08x faster                                                      |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.67 ms: 1.08x faster                                                     |
| pyflate                    | 470 ms                                                 | 437 ms: 1.08x faster                                                      |
| richards_super             | 53.7 ms                                                | 50.0 ms: 1.07x faster                                                     |
| 2to3                       | 266 ms                                                 | 248 ms: 1.07x faster                                                      |
| scimark_fft                | 367 ms                                                 | 344 ms: 1.07x faster                                                      |
| genshi_text                | 22.6 ms                                                | 21.2 ms: 1.06x faster                                                     |
| pycparser                  | 1.20 sec                                               | 1.15 sec: 1.05x faster                                                    |
| regex_compile              | 132 ms                                                 | 126 ms: 1.04x faster                                                      |
| k_core                     | 2.37 sec                                               | 2.27 sec: 1.04x faster                                                    |
| pathlib                    | 17.4 ms                                                | 16.7 ms: 1.04x faster                                                     |
| sympy_integrate            | 19.8 ms                                                | 19.1 ms: 1.04x faster                                                     |
| bpe_tokeniser              | 4.69 sec                                               | 4.53 sec: 1.03x faster                                                    |
| crypto_pyaes               | 74.7 ms                                                | 72.5 ms: 1.03x faster                                                     |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.03x faster                                                      |
| gc_traversal               | 4.90 ms                                                | 4.76 ms: 1.03x faster                                                     |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.03x faster                                                      |
| sqlite_synth               | 2.90 us                                                | 2.83 us: 1.03x faster                                                     |
| scimark_monte_carlo        | 66.8 ms                                                | 65.1 ms: 1.03x faster                                                     |
| xml_etree_generate         | 86.8 ms                                                | 84.9 ms: 1.02x faster                                                     |
| xml_etree_iterparse        | 101 ms                                                 | 99.0 ms: 1.02x faster                                                     |
| sympy_str                  | 273 ms                                                 | 267 ms: 1.02x faster                                                      |
| chaos                      | 58.0 ms                                                | 56.8 ms: 1.02x faster                                                     |
| html5lib                   | 63.4 ms                                                | 62.1 ms: 1.02x faster                                                     |
| logging_silent             | 101 ns                                                 | 99.0 ns: 1.02x faster                                                     |
| regex_dna                  | 220 ms                                                 | 216 ms: 1.02x faster                                                      |
| genshi_xml                 | 50.5 ms                                                | 49.6 ms: 1.02x faster                                                     |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                    |
| xml_etree_process          | 60.5 ms                                                | 59.7 ms: 1.01x faster                                                     |
| sqlalchemy_declarative     | 133 ms                                                 | 131 ms: 1.01x faster                                                      |
| sympy_sum                  | 150 ms                                                 | 149 ms: 1.01x faster                                                      |
| pprint_safe_repr           | 727 ms                                                 | 723 ms: 1.01x faster                                                      |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                      |
| raytrace                   | 262 ms                                                 | 262 ms: 1.00x slower                                                      |
| docutils                   | 2.58 sec                                               | 2.59 sec: 1.00x slower                                                    |
| sympy_expand               | 456 ms                                                 | 459 ms: 1.01x slower                                                      |
| create_gc_cycles           | 2.45 ms                                                | 2.46 ms: 1.01x slower                                                     |
| pprint_pformat             | 1.48 sec                                               | 1.49 sec: 1.01x slower                                                    |
| shortest_path              | 487 ms                                                 | 491 ms: 1.01x slower                                                      |
| django_template            | 31.7 ms                                                | 32.1 ms: 1.01x slower                                                     |
| comprehensions             | 16.5 us                                                | 16.8 us: 1.02x slower                                                     |
| nqueens                    | 80.9 ms                                                | 82.4 ms: 1.02x slower                                                     |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.02x slower                                                      |
| coverage                   | 82.8 ms                                                | 84.6 ms: 1.02x slower                                                     |
| fannkuch                   | 394 ms                                                 | 405 ms: 1.03x slower                                                      |
| hexiom                     | 6.08 ms                                                | 6.29 ms: 1.03x slower                                                     |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.04x slower                                                     |
| unpickle_pure_python       | 213 us                                                 | 221 us: 1.04x slower                                                      |
| pickle_pure_python         | 302 us                                                 | 316 us: 1.04x slower                                                      |
| nbody                      | 87.7 ms                                                | 91.6 ms: 1.05x slower                                                     |
| generators                 | 28.8 ms                                                | 30.5 ms: 1.06x slower                                                     |
| deltablue                  | 3.19 ms                                                | 3.43 ms: 1.07x slower                                                     |
| mako                       | 10.7 ms                                                | 11.5 ms: 1.08x slower                                                     |
| bench_thread_pool          | 818 us                                                 | 881 us: 1.08x slower                                                      |
| many_optionals             | 857 us                                                 | 925 us: 1.08x slower                                                      |
| coroutines                 | 22.2 ms                                                | 24.2 ms: 1.09x slower                                                     |
| json_loads                 | 27.2 us                                                | 29.7 us: 1.09x slower                                                     |
| json_dumps                 | 10.1 ms                                                | 11.6 ms: 1.15x slower                                                     |
| python_startup_no_site     | 7.00 ms                                                | 8.18 ms: 1.17x slower                                                     |
| subparsers                 | 15.5 ms                                                | 20.8 ms: 1.34x slower                                                     |
| bench_mp_pool              | 24.0 ms                                                | 81.9 ms: 3.41x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                              |

Benchmark hidden because not significant (7): json, typing_runtime_protocols, connected_components, logging_format, sqlalchemy_imperative, asyncio_websockets, logging_simple
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250404-3.14.0a6+-492df4e/bm-20250404-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.053x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x