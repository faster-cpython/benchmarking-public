
# Results vs. base

- fork: brandtbucher
- ref: un_materialize
- machine: linux-x86_64
- commit hash: 0ab8274
- commit date: 2023-07-06
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230706-linux-x86_64-python-67a798888dcde13bbb1e-3.13.0a0-67a7988 | bm-20230706-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-0ab8274 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 92.7 ms                                                               | 88.8 ms: 1.04x faster                                                 |
| pidigits       | 197 ms                                                                | 197 ms: 1.00x slower                                                  |
| float          | 78.5 ms                                                               | 80.4 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230706-linux-x86_64-python-67a798888dcde13bbb1e-3.13.0a0-67a7988 | bm-20230706-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-0ab8274 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.53 ms                                                               | 3.51 ms: 1.01x faster                                                 |
| regex_v8       | 22.1 ms                                                               | 22.3 ms: 1.01x slower                                                 |
| regex_dna      | 208 ms                                                                | 211 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20230706-linux-x86_64-python-67a798888dcde13bbb1e-3.13.0a0-67a7988 | bm-20230706-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-0ab8274 |
|--------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python | 306 us                                                                | 300 us: 1.02x faster                                                  |
| tomli_loads        | 2.35 sec                                                              | 2.31 sec: 1.02x faster                                                |
| xml_etree_generate | 83.7 ms                                                               | 84.0 ms: 1.00x slower                                                 |
| xml_etree_process  | 57.4 ms                                                               | 57.9 ms: 1.01x slower                                                 |
| xml_etree_parse    | 153 ms                                                                | 154 ms: 1.01x slower                                                  |
| json_dumps         | 9.74 ms                                                               | 9.89 ms: 1.02x slower                                                 |
| pickle_dict        | 30.9 us                                                               | 31.5 us: 1.02x slower                                                 |
| unpickle_list      | 4.89 us                                                               | 4.99 us: 1.02x slower                                                 |
| unpickle           | 14.8 us                                                               | 15.2 us: 1.03x slower                                                 |
| pickle_list        | 4.51 us                                                               | 4.64 us: 1.03x slower                                                 |
| Geometric mean     | (ref)                                                                 | 1.01x slower                                                          |

Benchmark hidden because not significant (4): pickle, xml_etree_iterparse, json_loads, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230706-linux-x86_64-python-67a798888dcde13bbb1e-3.13.0a0-67a7988 | bm-20230706-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-0ab8274 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.67 ms                                                               | 6.72 ms: 1.01x slower                                                 |
| python_startup         | 9.16 ms                                                               | 9.24 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230706-linux-x86_64-python-67a798888dcde13bbb1e-3.13.0a0-67a7988 | bm-20230706-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-0ab8274 |
|-----------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako      | 10.6 ms                                                               | 10.4 ms: 1.02x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20230706-linux-x86_64-python-67a798888dcde13bbb1e-3.13.0a0-67a7988 | bm-20230706-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-0ab8274 |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody                    | 92.7 ms                                                               | 88.8 ms: 1.04x faster                                                 |
| generators               | 29.5 ms                                                               | 28.5 ms: 1.04x faster                                                 |
| scimark_sparse_mat_mult  | 4.74 ms                                                               | 4.62 ms: 1.03x faster                                                 |
| unpack_sequence          | 49.2 ns                                                               | 48.1 ns: 1.02x faster                                                 |
| coverage                 | 93.4 ms                                                               | 91.3 ms: 1.02x faster                                                 |
| pickle_pure_python       | 306 us                                                                | 300 us: 1.02x faster                                                  |
| scimark_sor              | 121 ms                                                                | 118 ms: 1.02x faster                                                  |
| logging_format           | 6.52 us                                                               | 6.40 us: 1.02x faster                                                 |
| tomli_loads              | 2.35 sec                                                              | 2.31 sec: 1.02x faster                                                |
| mako                     | 10.6 ms                                                               | 10.4 ms: 1.02x faster                                                 |
| pycparser                | 1.16 sec                                                              | 1.14 sec: 1.02x faster                                                |
| scimark_lu               | 112 ms                                                                | 111 ms: 1.01x faster                                                  |
| pyflate                  | 446 ms                                                                | 441 ms: 1.01x faster                                                  |
| scimark_monte_carlo      | 72.5 ms                                                               | 71.7 ms: 1.01x faster                                                 |
| logging_simple           | 5.89 us                                                               | 5.83 us: 1.01x faster                                                 |
| regex_effbot             | 3.53 ms                                                               | 3.51 ms: 1.01x faster                                                 |
| crypto_pyaes             | 78.0 ms                                                               | 77.5 ms: 1.01x faster                                                 |
| async_generators         | 450 ms                                                                | 448 ms: 1.01x faster                                                  |
| nqueens                  | 79.4 ms                                                               | 79.0 ms: 1.01x faster                                                 |
| sqlglot_normalize        | 106 ms                                                                | 105 ms: 1.00x faster                                                  |
| scimark_fft              | 357 ms                                                                | 355 ms: 1.00x faster                                                  |
| async_tree_io            | 1.20 sec                                                              | 1.19 sec: 1.00x faster                                                |
| bench_thread_pool        | 816 us                                                                | 814 us: 1.00x faster                                                  |
| asyncio_tcp_ssl          | 1.79 sec                                                              | 1.79 sec: 1.00x faster                                                |
| pidigits                 | 197 ms                                                                | 197 ms: 1.00x slower                                                  |
| xml_etree_generate       | 83.7 ms                                                               | 84.0 ms: 1.00x slower                                                 |
| fannkuch                 | 386 ms                                                                | 388 ms: 1.01x slower                                                  |
| python_startup_no_site   | 6.67 ms                                                               | 6.72 ms: 1.01x slower                                                 |
| go                       | 136 ms                                                                | 137 ms: 1.01x slower                                                  |
| sqlglot_transpile        | 1.65 ms                                                               | 1.67 ms: 1.01x slower                                                 |
| python_startup           | 9.16 ms                                                               | 9.24 ms: 1.01x slower                                                 |
| coroutines               | 22.4 ms                                                               | 22.6 ms: 1.01x slower                                                 |
| telco                    | 7.20 ms                                                               | 7.26 ms: 1.01x slower                                                 |
| xml_etree_process        | 57.4 ms                                                               | 57.9 ms: 1.01x slower                                                 |
| xml_etree_parse          | 153 ms                                                                | 154 ms: 1.01x slower                                                  |
| regex_v8                 | 22.1 ms                                                               | 22.3 ms: 1.01x slower                                                 |
| pprint_safe_repr         | 708 ms                                                                | 716 ms: 1.01x slower                                                  |
| sqlglot_parse            | 1.33 ms                                                               | 1.34 ms: 1.01x slower                                                 |
| regex_dna                | 208 ms                                                                | 211 ms: 1.01x slower                                                  |
| deepcopy                 | 343 us                                                                | 348 us: 1.01x slower                                                  |
| json_dumps               | 9.74 ms                                                               | 9.89 ms: 1.02x slower                                                 |
| create_gc_cycles         | 1.48 ms                                                               | 1.51 ms: 1.02x slower                                                 |
| pickle_dict              | 30.9 us                                                               | 31.5 us: 1.02x slower                                                 |
| comprehensions           | 20.4 us                                                               | 20.9 us: 1.02x slower                                                 |
| unpickle_list            | 4.89 us                                                               | 4.99 us: 1.02x slower                                                 |
| float                    | 78.5 ms                                                               | 80.4 ms: 1.02x slower                                                 |
| unpickle                 | 14.8 us                                                               | 15.2 us: 1.03x slower                                                 |
| raytrace                 | 266 ms                                                                | 273 ms: 1.03x slower                                                  |
| pickle_list              | 4.51 us                                                               | 4.64 us: 1.03x slower                                                 |
| typing_runtime_protocols | 141 us                                                                | 146 us: 1.03x slower                                                  |
| mdp                      | 2.52 sec                                                              | 2.65 sec: 1.05x slower                                                |
| gc_traversal             | 4.07 ms                                                               | 4.33 ms: 1.07x slower                                                 |
| mypy2                    | 336 ms                                                                | 453 ms: 1.35x slower                                                  |
| Geometric mean           | (ref)                                                                 | 1.01x slower                                                          |

Benchmark hidden because not significant (29): pickle, logging_silent, dask, hexiom, dulwich_log, spectral_norm, docutils, xml_etree_iterparse, meteor_contest, deepcopy_memo, json_loads, json, deltablue, tornado_http, bench_mp_pool, async_tree_none, pprint_pformat, regex_compile, richards_super, asyncio_tcp, sqlglot_optimize, chaos, richards, async_tree_memoization, unpickle_pure_python, async_tree_cpu_io_mixed, pathlib, deepcopy_reduce, sqlite_synth
