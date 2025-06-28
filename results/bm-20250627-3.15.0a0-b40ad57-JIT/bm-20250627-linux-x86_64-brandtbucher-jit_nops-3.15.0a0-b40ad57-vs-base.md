# Results vs. base

- fork: brandtbucher
- ref: jit_nops
- machine: linux-x86_64
- commit hash: b40ad57
- commit date: 2025-06-27
- overall geometric mean: 1.008x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-b40ad57 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 258 ms                                                                | 259 ms: 1.01x slower                                            |
| docutils       | 2.62 sec                                                              | 2.64 sec: 1.01x slower                                          |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                    |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-b40ad57 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| coroutines                 | 25.0 ms                                                               | 24.7 ms: 1.01x faster                                           |
| async_tree_cpu_io_mixed_tg | 494 ms                                                                | 490 ms: 1.01x faster                                            |
| async_generators           | 432 ms                                                                | 429 ms: 1.01x faster                                            |
| async_tree_cpu_io_mixed    | 499 ms                                                                | 496 ms: 1.01x faster                                            |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                    |

Benchmark hidden because not significant (7): async_tree_memoization_tg, async_tree_io, async_tree_io_tg, async_tree_none_tg, asyncio_websockets, async_tree_memoization, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-b40ad57 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 65.3 ms                                                               | 66.1 ms: 1.01x slower                                           |
| nbody          | 93.4 ms                                                               | 96.9 ms: 1.04x slower                                           |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-b40ad57 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 126 ms                                                                | 127 ms: 1.01x slower                                            |
| regex_effbot   | 3.18 ms                                                               | 3.25 ms: 1.02x slower                                           |
| regex_dna      | 202 ms                                                                | 211 ms: 1.05x slower                                            |
| regex_v8       | 21.9 ms                                                               | 23.2 ms: 1.06x slower                                           |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-b40ad57 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| xml_etree_iterparse  | 98.2 ms                                                               | 99.0 ms: 1.01x slower                                           |
| xml_etree_generate   | 79.6 ms                                                               | 80.5 ms: 1.01x slower                                           |
| xml_etree_process    | 55.6 ms                                                               | 56.3 ms: 1.01x slower                                           |
| tomli_loads          | 1.81 sec                                                              | 1.85 sec: 1.02x slower                                          |
| pickle_pure_python   | 318 us                                                                | 328 us: 1.03x slower                                            |
| unpickle_pure_python | 193 us                                                                | 201 us: 1.05x slower                                            |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                    |

Benchmark hidden because not significant (3): json_dumps, xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-b40ad57 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                               | 6.93 ms: 1.00x faster                                           |
| python_startup         | 12.2 ms                                                               | 12.2 ms: 1.00x faster                                           |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-b40ad57 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| genshi_text     | 21.4 ms                                                               | 21.6 ms: 1.01x slower                                           |
| django_template | 32.5 ms                                                               | 32.8 ms: 1.01x slower                                           |
| genshi_xml      | 50.1 ms                                                               | 51.3 ms: 1.02x slower                                           |
| mako            | 10.5 ms                                                               | 10.8 ms: 1.03x slower                                           |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250627-linux-x86_64-brandtbucher-jit_nops-3.15.0a0-b40ad57 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols   | 170 us                                                                | 167 us: 1.02x faster                                            |
| coroutines                 | 25.0 ms                                                               | 24.7 ms: 1.01x faster                                           |
| deepcopy_memo              | 29.5 us                                                               | 29.2 us: 1.01x faster                                           |
| pathlib                    | 17.2 ms                                                               | 17.0 ms: 1.01x faster                                           |
| async_tree_cpu_io_mixed_tg | 494 ms                                                                | 490 ms: 1.01x faster                                            |
| meteor_contest             | 107 ms                                                                | 106 ms: 1.01x faster                                            |
| create_gc_cycles           | 2.59 ms                                                               | 2.58 ms: 1.01x faster                                           |
| async_generators           | 432 ms                                                                | 429 ms: 1.01x faster                                            |
| deepcopy                   | 258 us                                                                | 256 us: 1.01x faster                                            |
| async_tree_cpu_io_mixed    | 499 ms                                                                | 496 ms: 1.01x faster                                            |
| pyflate                    | 418 ms                                                                | 416 ms: 1.01x faster                                            |
| scimark_sor                | 119 ms                                                                | 119 ms: 1.01x faster                                            |
| python_startup_no_site     | 6.94 ms                                                               | 6.93 ms: 1.00x faster                                           |
| python_startup             | 12.2 ms                                                               | 12.2 ms: 1.00x faster                                           |
| gc_traversal               | 4.96 ms                                                               | 4.96 ms: 1.00x slower                                           |
| sqlglot_v2_optimize        | 52.7 ms                                                               | 52.9 ms: 1.00x slower                                           |
| sympy_expand               | 466 ms                                                                | 467 ms: 1.00x slower                                            |
| sympy_str                  | 271 ms                                                                | 272 ms: 1.00x slower                                            |
| raytrace                   | 271 ms                                                                | 273 ms: 1.01x slower                                            |
| 2to3                       | 258 ms                                                                | 259 ms: 1.01x slower                                            |
| sympy_sum                  | 149 ms                                                                | 150 ms: 1.01x slower                                            |
| sympy_integrate            | 19.2 ms                                                               | 19.3 ms: 1.01x slower                                           |
| logging_simple             | 5.61 us                                                               | 5.65 us: 1.01x slower                                           |
| sqlite_synth               | 2.79 us                                                               | 2.80 us: 1.01x slower                                           |
| logging_format             | 6.24 us                                                               | 6.28 us: 1.01x slower                                           |
| coverage                   | 87.2 ms                                                               | 87.8 ms: 1.01x slower                                           |
| subparsers                 | 23.7 ms                                                               | 23.8 ms: 1.01x slower                                           |
| logging_silent             | 101 ns                                                                | 102 ns: 1.01x slower                                            |
| thrift                     | 774 us                                                                | 780 us: 1.01x slower                                            |
| xml_etree_iterparse        | 98.2 ms                                                               | 99.0 ms: 1.01x slower                                           |
| connected_components       | 456 ms                                                                | 460 ms: 1.01x slower                                            |
| regex_compile              | 126 ms                                                                | 127 ms: 1.01x slower                                            |
| docutils                   | 2.62 sec                                                              | 2.64 sec: 1.01x slower                                          |
| genshi_text                | 21.4 ms                                                               | 21.6 ms: 1.01x slower                                           |
| django_template            | 32.5 ms                                                               | 32.8 ms: 1.01x slower                                           |
| scimark_monte_carlo        | 65.2 ms                                                               | 65.8 ms: 1.01x slower                                           |
| json                       | 5.17 ms                                                               | 5.23 ms: 1.01x slower                                           |
| sqlglot_v2_parse           | 1.24 ms                                                               | 1.25 ms: 1.01x slower                                           |
| scimark_lu                 | 118 ms                                                                | 120 ms: 1.01x slower                                            |
| xml_etree_generate         | 79.6 ms                                                               | 80.5 ms: 1.01x slower                                           |
| xml_etree_process          | 55.6 ms                                                               | 56.3 ms: 1.01x slower                                           |
| hexiom                     | 6.24 ms                                                               | 6.32 ms: 1.01x slower                                           |
| float                      | 65.3 ms                                                               | 66.1 ms: 1.01x slower                                           |
| sqlglot_v2_transpile       | 1.55 ms                                                               | 1.57 ms: 1.01x slower                                           |
| chaos                      | 60.1 ms                                                               | 60.9 ms: 1.01x slower                                           |
| pprint_safe_repr           | 712 ms                                                                | 722 ms: 1.01x slower                                            |
| spectral_norm              | 92.2 ms                                                               | 93.6 ms: 1.01x slower                                           |
| telco                      | 7.65 ms                                                               | 7.77 ms: 1.02x slower                                           |
| bpe_tokeniser              | 4.33 sec                                                              | 4.40 sec: 1.02x slower                                          |
| regex_effbot               | 3.18 ms                                                               | 3.25 ms: 1.02x slower                                           |
| tomli_loads                | 1.81 sec                                                              | 1.85 sec: 1.02x slower                                          |
| deltablue                  | 3.05 ms                                                               | 3.12 ms: 1.02x slower                                           |
| nqueens                    | 82.1 ms                                                               | 84.0 ms: 1.02x slower                                           |
| genshi_xml                 | 50.1 ms                                                               | 51.3 ms: 1.02x slower                                           |
| comprehensions             | 16.6 us                                                               | 17.0 us: 1.02x slower                                           |
| shortest_path              | 492 ms                                                                | 505 ms: 1.03x slower                                            |
| go                         | 115 ms                                                                | 118 ms: 1.03x slower                                            |
| mako                       | 10.5 ms                                                               | 10.8 ms: 1.03x slower                                           |
| pickle_pure_python         | 318 us                                                                | 328 us: 1.03x slower                                            |
| richards                   | 32.2 ms                                                               | 33.3 ms: 1.03x slower                                           |
| fannkuch                   | 400 ms                                                                | 414 ms: 1.03x slower                                            |
| nbody                      | 93.4 ms                                                               | 96.9 ms: 1.04x slower                                           |
| scimark_fft                | 311 ms                                                                | 324 ms: 1.04x slower                                            |
| unpickle_pure_python       | 193 us                                                                | 201 us: 1.05x slower                                            |
| regex_dna                  | 202 ms                                                                | 211 ms: 1.05x slower                                            |
| generators                 | 30.2 ms                                                               | 32.0 ms: 1.06x slower                                           |
| regex_v8                   | 21.9 ms                                                               | 23.2 ms: 1.06x slower                                           |
| Geometric mean             | (ref)                                                                 | 1.01x slower                                                    |

Benchmark hidden because not significant (26): pprint_pformat, async_tree_memoization_tg, json_dumps, async_tree_io, async_tree_io_tg, sqlglot_v2_normalize, async_tree_none_tg, asyncio_websockets, xml_etree_parse, html5lib, dulwich_log, k_core, pidigits, many_optionals, async_tree_memoization, json_loads, pycparser, mdp, crypto_pyaes, deepcopy_reduce, pylint, sphinx, async_tree_none, scimark_sparse_mat_mult, djangocms, richards_super

- Geometric mean (including insignificant results): 1.008x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x