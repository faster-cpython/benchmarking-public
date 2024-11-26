# Results vs. base

- fork: brandtbucher
- ref: 6de23b358e9e3dd796a2
- machine: linux-x86_64
- commit hash: 6de23b3
- commit date: 2024-11-14
- overall geometric mean: 1.111x slower
- HPT reliability: 99.80%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-linux-x86_64-brandtbucher-6de23b358e9e3dd796a2-3.14.0a1+-6de23b3 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                                 | 1.29 sec: 4.59x slower                                                       |
| docutils       | 2.95 sec                                                               | 6.92 sec: 2.35x slower                                                       |
| sphinx         | 1.18 sec                                                               | 3.01 sec: 2.55x slower                                                       |
| Geometric mean | (ref)                                                                  | 2.29x slower                                                                 |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-linux-x86_64-brandtbucher-6de23b358e9e3dd796a2-3.14.0a1+-6de23b3 |
|------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| coroutines       | 23.2 ms                                                                | 22.9 ms: 1.02x faster                                                        |
| async_generators | 456 ms                                                                 | 459 ms: 1.01x slower                                                         |
| async_tree_none  | 332 ms                                                                 | 335 ms: 1.01x slower                                                         |
| Geometric mean   | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (8): async_tree_memoization, async_tree_io_tg, async_tree_memoization_tg, asyncio_websockets, async_tree_none_tg, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-linux-x86_64-brandtbucher-6de23b358e9e3dd796a2-3.14.0a1+-6de23b3 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 187 ms                                                                 | 187 ms: 1.00x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (2): nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-linux-x86_64-brandtbucher-6de23b358e9e3dd796a2-3.14.0a1+-6de23b3 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                                | 3.70 ms: 1.02x faster                                                        |
| regex_dna      | 216 ms                                                                 | 218 ms: 1.01x slower                                                         |
| regex_compile  | 140 ms                                                                 | 226 ms: 1.61x slower                                                         |
| regex_v8       | 24.6 ms                                                                | 48.9 ms: 1.99x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.33x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-linux-x86_64-brandtbucher-6de23b358e9e3dd796a2-3.14.0a1+-6de23b3 |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.00 sec                                                               | 1.95 sec: 1.02x faster                                                       |
| xml_etree_generate   | 79.6 ms                                                                | 79.0 ms: 1.01x faster                                                        |
| unpickle_pure_python | 219 us                                                                 | 222 us: 1.01x slower                                                         |
| xml_etree_iterparse  | 101 ms                                                                 | 103 ms: 1.03x slower                                                         |
| xml_etree_process    | 56.0 ms                                                                | 57.9 ms: 1.03x slower                                                        |
| json_dumps           | 11.1 ms                                                                | 13.5 ms: 1.22x slower                                                        |
| json_loads           | 26.8 us                                                                | 34.0 us: 1.27x slower                                                        |
| pickle_pure_python   | 321 us                                                                 | 623 us: 1.94x slower                                                         |
| Geometric mean       | (ref)                                                                  | 1.13x slower                                                                 |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-linux-x86_64-brandtbucher-6de23b358e9e3dd796a2-3.14.0a1+-6de23b3 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 12.8 ms                                                                | 12.9 ms: 1.00x slower                                                        |
| python_startup_no_site | 7.14 ms                                                                | 7.16 ms: 1.00x slower                                                        |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-linux-x86_64-brandtbucher-6de23b358e9e3dd796a2-3.14.0a1+-6de23b3 |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 10.3 ms                                                                | 10.0 ms: 1.02x faster                                                        |
| django_template | 34.3 ms                                                                | 33.8 ms: 1.01x faster                                                        |
| genshi_xml      | 59.9 ms                                                                | 61.8 ms: 1.03x slower                                                        |
| genshi_text     | 25.1 ms                                                                | 26.6 ms: 1.06x slower                                                        |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-linux-x86_64-brandtbucher-6de23b358e9e3dd796a2-3.14.0a1+-6de23b3 |
|-------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| gc_traversal            | 4.74 ms                                                                | 4.57 ms: 1.04x faster                                                        |
| scimark_sparse_mat_mult | 4.62 ms                                                                | 4.47 ms: 1.03x faster                                                        |
| richards_super          | 47.1 ms                                                                | 45.7 ms: 1.03x faster                                                        |
| logging_silent          | 102 ns                                                                 | 99.1 ns: 1.03x faster                                                        |
| raytrace                | 283 ms                                                                 | 276 ms: 1.02x faster                                                         |
| tomli_loads             | 2.00 sec                                                               | 1.95 sec: 1.02x faster                                                       |
| mako                    | 10.3 ms                                                                | 10.0 ms: 1.02x faster                                                        |
| regex_effbot            | 3.77 ms                                                                | 3.70 ms: 1.02x faster                                                        |
| fannkuch                | 389 ms                                                                 | 382 ms: 1.02x faster                                                         |
| pprint_pformat          | 1.51 sec                                                               | 1.49 sec: 1.02x faster                                                       |
| pprint_safe_repr        | 724 ms                                                                 | 711 ms: 1.02x faster                                                         |
| meteor_contest          | 109 ms                                                                 | 107 ms: 1.02x faster                                                         |
| coroutines              | 23.2 ms                                                                | 22.9 ms: 1.02x faster                                                        |
| generators              | 36.6 ms                                                                | 36.1 ms: 1.02x faster                                                        |
| django_template         | 34.3 ms                                                                | 33.8 ms: 1.01x faster                                                        |
| coverage                | 84.9 ms                                                                | 84.1 ms: 1.01x faster                                                        |
| comprehensions          | 17.5 us                                                                | 17.4 us: 1.01x faster                                                        |
| xml_etree_generate      | 79.6 ms                                                                | 79.0 ms: 1.01x faster                                                        |
| bpe_tokeniser           | 4.53 sec                                                               | 4.49 sec: 1.01x faster                                                       |
| scimark_monte_carlo     | 64.8 ms                                                                | 64.3 ms: 1.01x faster                                                        |
| shortest_path           | 482 ms                                                                 | 479 ms: 1.01x faster                                                         |
| scimark_sor             | 119 ms                                                                 | 118 ms: 1.01x faster                                                         |
| create_gc_cycles        | 2.71 ms                                                                | 2.70 ms: 1.00x faster                                                        |
| python_startup          | 12.8 ms                                                                | 12.9 ms: 1.00x slower                                                        |
| python_startup_no_site  | 7.14 ms                                                                | 7.16 ms: 1.00x slower                                                        |
| pidigits                | 187 ms                                                                 | 187 ms: 1.00x slower                                                         |
| mdp                     | 2.62 sec                                                               | 2.63 sec: 1.01x slower                                                       |
| sqlglot_transpile       | 1.69 ms                                                                | 1.70 ms: 1.01x slower                                                        |
| deepcopy_reduce         | 2.66 us                                                                | 2.68 us: 1.01x slower                                                        |
| regex_dna               | 216 ms                                                                 | 218 ms: 1.01x slower                                                         |
| async_generators        | 456 ms                                                                 | 459 ms: 1.01x slower                                                         |
| chaos                   | 59.1 ms                                                                | 59.7 ms: 1.01x slower                                                        |
| logging_simple          | 5.56 us                                                                | 5.61 us: 1.01x slower                                                        |
| async_tree_none         | 332 ms                                                                 | 335 ms: 1.01x slower                                                         |
| deepcopy_memo           | 29.6 us                                                                | 30.0 us: 1.01x slower                                                        |
| unpickle_pure_python    | 219 us                                                                 | 222 us: 1.01x slower                                                         |
| pathlib                 | 16.1 ms                                                                | 16.3 ms: 1.01x slower                                                        |
| crypto_pyaes            | 68.5 ms                                                                | 69.4 ms: 1.01x slower                                                        |
| deepcopy                | 267 us                                                                 | 271 us: 1.01x slower                                                         |
| nqueens                 | 87.9 ms                                                                | 89.2 ms: 1.01x slower                                                        |
| go                      | 133 ms                                                                 | 136 ms: 1.02x slower                                                         |
| xml_etree_iterparse     | 101 ms                                                                 | 103 ms: 1.03x slower                                                         |
| djangocms               | 23.7 us                                                                | 24.5 us: 1.03x slower                                                        |
| genshi_xml              | 59.9 ms                                                                | 61.8 ms: 1.03x slower                                                        |
| xml_etree_process       | 56.0 ms                                                                | 57.9 ms: 1.03x slower                                                        |
| pycparser               | 1.16 sec                                                               | 1.21 sec: 1.04x slower                                                       |
| scimark_lu              | 113 ms                                                                 | 119 ms: 1.05x slower                                                         |
| genshi_text             | 25.1 ms                                                                | 26.6 ms: 1.06x slower                                                        |
| sympy_integrate         | 23.6 ms                                                                | 26.3 ms: 1.12x slower                                                        |
| pyflate                 | 449 ms                                                                 | 509 ms: 1.13x slower                                                         |
| sympy_expand            | 509 ms                                                                 | 599 ms: 1.18x slower                                                         |
| sqlite_synth            | 2.80 us                                                                | 3.37 us: 1.20x slower                                                        |
| json_dumps              | 11.1 ms                                                                | 13.5 ms: 1.22x slower                                                        |
| json                    | 4.98 ms                                                                | 6.16 ms: 1.24x slower                                                        |
| json_loads              | 26.8 us                                                                | 34.0 us: 1.27x slower                                                        |
| bench_mp_pool           | 84.8 ms                                                                | 108 ms: 1.27x slower                                                         |
| telco                   | 7.67 ms                                                                | 10.4 ms: 1.36x slower                                                        |
| thrift                  | 779 us                                                                 | 1.10 ms: 1.41x slower                                                        |
| dulwich_log             | 67.7 ms                                                                | 96.5 ms: 1.43x slower                                                        |
| sympy_str               | 305 ms                                                                 | 457 ms: 1.50x slower                                                         |
| regex_compile           | 140 ms                                                                 | 226 ms: 1.61x slower                                                         |
| sqlglot_normalize       | 114 ms                                                                 | 194 ms: 1.69x slower                                                         |
| sympy_sum               | 176 ms                                                                 | 317 ms: 1.80x slower                                                         |
| sqlalchemy_declarative  | 148 ms                                                                 | 284 ms: 1.93x slower                                                         |
| pickle_pure_python      | 321 us                                                                 | 623 us: 1.94x slower                                                         |
| regex_v8                | 24.6 ms                                                                | 48.9 ms: 1.99x slower                                                        |
| sqlglot_optimize        | 60.3 ms                                                                | 140 ms: 2.33x slower                                                         |
| docutils                | 2.95 sec                                                               | 6.92 sec: 2.35x slower                                                       |
| sphinx                  | 1.18 sec                                                               | 3.01 sec: 2.55x slower                                                       |
| 2to3                    | 280 ms                                                                 | 1.29 sec: 4.59x slower                                                       |
| pylint                  | 380 ms                                                                 | 2.03 sec: 5.34x slower                                                       |
| Geometric mean          | (ref)                                                                  | 1.14x slower                                                                 |

Benchmark hidden because not significant (24): k_core, typing_runtime_protocols, nbody, async_tree_memoization, scimark_fft, sqlglot_parse, spectral_norm, connected_components, async_tree_io_tg, async_tree_memoization_tg, bench_thread_pool, sqlalchemy_imperative, asyncio_websockets, xml_etree_parse, deltablue, hexiom, html5lib, float, async_tree_none_tg, async_tree_io, logging_format, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, richards
Ignored benchmarks (2) of results/bm-20241107-3.14.0a1+-09d6f5d-JIT/bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d.json: many_optionals, subparsers

- Geometric mean (including insignificant results): 1.111x slower
# HPT report

- Reliability score: 99.80% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.04x