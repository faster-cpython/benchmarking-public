# Results vs. base

- fork: brandtbucher
- ref: jit_binary_op_extend
- machine: linux-x86_64
- commit hash: edbf7ef
- commit date: 2025-03-17
- overall geometric mean: 1.001x faster
- HPT reliability: 55.88%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250317-linux-x86_64-python-fd545d735d5f9c048f99-3.14.0a6+-fd545d7 | bm-20250317-linux-x86_64-brandtbucher-jit_binary_op_extend-3.14.0a6+-edbf7ef |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| docutils       | 2.68 sec                                                               | 2.69 sec: 1.00x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250317-linux-x86_64-python-fd545d735d5f9c048f99-3.14.0a6+-fd545d7 | bm-20250317-linux-x86_64-brandtbucher-jit_binary_op_extend-3.14.0a6+-edbf7ef |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| coroutines                 | 23.7 ms                                                                | 23.4 ms: 1.01x faster                                                        |
| async_tree_cpu_io_mixed_tg | 481 ms                                                                 | 477 ms: 1.01x faster                                                         |
| async_tree_cpu_io_mixed    | 497 ms                                                                 | 493 ms: 1.01x faster                                                         |
| async_tree_memoization     | 319 ms                                                                 | 317 ms: 1.01x faster                                                         |
| async_generators           | 417 ms                                                                 | 425 ms: 1.02x slower                                                         |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (6): async_tree_io_tg, async_tree_memoization_tg, async_tree_io, async_tree_none, async_tree_none_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): float, pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250317-linux-x86_64-python-fd545d735d5f9c048f99-3.14.0a6+-fd545d7 | bm-20250317-linux-x86_64-brandtbucher-jit_binary_op_extend-3.14.0a6+-edbf7ef |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.48 ms                                                                | 3.34 ms: 1.04x faster                                                        |
| regex_v8       | 23.9 ms                                                                | 24.2 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (2): regex_compile, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250317-linux-x86_64-python-fd545d735d5f9c048f99-3.14.0a6+-fd545d7 | bm-20250317-linux-x86_64-brandtbucher-jit_binary_op_extend-3.14.0a6+-edbf7ef |
|---------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps          | 11.8 ms                                                                | 11.6 ms: 1.02x faster                                                        |
| xml_etree_parse     | 142 ms                                                                 | 141 ms: 1.01x faster                                                         |
| json_loads          | 30.2 us                                                                | 29.9 us: 1.01x faster                                                        |
| xml_etree_iterparse | 98.7 ms                                                                | 98.3 ms: 1.00x faster                                                        |
| xml_etree_process   | 56.2 ms                                                                | 56.6 ms: 1.01x slower                                                        |
| tomli_loads         | 1.87 sec                                                               | 1.88 sec: 1.01x slower                                                       |
| Geometric mean      | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (3): pickle_pure_python, xml_etree_generate, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250317-linux-x86_64-python-fd545d735d5f9c048f99-3.14.0a6+-fd545d7 | bm-20250317-linux-x86_64-brandtbucher-jit_binary_op_extend-3.14.0a6+-edbf7ef |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.22 ms                                                                | 8.18 ms: 1.01x faster                                                        |
| python_startup         | 13.1 ms                                                                | 13.1 ms: 1.00x faster                                                        |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250317-linux-x86_64-python-fd545d735d5f9c048f99-3.14.0a6+-fd545d7 | bm-20250317-linux-x86_64-brandtbucher-jit_binary_op_extend-3.14.0a6+-edbf7ef |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 31.9 ms                                                                | 32.1 ms: 1.01x slower                                                        |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (3): genshi_text, genshi_xml, mako

All benchmarks:
===============

| Benchmark                  | bm-20250317-linux-x86_64-python-fd545d735d5f9c048f99-3.14.0a6+-fd545d7 | bm-20250317-linux-x86_64-brandtbucher-jit_binary_op_extend-3.14.0a6+-edbf7ef |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot               | 3.48 ms                                                                | 3.34 ms: 1.04x faster                                                        |
| scimark_lu                 | 121 ms                                                                 | 117 ms: 1.03x faster                                                         |
| pycparser                  | 1.18 sec                                                               | 1.15 sec: 1.03x faster                                                       |
| hexiom                     | 6.90 ms                                                                | 6.74 ms: 1.02x faster                                                        |
| json_dumps                 | 11.8 ms                                                                | 11.6 ms: 1.02x faster                                                        |
| scimark_sor                | 121 ms                                                                 | 120 ms: 1.01x faster                                                         |
| meteor_contest             | 110 ms                                                                 | 108 ms: 1.01x faster                                                         |
| coroutines                 | 23.7 ms                                                                | 23.4 ms: 1.01x faster                                                        |
| crypto_pyaes               | 79.0 ms                                                                | 78.1 ms: 1.01x faster                                                        |
| raytrace                   | 270 ms                                                                 | 267 ms: 1.01x faster                                                         |
| xml_etree_parse            | 142 ms                                                                 | 141 ms: 1.01x faster                                                         |
| async_tree_cpu_io_mixed_tg | 481 ms                                                                 | 477 ms: 1.01x faster                                                         |
| logging_silent             | 100 ns                                                                 | 99.2 ns: 1.01x faster                                                        |
| logging_simple             | 5.59 us                                                                | 5.55 us: 1.01x faster                                                        |
| sqlite_synth               | 2.75 us                                                                | 2.73 us: 1.01x faster                                                        |
| json_loads                 | 30.2 us                                                                | 29.9 us: 1.01x faster                                                        |
| async_tree_cpu_io_mixed    | 497 ms                                                                 | 493 ms: 1.01x faster                                                         |
| deltablue                  | 3.08 ms                                                                | 3.06 ms: 1.01x faster                                                        |
| python_startup_no_site     | 8.22 ms                                                                | 8.18 ms: 1.01x faster                                                        |
| deepcopy_memo              | 30.0 us                                                                | 29.9 us: 1.01x faster                                                        |
| sqlglot_v2_transpile       | 1.61 ms                                                                | 1.61 ms: 1.01x faster                                                        |
| async_tree_memoization     | 319 ms                                                                 | 317 ms: 1.01x faster                                                         |
| xml_etree_iterparse        | 98.7 ms                                                                | 98.3 ms: 1.00x faster                                                        |
| python_startup             | 13.1 ms                                                                | 13.1 ms: 1.00x faster                                                        |
| bench_thread_pool          | 883 us                                                                 | 885 us: 1.00x slower                                                         |
| docutils                   | 2.68 sec                                                               | 2.69 sec: 1.00x slower                                                       |
| create_gc_cycles           | 2.49 ms                                                                | 2.50 ms: 1.00x slower                                                        |
| spectral_norm              | 95.2 ms                                                                | 95.8 ms: 1.01x slower                                                        |
| many_optionals             | 962 us                                                                 | 968 us: 1.01x slower                                                         |
| sympy_expand               | 474 ms                                                                 | 477 ms: 1.01x slower                                                         |
| subparsers                 | 21.1 ms                                                                | 21.3 ms: 1.01x slower                                                        |
| xml_etree_process          | 56.2 ms                                                                | 56.6 ms: 1.01x slower                                                        |
| django_template            | 31.9 ms                                                                | 32.1 ms: 1.01x slower                                                        |
| sqlglot_v2_normalize       | 109 ms                                                                 | 109 ms: 1.01x slower                                                         |
| tomli_loads                | 1.87 sec                                                               | 1.88 sec: 1.01x slower                                                       |
| deepcopy_reduce            | 2.71 us                                                                | 2.73 us: 1.01x slower                                                        |
| dulwich_log                | 60.2 ms                                                                | 60.8 ms: 1.01x slower                                                        |
| sympy_str                  | 274 ms                                                                 | 277 ms: 1.01x slower                                                         |
| regex_v8                   | 23.9 ms                                                                | 24.2 ms: 1.01x slower                                                        |
| deepcopy                   | 257 us                                                                 | 260 us: 1.01x slower                                                         |
| generators                 | 28.3 ms                                                                | 28.7 ms: 1.01x slower                                                        |
| pprint_safe_repr           | 755 ms                                                                 | 768 ms: 1.02x slower                                                         |
| scimark_sparse_mat_mult    | 4.76 ms                                                                | 4.84 ms: 1.02x slower                                                        |
| async_generators           | 417 ms                                                                 | 425 ms: 1.02x slower                                                         |
| scimark_fft                | 308 ms                                                                 | 315 ms: 1.02x slower                                                         |
| gc_traversal               | 4.85 ms                                                                | 4.97 ms: 1.02x slower                                                        |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (50): async_tree_io_tg, pickle_pure_python, async_tree_memoization_tg, telco, xml_etree_generate, shortest_path, richards, richards_super, connected_components, nqueens, genshi_text, async_tree_io, logging_format, sphinx, bench_mp_pool, sqlalchemy_imperative, sqlglot_v2_parse, comprehensions, async_tree_none, fannkuch, typing_runtime_protocols, pprint_pformat, coverage, mdp, 2to3, async_tree_none_tg, sqlalchemy_declarative, sqlglot_v2_optimize, sympy_sum, asyncio_websockets, float, pidigits, nbody, regex_compile, chaos, regex_dna, sympy_integrate, pylint, go, json, pathlib, unpickle_pure_python, thrift, bpe_tokeniser, scimark_monte_carlo, genshi_xml, pyflate, k_core, html5lib, mako

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 55.88% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x