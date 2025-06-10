# Results vs. base

- fork: brandtbucher
- ref: keep_tracing
- machine: linux-x86_64
- commit hash: 8746972
- commit date: 2025-06-09
- overall geometric mean: 1.006x slower
- HPT reliability: 99.95%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250610-linux-x86_64-python-49fc1f215aeb0f714455-3.15.0a0-49fc1f2 | bm-20250609-linux-x86_64-brandtbucher-keep_tracing-3.15.0a0-8746972 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 260 ms                                                                | 262 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                        |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250610-linux-x86_64-python-49fc1f215aeb0f714455-3.15.0a0-49fc1f2 | bm-20250609-linux-x86_64-brandtbucher-keep_tracing-3.15.0a0-8746972 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_generators           | 433 ms                                                                | 424 ms: 1.02x faster                                                |
| async_tree_io_tg           | 629 ms                                                                | 616 ms: 1.02x faster                                                |
| coroutines                 | 25.6 ms                                                               | 25.2 ms: 1.02x faster                                               |
| async_tree_cpu_io_mixed_tg | 491 ms                                                                | 498 ms: 1.01x slower                                                |
| async_tree_cpu_io_mixed    | 499 ms                                                                | 506 ms: 1.01x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                        |

Benchmark hidden because not significant (6): async_tree_none_tg, asyncio_websockets, async_tree_none, async_tree_io, async_tree_memoization, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250610-linux-x86_64-python-49fc1f215aeb0f714455-3.15.0a0-49fc1f2 | bm-20250609-linux-x86_64-brandtbucher-keep_tracing-3.15.0a0-8746972 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 92.8 ms                                                               | 90.4 ms: 1.03x faster                                               |
| pidigits       | 187 ms                                                                | 191 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                        |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250610-linux-x86_64-python-49fc1f215aeb0f714455-3.15.0a0-49fc1f2 | bm-20250609-linux-x86_64-brandtbucher-keep_tracing-3.15.0a0-8746972 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 128 ms                                                                | 129 ms: 1.01x slower                                                |
| regex_v8       | 22.5 ms                                                               | 22.8 ms: 1.02x slower                                               |
| regex_effbot   | 3.39 ms                                                               | 3.49 ms: 1.03x slower                                               |
| regex_dna      | 201 ms                                                                | 219 ms: 1.09x slower                                                |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250610-linux-x86_64-python-49fc1f215aeb0f714455-3.15.0a0-49fc1f2 | bm-20250609-linux-x86_64-brandtbucher-keep_tracing-3.15.0a0-8746972 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_pure_python | 201 us                                                                | 205 us: 1.02x slower                                                |
| xml_etree_parse      | 142 ms                                                                | 145 ms: 1.02x slower                                                |
| json_dumps           | 11.0 ms                                                               | 11.2 ms: 1.02x slower                                               |
| pickle_pure_python   | 322 us                                                                | 330 us: 1.02x slower                                                |
| xml_etree_iterparse  | 98.1 ms                                                               | 101 ms: 1.03x slower                                                |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                        |

Benchmark hidden because not significant (4): xml_etree_generate, tomli_loads, json_loads, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250610-linux-x86_64-python-49fc1f215aeb0f714455-3.15.0a0-49fc1f2 | bm-20250609-linux-x86_64-brandtbucher-keep_tracing-3.15.0a0-8746972 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.91 ms                                                               | 6.94 ms: 1.00x slower                                               |
| python_startup         | 12.1 ms                                                               | 12.2 ms: 1.00x slower                                               |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250610-linux-x86_64-python-49fc1f215aeb0f714455-3.15.0a0-49fc1f2 | bm-20250609-linux-x86_64-brandtbucher-keep_tracing-3.15.0a0-8746972 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 10.7 ms                                                               | 10.8 ms: 1.01x slower                                               |
| django_template | 32.2 ms                                                               | 32.8 ms: 1.02x slower                                               |
| genshi_xml      | 49.9 ms                                                               | 51.1 ms: 1.02x slower                                               |
| genshi_text     | 21.2 ms                                                               | 22.0 ms: 1.04x slower                                               |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20250610-linux-x86_64-python-49fc1f215aeb0f714455-3.15.0a0-49fc1f2 | bm-20250609-linux-x86_64-brandtbucher-keep_tracing-3.15.0a0-8746972 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| generators                 | 30.6 ms                                                               | 29.7 ms: 1.03x faster                                               |
| scimark_sparse_mat_mult    | 5.05 ms                                                               | 4.91 ms: 1.03x faster                                               |
| pprint_pformat             | 1.71 sec                                                              | 1.66 sec: 1.03x faster                                              |
| nqueens                    | 85.2 ms                                                               | 83.0 ms: 1.03x faster                                               |
| nbody                      | 92.8 ms                                                               | 90.4 ms: 1.03x faster                                               |
| logging_simple             | 6.24 us                                                               | 6.09 us: 1.02x faster                                               |
| json                       | 5.26 ms                                                               | 5.14 ms: 1.02x faster                                               |
| comprehensions             | 17.2 us                                                               | 16.8 us: 1.02x faster                                               |
| coverage                   | 437 ms                                                                | 428 ms: 1.02x faster                                                |
| async_generators           | 433 ms                                                                | 424 ms: 1.02x faster                                                |
| async_tree_io_tg           | 629 ms                                                                | 616 ms: 1.02x faster                                                |
| scimark_lu                 | 119 ms                                                                | 117 ms: 1.02x faster                                                |
| coroutines                 | 25.6 ms                                                               | 25.2 ms: 1.02x faster                                               |
| sqlglot_v2_parse           | 1.28 ms                                                               | 1.26 ms: 1.02x faster                                               |
| scimark_monte_carlo        | 68.9 ms                                                               | 67.8 ms: 1.02x faster                                               |
| sqlite_synth               | 2.85 us                                                               | 2.81 us: 1.01x faster                                               |
| logging_format             | 6.88 us                                                               | 6.79 us: 1.01x faster                                               |
| scimark_sor                | 124 ms                                                                | 123 ms: 1.01x faster                                                |
| raytrace                   | 279 ms                                                                | 278 ms: 1.00x faster                                                |
| dulwich_log                | 61.5 ms                                                               | 61.7 ms: 1.00x slower                                               |
| create_gc_cycles           | 2.59 ms                                                               | 2.60 ms: 1.00x slower                                               |
| deepcopy_memo              | 29.7 us                                                               | 29.8 us: 1.00x slower                                               |
| python_startup_no_site     | 6.91 ms                                                               | 6.94 ms: 1.00x slower                                               |
| chaos                      | 62.6 ms                                                               | 62.9 ms: 1.00x slower                                               |
| python_startup             | 12.1 ms                                                               | 12.2 ms: 1.00x slower                                               |
| regex_compile              | 128 ms                                                                | 129 ms: 1.01x slower                                                |
| 2to3                       | 260 ms                                                                | 262 ms: 1.01x slower                                                |
| mako                       | 10.7 ms                                                               | 10.8 ms: 1.01x slower                                               |
| deepcopy                   | 260 us                                                                | 262 us: 1.01x slower                                                |
| sympy_integrate            | 19.4 ms                                                               | 19.6 ms: 1.01x slower                                               |
| sympy_sum                  | 151 ms                                                                | 152 ms: 1.01x slower                                                |
| scimark_fft                | 336 ms                                                                | 339 ms: 1.01x slower                                                |
| bpe_tokeniser              | 4.44 sec                                                              | 4.49 sec: 1.01x slower                                              |
| mdp                        | 1.25 sec                                                              | 1.26 sec: 1.01x slower                                              |
| async_tree_cpu_io_mixed_tg | 491 ms                                                                | 498 ms: 1.01x slower                                                |
| crypto_pyaes               | 75.6 ms                                                               | 76.7 ms: 1.01x slower                                               |
| async_tree_cpu_io_mixed    | 499 ms                                                                | 506 ms: 1.01x slower                                                |
| fannkuch                   | 412 ms                                                                | 418 ms: 1.02x slower                                                |
| shortest_path              | 492 ms                                                                | 500 ms: 1.02x slower                                                |
| regex_v8                   | 22.5 ms                                                               | 22.8 ms: 1.02x slower                                               |
| django_template            | 32.2 ms                                                               | 32.8 ms: 1.02x slower                                               |
| unpickle_pure_python       | 201 us                                                                | 205 us: 1.02x slower                                                |
| gc_traversal               | 5.08 ms                                                               | 5.18 ms: 1.02x slower                                               |
| xml_etree_parse            | 142 ms                                                                | 145 ms: 1.02x slower                                                |
| json_dumps                 | 11.0 ms                                                               | 11.2 ms: 1.02x slower                                               |
| spectral_norm              | 103 ms                                                                | 106 ms: 1.02x slower                                                |
| pickle_pure_python         | 322 us                                                                | 330 us: 1.02x slower                                                |
| pidigits                   | 187 ms                                                                | 191 ms: 1.02x slower                                                |
| logging_silent             | 476 ns                                                                | 487 ns: 1.02x slower                                                |
| meteor_contest             | 106 ms                                                                | 108 ms: 1.02x slower                                                |
| genshi_xml                 | 49.9 ms                                                               | 51.1 ms: 1.02x slower                                               |
| xml_etree_iterparse        | 98.1 ms                                                               | 101 ms: 1.03x slower                                                |
| pyflate                    | 414 ms                                                                | 425 ms: 1.03x slower                                                |
| hexiom                     | 6.55 ms                                                               | 6.74 ms: 1.03x slower                                               |
| regex_effbot               | 3.39 ms                                                               | 3.49 ms: 1.03x slower                                               |
| genshi_text                | 21.2 ms                                                               | 22.0 ms: 1.04x slower                                               |
| pprint_safe_repr           | 801 ms                                                                | 831 ms: 1.04x slower                                                |
| pycparser                  | 1.13 sec                                                              | 1.18 sec: 1.05x slower                                              |
| telco                      | 7.68 ms                                                               | 8.07 ms: 1.05x slower                                               |
| deepcopy_reduce            | 2.69 us                                                               | 2.82 us: 1.05x slower                                               |
| richards_super             | 39.9 ms                                                               | 42.4 ms: 1.06x slower                                               |
| richards                   | 34.4 ms                                                               | 37.0 ms: 1.08x slower                                               |
| regex_dna                  | 201 ms                                                                | 219 ms: 1.09x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.01x slower                                                        |

Benchmark hidden because not significant (29): async_tree_none_tg, pathlib, deltablue, subparsers, sqlglot_v2_transpile, float, xml_etree_generate, docutils, thrift, asyncio_websockets, async_tree_none, connected_components, tomli_loads, k_core, async_tree_io, async_tree_memoization, many_optionals, async_tree_memoization_tg, sympy_str, sympy_expand, sqlglot_v2_normalize, sqlglot_v2_optimize, go, sphinx, json_loads, xml_etree_process, pylint, html5lib, typing_runtime_protocols

- Geometric mean (including insignificant results): 1.006x slower

# HPT report

- Reliability score: 99.95% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x