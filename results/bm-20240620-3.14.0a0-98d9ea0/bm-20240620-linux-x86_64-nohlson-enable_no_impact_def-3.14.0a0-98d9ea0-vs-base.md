# Results vs. base

- fork: nohlson
- ref: enable_no_impact_def
- machine: linux-x86_64
- commit hash: 98d9ea0
- commit date: 2024-06-20
- overall geometric mean: 1.00x slower
- HPT reliability: 70.47%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240619-linux-x86_64-python-1e4815692f6c8a37a397-3.14.0a0-1e48156 | bm-20240620-linux-x86_64-nohlson-enable_no_impact_def-3.14.0a0-98d9ea0 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 265 ms                                                                | 265 ms: 1.00x slower                                                   |
| html5lib       | 66.9 ms                                                               | 67.4 ms: 1.01x slower                                                  |
| tornado_http   | 91.0 ms                                                               | 91.6 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                           |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_io_tg, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240619-linux-x86_64-python-1e4815692f6c8a37a397-3.14.0a0-1e48156 | bm-20240620-linux-x86_64-nohlson-enable_no_impact_def-3.14.0a0-98d9ea0 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 77.8 ms                                                               | 76.6 ms: 1.02x faster                                                  |
| pidigits       | 188 ms                                                                | 187 ms: 1.00x faster                                                   |
| nbody          | 90.8 ms                                                               | 91.9 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240619-linux-x86_64-python-1e4815692f6c8a37a397-3.14.0a0-1e48156 | bm-20240620-linux-x86_64-nohlson-enable_no_impact_def-3.14.0a0-98d9ea0 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.70 ms                                                               | 3.55 ms: 1.04x faster                                                  |
| regex_v8       | 25.2 ms                                                               | 24.6 ms: 1.02x faster                                                  |
| regex_dna      | 227 ms                                                                | 224 ms: 1.01x faster                                                   |
| regex_compile  | 130 ms                                                                | 132 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240619-linux-x86_64-python-1e4815692f6c8a37a397-3.14.0a0-1e48156 | bm-20240620-linux-x86_64-nohlson-enable_no_impact_def-3.14.0a0-98d9ea0 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle               | 11.7 us                                                               | 11.3 us: 1.04x faster                                                  |
| unpickle_list        | 5.55 us                                                               | 5.37 us: 1.03x faster                                                  |
| json_dumps           | 10.5 ms                                                               | 10.4 ms: 1.01x faster                                                  |
| pickle_list          | 5.17 us                                                               | 5.11 us: 1.01x faster                                                  |
| xml_etree_process    | 59.0 ms                                                               | 59.3 ms: 1.00x slower                                                  |
| pickle_pure_python   | 299 us                                                                | 301 us: 1.01x slower                                                   |
| xml_etree_generate   | 84.3 ms                                                               | 84.9 ms: 1.01x slower                                                  |
| tomli_loads          | 2.11 sec                                                              | 2.14 sec: 1.01x slower                                                 |
| unpickle_pure_python | 214 us                                                                | 217 us: 1.01x slower                                                   |
| pickle_dict          | 35.4 us                                                               | 36.6 us: 1.04x slower                                                  |
| unpickle             | 14.9 us                                                               | 15.7 us: 1.05x slower                                                  |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                           |

Benchmark hidden because not significant (3): xml_etree_parse, json_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240619-linux-x86_64-python-1e4815692f6c8a37a397-3.14.0a0-1e48156 | bm-20240620-linux-x86_64-nohlson-enable_no_impact_def-3.14.0a0-98d9ea0 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.4 ms                                                               | 10.4 ms: 1.00x slower                                                  |
| python_startup_no_site | 6.91 ms                                                               | 6.93 ms: 1.00x slower                                                  |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240619-linux-x86_64-python-1e4815692f6c8a37a397-3.14.0a0-1e48156 | bm-20240620-linux-x86_64-nohlson-enable_no_impact_def-3.14.0a0-98d9ea0 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text    | 23.5 ms                                                               | 23.1 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                           |

Benchmark hidden because not significant (3): genshi_xml, mako, django_template

All benchmarks:
===============

| Benchmark                | bm-20240619-linux-x86_64-python-1e4815692f6c8a37a397-3.14.0a0-1e48156 | bm-20240620-linux-x86_64-nohlson-enable_no_impact_def-3.14.0a0-98d9ea0 |
|--------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle                   | 11.7 us                                                               | 11.3 us: 1.04x faster                                                  |
| regex_effbot             | 3.70 ms                                                               | 3.55 ms: 1.04x faster                                                  |
| gc_traversal             | 3.75 ms                                                               | 3.60 ms: 1.04x faster                                                  |
| unpickle_list            | 5.55 us                                                               | 5.37 us: 1.03x faster                                                  |
| regex_v8                 | 25.2 ms                                                               | 24.6 ms: 1.02x faster                                                  |
| chaos                    | 60.6 ms                                                               | 59.6 ms: 1.02x faster                                                  |
| float                    | 77.8 ms                                                               | 76.6 ms: 1.02x faster                                                  |
| genshi_text              | 23.5 ms                                                               | 23.1 ms: 1.01x faster                                                  |
| json_dumps               | 10.5 ms                                                               | 10.4 ms: 1.01x faster                                                  |
| richards                 | 48.6 ms                                                               | 48.0 ms: 1.01x faster                                                  |
| pickle_list              | 5.17 us                                                               | 5.11 us: 1.01x faster                                                  |
| fannkuch                 | 396 ms                                                                | 392 ms: 1.01x faster                                                   |
| deepcopy_reduce          | 2.71 us                                                               | 2.68 us: 1.01x faster                                                  |
| spectral_norm            | 115 ms                                                                | 114 ms: 1.01x faster                                                   |
| regex_dna                | 227 ms                                                                | 224 ms: 1.01x faster                                                   |
| coroutines               | 22.8 ms                                                               | 22.6 ms: 1.01x faster                                                  |
| async_generators         | 439 ms                                                                | 436 ms: 1.01x faster                                                   |
| thrift                   | 806 us                                                                | 799 us: 1.01x faster                                                   |
| nqueens                  | 79.2 ms                                                               | 78.5 ms: 1.01x faster                                                  |
| generators               | 28.8 ms                                                               | 28.6 ms: 1.01x faster                                                  |
| pprint_safe_repr         | 744 ms                                                                | 739 ms: 1.01x faster                                                   |
| bench_thread_pool        | 791 us                                                                | 789 us: 1.00x faster                                                   |
| sympy_str                | 275 ms                                                                | 274 ms: 1.00x faster                                                   |
| pidigits                 | 188 ms                                                                | 187 ms: 1.00x faster                                                   |
| python_startup           | 10.4 ms                                                               | 10.4 ms: 1.00x slower                                                  |
| 2to3                     | 265 ms                                                                | 265 ms: 1.00x slower                                                   |
| asyncio_tcp_ssl          | 1.77 sec                                                              | 1.77 sec: 1.00x slower                                                 |
| python_startup_no_site   | 6.91 ms                                                               | 6.93 ms: 1.00x slower                                                  |
| asyncio_tcp              | 481 ms                                                                | 482 ms: 1.00x slower                                                   |
| sqlglot_optimize         | 53.8 ms                                                               | 54.0 ms: 1.00x slower                                                  |
| xml_etree_process        | 59.0 ms                                                               | 59.3 ms: 1.00x slower                                                  |
| dulwich_log              | 64.2 ms                                                               | 64.5 ms: 1.01x slower                                                  |
| pickle_pure_python       | 299 us                                                                | 301 us: 1.01x slower                                                   |
| xml_etree_generate       | 84.3 ms                                                               | 84.9 ms: 1.01x slower                                                  |
| sqlglot_normalize        | 107 ms                                                                | 108 ms: 1.01x slower                                                   |
| tornado_http             | 91.0 ms                                                               | 91.6 ms: 1.01x slower                                                  |
| comprehensions           | 16.8 us                                                               | 16.9 us: 1.01x slower                                                  |
| pyflate                  | 481 ms                                                                | 484 ms: 1.01x slower                                                   |
| html5lib                 | 66.9 ms                                                               | 67.4 ms: 1.01x slower                                                  |
| scimark_sor              | 125 ms                                                                | 126 ms: 1.01x slower                                                   |
| logging_simple           | 5.46 us                                                               | 5.51 us: 1.01x slower                                                  |
| regex_compile            | 130 ms                                                                | 132 ms: 1.01x slower                                                   |
| nbody                    | 90.8 ms                                                               | 91.9 ms: 1.01x slower                                                  |
| tomli_loads              | 2.11 sec                                                              | 2.14 sec: 1.01x slower                                                 |
| unpickle_pure_python     | 214 us                                                                | 217 us: 1.01x slower                                                   |
| scimark_monte_carlo      | 68.8 ms                                                               | 69.8 ms: 1.01x slower                                                  |
| deepcopy_memo            | 29.4 us                                                               | 29.9 us: 1.02x slower                                                  |
| telco                    | 8.16 ms                                                               | 8.29 ms: 1.02x slower                                                  |
| deltablue                | 3.22 ms                                                               | 3.28 ms: 1.02x slower                                                  |
| hexiom                   | 6.08 ms                                                               | 6.19 ms: 1.02x slower                                                  |
| bpe_tokeniser            | 4.79 sec                                                              | 4.89 sec: 1.02x slower                                                 |
| typing_runtime_protocols | 160 us                                                                | 164 us: 1.02x slower                                                   |
| deepcopy                 | 259 us                                                                | 265 us: 1.02x slower                                                   |
| logging_silent           | 102 ns                                                                | 105 ns: 1.03x slower                                                   |
| pickle_dict              | 35.4 us                                                               | 36.6 us: 1.04x slower                                                  |
| unpickle                 | 14.9 us                                                               | 15.7 us: 1.05x slower                                                  |
| mdp                      | 2.53 sec                                                              | 2.73 sec: 1.08x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                           |

Benchmark hidden because not significant (40): async_tree_io_tg, xml_etree_parse, async_tree_none_tg, scimark_lu, async_tree_cpu_io_mixed_tg, pycparser, sqlite_synth, sympy_expand, async_tree_none, logging_format, async_tree_cpu_io_mixed, scimark_sparse_mat_mult, coverage, async_tree_io, json_loads, genshi_xml, docutils, richards_super, async_tree_memoization, sqlglot_parse, pprint_pformat, sqlglot_transpile, asyncio_websockets, create_gc_cycles, json, async_tree_memoization_tg, sympy_sum, bench_mp_pool, sympy_integrate, raytrace, pylint, scimark_fft, pathlib, crypto_pyaes, mako, go, meteor_contest, dask, xml_etree_iterparse, django_template

# HPT report

- Reliability score: 70.47% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x