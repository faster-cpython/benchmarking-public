
# Results vs. base

- fork: brandtbucher
- ref: to_bool
- machine: linux-x86_64
- commit hash: f9fa498
- commit date: 2023-06-21
- overall geometric mean: 1.00x faster
- HPT reliability: 67.22%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230620-linux-x86_64-python-4d140e5e067d3315e163-3.13.0a0-4d140e5 | bm-20230621-linux-x86_64-brandtbucher-to_bool-3.13.0a0-f9fa498 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| nbody          | 90.8 ms                                                               | 88.3 ms: 1.03x faster                                          |
| pidigits       | 197 ms                                                                | 196 ms: 1.00x faster                                           |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                   |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230620-linux-x86_64-python-4d140e5e067d3315e163-3.13.0a0-4d140e5 | bm-20230621-linux-x86_64-brandtbucher-to_bool-3.13.0a0-f9fa498 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_dna      | 218 ms                                                                | 207 ms: 1.05x faster                                           |
| regex_effbot   | 3.60 ms                                                               | 3.50 ms: 1.03x faster                                          |
| regex_v8       | 22.2 ms                                                               | 21.8 ms: 1.02x faster                                          |
| regex_compile  | 136 ms                                                                | 135 ms: 1.01x faster                                           |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230620-linux-x86_64-python-4d140e5e067d3315e163-3.13.0a0-4d140e5 | bm-20230621-linux-x86_64-brandtbucher-to_bool-3.13.0a0-f9fa498 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| unpickle             | 15.4 us                                                               | 14.9 us: 1.04x faster                                          |
| pickle_pure_python   | 310 us                                                                | 301 us: 1.03x faster                                           |
| unpickle_pure_python | 216 us                                                                | 209 us: 1.03x faster                                           |
| xml_etree_generate   | 85.2 ms                                                               | 84.4 ms: 1.01x faster                                          |
| pickle               | 10.8 us                                                               | 10.7 us: 1.01x faster                                          |
| unpickle_list        | 4.93 us                                                               | 4.90 us: 1.01x faster                                          |
| json_dumps           | 9.82 ms                                                               | 9.91 ms: 1.01x slower                                          |
| tomli_loads          | 2.21 sec                                                              | 2.24 sec: 1.01x slower                                         |
| pickle_list          | 4.61 us                                                               | 4.67 us: 1.01x slower                                          |
| xml_etree_parse      | 154 ms                                                                | 156 ms: 1.02x slower                                           |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                   |

Benchmark hidden because not significant (4): xml_etree_process, json_loads, pickle_dict, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230620-linux-x86_64-python-4d140e5e067d3315e163-3.13.0a0-4d140e5 | bm-20230621-linux-x86_64-brandtbucher-to_bool-3.13.0a0-f9fa498 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup_no_site | 6.68 ms                                                               | 6.67 ms: 1.00x faster                                          |
| python_startup         | 9.19 ms                                                               | 9.19 ms: 1.00x slower                                          |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230620-linux-x86_64-python-4d140e5e067d3315e163-3.13.0a0-4d140e5 | bm-20230621-linux-x86_64-brandtbucher-to_bool-3.13.0a0-f9fa498 |
|-----------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| mako      | 10.9 ms                                                               | 10.6 ms: 1.03x faster                                          |

All benchmarks:
===============

| Benchmark               | bm-20230620-linux-x86_64-python-4d140e5e067d3315e163-3.13.0a0-4d140e5 | bm-20230621-linux-x86_64-brandtbucher-to_bool-3.13.0a0-f9fa498 |
|-------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_dna               | 218 ms                                                                | 207 ms: 1.05x faster                                           |
| generators              | 30.5 ms                                                               | 29.1 ms: 1.05x faster                                          |
| fannkuch                | 396 ms                                                                | 380 ms: 1.04x faster                                           |
| deepcopy_reduce         | 3.23 us                                                               | 3.10 us: 1.04x faster                                          |
| logging_simple          | 6.10 us                                                               | 5.85 us: 1.04x faster                                          |
| scimark_sor             | 121 ms                                                                | 116 ms: 1.04x faster                                           |
| unpickle                | 15.4 us                                                               | 14.9 us: 1.04x faster                                          |
| hexiom                  | 6.10 ms                                                               | 5.90 ms: 1.03x faster                                          |
| pickle_pure_python      | 310 us                                                                | 301 us: 1.03x faster                                           |
| unpickle_pure_python    | 216 us                                                                | 209 us: 1.03x faster                                           |
| logging_format          | 6.61 us                                                               | 6.41 us: 1.03x faster                                          |
| coverage                | 95.3 ms                                                               | 92.6 ms: 1.03x faster                                          |
| pycparser               | 1.18 sec                                                              | 1.15 sec: 1.03x faster                                         |
| nbody                   | 90.8 ms                                                               | 88.3 ms: 1.03x faster                                          |
| mako                    | 10.9 ms                                                               | 10.6 ms: 1.03x faster                                          |
| regex_effbot            | 3.60 ms                                                               | 3.50 ms: 1.03x faster                                          |
| pyflate                 | 450 ms                                                                | 441 ms: 1.02x faster                                           |
| coroutines              | 22.6 ms                                                               | 22.1 ms: 1.02x faster                                          |
| telco                   | 6.91 ms                                                               | 6.80 ms: 1.02x faster                                          |
| json                    | 4.87 ms                                                               | 4.79 ms: 1.02x faster                                          |
| deepcopy                | 352 us                                                                | 346 us: 1.02x faster                                           |
| regex_v8                | 22.2 ms                                                               | 21.8 ms: 1.02x faster                                          |
| logging_silent          | 101 ns                                                                | 99.5 ns: 1.01x faster                                          |
| regex_compile           | 136 ms                                                                | 135 ms: 1.01x faster                                           |
| xml_etree_generate      | 85.2 ms                                                               | 84.4 ms: 1.01x faster                                          |
| spectral_norm           | 105 ms                                                                | 104 ms: 1.01x faster                                           |
| async_generators        | 455 ms                                                                | 451 ms: 1.01x faster                                           |
| comprehensions          | 20.5 us                                                               | 20.3 us: 1.01x faster                                          |
| pickle                  | 10.8 us                                                               | 10.7 us: 1.01x faster                                          |
| mdp                     | 2.55 sec                                                              | 2.53 sec: 1.01x faster                                         |
| unpickle_list           | 4.93 us                                                               | 4.90 us: 1.01x faster                                          |
| deepcopy_memo           | 37.4 us                                                               | 37.2 us: 1.01x faster                                          |
| mypy2                   | 337 ms                                                                | 335 ms: 1.01x faster                                           |
| gc_traversal            | 3.84 ms                                                               | 3.82 ms: 1.01x faster                                          |
| create_gc_cycles        | 1.52 ms                                                               | 1.51 ms: 1.01x faster                                          |
| bench_thread_pool       | 823 us                                                                | 819 us: 1.00x faster                                           |
| pidigits                | 197 ms                                                                | 196 ms: 1.00x faster                                           |
| python_startup_no_site  | 6.68 ms                                                               | 6.67 ms: 1.00x faster                                          |
| python_startup          | 9.19 ms                                                               | 9.19 ms: 1.00x slower                                          |
| asyncio_tcp_ssl         | 1.79 sec                                                              | 1.80 sec: 1.00x slower                                         |
| async_tree_io           | 1.20 sec                                                              | 1.21 sec: 1.00x slower                                         |
| sqlglot_optimize        | 52.8 ms                                                               | 53.1 ms: 1.01x slower                                          |
| async_tree_memoization  | 588 ms                                                                | 592 ms: 1.01x slower                                           |
| dulwich_log             | 65.2 ms                                                               | 65.7 ms: 1.01x slower                                          |
| pprint_safe_repr        | 714 ms                                                                | 719 ms: 1.01x slower                                           |
| json_dumps              | 9.82 ms                                                               | 9.91 ms: 1.01x slower                                          |
| asyncio_tcp             | 503 ms                                                                | 508 ms: 1.01x slower                                           |
| scimark_monte_carlo     | 70.7 ms                                                               | 71.5 ms: 1.01x slower                                          |
| sqlglot_parse           | 1.30 ms                                                               | 1.32 ms: 1.01x slower                                          |
| pprint_pformat          | 1.46 sec                                                              | 1.48 sec: 1.01x slower                                         |
| tomli_loads             | 2.21 sec                                                              | 2.24 sec: 1.01x slower                                         |
| pickle_list             | 4.61 us                                                               | 4.67 us: 1.01x slower                                          |
| sqlglot_transpile       | 1.61 ms                                                               | 1.64 ms: 1.02x slower                                          |
| pathlib                 | 18.9 ms                                                               | 19.2 ms: 1.02x slower                                          |
| go                      | 135 ms                                                                | 137 ms: 1.02x slower                                           |
| xml_etree_parse         | 154 ms                                                                | 156 ms: 1.02x slower                                           |
| chaos                   | 61.0 ms                                                               | 62.2 ms: 1.02x slower                                          |
| meteor_contest          | 103 ms                                                                | 105 ms: 1.02x slower                                           |
| crypto_pyaes            | 75.8 ms                                                               | 77.3 ms: 1.02x slower                                          |
| scimark_sparse_mat_mult | 4.50 ms                                                               | 4.60 ms: 1.02x slower                                          |
| richards_super          | 50.4 ms                                                               | 52.4 ms: 1.04x slower                                          |
| nqueens                 | 78.5 ms                                                               | 82.3 ms: 1.05x slower                                          |
| richards                | 44.0 ms                                                               | 46.1 ms: 1.05x slower                                          |
| Geometric mean          | (ref)                                                                 | 1.00x faster                                                   |

Benchmark hidden because not significant (19): unpack_sequence, xml_etree_process, scimark_lu, float, docutils, scimark_fft, tornado_http, json_loads, async_tree_cpu_io_mixed, bench_mp_pool, sqlglot_normalize, raytrace, pickle_dict, deltablue, sqlite_synth, dask, xml_etree_iterparse, async_tree_none, typing_runtime_protocols


# HPT report

- Reliability score: 67.22% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
