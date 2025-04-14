# Results vs. base

- fork: iritkatriel
- ref: binary_subscr_to_op
- machine: linux-x86_64
- commit hash: c05e483
- commit date: 2025-02-05
- overall geometric mean: 1.002x slower
- HPT reliability: 97.05%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec | bm-20250205-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-c05e483 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 2.58 sec                                                               | 2.59 sec: 1.00x slower                                                     |
| html5lib       | 59.8 ms                                                                | 61.6 ms: 1.03x slower                                                      |
| sphinx         | 994 ms                                                                 | 1.01 sec: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                               |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec | bm-20250205-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-c05e483 |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 499 ms                                                                 | 488 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed_tg | 488 ms                                                                 | 481 ms: 1.02x faster                                                       |
| async_tree_memoization_tg  | 321 ms                                                                 | 316 ms: 1.02x faster                                                       |
| async_generators           | 383 ms                                                                 | 381 ms: 1.01x faster                                                       |
| coroutines                 | 23.3 ms                                                                | 23.5 ms: 1.01x slower                                                      |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (6): async_tree_none, async_tree_io, async_tree_memoization, async_tree_none_tg, asyncio_websockets, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec | bm-20250205-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-c05e483 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 70.5 ms                                                                | 68.8 ms: 1.03x faster                                                      |
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x faster                                                       |
| nbody          | 92.7 ms                                                                | 94.7 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec | bm-20250205-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-c05e483 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 126 ms                                                                 | 125 ms: 1.01x faster                                                       |
| regex_dna      | 210 ms                                                                 | 213 ms: 1.01x slower                                                       |
| regex_effbot   | 3.30 ms                                                                | 3.36 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec | bm-20250205-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-c05e483 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 317 us                                                                 | 312 us: 1.02x faster                                                       |
| json_dumps           | 11.9 ms                                                                | 11.8 ms: 1.01x faster                                                      |
| xml_etree_process    | 58.4 ms                                                                | 58.1 ms: 1.01x faster                                                      |
| xml_etree_generate   | 82.9 ms                                                                | 83.5 ms: 1.01x slower                                                      |
| unpickle_pure_python | 216 us                                                                 | 218 us: 1.01x slower                                                       |
| tomli_loads          | 1.94 sec                                                               | 1.96 sec: 1.01x slower                                                     |
| json_loads           | 28.5 us                                                                | 28.9 us: 1.01x slower                                                      |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec | bm-20250205-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-c05e483 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 7.05 ms                                                                | 7.10 ms: 1.01x slower                                                      |
| python_startup         | 12.8 ms                                                                | 13.0 ms: 1.01x slower                                                      |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec | bm-20250205-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-c05e483 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako           | 11.0 ms                                                                | 10.8 ms: 1.02x faster                                                      |
| genshi_xml     | 47.8 ms                                                                | 48.1 ms: 1.00x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec | bm-20250205-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-c05e483 |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| logging_silent             | 107 ns                                                                 | 103 ns: 1.04x faster                                                       |
| go                         | 119 ms                                                                 | 115 ms: 1.04x faster                                                       |
| sqlglot_parse              | 1.26 ms                                                                | 1.23 ms: 1.03x faster                                                      |
| float                      | 70.5 ms                                                                | 68.8 ms: 1.03x faster                                                      |
| logging_format             | 6.12 us                                                                | 5.98 us: 1.02x faster                                                      |
| async_tree_cpu_io_mixed    | 499 ms                                                                 | 488 ms: 1.02x faster                                                       |
| deltablue                  | 3.22 ms                                                                | 3.16 ms: 1.02x faster                                                      |
| mako                       | 11.0 ms                                                                | 10.8 ms: 1.02x faster                                                      |
| pathlib                    | 16.1 ms                                                                | 15.8 ms: 1.02x faster                                                      |
| richards_super             | 50.2 ms                                                                | 49.3 ms: 1.02x faster                                                      |
| pickle_pure_python         | 317 us                                                                 | 312 us: 1.02x faster                                                       |
| async_tree_cpu_io_mixed_tg | 488 ms                                                                 | 481 ms: 1.02x faster                                                       |
| scimark_sor                | 121 ms                                                                 | 119 ms: 1.02x faster                                                       |
| async_tree_memoization_tg  | 321 ms                                                                 | 316 ms: 1.02x faster                                                       |
| sqlglot_transpile          | 1.56 ms                                                                | 1.54 ms: 1.01x faster                                                      |
| json                       | 5.14 ms                                                                | 5.08 ms: 1.01x faster                                                      |
| richards                   | 43.8 ms                                                                | 43.4 ms: 1.01x faster                                                      |
| logging_simple             | 5.48 us                                                                | 5.42 us: 1.01x faster                                                      |
| regex_compile              | 126 ms                                                                 | 125 ms: 1.01x faster                                                       |
| thrift                     | 766 us                                                                 | 759 us: 1.01x faster                                                       |
| json_dumps                 | 11.9 ms                                                                | 11.8 ms: 1.01x faster                                                      |
| sympy_expand               | 454 ms                                                                 | 450 ms: 1.01x faster                                                       |
| async_generators           | 383 ms                                                                 | 381 ms: 1.01x faster                                                       |
| pprint_safe_repr           | 707 ms                                                                 | 703 ms: 1.01x faster                                                       |
| comprehensions             | 16.3 us                                                                | 16.2 us: 1.01x faster                                                      |
| xml_etree_process          | 58.4 ms                                                                | 58.1 ms: 1.01x faster                                                      |
| scimark_monte_carlo        | 67.4 ms                                                                | 67.1 ms: 1.01x faster                                                      |
| sqlglot_optimize           | 51.8 ms                                                                | 51.7 ms: 1.00x faster                                                      |
| create_gc_cycles           | 2.48 ms                                                                | 2.47 ms: 1.00x faster                                                      |
| pidigits                   | 186 ms                                                                 | 186 ms: 1.00x faster                                                       |
| gc_traversal               | 5.03 ms                                                                | 5.03 ms: 1.00x faster                                                      |
| docutils                   | 2.58 sec                                                               | 2.59 sec: 1.00x slower                                                     |
| nqueens                    | 79.6 ms                                                                | 79.9 ms: 1.00x slower                                                      |
| genshi_xml                 | 47.8 ms                                                                | 48.1 ms: 1.00x slower                                                      |
| deepcopy                   | 255 us                                                                 | 257 us: 1.01x slower                                                       |
| xml_etree_generate         | 82.9 ms                                                                | 83.5 ms: 1.01x slower                                                      |
| raytrace                   | 269 ms                                                                 | 271 ms: 1.01x slower                                                       |
| python_startup_no_site     | 7.05 ms                                                                | 7.10 ms: 1.01x slower                                                      |
| coroutines                 | 23.3 ms                                                                | 23.5 ms: 1.01x slower                                                      |
| sympy_str                  | 265 ms                                                                 | 267 ms: 1.01x slower                                                       |
| bench_thread_pool          | 864 us                                                                 | 872 us: 1.01x slower                                                       |
| hexiom                     | 6.27 ms                                                                | 6.33 ms: 1.01x slower                                                      |
| unpickle_pure_python       | 216 us                                                                 | 218 us: 1.01x slower                                                       |
| tomli_loads                | 1.94 sec                                                               | 1.96 sec: 1.01x slower                                                     |
| shortest_path              | 471 ms                                                                 | 476 ms: 1.01x slower                                                       |
| python_startup             | 12.8 ms                                                                | 13.0 ms: 1.01x slower                                                      |
| sphinx                     | 994 ms                                                                 | 1.01 sec: 1.01x slower                                                     |
| sqlalchemy_declarative     | 128 ms                                                                 | 130 ms: 1.01x slower                                                       |
| deepcopy_reduce            | 2.68 us                                                                | 2.71 us: 1.01x slower                                                      |
| scimark_lu                 | 115 ms                                                                 | 116 ms: 1.01x slower                                                       |
| connected_components       | 434 ms                                                                 | 439 ms: 1.01x slower                                                       |
| crypto_pyaes               | 70.2 ms                                                                | 71.1 ms: 1.01x slower                                                      |
| json_loads                 | 28.5 us                                                                | 28.9 us: 1.01x slower                                                      |
| regex_dna                  | 210 ms                                                                 | 213 ms: 1.01x slower                                                       |
| many_optionals             | 932 us                                                                 | 946 us: 1.02x slower                                                       |
| bench_mp_pool              | 81.0 ms                                                                | 82.3 ms: 1.02x slower                                                      |
| regex_effbot               | 3.30 ms                                                                | 3.36 ms: 1.02x slower                                                      |
| generators                 | 27.6 ms                                                                | 28.1 ms: 1.02x slower                                                      |
| chaos                      | 57.6 ms                                                                | 58.7 ms: 1.02x slower                                                      |
| sympy_integrate            | 19.5 ms                                                                | 19.9 ms: 1.02x slower                                                      |
| pyflate                    | 452 ms                                                                 | 460 ms: 1.02x slower                                                       |
| nbody                      | 92.7 ms                                                                | 94.7 ms: 1.02x slower                                                      |
| typing_runtime_protocols   | 157 us                                                                 | 161 us: 1.02x slower                                                       |
| fannkuch                   | 396 ms                                                                 | 407 ms: 1.03x slower                                                       |
| html5lib                   | 59.8 ms                                                                | 61.6 ms: 1.03x slower                                                      |
| sympy_sum                  | 147 ms                                                                 | 152 ms: 1.04x slower                                                       |
| dulwich_log                | 64.0 ms                                                                | 66.9 ms: 1.05x slower                                                      |
| sqlalchemy_imperative      | 16.4 ms                                                                | 17.3 ms: 1.05x slower                                                      |
| scimark_sparse_mat_mult    | 4.53 ms                                                                | 4.85 ms: 1.07x slower                                                      |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (27): async_tree_none, async_tree_io, telco, sqlite_synth, meteor_contest, regex_v8, async_tree_memoization, sqlglot_normalize, async_tree_none_tg, genshi_text, subparsers, coverage, asyncio_websockets, pprint_pformat, 2to3, scimark_fft, mdp, xml_etree_parse, django_template, bpe_tokeniser, spectral_norm, xml_etree_iterparse, deepcopy_memo, pylint, pycparser, async_tree_io_tg, k_core

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 97.05% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x