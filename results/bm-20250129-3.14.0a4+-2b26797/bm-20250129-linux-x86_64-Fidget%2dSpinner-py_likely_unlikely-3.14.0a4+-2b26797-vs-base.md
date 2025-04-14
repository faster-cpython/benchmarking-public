# Results vs. base

- fork: Fidget-Spinner
- ref: py_likely_unlikely
- machine: linux-x86_64
- commit hash: 2b26797
- commit date: 2025-01-29
- overall geometric mean: 1.003x faster
- HPT reliability: 81.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250123-linux-x86_64-python-5c9a63f62c9e56d1576c-3.14.0a4+-5c9a63f | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 254 ms                                                                 | 252 ms: 1.01x faster                                                           |
| html5lib       | 61.8 ms                                                                | 61.1 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                   |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20250123-linux-x86_64-python-5c9a63f62c9e56d1576c-3.14.0a4+-5c9a63f | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|--------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none_tg | 253 ms                                                                 | 256 ms: 1.01x slower                                                           |
| async_generators   | 379 ms                                                                 | 387 ms: 1.02x slower                                                           |
| coroutines         | 23.0 ms                                                                | 23.9 ms: 1.04x slower                                                          |
| Geometric mean     | (ref)                                                                  | 1.01x slower                                                                   |

Benchmark hidden because not significant (8): async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_none, async_tree_memoization, asyncio_websockets, async_tree_io_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250123-linux-x86_64-python-5c9a63f62c9e56d1576c-3.14.0a4+-5c9a63f | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 94.2 ms                                                                | 93.0 ms: 1.01x faster                                                          |
| pidigits       | 187 ms                                                                 | 186 ms: 1.00x faster                                                           |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250123-linux-x86_64-python-5c9a63f62c9e56d1576c-3.14.0a4+-5c9a63f | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 3.41 ms                                                                | 3.38 ms: 1.01x faster                                                          |
| regex_compile  | 127 ms                                                                 | 127 ms: 1.00x faster                                                           |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                   |

Benchmark hidden because not significant (2): regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250123-linux-x86_64-python-5c9a63f62c9e56d1576c-3.14.0a4+-5c9a63f | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|----------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pickle_pure_python   | 320 us                                                                 | 314 us: 1.02x faster                                                           |
| unpickle_pure_python | 219 us                                                                 | 216 us: 1.02x faster                                                           |
| xml_etree_generate   | 85.1 ms                                                                | 83.9 ms: 1.01x faster                                                          |
| xml_etree_process    | 59.4 ms                                                                | 59.0 ms: 1.01x faster                                                          |
| json_loads           | 29.3 us                                                                | 29.1 us: 1.00x faster                                                          |
| json_dumps           | 11.8 ms                                                                | 11.9 ms: 1.00x slower                                                          |
| tomli_loads          | 1.94 sec                                                               | 1.98 sec: 1.02x slower                                                         |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                                   |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250123-linux-x86_64-python-5c9a63f62c9e56d1576c-3.14.0a4+-5c9a63f | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup | 12.8 ms                                                                | 12.8 ms: 1.00x slower                                                          |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                   |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250123-linux-x86_64-python-5c9a63f62c9e56d1576c-3.14.0a4+-5c9a63f | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|-----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| django_template | 32.7 ms                                                                | 32.0 ms: 1.02x faster                                                          |
| genshi_xml      | 48.7 ms                                                                | 48.4 ms: 1.01x faster                                                          |
| mako            | 11.2 ms                                                                | 11.4 ms: 1.02x slower                                                          |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                                   |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20250123-linux-x86_64-python-5c9a63f62c9e56d1576c-3.14.0a4+-5c9a63f | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|--------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| gc_traversal             | 4.94 ms                                                                | 4.57 ms: 1.08x faster                                                          |
| spectral_norm            | 101 ms                                                                 | 94.9 ms: 1.06x faster                                                          |
| django_template          | 32.7 ms                                                                | 32.0 ms: 1.02x faster                                                          |
| pprint_pformat           | 1.49 sec                                                               | 1.46 sec: 1.02x faster                                                         |
| coverage                 | 92.8 ms                                                                | 90.9 ms: 1.02x faster                                                          |
| meteor_contest           | 108 ms                                                                 | 105 ms: 1.02x faster                                                           |
| pickle_pure_python       | 320 us                                                                 | 314 us: 1.02x faster                                                           |
| generators               | 28.2 ms                                                                | 27.7 ms: 1.02x faster                                                          |
| deepcopy_memo            | 31.4 us                                                                | 30.8 us: 1.02x faster                                                          |
| logging_silent           | 107 ns                                                                 | 105 ns: 1.02x faster                                                           |
| unpickle_pure_python     | 219 us                                                                 | 216 us: 1.02x faster                                                           |
| crypto_pyaes             | 72.5 ms                                                                | 71.4 ms: 1.01x faster                                                          |
| xml_etree_generate       | 85.1 ms                                                                | 83.9 ms: 1.01x faster                                                          |
| nbody                    | 94.2 ms                                                                | 93.0 ms: 1.01x faster                                                          |
| mdp                      | 2.50 sec                                                               | 2.47 sec: 1.01x faster                                                         |
| hexiom                   | 6.26 ms                                                                | 6.19 ms: 1.01x faster                                                          |
| html5lib                 | 61.8 ms                                                                | 61.1 ms: 1.01x faster                                                          |
| scimark_monte_carlo      | 68.2 ms                                                                | 67.4 ms: 1.01x faster                                                          |
| pprint_safe_repr         | 724 ms                                                                 | 717 ms: 1.01x faster                                                           |
| deepcopy_reduce          | 2.65 us                                                                | 2.62 us: 1.01x faster                                                          |
| go                       | 118 ms                                                                 | 117 ms: 1.01x faster                                                           |
| sympy_str                | 268 ms                                                                 | 265 ms: 1.01x faster                                                           |
| deepcopy                 | 258 us                                                                 | 256 us: 1.01x faster                                                           |
| xml_etree_process        | 59.4 ms                                                                | 59.0 ms: 1.01x faster                                                          |
| sqlglot_transpile        | 1.57 ms                                                                | 1.56 ms: 1.01x faster                                                          |
| create_gc_cycles         | 2.46 ms                                                                | 2.44 ms: 1.01x faster                                                          |
| genshi_xml               | 48.7 ms                                                                | 48.4 ms: 1.01x faster                                                          |
| regex_effbot             | 3.41 ms                                                                | 3.38 ms: 1.01x faster                                                          |
| sqlglot_parse            | 1.26 ms                                                                | 1.25 ms: 1.01x faster                                                          |
| 2to3                     | 254 ms                                                                 | 252 ms: 1.01x faster                                                           |
| json_loads               | 29.3 us                                                                | 29.1 us: 1.00x faster                                                          |
| scimark_fft              | 349 ms                                                                 | 347 ms: 1.00x faster                                                           |
| sqlglot_normalize        | 105 ms                                                                 | 104 ms: 1.00x faster                                                           |
| scimark_lu               | 117 ms                                                                 | 116 ms: 1.00x faster                                                           |
| sqlalchemy_declarative   | 129 ms                                                                 | 129 ms: 1.00x faster                                                           |
| sympy_integrate          | 19.7 ms                                                                | 19.6 ms: 1.00x faster                                                          |
| regex_compile            | 127 ms                                                                 | 127 ms: 1.00x faster                                                           |
| bench_thread_pool        | 865 us                                                                 | 863 us: 1.00x faster                                                           |
| raytrace                 | 272 ms                                                                 | 272 ms: 1.00x faster                                                           |
| pidigits                 | 187 ms                                                                 | 186 ms: 1.00x faster                                                           |
| python_startup           | 12.8 ms                                                                | 12.8 ms: 1.00x slower                                                          |
| sqlglot_optimize         | 52.6 ms                                                                | 52.7 ms: 1.00x slower                                                          |
| many_optionals           | 934 us                                                                 | 937 us: 1.00x slower                                                           |
| json_dumps               | 11.8 ms                                                                | 11.9 ms: 1.00x slower                                                          |
| bpe_tokeniser            | 4.50 sec                                                               | 4.52 sec: 1.00x slower                                                         |
| pyflate                  | 454 ms                                                                 | 458 ms: 1.01x slower                                                           |
| nqueens                  | 80.3 ms                                                                | 81.1 ms: 1.01x slower                                                          |
| async_tree_none_tg       | 253 ms                                                                 | 256 ms: 1.01x slower                                                           |
| logging_format           | 6.06 us                                                                | 6.13 us: 1.01x slower                                                          |
| typing_runtime_protocols | 159 us                                                                 | 162 us: 1.02x slower                                                           |
| mako                     | 11.2 ms                                                                | 11.4 ms: 1.02x slower                                                          |
| tomli_loads              | 1.94 sec                                                               | 1.98 sec: 1.02x slower                                                         |
| async_generators         | 379 ms                                                                 | 387 ms: 1.02x slower                                                           |
| scimark_sparse_mat_mult  | 4.74 ms                                                                | 4.86 ms: 1.03x slower                                                          |
| pathlib                  | 15.9 ms                                                                | 16.4 ms: 1.03x slower                                                          |
| coroutines               | 23.0 ms                                                                | 23.9 ms: 1.04x slower                                                          |
| Geometric mean           | (ref)                                                                  | 1.00x faster                                                                   |

Benchmark hidden because not significant (40): float, scimark_sor, async_tree_memoization_tg, sympy_expand, richards_super, telco, sympy_sum, chaos, comprehensions, deltablue, async_tree_cpu_io_mixed_tg, docutils, json, regex_dna, fannkuch, python_startup_no_site, sqlalchemy_imperative, sphinx, thrift, regex_v8, pylint, async_tree_io, dulwich_log, connected_components, logging_simple, shortest_path, pycparser, k_core, richards, async_tree_none, async_tree_memoization, asyncio_websockets, genshi_text, bench_mp_pool, subparsers, async_tree_io_tg, xml_etree_parse, async_tree_cpu_io_mixed, xml_etree_iterparse, sqlite_synth

- Geometric mean (including insignificant results): 1.003x faster

# HPT report

- Reliability score: 81.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x