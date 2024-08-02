# Results vs. base

- fork: nohlson
- ref: 1_investigate_compil
- machine: linux-x86_64
- commit hash: 5b8a44e
- commit date: 2024-06-18
- overall geometric mean: 1.01x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240617-linux-x86_64-python-2c66318cdc0545da37e7-3.14.0a0-2c66318 | bm-20240618-linux-x86_64-nohlson-1_investigate_compil-3.14.0a0-5b8a44e |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 272 ms                                                                | 267 ms: 1.02x faster                                                   |
| html5lib       | 67.0 ms                                                               | 65.1 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                           |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_memoization, async_tree_none_tg, async_tree_io, async_tree_memoization_tg, async_tree_none, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240617-linux-x86_64-python-2c66318cdc0545da37e7-3.14.0a0-2c66318 | bm-20240618-linux-x86_64-nohlson-1_investigate_compil-3.14.0a0-5b8a44e |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 90.5 ms                                                               | 87.4 ms: 1.04x faster                                                  |
| float          | 79.3 ms                                                               | 77.6 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240617-linux-x86_64-python-2c66318cdc0545da37e7-3.14.0a0-2c66318 | bm-20240618-linux-x86_64-nohlson-1_investigate_compil-3.14.0a0-5b8a44e |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 134 ms                                                                | 133 ms: 1.01x faster                                                   |
| regex_dna      | 229 ms                                                                | 231 ms: 1.01x slower                                                   |
| regex_v8       | 25.8 ms                                                               | 27.2 ms: 1.05x slower                                                  |
| regex_effbot   | 3.68 ms                                                               | 3.92 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240617-linux-x86_64-python-2c66318cdc0545da37e7-3.14.0a0-2c66318 | bm-20240618-linux-x86_64-nohlson-1_investigate_compil-3.14.0a0-5b8a44e |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 220 us                                                                | 212 us: 1.04x faster                                                   |
| pickle_pure_python   | 308 us                                                                | 302 us: 1.02x faster                                                   |
| xml_etree_process    | 60.0 ms                                                               | 59.2 ms: 1.01x faster                                                  |
| tomli_loads          | 2.20 sec                                                              | 2.18 sec: 1.01x faster                                                 |
| pickle_dict          | 34.3 us                                                               | 34.0 us: 1.01x faster                                                  |
| pickle_list          | 4.99 us                                                               | 5.04 us: 1.01x slower                                                  |
| xml_etree_iterparse  | 106 ms                                                                | 107 ms: 1.01x slower                                                   |
| pickle               | 11.8 us                                                               | 11.9 us: 1.01x slower                                                  |
| unpickle_list        | 5.40 us                                                               | 5.53 us: 1.02x slower                                                  |
| json_dumps           | 10.5 ms                                                               | 10.7 ms: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                           |

Benchmark hidden because not significant (4): json_loads, xml_etree_generate, unpickle, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240617-linux-x86_64-python-2c66318cdc0545da37e7-3.14.0a0-2c66318 | bm-20240618-linux-x86_64-nohlson-1_investigate_compil-3.14.0a0-5b8a44e |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.7 ms                                                               | 10.7 ms: 1.00x slower                                                  |
| python_startup_no_site | 7.11 ms                                                               | 7.15 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240617-linux-x86_64-python-2c66318cdc0545da37e7-3.14.0a0-2c66318 | bm-20240618-linux-x86_64-nohlson-1_investigate_compil-3.14.0a0-5b8a44e |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 11.3 ms                                                               | 11.0 ms: 1.03x faster                                                  |
| genshi_text     | 23.6 ms                                                               | 23.4 ms: 1.01x faster                                                  |
| django_template | 35.0 ms                                                               | 34.8 ms: 1.01x faster                                                  |
| genshi_xml      | 50.4 ms                                                               | 50.7 ms: 1.01x slower                                                  |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20240617-linux-x86_64-python-2c66318cdc0545da37e7-3.14.0a0-2c66318 | bm-20240618-linux-x86_64-nohlson-1_investigate_compil-3.14.0a0-5b8a44e |
|--------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| scimark_sor              | 135 ms                                                                | 122 ms: 1.10x faster                                                   |
| mdp                      | 2.79 sec                                                              | 2.55 sec: 1.10x faster                                                 |
| logging_silent           | 106 ns                                                                | 97.4 ns: 1.08x faster                                                  |
| fannkuch                 | 408 ms                                                                | 385 ms: 1.06x faster                                                   |
| scimark_fft              | 377 ms                                                                | 357 ms: 1.06x faster                                                   |
| richards_super           | 56.1 ms                                                               | 53.2 ms: 1.05x faster                                                  |
| scimark_sparse_mat_mult  | 5.10 ms                                                               | 4.83 ms: 1.05x faster                                                  |
| scimark_monte_carlo      | 69.4 ms                                                               | 66.0 ms: 1.05x faster                                                  |
| richards                 | 49.2 ms                                                               | 46.8 ms: 1.05x faster                                                  |
| pycparser                | 1.20 sec                                                              | 1.15 sec: 1.04x faster                                                 |
| go                       | 146 ms                                                                | 140 ms: 1.04x faster                                                   |
| deepcopy_memo            | 30.3 us                                                               | 29.0 us: 1.04x faster                                                  |
| spectral_norm            | 117 ms                                                                | 113 ms: 1.04x faster                                                   |
| raytrace                 | 266 ms                                                                | 257 ms: 1.04x faster                                                   |
| crypto_pyaes             | 76.9 ms                                                               | 74.2 ms: 1.04x faster                                                  |
| unpickle_pure_python     | 220 us                                                                | 212 us: 1.04x faster                                                   |
| nbody                    | 90.5 ms                                                               | 87.4 ms: 1.04x faster                                                  |
| mako                     | 11.3 ms                                                               | 11.0 ms: 1.03x faster                                                  |
| chaos                    | 60.9 ms                                                               | 59.0 ms: 1.03x faster                                                  |
| deltablue                | 3.32 ms                                                               | 3.22 ms: 1.03x faster                                                  |
| html5lib                 | 67.0 ms                                                               | 65.1 ms: 1.03x faster                                                  |
| float                    | 79.3 ms                                                               | 77.6 ms: 1.02x faster                                                  |
| pickle_pure_python       | 308 us                                                                | 302 us: 1.02x faster                                                   |
| 2to3                     | 272 ms                                                                | 267 ms: 1.02x faster                                                   |
| sqlglot_parse            | 1.33 ms                                                               | 1.31 ms: 1.02x faster                                                  |
| pyflate                  | 488 ms                                                                | 480 ms: 1.02x faster                                                   |
| comprehensions           | 16.9 us                                                               | 16.6 us: 1.02x faster                                                  |
| deepcopy_reduce          | 2.75 us                                                               | 2.71 us: 1.01x faster                                                  |
| meteor_contest           | 110 ms                                                                | 108 ms: 1.01x faster                                                   |
| xml_etree_process        | 60.0 ms                                                               | 59.2 ms: 1.01x faster                                                  |
| scimark_lu               | 115 ms                                                                | 114 ms: 1.01x faster                                                   |
| deepcopy                 | 266 us                                                                | 263 us: 1.01x faster                                                   |
| sqlite_synth             | 2.95 us                                                               | 2.91 us: 1.01x faster                                                  |
| thrift                   | 801 us                                                                | 791 us: 1.01x faster                                                   |
| tomli_loads              | 2.20 sec                                                              | 2.18 sec: 1.01x faster                                                 |
| bpe_tokeniser            | 4.96 sec                                                              | 4.91 sec: 1.01x faster                                                 |
| telco                    | 8.46 ms                                                               | 8.38 ms: 1.01x faster                                                  |
| genshi_text              | 23.6 ms                                                               | 23.4 ms: 1.01x faster                                                  |
| pickle_dict              | 34.3 us                                                               | 34.0 us: 1.01x faster                                                  |
| typing_runtime_protocols | 166 us                                                                | 165 us: 1.01x faster                                                   |
| regex_compile            | 134 ms                                                                | 133 ms: 1.01x faster                                                   |
| django_template          | 35.0 ms                                                               | 34.8 ms: 1.01x faster                                                  |
| sqlglot_transpile        | 1.62 ms                                                               | 1.61 ms: 1.01x faster                                                  |
| bench_thread_pool        | 834 us                                                                | 828 us: 1.01x faster                                                   |
| asyncio_tcp_ssl          | 1.85 sec                                                              | 1.84 sec: 1.01x faster                                                 |
| coverage                 | 94.1 ms                                                               | 93.4 ms: 1.01x faster                                                  |
| asyncio_websockets       | 569 ms                                                                | 566 ms: 1.01x faster                                                   |
| sqlglot_normalize        | 110 ms                                                                | 109 ms: 1.01x faster                                                   |
| sympy_sum                | 155 ms                                                                | 154 ms: 1.01x faster                                                   |
| dulwich_log              | 65.1 ms                                                               | 64.8 ms: 1.01x faster                                                  |
| logging_format           | 6.34 us                                                               | 6.30 us: 1.01x faster                                                  |
| nqueens                  | 79.7 ms                                                               | 79.3 ms: 1.01x faster                                                  |
| asyncio_tcp              | 502 ms                                                                | 500 ms: 1.01x faster                                                   |
| pprint_safe_repr         | 762 ms                                                                | 759 ms: 1.00x faster                                                   |
| sqlglot_optimize         | 54.7 ms                                                               | 54.6 ms: 1.00x faster                                                  |
| python_startup           | 10.7 ms                                                               | 10.7 ms: 1.00x slower                                                  |
| pathlib                  | 16.1 ms                                                               | 16.2 ms: 1.01x slower                                                  |
| async_generators         | 446 ms                                                                | 448 ms: 1.01x slower                                                   |
| python_startup_no_site   | 7.11 ms                                                               | 7.15 ms: 1.01x slower                                                  |
| genshi_xml               | 50.4 ms                                                               | 50.7 ms: 1.01x slower                                                  |
| pprint_pformat           | 1.56 sec                                                              | 1.57 sec: 1.01x slower                                                 |
| gc_traversal             | 3.58 ms                                                               | 3.60 ms: 1.01x slower                                                  |
| regex_dna                | 229 ms                                                                | 231 ms: 1.01x slower                                                   |
| pickle_list              | 4.99 us                                                               | 5.04 us: 1.01x slower                                                  |
| xml_etree_iterparse      | 106 ms                                                                | 107 ms: 1.01x slower                                                   |
| pickle                   | 11.8 us                                                               | 11.9 us: 1.01x slower                                                  |
| unpickle_list            | 5.40 us                                                               | 5.53 us: 1.02x slower                                                  |
| json_dumps               | 10.5 ms                                                               | 10.7 ms: 1.03x slower                                                  |
| regex_v8                 | 25.8 ms                                                               | 27.2 ms: 1.05x slower                                                  |
| regex_effbot             | 3.68 ms                                                               | 3.92 ms: 1.07x slower                                                  |
| Geometric mean           | (ref)                                                                 | 1.01x faster                                                           |

Benchmark hidden because not significant (27): async_tree_memoization, async_tree_none_tg, async_tree_io, async_tree_memoization_tg, json_loads, async_tree_none, json, xml_etree_generate, dask, pylint, sympy_str, tornado_http, async_tree_io_tg, coroutines, hexiom, sympy_expand, create_gc_cycles, docutils, pidigits, sympy_integrate, generators, unpickle, logging_simple, bench_mp_pool, xml_etree_parse, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x