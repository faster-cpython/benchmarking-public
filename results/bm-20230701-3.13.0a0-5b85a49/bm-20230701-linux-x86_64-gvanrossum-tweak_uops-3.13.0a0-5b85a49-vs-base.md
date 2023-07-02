
# Results vs. base

- fork: gvanrossum
- ref: tweak_uops
- machine: linux-x86_64
- commit hash: 5b85a49
- commit date: 2023-07-01
- overall geometric mean: 1.02x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230701-linux-x86_64-python-822db860eada721742f8-3.13.0a0-822db86 | bm-20230701-linux-x86_64-gvanrossum-tweak_uops-3.13.0a0-5b85a49 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| docutils       | 2.68 sec                                                              | 2.71 sec: 1.01x slower                                          |
| tornado_http   | 96.5 ms                                                               | 97.1 ms: 1.01x slower                                           |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230701-linux-x86_64-python-822db860eada721742f8-3.13.0a0-822db86 | bm-20230701-linux-x86_64-gvanrossum-tweak_uops-3.13.0a0-5b85a49 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| pidigits       | 197 ms                                                                | 197 ms: 1.00x slower                                            |
| float          | 80.6 ms                                                               | 82.6 ms: 1.03x slower                                           |
| nbody          | 90.9 ms                                                               | 95.8 ms: 1.05x slower                                           |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230701-linux-x86_64-python-822db860eada721742f8-3.13.0a0-822db86 | bm-20230701-linux-x86_64-gvanrossum-tweak_uops-3.13.0a0-5b85a49 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_v8       | 22.6 ms                                                               | 22.7 ms: 1.00x slower                                           |
| regex_dna      | 212 ms                                                                | 217 ms: 1.02x slower                                            |
| regex_compile  | 137 ms                                                                | 141 ms: 1.02x slower                                            |
| regex_effbot   | 3.68 ms                                                               | 3.85 ms: 1.05x slower                                           |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230701-linux-x86_64-python-822db860eada721742f8-3.13.0a0-822db86 | bm-20230701-linux-x86_64-gvanrossum-tweak_uops-3.13.0a0-5b85a49 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| pickle               | 10.7 us                                                               | 10.5 us: 1.02x faster                                           |
| json_dumps           | 9.86 ms                                                               | 9.74 ms: 1.01x faster                                           |
| unpickle             | 15.1 us                                                               | 15.0 us: 1.01x faster                                           |
| unpickle_list        | 5.08 us                                                               | 5.06 us: 1.00x faster                                           |
| pickle_list          | 4.54 us                                                               | 4.59 us: 1.01x slower                                           |
| json_loads           | 25.5 us                                                               | 25.8 us: 1.01x slower                                           |
| xml_etree_generate   | 84.1 ms                                                               | 85.5 ms: 1.02x slower                                           |
| xml_etree_process    | 58.2 ms                                                               | 59.2 ms: 1.02x slower                                           |
| pickle_dict          | 31.8 us                                                               | 32.4 us: 1.02x slower                                           |
| xml_etree_iterparse  | 103 ms                                                                | 106 ms: 1.03x slower                                            |
| unpickle_pure_python | 215 us                                                                | 223 us: 1.04x slower                                            |
| tomli_loads          | 2.31 sec                                                              | 2.52 sec: 1.09x slower                                          |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                    |

Benchmark hidden because not significant (2): pickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230701-linux-x86_64-python-822db860eada721742f8-3.13.0a0-822db86 | bm-20230701-linux-x86_64-gvanrossum-tweak_uops-3.13.0a0-5b85a49 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 6.71 ms                                                               | 6.72 ms: 1.00x slower                                           |
| python_startup         | 9.22 ms                                                               | 9.24 ms: 1.00x slower                                           |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230701-linux-x86_64-python-822db860eada721742f8-3.13.0a0-822db86 | bm-20230701-linux-x86_64-gvanrossum-tweak_uops-3.13.0a0-5b85a49 |
|-----------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| mako      | 10.6 ms                                                               | 10.9 ms: 1.03x slower                                           |

All benchmarks:
===============

| Benchmark                | bm-20230701-linux-x86_64-python-822db860eada721742f8-3.13.0a0-822db86 | bm-20230701-linux-x86_64-gvanrossum-tweak_uops-3.13.0a0-5b85a49 |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| logging_silent           | 106 ns                                                                | 103 ns: 1.03x faster                                            |
| logging_format           | 6.70 us                                                               | 6.54 us: 1.02x faster                                           |
| pickle                   | 10.7 us                                                               | 10.5 us: 1.02x faster                                           |
| logging_simple           | 6.09 us                                                               | 5.99 us: 1.02x faster                                           |
| json_dumps               | 9.86 ms                                                               | 9.74 ms: 1.01x faster                                           |
| pprint_safe_repr         | 733 ms                                                                | 726 ms: 1.01x faster                                            |
| scimark_sor              | 122 ms                                                                | 120 ms: 1.01x faster                                            |
| unpickle                 | 15.1 us                                                               | 15.0 us: 1.01x faster                                           |
| generators               | 30.1 ms                                                               | 29.9 ms: 1.01x faster                                           |
| pprint_pformat           | 1.50 sec                                                              | 1.49 sec: 1.01x faster                                          |
| unpickle_list            | 5.08 us                                                               | 5.06 us: 1.00x faster                                           |
| asyncio_tcp_ssl          | 1.80 sec                                                              | 1.79 sec: 1.00x faster                                          |
| python_startup_no_site   | 6.71 ms                                                               | 6.72 ms: 1.00x slower                                           |
| python_startup           | 9.22 ms                                                               | 9.24 ms: 1.00x slower                                           |
| regex_v8                 | 22.6 ms                                                               | 22.7 ms: 1.00x slower                                           |
| pidigits                 | 197 ms                                                                | 197 ms: 1.00x slower                                            |
| create_gc_cycles         | 1.51 ms                                                               | 1.52 ms: 1.00x slower                                           |
| async_tree_io            | 1.20 sec                                                              | 1.21 sec: 1.01x slower                                          |
| deepcopy                 | 350 us                                                                | 352 us: 1.01x slower                                            |
| tornado_http             | 96.5 ms                                                               | 97.1 ms: 1.01x slower                                           |
| asyncio_tcp              | 510 ms                                                                | 514 ms: 1.01x slower                                            |
| coroutines               | 22.3 ms                                                               | 22.4 ms: 1.01x slower                                           |
| async_tree_memoization   | 590 ms                                                                | 596 ms: 1.01x slower                                            |
| chaos                    | 60.3 ms                                                               | 60.9 ms: 1.01x slower                                           |
| pickle_list              | 4.54 us                                                               | 4.59 us: 1.01x slower                                           |
| mypy2                    | 337 ms                                                                | 341 ms: 1.01x slower                                            |
| docutils                 | 2.68 sec                                                              | 2.71 sec: 1.01x slower                                          |
| dulwich_log              | 65.6 ms                                                               | 66.4 ms: 1.01x slower                                           |
| telco                    | 7.21 ms                                                               | 7.30 ms: 1.01x slower                                           |
| json_loads               | 25.5 us                                                               | 25.8 us: 1.01x slower                                           |
| sqlglot_parse            | 1.34 ms                                                               | 1.36 ms: 1.02x slower                                           |
| sqlglot_transpile        | 1.66 ms                                                               | 1.69 ms: 1.02x slower                                           |
| xml_etree_generate       | 84.1 ms                                                               | 85.5 ms: 1.02x slower                                           |
| xml_etree_process        | 58.2 ms                                                               | 59.2 ms: 1.02x slower                                           |
| scimark_lu               | 111 ms                                                                | 113 ms: 1.02x slower                                            |
| bench_thread_pool        | 820 us                                                                | 835 us: 1.02x slower                                            |
| pickle_dict              | 31.8 us                                                               | 32.4 us: 1.02x slower                                           |
| raytrace                 | 269 ms                                                                | 274 ms: 1.02x slower                                            |
| regex_dna                | 212 ms                                                                | 217 ms: 1.02x slower                                            |
| deltablue                | 3.30 ms                                                               | 3.38 ms: 1.02x slower                                           |
| regex_compile            | 137 ms                                                                | 141 ms: 1.02x slower                                            |
| pycparser                | 1.17 sec                                                              | 1.20 sec: 1.02x slower                                          |
| float                    | 80.6 ms                                                               | 82.6 ms: 1.03x slower                                           |
| deepcopy_reduce          | 3.17 us                                                               | 3.25 us: 1.03x slower                                           |
| scimark_monte_carlo      | 71.9 ms                                                               | 73.8 ms: 1.03x slower                                           |
| pyflate                  | 444 ms                                                                | 458 ms: 1.03x slower                                            |
| comprehensions           | 20.5 us                                                               | 21.1 us: 1.03x slower                                           |
| sqlglot_optimize         | 53.2 ms                                                               | 54.9 ms: 1.03x slower                                           |
| xml_etree_iterparse      | 103 ms                                                                | 106 ms: 1.03x slower                                            |
| typing_runtime_protocols | 143 us                                                                | 148 us: 1.03x slower                                            |
| mako                     | 10.6 ms                                                               | 10.9 ms: 1.03x slower                                           |
| go                       | 139 ms                                                                | 143 ms: 1.03x slower                                            |
| sqlglot_normalize        | 106 ms                                                                | 110 ms: 1.03x slower                                            |
| scimark_fft              | 357 ms                                                                | 370 ms: 1.04x slower                                            |
| deepcopy_memo            | 37.2 us                                                               | 38.5 us: 1.04x slower                                           |
| unpickle_pure_python     | 215 us                                                                | 223 us: 1.04x slower                                            |
| nqueens                  | 79.8 ms                                                               | 83.0 ms: 1.04x slower                                           |
| async_generators         | 448 ms                                                                | 466 ms: 1.04x slower                                            |
| spectral_norm            | 107 ms                                                                | 112 ms: 1.04x slower                                            |
| regex_effbot             | 3.68 ms                                                               | 3.85 ms: 1.05x slower                                           |
| nbody                    | 90.9 ms                                                               | 95.8 ms: 1.05x slower                                           |
| meteor_contest           | 105 ms                                                                | 113 ms: 1.08x slower                                            |
| scimark_sparse_mat_mult  | 4.74 ms                                                               | 5.11 ms: 1.08x slower                                           |
| hexiom                   | 6.07 ms                                                               | 6.57 ms: 1.08x slower                                           |
| tomli_loads              | 2.31 sec                                                              | 2.52 sec: 1.09x slower                                          |
| mdp                      | 2.53 sec                                                              | 2.77 sec: 1.09x slower                                          |
| gc_traversal             | 3.61 ms                                                               | 3.98 ms: 1.10x slower                                           |
| unpack_sequence          | 42.3 ns                                                               | 46.9 ns: 1.11x slower                                           |
| fannkuch                 | 393 ms                                                                | 437 ms: 1.11x slower                                            |
| Geometric mean           | (ref)                                                                 | 1.02x slower                                                    |

Benchmark hidden because not significant (13): async_tree_cpu_io_mixed, crypto_pyaes, json, bench_mp_pool, pickle_pure_python, richards_super, coverage, richards, sqlite_synth, async_tree_none, dask, xml_etree_parse, pathlib
