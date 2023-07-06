
# Results vs. base

- fork: brandtbucher
- ref: justin
- machine: linux-x86_64
- commit hash: 3346d48
- commit date: 2023-07-05
- overall geometric mean: 1.02x slower

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230601-linux-x86_64-python-ede89af605b1c0442353-3.13.0a0-ede89af | bm-20230705-linux-x86_64-brandtbucher-justin-3.13.0a0-3346d48 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| pidigits       | 196 ms                                                                | 198 ms: 1.01x slower                                          |
| nbody          | 90.9 ms                                                               | 93.1 ms: 1.02x slower                                         |
| float          | 79.8 ms                                                               | 88.9 ms: 1.11x slower                                         |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230601-linux-x86_64-python-ede89af605b1c0442353-3.13.0a0-ede89af | bm-20230705-linux-x86_64-brandtbucher-justin-3.13.0a0-3346d48 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 144 ms                                                                | 142 ms: 1.01x faster                                          |
| regex_dna      | 204 ms                                                                | 212 ms: 1.04x slower                                          |
| regex_effbot   | 3.52 ms                                                               | 3.69 ms: 1.05x slower                                         |
| regex_v8       | 21.8 ms                                                               | 23.4 ms: 1.07x slower                                         |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230601-linux-x86_64-python-ede89af605b1c0442353-3.13.0a0-ede89af | bm-20230705-linux-x86_64-brandtbucher-justin-3.13.0a0-3346d48 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| pickle               | 11.0 us                                                               | 10.3 us: 1.06x faster                                         |
| unpickle_list        | 4.95 us                                                               | 4.87 us: 1.02x faster                                         |
| pickle_list          | 4.64 us                                                               | 4.57 us: 1.02x faster                                         |
| json_dumps           | 9.98 ms                                                               | 9.83 ms: 1.02x faster                                         |
| json_loads           | 25.4 us                                                               | 25.0 us: 1.01x faster                                         |
| unpickle             | 14.9 us                                                               | 14.8 us: 1.01x faster                                         |
| pickle_pure_python   | 313 us                                                                | 315 us: 1.01x slower                                          |
| unpickle_pure_python | 217 us                                                                | 219 us: 1.01x slower                                          |
| xml_etree_generate   | 85.7 ms                                                               | 86.9 ms: 1.01x slower                                         |
| pickle_dict          | 31.7 us                                                               | 32.5 us: 1.03x slower                                         |
| tomli_loads          | 2.22 sec                                                              | 2.37 sec: 1.07x slower                                        |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                  |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_process, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230601-linux-x86_64-python-ede89af605b1c0442353-3.13.0a0-ede89af | bm-20230705-linux-x86_64-brandtbucher-justin-3.13.0a0-3346d48 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup_no_site | 6.77 ms                                                               | 6.83 ms: 1.01x slower                                         |
| python_startup         | 9.30 ms                                                               | 9.43 ms: 1.01x slower                                         |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230601-linux-x86_64-python-ede89af605b1c0442353-3.13.0a0-ede89af | bm-20230705-linux-x86_64-brandtbucher-justin-3.13.0a0-3346d48 |
|-----------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| mako      | 10.6 ms                                                               | 12.6 ms: 1.18x slower                                         |

All benchmarks:
===============

| Benchmark                | bm-20230601-linux-x86_64-python-ede89af605b1c0442353-3.13.0a0-ede89af | bm-20230705-linux-x86_64-brandtbucher-justin-3.13.0a0-3346d48 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| unpack_sequence          | 53.2 ns                                                               | 45.7 ns: 1.16x faster                                         |
| logging_format           | 7.01 us                                                               | 6.51 us: 1.08x faster                                         |
| generators               | 31.2 ms                                                               | 29.1 ms: 1.07x faster                                         |
| pickle                   | 11.0 us                                                               | 10.3 us: 1.06x faster                                         |
| logging_simple           | 6.32 us                                                               | 5.97 us: 1.06x faster                                         |
| pycparser                | 1.20 sec                                                              | 1.14 sec: 1.05x faster                                        |
| dulwich_log              | 67.8 ms                                                               | 65.2 ms: 1.04x faster                                         |
| gc_traversal             | 3.98 ms                                                               | 3.84 ms: 1.04x faster                                         |
| coverage                 | 96.9 ms                                                               | 94.2 ms: 1.03x faster                                         |
| unpickle_list            | 4.95 us                                                               | 4.87 us: 1.02x faster                                         |
| dask                     | 538 ms                                                                | 529 ms: 1.02x faster                                          |
| pickle_list              | 4.64 us                                                               | 4.57 us: 1.02x faster                                         |
| json_dumps               | 9.98 ms                                                               | 9.83 ms: 1.02x faster                                         |
| json_loads               | 25.4 us                                                               | 25.0 us: 1.01x faster                                         |
| sqlglot_normalize        | 109 ms                                                                | 107 ms: 1.01x faster                                          |
| json                     | 4.85 ms                                                               | 4.79 ms: 1.01x faster                                         |
| regex_compile            | 144 ms                                                                | 142 ms: 1.01x faster                                          |
| raytrace                 | 300 ms                                                                | 297 ms: 1.01x faster                                          |
| create_gc_cycles         | 1.52 ms                                                               | 1.51 ms: 1.01x faster                                         |
| sqlglot_optimize         | 53.9 ms                                                               | 53.6 ms: 1.01x faster                                         |
| unpickle                 | 14.9 us                                                               | 14.8 us: 1.01x faster                                         |
| asyncio_tcp_ssl          | 1.80 sec                                                              | 1.79 sec: 1.01x faster                                        |
| mypy2                    | 345 ms                                                                | 343 ms: 1.01x faster                                          |
| pickle_pure_python       | 313 us                                                                | 315 us: 1.01x slower                                          |
| pidigits                 | 196 ms                                                                | 198 ms: 1.01x slower                                          |
| sqlite_synth             | 2.71 us                                                               | 2.73 us: 1.01x slower                                         |
| bench_thread_pool        | 826 us                                                                | 832 us: 1.01x slower                                          |
| coroutines               | 22.4 ms                                                               | 22.5 ms: 1.01x slower                                         |
| typing_runtime_protocols | 144 us                                                                | 145 us: 1.01x slower                                          |
| unpickle_pure_python     | 217 us                                                                | 219 us: 1.01x slower                                          |
| python_startup_no_site   | 6.77 ms                                                               | 6.83 ms: 1.01x slower                                         |
| deepcopy                 | 357 us                                                                | 360 us: 1.01x slower                                          |
| async_tree_io            | 1.23 sec                                                              | 1.25 sec: 1.01x slower                                        |
| python_startup           | 9.30 ms                                                               | 9.43 ms: 1.01x slower                                         |
| xml_etree_generate       | 85.7 ms                                                               | 86.9 ms: 1.01x slower                                         |
| richards_super           | 50.1 ms                                                               | 50.8 ms: 1.01x slower                                         |
| pathlib                  | 18.6 ms                                                               | 19.0 ms: 1.02x slower                                         |
| sqlglot_transpile        | 1.66 ms                                                               | 1.69 ms: 1.02x slower                                         |
| telco                    | 6.75 ms                                                               | 6.87 ms: 1.02x slower                                         |
| pprint_pformat           | 1.48 sec                                                              | 1.51 sec: 1.02x slower                                        |
| sqlglot_parse            | 1.34 ms                                                               | 1.37 ms: 1.02x slower                                         |
| nbody                    | 90.9 ms                                                               | 93.1 ms: 1.02x slower                                         |
| pprint_safe_repr         | 722 ms                                                                | 741 ms: 1.03x slower                                          |
| pickle_dict              | 31.7 us                                                               | 32.5 us: 1.03x slower                                         |
| async_generators         | 447 ms                                                                | 459 ms: 1.03x slower                                          |
| nqueens                  | 81.4 ms                                                               | 83.7 ms: 1.03x slower                                         |
| meteor_contest           | 103 ms                                                                | 106 ms: 1.03x slower                                          |
| deepcopy_reduce          | 3.17 us                                                               | 3.26 us: 1.03x slower                                         |
| regex_dna                | 204 ms                                                                | 212 ms: 1.04x slower                                          |
| deltablue                | 3.49 ms                                                               | 3.64 ms: 1.04x slower                                         |
| spectral_norm            | 107 ms                                                                | 111 ms: 1.04x slower                                          |
| scimark_sor              | 121 ms                                                                | 127 ms: 1.05x slower                                          |
| regex_effbot             | 3.52 ms                                                               | 3.69 ms: 1.05x slower                                         |
| scimark_sparse_mat_mult  | 4.80 ms                                                               | 5.06 ms: 1.05x slower                                         |
| go                       | 135 ms                                                                | 143 ms: 1.06x slower                                          |
| logging_silent           | 99.1 ns                                                               | 105 ns: 1.06x slower                                          |
| tomli_loads              | 2.22 sec                                                              | 2.37 sec: 1.07x slower                                        |
| scimark_fft              | 350 ms                                                                | 375 ms: 1.07x slower                                          |
| regex_v8                 | 21.8 ms                                                               | 23.4 ms: 1.07x slower                                         |
| pyflate                  | 446 ms                                                                | 485 ms: 1.09x slower                                          |
| crypto_pyaes             | 78.8 ms                                                               | 86.0 ms: 1.09x slower                                         |
| hexiom                   | 6.08 ms                                                               | 6.66 ms: 1.10x slower                                         |
| float                    | 79.8 ms                                                               | 88.9 ms: 1.11x slower                                         |
| fannkuch                 | 385 ms                                                                | 437 ms: 1.13x slower                                          |
| comprehensions           | 20.5 us                                                               | 23.4 us: 1.14x slower                                         |
| mako                     | 10.6 ms                                                               | 12.6 ms: 1.18x slower                                         |
| scimark_lu               | 112 ms                                                                | 133 ms: 1.19x slower                                          |
| deepcopy_memo            | 37.2 us                                                               | 49.5 us: 1.33x slower                                         |
| Geometric mean           | (ref)                                                                 | 1.02x slower                                                  |

Benchmark hidden because not significant (14): xml_etree_parse, tornado_http, xml_etree_process, richards, bench_mp_pool, docutils, mdp, scimark_monte_carlo, asyncio_tcp, xml_etree_iterparse, async_tree_none, chaos, async_tree_memoization, async_tree_cpu_io_mixed
