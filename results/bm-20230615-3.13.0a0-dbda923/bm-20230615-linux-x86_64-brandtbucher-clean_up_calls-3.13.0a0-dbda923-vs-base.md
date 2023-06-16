
# Results vs. base

- fork: brandtbucher
- ref: clean_up_calls
- machine: linux-x86_64
- commit hash: dbda923
- commit date: 2023-06-15
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230615-linux-x86_64-python-8f10140e74d141a0a894-3.13.0a0-8f10140 | bm-20230615-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-dbda923 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| docutils       | 2.64 sec                                                              | 2.68 sec: 1.02x slower                                                |
| tornado_http   | 96.8 ms                                                               | 98.7 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230615-linux-x86_64-python-8f10140e74d141a0a894-3.13.0a0-8f10140 | bm-20230615-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-dbda923 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 197 ms                                                                | 197 ms: 1.00x slower                                                  |
| nbody          | 89.3 ms                                                               | 90.3 ms: 1.01x slower                                                 |
| float          | 78.8 ms                                                               | 80.3 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230615-linux-x86_64-python-8f10140e74d141a0a894-3.13.0a0-8f10140 | bm-20230615-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-dbda923 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 4.10 ms                                                               | 3.39 ms: 1.21x faster                                                 |
| regex_dna      | 205 ms                                                                | 202 ms: 1.01x faster                                                  |
| regex_v8       | 21.8 ms                                                               | 22.0 ms: 1.01x slower                                                 |
| regex_compile  | 137 ms                                                                | 139 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.05x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230615-linux-x86_64-python-8f10140e74d141a0a894-3.13.0a0-8f10140 | bm-20230615-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-dbda923 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_list        | 5.03 us                                                               | 4.92 us: 1.02x faster                                                 |
| xml_etree_process    | 57.7 ms                                                               | 58.1 ms: 1.01x slower                                                 |
| xml_etree_iterparse  | 103 ms                                                                | 104 ms: 1.01x slower                                                  |
| unpickle_pure_python | 214 us                                                                | 217 us: 1.02x slower                                                  |
| xml_etree_generate   | 83.5 ms                                                               | 85.0 ms: 1.02x slower                                                 |
| tomli_loads          | 2.17 sec                                                              | 2.22 sec: 1.02x slower                                                |
| json_loads           | 24.8 us                                                               | 25.3 us: 1.02x slower                                                 |
| json_dumps           | 9.69 ms                                                               | 9.93 ms: 1.03x slower                                                 |
| unpickle             | 14.7 us                                                               | 15.1 us: 1.03x slower                                                 |
| pickle_pure_python   | 304 us                                                                | 319 us: 1.05x slower                                                  |
| pickle_list          | 4.54 us                                                               | 4.78 us: 1.05x slower                                                 |
| pickle_dict          | 31.0 us                                                               | 33.0 us: 1.06x slower                                                 |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                          |

Benchmark hidden because not significant (2): xml_etree_parse, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230615-linux-x86_64-python-8f10140e74d141a0a894-3.13.0a0-8f10140 | bm-20230615-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-dbda923 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 9.17 ms                                                               | 9.18 ms: 1.00x slower                                                 |
| python_startup_no_site | 6.66 ms                                                               | 6.67 ms: 1.00x slower                                                 |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230615-linux-x86_64-python-8f10140e74d141a0a894-3.13.0a0-8f10140 | bm-20230615-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-dbda923 |
|-----------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako      | 10.8 ms                                                               | 10.8 ms: 1.00x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20230615-linux-x86_64-python-8f10140e74d141a0a894-3.13.0a0-8f10140 | bm-20230615-linux-x86_64-brandtbucher-clean_up_calls-3.13.0a0-dbda923 |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot             | 4.10 ms                                                               | 3.39 ms: 1.21x faster                                                 |
| generators               | 30.6 ms                                                               | 28.6 ms: 1.07x faster                                                 |
| coroutines               | 22.4 ms                                                               | 21.6 ms: 1.03x faster                                                 |
| typing_runtime_protocols | 146 us                                                                | 142 us: 1.03x faster                                                  |
| unpickle_list            | 5.03 us                                                               | 4.92 us: 1.02x faster                                                 |
| async_generators         | 458 ms                                                                | 449 ms: 1.02x faster                                                  |
| spectral_norm            | 104 ms                                                                | 102 ms: 1.02x faster                                                  |
| regex_dna                | 205 ms                                                                | 202 ms: 1.01x faster                                                  |
| scimark_lu               | 112 ms                                                                | 110 ms: 1.01x faster                                                  |
| scimark_sor              | 118 ms                                                                | 117 ms: 1.01x faster                                                  |
| mako                     | 10.8 ms                                                               | 10.8 ms: 1.00x faster                                                 |
| python_startup           | 9.17 ms                                                               | 9.18 ms: 1.00x slower                                                 |
| pidigits                 | 197 ms                                                                | 197 ms: 1.00x slower                                                  |
| python_startup_no_site   | 6.66 ms                                                               | 6.67 ms: 1.00x slower                                                 |
| meteor_contest           | 105 ms                                                                | 105 ms: 1.00x slower                                                  |
| xml_etree_process        | 57.7 ms                                                               | 58.1 ms: 1.01x slower                                                 |
| bench_thread_pool        | 820 us                                                                | 826 us: 1.01x slower                                                  |
| pprint_pformat           | 1.46 sec                                                              | 1.47 sec: 1.01x slower                                                |
| regex_v8                 | 21.8 ms                                                               | 22.0 ms: 1.01x slower                                                 |
| logging_simple           | 6.02 us                                                               | 6.07 us: 1.01x slower                                                 |
| xml_etree_iterparse      | 103 ms                                                                | 104 ms: 1.01x slower                                                  |
| nbody                    | 89.3 ms                                                               | 90.3 ms: 1.01x slower                                                 |
| logging_silent           | 98.3 ns                                                               | 99.4 ns: 1.01x slower                                                 |
| pathlib                  | 18.7 ms                                                               | 18.9 ms: 1.01x slower                                                 |
| mdp                      | 2.53 sec                                                              | 2.56 sec: 1.01x slower                                                |
| async_tree_memoization   | 584 ms                                                                | 592 ms: 1.01x slower                                                  |
| go                       | 134 ms                                                                | 135 ms: 1.01x slower                                                  |
| raytrace                 | 288 ms                                                                | 292 ms: 1.01x slower                                                  |
| nqueens                  | 78.4 ms                                                               | 79.4 ms: 1.01x slower                                                 |
| crypto_pyaes             | 77.5 ms                                                               | 78.6 ms: 1.01x slower                                                 |
| json                     | 4.78 ms                                                               | 4.85 ms: 1.01x slower                                                 |
| docutils                 | 2.64 sec                                                              | 2.68 sec: 1.02x slower                                                |
| hexiom                   | 5.99 ms                                                               | 6.08 ms: 1.02x slower                                                 |
| richards_super           | 49.7 ms                                                               | 50.5 ms: 1.02x slower                                                 |
| dask                     | 519 ms                                                                | 527 ms: 1.02x slower                                                  |
| scimark_monte_carlo      | 70.8 ms                                                               | 72.0 ms: 1.02x slower                                                 |
| unpickle_pure_python     | 214 us                                                                | 217 us: 1.02x slower                                                  |
| xml_etree_generate       | 83.5 ms                                                               | 85.0 ms: 1.02x slower                                                 |
| regex_compile            | 137 ms                                                                | 139 ms: 1.02x slower                                                  |
| mypy2                    | 337 ms                                                                | 343 ms: 1.02x slower                                                  |
| tornado_http             | 96.8 ms                                                               | 98.7 ms: 1.02x slower                                                 |
| float                    | 78.8 ms                                                               | 80.3 ms: 1.02x slower                                                 |
| gc_traversal             | 3.61 ms                                                               | 3.68 ms: 1.02x slower                                                 |
| tomli_loads              | 2.17 sec                                                              | 2.22 sec: 1.02x slower                                                |
| dulwich_log              | 65.4 ms                                                               | 66.8 ms: 1.02x slower                                                 |
| json_loads               | 24.8 us                                                               | 25.3 us: 1.02x slower                                                 |
| comprehensions           | 20.2 us                                                               | 20.7 us: 1.02x slower                                                 |
| sqlglot_transpile        | 1.62 ms                                                               | 1.66 ms: 1.02x slower                                                 |
| json_dumps               | 9.69 ms                                                               | 9.93 ms: 1.03x slower                                                 |
| sqlglot_optimize         | 52.6 ms                                                               | 53.9 ms: 1.03x slower                                                 |
| logging_format           | 6.51 us                                                               | 6.68 us: 1.03x slower                                                 |
| pycparser                | 1.13 sec                                                              | 1.16 sec: 1.03x slower                                                |
| sqlglot_normalize        | 106 ms                                                                | 109 ms: 1.03x slower                                                  |
| telco                    | 6.77 ms                                                               | 6.95 ms: 1.03x slower                                                 |
| coverage                 | 93.5 ms                                                               | 96.1 ms: 1.03x slower                                                 |
| unpickle                 | 14.7 us                                                               | 15.1 us: 1.03x slower                                                 |
| scimark_sparse_mat_mult  | 4.65 ms                                                               | 4.79 ms: 1.03x slower                                                 |
| sqlglot_parse            | 1.30 ms                                                               | 1.34 ms: 1.03x slower                                                 |
| richards                 | 43.2 ms                                                               | 44.7 ms: 1.03x slower                                                 |
| chaos                    | 60.4 ms                                                               | 62.6 ms: 1.04x slower                                                 |
| deepcopy                 | 347 us                                                                | 362 us: 1.04x slower                                                  |
| deepcopy_memo            | 37.3 us                                                               | 39.1 us: 1.05x slower                                                 |
| pickle_pure_python       | 304 us                                                                | 319 us: 1.05x slower                                                  |
| deepcopy_reduce          | 3.13 us                                                               | 3.29 us: 1.05x slower                                                 |
| pickle_list              | 4.54 us                                                               | 4.78 us: 1.05x slower                                                 |
| pickle_dict              | 31.0 us                                                               | 33.0 us: 1.06x slower                                                 |
| unpack_sequence          | 43.5 ns                                                               | 48.9 ns: 1.12x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.01x slower                                                          |

Benchmark hidden because not significant (15): async_tree_io, pyflate, create_gc_cycles, scimark_fft, bench_mp_pool, asyncio_tcp, xml_etree_parse, async_tree_none, asyncio_tcp_ssl, pickle, pprint_safe_repr, fannkuch, async_tree_cpu_io_mixed, deltablue, sqlite_synth
