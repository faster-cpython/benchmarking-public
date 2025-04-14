# Results vs. base

- fork: brandtbucher
- ref: jit_cached_consts
- machine: linux-x86_64
- commit hash: 32ebfed
- commit date: 2025-03-19
- overall geometric mean: 1.005x faster
- HPT reliability: 97.75%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250317-linux-x86_64-python-fd545d735d5f9c048f99-3.14.0a6+-fd545d7 | bm-20250319-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-32ebfed |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 263 ms                                                                 | 262 ms: 1.00x faster                                                      |
| docutils       | 2.68 sec                                                               | 2.69 sec: 1.00x slower                                                    |
| html5lib       | 62.2 ms                                                                | 63.3 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250317-linux-x86_64-python-fd545d735d5f9c048f99-3.14.0a6+-fd545d7 | bm-20250319-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-32ebfed |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 481 ms                                                                 | 478 ms: 1.01x faster                                                      |
| coroutines                 | 23.7 ms                                                                | 23.8 ms: 1.00x slower                                                     |
| async_generators           | 417 ms                                                                 | 421 ms: 1.01x slower                                                      |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (8): async_tree_memoization_tg, asyncio_websockets, async_tree_cpu_io_mixed, async_tree_none, async_tree_memoization, async_tree_none_tg, async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250317-linux-x86_64-python-fd545d735d5f9c048f99-3.14.0a6+-fd545d7 | bm-20250319-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-32ebfed |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (2): nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250317-linux-x86_64-python-fd545d735d5f9c048f99-3.14.0a6+-fd545d7 | bm-20250319-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-32ebfed |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 23.9 ms                                                                | 23.2 ms: 1.03x faster                                                     |
| regex_dna      | 225 ms                                                                 | 221 ms: 1.02x faster                                                      |
| regex_effbot   | 3.48 ms                                                                | 3.45 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250317-linux-x86_64-python-fd545d735d5f9c048f99-3.14.0a6+-fd545d7 | bm-20250319-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-32ebfed |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 11.8 ms                                                                | 11.5 ms: 1.02x faster                                                     |
| pickle_pure_python   | 326 us                                                                 | 321 us: 1.02x faster                                                      |
| xml_etree_generate   | 80.4 ms                                                                | 79.3 ms: 1.01x faster                                                     |
| unpickle_pure_python | 216 us                                                                 | 213 us: 1.01x faster                                                      |
| xml_etree_parse      | 142 ms                                                                 | 140 ms: 1.01x faster                                                      |
| json_loads           | 30.2 us                                                                | 29.8 us: 1.01x faster                                                     |
| xml_etree_process    | 56.2 ms                                                                | 55.5 ms: 1.01x faster                                                     |
| xml_etree_iterparse  | 98.7 ms                                                                | 97.7 ms: 1.01x faster                                                     |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250317-linux-x86_64-python-fd545d735d5f9c048f99-3.14.0a6+-fd545d7 | bm-20250319-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-32ebfed |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 8.22 ms                                                                | 8.20 ms: 1.00x faster                                                     |
| python_startup         | 13.1 ms                                                                | 13.1 ms: 1.00x faster                                                     |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250317-linux-x86_64-python-fd545d735d5f9c048f99-3.14.0a6+-fd545d7 | bm-20250319-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-32ebfed |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 21.6 ms                                                                | 21.0 ms: 1.03x faster                                                     |
| genshi_xml      | 51.0 ms                                                                | 49.9 ms: 1.02x faster                                                     |
| mako            | 11.1 ms                                                                | 10.9 ms: 1.02x faster                                                     |
| django_template | 31.9 ms                                                                | 31.6 ms: 1.01x faster                                                     |
| Geometric mean  | (ref)                                                                  | 1.02x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20250317-linux-x86_64-python-fd545d735d5f9c048f99-3.14.0a6+-fd545d7 | bm-20250319-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-32ebfed |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| scimark_sor                | 121 ms                                                                 | 117 ms: 1.03x faster                                                      |
| regex_v8                   | 23.9 ms                                                                | 23.2 ms: 1.03x faster                                                     |
| genshi_text                | 21.6 ms                                                                | 21.0 ms: 1.03x faster                                                     |
| scimark_lu                 | 121 ms                                                                 | 118 ms: 1.03x faster                                                      |
| deltablue                  | 3.08 ms                                                                | 3.01 ms: 1.02x faster                                                     |
| nqueens                    | 85.9 ms                                                                | 84.1 ms: 1.02x faster                                                     |
| genshi_xml                 | 51.0 ms                                                                | 49.9 ms: 1.02x faster                                                     |
| sqlite_synth               | 2.75 us                                                                | 2.69 us: 1.02x faster                                                     |
| json_dumps                 | 11.8 ms                                                                | 11.5 ms: 1.02x faster                                                     |
| deepcopy_memo              | 30.0 us                                                                | 29.4 us: 1.02x faster                                                     |
| richards                   | 35.6 ms                                                                | 34.9 ms: 1.02x faster                                                     |
| logging_silent             | 100 ns                                                                 | 98.1 ns: 1.02x faster                                                     |
| generators                 | 28.3 ms                                                                | 27.8 ms: 1.02x faster                                                     |
| regex_dna                  | 225 ms                                                                 | 221 ms: 1.02x faster                                                      |
| mako                       | 11.1 ms                                                                | 10.9 ms: 1.02x faster                                                     |
| scimark_monte_carlo        | 68.9 ms                                                                | 67.6 ms: 1.02x faster                                                     |
| pickle_pure_python         | 326 us                                                                 | 321 us: 1.02x faster                                                      |
| hexiom                     | 6.90 ms                                                                | 6.79 ms: 1.02x faster                                                     |
| xml_etree_generate         | 80.4 ms                                                                | 79.3 ms: 1.01x faster                                                     |
| unpickle_pure_python       | 216 us                                                                 | 213 us: 1.01x faster                                                      |
| xml_etree_parse            | 142 ms                                                                 | 140 ms: 1.01x faster                                                      |
| chaos                      | 60.2 ms                                                                | 59.4 ms: 1.01x faster                                                     |
| json                       | 5.36 ms                                                                | 5.29 ms: 1.01x faster                                                     |
| json_loads                 | 30.2 us                                                                | 29.8 us: 1.01x faster                                                     |
| xml_etree_process          | 56.2 ms                                                                | 55.5 ms: 1.01x faster                                                     |
| raytrace                   | 270 ms                                                                 | 266 ms: 1.01x faster                                                      |
| richards_super             | 40.8 ms                                                                | 40.3 ms: 1.01x faster                                                     |
| sqlalchemy_imperative      | 17.1 ms                                                                | 16.9 ms: 1.01x faster                                                     |
| logging_simple             | 5.59 us                                                                | 5.53 us: 1.01x faster                                                     |
| mdp                        | 2.50 sec                                                               | 2.48 sec: 1.01x faster                                                    |
| xml_etree_iterparse        | 98.7 ms                                                                | 97.7 ms: 1.01x faster                                                     |
| django_template            | 31.9 ms                                                                | 31.6 ms: 1.01x faster                                                     |
| async_tree_cpu_io_mixed_tg | 481 ms                                                                 | 478 ms: 1.01x faster                                                      |
| regex_effbot               | 3.48 ms                                                                | 3.45 ms: 1.01x faster                                                     |
| sqlglot_v2_parse           | 1.30 ms                                                                | 1.29 ms: 1.01x faster                                                     |
| pyflate                    | 447 ms                                                                 | 444 ms: 1.01x faster                                                      |
| gc_traversal               | 4.85 ms                                                                | 4.83 ms: 1.01x faster                                                     |
| bench_mp_pool              | 83.2 ms                                                                | 82.8 ms: 1.01x faster                                                     |
| sqlglot_v2_optimize        | 54.2 ms                                                                | 54.0 ms: 1.00x faster                                                     |
| sqlglot_v2_normalize       | 109 ms                                                                 | 108 ms: 1.00x faster                                                      |
| python_startup_no_site     | 8.22 ms                                                                | 8.20 ms: 1.00x faster                                                     |
| 2to3                       | 263 ms                                                                 | 262 ms: 1.00x faster                                                      |
| python_startup             | 13.1 ms                                                                | 13.1 ms: 1.00x faster                                                     |
| bench_thread_pool          | 883 us                                                                 | 882 us: 1.00x faster                                                      |
| pidigits                   | 186 ms                                                                 | 186 ms: 1.00x slower                                                      |
| docutils                   | 2.68 sec                                                               | 2.69 sec: 1.00x slower                                                    |
| sqlalchemy_declarative     | 133 ms                                                                 | 133 ms: 1.00x slower                                                      |
| create_gc_cycles           | 2.49 ms                                                                | 2.50 ms: 1.00x slower                                                     |
| coroutines                 | 23.7 ms                                                                | 23.8 ms: 1.00x slower                                                     |
| many_optionals             | 962 us                                                                 | 968 us: 1.01x slower                                                      |
| spectral_norm              | 95.2 ms                                                                | 95.8 ms: 1.01x slower                                                     |
| thrift                     | 779 us                                                                 | 786 us: 1.01x slower                                                      |
| typing_runtime_protocols   | 170 us                                                                 | 171 us: 1.01x slower                                                      |
| async_generators           | 417 ms                                                                 | 421 ms: 1.01x slower                                                      |
| scimark_fft                | 308 ms                                                                 | 311 ms: 1.01x slower                                                      |
| dulwich_log                | 60.2 ms                                                                | 60.9 ms: 1.01x slower                                                     |
| pprint_safe_repr           | 755 ms                                                                 | 767 ms: 1.02x slower                                                      |
| html5lib                   | 62.2 ms                                                                | 63.3 ms: 1.02x slower                                                     |
| deepcopy_reduce            | 2.71 us                                                                | 2.75 us: 1.02x slower                                                     |
| scimark_sparse_mat_mult    | 4.76 ms                                                                | 4.86 ms: 1.02x slower                                                     |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (32): nbody, crypto_pyaes, pycparser, sqlglot_v2_transpile, go, meteor_contest, pathlib, async_tree_memoization_tg, comprehensions, logging_format, sphinx, pylint, tomli_loads, deepcopy, asyncio_websockets, async_tree_cpu_io_mixed, regex_compile, async_tree_none, shortest_path, fannkuch, async_tree_memoization, async_tree_none_tg, subparsers, float, connected_components, async_tree_io_tg, bpe_tokeniser, coverage, telco, pprint_pformat, k_core, async_tree_io
Ignored benchmarks (4) of results/bm-20250317-3.14.0a6+-fd545d7-JIT/bm-20250317-linux-x86_64-python-fd545d735d5f9c048f99-3.14.0a6+-fd545d7.json: sympy_expand, sympy_integrate, sympy_str, sympy_sum

- Geometric mean (including insignificant results): 1.005x faster

# HPT report

- Reliability score: 97.75% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x