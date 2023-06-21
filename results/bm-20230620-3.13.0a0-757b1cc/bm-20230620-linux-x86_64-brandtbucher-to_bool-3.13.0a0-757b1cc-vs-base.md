
# Results vs. base

- fork: brandtbucher
- ref: to_bool
- machine: linux-x86_64
- commit hash: 757b1cc
- commit date: 2023-06-20
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230620-linux-x86_64-python-4d140e5e067d3315e163-3.13.0a0-4d140e5 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-757b1cc |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| tornado_http   | 96.4 ms                                                               | 97.0 ms: 1.01x slower                                          |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                   |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230620-linux-x86_64-python-4d140e5e067d3315e163-3.13.0a0-4d140e5 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-757b1cc |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| pidigits       | 197 ms                                                                | 192 ms: 1.03x faster                                           |
| nbody          | 90.8 ms                                                               | 92.2 ms: 1.02x slower                                          |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                   |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230620-linux-x86_64-python-4d140e5e067d3315e163-3.13.0a0-4d140e5 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-757b1cc |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_effbot   | 3.60 ms                                                               | 3.56 ms: 1.01x faster                                          |
| regex_v8       | 22.2 ms                                                               | 22.6 ms: 1.02x slower                                          |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                   |

Benchmark hidden because not significant (2): regex_dna, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230620-linux-x86_64-python-4d140e5e067d3315e163-3.13.0a0-4d140e5 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-757b1cc |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| unpickle             | 15.4 us                                                               | 14.8 us: 1.04x faster                                          |
| pickle               | 10.8 us                                                               | 10.4 us: 1.04x faster                                          |
| xml_etree_generate   | 85.2 ms                                                               | 84.3 ms: 1.01x faster                                          |
| pickle_pure_python   | 310 us                                                                | 308 us: 1.01x faster                                           |
| unpickle_pure_python | 216 us                                                                | 215 us: 1.00x faster                                           |
| json_loads           | 25.2 us                                                               | 25.1 us: 1.00x faster                                          |
| pickle_dict          | 31.9 us                                                               | 32.1 us: 1.00x slower                                          |
| unpickle_list        | 4.93 us                                                               | 4.96 us: 1.01x slower                                          |
| json_dumps           | 9.82 ms                                                               | 9.95 ms: 1.01x slower                                          |
| tomli_loads          | 2.21 sec                                                              | 2.27 sec: 1.03x slower                                         |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                   |

Benchmark hidden because not significant (4): xml_etree_process, xml_etree_iterparse, xml_etree_parse, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20230620-linux-x86_64-python-4d140e5e067d3315e163-3.13.0a0-4d140e5 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-757b1cc |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup | 9.19 ms                                                               | 9.17 ms: 1.00x faster                                          |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                   |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230620-linux-x86_64-python-4d140e5e067d3315e163-3.13.0a0-4d140e5 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-757b1cc |
|-----------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| mako      | 10.9 ms                                                               | 10.7 ms: 1.02x faster                                          |

All benchmarks:
===============

| Benchmark               | bm-20230620-linux-x86_64-python-4d140e5e067d3315e163-3.13.0a0-4d140e5 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-757b1cc |
|-------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| gc_traversal            | 3.84 ms                                                               | 3.68 ms: 1.04x faster                                          |
| unpickle                | 15.4 us                                                               | 14.8 us: 1.04x faster                                          |
| pickle                  | 10.8 us                                                               | 10.4 us: 1.04x faster                                          |
| generators              | 30.5 ms                                                               | 29.4 ms: 1.04x faster                                          |
| pidigits                | 197 ms                                                                | 192 ms: 1.03x faster                                           |
| coverage                | 95.3 ms                                                               | 92.9 ms: 1.03x faster                                          |
| telco                   | 6.91 ms                                                               | 6.75 ms: 1.02x faster                                          |
| mako                    | 10.9 ms                                                               | 10.7 ms: 1.02x faster                                          |
| json                    | 4.87 ms                                                               | 4.78 ms: 1.02x faster                                          |
| scimark_sor             | 121 ms                                                                | 119 ms: 1.02x faster                                           |
| async_generators        | 455 ms                                                                | 448 ms: 1.01x faster                                           |
| spectral_norm           | 105 ms                                                                | 104 ms: 1.01x faster                                           |
| xml_etree_generate      | 85.2 ms                                                               | 84.3 ms: 1.01x faster                                          |
| logging_format          | 6.61 us                                                               | 6.53 us: 1.01x faster                                          |
| logging_simple          | 6.10 us                                                               | 6.03 us: 1.01x faster                                          |
| nqueens                 | 78.5 ms                                                               | 77.7 ms: 1.01x faster                                          |
| create_gc_cycles        | 1.52 ms                                                               | 1.50 ms: 1.01x faster                                          |
| deepcopy_reduce         | 3.23 us                                                               | 3.20 us: 1.01x faster                                          |
| regex_effbot            | 3.60 ms                                                               | 3.56 ms: 1.01x faster                                          |
| pickle_pure_python      | 310 us                                                                | 308 us: 1.01x faster                                           |
| bench_thread_pool       | 823 us                                                                | 819 us: 1.01x faster                                           |
| deepcopy                | 352 us                                                                | 351 us: 1.00x faster                                           |
| unpickle_pure_python    | 216 us                                                                | 215 us: 1.00x faster                                           |
| hexiom                  | 6.10 ms                                                               | 6.07 ms: 1.00x faster                                          |
| fannkuch                | 396 ms                                                                | 395 ms: 1.00x faster                                           |
| json_loads              | 25.2 us                                                               | 25.1 us: 1.00x faster                                          |
| python_startup          | 9.19 ms                                                               | 9.17 ms: 1.00x faster                                          |
| dulwich_log             | 65.2 ms                                                               | 65.5 ms: 1.00x slower                                          |
| asyncio_tcp_ssl         | 1.79 sec                                                              | 1.80 sec: 1.00x slower                                         |
| pickle_dict             | 31.9 us                                                               | 32.1 us: 1.00x slower                                          |
| unpickle_list           | 4.93 us                                                               | 4.96 us: 1.01x slower                                          |
| asyncio_tcp             | 503 ms                                                                | 506 ms: 1.01x slower                                           |
| tornado_http            | 96.4 ms                                                               | 97.0 ms: 1.01x slower                                          |
| async_tree_none         | 484 ms                                                                | 487 ms: 1.01x slower                                           |
| unpack_sequence         | 46.1 ns                                                               | 46.3 ns: 1.01x slower                                          |
| raytrace                | 293 ms                                                                | 295 ms: 1.01x slower                                           |
| scimark_fft             | 346 ms                                                                | 349 ms: 1.01x slower                                           |
| pycparser               | 1.18 sec                                                              | 1.19 sec: 1.01x slower                                         |
| async_tree_memoization  | 588 ms                                                                | 594 ms: 1.01x slower                                           |
| deltablue               | 3.28 ms                                                               | 3.32 ms: 1.01x slower                                          |
| pyflate                 | 450 ms                                                                | 456 ms: 1.01x slower                                           |
| json_dumps              | 9.82 ms                                                               | 9.95 ms: 1.01x slower                                          |
| meteor_contest          | 103 ms                                                                | 105 ms: 1.01x slower                                           |
| sqlglot_optimize        | 52.8 ms                                                               | 53.5 ms: 1.01x slower                                          |
| dask                    | 519 ms                                                                | 526 ms: 1.01x slower                                           |
| nbody                   | 90.8 ms                                                               | 92.2 ms: 1.02x slower                                          |
| scimark_monte_carlo     | 70.7 ms                                                               | 72.0 ms: 1.02x slower                                          |
| chaos                   | 61.0 ms                                                               | 62.1 ms: 1.02x slower                                          |
| regex_v8                | 22.2 ms                                                               | 22.6 ms: 1.02x slower                                          |
| crypto_pyaes            | 75.8 ms                                                               | 77.3 ms: 1.02x slower                                          |
| scimark_lu              | 109 ms                                                                | 112 ms: 1.02x slower                                           |
| pprint_pformat          | 1.46 sec                                                              | 1.50 sec: 1.03x slower                                         |
| tomli_loads             | 2.21 sec                                                              | 2.27 sec: 1.03x slower                                         |
| pprint_safe_repr        | 714 ms                                                                | 735 ms: 1.03x slower                                           |
| logging_silent          | 101 ns                                                                | 104 ns: 1.03x slower                                           |
| sqlglot_parse           | 1.30 ms                                                               | 1.35 ms: 1.03x slower                                          |
| sqlglot_transpile       | 1.61 ms                                                               | 1.67 ms: 1.03x slower                                          |
| scimark_sparse_mat_mult | 4.50 ms                                                               | 4.66 ms: 1.03x slower                                          |
| go                      | 135 ms                                                                | 141 ms: 1.04x slower                                           |
| coroutines              | 22.6 ms                                                               | 23.6 ms: 1.04x slower                                          |
| mdp                     | 2.55 sec                                                              | 2.69 sec: 1.05x slower                                         |
| richards_super          | 50.4 ms                                                               | 53.4 ms: 1.06x slower                                          |
| richards                | 44.0 ms                                                               | 47.5 ms: 1.08x slower                                          |
| Geometric mean          | (ref)                                                                 | 1.00x slower                                                   |

Benchmark hidden because not significant (19): pathlib, xml_etree_process, comprehensions, regex_dna, mypy2, xml_etree_iterparse, python_startup_no_site, float, async_tree_io, xml_etree_parse, bench_mp_pool, regex_compile, sqlite_synth, async_tree_cpu_io_mixed, docutils, deepcopy_memo, pickle_list, sqlglot_normalize, typing_runtime_protocols
