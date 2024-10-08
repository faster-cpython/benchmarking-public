# Results vs. base

- fork: mdboom
- ref: remove_redundant_typ
- machine: windows-amd64
- commit hash: b0f5f3a
- commit date: 2024-09-23
- overall geometric mean: 1.00x slower
- HPT reliability: 68.79%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 | bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 222 ms                                                                     | 224 ms: 1.01x slower                                                       |
| docutils       | 1.71 sec                                                                   | 1.69 sec: 1.01x faster                                                     |
| html5lib       | 40.5 ms                                                                    | 40.1 ms: 1.01x faster                                                      |
| tornado_http   | 83.1 ms                                                                    | 84.2 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                      | 1.00x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 | bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_generators           | 243 ms                                                                     | 241 ms: 1.01x faster                                                       |
| async_tree_memoization     | 261 ms                                                                     | 265 ms: 1.01x slower                                                       |
| async_tree_cpu_io_mixed_tg | 388 ms                                                                     | 397 ms: 1.02x slower                                                       |
| asyncio_tcp_ssl            | 1.48 sec                                                                   | 1.62 sec: 1.09x slower                                                     |
| Geometric mean             | (ref)                                                                      | 1.02x slower                                                               |

Benchmark hidden because not significant (8): coroutines, asyncio_tcp, async_tree_io, async_tree_cpu_io_mixed, async_tree_none, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 | bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 83.2 ms                                                                    | 81.8 ms: 1.02x faster                                                      |
| float          | 55.2 ms                                                                    | 55.8 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                      | 1.00x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 | bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.57 ms                                                                    | 1.55 ms: 1.01x faster                                                      |
| regex_dna      | 118 ms                                                                     | 117 ms: 1.01x faster                                                       |
| regex_compile  | 90.4 ms                                                                    | 91.4 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                      | 1.00x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 | bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 6.35 ms                                                                    | 6.23 ms: 1.02x faster                                                      |
| xml_etree_process    | 40.9 ms                                                                    | 40.3 ms: 1.01x faster                                                      |
| json_loads           | 14.8 us                                                                    | 14.6 us: 1.01x faster                                                      |
| xml_etree_generate   | 57.7 ms                                                                    | 57.3 ms: 1.01x faster                                                      |
| unpickle_pure_python | 149 us                                                                     | 149 us: 1.01x faster                                                       |
| pickle_pure_python   | 212 us                                                                     | 213 us: 1.01x slower                                                       |
| xml_etree_iterparse  | 63.9 ms                                                                    | 64.6 ms: 1.01x slower                                                      |
| xml_etree_parse      | 92.5 ms                                                                    | 93.8 ms: 1.01x slower                                                      |
| pickle               | 7.04 us                                                                    | 7.31 us: 1.04x slower                                                      |
| Geometric mean       | (ref)                                                                      | 1.00x slower                                                               |

Benchmark hidden because not significant (5): unpickle, unpickle_list, pickle_dict, tomli_loads, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 | bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|------------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 18.4 ms                                                                    | 18.0 ms: 1.03x faster                                                      |
| python_startup         | 22.2 ms                                                                    | 21.9 ms: 1.02x faster                                                      |
| Geometric mean         | (ref)                                                                      | 1.02x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 | bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|-----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 17.0 ms                                                                    | 17.5 ms: 1.03x slower                                                      |
| django_template | 24.8 ms                                                                    | 25.7 ms: 1.03x slower                                                      |
| genshi_xml      | 35.4 ms                                                                    | 37.5 ms: 1.06x slower                                                      |
| Geometric mean  | (ref)                                                                      | 1.03x slower                                                               |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 | bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| coverage                   | 49.3 ms                                                                    | 46.3 ms: 1.07x faster                                                      |
| nqueens                    | 65.5 ms                                                                    | 63.8 ms: 1.03x faster                                                      |
| python_startup_no_site     | 18.4 ms                                                                    | 18.0 ms: 1.03x faster                                                      |
| scimark_sparse_mat_mult    | 2.66 ms                                                                    | 2.60 ms: 1.03x faster                                                      |
| richards_super             | 36.4 ms                                                                    | 35.6 ms: 1.02x faster                                                      |
| fannkuch                   | 299 ms                                                                     | 293 ms: 1.02x faster                                                       |
| scimark_lu                 | 62.5 ms                                                                    | 61.3 ms: 1.02x faster                                                      |
| json_dumps                 | 6.35 ms                                                                    | 6.23 ms: 1.02x faster                                                      |
| nbody                      | 83.2 ms                                                                    | 81.8 ms: 1.02x faster                                                      |
| python_startup             | 22.2 ms                                                                    | 21.9 ms: 1.02x faster                                                      |
| xml_etree_process          | 40.9 ms                                                                    | 40.3 ms: 1.01x faster                                                      |
| logging_silent             | 63.8 ns                                                                    | 63.0 ns: 1.01x faster                                                      |
| pprint_pformat             | 1.12 sec                                                                   | 1.10 sec: 1.01x faster                                                     |
| json_loads                 | 14.8 us                                                                    | 14.6 us: 1.01x faster                                                      |
| mdp                        | 1.44 sec                                                                   | 1.43 sec: 1.01x faster                                                     |
| sqlglot_normalize          | 193 ms                                                                     | 191 ms: 1.01x faster                                                       |
| html5lib                   | 40.5 ms                                                                    | 40.1 ms: 1.01x faster                                                      |
| dulwich_log                | 42.8 ms                                                                    | 42.4 ms: 1.01x faster                                                      |
| spectral_norm              | 69.8 ms                                                                    | 69.0 ms: 1.01x faster                                                      |
| meteor_contest             | 78.6 ms                                                                    | 77.8 ms: 1.01x faster                                                      |
| regex_effbot               | 1.57 ms                                                                    | 1.55 ms: 1.01x faster                                                      |
| docutils                   | 1.71 sec                                                                   | 1.69 sec: 1.01x faster                                                     |
| scimark_sor                | 93.1 ms                                                                    | 92.2 ms: 1.01x faster                                                      |
| xml_etree_generate         | 57.7 ms                                                                    | 57.3 ms: 1.01x faster                                                      |
| richards                   | 32.3 ms                                                                    | 32.0 ms: 1.01x faster                                                      |
| async_generators           | 243 ms                                                                     | 241 ms: 1.01x faster                                                       |
| thrift                     | 523 us                                                                     | 519 us: 1.01x faster                                                       |
| telco                      | 5.09 ms                                                                    | 5.05 ms: 1.01x faster                                                      |
| regex_dna                  | 118 ms                                                                     | 117 ms: 1.01x faster                                                       |
| scimark_fft                | 204 ms                                                                     | 203 ms: 1.01x faster                                                       |
| unpickle_pure_python       | 149 us                                                                     | 149 us: 1.01x faster                                                       |
| deepcopy                   | 193 us                                                                     | 192 us: 1.01x faster                                                       |
| deltablue                  | 2.28 ms                                                                    | 2.27 ms: 1.00x faster                                                      |
| pathlib                    | 75.9 ms                                                                    | 75.6 ms: 1.00x faster                                                      |
| chaos                      | 42.7 ms                                                                    | 42.6 ms: 1.00x faster                                                      |
| pyflate                    | 322 ms                                                                     | 322 ms: 1.00x faster                                                       |
| sqlite_synth               | 1.63 us                                                                    | 1.64 us: 1.01x slower                                                      |
| sqlglot_parse              | 888 us                                                                     | 895 us: 1.01x slower                                                       |
| hexiom                     | 4.39 ms                                                                    | 4.42 ms: 1.01x slower                                                      |
| crypto_pyaes               | 47.8 ms                                                                    | 48.1 ms: 1.01x slower                                                      |
| pickle_pure_python         | 212 us                                                                     | 213 us: 1.01x slower                                                       |
| logging_format             | 6.85 us                                                                    | 6.91 us: 1.01x slower                                                      |
| generators                 | 21.0 ms                                                                    | 21.2 ms: 1.01x slower                                                      |
| 2to3                       | 222 ms                                                                     | 224 ms: 1.01x slower                                                       |
| deepcopy_reduce            | 1.94 us                                                                    | 1.96 us: 1.01x slower                                                      |
| xml_etree_iterparse        | 63.9 ms                                                                    | 64.6 ms: 1.01x slower                                                      |
| regex_compile              | 90.4 ms                                                                    | 91.4 ms: 1.01x slower                                                      |
| float                      | 55.2 ms                                                                    | 55.8 ms: 1.01x slower                                                      |
| comprehensions             | 11.9 us                                                                    | 12.0 us: 1.01x slower                                                      |
| tornado_http               | 83.1 ms                                                                    | 84.2 ms: 1.01x slower                                                      |
| xml_etree_parse            | 92.5 ms                                                                    | 93.8 ms: 1.01x slower                                                      |
| async_tree_memoization     | 261 ms                                                                     | 265 ms: 1.01x slower                                                       |
| logging_simple             | 6.35 us                                                                    | 6.46 us: 1.02x slower                                                      |
| async_tree_cpu_io_mixed_tg | 388 ms                                                                     | 397 ms: 1.02x slower                                                       |
| raytrace                   | 189 ms                                                                     | 194 ms: 1.02x slower                                                       |
| genshi_text                | 17.0 ms                                                                    | 17.5 ms: 1.03x slower                                                      |
| django_template            | 24.8 ms                                                                    | 25.7 ms: 1.03x slower                                                      |
| pickle                     | 7.04 us                                                                    | 7.31 us: 1.04x slower                                                      |
| genshi_xml                 | 35.4 ms                                                                    | 37.5 ms: 1.06x slower                                                      |
| asyncio_tcp_ssl            | 1.48 sec                                                                   | 1.62 sec: 1.09x slower                                                     |
| unpack_sequence            | 40.3 ns                                                                    | 46.4 ns: 1.15x slower                                                      |
| Geometric mean             | (ref)                                                                      | 1.00x slower                                                               |

Benchmark hidden because not significant (34): json, pycparser, unpickle, mako, create_gc_cycles, pidigits, scimark_monte_carlo, sqlglot_optimize, unpickle_list, sympy_expand, sympy_integrate, go, pickle_dict, pprint_safe_repr, coroutines, sqlglot_transpile, sympy_sum, deepcopy_memo, gc_traversal, pylint, sympy_str, bench_mp_pool, tomli_loads, bench_thread_pool, typing_runtime_protocols, regex_v8, asyncio_tcp, async_tree_io, async_tree_cpu_io_mixed, async_tree_none, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, pickle_list

# HPT report

- Reliability score: 68.79% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown