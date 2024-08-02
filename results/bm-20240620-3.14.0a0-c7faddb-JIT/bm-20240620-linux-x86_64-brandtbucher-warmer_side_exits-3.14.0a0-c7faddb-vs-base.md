# Results vs. base

- fork: brandtbucher
- ref: warmer_side_exits
- machine: linux-x86_64
- commit hash: c7faddb
- commit date: 2024-06-20
- overall geometric mean: 1.01x slower
- HPT reliability: 99.94%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-c7faddb |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 272 ms                                                                | 276 ms: 1.01x slower                                                     |
| docutils       | 2.86 sec                                                              | 2.89 sec: 1.01x slower                                                   |
| html5lib       | 67.1 ms                                                               | 67.8 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                             |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-c7faddb |
|---------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg          | 985 ms                                                                | 882 ms: 1.12x faster                                                     |
| async_tree_memoization_tg | 448 ms                                                                | 422 ms: 1.06x faster                                                     |
| async_tree_memoization    | 478 ms                                                                | 452 ms: 1.06x faster                                                     |
| async_tree_io             | 931 ms                                                                | 904 ms: 1.03x faster                                                     |
| Geometric mean            | (ref)                                                                 | 1.03x faster                                                             |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-c7faddb |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 185 ms                                                                | 185 ms: 1.00x slower                                                     |
| nbody          | 80.7 ms                                                               | 81.2 ms: 1.01x slower                                                    |
| float          | 69.6 ms                                                               | 70.2 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-c7faddb |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 135 ms                                                                | 136 ms: 1.00x slower                                                     |
| regex_dna      | 221 ms                                                                | 233 ms: 1.05x slower                                                     |
| regex_effbot   | 3.56 ms                                                               | 3.95 ms: 1.11x slower                                                    |
| regex_v8       | 23.1 ms                                                               | 26.3 ms: 1.14x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.07x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-c7faddb |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 218 us                                                                | 202 us: 1.08x faster                                                     |
| pickle_dict          | 35.7 us                                                               | 34.5 us: 1.04x faster                                                    |
| tomli_loads          | 1.93 sec                                                              | 1.90 sec: 1.01x faster                                                   |
| json_dumps           | 10.5 ms                                                               | 10.4 ms: 1.01x faster                                                    |
| json_loads           | 28.5 us                                                               | 28.3 us: 1.00x faster                                                    |
| xml_etree_generate   | 80.5 ms                                                               | 81.0 ms: 1.01x slower                                                    |
| unpickle_list        | 5.15 us                                                               | 5.20 us: 1.01x slower                                                    |
| pickle_pure_python   | 291 us                                                                | 296 us: 1.01x slower                                                     |
| pickle_list          | 4.93 us                                                               | 5.01 us: 1.01x slower                                                    |
| xml_etree_iterparse  | 98.6 ms                                                               | 100 ms: 1.02x slower                                                     |
| pickle               | 11.7 us                                                               | 11.9 us: 1.02x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                             |

Benchmark hidden because not significant (3): unpickle, xml_etree_process, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-c7faddb |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                               | 10.8 ms: 1.00x faster                                                    |
| python_startup_no_site | 7.41 ms                                                               | 7.41 ms: 1.00x faster                                                    |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-c7faddb |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 37.4 ms                                                               | 36.5 ms: 1.02x faster                                                    |
| mako            | 9.54 ms                                                               | 9.80 ms: 1.03x slower                                                    |
| genshi_xml      | 56.8 ms                                                               | 59.4 ms: 1.05x slower                                                    |
| genshi_text     | 24.6 ms                                                               | 25.8 ms: 1.05x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                             |

All benchmarks:
===============

| Benchmark                 | bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-c7faddb |
|---------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg          | 985 ms                                                                | 882 ms: 1.12x faster                                                     |
| unpickle_pure_python      | 218 us                                                                | 202 us: 1.08x faster                                                     |
| async_tree_memoization_tg | 448 ms                                                                | 422 ms: 1.06x faster                                                     |
| async_tree_memoization    | 478 ms                                                                | 452 ms: 1.06x faster                                                     |
| scimark_sparse_mat_mult   | 4.52 ms                                                               | 4.36 ms: 1.04x faster                                                    |
| pickle_dict               | 35.7 us                                                               | 34.5 us: 1.04x faster                                                    |
| async_tree_io             | 931 ms                                                                | 904 ms: 1.03x faster                                                     |
| mdp                       | 2.76 sec                                                              | 2.69 sec: 1.03x faster                                                   |
| pyflate                   | 435 ms                                                                | 425 ms: 1.03x faster                                                     |
| django_template           | 37.4 ms                                                               | 36.5 ms: 1.02x faster                                                    |
| chaos                     | 60.4 ms                                                               | 59.2 ms: 1.02x faster                                                    |
| fannkuch                  | 350 ms                                                                | 345 ms: 1.02x faster                                                     |
| scimark_fft               | 318 ms                                                                | 313 ms: 1.01x faster                                                     |
| tomli_loads               | 1.93 sec                                                              | 1.90 sec: 1.01x faster                                                   |
| scimark_monte_carlo       | 62.2 ms                                                               | 61.4 ms: 1.01x faster                                                    |
| json_dumps                | 10.5 ms                                                               | 10.4 ms: 1.01x faster                                                    |
| comprehensions            | 16.4 us                                                               | 16.4 us: 1.01x faster                                                    |
| json_loads                | 28.5 us                                                               | 28.3 us: 1.00x faster                                                    |
| bench_thread_pool         | 834 us                                                                | 830 us: 1.00x faster                                                     |
| asyncio_tcp_ssl           | 1.79 sec                                                              | 1.79 sec: 1.00x faster                                                   |
| python_startup            | 10.8 ms                                                               | 10.8 ms: 1.00x faster                                                    |
| python_startup_no_site    | 7.41 ms                                                               | 7.41 ms: 1.00x faster                                                    |
| pidigits                  | 185 ms                                                                | 185 ms: 1.00x slower                                                     |
| bpe_tokeniser             | 4.80 sec                                                              | 4.82 sec: 1.00x slower                                                   |
| create_gc_cycles          | 1.75 ms                                                               | 1.76 ms: 1.00x slower                                                    |
| regex_compile             | 135 ms                                                                | 136 ms: 1.00x slower                                                     |
| async_generators          | 459 ms                                                                | 461 ms: 1.00x slower                                                     |
| sqlglot_transpile         | 1.60 ms                                                               | 1.61 ms: 1.00x slower                                                    |
| logging_silent            | 105 ns                                                                | 106 ns: 1.00x slower                                                     |
| pathlib                   | 16.0 ms                                                               | 16.1 ms: 1.01x slower                                                    |
| dulwich_log               | 67.6 ms                                                               | 67.9 ms: 1.01x slower                                                    |
| crypto_pyaes              | 66.4 ms                                                               | 66.8 ms: 1.01x slower                                                    |
| xml_etree_generate        | 80.5 ms                                                               | 81.0 ms: 1.01x slower                                                    |
| nbody                     | 80.7 ms                                                               | 81.2 ms: 1.01x slower                                                    |
| logging_simple            | 5.46 us                                                               | 5.50 us: 1.01x slower                                                    |
| scimark_lu                | 125 ms                                                                | 126 ms: 1.01x slower                                                     |
| raytrace                  | 275 ms                                                                | 277 ms: 1.01x slower                                                     |
| nqueens                   | 83.5 ms                                                               | 84.2 ms: 1.01x slower                                                    |
| float                     | 69.6 ms                                                               | 70.2 ms: 1.01x slower                                                    |
| hexiom                    | 6.51 ms                                                               | 6.57 ms: 1.01x slower                                                    |
| unpickle_list             | 5.15 us                                                               | 5.20 us: 1.01x slower                                                    |
| sqlglot_parse             | 1.28 ms                                                               | 1.29 ms: 1.01x slower                                                    |
| go                        | 145 ms                                                                | 147 ms: 1.01x slower                                                     |
| html5lib                  | 67.1 ms                                                               | 67.8 ms: 1.01x slower                                                    |
| meteor_contest            | 106 ms                                                                | 107 ms: 1.01x slower                                                     |
| 2to3                      | 272 ms                                                                | 276 ms: 1.01x slower                                                     |
| docutils                  | 2.86 sec                                                              | 2.89 sec: 1.01x slower                                                   |
| pickle_pure_python        | 291 us                                                                | 296 us: 1.01x slower                                                     |
| logging_format            | 6.00 us                                                               | 6.08 us: 1.01x slower                                                    |
| pickle_list               | 4.93 us                                                               | 5.01 us: 1.01x slower                                                    |
| asyncio_tcp               | 481 ms                                                                | 489 ms: 1.02x slower                                                     |
| sqlglot_normalize         | 113 ms                                                                | 115 ms: 1.02x slower                                                     |
| xml_etree_iterparse       | 98.6 ms                                                               | 100 ms: 1.02x slower                                                     |
| pickle                    | 11.7 us                                                               | 11.9 us: 1.02x slower                                                    |
| deepcopy                  | 273 us                                                                | 278 us: 1.02x slower                                                     |
| pycparser                 | 1.14 sec                                                              | 1.16 sec: 1.02x slower                                                   |
| pprint_safe_repr          | 695 ms                                                                | 712 ms: 1.02x slower                                                     |
| generators                | 29.4 ms                                                               | 30.2 ms: 1.03x slower                                                    |
| mako                      | 9.54 ms                                                               | 9.80 ms: 1.03x slower                                                    |
| sqlglot_optimize          | 56.1 ms                                                               | 57.7 ms: 1.03x slower                                                    |
| scimark_sor               | 128 ms                                                                | 134 ms: 1.04x slower                                                     |
| genshi_xml                | 56.8 ms                                                               | 59.4 ms: 1.05x slower                                                    |
| genshi_text               | 24.6 ms                                                               | 25.8 ms: 1.05x slower                                                    |
| regex_dna                 | 221 ms                                                                | 233 ms: 1.05x slower                                                     |
| richards_super            | 48.0 ms                                                               | 50.5 ms: 1.05x slower                                                    |
| richards                  | 42.0 ms                                                               | 44.6 ms: 1.06x slower                                                    |
| gc_traversal              | 3.74 ms                                                               | 4.01 ms: 1.07x slower                                                    |
| deltablue                 | 3.54 ms                                                               | 3.85 ms: 1.09x slower                                                    |
| regex_effbot              | 3.56 ms                                                               | 3.95 ms: 1.11x slower                                                    |
| regex_v8                  | 23.1 ms                                                               | 26.3 ms: 1.14x slower                                                    |
| Geometric mean            | (ref)                                                                 | 1.01x slower                                                             |

Benchmark hidden because not significant (27): async_tree_cpu_io_mixed, unpickle, async_tree_cpu_io_mixed_tg, typing_runtime_protocols, deepcopy_memo, json, xml_etree_process, sympy_integrate, sympy_expand, asyncio_websockets, telco, xml_etree_parse, bench_mp_pool, sympy_str, thrift, coroutines, tornado_http, sympy_sum, coverage, spectral_norm, deepcopy_reduce, sqlite_synth, dask, pprint_pformat, async_tree_none_tg, async_tree_none, pylint

# HPT report

- Reliability score: 99.94% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x