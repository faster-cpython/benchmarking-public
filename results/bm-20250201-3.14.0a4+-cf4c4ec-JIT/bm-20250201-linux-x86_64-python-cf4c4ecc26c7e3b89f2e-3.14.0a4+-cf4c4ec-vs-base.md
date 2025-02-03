# Results vs. base

- fork: python
- ref: cf4c4ecc26c7e3b89f2e
- machine: linux-x86_64
- commit hash: cf4c4ec
- commit date: 2025-02-01
- overall geometric mean: 1.006x slower
- HPT reliability: 78.19%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json | results/bm-20250201-3.14.0a4+-cf4c4ec-JIT/bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 254 ms                                                                                                            | 260 ms: 1.02x slower                                                                                                  |
| docutils       | 2.62 sec                                                                                                          | 2.67 sec: 1.02x slower                                                                                                |
| html5lib       | 61.3 ms                                                                                                           | 64.8 ms: 1.06x slower                                                                                                 |
| sphinx         | 1.01 sec                                                                                                          | 1.04 sec: 1.02x slower                                                                                                |
| Geometric mean | (ref)                                                                                                             | 1.03x slower                                                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json | results/bm-20250201-3.14.0a4+-cf4c4ec-JIT/bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 488 ms                                                                                                            | 477 ms: 1.02x faster                                                                                                  |
| coroutines                 | 23.7 ms                                                                                                           | 23.5 ms: 1.01x faster                                                                                                 |
| async_tree_none_tg         | 257 ms                                                                                                            | 255 ms: 1.01x faster                                                                                                  |
| async_tree_cpu_io_mixed    | 495 ms                                                                                                            | 492 ms: 1.01x faster                                                                                                  |
| asyncio_tcp_ssl            | 1.80 sec                                                                                                          | 1.82 sec: 1.01x slower                                                                                                |
| async_tree_memoization     | 322 ms                                                                                                            | 328 ms: 1.02x slower                                                                                                  |
| async_tree_none            | 263 ms                                                                                                            | 270 ms: 1.03x slower                                                                                                  |
| async_generators           | 392 ms                                                                                                            | 407 ms: 1.04x slower                                                                                                  |
| Geometric mean             | (ref)                                                                                                             | 1.00x slower                                                                                                          |

Benchmark hidden because not significant (5): async_tree_io_tg, asyncio_websockets, asyncio_tcp, async_tree_memoization_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json | results/bm-20250201-3.14.0a4+-cf4c4ec-JIT/bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| float          | 71.4 ms                                                                                                           | 67.0 ms: 1.07x faster                                                                                                 |
| nbody          | 92.3 ms                                                                                                           | 88.0 ms: 1.05x faster                                                                                                 |
| pidigits       | 186 ms                                                                                                            | 186 ms: 1.00x faster                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.04x faster                                                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json | results/bm-20250201-3.14.0a4+-cf4c4ec-JIT/bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 25.7 ms                                                                                                           | 23.5 ms: 1.09x faster                                                                                                 |
| regex_effbot   | 3.40 ms                                                                                                           | 3.17 ms: 1.07x faster                                                                                                 |
| regex_dna      | 214 ms                                                                                                            | 208 ms: 1.03x faster                                                                                                  |
| regex_compile  | 126 ms                                                                                                            | 128 ms: 1.02x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.04x faster                                                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json | results/bm-20250201-3.14.0a4+-cf4c4ec-JIT/bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 217 us                                                                                                            | 196 us: 1.11x faster                                                                                                  |
| xml_etree_process    | 59.4 ms                                                                                                           | 55.3 ms: 1.07x faster                                                                                                 |
| tomli_loads          | 1.95 sec                                                                                                          | 1.84 sec: 1.06x faster                                                                                                |
| xml_etree_generate   | 84.2 ms                                                                                                           | 79.4 ms: 1.06x faster                                                                                                 |
| json_dumps           | 11.7 ms                                                                                                           | 11.3 ms: 1.04x faster                                                                                                 |
| unpickle_list        | 5.77 us                                                                                                           | 5.60 us: 1.03x faster                                                                                                 |
| pickle_pure_python   | 318 us                                                                                                            | 309 us: 1.03x faster                                                                                                  |
| xml_etree_iterparse  | 96.9 ms                                                                                                           | 95.0 ms: 1.02x faster                                                                                                 |
| pickle               | 12.6 us                                                                                                           | 12.7 us: 1.01x slower                                                                                                 |
| json_loads           | 28.4 us                                                                                                           | 28.8 us: 1.01x slower                                                                                                 |
| unpickle             | 13.9 us                                                                                                           | 14.4 us: 1.03x slower                                                                                                 |
| pickle_dict          | 35.3 us                                                                                                           | 36.6 us: 1.04x slower                                                                                                 |
| pickle_list          | 5.42 us                                                                                                           | 5.70 us: 1.05x slower                                                                                                 |
| Geometric mean       | (ref)                                                                                                             | 1.02x faster                                                                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json | results/bm-20250201-3.14.0a4+-cf4c4ec-JIT/bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                                                                           | 12.8 ms: 1.01x faster                                                                                                 |
| python_startup_no_site | 7.09 ms                                                                                                           | 7.06 ms: 1.00x faster                                                                                                 |
| Geometric mean         | (ref)                                                                                                             | 1.01x faster                                                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json | results/bm-20250201-3.14.0a4+-cf4c4ec-JIT/bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako            | 11.5 ms                                                                                                           | 10.0 ms: 1.15x faster                                                                                                 |
| django_template | 31.7 ms                                                                                                           | 33.8 ms: 1.06x slower                                                                                                 |
| genshi_text     | 21.4 ms                                                                                                           | 23.1 ms: 1.08x slower                                                                                                 |
| genshi_xml      | 48.2 ms                                                                                                           | 58.4 ms: 1.21x slower                                                                                                 |
| Geometric mean  | (ref)                                                                                                             | 1.05x slower                                                                                                          |

All benchmarks:
===============

| Benchmark                  | results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json | results/bm-20250201-3.14.0a4+-cf4c4ec-JIT/bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako                       | 11.5 ms                                                                                                           | 10.0 ms: 1.15x faster                                                                                                 |
| unpickle_pure_python       | 217 us                                                                                                            | 196 us: 1.11x faster                                                                                                  |
| scimark_fft                | 343 ms                                                                                                            | 310 ms: 1.11x faster                                                                                                  |
| regex_v8                   | 25.7 ms                                                                                                           | 23.5 ms: 1.09x faster                                                                                                 |
| scimark_sparse_mat_mult    | 4.67 ms                                                                                                           | 4.33 ms: 1.08x faster                                                                                                 |
| scimark_monte_carlo        | 67.5 ms                                                                                                           | 62.7 ms: 1.08x faster                                                                                                 |
| xml_etree_process          | 59.4 ms                                                                                                           | 55.3 ms: 1.07x faster                                                                                                 |
| regex_effbot               | 3.40 ms                                                                                                           | 3.17 ms: 1.07x faster                                                                                                 |
| scimark_sor                | 123 ms                                                                                                            | 115 ms: 1.07x faster                                                                                                  |
| spectral_norm              | 101 ms                                                                                                            | 94.4 ms: 1.07x faster                                                                                                 |
| float                      | 71.4 ms                                                                                                           | 67.0 ms: 1.07x faster                                                                                                 |
| tomli_loads                | 1.95 sec                                                                                                          | 1.84 sec: 1.06x faster                                                                                                |
| xml_etree_generate         | 84.2 ms                                                                                                           | 79.4 ms: 1.06x faster                                                                                                 |
| fannkuch                   | 409 ms                                                                                                            | 390 ms: 1.05x faster                                                                                                  |
| nbody                      | 92.3 ms                                                                                                           | 88.0 ms: 1.05x faster                                                                                                 |
| richards                   | 45.0 ms                                                                                                           | 43.0 ms: 1.05x faster                                                                                                 |
| sqlalchemy_imperative      | 17.5 ms                                                                                                           | 16.8 ms: 1.04x faster                                                                                                 |
| richards_super             | 51.1 ms                                                                                                           | 49.2 ms: 1.04x faster                                                                                                 |
| json_dumps                 | 11.7 ms                                                                                                           | 11.3 ms: 1.04x faster                                                                                                 |
| unpickle_list              | 5.77 us                                                                                                           | 5.60 us: 1.03x faster                                                                                                 |
| pickle_pure_python         | 318 us                                                                                                            | 309 us: 1.03x faster                                                                                                  |
| telco                      | 7.84 ms                                                                                                           | 7.62 ms: 1.03x faster                                                                                                 |
| regex_dna                  | 214 ms                                                                                                            | 208 ms: 1.03x faster                                                                                                  |
| bpe_tokeniser              | 4.43 sec                                                                                                          | 4.33 sec: 1.02x faster                                                                                                |
| async_tree_cpu_io_mixed_tg | 488 ms                                                                                                            | 477 ms: 1.02x faster                                                                                                  |
| bench_mp_pool              | 82.5 ms                                                                                                           | 80.8 ms: 1.02x faster                                                                                                 |
| sqlite_synth               | 2.77 us                                                                                                           | 2.72 us: 1.02x faster                                                                                                 |
| xml_etree_iterparse        | 96.9 ms                                                                                                           | 95.0 ms: 1.02x faster                                                                                                 |
| coverage                   | 91.1 ms                                                                                                           | 89.6 ms: 1.02x faster                                                                                                 |
| deepcopy_memo              | 30.9 us                                                                                                           | 30.4 us: 1.02x faster                                                                                                 |
| coroutines                 | 23.7 ms                                                                                                           | 23.5 ms: 1.01x faster                                                                                                 |
| python_startup             | 13.0 ms                                                                                                           | 12.8 ms: 1.01x faster                                                                                                 |
| async_tree_none_tg         | 257 ms                                                                                                            | 255 ms: 1.01x faster                                                                                                  |
| pyflate                    | 470 ms                                                                                                            | 465 ms: 1.01x faster                                                                                                  |
| async_tree_cpu_io_mixed    | 495 ms                                                                                                            | 492 ms: 1.01x faster                                                                                                  |
| chaos                      | 58.9 ms                                                                                                           | 58.6 ms: 1.00x faster                                                                                                 |
| dulwich_log                | 67.0 ms                                                                                                           | 66.7 ms: 1.00x faster                                                                                                 |
| python_startup_no_site     | 7.09 ms                                                                                                           | 7.06 ms: 1.00x faster                                                                                                 |
| pidigits                   | 186 ms                                                                                                            | 186 ms: 1.00x faster                                                                                                  |
| create_gc_cycles           | 2.45 ms                                                                                                           | 2.46 ms: 1.00x slower                                                                                                 |
| sqlalchemy_declarative     | 130 ms                                                                                                            | 131 ms: 1.01x slower                                                                                                  |
| pickle                     | 12.6 us                                                                                                           | 12.7 us: 1.01x slower                                                                                                 |
| shortest_path              | 473 ms                                                                                                            | 478 ms: 1.01x slower                                                                                                  |
| sqlglot_parse              | 1.27 ms                                                                                                           | 1.28 ms: 1.01x slower                                                                                                 |
| connected_components       | 433 ms                                                                                                            | 438 ms: 1.01x slower                                                                                                  |
| json_loads                 | 28.4 us                                                                                                           | 28.8 us: 1.01x slower                                                                                                 |
| asyncio_tcp_ssl            | 1.80 sec                                                                                                          | 1.82 sec: 1.01x slower                                                                                                |
| sqlglot_transpile          | 1.57 ms                                                                                                           | 1.59 ms: 1.01x slower                                                                                                 |
| json                       | 5.13 ms                                                                                                           | 5.19 ms: 1.01x slower                                                                                                 |
| many_optionals             | 947 us                                                                                                            | 960 us: 1.01x slower                                                                                                  |
| regex_compile              | 126 ms                                                                                                            | 128 ms: 1.02x slower                                                                                                  |
| deepcopy_reduce            | 2.66 us                                                                                                           | 2.70 us: 1.02x slower                                                                                                 |
| logging_silent             | 107 ns                                                                                                            | 109 ns: 1.02x slower                                                                                                  |
| 2to3                       | 254 ms                                                                                                            | 260 ms: 1.02x slower                                                                                                  |
| async_tree_memoization     | 322 ms                                                                                                            | 328 ms: 1.02x slower                                                                                                  |
| docutils                   | 2.62 sec                                                                                                          | 2.67 sec: 1.02x slower                                                                                                |
| bench_thread_pool          | 871 us                                                                                                            | 891 us: 1.02x slower                                                                                                  |
| sphinx                     | 1.01 sec                                                                                                          | 1.04 sec: 1.02x slower                                                                                                |
| async_tree_none            | 263 ms                                                                                                            | 270 ms: 1.03x slower                                                                                                  |
| meteor_contest             | 105 ms                                                                                                            | 108 ms: 1.03x slower                                                                                                  |
| mdp                        | 2.48 sec                                                                                                          | 2.56 sec: 1.03x slower                                                                                                |
| subparsers                 | 20.3 ms                                                                                                           | 20.9 ms: 1.03x slower                                                                                                 |
| gc_traversal               | 4.58 ms                                                                                                           | 4.72 ms: 1.03x slower                                                                                                 |
| pprint_pformat             | 1.46 sec                                                                                                          | 1.51 sec: 1.03x slower                                                                                                |
| sympy_sum                  | 150 ms                                                                                                            | 155 ms: 1.03x slower                                                                                                  |
| unpickle                   | 13.9 us                                                                                                           | 14.4 us: 1.03x slower                                                                                                 |
| sympy_integrate            | 19.9 ms                                                                                                           | 20.5 ms: 1.03x slower                                                                                                 |
| sympy_expand               | 455 ms                                                                                                            | 471 ms: 1.04x slower                                                                                                  |
| async_generators           | 392 ms                                                                                                            | 407 ms: 1.04x slower                                                                                                  |
| pickle_dict                | 35.3 us                                                                                                           | 36.6 us: 1.04x slower                                                                                                 |
| pylint                     | 276 ms                                                                                                            | 287 ms: 1.04x slower                                                                                                  |
| comprehensions             | 16.5 us                                                                                                           | 17.2 us: 1.04x slower                                                                                                 |
| pprint_safe_repr           | 714 ms                                                                                                            | 744 ms: 1.04x slower                                                                                                  |
| sympy_str                  | 268 ms                                                                                                            | 280 ms: 1.04x slower                                                                                                  |
| pickle_list                | 5.42 us                                                                                                           | 5.70 us: 1.05x slower                                                                                                 |
| logging_format             | 6.06 us                                                                                                           | 6.38 us: 1.05x slower                                                                                                 |
| html5lib                   | 61.3 ms                                                                                                           | 64.8 ms: 1.06x slower                                                                                                 |
| typing_runtime_protocols   | 158 us                                                                                                            | 167 us: 1.06x slower                                                                                                  |
| go                         | 118 ms                                                                                                            | 124 ms: 1.06x slower                                                                                                  |
| sqlglot_normalize          | 103 ms                                                                                                            | 109 ms: 1.06x slower                                                                                                  |
| sqlglot_optimize           | 52.0 ms                                                                                                           | 55.0 ms: 1.06x slower                                                                                                 |
| raytrace                   | 272 ms                                                                                                            | 288 ms: 1.06x slower                                                                                                  |
| django_template            | 31.7 ms                                                                                                           | 33.8 ms: 1.06x slower                                                                                                 |
| deltablue                  | 3.26 ms                                                                                                           | 3.47 ms: 1.07x slower                                                                                                 |
| logging_simple             | 5.43 us                                                                                                           | 5.81 us: 1.07x slower                                                                                                 |
| genshi_text                | 21.4 ms                                                                                                           | 23.1 ms: 1.08x slower                                                                                                 |
| deepcopy                   | 255 us                                                                                                            | 279 us: 1.09x slower                                                                                                  |
| nqueens                    | 80.1 ms                                                                                                           | 89.2 ms: 1.11x slower                                                                                                 |
| hexiom                     | 6.22 ms                                                                                                           | 7.40 ms: 1.19x slower                                                                                                 |
| genshi_xml                 | 48.2 ms                                                                                                           | 58.4 ms: 1.21x slower                                                                                                 |
| generators                 | 27.5 ms                                                                                                           | 37.4 ms: 1.36x slower                                                                                                 |
| unpack_sequence            | 44.5 ns                                                                                                           | 70.4 ns: 1.58x slower                                                                                                 |
| Geometric mean             | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmark hidden because not significant (12): crypto_pyaes, async_tree_io_tg, asyncio_websockets, pathlib, pycparser, asyncio_tcp, scimark_lu, async_tree_memoization_tg, xml_etree_parse, thrift, async_tree_io, k_core

- Geometric mean (including insignificant results): 1.006x slower

# HPT report

- Reliability score: 78.19% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x