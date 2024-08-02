# Results vs. base

- fork: faster-cpython
- ref: deferred_rc_overhead
- machine: linux-x86_64
- commit hash: e12729e
- commit date: 2024-05-30
- overall geometric mean: 1.01x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240529-linux-x86_64-python-1f481fd3275dbc12a88c-3.14.0a0-1f481fd | bm-20240530-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-e12729e |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 268 ms                                                                | 274 ms: 1.02x slower                                                            |
| docutils       | 2.78 sec                                                              | 2.81 sec: 1.01x slower                                                          |
| html5lib       | 68.2 ms                                                               | 66.7 ms: 1.02x faster                                                           |
| tornado_http   | 93.4 ms                                                               | 94.3 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_none_tg, async_tree_memoization_tg, async_tree_io_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240529-linux-x86_64-python-1f481fd3275dbc12a88c-3.14.0a0-1f481fd | bm-20240530-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-e12729e |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 189 ms                                                                | 189 ms: 1.00x slower                                                            |
| float          | 78.2 ms                                                               | 79.6 ms: 1.02x slower                                                           |
| nbody          | 88.8 ms                                                               | 92.4 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240529-linux-x86_64-python-1f481fd3275dbc12a88c-3.14.0a0-1f481fd | bm-20240530-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-e12729e |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 232 ms                                                                | 226 ms: 1.03x faster                                                            |
| regex_v8       | 24.4 ms                                                               | 24.6 ms: 1.01x slower                                                           |
| regex_compile  | 135 ms                                                                | 137 ms: 1.02x slower                                                            |
| regex_effbot   | 3.70 ms                                                               | 3.80 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240529-linux-x86_64-python-1f481fd3275dbc12a88c-3.14.0a0-1f481fd | bm-20240530-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-e12729e |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle               | 12.1 us                                                               | 11.7 us: 1.04x faster                                                           |
| pickle_dict          | 36.3 us                                                               | 35.3 us: 1.03x faster                                                           |
| json_dumps           | 10.7 ms                                                               | 10.6 ms: 1.01x faster                                                           |
| unpickle_list        | 5.50 us                                                               | 5.43 us: 1.01x faster                                                           |
| pickle_list          | 5.18 us                                                               | 5.14 us: 1.01x faster                                                           |
| xml_etree_process    | 61.6 ms                                                               | 61.3 ms: 1.00x faster                                                           |
| xml_etree_generate   | 88.6 ms                                                               | 88.3 ms: 1.00x faster                                                           |
| xml_etree_iterparse  | 107 ms                                                                | 108 ms: 1.01x slower                                                            |
| pickle_pure_python   | 305 us                                                                | 313 us: 1.03x slower                                                            |
| tomli_loads          | 2.15 sec                                                              | 2.22 sec: 1.03x slower                                                          |
| unpickle_pure_python | 216 us                                                                | 225 us: 1.04x slower                                                            |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (3): xml_etree_parse, unpickle, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240529-linux-x86_64-python-1f481fd3275dbc12a88c-3.14.0a0-1f481fd | bm-20240530-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-e12729e |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                               | 10.6 ms: 1.01x faster                                                           |
| python_startup_no_site | 7.12 ms                                                               | 7.08 ms: 1.00x faster                                                           |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240529-linux-x86_64-python-1f481fd3275dbc12a88c-3.14.0a0-1f481fd | bm-20240530-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-e12729e |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                               | 11.4 ms: 1.02x slower                                                           |
| django_template | 35.1 ms                                                               | 35.8 ms: 1.02x slower                                                           |
| genshi_xml      | 51.4 ms                                                               | 52.6 ms: 1.02x slower                                                           |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                                    |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20240529-linux-x86_64-python-1f481fd3275dbc12a88c-3.14.0a0-1f481fd | bm-20240530-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-e12729e |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                      | 2.79 sec                                                              | 2.59 sec: 1.08x faster                                                          |
| gc_traversal             | 3.97 ms                                                               | 3.72 ms: 1.07x faster                                                           |
| pickle                   | 12.1 us                                                               | 11.7 us: 1.04x faster                                                           |
| pickle_dict              | 36.3 us                                                               | 35.3 us: 1.03x faster                                                           |
| regex_dna                | 232 ms                                                                | 226 ms: 1.03x faster                                                            |
| html5lib                 | 68.2 ms                                                               | 66.7 ms: 1.02x faster                                                           |
| json_dumps               | 10.7 ms                                                               | 10.6 ms: 1.01x faster                                                           |
| unpickle_list            | 5.50 us                                                               | 5.43 us: 1.01x faster                                                           |
| coroutines               | 23.9 ms                                                               | 23.7 ms: 1.01x faster                                                           |
| json                     | 5.32 ms                                                               | 5.28 ms: 1.01x faster                                                           |
| python_startup           | 10.6 ms                                                               | 10.6 ms: 1.01x faster                                                           |
| pickle_list              | 5.18 us                                                               | 5.14 us: 1.01x faster                                                           |
| python_startup_no_site   | 7.12 ms                                                               | 7.08 ms: 1.00x faster                                                           |
| xml_etree_process        | 61.6 ms                                                               | 61.3 ms: 1.00x faster                                                           |
| xml_etree_generate       | 88.6 ms                                                               | 88.3 ms: 1.00x faster                                                           |
| pidigits                 | 189 ms                                                                | 189 ms: 1.00x slower                                                            |
| create_gc_cycles         | 1.78 ms                                                               | 1.79 ms: 1.01x slower                                                           |
| regex_v8                 | 24.4 ms                                                               | 24.6 ms: 1.01x slower                                                           |
| typing_runtime_protocols | 170 us                                                                | 172 us: 1.01x slower                                                            |
| tornado_http             | 93.4 ms                                                               | 94.3 ms: 1.01x slower                                                           |
| xml_etree_iterparse      | 107 ms                                                                | 108 ms: 1.01x slower                                                            |
| coverage                 | 92.7 ms                                                               | 93.6 ms: 1.01x slower                                                           |
| docutils                 | 2.78 sec                                                              | 2.81 sec: 1.01x slower                                                          |
| sqlite_synth             | 2.94 us                                                               | 2.98 us: 1.01x slower                                                           |
| sympy_sum                | 155 ms                                                                | 157 ms: 1.01x slower                                                            |
| scimark_sparse_mat_mult  | 5.18 ms                                                               | 5.25 ms: 1.01x slower                                                           |
| sympy_expand             | 470 ms                                                                | 477 ms: 1.01x slower                                                            |
| bench_thread_pool        | 824 us                                                                | 836 us: 1.02x slower                                                            |
| comprehensions           | 16.8 us                                                               | 17.0 us: 1.02x slower                                                           |
| telco                    | 8.46 ms                                                               | 8.60 ms: 1.02x slower                                                           |
| mako                     | 11.2 ms                                                               | 11.4 ms: 1.02x slower                                                           |
| float                    | 78.2 ms                                                               | 79.6 ms: 1.02x slower                                                           |
| sympy_str                | 279 ms                                                                | 284 ms: 1.02x slower                                                            |
| deepcopy                 | 367 us                                                                | 374 us: 1.02x slower                                                            |
| sympy_integrate          | 20.3 ms                                                               | 20.7 ms: 1.02x slower                                                           |
| logging_simple           | 5.68 us                                                               | 5.80 us: 1.02x slower                                                           |
| regex_compile            | 135 ms                                                                | 137 ms: 1.02x slower                                                            |
| deepcopy_reduce          | 3.29 us                                                               | 3.35 us: 1.02x slower                                                           |
| generators               | 29.3 ms                                                               | 29.9 ms: 1.02x slower                                                           |
| dulwich_log              | 65.2 ms                                                               | 66.6 ms: 1.02x slower                                                           |
| 2to3                     | 268 ms                                                                | 274 ms: 1.02x slower                                                            |
| django_template          | 35.1 ms                                                               | 35.8 ms: 1.02x slower                                                           |
| asyncio_tcp              | 497 ms                                                                | 508 ms: 1.02x slower                                                            |
| genshi_xml               | 51.4 ms                                                               | 52.6 ms: 1.02x slower                                                           |
| richards                 | 48.5 ms                                                               | 49.8 ms: 1.03x slower                                                           |
| logging_silent           | 100 ns                                                                | 103 ns: 1.03x slower                                                            |
| pickle_pure_python       | 305 us                                                                | 313 us: 1.03x slower                                                            |
| scimark_fft              | 374 ms                                                                | 384 ms: 1.03x slower                                                            |
| meteor_contest           | 109 ms                                                                | 112 ms: 1.03x slower                                                            |
| go                       | 143 ms                                                                | 147 ms: 1.03x slower                                                            |
| regex_effbot             | 3.70 ms                                                               | 3.80 ms: 1.03x slower                                                           |
| sqlglot_transpile        | 1.61 ms                                                               | 1.65 ms: 1.03x slower                                                           |
| sqlglot_optimize         | 54.7 ms                                                               | 56.3 ms: 1.03x slower                                                           |
| async_generators         | 439 ms                                                                | 452 ms: 1.03x slower                                                            |
| sqlglot_normalize        | 109 ms                                                                | 112 ms: 1.03x slower                                                            |
| sqlglot_parse            | 1.31 ms                                                               | 1.35 ms: 1.03x slower                                                           |
| deltablue                | 3.23 ms                                                               | 3.33 ms: 1.03x slower                                                           |
| logging_format           | 6.27 us                                                               | 6.47 us: 1.03x slower                                                           |
| fannkuch                 | 393 ms                                                                | 406 ms: 1.03x slower                                                            |
| tomli_loads              | 2.15 sec                                                              | 2.22 sec: 1.03x slower                                                          |
| chaos                    | 60.5 ms                                                               | 62.6 ms: 1.03x slower                                                           |
| scimark_sor              | 123 ms                                                                | 128 ms: 1.04x slower                                                            |
| richards_super           | 54.2 ms                                                               | 56.2 ms: 1.04x slower                                                           |
| pprint_pformat           | 1.52 sec                                                              | 1.57 sec: 1.04x slower                                                          |
| scimark_lu               | 116 ms                                                                | 120 ms: 1.04x slower                                                            |
| unpickle_pure_python     | 216 us                                                                | 225 us: 1.04x slower                                                            |
| nbody                    | 88.8 ms                                                               | 92.4 ms: 1.04x slower                                                           |
| scimark_monte_carlo      | 69.0 ms                                                               | 71.9 ms: 1.04x slower                                                           |
| spectral_norm            | 113 ms                                                                | 118 ms: 1.04x slower                                                            |
| raytrace                 | 263 ms                                                                | 274 ms: 1.04x slower                                                            |
| nqueens                  | 79.7 ms                                                               | 83.2 ms: 1.04x slower                                                           |
| deepcopy_memo            | 39.7 us                                                               | 41.5 us: 1.04x slower                                                           |
| pprint_safe_repr         | 740 ms                                                                | 774 ms: 1.05x slower                                                            |
| hexiom                   | 6.13 ms                                                               | 6.43 ms: 1.05x slower                                                           |
| crypto_pyaes             | 74.3 ms                                                               | 78.0 ms: 1.05x slower                                                           |
| Geometric mean           | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (21): xml_etree_parse, unpickle, json_loads, pathlib, asyncio_tcp_ssl, asyncio_websockets, thrift, bench_mp_pool, genshi_text, pycparser, pyflate, async_tree_cpu_io_mixed, dask, async_tree_io, async_tree_cpu_io_mixed_tg, pylint, async_tree_none, async_tree_none_tg, async_tree_memoization_tg, async_tree_io_tg, async_tree_memoization

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.02x