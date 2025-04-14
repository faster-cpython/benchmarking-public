# Results vs. base

- fork: brandtbucher
- ref: unbox
- machine: linux-x86_64
- commit hash: 1baa231
- commit date: 2025-04-01
- overall geometric mean: 1.032x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 262 ms                                                                 | 270 ms: 1.03x slower                                          |
| docutils       | 2.66 sec                                                               | 2.73 sec: 1.03x slower                                        |
| html5lib       | 63.2 ms                                                                | 63.9 ms: 1.01x slower                                         |
| sphinx         | 1.02 sec                                                               | 1.04 sec: 1.02x slower                                        |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| coroutines                 | 23.1 ms                                                                | 20.7 ms: 1.12x faster                                         |
| async_tree_cpu_io_mixed    | 488 ms                                                                 | 497 ms: 1.02x slower                                          |
| async_tree_cpu_io_mixed_tg | 476 ms                                                                 | 486 ms: 1.02x slower                                          |
| async_tree_none            | 261 ms                                                                 | 267 ms: 1.02x slower                                          |
| async_tree_memoization     | 314 ms                                                                 | 323 ms: 1.03x slower                                          |
| async_tree_io              | 617 ms                                                                 | 634 ms: 1.03x slower                                          |
| async_generators           | 412 ms                                                                 | 426 ms: 1.03x slower                                          |
| async_tree_io_tg           | 614 ms                                                                 | 637 ms: 1.04x slower                                          |
| async_tree_none_tg         | 249 ms                                                                 | 259 ms: 1.04x slower                                          |
| async_tree_memoization_tg  | 315 ms                                                                 | 328 ms: 1.04x slower                                          |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                  |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| pidigits       | 185 ms                                                                 | 188 ms: 1.01x slower                                          |
| nbody          | 84.7 ms                                                                | 91.3 ms: 1.08x slower                                         |
| float          | 62.7 ms                                                                | 69.7 ms: 1.11x slower                                         |
| Geometric mean | (ref)                                                                  | 1.07x slower                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_v8       | 22.2 ms                                                                | 22.5 ms: 1.01x slower                                         |
| regex_effbot   | 3.16 ms                                                                | 3.19 ms: 1.01x slower                                         |
| regex_compile  | 128 ms                                                                 | 133 ms: 1.04x slower                                          |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                  |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| tomli_loads          | 1.87 sec                                                               | 1.79 sec: 1.05x faster                                        |
| json_dumps           | 11.6 ms                                                                | 11.5 ms: 1.01x faster                                         |
| xml_etree_parse      | 140 ms                                                                 | 142 ms: 1.01x slower                                          |
| xml_etree_iterparse  | 98.3 ms                                                                | 100 ms: 1.02x slower                                          |
| pickle_pure_python   | 322 us                                                                 | 334 us: 1.04x slower                                          |
| xml_etree_process    | 56.4 ms                                                                | 58.8 ms: 1.04x slower                                         |
| xml_etree_generate   | 79.7 ms                                                                | 83.5 ms: 1.05x slower                                         |
| json_loads           | 29.5 us                                                                | 31.9 us: 1.08x slower                                         |
| unpickle_pure_python | 214 us                                                                 | 231 us: 1.08x slower                                          |
| Geometric mean       | (ref)                                                                  | 1.03x slower                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup_no_site | 8.17 ms                                                                | 8.21 ms: 1.00x slower                                         |
| python_startup         | 13.1 ms                                                                | 13.2 ms: 1.01x slower                                         |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| genshi_xml      | 49.6 ms                                                                | 50.5 ms: 1.02x slower                                         |
| django_template | 32.2 ms                                                                | 33.1 ms: 1.03x slower                                         |
| genshi_text     | 21.1 ms                                                                | 21.9 ms: 1.03x slower                                         |
| mako            | 10.9 ms                                                                | 11.8 ms: 1.07x slower                                         |
| Geometric mean  | (ref)                                                                  | 1.04x slower                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| coroutines                 | 23.1 ms                                                                | 20.7 ms: 1.12x faster                                         |
| tomli_loads                | 1.87 sec                                                               | 1.79 sec: 1.05x faster                                        |
| json_dumps                 | 11.6 ms                                                                | 11.5 ms: 1.01x faster                                         |
| python_startup_no_site     | 8.17 ms                                                                | 8.21 ms: 1.00x slower                                         |
| python_startup             | 13.1 ms                                                                | 13.2 ms: 1.01x slower                                         |
| gc_traversal               | 5.03 ms                                                                | 5.06 ms: 1.01x slower                                         |
| create_gc_cycles           | 2.48 ms                                                                | 2.49 ms: 1.01x slower                                         |
| bench_mp_pool              | 83.0 ms                                                                | 83.7 ms: 1.01x slower                                         |
| pathlib                    | 16.6 ms                                                                | 16.8 ms: 1.01x slower                                         |
| regex_v8                   | 22.2 ms                                                                | 22.5 ms: 1.01x slower                                         |
| connected_components       | 454 ms                                                                 | 459 ms: 1.01x slower                                          |
| bpe_tokeniser              | 4.56 sec                                                               | 4.61 sec: 1.01x slower                                        |
| regex_effbot               | 3.16 ms                                                                | 3.19 ms: 1.01x slower                                         |
| html5lib                   | 63.2 ms                                                                | 63.9 ms: 1.01x slower                                         |
| pidigits                   | 185 ms                                                                 | 188 ms: 1.01x slower                                          |
| xml_etree_parse            | 140 ms                                                                 | 142 ms: 1.01x slower                                          |
| deepcopy                   | 262 us                                                                 | 266 us: 1.01x slower                                          |
| sqlite_synth               | 2.75 us                                                                | 2.79 us: 1.01x slower                                         |
| bench_thread_pool          | 883 us                                                                 | 897 us: 1.02x slower                                          |
| sqlglot_v2_normalize       | 109 ms                                                                 | 111 ms: 1.02x slower                                          |
| genshi_xml                 | 49.6 ms                                                                | 50.5 ms: 1.02x slower                                         |
| xml_etree_iterparse        | 98.3 ms                                                                | 100 ms: 1.02x slower                                          |
| async_tree_cpu_io_mixed    | 488 ms                                                                 | 497 ms: 1.02x slower                                          |
| sphinx                     | 1.02 sec                                                               | 1.04 sec: 1.02x slower                                        |
| sqlalchemy_imperative      | 17.1 ms                                                                | 17.5 ms: 1.02x slower                                         |
| k_core                     | 2.31 sec                                                               | 2.36 sec: 1.02x slower                                        |
| subparsers                 | 21.0 ms                                                                | 21.4 ms: 1.02x slower                                         |
| shortest_path              | 496 ms                                                                 | 507 ms: 1.02x slower                                          |
| async_tree_cpu_io_mixed_tg | 476 ms                                                                 | 486 ms: 1.02x slower                                          |
| pprint_pformat             | 1.60 sec                                                               | 1.63 sec: 1.02x slower                                        |
| sqlalchemy_declarative     | 132 ms                                                                 | 135 ms: 1.02x slower                                          |
| async_tree_none            | 261 ms                                                                 | 267 ms: 1.02x slower                                          |
| generators                 | 27.9 ms                                                                | 28.5 ms: 1.02x slower                                         |
| sympy_str                  | 274 ms                                                                 | 281 ms: 1.02x slower                                          |
| sympy_sum                  | 150 ms                                                                 | 154 ms: 1.02x slower                                          |
| logging_silent             | 101 ns                                                                 | 103 ns: 1.02x slower                                          |
| dulwich_log                | 60.3 ms                                                                | 61.9 ms: 1.03x slower                                         |
| sympy_expand               | 475 ms                                                                 | 487 ms: 1.03x slower                                          |
| many_optionals             | 971 us                                                                 | 997 us: 1.03x slower                                          |
| async_tree_memoization     | 314 ms                                                                 | 323 ms: 1.03x slower                                          |
| docutils                   | 2.66 sec                                                               | 2.73 sec: 1.03x slower                                        |
| async_tree_io              | 617 ms                                                                 | 634 ms: 1.03x slower                                          |
| sqlglot_v2_optimize        | 54.6 ms                                                                | 56.1 ms: 1.03x slower                                         |
| django_template            | 32.2 ms                                                                | 33.1 ms: 1.03x slower                                         |
| deepcopy_memo              | 29.0 us                                                                | 29.9 us: 1.03x slower                                         |
| sympy_integrate            | 19.8 ms                                                                | 20.4 ms: 1.03x slower                                         |
| mdp                        | 1.24 sec                                                               | 1.27 sec: 1.03x slower                                        |
| 2to3                       | 262 ms                                                                 | 270 ms: 1.03x slower                                          |
| fannkuch                   | 418 ms                                                                 | 431 ms: 1.03x slower                                          |
| async_generators           | 412 ms                                                                 | 426 ms: 1.03x slower                                          |
| hexiom                     | 6.73 ms                                                                | 6.96 ms: 1.03x slower                                         |
| genshi_text                | 21.1 ms                                                                | 21.9 ms: 1.03x slower                                         |
| json                       | 5.27 ms                                                                | 5.46 ms: 1.04x slower                                         |
| nqueens                    | 83.5 ms                                                                | 86.4 ms: 1.04x slower                                         |
| deepcopy_reduce            | 2.72 us                                                                | 2.82 us: 1.04x slower                                         |
| meteor_contest             | 108 ms                                                                 | 112 ms: 1.04x slower                                          |
| pickle_pure_python         | 322 us                                                                 | 334 us: 1.04x slower                                          |
| telco                      | 7.77 ms                                                                | 8.06 ms: 1.04x slower                                         |
| async_tree_io_tg           | 614 ms                                                                 | 637 ms: 1.04x slower                                          |
| async_tree_none_tg         | 249 ms                                                                 | 259 ms: 1.04x slower                                          |
| typing_runtime_protocols   | 168 us                                                                 | 174 us: 1.04x slower                                          |
| raytrace                   | 270 ms                                                                 | 281 ms: 1.04x slower                                          |
| pprint_safe_repr           | 773 ms                                                                 | 805 ms: 1.04x slower                                          |
| async_tree_memoization_tg  | 315 ms                                                                 | 328 ms: 1.04x slower                                          |
| scimark_monte_carlo        | 67.0 ms                                                                | 69.8 ms: 1.04x slower                                         |
| xml_etree_process          | 56.4 ms                                                                | 58.8 ms: 1.04x slower                                         |
| regex_compile              | 128 ms                                                                 | 133 ms: 1.04x slower                                          |
| comprehensions             | 18.8 us                                                                | 19.6 us: 1.04x slower                                         |
| sqlglot_v2_transpile       | 1.59 ms                                                                | 1.66 ms: 1.05x slower                                         |
| xml_etree_generate         | 79.7 ms                                                                | 83.5 ms: 1.05x slower                                         |
| sqlglot_v2_parse           | 1.28 ms                                                                | 1.35 ms: 1.05x slower                                         |
| spectral_norm              | 93.8 ms                                                                | 99.5 ms: 1.06x slower                                         |
| scimark_fft                | 310 ms                                                                 | 329 ms: 1.06x slower                                          |
| mako                       | 10.9 ms                                                                | 11.8 ms: 1.07x slower                                         |
| scimark_lu                 | 116 ms                                                                 | 124 ms: 1.07x slower                                          |
| richards                   | 35.3 ms                                                                | 38.0 ms: 1.08x slower                                         |
| nbody                      | 84.7 ms                                                                | 91.3 ms: 1.08x slower                                         |
| json_loads                 | 29.5 us                                                                | 31.9 us: 1.08x slower                                         |
| unpickle_pure_python       | 214 us                                                                 | 231 us: 1.08x slower                                          |
| richards_super             | 40.7 ms                                                                | 44.1 ms: 1.08x slower                                         |
| go                         | 126 ms                                                                 | 138 ms: 1.09x slower                                          |
| pyflate                    | 429 ms                                                                 | 470 ms: 1.09x slower                                          |
| deltablue                  | 3.04 ms                                                                | 3.34 ms: 1.10x slower                                         |
| pycparser                  | 1.14 sec                                                               | 1.25 sec: 1.10x slower                                        |
| float                      | 62.7 ms                                                                | 69.7 ms: 1.11x slower                                         |
| scimark_sparse_mat_mult    | 4.56 ms                                                                | 5.21 ms: 1.14x slower                                         |
| crypto_pyaes               | 75.3 ms                                                                | 87.4 ms: 1.16x slower                                         |
| scimark_sor                | 120 ms                                                                 | 141 ms: 1.18x slower                                          |
| Geometric mean             | (ref)                                                                  | 1.03x slower                                                  |

Benchmark hidden because not significant (7): chaos, regex_dna, logging_format, asyncio_websockets, logging_simple, coverage, pylint

- Geometric mean (including insignificant results): 1.032x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.00x