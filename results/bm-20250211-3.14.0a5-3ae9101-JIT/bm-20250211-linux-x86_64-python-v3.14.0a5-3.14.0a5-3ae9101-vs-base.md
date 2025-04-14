# Results vs. base

- fork: python
- ref: v3.14.0a5
- machine: linux-x86_64
- commit hash: 3ae9101
- commit date: 2025-02-11
- overall geometric mean: 1.002x slower
- HPT reliability: 75.22%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250212-linux-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 | bm-20250211-linux-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 258 ms                                                                 | 257 ms: 1.00x faster                                       |
| docutils       | 2.67 sec                                                               | 2.66 sec: 1.00x faster                                     |
| html5lib       | 61.9 ms                                                                | 60.6 ms: 1.02x faster                                      |
| Geometric mean | (ref)                                                                  | 1.01x faster                                               |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250212-linux-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 | bm-20250211-linux-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------:|
| async_generators           | 413 ms                                                                 | 408 ms: 1.01x faster                                       |
| async_tree_cpu_io_mixed_tg | 485 ms                                                                 | 493 ms: 1.02x slower                                       |
| async_tree_cpu_io_mixed    | 493 ms                                                                 | 503 ms: 1.02x slower                                       |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                               |

Benchmark hidden because not significant (8): async_tree_io, coroutines, async_tree_io_tg, async_tree_memoization_tg, async_tree_memoization, asyncio_websockets, async_tree_none, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250212-linux-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 | bm-20250211-linux-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 70.5 ms                                                                | 69.1 ms: 1.02x faster                                      |
| pidigits       | 188 ms                                                                 | 188 ms: 1.00x slower                                       |
| nbody          | 93.5 ms                                                                | 97.7 ms: 1.04x slower                                      |
| Geometric mean | (ref)                                                                  | 1.01x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250212-linux-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 | bm-20250211-linux-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------:|
| regex_v8       | 23.9 ms                                                                | 23.5 ms: 1.01x faster                                      |
| regex_compile  | 126 ms                                                                 | 125 ms: 1.01x faster                                       |
| regex_dna      | 207 ms                                                                 | 206 ms: 1.00x faster                                       |
| regex_effbot   | 3.16 ms                                                                | 3.20 ms: 1.01x slower                                      |
| Geometric mean | (ref)                                                                  | 1.00x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250212-linux-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 | bm-20250211-linux-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|--------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------:|
| json_dumps         | 11.9 ms                                                                | 11.7 ms: 1.01x faster                                      |
| json_loads         | 29.0 us                                                                | 28.8 us: 1.01x faster                                      |
| xml_etree_generate | 78.3 ms                                                                | 78.7 ms: 1.01x slower                                      |
| xml_etree_parse    | 138 ms                                                                 | 139 ms: 1.01x slower                                       |
| tomli_loads        | 1.84 sec                                                               | 1.86 sec: 1.01x slower                                     |
| Geometric mean     | (ref)                                                                  | 1.00x slower                                               |

Benchmark hidden because not significant (4): xml_etree_iterparse, unpickle_pure_python, xml_etree_process, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250212-linux-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 | bm-20250211-linux-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup_no_site | 7.08 ms                                                                | 7.05 ms: 1.00x faster                                      |
| python_startup         | 12.9 ms                                                                | 12.8 ms: 1.00x faster                                      |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250212-linux-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 | bm-20250211-linux-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------:|
| django_template | 31.7 ms                                                                | 31.5 ms: 1.01x faster                                      |
| genshi_xml      | 49.4 ms                                                                | 50.5 ms: 1.02x slower                                      |
| mako            | 10.1 ms                                                                | 10.5 ms: 1.04x slower                                      |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                               |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20250212-linux-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 | bm-20250211-linux-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------:|
| pyflate                    | 457 ms                                                                 | 441 ms: 1.04x faster                                       |
| scimark_sparse_mat_mult    | 4.48 ms                                                                | 4.34 ms: 1.03x faster                                      |
| logging_silent             | 106 ns                                                                 | 103 ns: 1.02x faster                                       |
| html5lib                   | 61.9 ms                                                                | 60.6 ms: 1.02x faster                                      |
| float                      | 70.5 ms                                                                | 69.1 ms: 1.02x faster                                      |
| gc_traversal               | 4.95 ms                                                                | 4.87 ms: 1.02x faster                                      |
| crypto_pyaes               | 70.7 ms                                                                | 69.5 ms: 1.02x faster                                      |
| regex_v8                   | 23.9 ms                                                                | 23.5 ms: 1.01x faster                                      |
| json_dumps                 | 11.9 ms                                                                | 11.7 ms: 1.01x faster                                      |
| async_generators           | 413 ms                                                                 | 408 ms: 1.01x faster                                       |
| mdp                        | 2.57 sec                                                               | 2.54 sec: 1.01x faster                                     |
| sqlite_synth               | 2.77 us                                                                | 2.74 us: 1.01x faster                                      |
| logging_simple             | 5.56 us                                                                | 5.50 us: 1.01x faster                                      |
| sqlglot_transpile          | 1.60 ms                                                                | 1.58 ms: 1.01x faster                                      |
| typing_runtime_protocols   | 164 us                                                                 | 162 us: 1.01x faster                                       |
| go                         | 131 ms                                                                 | 129 ms: 1.01x faster                                       |
| many_optionals             | 958 us                                                                 | 948 us: 1.01x faster                                       |
| regex_compile              | 126 ms                                                                 | 125 ms: 1.01x faster                                       |
| json_loads                 | 29.0 us                                                                | 28.8 us: 1.01x faster                                      |
| logging_format             | 6.12 us                                                                | 6.08 us: 1.01x faster                                      |
| bpe_tokeniser              | 4.39 sec                                                               | 4.36 sec: 1.01x faster                                     |
| sqlglot_parse              | 1.28 ms                                                                | 1.27 ms: 1.01x faster                                      |
| django_template            | 31.7 ms                                                                | 31.5 ms: 1.01x faster                                      |
| thrift                     | 763 us                                                                 | 759 us: 1.01x faster                                       |
| deepcopy_memo              | 30.7 us                                                                | 30.5 us: 1.01x faster                                      |
| regex_dna                  | 207 ms                                                                 | 206 ms: 1.00x faster                                       |
| docutils                   | 2.67 sec                                                               | 2.66 sec: 1.00x faster                                     |
| sqlalchemy_declarative     | 131 ms                                                                 | 131 ms: 1.00x faster                                       |
| python_startup_no_site     | 7.08 ms                                                                | 7.05 ms: 1.00x faster                                      |
| create_gc_cycles           | 2.47 ms                                                                | 2.47 ms: 1.00x faster                                      |
| sympy_expand               | 470 ms                                                                 | 469 ms: 1.00x faster                                       |
| 2to3                       | 258 ms                                                                 | 257 ms: 1.00x faster                                       |
| python_startup             | 12.9 ms                                                                | 12.8 ms: 1.00x faster                                      |
| pidigits                   | 188 ms                                                                 | 188 ms: 1.00x slower                                       |
| hexiom                     | 6.93 ms                                                                | 6.96 ms: 1.00x slower                                      |
| chaos                      | 58.4 ms                                                                | 58.7 ms: 1.00x slower                                      |
| dulwich_log                | 66.1 ms                                                                | 66.4 ms: 1.00x slower                                      |
| sympy_sum                  | 151 ms                                                                 | 152 ms: 1.01x slower                                       |
| xml_etree_generate         | 78.3 ms                                                                | 78.7 ms: 1.01x slower                                      |
| scimark_lu                 | 117 ms                                                                 | 118 ms: 1.01x slower                                       |
| xml_etree_parse            | 138 ms                                                                 | 139 ms: 1.01x slower                                       |
| telco                      | 7.59 ms                                                                | 7.67 ms: 1.01x slower                                      |
| tomli_loads                | 1.84 sec                                                               | 1.86 sec: 1.01x slower                                     |
| spectral_norm              | 95.7 ms                                                                | 96.7 ms: 1.01x slower                                      |
| regex_effbot               | 3.16 ms                                                                | 3.20 ms: 1.01x slower                                      |
| meteor_contest             | 107 ms                                                                 | 109 ms: 1.01x slower                                       |
| raytrace                   | 275 ms                                                                 | 279 ms: 1.01x slower                                       |
| scimark_sor                | 120 ms                                                                 | 122 ms: 1.01x slower                                       |
| scimark_monte_carlo        | 65.8 ms                                                                | 66.7 ms: 1.01x slower                                      |
| scimark_fft                | 312 ms                                                                 | 317 ms: 1.02x slower                                       |
| async_tree_cpu_io_mixed_tg | 485 ms                                                                 | 493 ms: 1.02x slower                                       |
| pprint_safe_repr           | 751 ms                                                                 | 764 ms: 1.02x slower                                       |
| async_tree_cpu_io_mixed    | 493 ms                                                                 | 503 ms: 1.02x slower                                       |
| genshi_xml                 | 49.4 ms                                                                | 50.5 ms: 1.02x slower                                      |
| richards_super             | 49.8 ms                                                                | 51.3 ms: 1.03x slower                                      |
| pprint_pformat             | 1.50 sec                                                               | 1.56 sec: 1.04x slower                                     |
| richards                   | 43.4 ms                                                                | 45.0 ms: 1.04x slower                                      |
| mako                       | 10.1 ms                                                                | 10.5 ms: 1.04x slower                                      |
| nbody                      | 93.5 ms                                                                | 97.7 ms: 1.04x slower                                      |
| generators                 | 27.7 ms                                                                | 28.9 ms: 1.04x slower                                      |
| coverage                   | 89.8 ms                                                                | 96.8 ms: 1.08x slower                                      |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                               |

Benchmark hidden because not significant (35): nqueens, deepcopy_reduce, sphinx, pylint, async_tree_io, coroutines, subparsers, sqlalchemy_imperative, json, k_core, xml_etree_iterparse, async_tree_io_tg, bench_mp_pool, connected_components, bench_thread_pool, unpickle_pure_python, sqlglot_normalize, async_tree_memoization_tg, shortest_path, async_tree_memoization, sqlglot_optimize, sympy_str, deepcopy, fannkuch, comprehensions, sympy_integrate, xml_etree_process, asyncio_websockets, deltablue, pathlib, async_tree_none, genshi_text, async_tree_none_tg, pycparser, pickle_pure_python

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 75.22% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x