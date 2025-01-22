# Results vs. base

- fork: mdboom
- ref: aa_test_2025
- machine: linux-x86_64
- commit hash: 4844db8
- commit date: 2025-01-21
- overall geometric mean: 1.003x faster
- HPT reliability: 77.15%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250121-linux-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 256 ms                                                                 | 256 ms: 1.00x faster                                           |
| docutils       | 2.61 sec                                                               | 2.60 sec: 1.00x faster                                         |
| html5lib       | 62.1 ms                                                                | 61.2 ms: 1.02x faster                                          |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                   |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250121-linux-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 491 ms                                                                 | 482 ms: 1.02x faster                                           |
| async_tree_cpu_io_mixed_tg | 470 ms                                                                 | 465 ms: 1.01x faster                                           |
| async_tree_io_tg           | 591 ms                                                                 | 585 ms: 1.01x faster                                           |
| async_generators           | 385 ms                                                                 | 389 ms: 1.01x slower                                           |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                   |

Benchmark hidden because not significant (7): async_tree_none, async_tree_io, coroutines, async_tree_memoization, async_tree_memoization_tg, asyncio_websockets, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250121-linux-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 71.3 ms                                                                | 70.1 ms: 1.02x faster                                          |
| pidigits       | 186 ms                                                                 | 187 ms: 1.00x slower                                           |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                   |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250121-linux-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 128 ms                                                                 | 128 ms: 1.00x faster                                           |
| regex_effbot   | 3.29 ms                                                                | 3.31 ms: 1.01x slower                                          |
| regex_v8       | 25.6 ms                                                                | 26.3 ms: 1.03x slower                                          |
| regex_dna      | 203 ms                                                                 | 209 ms: 1.03x slower                                           |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250121-linux-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|--------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| tomli_loads        | 1.99 sec                                                               | 1.97 sec: 1.01x faster                                         |
| json_loads         | 29.1 us                                                                | 28.9 us: 1.01x faster                                          |
| pickle_pure_python | 326 us                                                                 | 328 us: 1.00x slower                                           |
| xml_etree_generate | 84.2 ms                                                                | 84.6 ms: 1.01x slower                                          |
| xml_etree_process  | 61.0 ms                                                                | 61.4 ms: 1.01x slower                                          |
| json_dumps         | 11.9 ms                                                                | 12.0 ms: 1.01x slower                                          |
| Geometric mean     | (ref)                                                                  | 1.00x slower                                                   |

Benchmark hidden because not significant (3): unpickle_pure_python, xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250121-linux-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup_no_site | 7.06 ms                                                                | 7.02 ms: 1.01x faster                                          |
| python_startup         | 12.9 ms                                                                | 12.8 ms: 1.01x faster                                          |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250121-linux-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| django_template | 32.0 ms                                                                | 32.2 ms: 1.01x slower                                          |
| mako            | 11.1 ms                                                                | 11.2 ms: 1.02x slower                                          |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                   |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20250121-linux-x86_64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| gc_traversal               | 4.96 ms                                                                | 4.62 ms: 1.07x faster                                          |
| scimark_sparse_mat_mult    | 4.78 ms                                                                | 4.54 ms: 1.05x faster                                          |
| pathlib                    | 16.4 ms                                                                | 15.8 ms: 1.04x faster                                          |
| logging_simple             | 5.88 us                                                                | 5.73 us: 1.03x faster                                          |
| logging_format             | 6.36 us                                                                | 6.21 us: 1.02x faster                                          |
| logging_silent             | 104 ns                                                                 | 103 ns: 1.02x faster                                           |
| scimark_fft                | 344 ms                                                                 | 337 ms: 1.02x faster                                           |
| async_tree_cpu_io_mixed    | 491 ms                                                                 | 482 ms: 1.02x faster                                           |
| float                      | 71.3 ms                                                                | 70.1 ms: 1.02x faster                                          |
| crypto_pyaes               | 72.9 ms                                                                | 71.8 ms: 1.02x faster                                          |
| html5lib                   | 62.1 ms                                                                | 61.2 ms: 1.02x faster                                          |
| sqlalchemy_declarative     | 132 ms                                                                 | 130 ms: 1.01x faster                                           |
| sympy_str                  | 269 ms                                                                 | 266 ms: 1.01x faster                                           |
| sqlalchemy_imperative      | 16.8 ms                                                                | 16.6 ms: 1.01x faster                                          |
| scimark_monte_carlo        | 67.1 ms                                                                | 66.3 ms: 1.01x faster                                          |
| bench_mp_pool              | 82.0 ms                                                                | 81.0 ms: 1.01x faster                                          |
| create_gc_cycles           | 2.47 ms                                                                | 2.44 ms: 1.01x faster                                          |
| async_tree_cpu_io_mixed_tg | 470 ms                                                                 | 465 ms: 1.01x faster                                           |
| async_tree_io_tg           | 591 ms                                                                 | 585 ms: 1.01x faster                                           |
| tomli_loads                | 1.99 sec                                                               | 1.97 sec: 1.01x faster                                         |
| spectral_norm              | 98.8 ms                                                                | 97.9 ms: 1.01x faster                                          |
| sympy_sum                  | 148 ms                                                                 | 147 ms: 1.01x faster                                           |
| comprehensions             | 16.8 us                                                                | 16.7 us: 1.01x faster                                          |
| sympy_expand               | 458 ms                                                                 | 455 ms: 1.01x faster                                           |
| deepcopy                   | 260 us                                                                 | 258 us: 1.01x faster                                           |
| sympy_integrate            | 19.8 ms                                                                | 19.7 ms: 1.01x faster                                          |
| many_optionals             | 955 us                                                                 | 949 us: 1.01x faster                                           |
| hexiom                     | 6.33 ms                                                                | 6.29 ms: 1.01x faster                                          |
| python_startup_no_site     | 7.06 ms                                                                | 7.02 ms: 1.01x faster                                          |
| python_startup             | 12.9 ms                                                                | 12.8 ms: 1.01x faster                                          |
| dulwich_log                | 64.8 ms                                                                | 64.4 ms: 1.01x faster                                          |
| nqueens                    | 80.3 ms                                                                | 79.9 ms: 1.01x faster                                          |
| json_loads                 | 29.1 us                                                                | 28.9 us: 1.01x faster                                          |
| generators                 | 28.1 ms                                                                | 28.0 ms: 1.01x faster                                          |
| sqlglot_transpile          | 1.57 ms                                                                | 1.56 ms: 1.01x faster                                          |
| regex_compile              | 128 ms                                                                 | 128 ms: 1.00x faster                                           |
| richards                   | 43.5 ms                                                                | 43.3 ms: 1.00x faster                                          |
| bench_thread_pool          | 866 us                                                                 | 862 us: 1.00x faster                                           |
| docutils                   | 2.61 sec                                                               | 2.60 sec: 1.00x faster                                         |
| 2to3                       | 256 ms                                                                 | 256 ms: 1.00x faster                                           |
| pidigits                   | 186 ms                                                                 | 187 ms: 1.00x slower                                           |
| pickle_pure_python         | 326 us                                                                 | 328 us: 1.00x slower                                           |
| bpe_tokeniser              | 4.48 sec                                                               | 4.49 sec: 1.00x slower                                         |
| meteor_contest             | 105 ms                                                                 | 106 ms: 1.00x slower                                           |
| xml_etree_generate         | 84.2 ms                                                                | 84.6 ms: 1.01x slower                                          |
| thrift                     | 783 us                                                                 | 787 us: 1.01x slower                                           |
| regex_effbot               | 3.29 ms                                                                | 3.31 ms: 1.01x slower                                          |
| xml_etree_process          | 61.0 ms                                                                | 61.4 ms: 1.01x slower                                          |
| django_template            | 32.0 ms                                                                | 32.2 ms: 1.01x slower                                          |
| json                       | 5.20 ms                                                                | 5.25 ms: 1.01x slower                                          |
| deepcopy_reduce            | 2.65 us                                                                | 2.67 us: 1.01x slower                                          |
| json_dumps                 | 11.9 ms                                                                | 12.0 ms: 1.01x slower                                          |
| fannkuch                   | 400 ms                                                                 | 404 ms: 1.01x slower                                           |
| async_generators           | 385 ms                                                                 | 389 ms: 1.01x slower                                           |
| pprint_pformat             | 1.47 sec                                                               | 1.49 sec: 1.01x slower                                         |
| chaos                      | 57.7 ms                                                                | 58.5 ms: 1.01x slower                                          |
| mako                       | 11.1 ms                                                                | 11.2 ms: 1.02x slower                                          |
| typing_runtime_protocols   | 162 us                                                                 | 165 us: 1.02x slower                                           |
| regex_v8                   | 25.6 ms                                                                | 26.3 ms: 1.03x slower                                          |
| regex_dna                  | 203 ms                                                                 | 209 ms: 1.03x slower                                           |
| pyflate                    | 449 ms                                                                 | 462 ms: 1.03x slower                                           |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                   |

Benchmark hidden because not significant (35): pylint, async_tree_none, sphinx, sqlite_synth, async_tree_io, scimark_sor, coverage, coroutines, deltablue, connected_components, unpickle_pure_python, deepcopy_memo, subparsers, async_tree_memoization, sqlglot_parse, async_tree_memoization_tg, mdp, sqlglot_optimize, raytrace, richards_super, go, telco, scimark_lu, xml_etree_parse, pprint_safe_repr, asyncio_websockets, xml_etree_iterparse, sqlglot_normalize, genshi_text, genshi_xml, nbody, shortest_path, async_tree_none_tg, k_core, pycparser

- Geometric mean (including insignificant results): 1.003x faster

# HPT report

- Reliability score: 77.15% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x