# Results vs. base

- fork: brandtbucher
- ref: jit_unknown_syms
- machine: linux-x86_64
- commit hash: 88219fd
- commit date: 2025-03-19
- overall geometric mean: 1.004x faster
- HPT reliability: 99.86%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250317-linux-x86_64-python-fd545d735d5f9c048f99-3.14.0a6+-fd545d7 | bm-20250319-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-88219fd |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 263 ms                                                                 | 262 ms: 1.00x faster                                                     |
| docutils       | 2.68 sec                                                               | 2.69 sec: 1.00x slower                                                   |
| html5lib       | 62.2 ms                                                                | 63.6 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                             |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250317-linux-x86_64-python-fd545d735d5f9c048f99-3.14.0a6+-fd545d7 | bm-20250319-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-88219fd |
|----------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 319 ms                                                                 | 315 ms: 1.01x faster                                                     |
| coroutines                 | 23.7 ms                                                                | 23.4 ms: 1.01x faster                                                    |
| async_tree_cpu_io_mixed_tg | 481 ms                                                                 | 478 ms: 1.01x faster                                                     |
| async_generators           | 417 ms                                                                 | 415 ms: 1.01x faster                                                     |
| async_tree_cpu_io_mixed    | 497 ms                                                                 | 494 ms: 1.01x faster                                                     |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (6): async_tree_memoization_tg, async_tree_io_tg, async_tree_none, async_tree_none_tg, async_tree_io, asyncio_websockets

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250317-linux-x86_64-python-fd545d735d5f9c048f99-3.14.0a6+-fd545d7 | bm-20250319-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-88219fd |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 23.9 ms                                                                | 23.3 ms: 1.02x faster                                                    |
| regex_dna      | 225 ms                                                                 | 221 ms: 1.02x faster                                                     |
| regex_effbot   | 3.48 ms                                                                | 3.53 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250317-linux-x86_64-python-fd545d735d5f9c048f99-3.14.0a6+-fd545d7 | bm-20250319-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-88219fd |
|---------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps          | 11.8 ms                                                                | 11.4 ms: 1.03x faster                                                    |
| pickle_pure_python  | 326 us                                                                 | 320 us: 1.02x faster                                                     |
| json_loads          | 30.2 us                                                                | 29.6 us: 1.02x faster                                                    |
| xml_etree_parse     | 142 ms                                                                 | 140 ms: 1.01x faster                                                     |
| xml_etree_iterparse | 98.7 ms                                                                | 97.8 ms: 1.01x faster                                                    |
| xml_etree_process   | 56.2 ms                                                                | 55.8 ms: 1.01x faster                                                    |
| Geometric mean      | (ref)                                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (3): xml_etree_generate, unpickle_pure_python, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250317-linux-x86_64-python-fd545d735d5f9c048f99-3.14.0a6+-fd545d7 | bm-20250319-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-88219fd |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.22 ms                                                                | 8.16 ms: 1.01x faster                                                    |
| python_startup         | 13.1 ms                                                                | 13.1 ms: 1.01x faster                                                    |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250317-linux-x86_64-python-fd545d735d5f9c048f99-3.14.0a6+-fd545d7 | bm-20250319-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-88219fd |
|-----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 51.0 ms                                                                | 50.2 ms: 1.02x faster                                                    |
| mako            | 11.1 ms                                                                | 11.0 ms: 1.01x faster                                                    |
| django_template | 31.9 ms                                                                | 31.4 ms: 1.01x faster                                                    |
| genshi_text     | 21.6 ms                                                                | 21.3 ms: 1.01x faster                                                    |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20250317-linux-x86_64-python-fd545d735d5f9c048f99-3.14.0a6+-fd545d7 | bm-20250319-linux-x86_64-brandtbucher-jit_unknown_syms-3.14.0a6+-88219fd |
|----------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| logging_silent             | 100 ns                                                                 | 95.4 ns: 1.05x faster                                                    |
| json_dumps                 | 11.8 ms                                                                | 11.4 ms: 1.03x faster                                                    |
| deepcopy_memo              | 30.0 us                                                                | 29.2 us: 1.03x faster                                                    |
| scimark_sparse_mat_mult    | 4.76 ms                                                                | 4.62 ms: 1.03x faster                                                    |
| scimark_lu                 | 121 ms                                                                 | 118 ms: 1.02x faster                                                     |
| regex_v8                   | 23.9 ms                                                                | 23.3 ms: 1.02x faster                                                    |
| scimark_sor                | 121 ms                                                                 | 119 ms: 1.02x faster                                                     |
| pickle_pure_python         | 326 us                                                                 | 320 us: 1.02x faster                                                     |
| typing_runtime_protocols   | 170 us                                                                 | 166 us: 1.02x faster                                                     |
| json_loads                 | 30.2 us                                                                | 29.6 us: 1.02x faster                                                    |
| regex_dna                  | 225 ms                                                                 | 221 ms: 1.02x faster                                                     |
| hexiom                     | 6.90 ms                                                                | 6.79 ms: 1.02x faster                                                    |
| genshi_xml                 | 51.0 ms                                                                | 50.2 ms: 1.02x faster                                                    |
| mako                       | 11.1 ms                                                                | 11.0 ms: 1.01x faster                                                    |
| json                       | 5.36 ms                                                                | 5.28 ms: 1.01x faster                                                    |
| scimark_monte_carlo        | 68.9 ms                                                                | 67.9 ms: 1.01x faster                                                    |
| django_template            | 31.9 ms                                                                | 31.4 ms: 1.01x faster                                                    |
| xml_etree_parse            | 142 ms                                                                 | 140 ms: 1.01x faster                                                     |
| connected_components       | 459 ms                                                                 | 453 ms: 1.01x faster                                                     |
| shortest_path              | 498 ms                                                                 | 492 ms: 1.01x faster                                                     |
| async_tree_memoization     | 319 ms                                                                 | 315 ms: 1.01x faster                                                     |
| genshi_text                | 21.6 ms                                                                | 21.3 ms: 1.01x faster                                                    |
| coroutines                 | 23.7 ms                                                                | 23.4 ms: 1.01x faster                                                    |
| sqlite_synth               | 2.75 us                                                                | 2.72 us: 1.01x faster                                                    |
| crypto_pyaes               | 79.0 ms                                                                | 78.1 ms: 1.01x faster                                                    |
| mdp                        | 2.50 sec                                                               | 2.48 sec: 1.01x faster                                                   |
| xml_etree_iterparse        | 98.7 ms                                                                | 97.8 ms: 1.01x faster                                                    |
| thrift                     | 779 us                                                                 | 773 us: 1.01x faster                                                     |
| python_startup_no_site     | 8.22 ms                                                                | 8.16 ms: 1.01x faster                                                    |
| async_tree_cpu_io_mixed_tg | 481 ms                                                                 | 478 ms: 1.01x faster                                                     |
| xml_etree_process          | 56.2 ms                                                                | 55.8 ms: 1.01x faster                                                    |
| bench_mp_pool              | 83.2 ms                                                                | 82.6 ms: 1.01x faster                                                    |
| raytrace                   | 270 ms                                                                 | 268 ms: 1.01x faster                                                     |
| python_startup             | 13.1 ms                                                                | 13.1 ms: 1.01x faster                                                    |
| sqlalchemy_imperative      | 17.1 ms                                                                | 17.0 ms: 1.01x faster                                                    |
| subparsers                 | 21.1 ms                                                                | 21.0 ms: 1.01x faster                                                    |
| richards                   | 35.6 ms                                                                | 35.3 ms: 1.01x faster                                                    |
| richards_super             | 40.8 ms                                                                | 40.6 ms: 1.01x faster                                                    |
| async_generators           | 417 ms                                                                 | 415 ms: 1.01x faster                                                     |
| sqlglot_v2_normalize       | 109 ms                                                                 | 108 ms: 1.01x faster                                                     |
| chaos                      | 60.2 ms                                                                | 59.8 ms: 1.01x faster                                                    |
| async_tree_cpu_io_mixed    | 497 ms                                                                 | 494 ms: 1.01x faster                                                     |
| sqlglot_v2_transpile       | 1.61 ms                                                                | 1.61 ms: 1.00x faster                                                    |
| deepcopy                   | 257 us                                                                 | 256 us: 1.00x faster                                                     |
| bench_thread_pool          | 883 us                                                                 | 881 us: 1.00x faster                                                     |
| 2to3                       | 263 ms                                                                 | 262 ms: 1.00x faster                                                     |
| dulwich_log                | 60.2 ms                                                                | 60.4 ms: 1.00x slower                                                    |
| docutils                   | 2.68 sec                                                               | 2.69 sec: 1.00x slower                                                   |
| pyflate                    | 447 ms                                                                 | 451 ms: 1.01x slower                                                     |
| spectral_norm              | 95.2 ms                                                                | 96.3 ms: 1.01x slower                                                    |
| logging_format             | 6.17 us                                                                | 6.25 us: 1.01x slower                                                    |
| generators                 | 28.3 ms                                                                | 28.7 ms: 1.01x slower                                                    |
| regex_effbot               | 3.48 ms                                                                | 3.53 ms: 1.02x slower                                                    |
| scimark_fft                | 308 ms                                                                 | 313 ms: 1.02x slower                                                     |
| pprint_safe_repr           | 755 ms                                                                 | 769 ms: 1.02x slower                                                     |
| html5lib                   | 62.2 ms                                                                | 63.6 ms: 1.02x slower                                                    |
| gc_traversal               | 4.85 ms                                                                | 4.98 ms: 1.03x slower                                                    |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (35): async_tree_memoization_tg, k_core, nbody, async_tree_io_tg, async_tree_none, async_tree_none_tg, xml_etree_generate, unpickle_pure_python, logging_simple, pathlib, comprehensions, async_tree_io, sphinx, deltablue, coverage, meteor_contest, asyncio_websockets, deepcopy_reduce, sqlglot_v2_parse, pylint, sqlalchemy_declarative, float, nqueens, sqlglot_v2_optimize, pidigits, telco, go, create_gc_cycles, regex_compile, pycparser, bpe_tokeniser, pprint_pformat, fannkuch, many_optionals, tomli_loads
Ignored benchmarks (4) of results/bm-20250317-3.14.0a6+-fd545d7-JIT/bm-20250317-linux-x86_64-python-fd545d735d5f9c048f99-3.14.0a6+-fd545d7.json: sympy_expand, sympy_integrate, sympy_str, sympy_sum

- Geometric mean (including insignificant results): 1.004x faster

# HPT report

- Reliability score: 99.86% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x