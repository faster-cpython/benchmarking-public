# Results vs. base

- fork: brandtbucher
- ref: reset_counters
- machine: linux-x86_64
- commit hash: 3517502
- commit date: 2024-11-07
- overall geometric mean: 1.001x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241107-linux-x86_64-brandtbucher-reset_counters-3.14.0a1+-3517502 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| docutils       | 2.95 sec                                                               | 2.92 sec: 1.01x faster                                                 |
| html5lib       | 67.0 ms                                                                | 65.4 ms: 1.03x faster                                                  |
| sphinx         | 1.18 sec                                                               | 1.17 sec: 1.01x faster                                                 |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241107-linux-x86_64-brandtbucher-reset_counters-3.14.0a1+-3517502 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| coroutines                 | 23.2 ms                                                                | 22.4 ms: 1.04x faster                                                  |
| async_tree_cpu_io_mixed_tg | 565 ms                                                                 | 560 ms: 1.01x faster                                                   |
| asyncio_websockets         | 551 ms                                                                 | 558 ms: 1.01x slower                                                   |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed, async_tree_memoization, async_tree_io_tg, async_tree_io, async_tree_none_tg, async_tree_none, async_tree_memoization_tg, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241107-linux-x86_64-brandtbucher-reset_counters-3.14.0a1+-3517502 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 187 ms                                                                 | 186 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241107-linux-x86_64-brandtbucher-reset_counters-3.14.0a1+-3517502 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                                | 3.68 ms: 1.02x faster                                                  |
| regex_v8       | 24.6 ms                                                                | 24.5 ms: 1.00x faster                                                  |
| regex_dna      | 216 ms                                                                 | 216 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241107-linux-x86_64-brandtbucher-reset_counters-3.14.0a1+-3517502 |
|--------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads        | 2.00 sec                                                               | 1.94 sec: 1.03x faster                                                 |
| json_dumps         | 11.1 ms                                                                | 11.0 ms: 1.01x faster                                                  |
| json_loads         | 26.8 us                                                                | 26.6 us: 1.01x faster                                                  |
| pickle_pure_python | 321 us                                                                 | 327 us: 1.02x slower                                                   |
| Geometric mean     | (ref)                                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (5): xml_etree_generate, xml_etree_process, xml_etree_parse, unpickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241107-linux-x86_64-brandtbucher-reset_counters-3.14.0a1+-3517502 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.01x faster                                                  |
| python_startup_no_site | 7.14 ms                                                                | 7.12 ms: 1.00x faster                                                  |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241107-linux-x86_64-brandtbucher-reset_counters-3.14.0a1+-3517502 |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 10.3 ms                                                                | 10.2 ms: 1.01x faster                                                  |
| genshi_xml      | 59.9 ms                                                                | 61.9 ms: 1.03x slower                                                  |
| genshi_text     | 25.1 ms                                                                | 25.9 ms: 1.03x slower                                                  |
| django_template | 34.3 ms                                                                | 36.1 ms: 1.05x slower                                                  |
| Geometric mean  | (ref)                                                                  | 1.03x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241107-linux-x86_64-brandtbucher-reset_counters-3.14.0a1+-3517502 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| coroutines                 | 23.2 ms                                                                | 22.4 ms: 1.04x faster                                                  |
| tomli_loads                | 2.00 sec                                                               | 1.94 sec: 1.03x faster                                                 |
| comprehensions             | 17.5 us                                                                | 17.1 us: 1.03x faster                                                  |
| html5lib                   | 67.0 ms                                                                | 65.4 ms: 1.03x faster                                                  |
| regex_effbot               | 3.77 ms                                                                | 3.68 ms: 1.02x faster                                                  |
| scimark_sparse_mat_mult    | 4.62 ms                                                                | 4.51 ms: 1.02x faster                                                  |
| generators                 | 36.6 ms                                                                | 35.9 ms: 1.02x faster                                                  |
| meteor_contest             | 109 ms                                                                 | 107 ms: 1.02x faster                                                   |
| raytrace                   | 283 ms                                                                 | 278 ms: 1.02x faster                                                   |
| gc_traversal               | 4.74 ms                                                                | 4.67 ms: 1.01x faster                                                  |
| sphinx                     | 1.18 sec                                                               | 1.17 sec: 1.01x faster                                                 |
| logging_silent             | 102 ns                                                                 | 100 ns: 1.01x faster                                                   |
| sympy_str                  | 305 ms                                                                 | 301 ms: 1.01x faster                                                   |
| sympy_sum                  | 176 ms                                                                 | 174 ms: 1.01x faster                                                   |
| connected_components       | 437 ms                                                                 | 432 ms: 1.01x faster                                                   |
| bpe_tokeniser              | 4.53 sec                                                               | 4.47 sec: 1.01x faster                                                 |
| sympy_integrate            | 23.6 ms                                                                | 23.3 ms: 1.01x faster                                                  |
| sqlglot_optimize           | 60.3 ms                                                                | 59.6 ms: 1.01x faster                                                  |
| sympy_expand               | 509 ms                                                                 | 503 ms: 1.01x faster                                                   |
| create_gc_cycles           | 2.71 ms                                                                | 2.69 ms: 1.01x faster                                                  |
| mako                       | 10.3 ms                                                                | 10.2 ms: 1.01x faster                                                  |
| json_dumps                 | 11.1 ms                                                                | 11.0 ms: 1.01x faster                                                  |
| shortest_path              | 482 ms                                                                 | 478 ms: 1.01x faster                                                   |
| async_tree_cpu_io_mixed_tg | 565 ms                                                                 | 560 ms: 1.01x faster                                                   |
| json_loads                 | 26.8 us                                                                | 26.6 us: 1.01x faster                                                  |
| sqlite_synth               | 2.80 us                                                                | 2.78 us: 1.01x faster                                                  |
| docutils                   | 2.95 sec                                                               | 2.92 sec: 1.01x faster                                                 |
| deltablue                  | 3.31 ms                                                                | 3.29 ms: 1.01x faster                                                  |
| python_startup             | 12.8 ms                                                                | 12.8 ms: 1.01x faster                                                  |
| scimark_monte_carlo        | 64.8 ms                                                                | 64.4 ms: 1.01x faster                                                  |
| regex_v8                   | 24.6 ms                                                                | 24.5 ms: 1.00x faster                                                  |
| python_startup_no_site     | 7.14 ms                                                                | 7.12 ms: 1.00x faster                                                  |
| regex_dna                  | 216 ms                                                                 | 216 ms: 1.00x faster                                                   |
| pidigits                   | 187 ms                                                                 | 186 ms: 1.00x faster                                                   |
| bench_thread_pool          | 889 us                                                                 | 891 us: 1.00x slower                                                   |
| sqlalchemy_declarative     | 148 ms                                                                 | 148 ms: 1.00x slower                                                   |
| pathlib                    | 16.1 ms                                                                | 16.1 ms: 1.00x slower                                                  |
| pyflate                    | 449 ms                                                                 | 451 ms: 1.00x slower                                                   |
| go                         | 133 ms                                                                 | 134 ms: 1.01x slower                                                   |
| scimark_sor                | 119 ms                                                                 | 120 ms: 1.01x slower                                                   |
| deepcopy_memo              | 29.6 us                                                                | 29.9 us: 1.01x slower                                                  |
| coverage                   | 84.9 ms                                                                | 85.7 ms: 1.01x slower                                                  |
| asyncio_websockets         | 551 ms                                                                 | 558 ms: 1.01x slower                                                   |
| deepcopy_reduce            | 2.66 us                                                                | 2.70 us: 1.01x slower                                                  |
| json                       | 4.98 ms                                                                | 5.06 ms: 1.02x slower                                                  |
| pickle_pure_python         | 321 us                                                                 | 327 us: 1.02x slower                                                   |
| richards_super             | 47.1 ms                                                                | 48.2 ms: 1.02x slower                                                  |
| genshi_xml                 | 59.9 ms                                                                | 61.9 ms: 1.03x slower                                                  |
| genshi_text                | 25.1 ms                                                                | 25.9 ms: 1.03x slower                                                  |
| pprint_safe_repr           | 724 ms                                                                 | 749 ms: 1.03x slower                                                   |
| django_template            | 34.3 ms                                                                | 36.1 ms: 1.05x slower                                                  |
| mdp                        | 2.62 sec                                                               | 2.76 sec: 1.06x slower                                                 |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (42): async_tree_cpu_io_mixed, async_tree_memoization, k_core, telco, async_tree_io_tg, logging_format, pylint, xml_etree_generate, pycparser, async_tree_io, xml_etree_process, fannkuch, hexiom, async_tree_none_tg, bench_mp_pool, async_tree_none, float, sqlglot_normalize, 2to3, scimark_fft, xml_etree_parse, deepcopy, sqlglot_transpile, dulwich_log, typing_runtime_protocols, spectral_norm, sqlalchemy_imperative, sqlglot_parse, nqueens, nbody, unpickle_pure_python, xml_etree_iterparse, crypto_pyaes, regex_compile, scimark_lu, async_tree_memoization_tg, async_generators, thrift, logging_simple, chaos, richards, pprint_pformat
Ignored benchmarks (3) of results/bm-20241107-3.14.0a1+-09d6f5d-JIT/bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d.json: djangocms, many_optionals, subparsers

- Geometric mean (including insignificant results): 1.001x faster
# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x