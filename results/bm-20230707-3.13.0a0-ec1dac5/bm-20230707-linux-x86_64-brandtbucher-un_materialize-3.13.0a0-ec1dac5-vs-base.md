
# Results vs. base

- fork: brandtbucher
- ref: un_materialize
- machine: linux-x86_64
- commit hash: ec1dac5
- commit date: 2023-07-07
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230707-linux-x86_64-python-80b9b3a51757ebb1e354-3.13.0a0-80b9b3a | bm-20230707-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-ec1dac5 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 196 ms                                                                | 197 ms: 1.01x slower                                                  |
| nbody          | 89.8 ms                                                               | 91.3 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                          |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230707-linux-x86_64-python-80b9b3a51757ebb1e354-3.13.0a0-80b9b3a | bm-20230707-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-ec1dac5 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 22.3 ms                                                               | 21.8 ms: 1.02x faster                                                 |
| regex_effbot   | 3.56 ms                                                               | 3.51 ms: 1.01x faster                                                 |
| regex_compile  | 136 ms                                                                | 136 ms: 1.00x faster                                                  |
| regex_dna      | 211 ms                                                                | 213 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230707-linux-x86_64-python-80b9b3a51757ebb1e354-3.13.0a0-80b9b3a | bm-20230707-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-ec1dac5 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 312 us                                                                | 300 us: 1.04x faster                                                  |
| json_dumps           | 9.86 ms                                                               | 9.69 ms: 1.02x faster                                                 |
| pickle               | 10.7 us                                                               | 10.5 us: 1.02x faster                                                 |
| xml_etree_generate   | 84.3 ms                                                               | 83.5 ms: 1.01x faster                                                 |
| tomli_loads          | 2.30 sec                                                              | 2.28 sec: 1.01x faster                                                |
| json_loads           | 25.8 us                                                               | 25.6 us: 1.01x faster                                                 |
| xml_etree_process    | 57.8 ms                                                               | 57.5 ms: 1.01x faster                                                 |
| unpickle_pure_python | 213 us                                                                | 212 us: 1.00x faster                                                  |
| unpickle_list        | 5.06 us                                                               | 5.10 us: 1.01x slower                                                 |
| pickle_dict          | 30.8 us                                                               | 31.8 us: 1.03x slower                                                 |
| pickle_list          | 4.72 us                                                               | 4.93 us: 1.04x slower                                                 |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (3): xml_etree_iterparse, xml_etree_parse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230707-linux-x86_64-python-80b9b3a51757ebb1e354-3.13.0a0-80b9b3a | bm-20230707-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-ec1dac5 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.67 ms                                                               | 6.67 ms: 1.00x faster                                                 |
| python_startup         | 9.18 ms                                                               | 9.19 ms: 1.00x slower                                                 |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230707-linux-x86_64-python-80b9b3a51757ebb1e354-3.13.0a0-80b9b3a | bm-20230707-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-ec1dac5 |
|-----------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako      | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                                 |

All benchmarks:
===============

| Benchmark                | bm-20230707-linux-x86_64-python-80b9b3a51757ebb1e354-3.13.0a0-80b9b3a | bm-20230707-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-ec1dac5 |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpack_sequence          | 46.7 ns                                                               | 42.9 ns: 1.09x faster                                                 |
| gc_traversal             | 4.30 ms                                                               | 4.07 ms: 1.06x faster                                                 |
| pickle_pure_python       | 312 us                                                                | 300 us: 1.04x faster                                                  |
| spectral_norm            | 110 ms                                                                | 106 ms: 1.04x faster                                                  |
| crypto_pyaes             | 78.9 ms                                                               | 75.9 ms: 1.04x faster                                                 |
| logging_format           | 6.68 us                                                               | 6.48 us: 1.03x faster                                                 |
| scimark_sparse_mat_mult  | 4.74 ms                                                               | 4.61 ms: 1.03x faster                                                 |
| json                     | 4.95 ms                                                               | 4.84 ms: 1.02x faster                                                 |
| regex_v8                 | 22.3 ms                                                               | 21.8 ms: 1.02x faster                                                 |
| json_dumps               | 9.86 ms                                                               | 9.69 ms: 1.02x faster                                                 |
| fannkuch                 | 394 ms                                                                | 388 ms: 1.02x faster                                                  |
| logging_silent           | 103 ns                                                                | 102 ns: 1.02x faster                                                  |
| async_generators         | 453 ms                                                                | 446 ms: 1.02x faster                                                  |
| pickle                   | 10.7 us                                                               | 10.5 us: 1.02x faster                                                 |
| coroutines               | 23.1 ms                                                               | 22.7 ms: 1.01x faster                                                 |
| logging_simple           | 5.99 us                                                               | 5.90 us: 1.01x faster                                                 |
| regex_effbot             | 3.56 ms                                                               | 3.51 ms: 1.01x faster                                                 |
| telco                    | 7.19 ms                                                               | 7.11 ms: 1.01x faster                                                 |
| richards                 | 47.2 ms                                                               | 46.7 ms: 1.01x faster                                                 |
| xml_etree_generate       | 84.3 ms                                                               | 83.5 ms: 1.01x faster                                                 |
| deepcopy                 | 350 us                                                                | 347 us: 1.01x faster                                                  |
| tomli_loads              | 2.30 sec                                                              | 2.28 sec: 1.01x faster                                                |
| chaos                    | 59.9 ms                                                               | 59.4 ms: 1.01x faster                                                 |
| json_loads               | 25.8 us                                                               | 25.6 us: 1.01x faster                                                 |
| sqlite_synth             | 2.78 us                                                               | 2.76 us: 1.01x faster                                                 |
| dulwich_log              | 66.1 ms                                                               | 65.6 ms: 1.01x faster                                                 |
| richards_super           | 53.1 ms                                                               | 52.8 ms: 1.01x faster                                                 |
| xml_etree_process        | 57.8 ms                                                               | 57.5 ms: 1.01x faster                                                 |
| async_tree_io            | 1.20 sec                                                              | 1.20 sec: 1.01x faster                                                |
| scimark_fft              | 353 ms                                                                | 352 ms: 1.00x faster                                                  |
| unpickle_pure_python     | 213 us                                                                | 212 us: 1.00x faster                                                  |
| bench_thread_pool        | 821 us                                                                | 818 us: 1.00x faster                                                  |
| regex_compile            | 136 ms                                                                | 136 ms: 1.00x faster                                                  |
| sqlglot_optimize         | 53.2 ms                                                               | 53.0 ms: 1.00x faster                                                 |
| python_startup_no_site   | 6.67 ms                                                               | 6.67 ms: 1.00x faster                                                 |
| python_startup           | 9.18 ms                                                               | 9.19 ms: 1.00x slower                                                 |
| asyncio_tcp_ssl          | 1.79 sec                                                              | 1.79 sec: 1.00x slower                                                |
| nqueens                  | 79.7 ms                                                               | 79.9 ms: 1.00x slower                                                 |
| deepcopy_memo            | 37.3 us                                                               | 37.5 us: 1.00x slower                                                 |
| pidigits                 | 196 ms                                                                | 197 ms: 1.01x slower                                                  |
| asyncio_tcp              | 507 ms                                                                | 510 ms: 1.01x slower                                                  |
| coverage                 | 93.2 ms                                                               | 93.8 ms: 1.01x slower                                                 |
| unpickle_list            | 5.06 us                                                               | 5.10 us: 1.01x slower                                                 |
| regex_dna                | 211 ms                                                                | 213 ms: 1.01x slower                                                  |
| mako                     | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                                 |
| generators               | 28.4 ms                                                               | 28.7 ms: 1.01x slower                                                 |
| comprehensions           | 20.4 us                                                               | 20.7 us: 1.01x slower                                                 |
| nbody                    | 89.8 ms                                                               | 91.3 ms: 1.02x slower                                                 |
| typing_runtime_protocols | 143 us                                                                | 146 us: 1.02x slower                                                  |
| scimark_lu               | 110 ms                                                                | 112 ms: 1.02x slower                                                  |
| raytrace                 | 268 ms                                                                | 275 ms: 1.02x slower                                                  |
| pickle_dict              | 30.8 us                                                               | 31.8 us: 1.03x slower                                                 |
| pickle_list              | 4.72 us                                                               | 4.93 us: 1.04x slower                                                 |
| mdp                      | 2.53 sec                                                              | 2.68 sec: 1.06x slower                                                |
| mypy2                    | 337 ms                                                                | 455 ms: 1.35x slower                                                  |
| Geometric mean           | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (27): async_tree_cpu_io_mixed, pathlib, sqlglot_transpile, async_tree_none, async_tree_memoization, pprint_safe_repr, xml_etree_iterparse, dask, pycparser, tornado_http, docutils, go, scimark_monte_carlo, bench_mp_pool, hexiom, scimark_sor, sqlglot_parse, float, create_gc_cycles, sqlglot_normalize, meteor_contest, pprint_pformat, pyflate, xml_etree_parse, deepcopy_reduce, deltablue, unpickle
