# Results vs. base

- fork: mdboom
- ref: remove_redundant_typ
- machine: linux-x86_64
- commit hash: b0f5f3a
- commit date: 2024-09-23
- overall geometric mean: 1.00x slower
- HPT reliability: 99.89%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240924-linux-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 | bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 254 ms                                                                | 255 ms: 1.00x slower                                                  |
| docutils       | 2.65 sec                                                              | 2.63 sec: 1.01x faster                                                |
| html5lib       | 63.7 ms                                                               | 61.5 ms: 1.04x faster                                                 |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240924-linux-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 | bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| coroutines       | 23.2 ms                                                               | 22.8 ms: 1.02x faster                                                 |
| async_generators | 434 ms                                                                | 430 ms: 1.01x faster                                                  |
| asyncio_tcp_ssl  | 1.79 sec                                                              | 1.78 sec: 1.00x faster                                                |
| asyncio_tcp      | 474 ms                                                                | 477 ms: 1.01x slower                                                  |
| Geometric mean   | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (9): async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_memoization_tg, async_tree_io_tg, async_tree_io, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240924-linux-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 | bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 76.0 ms                                                               | 75.6 ms: 1.00x faster                                                 |
| pidigits       | 186 ms                                                                | 187 ms: 1.00x slower                                                  |
| nbody          | 84.6 ms                                                               | 86.7 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240924-linux-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 | bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 25.0 ms                                                               | 25.1 ms: 1.00x slower                                                 |
| regex_compile  | 127 ms                                                                | 128 ms: 1.00x slower                                                  |
| regex_dna      | 220 ms                                                                | 225 ms: 1.02x slower                                                  |
| regex_effbot   | 3.70 ms                                                               | 3.89 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240924-linux-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 | bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle             | 17.4 us                                                               | 15.5 us: 1.12x faster                                                 |
| pickle_list          | 5.12 us                                                               | 4.98 us: 1.03x faster                                                 |
| pickle_dict          | 33.5 us                                                               | 32.7 us: 1.02x faster                                                 |
| unpickle_list        | 5.24 us                                                               | 5.15 us: 1.02x faster                                                 |
| json_loads           | 27.1 us                                                               | 26.7 us: 1.02x faster                                                 |
| json_dumps           | 10.3 ms                                                               | 10.3 ms: 1.01x faster                                                 |
| xml_etree_process    | 58.4 ms                                                               | 58.6 ms: 1.00x slower                                                 |
| xml_etree_generate   | 84.2 ms                                                               | 84.8 ms: 1.01x slower                                                 |
| pickle               | 11.7 us                                                               | 11.8 us: 1.01x slower                                                 |
| pickle_pure_python   | 301 us                                                                | 305 us: 1.01x slower                                                  |
| unpickle_pure_python | 212 us                                                                | 216 us: 1.02x slower                                                  |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                          |

Benchmark hidden because not significant (3): xml_etree_iterparse, xml_etree_parse, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240924-linux-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 | bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 7.03 ms                                                               | 7.00 ms: 1.00x faster                                                 |
| python_startup         | 10.6 ms                                                               | 10.5 ms: 1.00x faster                                                 |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240924-linux-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 | bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.3 ms                                                               | 11.1 ms: 1.02x faster                                                 |
| genshi_xml      | 49.6 ms                                                               | 48.6 ms: 1.02x faster                                                 |
| django_template | 34.0 ms                                                               | 34.2 ms: 1.00x slower                                                 |
| genshi_text     | 21.5 ms                                                               | 22.1 ms: 1.02x slower                                                 |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20240924-linux-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 | bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle                 | 17.4 us                                                               | 15.5 us: 1.12x faster                                                 |
| coverage                 | 89.1 ms                                                               | 83.7 ms: 1.06x faster                                                 |
| html5lib                 | 63.7 ms                                                               | 61.5 ms: 1.04x faster                                                 |
| json                     | 5.11 ms                                                               | 4.94 ms: 1.03x faster                                                 |
| pickle_list              | 5.12 us                                                               | 4.98 us: 1.03x faster                                                 |
| richards                 | 46.5 ms                                                               | 45.4 ms: 1.02x faster                                                 |
| pickle_dict              | 33.5 us                                                               | 32.7 us: 1.02x faster                                                 |
| mako                     | 11.3 ms                                                               | 11.1 ms: 1.02x faster                                                 |
| genshi_xml               | 49.6 ms                                                               | 48.6 ms: 1.02x faster                                                 |
| pathlib                  | 16.3 ms                                                               | 16.0 ms: 1.02x faster                                                 |
| unpickle_list            | 5.24 us                                                               | 5.15 us: 1.02x faster                                                 |
| coroutines               | 23.2 ms                                                               | 22.8 ms: 1.02x faster                                                 |
| json_loads               | 27.1 us                                                               | 26.7 us: 1.02x faster                                                 |
| spectral_norm            | 114 ms                                                                | 112 ms: 1.01x faster                                                  |
| richards_super           | 52.2 ms                                                               | 51.6 ms: 1.01x faster                                                 |
| comprehensions           | 16.4 us                                                               | 16.2 us: 1.01x faster                                                 |
| async_generators         | 434 ms                                                                | 430 ms: 1.01x faster                                                  |
| docutils                 | 2.65 sec                                                              | 2.63 sec: 1.01x faster                                                |
| json_dumps               | 10.3 ms                                                               | 10.3 ms: 1.01x faster                                                 |
| create_gc_cycles         | 1.73 ms                                                               | 1.72 ms: 1.01x faster                                                 |
| python_startup_no_site   | 7.03 ms                                                               | 7.00 ms: 1.00x faster                                                 |
| float                    | 76.0 ms                                                               | 75.6 ms: 1.00x faster                                                 |
| python_startup           | 10.6 ms                                                               | 10.5 ms: 1.00x faster                                                 |
| asyncio_tcp_ssl          | 1.79 sec                                                              | 1.78 sec: 1.00x faster                                                |
| pidigits                 | 186 ms                                                                | 187 ms: 1.00x slower                                                  |
| bench_thread_pool        | 788 us                                                                | 789 us: 1.00x slower                                                  |
| regex_v8                 | 25.0 ms                                                               | 25.1 ms: 1.00x slower                                                 |
| xml_etree_process        | 58.4 ms                                                               | 58.6 ms: 1.00x slower                                                 |
| 2to3                     | 254 ms                                                                | 255 ms: 1.00x slower                                                  |
| dulwich_log              | 64.5 ms                                                               | 64.8 ms: 1.00x slower                                                 |
| sqlglot_transpile        | 1.57 ms                                                               | 1.58 ms: 1.00x slower                                                 |
| sqlglot_optimize         | 52.9 ms                                                               | 53.1 ms: 1.00x slower                                                 |
| pprint_pformat           | 1.45 sec                                                              | 1.45 sec: 1.00x slower                                                |
| crypto_pyaes             | 71.7 ms                                                               | 72.0 ms: 1.00x slower                                                 |
| regex_compile            | 127 ms                                                                | 128 ms: 1.00x slower                                                  |
| django_template          | 34.0 ms                                                               | 34.2 ms: 1.00x slower                                                 |
| deepcopy                 | 254 us                                                                | 255 us: 1.01x slower                                                  |
| sympy_expand             | 450 ms                                                                | 453 ms: 1.01x slower                                                  |
| asyncio_tcp              | 474 ms                                                                | 477 ms: 1.01x slower                                                  |
| sqlglot_normalize        | 105 ms                                                                | 106 ms: 1.01x slower                                                  |
| thrift                   | 772 us                                                                | 777 us: 1.01x slower                                                  |
| xml_etree_generate       | 84.2 ms                                                               | 84.8 ms: 1.01x slower                                                 |
| fannkuch                 | 401 ms                                                                | 404 ms: 1.01x slower                                                  |
| meteor_contest           | 106 ms                                                                | 107 ms: 1.01x slower                                                  |
| typing_runtime_protocols | 158 us                                                                | 159 us: 1.01x slower                                                  |
| sympy_integrate          | 19.4 ms                                                               | 19.6 ms: 1.01x slower                                                 |
| hexiom                   | 6.13 ms                                                               | 6.19 ms: 1.01x slower                                                 |
| pickle                   | 11.7 us                                                               | 11.8 us: 1.01x slower                                                 |
| go                       | 118 ms                                                                | 119 ms: 1.01x slower                                                  |
| telco                    | 8.33 ms                                                               | 8.43 ms: 1.01x slower                                                 |
| pyflate                  | 468 ms                                                                | 473 ms: 1.01x slower                                                  |
| pickle_pure_python       | 301 us                                                                | 305 us: 1.01x slower                                                  |
| deepcopy_memo            | 29.5 us                                                               | 29.9 us: 1.01x slower                                                 |
| chaos                    | 57.9 ms                                                               | 58.6 ms: 1.01x slower                                                 |
| scimark_sparse_mat_mult  | 4.89 ms                                                               | 4.95 ms: 1.01x slower                                                 |
| generators               | 27.8 ms                                                               | 28.2 ms: 1.01x slower                                                 |
| scimark_monte_carlo      | 67.1 ms                                                               | 68.2 ms: 1.02x slower                                                 |
| raytrace                 | 260 ms                                                                | 264 ms: 1.02x slower                                                  |
| unpickle_pure_python     | 212 us                                                                | 216 us: 1.02x slower                                                  |
| regex_dna                | 220 ms                                                                | 225 ms: 1.02x slower                                                  |
| scimark_fft              | 362 ms                                                                | 370 ms: 1.02x slower                                                  |
| deltablue                | 3.18 ms                                                               | 3.25 ms: 1.02x slower                                                 |
| genshi_text              | 21.5 ms                                                               | 22.1 ms: 1.02x slower                                                 |
| nbody                    | 84.6 ms                                                               | 86.7 ms: 1.03x slower                                                 |
| unpack_sequence          | 47.7 ns                                                               | 49.3 ns: 1.03x slower                                                 |
| logging_silent           | 102 ns                                                                | 106 ns: 1.04x slower                                                  |
| pycparser                | 1.13 sec                                                              | 1.17 sec: 1.04x slower                                                |
| regex_effbot             | 3.70 ms                                                               | 3.89 ms: 1.05x slower                                                 |
| mdp                      | 2.53 sec                                                              | 2.69 sec: 1.06x slower                                                |
| gc_traversal             | 3.55 ms                                                               | 3.83 ms: 1.08x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (27): async_tree_none_tg, xml_etree_iterparse, async_tree_cpu_io_mixed_tg, logging_format, xml_etree_parse, scimark_sor, tornado_http, scimark_lu, sympy_sum, pylint, nqueens, pprint_safe_repr, bench_mp_pool, async_tree_memoization, async_tree_cpu_io_mixed, asyncio_websockets, bpe_tokeniser, async_tree_memoization_tg, deepcopy_reduce, logging_simple, sympy_str, tomli_loads, sqlglot_parse, async_tree_io_tg, sqlite_synth, async_tree_io, async_tree_none

# HPT report

- Reliability score: 99.89% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x