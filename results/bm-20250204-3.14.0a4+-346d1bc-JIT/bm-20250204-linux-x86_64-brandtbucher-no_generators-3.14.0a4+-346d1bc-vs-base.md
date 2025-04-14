# Results vs. base

- fork: brandtbucher
- ref: no_generators
- machine: linux-x86_64
- commit hash: 346d1bc
- commit date: 2025-02-04
- overall geometric mean: 1.005x faster
- HPT reliability: 69.77%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250204-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-346d1bc |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 261 ms                                                                 | 259 ms: 1.01x faster                                                  |
| html5lib       | 63.3 ms                                                                | 62.5 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250204-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-346d1bc |
|------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_generators | 411 ms                                                                 | 408 ms: 1.01x faster                                                  |
| Geometric mean   | (ref)                                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (10): async_tree_io, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_none_tg, asyncio_websockets, coroutines, async_tree_none, async_tree_io_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250204-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-346d1bc |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (2): nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250204-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-346d1bc |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 211 ms                                                                 | 194 ms: 1.09x faster                                                  |
| regex_effbot   | 3.18 ms                                                                | 2.97 ms: 1.07x faster                                                 |
| regex_compile  | 130 ms                                                                 | 129 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250204-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-346d1bc |
|--------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads        | 1.84 sec                                                               | 1.82 sec: 1.01x faster                                                |
| json_loads         | 28.9 us                                                                | 28.8 us: 1.00x faster                                                 |
| json_dumps         | 11.1 ms                                                                | 11.3 ms: 1.01x slower                                                 |
| xml_etree_generate | 78.0 ms                                                                | 79.7 ms: 1.02x slower                                                 |
| xml_etree_process  | 54.6 ms                                                                | 56.1 ms: 1.03x slower                                                 |
| Geometric mean     | (ref)                                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (4): pickle_pure_python, xml_etree_iterparse, xml_etree_parse, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250204-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-346d1bc |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 7.06 ms                                                                | 7.05 ms: 1.00x faster                                                 |
| python_startup         | 12.9 ms                                                                | 12.9 ms: 1.00x slower                                                 |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250204-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-346d1bc |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 57.7 ms                                                                | 54.4 ms: 1.06x faster                                                 |
| django_template | 33.1 ms                                                                | 32.6 ms: 1.01x faster                                                 |
| mako            | 10.3 ms                                                                | 10.2 ms: 1.01x faster                                                 |
| Geometric mean  | (ref)                                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250204-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-346d1bc |
|--------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| generators               | 37.5 ms                                                                | 28.8 ms: 1.30x faster                                                 |
| regex_dna                | 211 ms                                                                 | 194 ms: 1.09x faster                                                  |
| regex_effbot             | 3.18 ms                                                                | 2.97 ms: 1.07x faster                                                 |
| genshi_xml               | 57.7 ms                                                                | 54.4 ms: 1.06x faster                                                 |
| spectral_norm            | 95.6 ms                                                                | 93.4 ms: 1.02x faster                                                 |
| scimark_monte_carlo      | 63.9 ms                                                                | 62.6 ms: 1.02x faster                                                 |
| crypto_pyaes             | 71.3 ms                                                                | 70.1 ms: 1.02x faster                                                 |
| typing_runtime_protocols | 165 us                                                                 | 162 us: 1.01x faster                                                  |
| django_template          | 33.1 ms                                                                | 32.6 ms: 1.01x faster                                                 |
| tomli_loads              | 1.84 sec                                                               | 1.82 sec: 1.01x faster                                                |
| html5lib                 | 63.3 ms                                                                | 62.5 ms: 1.01x faster                                                 |
| pathlib                  | 16.1 ms                                                                | 15.9 ms: 1.01x faster                                                 |
| regex_compile            | 130 ms                                                                 | 129 ms: 1.01x faster                                                  |
| telco                    | 7.70 ms                                                                | 7.62 ms: 1.01x faster                                                 |
| go                       | 128 ms                                                                 | 127 ms: 1.01x faster                                                  |
| sqlglot_normalize        | 108 ms                                                                 | 107 ms: 1.01x faster                                                  |
| scimark_fft              | 314 ms                                                                 | 311 ms: 1.01x faster                                                  |
| mako                     | 10.3 ms                                                                | 10.2 ms: 1.01x faster                                                 |
| json                     | 5.18 ms                                                                | 5.13 ms: 1.01x faster                                                 |
| pyflate                  | 463 ms                                                                 | 460 ms: 1.01x faster                                                  |
| async_generators         | 411 ms                                                                 | 408 ms: 1.01x faster                                                  |
| 2to3                     | 261 ms                                                                 | 259 ms: 1.01x faster                                                  |
| hexiom                   | 7.46 ms                                                                | 7.42 ms: 1.01x faster                                                 |
| sqlglot_optimize         | 54.1 ms                                                                | 53.9 ms: 1.00x faster                                                 |
| json_loads               | 28.9 us                                                                | 28.8 us: 1.00x faster                                                 |
| pidigits                 | 186 ms                                                                 | 186 ms: 1.00x faster                                                  |
| python_startup_no_site   | 7.06 ms                                                                | 7.05 ms: 1.00x faster                                                 |
| python_startup           | 12.9 ms                                                                | 12.9 ms: 1.00x slower                                                 |
| create_gc_cycles         | 2.45 ms                                                                | 2.45 ms: 1.00x slower                                                 |
| shortest_path            | 481 ms                                                                 | 483 ms: 1.00x slower                                                  |
| meteor_contest           | 108 ms                                                                 | 109 ms: 1.00x slower                                                  |
| mdp                      | 2.54 sec                                                               | 2.56 sec: 1.01x slower                                                |
| deltablue                | 3.49 ms                                                                | 3.51 ms: 1.01x slower                                                 |
| connected_components     | 440 ms                                                                 | 443 ms: 1.01x slower                                                  |
| coverage                 | 89.7 ms                                                                | 90.7 ms: 1.01x slower                                                 |
| logging_silent           | 108 ns                                                                 | 109 ns: 1.01x slower                                                  |
| json_dumps               | 11.1 ms                                                                | 11.3 ms: 1.01x slower                                                 |
| deepcopy_memo            | 30.2 us                                                                | 30.6 us: 1.01x slower                                                 |
| deepcopy                 | 265 us                                                                 | 269 us: 1.02x slower                                                  |
| pprint_safe_repr         | 728 ms                                                                 | 741 ms: 1.02x slower                                                  |
| gc_traversal             | 4.77 ms                                                                | 4.86 ms: 1.02x slower                                                 |
| chaos                    | 58.8 ms                                                                | 60.0 ms: 1.02x slower                                                 |
| xml_etree_generate       | 78.0 ms                                                                | 79.7 ms: 1.02x slower                                                 |
| xml_etree_process        | 54.6 ms                                                                | 56.1 ms: 1.03x slower                                                 |
| scimark_lu               | 113 ms                                                                 | 117 ms: 1.03x slower                                                  |
| pycparser                | 1.14 sec                                                               | 1.21 sec: 1.07x slower                                                |
| Geometric mean           | (ref)                                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (50): pylint, sphinx, async_tree_io, pickle_pure_python, richards, thrift, comprehensions, raytrace, nbody, sqlalchemy_imperative, richards_super, subparsers, async_tree_cpu_io_mixed, logging_format, bench_thread_pool, sqlite_synth, sqlalchemy_declarative, sympy_sum, xml_etree_iterparse, dulwich_log, async_tree_memoization, sympy_expand, sympy_str, sympy_integrate, async_tree_cpu_io_mixed_tg, docutils, async_tree_none_tg, bpe_tokeniser, genshi_text, bench_mp_pool, xml_etree_parse, scimark_sor, pprint_pformat, regex_v8, asyncio_websockets, sqlglot_parse, scimark_sparse_mat_mult, coroutines, sqlglot_transpile, float, logging_simple, k_core, nqueens, many_optionals, deepcopy_reduce, unpickle_pure_python, fannkuch, async_tree_none, async_tree_io_tg, async_tree_memoization_tg

- Geometric mean (including insignificant results): 1.005x faster

# HPT report

- Reliability score: 69.77% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x