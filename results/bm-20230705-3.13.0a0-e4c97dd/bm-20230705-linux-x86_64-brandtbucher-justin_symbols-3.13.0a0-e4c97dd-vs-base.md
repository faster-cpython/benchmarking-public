
# Results vs. base

- fork: brandtbucher
- ref: justin_symbols
- machine: linux-x86_64
- commit hash: e4c97dd
- commit date: 2023-07-05
- overall geometric mean: 1.02x slower
- HPT reliability: 81.69%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230601-linux-x86_64-python-ede89af605b1c0442353-3.13.0a0-ede89af | bm-20230705-linux-x86_64-brandtbucher-justin_symbols-3.13.0a0-e4c97dd |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| docutils       | 2.71 sec                                                              | 2.72 sec: 1.00x slower                                                |
| tornado_http   | 99.5 ms                                                               | 98.9 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230601-linux-x86_64-python-ede89af605b1c0442353-3.13.0a0-ede89af | bm-20230705-linux-x86_64-brandtbucher-justin_symbols-3.13.0a0-e4c97dd |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 196 ms                                                                | 197 ms: 1.00x slower                                                  |
| nbody          | 90.9 ms                                                               | 99.0 ms: 1.09x slower                                                 |
| float          | 79.8 ms                                                               | 92.8 ms: 1.16x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.08x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230601-linux-x86_64-python-ede89af605b1c0442353-3.13.0a0-ede89af | bm-20230705-linux-x86_64-brandtbucher-justin_symbols-3.13.0a0-e4c97dd |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                                | 140 ms: 1.03x faster                                                  |
| regex_dna      | 204 ms                                                                | 215 ms: 1.05x slower                                                  |
| regex_v8       | 21.8 ms                                                               | 23.3 ms: 1.07x slower                                                 |
| regex_effbot   | 3.52 ms                                                               | 3.81 ms: 1.08x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230601-linux-x86_64-python-ede89af605b1c0442353-3.13.0a0-ede89af | bm-20230705-linux-x86_64-brandtbucher-justin_symbols-3.13.0a0-e4c97dd |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_list          | 4.64 us                                                               | 4.39 us: 1.06x faster                                                 |
| pickle               | 11.0 us                                                               | 10.5 us: 1.05x faster                                                 |
| unpickle_pure_python | 217 us                                                                | 211 us: 1.03x faster                                                  |
| pickle_pure_python   | 313 us                                                                | 305 us: 1.03x faster                                                  |
| xml_etree_process    | 59.2 ms                                                               | 57.9 ms: 1.02x faster                                                 |
| xml_etree_parse      | 155 ms                                                                | 152 ms: 1.02x faster                                                  |
| unpickle_list        | 4.95 us                                                               | 4.87 us: 1.02x faster                                                 |
| json_loads           | 25.4 us                                                               | 25.1 us: 1.01x faster                                                 |
| xml_etree_iterparse  | 104 ms                                                                | 103 ms: 1.01x faster                                                  |
| xml_etree_generate   | 85.7 ms                                                               | 85.2 ms: 1.01x faster                                                 |
| pickle_dict          | 31.7 us                                                               | 31.7 us: 1.00x slower                                                 |
| tomli_loads          | 2.22 sec                                                              | 2.48 sec: 1.11x slower                                                |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                          |

Benchmark hidden because not significant (2): json_dumps, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230601-linux-x86_64-python-ede89af605b1c0442353-3.13.0a0-ede89af | bm-20230705-linux-x86_64-brandtbucher-justin_symbols-3.13.0a0-e4c97dd |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 9.30 ms                                                               | 9.53 ms: 1.02x slower                                                 |
| python_startup_no_site | 6.77 ms                                                               | 6.94 ms: 1.03x slower                                                 |
| Geometric mean         | (ref)                                                                 | 1.03x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230601-linux-x86_64-python-ede89af605b1c0442353-3.13.0a0-ede89af | bm-20230705-linux-x86_64-brandtbucher-justin_symbols-3.13.0a0-e4c97dd |
|-----------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako      | 10.6 ms                                                               | 13.7 ms: 1.29x slower                                                 |

All benchmarks:
===============

| Benchmark                | bm-20230601-linux-x86_64-python-ede89af605b1c0442353-3.13.0a0-ede89af | bm-20230705-linux-x86_64-brandtbucher-justin_symbols-3.13.0a0-e4c97dd |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| gc_traversal             | 3.98 ms                                                               | 3.61 ms: 1.10x faster                                                 |
| generators               | 31.2 ms                                                               | 28.8 ms: 1.08x faster                                                 |
| logging_format           | 7.01 us                                                               | 6.51 us: 1.08x faster                                                 |
| pickle_list              | 4.64 us                                                               | 4.39 us: 1.06x faster                                                 |
| pickle                   | 11.0 us                                                               | 10.5 us: 1.05x faster                                                 |
| logging_simple           | 6.32 us                                                               | 6.04 us: 1.05x faster                                                 |
| pycparser                | 1.20 sec                                                              | 1.15 sec: 1.04x faster                                                |
| dulwich_log              | 67.8 ms                                                               | 65.7 ms: 1.03x faster                                                 |
| unpickle_pure_python     | 217 us                                                                | 211 us: 1.03x faster                                                  |
| pickle_pure_python       | 313 us                                                                | 305 us: 1.03x faster                                                  |
| regex_compile            | 144 ms                                                                | 140 ms: 1.03x faster                                                  |
| dask                     | 538 ms                                                                | 525 ms: 1.03x faster                                                  |
| xml_etree_process        | 59.2 ms                                                               | 57.9 ms: 1.02x faster                                                 |
| coverage                 | 96.9 ms                                                               | 94.9 ms: 1.02x faster                                                 |
| xml_etree_parse          | 155 ms                                                                | 152 ms: 1.02x faster                                                  |
| unpickle_list            | 4.95 us                                                               | 4.87 us: 1.02x faster                                                 |
| unpack_sequence          | 53.2 ns                                                               | 52.3 ns: 1.02x faster                                                 |
| deepcopy                 | 357 us                                                                | 351 us: 1.01x faster                                                  |
| deepcopy_reduce          | 3.17 us                                                               | 3.12 us: 1.01x faster                                                 |
| raytrace                 | 300 ms                                                                | 296 ms: 1.01x faster                                                  |
| json_loads               | 25.4 us                                                               | 25.1 us: 1.01x faster                                                 |
| json                     | 4.85 ms                                                               | 4.79 ms: 1.01x faster                                                 |
| xml_etree_iterparse      | 104 ms                                                                | 103 ms: 1.01x faster                                                  |
| richards                 | 44.9 ms                                                               | 44.5 ms: 1.01x faster                                                 |
| chaos                    | 64.7 ms                                                               | 64.0 ms: 1.01x faster                                                 |
| pprint_pformat           | 1.48 sec                                                              | 1.47 sec: 1.01x faster                                                |
| asyncio_tcp_ssl          | 1.80 sec                                                              | 1.79 sec: 1.01x faster                                                |
| sqlglot_normalize        | 109 ms                                                                | 108 ms: 1.01x faster                                                  |
| async_tree_none          | 500 ms                                                                | 496 ms: 1.01x faster                                                  |
| create_gc_cycles         | 1.52 ms                                                               | 1.51 ms: 1.01x faster                                                 |
| tornado_http             | 99.5 ms                                                               | 98.9 ms: 1.01x faster                                                 |
| mypy2                    | 345 ms                                                                | 343 ms: 1.01x faster                                                  |
| xml_etree_generate       | 85.7 ms                                                               | 85.2 ms: 1.01x faster                                                 |
| sqlglot_optimize         | 53.9 ms                                                               | 53.7 ms: 1.00x faster                                                 |
| async_tree_io            | 1.23 sec                                                              | 1.23 sec: 1.00x faster                                                |
| pidigits                 | 196 ms                                                                | 197 ms: 1.00x slower                                                  |
| pickle_dict              | 31.7 us                                                               | 31.7 us: 1.00x slower                                                 |
| docutils                 | 2.71 sec                                                              | 2.72 sec: 1.00x slower                                                |
| coroutines               | 22.4 ms                                                               | 22.5 ms: 1.01x slower                                                 |
| pathlib                  | 18.6 ms                                                               | 18.8 ms: 1.01x slower                                                 |
| typing_runtime_protocols | 144 us                                                                | 146 us: 1.01x slower                                                  |
| richards_super           | 50.1 ms                                                               | 50.7 ms: 1.01x slower                                                 |
| bench_thread_pool        | 826 us                                                                | 839 us: 1.02x slower                                                  |
| telco                    | 6.75 ms                                                               | 6.91 ms: 1.02x slower                                                 |
| meteor_contest           | 103 ms                                                                | 106 ms: 1.02x slower                                                  |
| python_startup           | 9.30 ms                                                               | 9.53 ms: 1.02x slower                                                 |
| python_startup_no_site   | 6.77 ms                                                               | 6.94 ms: 1.03x slower                                                 |
| scimark_sor              | 121 ms                                                                | 125 ms: 1.03x slower                                                  |
| sqlglot_parse            | 1.34 ms                                                               | 1.37 ms: 1.03x slower                                                 |
| sqlglot_transpile        | 1.66 ms                                                               | 1.70 ms: 1.03x slower                                                 |
| spectral_norm            | 107 ms                                                                | 111 ms: 1.04x slower                                                  |
| logging_silent           | 99.1 ns                                                               | 103 ns: 1.04x slower                                                  |
| go                       | 135 ms                                                                | 140 ms: 1.04x slower                                                  |
| sqlite_synth             | 2.71 us                                                               | 2.83 us: 1.05x slower                                                 |
| regex_dna                | 204 ms                                                                | 215 ms: 1.05x slower                                                  |
| mdp                      | 2.55 sec                                                              | 2.71 sec: 1.06x slower                                                |
| scimark_fft              | 350 ms                                                                | 374 ms: 1.07x slower                                                  |
| regex_v8                 | 21.8 ms                                                               | 23.3 ms: 1.07x slower                                                 |
| deltablue                | 3.49 ms                                                               | 3.74 ms: 1.07x slower                                                 |
| scimark_sparse_mat_mult  | 4.80 ms                                                               | 5.14 ms: 1.07x slower                                                 |
| pyflate                  | 446 ms                                                                | 480 ms: 1.08x slower                                                  |
| regex_effbot             | 3.52 ms                                                               | 3.81 ms: 1.08x slower                                                 |
| nqueens                  | 81.4 ms                                                               | 88.2 ms: 1.08x slower                                                 |
| nbody                    | 90.9 ms                                                               | 99.0 ms: 1.09x slower                                                 |
| hexiom                   | 6.08 ms                                                               | 6.72 ms: 1.11x slower                                                 |
| tomli_loads              | 2.22 sec                                                              | 2.48 sec: 1.11x slower                                                |
| crypto_pyaes             | 78.8 ms                                                               | 90.1 ms: 1.14x slower                                                 |
| float                    | 79.8 ms                                                               | 92.8 ms: 1.16x slower                                                 |
| fannkuch                 | 385 ms                                                                | 456 ms: 1.18x slower                                                  |
| comprehensions           | 20.5 us                                                               | 24.6 us: 1.20x slower                                                 |
| scimark_lu               | 112 ms                                                                | 144 ms: 1.28x slower                                                  |
| mako                     | 10.6 ms                                                               | 13.7 ms: 1.29x slower                                                 |
| deepcopy_memo            | 37.2 us                                                               | 53.0 us: 1.42x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.02x slower                                                          |

Benchmark hidden because not significant (9): json_dumps, scimark_monte_carlo, async_tree_memoization, async_tree_cpu_io_mixed, pprint_safe_repr, bench_mp_pool, asyncio_tcp, unpickle, async_generators


# HPT report

- Reliability score: 81.69% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
