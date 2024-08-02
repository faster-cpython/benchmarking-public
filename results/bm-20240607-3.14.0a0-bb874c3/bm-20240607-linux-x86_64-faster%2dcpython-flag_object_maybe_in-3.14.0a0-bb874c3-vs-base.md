# Results vs. base

- fork: faster-cpython
- ref: flag_object_maybe_in
- machine: linux-x86_64
- commit hash: bb874c3
- commit date: 2024-06-07
- overall geometric mean: 1.01x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240606-linux-x86_64-python-f878d46e5614f08a9302-3.14.0a0-f878d46 | bm-20240607-linux-x86_64-faster%2dcpython-flag_object_maybe_in-3.14.0a0-bb874c3 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 269 ms                                                                | 272 ms: 1.01x slower                                                            |
| html5lib       | 67.7 ms                                                               | 66.9 ms: 1.01x faster                                                           |
| tornado_http   | 94.4 ms                                                               | 94.8 ms: 1.00x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240606-linux-x86_64-python-f878d46e5614f08a9302-3.14.0a0-f878d46 | bm-20240607-linux-x86_64-faster%2dcpython-flag_object_maybe_in-3.14.0a0-bb874c3 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization | 463 ms                                                                | 478 ms: 1.03x slower                                                            |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (7): async_tree_io, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_none, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240606-linux-x86_64-python-f878d46e5614f08a9302-3.14.0a0-f878d46 | bm-20240607-linux-x86_64-faster%2dcpython-flag_object_maybe_in-3.14.0a0-bb874c3 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 190 ms                                                                | 190 ms: 1.00x slower                                                            |
| nbody          | 89.1 ms                                                               | 97.0 ms: 1.09x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                                    |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240606-linux-x86_64-python-f878d46e5614f08a9302-3.14.0a0-f878d46 | bm-20240607-linux-x86_64-faster%2dcpython-flag_object_maybe_in-3.14.0a0-bb874c3 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 234 ms                                                                | 222 ms: 1.05x faster                                                            |
| regex_v8       | 25.6 ms                                                               | 24.8 ms: 1.04x faster                                                           |
| regex_effbot   | 3.84 ms                                                               | 3.74 ms: 1.03x faster                                                           |
| regex_compile  | 133 ms                                                                | 135 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240606-linux-x86_64-python-f878d46e5614f08a9302-3.14.0a0-f878d46 | bm-20240607-linux-x86_64-faster%2dcpython-flag_object_maybe_in-3.14.0a0-bb874c3 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_dict          | 35.6 us                                                               | 33.7 us: 1.06x faster                                                           |
| pickle               | 12.0 us                                                               | 11.6 us: 1.03x faster                                                           |
| pickle_list          | 5.23 us                                                               | 5.15 us: 1.01x faster                                                           |
| json_loads           | 29.2 us                                                               | 28.8 us: 1.01x faster                                                           |
| xml_etree_iterparse  | 107 ms                                                                | 108 ms: 1.01x slower                                                            |
| unpickle_list        | 5.31 us                                                               | 5.38 us: 1.01x slower                                                           |
| xml_etree_process    | 60.2 ms                                                               | 61.1 ms: 1.02x slower                                                           |
| xml_etree_parse      | 157 ms                                                                | 159 ms: 1.02x slower                                                            |
| xml_etree_generate   | 85.8 ms                                                               | 87.3 ms: 1.02x slower                                                           |
| pickle_pure_python   | 305 us                                                                | 312 us: 1.02x slower                                                            |
| unpickle_pure_python | 218 us                                                                | 223 us: 1.02x slower                                                            |
| tomli_loads          | 2.15 sec                                                              | 2.21 sec: 1.03x slower                                                          |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (2): unpickle, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240606-linux-x86_64-python-f878d46e5614f08a9302-3.14.0a0-f878d46 | bm-20240607-linux-x86_64-faster%2dcpython-flag_object_maybe_in-3.14.0a0-bb874c3 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 7.09 ms                                                               | 7.12 ms: 1.00x slower                                                           |
| python_startup         | 10.7 ms                                                               | 10.7 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240606-linux-x86_64-python-f878d46e5614f08a9302-3.14.0a0-f878d46 | bm-20240607-linux-x86_64-faster%2dcpython-flag_object_maybe_in-3.14.0a0-bb874c3 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.4 ms                                                               | 11.5 ms: 1.01x slower                                                           |
| django_template | 34.3 ms                                                               | 35.3 ms: 1.03x slower                                                           |
| genshi_xml      | 50.6 ms                                                               | 52.1 ms: 1.03x slower                                                           |
| genshi_text     | 23.0 ms                                                               | 23.8 ms: 1.04x slower                                                           |
| Geometric mean  | (ref)                                                                 | 1.03x slower                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20240606-linux-x86_64-python-f878d46e5614f08a9302-3.14.0a0-f878d46 | bm-20240607-linux-x86_64-faster%2dcpython-flag_object_maybe_in-3.14.0a0-bb874c3 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_dict              | 35.6 us                                                               | 33.7 us: 1.06x faster                                                           |
| regex_dna                | 234 ms                                                                | 222 ms: 1.05x faster                                                            |
| mdp                      | 2.72 sec                                                              | 2.59 sec: 1.05x faster                                                          |
| scimark_sor              | 134 ms                                                                | 127 ms: 1.05x faster                                                            |
| pycparser                | 1.20 sec                                                              | 1.16 sec: 1.04x faster                                                          |
| regex_v8                 | 25.6 ms                                                               | 24.8 ms: 1.04x faster                                                           |
| pickle                   | 12.0 us                                                               | 11.6 us: 1.03x faster                                                           |
| regex_effbot             | 3.84 ms                                                               | 3.74 ms: 1.03x faster                                                           |
| scimark_sparse_mat_mult  | 5.11 ms                                                               | 5.01 ms: 1.02x faster                                                           |
| pathlib                  | 16.5 ms                                                               | 16.2 ms: 1.02x faster                                                           |
| pickle_list              | 5.23 us                                                               | 5.15 us: 1.01x faster                                                           |
| json_loads               | 29.2 us                                                               | 28.8 us: 1.01x faster                                                           |
| html5lib                 | 67.7 ms                                                               | 66.9 ms: 1.01x faster                                                           |
| typing_runtime_protocols | 167 us                                                                | 165 us: 1.01x faster                                                            |
| logging_silent           | 103 ns                                                                | 102 ns: 1.01x faster                                                            |
| sqlite_synth             | 2.94 us                                                               | 2.93 us: 1.01x faster                                                           |
| pidigits                 | 190 ms                                                                | 190 ms: 1.00x slower                                                            |
| asyncio_tcp_ssl          | 1.84 sec                                                              | 1.84 sec: 1.00x slower                                                          |
| tornado_http             | 94.4 ms                                                               | 94.8 ms: 1.00x slower                                                           |
| bench_thread_pool        | 836 us                                                                | 840 us: 1.00x slower                                                            |
| generators               | 29.5 ms                                                               | 29.6 ms: 1.00x slower                                                           |
| python_startup_no_site   | 7.09 ms                                                               | 7.12 ms: 1.00x slower                                                           |
| sqlglot_transpile        | 1.62 ms                                                               | 1.63 ms: 1.01x slower                                                           |
| mako                     | 11.4 ms                                                               | 11.5 ms: 1.01x slower                                                           |
| async_generators         | 446 ms                                                                | 449 ms: 1.01x slower                                                            |
| deepcopy_reduce          | 3.27 us                                                               | 3.29 us: 1.01x slower                                                           |
| python_startup           | 10.7 ms                                                               | 10.7 ms: 1.01x slower                                                           |
| scimark_monte_carlo      | 69.8 ms                                                               | 70.3 ms: 1.01x slower                                                           |
| richards                 | 48.9 ms                                                               | 49.4 ms: 1.01x slower                                                           |
| sympy_sum                | 155 ms                                                                | 157 ms: 1.01x slower                                                            |
| xml_etree_iterparse      | 107 ms                                                                | 108 ms: 1.01x slower                                                            |
| 2to3                     | 269 ms                                                                | 272 ms: 1.01x slower                                                            |
| dulwich_log              | 64.9 ms                                                               | 65.6 ms: 1.01x slower                                                           |
| unpickle_list            | 5.31 us                                                               | 5.38 us: 1.01x slower                                                           |
| scimark_fft              | 371 ms                                                                | 376 ms: 1.01x slower                                                            |
| telco                    | 8.30 ms                                                               | 8.41 ms: 1.01x slower                                                           |
| asyncio_tcp              | 493 ms                                                                | 500 ms: 1.01x slower                                                            |
| sympy_integrate          | 20.3 ms                                                               | 20.7 ms: 1.02x slower                                                           |
| xml_etree_process        | 60.2 ms                                                               | 61.1 ms: 1.02x slower                                                           |
| sympy_expand             | 467 ms                                                                | 475 ms: 1.02x slower                                                            |
| scimark_lu               | 117 ms                                                                | 119 ms: 1.02x slower                                                            |
| deepcopy                 | 363 us                                                                | 369 us: 1.02x slower                                                            |
| raytrace                 | 269 ms                                                                | 273 ms: 1.02x slower                                                            |
| sympy_str                | 277 ms                                                                | 281 ms: 1.02x slower                                                            |
| xml_etree_parse          | 157 ms                                                                | 159 ms: 1.02x slower                                                            |
| regex_compile            | 133 ms                                                                | 135 ms: 1.02x slower                                                            |
| xml_etree_generate       | 85.8 ms                                                               | 87.3 ms: 1.02x slower                                                           |
| chaos                    | 60.3 ms                                                               | 61.4 ms: 1.02x slower                                                           |
| sqlglot_optimize         | 54.6 ms                                                               | 55.6 ms: 1.02x slower                                                           |
| pickle_pure_python       | 305 us                                                                | 312 us: 1.02x slower                                                            |
| deepcopy_memo            | 39.4 us                                                               | 40.2 us: 1.02x slower                                                           |
| richards_super           | 54.9 ms                                                               | 56.0 ms: 1.02x slower                                                           |
| sqlglot_normalize        | 109 ms                                                                | 111 ms: 1.02x slower                                                            |
| go                       | 143 ms                                                                | 146 ms: 1.02x slower                                                            |
| unpickle_pure_python     | 218 us                                                                | 223 us: 1.02x slower                                                            |
| tomli_loads              | 2.15 sec                                                              | 2.21 sec: 1.03x slower                                                          |
| coroutines               | 22.7 ms                                                               | 23.3 ms: 1.03x slower                                                           |
| meteor_contest           | 108 ms                                                                | 111 ms: 1.03x slower                                                            |
| hexiom                   | 6.18 ms                                                               | 6.35 ms: 1.03x slower                                                           |
| django_template          | 34.3 ms                                                               | 35.3 ms: 1.03x slower                                                           |
| nqueens                  | 79.0 ms                                                               | 81.2 ms: 1.03x slower                                                           |
| deltablue                | 3.25 ms                                                               | 3.34 ms: 1.03x slower                                                           |
| pprint_pformat           | 1.52 sec                                                              | 1.57 sec: 1.03x slower                                                          |
| genshi_xml               | 50.6 ms                                                               | 52.1 ms: 1.03x slower                                                           |
| pprint_safe_repr         | 747 ms                                                                | 770 ms: 1.03x slower                                                            |
| async_tree_memoization   | 463 ms                                                                | 478 ms: 1.03x slower                                                            |
| logging_format           | 6.28 us                                                               | 6.48 us: 1.03x slower                                                           |
| crypto_pyaes             | 74.5 ms                                                               | 77.2 ms: 1.04x slower                                                           |
| genshi_text              | 23.0 ms                                                               | 23.8 ms: 1.04x slower                                                           |
| spectral_norm            | 114 ms                                                                | 118 ms: 1.04x slower                                                            |
| logging_simple           | 5.62 us                                                               | 5.87 us: 1.04x slower                                                           |
| pyflate                  | 485 ms                                                                | 514 ms: 1.06x slower                                                            |
| nbody                    | 89.1 ms                                                               | 97.0 ms: 1.09x slower                                                           |
| Geometric mean           | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (23): async_tree_io, unpickle, json_dumps, thrift, sqlglot_parse, comprehensions, fannkuch, json, float, async_tree_io_tg, asyncio_websockets, bench_mp_pool, create_gc_cycles, pylint, gc_traversal, docutils, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, coverage, dask, async_tree_memoization_tg, async_tree_none, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x