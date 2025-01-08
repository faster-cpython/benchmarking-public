# Results vs. base

- fork: brandtbucher
- ref: nojit
- machine: linux-x86_64
- commit hash: f098037
- commit date: 2025-01-07
- overall geometric mean: 1.001x faster
- HPT reliability: 93.52%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250106-linux-x86_64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 255 ms                                                                 | 255 ms: 1.00x faster                                          |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                  |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20250106-linux-x86_64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| coroutines       | 23.7 ms                                                                | 23.4 ms: 1.01x faster                                         |
| async_generators | 418 ms                                                                 | 421 ms: 1.01x slower                                          |
| Geometric mean   | (ref)                                                                  | 1.00x faster                                                  |

Benchmark hidden because not significant (9): async_tree_none, async_tree_none_tg, async_tree_io, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_io_tg, asyncio_websockets, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250106-linux-x86_64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| pidigits       | 190 ms                                                                 | 187 ms: 1.02x faster                                          |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                  |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250106-linux-x86_64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_effbot   | 3.52 ms                                                                | 3.43 ms: 1.03x faster                                         |
| regex_dna      | 221 ms                                                                 | 216 ms: 1.02x faster                                          |
| regex_compile  | 128 ms                                                                 | 126 ms: 1.01x faster                                          |
| regex_v8       | 25.6 ms                                                                | 25.5 ms: 1.00x faster                                         |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250106-linux-x86_64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|---------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| json_dumps          | 11.5 ms                                                                | 11.3 ms: 1.02x faster                                         |
| xml_etree_process   | 59.9 ms                                                                | 59.1 ms: 1.01x faster                                         |
| xml_etree_generate  | 85.6 ms                                                                | 84.8 ms: 1.01x faster                                         |
| tomli_loads         | 1.97 sec                                                               | 1.96 sec: 1.01x faster                                        |
| xml_etree_iterparse | 96.4 ms                                                                | 97.4 ms: 1.01x slower                                         |
| json_loads          | 26.4 us                                                                | 27.0 us: 1.02x slower                                         |
| Geometric mean      | (ref)                                                                  | 1.00x faster                                                  |

Benchmark hidden because not significant (3): xml_etree_parse, unpickle_pure_python, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250106-linux-x86_64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 12.8 ms                                                                | 12.9 ms: 1.00x slower                                         |
| python_startup_no_site | 7.06 ms                                                                | 7.08 ms: 1.00x slower                                         |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250106-linux-x86_64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| mako            | 11.7 ms                                                                | 11.5 ms: 1.01x faster                                         |
| django_template | 31.5 ms                                                                | 31.9 ms: 1.01x slower                                         |
| genshi_text     | 22.1 ms                                                                | 22.4 ms: 1.02x slower                                         |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                  |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20250106-linux-x86_64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|--------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| pyflate                  | 467 ms                                                                 | 443 ms: 1.06x faster                                          |
| logging_silent           | 109 ns                                                                 | 105 ns: 1.04x faster                                          |
| pprint_safe_repr         | 732 ms                                                                 | 710 ms: 1.03x faster                                          |
| scimark_fft              | 353 ms                                                                 | 344 ms: 1.03x faster                                          |
| regex_effbot             | 3.52 ms                                                                | 3.43 ms: 1.03x faster                                         |
| regex_dna                | 221 ms                                                                 | 216 ms: 1.02x faster                                          |
| json_dumps               | 11.5 ms                                                                | 11.3 ms: 1.02x faster                                         |
| pprint_pformat           | 1.49 sec                                                               | 1.46 sec: 1.02x faster                                        |
| deltablue                | 3.32 ms                                                                | 3.26 ms: 1.02x faster                                         |
| pidigits                 | 190 ms                                                                 | 187 ms: 1.02x faster                                          |
| nqueens                  | 80.5 ms                                                                | 79.3 ms: 1.02x faster                                         |
| mako                     | 11.7 ms                                                                | 11.5 ms: 1.01x faster                                         |
| deepcopy_memo            | 30.9 us                                                                | 30.5 us: 1.01x faster                                         |
| xml_etree_process        | 59.9 ms                                                                | 59.1 ms: 1.01x faster                                         |
| typing_runtime_protocols | 164 us                                                                 | 161 us: 1.01x faster                                          |
| regex_compile            | 128 ms                                                                 | 126 ms: 1.01x faster                                          |
| logging_simple           | 5.65 us                                                                | 5.58 us: 1.01x faster                                         |
| richards                 | 45.0 ms                                                                | 44.4 ms: 1.01x faster                                         |
| coroutines               | 23.7 ms                                                                | 23.4 ms: 1.01x faster                                         |
| scimark_sparse_mat_mult  | 4.82 ms                                                                | 4.77 ms: 1.01x faster                                         |
| scimark_sor              | 124 ms                                                                 | 123 ms: 1.01x faster                                          |
| xml_etree_generate       | 85.6 ms                                                                | 84.8 ms: 1.01x faster                                         |
| sqlglot_transpile        | 1.59 ms                                                                | 1.58 ms: 1.01x faster                                         |
| sympy_expand             | 459 ms                                                                 | 455 ms: 1.01x faster                                          |
| deepcopy_reduce          | 2.67 us                                                                | 2.65 us: 1.01x faster                                         |
| go                       | 118 ms                                                                 | 118 ms: 1.01x faster                                          |
| sqlglot_parse            | 1.28 ms                                                                | 1.27 ms: 1.01x faster                                         |
| tomli_loads              | 1.97 sec                                                               | 1.96 sec: 1.01x faster                                        |
| hexiom                   | 6.29 ms                                                                | 6.27 ms: 1.00x faster                                         |
| regex_v8                 | 25.6 ms                                                                | 25.5 ms: 1.00x faster                                         |
| 2to3                     | 255 ms                                                                 | 255 ms: 1.00x faster                                          |
| create_gc_cycles         | 2.45 ms                                                                | 2.46 ms: 1.00x slower                                         |
| python_startup           | 12.8 ms                                                                | 12.9 ms: 1.00x slower                                         |
| sympy_integrate          | 19.9 ms                                                                | 19.9 ms: 1.00x slower                                         |
| sqlalchemy_declarative   | 130 ms                                                                 | 130 ms: 1.00x slower                                          |
| python_startup_no_site   | 7.06 ms                                                                | 7.08 ms: 1.00x slower                                         |
| fannkuch                 | 401 ms                                                                 | 403 ms: 1.00x slower                                          |
| sqlite_synth             | 2.82 us                                                                | 2.83 us: 1.01x slower                                         |
| crypto_pyaes             | 71.7 ms                                                                | 72.2 ms: 1.01x slower                                         |
| async_generators         | 418 ms                                                                 | 421 ms: 1.01x slower                                          |
| meteor_contest           | 105 ms                                                                 | 106 ms: 1.01x slower                                          |
| telco                    | 7.71 ms                                                                | 7.77 ms: 1.01x slower                                         |
| json                     | 4.90 ms                                                                | 4.94 ms: 1.01x slower                                         |
| django_template          | 31.5 ms                                                                | 31.9 ms: 1.01x slower                                         |
| scimark_lu               | 116 ms                                                                 | 117 ms: 1.01x slower                                          |
| sqlglot_normalize        | 103 ms                                                                 | 104 ms: 1.01x slower                                          |
| sqlalchemy_imperative    | 16.4 ms                                                                | 16.6 ms: 1.01x slower                                         |
| xml_etree_iterparse      | 96.4 ms                                                                | 97.4 ms: 1.01x slower                                         |
| connected_components     | 437 ms                                                                 | 442 ms: 1.01x slower                                          |
| bpe_tokeniser            | 4.52 sec                                                               | 4.58 sec: 1.01x slower                                        |
| raytrace                 | 272 ms                                                                 | 276 ms: 1.01x slower                                          |
| genshi_text              | 22.1 ms                                                                | 22.4 ms: 1.02x slower                                         |
| dulwich_log              | 63.8 ms                                                                | 64.8 ms: 1.02x slower                                         |
| json_loads               | 26.4 us                                                                | 27.0 us: 1.02x slower                                         |
| thrift                   | 761 us                                                                 | 779 us: 1.02x slower                                          |
| spectral_norm            | 104 ms                                                                 | 107 ms: 1.03x slower                                          |
| generators               | 27.1 ms                                                                | 27.9 ms: 1.03x slower                                         |
| mdp                      | 2.53 sec                                                               | 2.62 sec: 1.03x slower                                        |
| gc_traversal             | 4.71 ms                                                                | 4.94 ms: 1.05x slower                                         |
| Geometric mean           | (ref)                                                                  | 1.00x faster                                                  |

Benchmark hidden because not significant (38): async_tree_none, async_tree_none_tg, pathlib, k_core, async_tree_io, richards_super, subparsers, sympy_str, deepcopy, async_tree_cpu_io_mixed, mypy2, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, xml_etree_parse, pylint, chaos, scimark_monte_carlo, unpickle_pure_python, float, docutils, sympy_sum, pickle_pure_python, genshi_xml, many_optionals, async_tree_io_tg, coverage, bench_thread_pool, sphinx, asyncio_websockets, sqlglot_optimize, async_tree_memoization, comprehensions, html5lib, bench_mp_pool, nbody, logging_format, pycparser, shortest_path

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 93.52% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x