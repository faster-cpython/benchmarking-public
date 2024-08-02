# Results vs. base

- fork: brandtbucher
- ref: warmer_side_exits
- machine: linux-x86_64
- commit hash: 080259b
- commit date: 2024-06-20
- overall geometric mean: 1.02x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-080259b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 281 ms                                                                | 276 ms: 1.02x faster                                                     |
| docutils       | 2.95 sec                                                              | 2.88 sec: 1.03x faster                                                   |
| html5lib       | 69.0 ms                                                               | 65.5 ms: 1.05x faster                                                    |
| tornado_http   | 96.8 ms                                                               | 94.1 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-080259b |
|---------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg          | 1.02 sec                                                              | 902 ms: 1.13x faster                                                     |
| async_tree_memoization_tg | 466 ms                                                                | 424 ms: 1.10x faster                                                     |
| async_tree_memoization    | 495 ms                                                                | 452 ms: 1.09x faster                                                     |
| async_tree_io             | 955 ms                                                                | 911 ms: 1.05x faster                                                     |
| async_tree_cpu_io_mixed   | 624 ms                                                                | 596 ms: 1.05x faster                                                     |
| async_tree_none           | 379 ms                                                                | 369 ms: 1.03x faster                                                     |
| Geometric mean            | (ref)                                                                 | 1.06x faster                                                             |

Benchmark hidden because not significant (2): async_tree_none_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-080259b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 72.4 ms                                                               | 70.6 ms: 1.02x faster                                                    |
| pidigits       | 188 ms                                                                | 185 ms: 1.01x faster                                                     |
| nbody          | 81.0 ms                                                               | 83.0 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-080259b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 138 ms                                                                | 134 ms: 1.03x faster                                                     |
| regex_v8       | 24.4 ms                                                               | 24.0 ms: 1.02x faster                                                    |
| regex_effbot   | 3.69 ms                                                               | 3.72 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-080259b |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 222 us                                                                | 204 us: 1.09x faster                                                     |
| unpickle_list        | 5.39 us                                                               | 5.13 us: 1.05x faster                                                    |
| pickle_dict          | 37.2 us                                                               | 35.9 us: 1.04x faster                                                    |
| tomli_loads          | 1.97 sec                                                              | 1.90 sec: 1.04x faster                                                   |
| pickle               | 12.2 us                                                               | 11.8 us: 1.03x faster                                                    |
| pickle_list          | 5.34 us                                                               | 5.19 us: 1.03x faster                                                    |
| json_loads           | 29.2 us                                                               | 28.5 us: 1.02x faster                                                    |
| xml_etree_process    | 59.1 ms                                                               | 57.8 ms: 1.02x faster                                                    |
| xml_etree_iterparse  | 101 ms                                                                | 99.3 ms: 1.02x faster                                                    |
| xml_etree_generate   | 82.0 ms                                                               | 80.6 ms: 1.02x faster                                                    |
| pickle_pure_python   | 297 us                                                                | 294 us: 1.01x faster                                                     |
| json_dumps           | 10.6 ms                                                               | 10.5 ms: 1.00x faster                                                    |
| unpickle             | 14.8 us                                                               | 15.5 us: 1.05x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.02x faster                                                             |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-080259b |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 7.64 ms                                                               | 7.39 ms: 1.03x faster                                                    |
| python_startup         | 11.2 ms                                                               | 10.8 ms: 1.03x faster                                                    |
| Geometric mean         | (ref)                                                                 | 1.03x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-080259b |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 59.2 ms                                                               | 55.9 ms: 1.06x faster                                                    |
| mako            | 10.1 ms                                                               | 9.58 ms: 1.05x faster                                                    |
| django_template | 37.1 ms                                                               | 35.5 ms: 1.05x faster                                                    |
| genshi_text     | 25.2 ms                                                               | 24.8 ms: 1.01x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.04x faster                                                             |

All benchmarks:
===============

| Benchmark                 | bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-080259b |
|---------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg          | 1.02 sec                                                              | 902 ms: 1.13x faster                                                     |
| async_tree_memoization_tg | 466 ms                                                                | 424 ms: 1.10x faster                                                     |
| async_tree_memoization    | 495 ms                                                                | 452 ms: 1.09x faster                                                     |
| unpickle_pure_python      | 222 us                                                                | 204 us: 1.09x faster                                                     |
| scimark_sparse_mat_mult   | 4.55 ms                                                               | 4.22 ms: 1.08x faster                                                    |
| gc_traversal              | 3.83 ms                                                               | 3.57 ms: 1.07x faster                                                    |
| richards                  | 43.3 ms                                                               | 40.5 ms: 1.07x faster                                                    |
| genshi_xml                | 59.2 ms                                                               | 55.9 ms: 1.06x faster                                                    |
| pyflate                   | 458 ms                                                                | 434 ms: 1.06x faster                                                     |
| html5lib                  | 69.0 ms                                                               | 65.5 ms: 1.05x faster                                                    |
| mako                      | 10.1 ms                                                               | 9.58 ms: 1.05x faster                                                    |
| unpickle_list             | 5.39 us                                                               | 5.13 us: 1.05x faster                                                    |
| async_tree_io             | 955 ms                                                                | 911 ms: 1.05x faster                                                     |
| async_tree_cpu_io_mixed   | 624 ms                                                                | 596 ms: 1.05x faster                                                     |
| django_template           | 37.1 ms                                                               | 35.5 ms: 1.05x faster                                                    |
| asyncio_tcp               | 513 ms                                                                | 491 ms: 1.05x faster                                                     |
| bench_thread_pool         | 858 us                                                                | 827 us: 1.04x faster                                                     |
| fannkuch                  | 358 ms                                                                | 345 ms: 1.04x faster                                                     |
| pickle_dict               | 37.2 us                                                               | 35.9 us: 1.04x faster                                                    |
| tomli_loads               | 1.97 sec                                                              | 1.90 sec: 1.04x faster                                                   |
| asyncio_tcp_ssl           | 1.86 sec                                                              | 1.79 sec: 1.04x faster                                                   |
| coverage                  | 96.2 ms                                                               | 92.9 ms: 1.03x faster                                                    |
| logging_simple            | 5.65 us                                                               | 5.46 us: 1.03x faster                                                    |
| python_startup_no_site    | 7.64 ms                                                               | 7.39 ms: 1.03x faster                                                    |
| logging_format            | 6.23 us                                                               | 6.03 us: 1.03x faster                                                    |
| python_startup            | 11.2 ms                                                               | 10.8 ms: 1.03x faster                                                    |
| richards_super            | 49.1 ms                                                               | 47.6 ms: 1.03x faster                                                    |
| pathlib                   | 16.4 ms                                                               | 15.9 ms: 1.03x faster                                                    |
| pickle                    | 12.2 us                                                               | 11.8 us: 1.03x faster                                                    |
| dask                      | 377 ms                                                                | 366 ms: 1.03x faster                                                     |
| tornado_http              | 96.8 ms                                                               | 94.1 ms: 1.03x faster                                                    |
| coroutines                | 23.7 ms                                                               | 23.0 ms: 1.03x faster                                                    |
| pickle_list               | 5.34 us                                                               | 5.19 us: 1.03x faster                                                    |
| sqlglot_parse             | 1.32 ms                                                               | 1.28 ms: 1.03x faster                                                    |
| create_gc_cycles          | 1.79 ms                                                               | 1.75 ms: 1.03x faster                                                    |
| sqlglot_transpile         | 1.64 ms                                                               | 1.59 ms: 1.03x faster                                                    |
| deepcopy_reduce           | 2.83 us                                                               | 2.76 us: 1.03x faster                                                    |
| regex_compile             | 138 ms                                                                | 134 ms: 1.03x faster                                                     |
| async_tree_none           | 379 ms                                                                | 369 ms: 1.03x faster                                                     |
| chaos                     | 59.8 ms                                                               | 58.3 ms: 1.03x faster                                                    |
| docutils                  | 2.95 sec                                                              | 2.88 sec: 1.03x faster                                                   |
| comprehensions            | 16.8 us                                                               | 16.4 us: 1.03x faster                                                    |
| scimark_sor               | 139 ms                                                                | 136 ms: 1.03x faster                                                     |
| float                     | 72.4 ms                                                               | 70.6 ms: 1.02x faster                                                    |
| json_loads                | 29.2 us                                                               | 28.5 us: 1.02x faster                                                    |
| json                      | 5.40 ms                                                               | 5.28 ms: 1.02x faster                                                    |
| raytrace                  | 283 ms                                                                | 277 ms: 1.02x faster                                                     |
| telco                     | 8.15 ms                                                               | 7.97 ms: 1.02x faster                                                    |
| dulwich_log               | 69.2 ms                                                               | 67.7 ms: 1.02x faster                                                    |
| xml_etree_process         | 59.1 ms                                                               | 57.8 ms: 1.02x faster                                                    |
| scimark_lu                | 126 ms                                                                | 124 ms: 1.02x faster                                                     |
| meteor_contest            | 109 ms                                                                | 106 ms: 1.02x faster                                                     |
| 2to3                      | 281 ms                                                                | 276 ms: 1.02x faster                                                     |
| pprint_pformat            | 1.49 sec                                                              | 1.46 sec: 1.02x faster                                                   |
| asyncio_websockets        | 566 ms                                                                | 556 ms: 1.02x faster                                                     |
| regex_v8                  | 24.4 ms                                                               | 24.0 ms: 1.02x faster                                                    |
| xml_etree_iterparse       | 101 ms                                                                | 99.3 ms: 1.02x faster                                                    |
| hexiom                    | 6.65 ms                                                               | 6.54 ms: 1.02x faster                                                    |
| sympy_expand              | 514 ms                                                                | 505 ms: 1.02x faster                                                     |
| xml_etree_generate        | 82.0 ms                                                               | 80.6 ms: 1.02x faster                                                    |
| generators                | 30.2 ms                                                               | 29.7 ms: 1.02x faster                                                    |
| sympy_sum                 | 171 ms                                                                | 169 ms: 1.02x faster                                                     |
| sympy_str                 | 304 ms                                                                | 300 ms: 1.01x faster                                                     |
| pidigits                  | 188 ms                                                                | 185 ms: 1.01x faster                                                     |
| genshi_text               | 25.2 ms                                                               | 24.8 ms: 1.01x faster                                                    |
| scimark_monte_carlo       | 62.8 ms                                                               | 61.9 ms: 1.01x faster                                                    |
| logging_silent            | 107 ns                                                                | 106 ns: 1.01x faster                                                     |
| nqueens                   | 85.8 ms                                                               | 84.7 ms: 1.01x faster                                                    |
| bpe_tokeniser             | 4.87 sec                                                              | 4.81 sec: 1.01x faster                                                   |
| scimark_fft               | 317 ms                                                                | 313 ms: 1.01x faster                                                     |
| crypto_pyaes              | 67.6 ms                                                               | 66.8 ms: 1.01x faster                                                    |
| async_generators          | 463 ms                                                                | 457 ms: 1.01x faster                                                     |
| pycparser                 | 1.20 sec                                                              | 1.19 sec: 1.01x faster                                                   |
| typing_runtime_protocols  | 171 us                                                                | 169 us: 1.01x faster                                                     |
| sympy_integrate           | 22.6 ms                                                               | 22.3 ms: 1.01x faster                                                    |
| thrift                    | 826 us                                                                | 817 us: 1.01x faster                                                     |
| pickle_pure_python        | 297 us                                                                | 294 us: 1.01x faster                                                     |
| go                        | 148 ms                                                                | 147 ms: 1.01x faster                                                     |
| sqlglot_optimize          | 56.8 ms                                                               | 56.3 ms: 1.01x faster                                                    |
| json_dumps                | 10.6 ms                                                               | 10.5 ms: 1.00x faster                                                    |
| regex_effbot              | 3.69 ms                                                               | 3.72 ms: 1.01x slower                                                    |
| deepcopy_memo             | 28.8 us                                                               | 29.1 us: 1.01x slower                                                    |
| nbody                     | 81.0 ms                                                               | 83.0 ms: 1.02x slower                                                    |
| mdp                       | 2.65 sec                                                              | 2.75 sec: 1.04x slower                                                   |
| unpickle                  | 14.8 us                                                               | 15.5 us: 1.05x slower                                                    |
| deltablue                 | 3.66 ms                                                               | 3.84 ms: 1.05x slower                                                    |
| Geometric mean            | (ref)                                                                 | 1.02x faster                                                             |

Benchmark hidden because not significant (11): async_tree_none_tg, async_tree_cpu_io_mixed_tg, pylint, xml_etree_parse, pprint_safe_repr, bench_mp_pool, sqlite_synth, regex_dna, deepcopy, spectral_norm, sqlglot_normalize

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.01x