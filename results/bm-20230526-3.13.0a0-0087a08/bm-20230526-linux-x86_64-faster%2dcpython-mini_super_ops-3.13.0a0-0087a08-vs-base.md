
# Results vs. base

- fork: faster-cpython
- ref: mini_super_ops
- machine: linux-x86_64
- commit hash: 0087a08
- commit date: 2023-05-26
- overall geometric mean: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230530-linux-x86_64-python-4b65d5638c607747e2f5-3.13.0a0-4b65d56 | bm-20230526-linux-x86_64-faster%2dcpython-mini_super_ops-3.13.0a0-0087a08 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 2.75 sec                                                              | 2.67 sec: 1.03x faster                                                    |
| tornado_http   | 103 ms                                                                | 96.1 ms: 1.07x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.05x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230530-linux-x86_64-python-4b65d5638c607747e2f5-3.13.0a0-4b65d56 | bm-20230526-linux-x86_64-faster%2dcpython-mini_super_ops-3.13.0a0-0087a08 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 197 ms                                                                | 192 ms: 1.03x faster                                                      |
| float          | 81.3 ms                                                               | 80.0 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                              |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230530-linux-x86_64-python-4b65d5638c607747e2f5-3.13.0a0-4b65d56 | bm-20230526-linux-x86_64-faster%2dcpython-mini_super_ops-3.13.0a0-0087a08 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                                | 137 ms: 1.05x faster                                                      |
| regex_v8       | 21.9 ms                                                               | 22.2 ms: 1.01x slower                                                     |
| regex_dna      | 209 ms                                                                | 216 ms: 1.03x slower                                                      |
| regex_effbot   | 3.56 ms                                                               | 3.85 ms: 1.08x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230530-linux-x86_64-python-4b65d5638c607747e2f5-3.13.0a0-4b65d56 | bm-20230526-linux-x86_64-faster%2dcpython-mini_super_ops-3.13.0a0-0087a08 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_pure_python | 219 us                                                                | 211 us: 1.04x faster                                                      |
| pickle_pure_python   | 316 us                                                                | 306 us: 1.03x faster                                                      |
| unpickle_list        | 4.99 us                                                               | 4.88 us: 1.02x faster                                                     |
| xml_etree_process    | 59.7 ms                                                               | 58.3 ms: 1.02x faster                                                     |
| tomli_loads          | 2.23 sec                                                              | 2.19 sec: 1.02x faster                                                    |
| pickle               | 11.0 us                                                               | 10.9 us: 1.01x faster                                                     |
| xml_etree_generate   | 85.7 ms                                                               | 84.7 ms: 1.01x faster                                                     |
| json_loads           | 25.1 us                                                               | 25.0 us: 1.00x faster                                                     |
| pickle_list          | 4.68 us                                                               | 4.72 us: 1.01x slower                                                     |
| pickle_dict          | 30.9 us                                                               | 32.0 us: 1.04x slower                                                     |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                              |

Benchmark hidden because not significant (4): unpickle, xml_etree_parse, xml_etree_iterparse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230530-linux-x86_64-python-4b65d5638c607747e2f5-3.13.0a0-4b65d56 | bm-20230526-linux-x86_64-faster%2dcpython-mini_super_ops-3.13.0a0-0087a08 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.76 ms                                                               | 6.71 ms: 1.01x faster                                                     |
| python_startup         | 9.30 ms                                                               | 9.24 ms: 1.01x faster                                                     |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                              |

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20230530-linux-x86_64-python-4b65d5638c607747e2f5-3.13.0a0-4b65d56 | bm-20230526-linux-x86_64-faster%2dcpython-mini_super_ops-3.13.0a0-0087a08 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deltablue                | 3.55 ms                                                               | 3.22 ms: 1.10x faster                                                     |
| logging_format           | 7.05 us                                                               | 6.53 us: 1.08x faster                                                     |
| generators               | 31.8 ms                                                               | 29.8 ms: 1.07x faster                                                     |
| tornado_http             | 103 ms                                                                | 96.1 ms: 1.07x faster                                                     |
| logging_simple           | 6.38 us                                                               | 6.00 us: 1.06x faster                                                     |
| coroutines               | 23.1 ms                                                               | 21.8 ms: 1.06x faster                                                     |
| logging_silent           | 102 ns                                                                | 96.8 ns: 1.06x faster                                                     |
| scimark_sor              | 123 ms                                                                | 116 ms: 1.06x faster                                                      |
| regex_compile            | 144 ms                                                                | 137 ms: 1.05x faster                                                      |
| dulwich_log              | 68.0 ms                                                               | 64.8 ms: 1.05x faster                                                     |
| sqlglot_parse            | 1.36 ms                                                               | 1.30 ms: 1.05x faster                                                     |
| hexiom                   | 6.16 ms                                                               | 5.92 ms: 1.04x faster                                                     |
| pycparser                | 1.19 sec                                                              | 1.15 sec: 1.04x faster                                                    |
| sqlglot_normalize        | 110 ms                                                                | 106 ms: 1.04x faster                                                      |
| deepcopy                 | 359 us                                                                | 345 us: 1.04x faster                                                      |
| sqlglot_transpile        | 1.68 ms                                                               | 1.62 ms: 1.04x faster                                                     |
| unpickle_pure_python     | 219 us                                                                | 211 us: 1.04x faster                                                      |
| dask                     | 539 ms                                                                | 519 ms: 1.04x faster                                                      |
| spectral_norm            | 108 ms                                                                | 104 ms: 1.03x faster                                                      |
| pickle_pure_python       | 316 us                                                                | 306 us: 1.03x faster                                                      |
| comprehensions           | 20.8 us                                                               | 20.2 us: 1.03x faster                                                     |
| sqlglot_optimize         | 54.1 ms                                                               | 52.5 ms: 1.03x faster                                                     |
| scimark_lu               | 117 ms                                                                | 113 ms: 1.03x faster                                                      |
| pidigits                 | 197 ms                                                                | 192 ms: 1.03x faster                                                      |
| docutils                 | 2.75 sec                                                              | 2.67 sec: 1.03x faster                                                    |
| nqueens                  | 81.1 ms                                                               | 78.9 ms: 1.03x faster                                                     |
| mypy2                    | 345 ms                                                                | 336 ms: 1.03x faster                                                      |
| typing_runtime_protocols | 143 us                                                                | 139 us: 1.03x faster                                                      |
| richards                 | 44.9 ms                                                               | 43.8 ms: 1.03x faster                                                     |
| async_generators         | 455 ms                                                                | 444 ms: 1.02x faster                                                      |
| unpickle_list            | 4.99 us                                                               | 4.88 us: 1.02x faster                                                     |
| xml_etree_process        | 59.7 ms                                                               | 58.3 ms: 1.02x faster                                                     |
| chaos                    | 64.2 ms                                                               | 62.7 ms: 1.02x faster                                                     |
| fannkuch                 | 391 ms                                                                | 383 ms: 1.02x faster                                                      |
| mdp                      | 2.59 sec                                                              | 2.53 sec: 1.02x faster                                                    |
| deepcopy_reduce          | 3.17 us                                                               | 3.10 us: 1.02x faster                                                     |
| scimark_monte_carlo      | 72.8 ms                                                               | 71.3 ms: 1.02x faster                                                     |
| pprint_pformat           | 1.50 sec                                                              | 1.47 sec: 1.02x faster                                                    |
| telco                    | 6.91 ms                                                               | 6.77 ms: 1.02x faster                                                     |
| meteor_contest           | 105 ms                                                                | 103 ms: 1.02x faster                                                      |
| deepcopy_memo            | 37.5 us                                                               | 36.8 us: 1.02x faster                                                     |
| tomli_loads              | 2.23 sec                                                              | 2.19 sec: 1.02x faster                                                    |
| pathlib                  | 18.8 ms                                                               | 18.5 ms: 1.02x faster                                                     |
| raytrace                 | 299 ms                                                                | 294 ms: 1.02x faster                                                      |
| pprint_safe_repr         | 732 ms                                                                | 720 ms: 1.02x faster                                                      |
| float                    | 81.3 ms                                                               | 80.0 ms: 1.02x faster                                                     |
| coverage                 | 96.9 ms                                                               | 95.4 ms: 1.02x faster                                                     |
| bench_thread_pool        | 829 us                                                                | 817 us: 1.01x faster                                                      |
| async_tree_none          | 499 ms                                                                | 492 ms: 1.01x faster                                                      |
| richards_super           | 50.2 ms                                                               | 49.6 ms: 1.01x faster                                                     |
| async_tree_memoization   | 604 ms                                                                | 597 ms: 1.01x faster                                                      |
| pickle                   | 11.0 us                                                               | 10.9 us: 1.01x faster                                                     |
| asyncio_tcp_ssl          | 1.81 sec                                                              | 1.79 sec: 1.01x faster                                                    |
| xml_etree_generate       | 85.7 ms                                                               | 84.7 ms: 1.01x faster                                                     |
| python_startup_no_site   | 6.76 ms                                                               | 6.71 ms: 1.01x faster                                                     |
| python_startup           | 9.30 ms                                                               | 9.24 ms: 1.01x faster                                                     |
| async_tree_io            | 1.24 sec                                                              | 1.23 sec: 1.01x faster                                                    |
| crypto_pyaes             | 78.1 ms                                                               | 77.7 ms: 1.00x faster                                                     |
| json_loads               | 25.1 us                                                               | 25.0 us: 1.00x faster                                                     |
| asyncio_tcp              | 513 ms                                                                | 511 ms: 1.00x faster                                                      |
| scimark_fft              | 349 ms                                                                | 352 ms: 1.01x slower                                                      |
| pickle_list              | 4.68 us                                                               | 4.72 us: 1.01x slower                                                     |
| regex_v8                 | 21.9 ms                                                               | 22.2 ms: 1.01x slower                                                     |
| pyflate                  | 440 ms                                                                | 446 ms: 1.01x slower                                                      |
| scimark_sparse_mat_mult  | 4.82 ms                                                               | 4.90 ms: 1.02x slower                                                     |
| regex_dna                | 209 ms                                                                | 216 ms: 1.03x slower                                                      |
| pickle_dict              | 30.9 us                                                               | 32.0 us: 1.04x slower                                                     |
| gc_traversal             | 3.82 ms                                                               | 3.99 ms: 1.04x slower                                                     |
| regex_effbot             | 3.56 ms                                                               | 3.85 ms: 1.08x slower                                                     |
| unpack_sequence          | 42.4 ns                                                               | 48.7 ns: 1.15x slower                                                     |
| Geometric mean           | (ref)                                                                 | 1.02x faster                                                              |

Benchmark hidden because not significant (12): unpickle, async_tree_cpu_io_mixed, xml_etree_parse, nbody, xml_etree_iterparse, json_dumps, bench_mp_pool, create_gc_cycles, mako, go, json, sqlite_synth
