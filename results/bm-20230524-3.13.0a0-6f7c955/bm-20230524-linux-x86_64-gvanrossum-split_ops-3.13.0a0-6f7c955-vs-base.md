
# Results vs. base

- fork: gvanrossum
- ref: split_ops
- machine: linux-x86_64
- commit hash: 6f7c955
- commit date: 2023-05-24
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230524-linux-x86_64-python-b1cb30ec8639e4e65f62-3.13.0a0-b1cb30e | bm-20230524-linux-x86_64-gvanrossum-split_ops-3.13.0a0-6f7c955 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| docutils       | 2.74 sec                                                              | 2.72 sec: 1.01x faster                                         |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230524-linux-x86_64-python-b1cb30ec8639e4e65f62-3.13.0a0-b1cb30e | bm-20230524-linux-x86_64-gvanrossum-split_ops-3.13.0a0-6f7c955 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 79.7 ms                                                               | 80.4 ms: 1.01x slower                                          |
| nbody          | 88.5 ms                                                               | 89.8 ms: 1.01x slower                                          |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230524-linux-x86_64-python-b1cb30ec8639e4e65f62-3.13.0a0-b1cb30e | bm-20230524-linux-x86_64-gvanrossum-split_ops-3.13.0a0-6f7c955 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 144 ms                                                                | 145 ms: 1.01x slower                                           |
| regex_dna      | 209 ms                                                                | 214 ms: 1.02x slower                                           |
| regex_effbot   | 3.55 ms                                                               | 3.64 ms: 1.02x slower                                          |
| regex_v8       | 21.9 ms                                                               | 22.8 ms: 1.04x slower                                          |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230524-linux-x86_64-python-b1cb30ec8639e4e65f62-3.13.0a0-b1cb30e | bm-20230524-linux-x86_64-gvanrossum-split_ops-3.13.0a0-6f7c955 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| pickle_dict          | 31.9 us                                                               | 31.0 us: 1.03x faster                                          |
| pickle               | 10.8 us                                                               | 10.7 us: 1.01x faster                                          |
| pickle_list          | 4.60 us                                                               | 4.57 us: 1.01x faster                                          |
| pickle_pure_python   | 317 us                                                                | 315 us: 1.01x faster                                           |
| tomli_loads          | 2.17 sec                                                              | 2.18 sec: 1.00x slower                                         |
| xml_etree_generate   | 85.0 ms                                                               | 85.7 ms: 1.01x slower                                          |
| unpickle_pure_python | 216 us                                                                | 218 us: 1.01x slower                                           |
| xml_etree_iterparse  | 103 ms                                                                | 104 ms: 1.01x slower                                           |
| unpickle             | 14.7 us                                                               | 15.2 us: 1.03x slower                                          |
| unpickle_list        | 4.87 us                                                               | 5.08 us: 1.04x slower                                          |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                   |

Benchmark hidden because not significant (4): xml_etree_process, json_loads, json_dumps, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230524-linux-x86_64-python-b1cb30ec8639e4e65f62-3.13.0a0-b1cb30e | bm-20230524-linux-x86_64-gvanrossum-split_ops-3.13.0a0-6f7c955 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup_no_site | 6.79 ms                                                               | 6.78 ms: 1.00x faster                                          |
| python_startup         | 9.34 ms                                                               | 9.33 ms: 1.00x faster                                          |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230524-linux-x86_64-python-b1cb30ec8639e4e65f62-3.13.0a0-b1cb30e | bm-20230524-linux-x86_64-gvanrossum-split_ops-3.13.0a0-6f7c955 |
|-----------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| mako      | 10.6 ms                                                               | 10.4 ms: 1.01x faster                                          |

All benchmarks:
===============

| Benchmark               | bm-20230524-linux-x86_64-python-b1cb30ec8639e4e65f62-3.13.0a0-b1cb30e | bm-20230524-linux-x86_64-gvanrossum-split_ops-3.13.0a0-6f7c955 |
|-------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| gc_traversal            | 4.33 ms                                                               | 3.94 ms: 1.10x faster                                          |
| logging_silent          | 101 ns                                                                | 97.2 ns: 1.03x faster                                          |
| pickle_dict             | 31.9 us                                                               | 31.0 us: 1.03x faster                                          |
| deepcopy_reduce         | 3.24 us                                                               | 3.15 us: 1.03x faster                                          |
| pathlib                 | 18.9 ms                                                               | 18.4 ms: 1.03x faster                                          |
| pycparser               | 1.19 sec                                                              | 1.17 sec: 1.02x faster                                         |
| deltablue               | 3.53 ms                                                               | 3.46 ms: 1.02x faster                                          |
| generators              | 31.7 ms                                                               | 31.1 ms: 1.02x faster                                          |
| richards_super          | 50.8 ms                                                               | 50.0 ms: 1.01x faster                                          |
| async_generators        | 452 ms                                                                | 446 ms: 1.01x faster                                           |
| mako                    | 10.6 ms                                                               | 10.4 ms: 1.01x faster                                          |
| nqueens                 | 82.6 ms                                                               | 81.5 ms: 1.01x faster                                          |
| scimark_sparse_mat_mult | 4.84 ms                                                               | 4.78 ms: 1.01x faster                                          |
| raytrace                | 302 ms                                                                | 298 ms: 1.01x faster                                           |
| deepcopy                | 361 us                                                                | 357 us: 1.01x faster                                           |
| pyflate                 | 445 ms                                                                | 441 ms: 1.01x faster                                           |
| pickle                  | 10.8 us                                                               | 10.7 us: 1.01x faster                                          |
| pickle_list             | 4.60 us                                                               | 4.57 us: 1.01x faster                                          |
| pprint_pformat          | 1.49 sec                                                              | 1.48 sec: 1.01x faster                                         |
| crypto_pyaes            | 78.7 ms                                                               | 78.1 ms: 1.01x faster                                          |
| scimark_fft             | 354 ms                                                                | 351 ms: 1.01x faster                                           |
| pickle_pure_python      | 317 us                                                                | 315 us: 1.01x faster                                           |
| docutils                | 2.74 sec                                                              | 2.72 sec: 1.01x faster                                         |
| fannkuch                | 381 ms                                                                | 380 ms: 1.00x faster                                           |
| python_startup_no_site  | 6.79 ms                                                               | 6.78 ms: 1.00x faster                                          |
| python_startup          | 9.34 ms                                                               | 9.33 ms: 1.00x faster                                          |
| asyncio_tcp             | 513 ms                                                                | 515 ms: 1.00x slower                                           |
| tomli_loads             | 2.17 sec                                                              | 2.18 sec: 1.00x slower                                         |
| sqlglot_normalize       | 108 ms                                                                | 109 ms: 1.01x slower                                           |
| sqlglot_optimize        | 53.7 ms                                                               | 54.1 ms: 1.01x slower                                          |
| xml_etree_generate      | 85.0 ms                                                               | 85.7 ms: 1.01x slower                                          |
| scimark_sor             | 121 ms                                                                | 122 ms: 1.01x slower                                           |
| float                   | 79.7 ms                                                               | 80.4 ms: 1.01x slower                                          |
| go                      | 134 ms                                                                | 136 ms: 1.01x slower                                           |
| regex_compile           | 144 ms                                                                | 145 ms: 1.01x slower                                           |
| unpickle_pure_python    | 216 us                                                                | 218 us: 1.01x slower                                           |
| sqlite_synth            | 2.71 us                                                               | 2.74 us: 1.01x slower                                          |
| dulwich_log             | 67.4 ms                                                               | 68.1 ms: 1.01x slower                                          |
| xml_etree_iterparse     | 103 ms                                                                | 104 ms: 1.01x slower                                           |
| hexiom                  | 6.03 ms                                                               | 6.09 ms: 1.01x slower                                          |
| create_gc_cycles        | 1.50 ms                                                               | 1.52 ms: 1.01x slower                                          |
| nbody                   | 88.5 ms                                                               | 89.8 ms: 1.01x slower                                          |
| deepcopy_memo           | 37.5 us                                                               | 38.2 us: 1.02x slower                                          |
| coroutines              | 22.2 ms                                                               | 22.6 ms: 1.02x slower                                          |
| spectral_norm           | 106 ms                                                                | 108 ms: 1.02x slower                                           |
| regex_dna               | 209 ms                                                                | 214 ms: 1.02x slower                                           |
| regex_effbot            | 3.55 ms                                                               | 3.64 ms: 1.02x slower                                          |
| telco                   | 6.72 ms                                                               | 6.88 ms: 1.03x slower                                          |
| coverage                | 95.0 ms                                                               | 97.5 ms: 1.03x slower                                          |
| unpickle                | 14.7 us                                                               | 15.2 us: 1.03x slower                                          |
| chaos                   | 63.4 ms                                                               | 65.4 ms: 1.03x slower                                          |
| scimark_lu              | 112 ms                                                                | 116 ms: 1.04x slower                                           |
| regex_v8                | 21.9 ms                                                               | 22.8 ms: 1.04x slower                                          |
| unpickle_list           | 4.87 us                                                               | 5.08 us: 1.04x slower                                          |
| mdp                     | 2.55 sec                                                              | 2.70 sec: 1.06x slower                                         |
| unpack_sequence         | 47.6 ns                                                               | 50.4 ns: 1.06x slower                                          |
| Geometric mean          | (ref)                                                                 | 1.00x slower                                                   |

Benchmark hidden because not significant (26): logging_simple, async_tree_cpu_io_mixed, meteor_contest, xml_etree_process, async_tree_none, async_tree_io, async_tree_memoization, json_loads, scimark_monte_carlo, dask, comprehensions, pidigits, pprint_safe_repr, bench_mp_pool, asyncio_tcp_ssl, sqlglot_parse, json, typing_runtime_protocols, sqlglot_transpile, bench_thread_pool, mypy2, logging_format, richards, tornado_http, json_dumps, xml_etree_parse
