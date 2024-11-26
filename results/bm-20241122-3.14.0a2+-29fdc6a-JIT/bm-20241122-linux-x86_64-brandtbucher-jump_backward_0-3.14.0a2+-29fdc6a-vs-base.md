# Results vs. base

- fork: brandtbucher
- ref: jump_backward_0
- machine: linux-x86_64
- commit hash: 29fdc6a
- commit date: 2024-11-22
- overall geometric mean: 1.034x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241122-linux-x86_64-python-615abb99a4538520f380-3.14.0a2+-615abb9 | bm-20241122-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a2+-29fdc6a |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 261 ms                                                                 | 268 ms: 1.03x slower                                                    |
| docutils       | 2.83 sec                                                               | 3.02 sec: 1.07x slower                                                  |
| sphinx         | 1.11 sec                                                               | 1.15 sec: 1.04x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                            |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241122-linux-x86_64-python-615abb99a4538520f380-3.14.0a2+-615abb9 | bm-20241122-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a2+-29fdc6a |
|----------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_generators           | 454 ms                                                                 | 457 ms: 1.01x slower                                                    |
| async_tree_io              | 913 ms                                                                 | 939 ms: 1.03x slower                                                    |
| async_tree_memoization     | 409 ms                                                                 | 423 ms: 1.03x slower                                                    |
| async_tree_memoization_tg  | 399 ms                                                                 | 412 ms: 1.03x slower                                                    |
| async_tree_none            | 326 ms                                                                 | 338 ms: 1.04x slower                                                    |
| async_tree_cpu_io_mixed_tg | 564 ms                                                                 | 586 ms: 1.04x slower                                                    |
| async_tree_cpu_io_mixed    | 559 ms                                                                 | 582 ms: 1.04x slower                                                    |
| coroutines                 | 23.1 ms                                                                | 27.1 ms: 1.17x slower                                                   |
| Geometric mean             | (ref)                                                                  | 1.04x slower                                                            |

Benchmark hidden because not significant (3): asyncio_websockets, async_tree_io_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241122-linux-x86_64-python-615abb99a4538520f380-3.14.0a2+-615abb9 | bm-20241122-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a2+-29fdc6a |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 78.6 ms                                                                | 77.4 ms: 1.01x faster                                                   |
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x faster                                                    |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                            |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241122-linux-x86_64-python-615abb99a4538520f380-3.14.0a2+-615abb9 | bm-20241122-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a2+-29fdc6a |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 25.5 ms                                                                | 25.7 ms: 1.00x slower                                                   |
| regex_compile  | 132 ms                                                                 | 137 ms: 1.04x slower                                                    |
| regex_dna      | 215 ms                                                                 | 225 ms: 1.04x slower                                                    |
| regex_effbot   | 3.30 ms                                                                | 3.45 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241122-linux-x86_64-python-615abb99a4538520f380-3.14.0a2+-615abb9 | bm-20241122-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a2+-29fdc6a |
|----------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_loads           | 26.8 us                                                                | 26.0 us: 1.03x faster                                                   |
| tomli_loads          | 1.95 sec                                                               | 1.97 sec: 1.01x slower                                                  |
| json_dumps           | 11.1 ms                                                                | 11.3 ms: 1.02x slower                                                   |
| xml_etree_generate   | 82.2 ms                                                                | 83.8 ms: 1.02x slower                                                   |
| pickle_pure_python   | 316 us                                                                 | 324 us: 1.02x slower                                                    |
| xml_etree_process    | 57.2 ms                                                                | 59.6 ms: 1.04x slower                                                   |
| unpickle_pure_python | 196 us                                                                 | 216 us: 1.10x slower                                                    |
| Geometric mean       | (ref)                                                                  | 1.02x slower                                                            |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241122-linux-x86_64-python-615abb99a4538520f380-3.14.0a2+-615abb9 | bm-20241122-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a2+-29fdc6a |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 7.06 ms                                                                | 7.07 ms: 1.00x slower                                                   |
| python_startup         | 12.8 ms                                                                | 12.9 ms: 1.00x slower                                                   |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241122-linux-x86_64-python-615abb99a4538520f380-3.14.0a2+-615abb9 | bm-20241122-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a2+-29fdc6a |
|-----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 24.9 ms                                                                | 24.3 ms: 1.02x faster                                                   |
| genshi_xml      | 57.4 ms                                                                | 58.2 ms: 1.01x slower                                                   |
| mako            | 10.1 ms                                                                | 10.6 ms: 1.05x slower                                                   |
| django_template | 33.4 ms                                                                | 36.2 ms: 1.08x slower                                                   |
| Geometric mean  | (ref)                                                                  | 1.03x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241122-linux-x86_64-python-615abb99a4538520f380-3.14.0a2+-615abb9 | bm-20241122-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a2+-29fdc6a |
|----------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| scimark_monte_carlo        | 66.0 ms                                                                | 62.4 ms: 1.06x faster                                                   |
| mdp                        | 2.78 sec                                                               | 2.64 sec: 1.06x faster                                                  |
| go                         | 136 ms                                                                 | 129 ms: 1.05x faster                                                    |
| scimark_sparse_mat_mult    | 4.81 ms                                                                | 4.58 ms: 1.05x faster                                                   |
| json_loads                 | 26.8 us                                                                | 26.0 us: 1.03x faster                                                   |
| genshi_text                | 24.9 ms                                                                | 24.3 ms: 1.02x faster                                                   |
| float                      | 78.6 ms                                                                | 77.4 ms: 1.01x faster                                                   |
| scimark_lu                 | 116 ms                                                                 | 114 ms: 1.01x faster                                                    |
| sqlite_synth               | 2.82 us                                                                | 2.79 us: 1.01x faster                                                   |
| meteor_contest             | 108 ms                                                                 | 107 ms: 1.01x faster                                                    |
| logging_silent             | 102 ns                                                                 | 102 ns: 1.00x faster                                                    |
| scimark_fft                | 318 ms                                                                 | 316 ms: 1.00x faster                                                    |
| shortest_path              | 485 ms                                                                 | 483 ms: 1.00x faster                                                    |
| pidigits                   | 186 ms                                                                 | 186 ms: 1.00x faster                                                    |
| python_startup_no_site     | 7.06 ms                                                                | 7.07 ms: 1.00x slower                                                   |
| create_gc_cycles           | 2.65 ms                                                                | 2.66 ms: 1.00x slower                                                   |
| python_startup             | 12.8 ms                                                                | 12.9 ms: 1.00x slower                                                   |
| regex_v8                   | 25.5 ms                                                                | 25.7 ms: 1.00x slower                                                   |
| bench_mp_pool              | 79.0 ms                                                                | 79.4 ms: 1.01x slower                                                   |
| bpe_tokeniser              | 4.53 sec                                                               | 4.57 sec: 1.01x slower                                                  |
| pathlib                    | 16.2 ms                                                                | 16.4 ms: 1.01x slower                                                   |
| async_generators           | 454 ms                                                                 | 457 ms: 1.01x slower                                                    |
| tomli_loads                | 1.95 sec                                                               | 1.97 sec: 1.01x slower                                                  |
| json                       | 4.78 ms                                                                | 4.84 ms: 1.01x slower                                                   |
| genshi_xml                 | 57.4 ms                                                                | 58.2 ms: 1.01x slower                                                   |
| dulwich_log                | 68.0 ms                                                                | 69.0 ms: 1.01x slower                                                   |
| typing_runtime_protocols   | 169 us                                                                 | 171 us: 1.02x slower                                                    |
| sqlalchemy_declarative     | 131 ms                                                                 | 133 ms: 1.02x slower                                                    |
| pprint_pformat             | 1.49 sec                                                               | 1.52 sec: 1.02x slower                                                  |
| pycparser                  | 1.18 sec                                                               | 1.20 sec: 1.02x slower                                                  |
| nqueens                    | 89.2 ms                                                                | 90.8 ms: 1.02x slower                                                   |
| json_dumps                 | 11.1 ms                                                                | 11.3 ms: 1.02x slower                                                   |
| xml_etree_generate         | 82.2 ms                                                                | 83.8 ms: 1.02x slower                                                   |
| scimark_sor                | 120 ms                                                                 | 123 ms: 1.02x slower                                                    |
| pickle_pure_python         | 316 us                                                                 | 324 us: 1.02x slower                                                    |
| 2to3                       | 261 ms                                                                 | 268 ms: 1.03x slower                                                    |
| pprint_safe_repr           | 723 ms                                                                 | 744 ms: 1.03x slower                                                    |
| async_tree_io              | 913 ms                                                                 | 939 ms: 1.03x slower                                                    |
| deepcopy                   | 269 us                                                                 | 277 us: 1.03x slower                                                    |
| generators                 | 35.7 ms                                                                | 36.9 ms: 1.03x slower                                                   |
| async_tree_memoization     | 409 ms                                                                 | 423 ms: 1.03x slower                                                    |
| chaos                      | 59.8 ms                                                                | 61.8 ms: 1.03x slower                                                   |
| sympy_str                  | 287 ms                                                                 | 297 ms: 1.03x slower                                                    |
| async_tree_memoization_tg  | 399 ms                                                                 | 412 ms: 1.03x slower                                                    |
| async_tree_none            | 326 ms                                                                 | 338 ms: 1.04x slower                                                    |
| async_tree_cpu_io_mixed_tg | 564 ms                                                                 | 586 ms: 1.04x slower                                                    |
| regex_compile              | 132 ms                                                                 | 137 ms: 1.04x slower                                                    |
| hexiom                     | 7.11 ms                                                                | 7.40 ms: 1.04x slower                                                   |
| coverage                   | 84.4 ms                                                                | 87.9 ms: 1.04x slower                                                   |
| xml_etree_process          | 57.2 ms                                                                | 59.6 ms: 1.04x slower                                                   |
| async_tree_cpu_io_mixed    | 559 ms                                                                 | 582 ms: 1.04x slower                                                    |
| sqlglot_normalize          | 112 ms                                                                 | 117 ms: 1.04x slower                                                    |
| sphinx                     | 1.11 sec                                                               | 1.15 sec: 1.04x slower                                                  |
| sympy_expand               | 481 ms                                                                 | 501 ms: 1.04x slower                                                    |
| regex_dna                  | 215 ms                                                                 | 225 ms: 1.04x slower                                                    |
| regex_effbot               | 3.30 ms                                                                | 3.45 ms: 1.04x slower                                                   |
| raytrace                   | 281 ms                                                                 | 294 ms: 1.05x slower                                                    |
| mako                       | 10.1 ms                                                                | 10.6 ms: 1.05x slower                                                   |
| gc_traversal               | 4.31 ms                                                                | 4.52 ms: 1.05x slower                                                   |
| spectral_norm              | 112 ms                                                                 | 118 ms: 1.05x slower                                                    |
| bench_thread_pool          | 873 us                                                                 | 923 us: 1.06x slower                                                    |
| thrift                     | 780 us                                                                 | 825 us: 1.06x slower                                                    |
| sqlglot_optimize           | 55.7 ms                                                                | 59.4 ms: 1.06x slower                                                   |
| docutils                   | 2.83 sec                                                               | 3.02 sec: 1.07x slower                                                  |
| sympy_integrate            | 21.0 ms                                                                | 22.4 ms: 1.07x slower                                                   |
| djangocms                  | 22.7 us                                                                | 24.3 us: 1.07x slower                                                   |
| pyflate                    | 436 ms                                                                 | 468 ms: 1.07x slower                                                    |
| sqlglot_parse              | 1.34 ms                                                                | 1.43 ms: 1.07x slower                                                   |
| deepcopy_reduce            | 2.69 us                                                                | 2.90 us: 1.08x slower                                                   |
| pylint                     | 283 ms                                                                 | 305 ms: 1.08x slower                                                    |
| many_optionals             | 988 us                                                                 | 1.07 ms: 1.08x slower                                                   |
| django_template            | 33.4 ms                                                                | 36.2 ms: 1.08x slower                                                   |
| subparsers                 | 21.1 ms                                                                | 22.8 ms: 1.08x slower                                                   |
| sqlglot_transpile          | 1.65 ms                                                                | 1.80 ms: 1.09x slower                                                   |
| unpickle_pure_python       | 196 us                                                                 | 216 us: 1.10x slower                                                    |
| sympy_sum                  | 160 ms                                                                 | 178 ms: 1.11x slower                                                    |
| sqlalchemy_imperative      | 17.4 ms                                                                | 20.2 ms: 1.17x slower                                                   |
| coroutines                 | 23.1 ms                                                                | 27.1 ms: 1.17x slower                                                   |
| logging_format             | 6.20 us                                                                | 7.46 us: 1.20x slower                                                   |
| logging_simple             | 5.63 us                                                                | 6.84 us: 1.21x slower                                                   |
| richards_super             | 43.0 ms                                                                | 52.7 ms: 1.22x slower                                                   |
| deltablue                  | 3.19 ms                                                                | 3.93 ms: 1.23x slower                                                   |
| richards                   | 37.4 ms                                                                | 46.7 ms: 1.25x slower                                                   |
| Geometric mean             | (ref)                                                                  | 1.04x slower                                                            |

Benchmark hidden because not significant (14): xml_etree_parse, nbody, deepcopy_memo, comprehensions, telco, connected_components, asyncio_websockets, fannkuch, html5lib, crypto_pyaes, xml_etree_iterparse, k_core, async_tree_io_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.034x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.00x