
# Results vs. base

- fork: brandtbucher
- ref: to_bool
- machine: linux-x86_64
- commit hash: bab539b
- commit date: 2023-06-20
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230620-linux-x86_64-python-4d140e5e067d3315e163-3.13.0a0-4d140e5 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-bab539b |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 80.0 ms                                                               | 79.2 ms: 1.01x faster                                          |
| pidigits       | 197 ms                                                                | 196 ms: 1.00x faster                                           |
| nbody          | 90.8 ms                                                               | 93.8 ms: 1.03x slower                                          |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230620-linux-x86_64-python-4d140e5e067d3315e163-3.13.0a0-4d140e5 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-bab539b |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_dna      | 218 ms                                                                | 203 ms: 1.07x faster                                           |
| regex_effbot   | 3.60 ms                                                               | 3.51 ms: 1.02x faster                                          |
| regex_v8       | 22.2 ms                                                               | 21.9 ms: 1.01x faster                                          |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                   |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230620-linux-x86_64-python-4d140e5e067d3315e163-3.13.0a0-4d140e5 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-bab539b |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| unpickle             | 15.4 us                                                               | 14.8 us: 1.04x faster                                          |
| pickle_dict          | 31.9 us                                                               | 30.8 us: 1.04x faster                                          |
| xml_etree_generate   | 85.2 ms                                                               | 83.7 ms: 1.02x faster                                          |
| pickle_list          | 4.61 us                                                               | 4.55 us: 1.01x faster                                          |
| xml_etree_process    | 58.6 ms                                                               | 57.9 ms: 1.01x faster                                          |
| pickle_pure_python   | 310 us                                                                | 307 us: 1.01x faster                                           |
| pickle               | 10.8 us                                                               | 10.7 us: 1.01x faster                                          |
| unpickle_pure_python | 216 us                                                                | 214 us: 1.01x faster                                           |
| unpickle_list        | 4.93 us                                                               | 4.91 us: 1.01x faster                                          |
| json_loads           | 25.2 us                                                               | 25.1 us: 1.00x faster                                          |
| json_dumps           | 9.82 ms                                                               | 10.0 ms: 1.02x slower                                          |
| tomli_loads          | 2.21 sec                                                              | 2.30 sec: 1.04x slower                                         |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                   |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230620-linux-x86_64-python-4d140e5e067d3315e163-3.13.0a0-4d140e5 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-bab539b |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 9.19 ms                                                               | 9.17 ms: 1.00x faster                                          |
| python_startup_no_site | 6.68 ms                                                               | 6.67 ms: 1.00x faster                                          |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230620-linux-x86_64-python-4d140e5e067d3315e163-3.13.0a0-4d140e5 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-bab539b |
|-----------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| mako      | 10.9 ms                                                               | 10.6 ms: 1.03x faster                                          |

All benchmarks:
===============

| Benchmark               | bm-20230620-linux-x86_64-python-4d140e5e067d3315e163-3.13.0a0-4d140e5 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-bab539b |
|-------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_dna               | 218 ms                                                                | 203 ms: 1.07x faster                                           |
| generators              | 30.5 ms                                                               | 28.9 ms: 1.06x faster                                          |
| pycparser               | 1.18 sec                                                              | 1.14 sec: 1.04x faster                                         |
| unpickle                | 15.4 us                                                               | 14.8 us: 1.04x faster                                          |
| pickle_dict             | 31.9 us                                                               | 30.8 us: 1.04x faster                                          |
| mako                    | 10.9 ms                                                               | 10.6 ms: 1.03x faster                                          |
| fannkuch                | 396 ms                                                                | 385 ms: 1.03x faster                                           |
| spectral_norm           | 105 ms                                                                | 102 ms: 1.03x faster                                           |
| coroutines              | 22.6 ms                                                               | 22.1 ms: 1.02x faster                                          |
| regex_effbot            | 3.60 ms                                                               | 3.51 ms: 1.02x faster                                          |
| deepcopy_reduce         | 3.23 us                                                               | 3.16 us: 1.02x faster                                          |
| coverage                | 95.3 ms                                                               | 93.2 ms: 1.02x faster                                          |
| async_generators        | 455 ms                                                                | 446 ms: 1.02x faster                                           |
| xml_etree_generate      | 85.2 ms                                                               | 83.7 ms: 1.02x faster                                          |
| scimark_sor             | 121 ms                                                                | 119 ms: 1.02x faster                                           |
| create_gc_cycles        | 1.52 ms                                                               | 1.49 ms: 1.02x faster                                          |
| pickle_list             | 4.61 us                                                               | 4.55 us: 1.01x faster                                          |
| pyflate                 | 450 ms                                                                | 445 ms: 1.01x faster                                           |
| regex_v8                | 22.2 ms                                                               | 21.9 ms: 1.01x faster                                          |
| xml_etree_process       | 58.6 ms                                                               | 57.9 ms: 1.01x faster                                          |
| pickle_pure_python      | 310 us                                                                | 307 us: 1.01x faster                                           |
| float                   | 80.0 ms                                                               | 79.2 ms: 1.01x faster                                          |
| pickle                  | 10.8 us                                                               | 10.7 us: 1.01x faster                                          |
| sqlglot_normalize       | 106 ms                                                                | 106 ms: 1.01x faster                                           |
| deepcopy                | 352 us                                                                | 349 us: 1.01x faster                                           |
| unpickle_pure_python    | 216 us                                                                | 214 us: 1.01x faster                                           |
| nqueens                 | 78.5 ms                                                               | 78.0 ms: 1.01x faster                                          |
| comprehensions          | 20.5 us                                                               | 20.3 us: 1.01x faster                                          |
| logging_simple          | 6.10 us                                                               | 6.06 us: 1.01x faster                                          |
| unpickle_list           | 4.93 us                                                               | 4.91 us: 1.01x faster                                          |
| json_loads              | 25.2 us                                                               | 25.1 us: 1.00x faster                                          |
| pidigits                | 197 ms                                                                | 196 ms: 1.00x faster                                           |
| async_tree_io           | 1.20 sec                                                              | 1.20 sec: 1.00x faster                                         |
| mypy2                   | 337 ms                                                                | 336 ms: 1.00x faster                                           |
| bench_thread_pool       | 823 us                                                                | 821 us: 1.00x faster                                           |
| python_startup          | 9.19 ms                                                               | 9.17 ms: 1.00x faster                                          |
| python_startup_no_site  | 6.68 ms                                                               | 6.67 ms: 1.00x faster                                          |
| deepcopy_memo           | 37.4 us                                                               | 37.7 us: 1.01x slower                                          |
| raytrace                | 293 ms                                                                | 296 ms: 1.01x slower                                           |
| dask                    | 519 ms                                                                | 523 ms: 1.01x slower                                           |
| asyncio_tcp             | 503 ms                                                                | 508 ms: 1.01x slower                                           |
| chaos                   | 61.0 ms                                                               | 61.6 ms: 1.01x slower                                          |
| dulwich_log             | 65.2 ms                                                               | 66.1 ms: 1.01x slower                                          |
| go                      | 135 ms                                                                | 137 ms: 1.02x slower                                           |
| scimark_fft             | 346 ms                                                                | 352 ms: 1.02x slower                                           |
| scimark_lu              | 109 ms                                                                | 111 ms: 1.02x slower                                           |
| json_dumps              | 9.82 ms                                                               | 10.0 ms: 1.02x slower                                          |
| scimark_monte_carlo     | 70.7 ms                                                               | 72.3 ms: 1.02x slower                                          |
| meteor_contest          | 103 ms                                                                | 106 ms: 1.02x slower                                           |
| sqlglot_parse           | 1.30 ms                                                               | 1.33 ms: 1.02x slower                                          |
| sqlglot_transpile       | 1.61 ms                                                               | 1.66 ms: 1.03x slower                                          |
| pprint_safe_repr        | 714 ms                                                                | 736 ms: 1.03x slower                                           |
| nbody                   | 90.8 ms                                                               | 93.8 ms: 1.03x slower                                          |
| pprint_pformat          | 1.46 sec                                                              | 1.51 sec: 1.04x slower                                         |
| tomli_loads             | 2.21 sec                                                              | 2.30 sec: 1.04x slower                                         |
| logging_silent          | 101 ns                                                                | 105 ns: 1.04x slower                                           |
| richards_super          | 50.4 ms                                                               | 52.8 ms: 1.05x slower                                          |
| scimark_sparse_mat_mult | 4.50 ms                                                               | 4.74 ms: 1.05x slower                                          |
| unpack_sequence         | 46.1 ns                                                               | 48.9 ns: 1.06x slower                                          |
| richards                | 44.0 ms                                                               | 47.1 ms: 1.07x slower                                          |
| gc_traversal            | 3.84 ms                                                               | 4.32 ms: 1.13x slower                                          |
| Geometric mean          | (ref)                                                                 | 1.00x slower                                                   |

Benchmark hidden because not significant (21): async_tree_cpu_io_mixed, pathlib, logging_format, async_tree_none, json, telco, xml_etree_parse, docutils, asyncio_tcp_ssl, mdp, typing_runtime_protocols, bench_mp_pool, async_tree_memoization, sqlglot_optimize, crypto_pyaes, sqlite_synth, deltablue, xml_etree_iterparse, hexiom, tornado_http, regex_compile
