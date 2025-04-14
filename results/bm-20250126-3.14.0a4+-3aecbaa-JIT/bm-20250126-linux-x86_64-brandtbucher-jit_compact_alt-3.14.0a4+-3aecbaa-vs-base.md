# Results vs. base

- fork: brandtbucher
- ref: jit_compact_alt
- machine: linux-x86_64
- commit hash: 3aecbaa
- commit date: 2025-01-26
- overall geometric mean: 1.029x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250122-linux-x86_64-python-86c1a60d5a28cfb51f88-3.14.0a4+-86c1a60 | bm-20250126-linux-x86_64-brandtbucher-jit_compact_alt-3.14.0a4+-3aecbaa |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 261 ms                                                                 | 263 ms: 1.01x slower                                                    |
| docutils       | 2.69 sec                                                               | 2.83 sec: 1.05x slower                                                  |
| html5lib       | 62.6 ms                                                                | 65.4 ms: 1.04x slower                                                   |
| sphinx         | 1.05 sec                                                               | 1.10 sec: 1.06x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.04x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250122-linux-x86_64-python-86c1a60d5a28cfb51f88-3.14.0a4+-86c1a60 | bm-20250126-linux-x86_64-brandtbucher-jit_compact_alt-3.14.0a4+-3aecbaa |
|----------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_generators           | 416 ms                                                                 | 396 ms: 1.05x faster                                                    |
| asyncio_websockets         | 552 ms                                                                 | 556 ms: 1.01x slower                                                    |
| async_tree_cpu_io_mixed_tg | 479 ms                                                                 | 488 ms: 1.02x slower                                                    |
| async_tree_cpu_io_mixed    | 496 ms                                                                 | 505 ms: 1.02x slower                                                    |
| coroutines                 | 23.8 ms                                                                | 24.3 ms: 1.02x slower                                                   |
| async_tree_memoization     | 324 ms                                                                 | 338 ms: 1.04x slower                                                    |
| async_tree_none            | 257 ms                                                                 | 268 ms: 1.04x slower                                                    |
| async_tree_memoization_tg  | 312 ms                                                                 | 326 ms: 1.05x slower                                                    |
| async_tree_none_tg         | 251 ms                                                                 | 262 ms: 1.05x slower                                                    |
| async_tree_io              | 605 ms                                                                 | 637 ms: 1.05x slower                                                    |
| async_tree_io_tg           | 592 ms                                                                 | 625 ms: 1.06x slower                                                    |
| Geometric mean             | (ref)                                                                  | 1.03x slower                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250122-linux-x86_64-python-86c1a60d5a28cfb51f88-3.14.0a4+-86c1a60 | bm-20250126-linux-x86_64-brandtbucher-jit_compact_alt-3.14.0a4+-3aecbaa |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 65.2 ms                                                                | 67.6 ms: 1.04x slower                                                   |
| nbody          | 87.2 ms                                                                | 92.9 ms: 1.06x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250122-linux-x86_64-python-86c1a60d5a28cfb51f88-3.14.0a4+-86c1a60 | bm-20250126-linux-x86_64-brandtbucher-jit_compact_alt-3.14.0a4+-3aecbaa |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 209 ms                                                                 | 209 ms: 1.00x faster                                                    |
| regex_effbot   | 3.24 ms                                                                | 3.27 ms: 1.01x slower                                                   |
| regex_v8       | 23.9 ms                                                                | 24.3 ms: 1.02x slower                                                   |
| regex_compile  | 130 ms                                                                 | 133 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250122-linux-x86_64-python-86c1a60d5a28cfb51f88-3.14.0a4+-86c1a60 | bm-20250126-linux-x86_64-brandtbucher-jit_compact_alt-3.14.0a4+-3aecbaa |
|----------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 139 ms                                                                 | 137 ms: 1.02x faster                                                    |
| json_loads           | 29.4 us                                                                | 29.2 us: 1.01x faster                                                   |
| xml_etree_generate   | 78.8 ms                                                                | 79.6 ms: 1.01x slower                                                   |
| json_dumps           | 11.7 ms                                                                | 11.9 ms: 1.02x slower                                                   |
| tomli_loads          | 1.84 sec                                                               | 1.90 sec: 1.03x slower                                                  |
| pickle_pure_python   | 318 us                                                                 | 332 us: 1.04x slower                                                    |
| xml_etree_process    | 57.0 ms                                                                | 59.7 ms: 1.05x slower                                                   |
| unpickle_pure_python | 205 us                                                                 | 237 us: 1.16x slower                                                    |
| Geometric mean       | (ref)                                                                  | 1.03x slower                                                            |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250122-linux-x86_64-python-86c1a60d5a28cfb51f88-3.14.0a4+-86c1a60 | bm-20250126-linux-x86_64-brandtbucher-jit_compact_alt-3.14.0a4+-3aecbaa |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 12.9 ms                                                                | 13.0 ms: 1.01x slower                                                   |
| python_startup_no_site | 7.10 ms                                                                | 7.33 ms: 1.03x slower                                                   |
| Geometric mean         | (ref)                                                                  | 1.02x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250122-linux-x86_64-python-86c1a60d5a28cfb51f88-3.14.0a4+-86c1a60 | bm-20250126-linux-x86_64-brandtbucher-jit_compact_alt-3.14.0a4+-3aecbaa |
|-----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 57.5 ms                                                                | 51.0 ms: 1.13x faster                                                   |
| genshi_text     | 24.2 ms                                                                | 23.2 ms: 1.04x faster                                                   |
| mako            | 9.99 ms                                                                | 10.4 ms: 1.04x slower                                                   |
| django_template | 33.0 ms                                                                | 34.7 ms: 1.05x slower                                                   |
| Geometric mean  | (ref)                                                                  | 1.02x faster                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20250122-linux-x86_64-python-86c1a60d5a28cfb51f88-3.14.0a4+-86c1a60 | bm-20250126-linux-x86_64-brandtbucher-jit_compact_alt-3.14.0a4+-3aecbaa |
|----------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| hexiom                     | 7.03 ms                                                                | 6.06 ms: 1.16x faster                                                   |
| richards                   | 46.8 ms                                                                | 41.1 ms: 1.14x faster                                                   |
| genshi_xml                 | 57.5 ms                                                                | 51.0 ms: 1.13x faster                                                   |
| nqueens                    | 89.5 ms                                                                | 81.2 ms: 1.10x faster                                                   |
| richards_super             | 49.3 ms                                                                | 46.9 ms: 1.05x faster                                                   |
| async_generators           | 416 ms                                                                 | 396 ms: 1.05x faster                                                    |
| genshi_text                | 24.2 ms                                                                | 23.2 ms: 1.04x faster                                                   |
| deepcopy_memo              | 30.3 us                                                                | 29.3 us: 1.03x faster                                                   |
| comprehensions             | 17.2 us                                                                | 16.7 us: 1.03x faster                                                   |
| meteor_contest             | 109 ms                                                                 | 106 ms: 1.02x faster                                                    |
| xml_etree_parse            | 139 ms                                                                 | 137 ms: 1.02x faster                                                    |
| mdp                        | 2.56 sec                                                               | 2.52 sec: 1.02x faster                                                  |
| logging_silent             | 107 ns                                                                 | 106 ns: 1.01x faster                                                    |
| gc_traversal               | 4.65 ms                                                                | 4.61 ms: 1.01x faster                                                   |
| generators                 | 38.8 ms                                                                | 38.5 ms: 1.01x faster                                                   |
| json_loads                 | 29.4 us                                                                | 29.2 us: 1.01x faster                                                   |
| shortest_path              | 476 ms                                                                 | 474 ms: 1.00x faster                                                    |
| regex_dna                  | 209 ms                                                                 | 209 ms: 1.00x faster                                                    |
| create_gc_cycles           | 2.46 ms                                                                | 2.46 ms: 1.00x slower                                                   |
| crypto_pyaes               | 68.6 ms                                                                | 69.0 ms: 1.01x slower                                                   |
| 2to3                       | 261 ms                                                                 | 263 ms: 1.01x slower                                                    |
| sqlglot_normalize          | 109 ms                                                                 | 110 ms: 1.01x slower                                                    |
| asyncio_websockets         | 552 ms                                                                 | 556 ms: 1.01x slower                                                    |
| json                       | 5.29 ms                                                                | 5.33 ms: 1.01x slower                                                   |
| python_startup             | 12.9 ms                                                                | 13.0 ms: 1.01x slower                                                   |
| pprint_pformat             | 1.51 sec                                                               | 1.53 sec: 1.01x slower                                                  |
| xml_etree_generate         | 78.8 ms                                                                | 79.6 ms: 1.01x slower                                                   |
| regex_effbot               | 3.24 ms                                                                | 3.27 ms: 1.01x slower                                                   |
| coverage                   | 91.3 ms                                                                | 92.5 ms: 1.01x slower                                                   |
| typing_runtime_protocols   | 169 us                                                                 | 172 us: 1.02x slower                                                    |
| regex_v8                   | 23.9 ms                                                                | 24.3 ms: 1.02x slower                                                   |
| json_dumps                 | 11.7 ms                                                                | 11.9 ms: 1.02x slower                                                   |
| async_tree_cpu_io_mixed_tg | 479 ms                                                                 | 488 ms: 1.02x slower                                                    |
| sqlite_synth               | 2.72 us                                                                | 2.77 us: 1.02x slower                                                   |
| async_tree_cpu_io_mixed    | 496 ms                                                                 | 505 ms: 1.02x slower                                                    |
| scimark_monte_carlo        | 62.9 ms                                                                | 64.1 ms: 1.02x slower                                                   |
| scimark_fft                | 312 ms                                                                 | 318 ms: 1.02x slower                                                    |
| coroutines                 | 23.8 ms                                                                | 24.3 ms: 1.02x slower                                                   |
| pprint_safe_repr           | 734 ms                                                                 | 750 ms: 1.02x slower                                                    |
| scimark_sparse_mat_mult    | 4.61 ms                                                                | 4.72 ms: 1.02x slower                                                   |
| regex_compile              | 130 ms                                                                 | 133 ms: 1.02x slower                                                    |
| raytrace                   | 281 ms                                                                 | 290 ms: 1.03x slower                                                    |
| tomli_loads                | 1.84 sec                                                               | 1.90 sec: 1.03x slower                                                  |
| python_startup_no_site     | 7.10 ms                                                                | 7.33 ms: 1.03x slower                                                   |
| pycparser                  | 1.14 sec                                                               | 1.18 sec: 1.03x slower                                                  |
| sympy_expand               | 472 ms                                                                 | 489 ms: 1.04x slower                                                    |
| scimark_sor                | 113 ms                                                                 | 117 ms: 1.04x slower                                                    |
| bpe_tokeniser              | 4.38 sec                                                               | 4.54 sec: 1.04x slower                                                  |
| float                      | 65.2 ms                                                                | 67.6 ms: 1.04x slower                                                   |
| sqlglot_optimize           | 54.6 ms                                                                | 56.8 ms: 1.04x slower                                                   |
| mako                       | 9.99 ms                                                                | 10.4 ms: 1.04x slower                                                   |
| async_tree_memoization     | 324 ms                                                                 | 338 ms: 1.04x slower                                                    |
| fannkuch                   | 389 ms                                                                 | 406 ms: 1.04x slower                                                    |
| telco                      | 7.54 ms                                                                | 7.86 ms: 1.04x slower                                                   |
| pickle_pure_python         | 318 us                                                                 | 332 us: 1.04x slower                                                    |
| async_tree_none            | 257 ms                                                                 | 268 ms: 1.04x slower                                                    |
| sympy_str                  | 280 ms                                                                 | 292 ms: 1.04x slower                                                    |
| html5lib                   | 62.6 ms                                                                | 65.4 ms: 1.04x slower                                                   |
| async_tree_memoization_tg  | 312 ms                                                                 | 326 ms: 1.05x slower                                                    |
| async_tree_none_tg         | 251 ms                                                                 | 262 ms: 1.05x slower                                                    |
| xml_etree_process          | 57.0 ms                                                                | 59.7 ms: 1.05x slower                                                   |
| sqlglot_parse              | 1.26 ms                                                                | 1.32 ms: 1.05x slower                                                   |
| pyflate                    | 430 ms                                                                 | 451 ms: 1.05x slower                                                    |
| django_template            | 33.0 ms                                                                | 34.7 ms: 1.05x slower                                                   |
| docutils                   | 2.69 sec                                                               | 2.83 sec: 1.05x slower                                                  |
| async_tree_io              | 605 ms                                                                 | 637 ms: 1.05x slower                                                    |
| sphinx                     | 1.05 sec                                                               | 1.10 sec: 1.06x slower                                                  |
| scimark_lu                 | 113 ms                                                                 | 120 ms: 1.06x slower                                                    |
| async_tree_io_tg           | 592 ms                                                                 | 625 ms: 1.06x slower                                                    |
| thrift                     | 780 us                                                                 | 824 us: 1.06x slower                                                    |
| spectral_norm              | 93.3 ms                                                                | 99.0 ms: 1.06x slower                                                   |
| sqlglot_transpile          | 1.59 ms                                                                | 1.69 ms: 1.06x slower                                                   |
| nbody                      | 87.2 ms                                                                | 92.9 ms: 1.06x slower                                                   |
| deltablue                  | 3.17 ms                                                                | 3.38 ms: 1.07x slower                                                   |
| subparsers                 | 21.0 ms                                                                | 22.6 ms: 1.08x slower                                                   |
| go                         | 131 ms                                                                 | 143 ms: 1.08x slower                                                    |
| many_optionals             | 986 us                                                                 | 1.07 ms: 1.09x slower                                                   |
| bench_thread_pool          | 888 us                                                                 | 972 us: 1.09x slower                                                    |
| bench_mp_pool              | 81.7 ms                                                                | 90.2 ms: 1.10x slower                                                   |
| dulwich_log                | 68.1 ms                                                                | 75.6 ms: 1.11x slower                                                   |
| sympy_integrate            | 20.6 ms                                                                | 23.1 ms: 1.12x slower                                                   |
| sympy_sum                  | 156 ms                                                                 | 178 ms: 1.14x slower                                                    |
| unpickle_pure_python       | 205 us                                                                 | 237 us: 1.16x slower                                                    |
| logging_format             | 6.57 us                                                                | 7.87 us: 1.20x slower                                                   |
| logging_simple             | 5.95 us                                                                | 7.26 us: 1.22x slower                                                   |
| pylint                     | 288 ms                                                                 | 353 ms: 1.23x slower                                                    |
| sqlalchemy_declarative     | 133 ms                                                                 | 166 ms: 1.25x slower                                                    |
| sqlalchemy_imperative      | 17.1 ms                                                                | 21.6 ms: 1.26x slower                                                   |
| Geometric mean             | (ref)                                                                  | 1.03x slower                                                            |

Benchmark hidden because not significant (8): k_core, pathlib, xml_etree_iterparse, connected_components, deepcopy, pidigits, deepcopy_reduce, chaos

- Geometric mean (including insignificant results): 1.029x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.12x