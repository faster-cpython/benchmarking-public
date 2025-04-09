# Results vs. base

- fork: brandtbucher
- ref: jit_peephole
- machine: linux-x86_64
- commit hash: edb68e1
- commit date: 2025-04-08
- overall geometric mean: 1.002x faster
- HPT reliability: 93.67%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250408-linux-x86_64-python-8421b648e91981e393a7-3.14.0a7+-8421b64 | bm-20250408-linux-x86_64-brandtbucher-jit_peephole-3.14.0a7+-edb68e1 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 256 ms                                                                 | 254 ms: 1.01x faster                                                 |
| docutils       | 2.65 sec                                                               | 2.66 sec: 1.00x slower                                               |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20250408-linux-x86_64-python-8421b648e91981e393a7-3.14.0a7+-8421b64 | bm-20250408-linux-x86_64-brandtbucher-jit_peephole-3.14.0a7+-edb68e1 |
|-------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 491 ms                                                                 | 495 ms: 1.01x slower                                                 |
| async_generators        | 412 ms                                                                 | 418 ms: 1.01x slower                                                 |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (9): async_tree_memoization_tg, async_tree_none_tg, coroutines, async_tree_io, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_memoization, async_tree_io_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250408-linux-x86_64-python-8421b648e91981e393a7-3.14.0a7+-8421b64 | bm-20250408-linux-x86_64-brandtbucher-jit_peephole-3.14.0a7+-edb68e1 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 89.5 ms                                                                | 88.4 ms: 1.01x faster                                                |
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x slower                                                 |
| float          | 67.8 ms                                                                | 68.8 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                         |

Benchmarks with tag 'regex':
============================

Benchmark hidden because not significant (4): regex_v8, regex_effbot, regex_compile, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250408-linux-x86_64-python-8421b648e91981e393a7-3.14.0a7+-8421b64 | bm-20250408-linux-x86_64-brandtbucher-jit_peephole-3.14.0a7+-edb68e1 |
|---------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| json_dumps          | 11.7 ms                                                                | 11.5 ms: 1.02x faster                                                |
| json_loads          | 29.6 us                                                                | 29.4 us: 1.01x faster                                                |
| xml_etree_iterparse | 97.4 ms                                                                | 97.1 ms: 1.00x faster                                                |
| xml_etree_generate  | 80.0 ms                                                                | 81.0 ms: 1.01x slower                                                |
| Geometric mean      | (ref)                                                                  | 1.00x faster                                                         |

Benchmark hidden because not significant (5): unpickle_pure_python, xml_etree_parse, tomli_loads, xml_etree_process, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250408-linux-x86_64-python-8421b648e91981e393a7-3.14.0a7+-8421b64 | bm-20250408-linux-x86_64-brandtbucher-jit_peephole-3.14.0a7+-edb68e1 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                                | 13.1 ms: 1.00x faster                                                |
| python_startup_no_site | 8.20 ms                                                                | 8.18 ms: 1.00x faster                                                |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250408-linux-x86_64-python-8421b648e91981e393a7-3.14.0a7+-8421b64 | bm-20250408-linux-x86_64-brandtbucher-jit_peephole-3.14.0a7+-edb68e1 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_text     | 21.4 ms                                                                | 20.7 ms: 1.03x faster                                                |
| genshi_xml      | 49.8 ms                                                                | 49.0 ms: 1.02x faster                                                |
| mako            | 10.8 ms                                                                | 10.8 ms: 1.00x faster                                                |
| django_template | 31.3 ms                                                                | 32.2 ms: 1.03x slower                                                |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                         |

All benchmarks:
===============

| Benchmark               | bm-20250408-linux-x86_64-python-8421b648e91981e393a7-3.14.0a7+-8421b64 | bm-20250408-linux-x86_64-brandtbucher-jit_peephole-3.14.0a7+-edb68e1 |
|-------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| pyflate                 | 451 ms                                                                 | 422 ms: 1.07x faster                                                 |
| genshi_text             | 21.4 ms                                                                | 20.7 ms: 1.03x faster                                                |
| scimark_sor             | 119 ms                                                                 | 115 ms: 1.03x faster                                                 |
| scimark_sparse_mat_mult | 4.64 ms                                                                | 4.51 ms: 1.03x faster                                                |
| spectral_norm           | 102 ms                                                                 | 98.8 ms: 1.03x faster                                                |
| go                      | 123 ms                                                                 | 120 ms: 1.03x faster                                                 |
| scimark_fft             | 309 ms                                                                 | 303 ms: 1.02x faster                                                 |
| json_dumps              | 11.7 ms                                                                | 11.5 ms: 1.02x faster                                                |
| genshi_xml              | 49.8 ms                                                                | 49.0 ms: 1.02x faster                                                |
| json                    | 5.38 ms                                                                | 5.29 ms: 1.02x faster                                                |
| sqlalchemy_imperative   | 17.4 ms                                                                | 17.1 ms: 1.02x faster                                                |
| sympy_str               | 272 ms                                                                 | 268 ms: 1.01x faster                                                 |
| nbody                   | 89.5 ms                                                                | 88.4 ms: 1.01x faster                                                |
| sqlglot_v2_optimize     | 53.2 ms                                                                | 52.7 ms: 1.01x faster                                                |
| crypto_pyaes            | 74.9 ms                                                                | 74.1 ms: 1.01x faster                                                |
| sympy_sum               | 150 ms                                                                 | 149 ms: 1.01x faster                                                 |
| sympy_expand            | 470 ms                                                                 | 466 ms: 1.01x faster                                                 |
| deepcopy_memo           | 29.0 us                                                                | 28.7 us: 1.01x faster                                                |
| sqlglot_v2_parse        | 1.24 ms                                                                | 1.23 ms: 1.01x faster                                                |
| raytrace                | 262 ms                                                                 | 260 ms: 1.01x faster                                                 |
| json_loads              | 29.6 us                                                                | 29.4 us: 1.01x faster                                                |
| 2to3                    | 256 ms                                                                 | 254 ms: 1.01x faster                                                 |
| many_optionals          | 945 us                                                                 | 941 us: 1.00x faster                                                 |
| python_startup          | 13.2 ms                                                                | 13.1 ms: 1.00x faster                                                |
| bench_mp_pool           | 82.4 ms                                                                | 82.0 ms: 1.00x faster                                                |
| bpe_tokeniser           | 4.50 sec                                                               | 4.48 sec: 1.00x faster                                               |
| mako                    | 10.8 ms                                                                | 10.8 ms: 1.00x faster                                                |
| shortest_path           | 490 ms                                                                 | 489 ms: 1.00x faster                                                 |
| python_startup_no_site  | 8.20 ms                                                                | 8.18 ms: 1.00x faster                                                |
| sympy_integrate         | 19.4 ms                                                                | 19.4 ms: 1.00x faster                                                |
| xml_etree_iterparse     | 97.4 ms                                                                | 97.1 ms: 1.00x faster                                                |
| pidigits                | 186 ms                                                                 | 186 ms: 1.00x slower                                                 |
| bench_thread_pool       | 890 us                                                                 | 892 us: 1.00x slower                                                 |
| create_gc_cycles        | 2.45 ms                                                                | 2.46 ms: 1.00x slower                                                |
| connected_components    | 451 ms                                                                 | 452 ms: 1.00x slower                                                 |
| chaos                   | 56.1 ms                                                                | 56.4 ms: 1.00x slower                                                |
| docutils                | 2.65 sec                                                               | 2.66 sec: 1.00x slower                                               |
| generators              | 28.9 ms                                                                | 29.0 ms: 1.00x slower                                                |
| dulwich_log             | 60.4 ms                                                                | 60.7 ms: 1.00x slower                                                |
| deepcopy                | 249 us                                                                 | 251 us: 1.01x slower                                                 |
| async_tree_cpu_io_mixed | 491 ms                                                                 | 495 ms: 1.01x slower                                                 |
| comprehensions          | 18.3 us                                                                | 18.5 us: 1.01x slower                                                |
| meteor_contest          | 108 ms                                                                 | 109 ms: 1.01x slower                                                 |
| telco                   | 7.59 ms                                                                | 7.68 ms: 1.01x slower                                                |
| xml_etree_generate      | 80.0 ms                                                                | 81.0 ms: 1.01x slower                                                |
| float                   | 67.8 ms                                                                | 68.8 ms: 1.01x slower                                                |
| async_generators        | 412 ms                                                                 | 418 ms: 1.01x slower                                                 |
| pathlib                 | 16.7 ms                                                                | 16.9 ms: 1.01x slower                                                |
| pprint_pformat          | 1.49 sec                                                               | 1.52 sec: 1.02x slower                                               |
| logging_silent          | 96.3 ns                                                                | 98.2 ns: 1.02x slower                                                |
| django_template         | 31.3 ms                                                                | 32.2 ms: 1.03x slower                                                |
| gc_traversal            | 4.60 ms                                                                | 5.05 ms: 1.10x slower                                                |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                         |

Benchmark hidden because not significant (43): unpickle_pure_python, richards, async_tree_memoization_tg, pprint_safe_repr, async_tree_none_tg, deltablue, fannkuch, regex_v8, sqlite_synth, subparsers, xml_etree_parse, sqlglot_v2_normalize, typing_runtime_protocols, regex_effbot, regex_compile, sqlglot_v2_transpile, coroutines, pylint, async_tree_io, sqlalchemy_declarative, mdp, richards_super, coverage, hexiom, tomli_loads, regex_dna, sphinx, html5lib, logging_format, nqueens, async_tree_cpu_io_mixed_tg, deepcopy_reduce, asyncio_websockets, async_tree_memoization, xml_etree_process, scimark_lu, pycparser, async_tree_io_tg, logging_simple, pickle_pure_python, scimark_monte_carlo, k_core, async_tree_none

- Geometric mean (including insignificant results): 1.002x faster

# HPT report

- Reliability score: 93.67% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x