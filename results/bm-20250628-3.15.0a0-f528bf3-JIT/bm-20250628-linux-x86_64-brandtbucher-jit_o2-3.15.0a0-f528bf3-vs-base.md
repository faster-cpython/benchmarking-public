# Results vs. base

- fork: brandtbucher
- ref: jit_o2
- machine: linux-x86_64
- commit hash: f528bf3
- commit date: 2025-06-28
- overall geometric mean: 1.003x slower
- HPT reliability: 99.25%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-linux-x86_64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 258 ms                                                                | 260 ms: 1.01x slower                                          |
| html5lib       | 61.0 ms                                                               | 61.7 ms: 1.01x slower                                         |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                  |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-linux-x86_64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| async_generators       | 435 ms                                                                | 428 ms: 1.02x faster                                          |
| async_tree_memoization | 311 ms                                                                | 313 ms: 1.01x slower                                          |
| coroutines             | 25.0 ms                                                               | 25.3 ms: 1.01x slower                                         |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                  |

Benchmark hidden because not significant (8): async_tree_io_tg, async_tree_io, async_tree_none_tg, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-linux-x86_64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 66.0 ms                                                               | 65.7 ms: 1.00x faster                                         |
| pidigits       | 188 ms                                                                | 188 ms: 1.00x slower                                          |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                  |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-linux-x86_64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_dna      | 206 ms                                                                | 207 ms: 1.01x slower                                          |
| regex_compile  | 126 ms                                                                | 127 ms: 1.01x slower                                          |
| regex_effbot   | 3.24 ms                                                               | 3.28 ms: 1.01x slower                                         |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                  |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-linux-x86_64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| json_loads           | 28.7 us                                                               | 28.2 us: 1.02x faster                                         |
| tomli_loads          | 1.84 sec                                                              | 1.82 sec: 1.01x faster                                        |
| unpickle_pure_python | 194 us                                                                | 195 us: 1.00x slower                                          |
| xml_etree_process    | 55.2 ms                                                               | 55.5 ms: 1.00x slower                                         |
| xml_etree_iterparse  | 98.2 ms                                                               | 99.0 ms: 1.01x slower                                         |
| xml_etree_generate   | 79.6 ms                                                               | 80.4 ms: 1.01x slower                                         |
| pickle_pure_python   | 319 us                                                                | 324 us: 1.01x slower                                          |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                  |

Benchmark hidden because not significant (2): json_dumps, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-linux-x86_64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup_no_site | 6.95 ms                                                               | 6.96 ms: 1.00x slower                                         |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                  |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-linux-x86_64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| mako            | 10.6 ms                                                               | 10.6 ms: 1.00x slower                                         |
| genshi_text     | 21.4 ms                                                               | 21.6 ms: 1.01x slower                                         |
| django_template | 32.4 ms                                                               | 32.6 ms: 1.01x slower                                         |
| Geometric mean  | (ref)                                                                 | 1.00x slower                                                  |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 | bm-20250628-linux-x86_64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|-------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| pprint_pformat          | 1.49 sec                                                              | 1.43 sec: 1.05x faster                                        |
| deepcopy_memo           | 29.8 us                                                               | 29.1 us: 1.02x faster                                         |
| thrift                  | 785 us                                                                | 769 us: 1.02x faster                                          |
| pprint_safe_repr        | 724 ms                                                                | 709 ms: 1.02x faster                                          |
| async_generators        | 435 ms                                                                | 428 ms: 1.02x faster                                          |
| json_loads              | 28.7 us                                                               | 28.2 us: 1.02x faster                                         |
| comprehensions          | 16.6 us                                                               | 16.4 us: 1.01x faster                                         |
| crypto_pyaes            | 74.8 ms                                                               | 74.0 ms: 1.01x faster                                         |
| tomli_loads             | 1.84 sec                                                              | 1.82 sec: 1.01x faster                                        |
| pathlib                 | 17.3 ms                                                               | 17.1 ms: 1.01x faster                                         |
| scimark_lu              | 118 ms                                                                | 117 ms: 1.01x faster                                          |
| nqueens                 | 82.4 ms                                                               | 81.9 ms: 1.01x faster                                         |
| sqlite_synth            | 2.79 us                                                               | 2.78 us: 1.00x faster                                         |
| float                   | 66.0 ms                                                               | 65.7 ms: 1.00x faster                                         |
| bpe_tokeniser           | 4.34 sec                                                              | 4.33 sec: 1.00x faster                                        |
| sympy_integrate         | 19.3 ms                                                               | 19.3 ms: 1.00x faster                                         |
| pidigits                | 188 ms                                                                | 188 ms: 1.00x slower                                          |
| python_startup_no_site  | 6.95 ms                                                               | 6.96 ms: 1.00x slower                                         |
| mako                    | 10.6 ms                                                               | 10.6 ms: 1.00x slower                                         |
| coverage                | 87.9 ms                                                               | 88.2 ms: 1.00x slower                                         |
| unpickle_pure_python    | 194 us                                                                | 195 us: 1.00x slower                                          |
| shortest_path           | 502 ms                                                                | 504 ms: 1.00x slower                                          |
| xml_etree_process       | 55.2 ms                                                               | 55.5 ms: 1.00x slower                                         |
| sympy_sum               | 149 ms                                                                | 150 ms: 1.01x slower                                          |
| async_tree_memoization  | 311 ms                                                                | 313 ms: 1.01x slower                                          |
| 2to3                    | 258 ms                                                                | 260 ms: 1.01x slower                                          |
| deltablue               | 3.03 ms                                                               | 3.05 ms: 1.01x slower                                         |
| go                      | 116 ms                                                                | 117 ms: 1.01x slower                                          |
| regex_dna               | 206 ms                                                                | 207 ms: 1.01x slower                                          |
| xml_etree_iterparse     | 98.2 ms                                                               | 99.0 ms: 1.01x slower                                         |
| scimark_fft             | 311 ms                                                                | 313 ms: 1.01x slower                                          |
| create_gc_cycles        | 2.57 ms                                                               | 2.59 ms: 1.01x slower                                         |
| genshi_text             | 21.4 ms                                                               | 21.6 ms: 1.01x slower                                         |
| django_template         | 32.4 ms                                                               | 32.6 ms: 1.01x slower                                         |
| xml_etree_generate      | 79.6 ms                                                               | 80.4 ms: 1.01x slower                                         |
| json                    | 5.23 ms                                                               | 5.28 ms: 1.01x slower                                         |
| logging_simple          | 5.52 us                                                               | 5.58 us: 1.01x slower                                         |
| html5lib                | 61.0 ms                                                               | 61.7 ms: 1.01x slower                                         |
| regex_compile           | 126 ms                                                                | 127 ms: 1.01x slower                                          |
| pyflate                 | 420 ms                                                                | 425 ms: 1.01x slower                                          |
| regex_effbot            | 3.24 ms                                                               | 3.28 ms: 1.01x slower                                         |
| sqlglot_v2_transpile    | 1.55 ms                                                               | 1.57 ms: 1.01x slower                                         |
| coroutines              | 25.0 ms                                                               | 25.3 ms: 1.01x slower                                         |
| pickle_pure_python      | 319 us                                                                | 324 us: 1.01x slower                                          |
| raytrace                | 271 ms                                                                | 275 ms: 1.02x slower                                          |
| spectral_norm           | 92.3 ms                                                               | 93.9 ms: 1.02x slower                                         |
| hexiom                  | 6.16 ms                                                               | 6.27 ms: 1.02x slower                                         |
| pycparser               | 1.15 sec                                                              | 1.17 sec: 1.02x slower                                        |
| sqlglot_v2_parse        | 1.23 ms                                                               | 1.25 ms: 1.02x slower                                         |
| meteor_contest          | 106 ms                                                                | 107 ms: 1.02x slower                                          |
| generators              | 30.0 ms                                                               | 30.5 ms: 1.02x slower                                         |
| richards                | 32.2 ms                                                               | 32.8 ms: 1.02x slower                                         |
| scimark_sparse_mat_mult | 4.86 ms                                                               | 4.97 ms: 1.02x slower                                         |
| scimark_monte_carlo     | 65.0 ms                                                               | 66.7 ms: 1.02x slower                                         |
| logging_format          | 6.15 us                                                               | 6.33 us: 1.03x slower                                         |
| logging_silent          | 101 ns                                                                | 104 ns: 1.04x slower                                          |
| gc_traversal            | 4.72 ms                                                               | 5.16 ms: 1.09x slower                                         |
| Geometric mean          | (ref)                                                                 | 1.00x slower                                                  |

Benchmark hidden because not significant (36): nbody, genshi_xml, typing_runtime_protocols, sqlglot_v2_normalize, async_tree_io_tg, k_core, connected_components, many_optionals, sympy_expand, async_tree_io, sqlglot_v2_optimize, async_tree_none_tg, json_dumps, async_tree_cpu_io_mixed, scimark_sor, xml_etree_parse, python_startup, docutils, asyncio_websockets, fannkuch, subparsers, deepcopy, regex_v8, mdp, dulwich_log, sympy_str, deepcopy_reduce, telco, chaos, async_tree_cpu_io_mixed_tg, pylint, async_tree_none, sphinx, async_tree_memoization_tg, richards_super, djangocms

- Geometric mean (including insignificant results): 1.003x slower

# HPT report

- Reliability score: 99.25% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x