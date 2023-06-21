
# Results vs. base

- fork: brandtbucher
- ref: to_bool
- machine: linux-x86_64
- commit hash: a0bd53a
- commit date: 2023-06-20
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230620-linux-x86_64-python-4d140e5e067d3315e163-3.13.0a0-4d140e5 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-a0bd53a |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| tornado_http   | 96.4 ms                                                               | 97.3 ms: 1.01x slower                                          |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                   |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230620-linux-x86_64-python-4d140e5e067d3315e163-3.13.0a0-4d140e5 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-a0bd53a |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| nbody          | 90.8 ms                                                               | 90.2 ms: 1.01x faster                                          |
| pidigits       | 197 ms                                                                | 196 ms: 1.01x faster                                           |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                   |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230620-linux-x86_64-python-4d140e5e067d3315e163-3.13.0a0-4d140e5 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-a0bd53a |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_dna      | 218 ms                                                                | 202 ms: 1.08x faster                                           |
| regex_effbot   | 3.60 ms                                                               | 3.44 ms: 1.04x faster                                          |
| regex_v8       | 22.2 ms                                                               | 21.7 ms: 1.02x faster                                          |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                   |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230620-linux-x86_64-python-4d140e5e067d3315e163-3.13.0a0-4d140e5 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-a0bd53a |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| unpickle             | 15.4 us                                                               | 14.8 us: 1.04x faster                                          |
| pickle               | 10.8 us                                                               | 10.7 us: 1.01x faster                                          |
| xml_etree_process    | 58.6 ms                                                               | 58.1 ms: 1.01x faster                                          |
| xml_etree_generate   | 85.2 ms                                                               | 84.5 ms: 1.01x faster                                          |
| unpickle_pure_python | 216 us                                                                | 217 us: 1.01x slower                                           |
| xml_etree_iterparse  | 103 ms                                                                | 104 ms: 1.01x slower                                           |
| json_loads           | 25.2 us                                                               | 25.4 us: 1.01x slower                                          |
| pickle_dict          | 31.9 us                                                               | 32.4 us: 1.02x slower                                          |
| unpickle_list        | 4.93 us                                                               | 5.03 us: 1.02x slower                                          |
| tomli_loads          | 2.21 sec                                                              | 2.30 sec: 1.04x slower                                         |
| json_dumps           | 9.82 ms                                                               | 10.2 ms: 1.04x slower                                          |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                   |

Benchmark hidden because not significant (3): xml_etree_parse, pickle_pure_python, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230620-linux-x86_64-python-4d140e5e067d3315e163-3.13.0a0-4d140e5 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-a0bd53a |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 9.19 ms                                                               | 9.23 ms: 1.00x slower                                          |
| python_startup_no_site | 6.68 ms                                                               | 6.71 ms: 1.01x slower                                          |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230620-linux-x86_64-python-4d140e5e067d3315e163-3.13.0a0-4d140e5 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-a0bd53a |
|-----------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| mako      | 10.9 ms                                                               | 10.6 ms: 1.03x faster                                          |

All benchmarks:
===============

| Benchmark               | bm-20230620-linux-x86_64-python-4d140e5e067d3315e163-3.13.0a0-4d140e5 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-a0bd53a |
|-------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| gc_traversal            | 3.84 ms                                                               | 3.54 ms: 1.08x faster                                          |
| regex_dna               | 218 ms                                                                | 202 ms: 1.08x faster                                           |
| generators              | 30.5 ms                                                               | 29.0 ms: 1.05x faster                                          |
| regex_effbot            | 3.60 ms                                                               | 3.44 ms: 1.04x faster                                          |
| unpickle                | 15.4 us                                                               | 14.8 us: 1.04x faster                                          |
| fannkuch                | 396 ms                                                                | 385 ms: 1.03x faster                                           |
| pycparser               | 1.18 sec                                                              | 1.15 sec: 1.03x faster                                         |
| mako                    | 10.9 ms                                                               | 10.6 ms: 1.03x faster                                          |
| coroutines              | 22.6 ms                                                               | 22.1 ms: 1.02x faster                                          |
| regex_v8                | 22.2 ms                                                               | 21.7 ms: 1.02x faster                                          |
| deepcopy_reduce         | 3.23 us                                                               | 3.16 us: 1.02x faster                                          |
| async_generators        | 455 ms                                                                | 446 ms: 1.02x faster                                           |
| unpack_sequence         | 46.1 ns                                                               | 45.2 ns: 1.02x faster                                          |
| coverage                | 95.3 ms                                                               | 93.5 ms: 1.02x faster                                          |
| pickle                  | 10.8 us                                                               | 10.7 us: 1.01x faster                                          |
| logging_simple          | 6.10 us                                                               | 6.01 us: 1.01x faster                                          |
| pathlib                 | 18.9 ms                                                               | 18.6 ms: 1.01x faster                                          |
| spectral_norm           | 105 ms                                                                | 104 ms: 1.01x faster                                           |
| xml_etree_process       | 58.6 ms                                                               | 58.1 ms: 1.01x faster                                          |
| create_gc_cycles        | 1.52 ms                                                               | 1.50 ms: 1.01x faster                                          |
| telco                   | 6.91 ms                                                               | 6.85 ms: 1.01x faster                                          |
| scimark_sor             | 121 ms                                                                | 120 ms: 1.01x faster                                           |
| xml_etree_generate      | 85.2 ms                                                               | 84.5 ms: 1.01x faster                                          |
| nbody                   | 90.8 ms                                                               | 90.2 ms: 1.01x faster                                          |
| pidigits                | 197 ms                                                                | 196 ms: 1.01x faster                                           |
| deepcopy                | 352 us                                                                | 351 us: 1.00x faster                                           |
| hexiom                  | 6.10 ms                                                               | 6.08 ms: 1.00x faster                                          |
| asyncio_tcp_ssl         | 1.79 sec                                                              | 1.79 sec: 1.00x faster                                         |
| python_startup          | 9.19 ms                                                               | 9.23 ms: 1.00x slower                                          |
| unpickle_pure_python    | 216 us                                                                | 217 us: 1.01x slower                                           |
| python_startup_no_site  | 6.68 ms                                                               | 6.71 ms: 1.01x slower                                          |
| xml_etree_iterparse     | 103 ms                                                                | 104 ms: 1.01x slower                                           |
| sqlglot_normalize       | 106 ms                                                                | 107 ms: 1.01x slower                                           |
| nqueens                 | 78.5 ms                                                               | 79.1 ms: 1.01x slower                                          |
| async_tree_io           | 1.20 sec                                                              | 1.21 sec: 1.01x slower                                         |
| pyflate                 | 450 ms                                                                | 454 ms: 1.01x slower                                           |
| json_loads              | 25.2 us                                                               | 25.4 us: 1.01x slower                                          |
| async_tree_memoization  | 588 ms                                                                | 593 ms: 1.01x slower                                           |
| tornado_http            | 96.4 ms                                                               | 97.3 ms: 1.01x slower                                          |
| comprehensions          | 20.5 us                                                               | 20.7 us: 1.01x slower                                          |
| dulwich_log             | 65.2 ms                                                               | 65.8 ms: 1.01x slower                                          |
| sqlglot_optimize        | 52.8 ms                                                               | 53.4 ms: 1.01x slower                                          |
| deepcopy_memo           | 37.4 us                                                               | 37.9 us: 1.01x slower                                          |
| asyncio_tcp             | 503 ms                                                                | 510 ms: 1.01x slower                                           |
| chaos                   | 61.0 ms                                                               | 61.9 ms: 1.01x slower                                          |
| scimark_monte_carlo     | 70.7 ms                                                               | 71.8 ms: 1.01x slower                                          |
| pickle_dict             | 31.9 us                                                               | 32.4 us: 1.02x slower                                          |
| dask                    | 519 ms                                                                | 527 ms: 1.02x slower                                           |
| crypto_pyaes            | 75.8 ms                                                               | 77.2 ms: 1.02x slower                                          |
| sqlglot_parse           | 1.30 ms                                                               | 1.33 ms: 1.02x slower                                          |
| unpickle_list           | 4.93 us                                                               | 5.03 us: 1.02x slower                                          |
| meteor_contest          | 103 ms                                                                | 106 ms: 1.02x slower                                           |
| sqlglot_transpile       | 1.61 ms                                                               | 1.65 ms: 1.02x slower                                          |
| pprint_pformat          | 1.46 sec                                                              | 1.50 sec: 1.03x slower                                         |
| go                      | 135 ms                                                                | 139 ms: 1.03x slower                                           |
| pprint_safe_repr        | 714 ms                                                                | 736 ms: 1.03x slower                                           |
| scimark_fft             | 346 ms                                                                | 358 ms: 1.03x slower                                           |
| tomli_loads             | 2.21 sec                                                              | 2.30 sec: 1.04x slower                                         |
| json_dumps              | 9.82 ms                                                               | 10.2 ms: 1.04x slower                                          |
| mdp                     | 2.55 sec                                                              | 2.69 sec: 1.05x slower                                         |
| logging_silent          | 101 ns                                                                | 107 ns: 1.06x slower                                           |
| scimark_sparse_mat_mult | 4.50 ms                                                               | 4.79 ms: 1.06x slower                                          |
| richards_super          | 50.4 ms                                                               | 54.0 ms: 1.07x slower                                          |
| richards                | 44.0 ms                                                               | 47.9 ms: 1.09x slower                                          |
| Geometric mean          | (ref)                                                                 | 1.00x slower                                                   |

Benchmark hidden because not significant (18): json, scimark_lu, xml_etree_parse, async_tree_cpu_io_mixed, mypy2, docutils, pickle_pure_python, bench_mp_pool, logging_format, bench_thread_pool, sqlite_synth, raytrace, float, async_tree_none, typing_runtime_protocols, deltablue, pickle_list, regex_compile
