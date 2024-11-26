# Results vs. base

- fork: brandtbucher
- ref: justin_reserved_fram
- machine: linux-x86_64
- commit hash: 735a0ce
- commit date: 2024-11-19
- overall geometric mean: 1.003x faster
- HPT reliability: 97.84%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241119-linux-x86_64-brandtbucher-justin_reserved_fram-3.14.0a1+-735a0ce |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                                 | 279 ms: 1.00x faster                                                         |
| docutils       | 2.95 sec                                                               | 2.93 sec: 1.00x faster                                                       |
| html5lib       | 67.0 ms                                                                | 65.7 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241119-linux-x86_64-brandtbucher-justin_reserved_fram-3.14.0a1+-735a0ce |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| coroutines                 | 23.2 ms                                                                | 22.7 ms: 1.02x faster                                                        |
| async_generators           | 456 ms                                                                 | 454 ms: 1.00x faster                                                         |
| asyncio_websockets         | 551 ms                                                                 | 553 ms: 1.00x slower                                                         |
| async_tree_io_tg           | 978 ms                                                                 | 986 ms: 1.01x slower                                                         |
| async_tree_cpu_io_mixed_tg | 565 ms                                                                 | 572 ms: 1.01x slower                                                         |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (6): async_tree_memoization_tg, async_tree_memoization, async_tree_io, async_tree_none, async_tree_cpu_io_mixed, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241119-linux-x86_64-brandtbucher-justin_reserved_fram-3.14.0a1+-735a0ce |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 187 ms                                                                 | 186 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241119-linux-x86_64-brandtbucher-justin_reserved_fram-3.14.0a1+-735a0ce |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                                | 3.65 ms: 1.03x faster                                                        |
| regex_compile  | 140 ms                                                                 | 139 ms: 1.01x faster                                                         |
| regex_dna      | 216 ms                                                                 | 219 ms: 1.01x slower                                                         |
| regex_v8       | 24.6 ms                                                                | 25.4 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241119-linux-x86_64-brandtbucher-justin_reserved_fram-3.14.0a1+-735a0ce |
|--------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads        | 2.00 sec                                                               | 1.97 sec: 1.01x faster                                                       |
| xml_etree_generate | 79.6 ms                                                                | 79.1 ms: 1.01x faster                                                        |
| json_loads         | 26.8 us                                                                | 26.7 us: 1.00x faster                                                        |
| pickle_pure_python | 321 us                                                                 | 325 us: 1.01x slower                                                         |
| Geometric mean     | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (5): xml_etree_process, unpickle_pure_python, json_dumps, xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241119-linux-x86_64-brandtbucher-justin_reserved_fram-3.14.0a1+-735a0ce |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.14 ms                                                                | 7.11 ms: 1.00x faster                                                        |
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                                        |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241119-linux-x86_64-brandtbucher-justin_reserved_fram-3.14.0a1+-735a0ce |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 59.9 ms                                                                | 58.8 ms: 1.02x faster                                                        |
| mako            | 10.3 ms                                                                | 10.1 ms: 1.01x faster                                                        |
| django_template | 34.3 ms                                                                | 33.9 ms: 1.01x faster                                                        |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241119-linux-x86_64-brandtbucher-justin_reserved_fram-3.14.0a1+-735a0ce |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| logging_silent             | 102 ns                                                                 | 96.3 ns: 1.06x faster                                                        |
| richards_super             | 47.1 ms                                                                | 45.1 ms: 1.04x faster                                                        |
| richards                   | 40.7 ms                                                                | 39.1 ms: 1.04x faster                                                        |
| gc_traversal               | 4.74 ms                                                                | 4.57 ms: 1.04x faster                                                        |
| regex_effbot               | 3.77 ms                                                                | 3.65 ms: 1.03x faster                                                        |
| raytrace                   | 283 ms                                                                 | 276 ms: 1.03x faster                                                         |
| coroutines                 | 23.2 ms                                                                | 22.7 ms: 1.02x faster                                                        |
| comprehensions             | 17.5 us                                                                | 17.1 us: 1.02x faster                                                        |
| generators                 | 36.6 ms                                                                | 35.9 ms: 1.02x faster                                                        |
| html5lib                   | 67.0 ms                                                                | 65.7 ms: 1.02x faster                                                        |
| meteor_contest             | 109 ms                                                                 | 107 ms: 1.02x faster                                                         |
| genshi_xml                 | 59.9 ms                                                                | 58.8 ms: 1.02x faster                                                        |
| mdp                        | 2.62 sec                                                               | 2.58 sec: 1.01x faster                                                       |
| mako                       | 10.3 ms                                                                | 10.1 ms: 1.01x faster                                                        |
| pyflate                    | 449 ms                                                                 | 443 ms: 1.01x faster                                                         |
| tomli_loads                | 2.00 sec                                                               | 1.97 sec: 1.01x faster                                                       |
| hexiom                     | 7.08 ms                                                                | 7.00 ms: 1.01x faster                                                        |
| sqlite_synth               | 2.80 us                                                                | 2.77 us: 1.01x faster                                                        |
| deltablue                  | 3.31 ms                                                                | 3.28 ms: 1.01x faster                                                        |
| regex_compile              | 140 ms                                                                 | 139 ms: 1.01x faster                                                         |
| django_template            | 34.3 ms                                                                | 33.9 ms: 1.01x faster                                                        |
| coverage                   | 84.9 ms                                                                | 84.0 ms: 1.01x faster                                                        |
| bpe_tokeniser              | 4.53 sec                                                               | 4.48 sec: 1.01x faster                                                       |
| sympy_expand               | 509 ms                                                                 | 504 ms: 1.01x faster                                                         |
| create_gc_cycles           | 2.71 ms                                                                | 2.69 ms: 1.01x faster                                                        |
| xml_etree_generate         | 79.6 ms                                                                | 79.1 ms: 1.01x faster                                                        |
| subparsers                 | 21.4 ms                                                                | 21.2 ms: 1.01x faster                                                        |
| sqlalchemy_declarative     | 148 ms                                                                 | 147 ms: 1.01x faster                                                         |
| bench_mp_pool              | 84.8 ms                                                                | 84.3 ms: 1.01x faster                                                        |
| sympy_integrate            | 23.6 ms                                                                | 23.4 ms: 1.01x faster                                                        |
| json_loads                 | 26.8 us                                                                | 26.7 us: 1.00x faster                                                        |
| scimark_sor                | 119 ms                                                                 | 118 ms: 1.00x faster                                                         |
| many_optionals             | 1.05 ms                                                                | 1.05 ms: 1.00x faster                                                        |
| docutils                   | 2.95 sec                                                               | 2.93 sec: 1.00x faster                                                       |
| pathlib                    | 16.1 ms                                                                | 16.0 ms: 1.00x faster                                                        |
| sympy_str                  | 305 ms                                                                 | 304 ms: 1.00x faster                                                         |
| 2to3                       | 280 ms                                                                 | 279 ms: 1.00x faster                                                         |
| async_generators           | 456 ms                                                                 | 454 ms: 1.00x faster                                                         |
| python_startup_no_site     | 7.14 ms                                                                | 7.11 ms: 1.00x faster                                                        |
| python_startup             | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                                        |
| pidigits                   | 187 ms                                                                 | 186 ms: 1.00x faster                                                         |
| connected_components       | 437 ms                                                                 | 438 ms: 1.00x slower                                                         |
| sqlglot_optimize           | 60.3 ms                                                                | 60.4 ms: 1.00x slower                                                        |
| asyncio_websockets         | 551 ms                                                                 | 553 ms: 1.00x slower                                                         |
| crypto_pyaes               | 68.5 ms                                                                | 68.9 ms: 1.01x slower                                                        |
| async_tree_io_tg           | 978 ms                                                                 | 986 ms: 1.01x slower                                                         |
| deepcopy_reduce            | 2.66 us                                                                | 2.69 us: 1.01x slower                                                        |
| async_tree_cpu_io_mixed_tg | 565 ms                                                                 | 572 ms: 1.01x slower                                                         |
| regex_dna                  | 216 ms                                                                 | 219 ms: 1.01x slower                                                         |
| pickle_pure_python         | 321 us                                                                 | 325 us: 1.01x slower                                                         |
| scimark_fft                | 318 ms                                                                 | 322 ms: 1.01x slower                                                         |
| scimark_lu                 | 113 ms                                                                 | 115 ms: 1.02x slower                                                         |
| sqlglot_normalize          | 114 ms                                                                 | 116 ms: 1.02x slower                                                         |
| deepcopy                   | 267 us                                                                 | 272 us: 1.02x slower                                                         |
| thrift                     | 779 us                                                                 | 795 us: 1.02x slower                                                         |
| pprint_safe_repr           | 724 ms                                                                 | 743 ms: 1.03x slower                                                         |
| spectral_norm              | 115 ms                                                                 | 118 ms: 1.03x slower                                                         |
| regex_v8                   | 24.6 ms                                                                | 25.4 ms: 1.03x slower                                                        |
| pycparser                  | 1.16 sec                                                               | 1.20 sec: 1.04x slower                                                       |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (38): pylint, k_core, xml_etree_process, logging_format, scimark_monte_carlo, sqlalchemy_imperative, unpickle_pure_python, genshi_text, sphinx, sympy_sum, float, bench_thread_pool, async_tree_memoization_tg, sqlglot_parse, json_dumps, logging_simple, shortest_path, nqueens, json, go, dulwich_log, pprint_pformat, nbody, xml_etree_parse, telco, fannkuch, async_tree_memoization, async_tree_io, djangocms, sqlglot_transpile, typing_runtime_protocols, async_tree_none, async_tree_cpu_io_mixed, xml_etree_iterparse, scimark_sparse_mat_mult, async_tree_none_tg, chaos, deepcopy_memo

- Geometric mean (including insignificant results): 1.003x faster
# HPT report

- Reliability score: 97.84% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x