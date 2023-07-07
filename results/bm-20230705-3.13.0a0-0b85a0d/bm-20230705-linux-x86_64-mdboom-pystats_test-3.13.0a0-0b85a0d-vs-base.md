
# Results vs. base

- fork: mdboom
- ref: pystats_test
- machine: linux-x86_64
- commit hash: 0b85a0d
- commit date: 2023-07-05
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230705-linux-x86_64-python-12a98138083589314d3d-3.13.0a0-12a9813 | bm-20230705-linux-x86_64-mdboom-pystats_test-3.13.0a0-0b85a0d |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 80.5 ms                                                               | 79.7 ms: 1.01x faster                                         |
| pidigits       | 197 ms                                                                | 197 ms: 1.00x faster                                          |
| nbody          | 88.4 ms                                                               | 89.9 ms: 1.02x slower                                         |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230705-linux-x86_64-python-12a98138083589314d3d-3.13.0a0-12a9813 | bm-20230705-linux-x86_64-mdboom-pystats_test-3.13.0a0-0b85a0d |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_effbot   | 3.53 ms                                                               | 3.44 ms: 1.03x faster                                         |
| regex_compile  | 138 ms                                                                | 137 ms: 1.00x faster                                          |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                  |

Benchmark hidden because not significant (2): regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20230705-linux-x86_64-python-12a98138083589314d3d-3.13.0a0-12a9813 | bm-20230705-linux-x86_64-mdboom-pystats_test-3.13.0a0-0b85a0d |
|---------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| pickle_dict         | 31.9 us                                                               | 31.0 us: 1.03x faster                                         |
| json_loads          | 26.2 us                                                               | 25.7 us: 1.02x faster                                         |
| xml_etree_parse     | 154 ms                                                                | 153 ms: 1.01x faster                                          |
| xml_etree_iterparse | 104 ms                                                                | 103 ms: 1.01x faster                                          |
| xml_etree_generate  | 84.5 ms                                                               | 84.9 ms: 1.00x slower                                         |
| xml_etree_process   | 58.0 ms                                                               | 58.3 ms: 1.01x slower                                         |
| pickle_pure_python  | 305 us                                                                | 307 us: 1.01x slower                                          |
| unpickle            | 14.7 us                                                               | 14.8 us: 1.01x slower                                         |
| pickle_list         | 4.48 us                                                               | 4.56 us: 1.02x slower                                         |
| Geometric mean      | (ref)                                                                 | 1.00x faster                                                  |

Benchmark hidden because not significant (5): json_dumps, unpickle_pure_python, unpickle_list, tomli_loads, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230705-linux-x86_64-python-12a98138083589314d3d-3.13.0a0-12a9813 | bm-20230705-linux-x86_64-mdboom-pystats_test-3.13.0a0-0b85a0d |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup_no_site | 6.73 ms                                                               | 6.68 ms: 1.01x faster                                         |
| python_startup         | 9.25 ms                                                               | 9.19 ms: 1.01x faster                                         |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230705-linux-x86_64-python-12a98138083589314d3d-3.13.0a0-12a9813 | bm-20230705-linux-x86_64-mdboom-pystats_test-3.13.0a0-0b85a0d |
|-----------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| mako      | 10.6 ms                                                               | 10.7 ms: 1.00x slower                                         |

All benchmarks:
===============

| Benchmark                | bm-20230705-linux-x86_64-python-12a98138083589314d3d-3.13.0a0-12a9813 | bm-20230705-linux-x86_64-mdboom-pystats_test-3.13.0a0-0b85a0d |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| unpack_sequence          | 48.1 ns                                                               | 45.3 ns: 1.06x faster                                         |
| scimark_sparse_mat_mult  | 4.83 ms                                                               | 4.63 ms: 1.04x faster                                         |
| pickle_dict              | 31.9 us                                                               | 31.0 us: 1.03x faster                                         |
| regex_effbot             | 3.53 ms                                                               | 3.44 ms: 1.03x faster                                         |
| json_loads               | 26.2 us                                                               | 25.7 us: 1.02x faster                                         |
| typing_runtime_protocols | 148 us                                                                | 146 us: 1.02x faster                                          |
| create_gc_cycles         | 1.51 ms                                                               | 1.49 ms: 1.01x faster                                         |
| meteor_contest           | 105 ms                                                                | 104 ms: 1.01x faster                                          |
| pathlib                  | 19.0 ms                                                               | 18.8 ms: 1.01x faster                                         |
| mdp                      | 2.54 sec                                                              | 2.51 sec: 1.01x faster                                        |
| coverage                 | 92.8 ms                                                               | 91.8 ms: 1.01x faster                                         |
| logging_format           | 6.59 us                                                               | 6.53 us: 1.01x faster                                         |
| float                    | 80.5 ms                                                               | 79.7 ms: 1.01x faster                                         |
| coroutines               | 22.8 ms                                                               | 22.6 ms: 1.01x faster                                         |
| pprint_safe_repr         | 723 ms                                                                | 717 ms: 1.01x faster                                          |
| nqueens                  | 80.5 ms                                                               | 79.8 ms: 1.01x faster                                         |
| python_startup_no_site   | 6.73 ms                                                               | 6.68 ms: 1.01x faster                                         |
| python_startup           | 9.25 ms                                                               | 9.19 ms: 1.01x faster                                         |
| xml_etree_parse          | 154 ms                                                                | 153 ms: 1.01x faster                                          |
| xml_etree_iterparse      | 104 ms                                                                | 103 ms: 1.01x faster                                          |
| pprint_pformat           | 1.47 sec                                                              | 1.46 sec: 1.01x faster                                        |
| regex_compile            | 138 ms                                                                | 137 ms: 1.00x faster                                          |
| async_tree_io            | 1.20 sec                                                              | 1.20 sec: 1.00x faster                                        |
| pidigits                 | 197 ms                                                                | 197 ms: 1.00x faster                                          |
| asyncio_tcp_ssl          | 1.79 sec                                                              | 1.80 sec: 1.00x slower                                        |
| raytrace                 | 268 ms                                                                | 269 ms: 1.00x slower                                          |
| xml_etree_generate       | 84.5 ms                                                               | 84.9 ms: 1.00x slower                                         |
| sqlglot_normalize        | 106 ms                                                                | 106 ms: 1.00x slower                                          |
| mako                     | 10.6 ms                                                               | 10.7 ms: 1.00x slower                                         |
| chaos                    | 59.3 ms                                                               | 59.6 ms: 1.01x slower                                         |
| xml_etree_process        | 58.0 ms                                                               | 58.3 ms: 1.01x slower                                         |
| deepcopy_memo            | 37.4 us                                                               | 37.6 us: 1.01x slower                                         |
| pickle_pure_python       | 305 us                                                                | 307 us: 1.01x slower                                          |
| unpickle                 | 14.7 us                                                               | 14.8 us: 1.01x slower                                         |
| generators               | 28.8 ms                                                               | 29.1 ms: 1.01x slower                                         |
| dulwich_log              | 65.3 ms                                                               | 65.8 ms: 1.01x slower                                         |
| deepcopy                 | 347 us                                                                | 350 us: 1.01x slower                                          |
| go                       | 136 ms                                                                | 138 ms: 1.01x slower                                          |
| telco                    | 7.15 ms                                                               | 7.22 ms: 1.01x slower                                         |
| deepcopy_reduce          | 3.18 us                                                               | 3.21 us: 1.01x slower                                         |
| async_generators         | 445 ms                                                                | 451 ms: 1.01x slower                                          |
| scimark_fft              | 356 ms                                                                | 361 ms: 1.01x slower                                          |
| richards_super           | 52.5 ms                                                               | 53.3 ms: 1.02x slower                                         |
| nbody                    | 88.4 ms                                                               | 89.9 ms: 1.02x slower                                         |
| deltablue                | 3.22 ms                                                               | 3.27 ms: 1.02x slower                                         |
| scimark_sor              | 119 ms                                                                | 121 ms: 1.02x slower                                          |
| pickle_list              | 4.48 us                                                               | 4.56 us: 1.02x slower                                         |
| scimark_monte_carlo      | 72.0 ms                                                               | 73.5 ms: 1.02x slower                                         |
| asyncio_tcp              | 500 ms                                                                | 511 ms: 1.02x slower                                          |
| fannkuch                 | 391 ms                                                                | 399 ms: 1.02x slower                                          |
| hexiom                   | 6.00 ms                                                               | 6.12 ms: 1.02x slower                                         |
| spectral_norm            | 108 ms                                                                | 112 ms: 1.03x slower                                          |
| gc_traversal             | 3.62 ms                                                               | 4.06 ms: 1.12x slower                                         |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                  |

Benchmark hidden because not significant (29): json, regex_dna, logging_silent, async_tree_cpu_io_mixed, scimark_lu, json_dumps, docutils, async_tree_memoization, unpickle_pure_python, logging_simple, pyflate, async_tree_none, bench_mp_pool, pycparser, unpickle_list, crypto_pyaes, sqlite_synth, mypy2, sqlglot_parse, sqlglot_optimize, sqlglot_transpile, tomli_loads, bench_thread_pool, comprehensions, richards, regex_v8, tornado_http, pickle, dask
