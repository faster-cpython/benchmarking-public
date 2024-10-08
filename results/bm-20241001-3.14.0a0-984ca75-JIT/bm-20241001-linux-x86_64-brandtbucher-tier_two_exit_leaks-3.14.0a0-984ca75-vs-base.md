# Results vs. base

- fork: brandtbucher
- ref: tier_two_exit_leaks
- machine: linux-x86_64
- commit hash: 984ca75
- commit date: 2024-10-01
- overall geometric mean: 1.00x slower
- HPT reliability: 90.99%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240929-linux-x86_64-python-6f4d64b048133c60d407-3.14.0a0-6f4d64b | bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                                | 279 ms: 1.00x faster                                                       |
| html5lib       | 65.5 ms                                                               | 66.2 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                               |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240929-linux-x86_64-python-6f4d64b048133c60d407-3.14.0a0-6f4d64b | bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75 |
|------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| coroutines       | 23.2 ms                                                               | 23.3 ms: 1.01x slower                                                      |
| asyncio_tcp_ssl  | 1.79 sec                                                              | 1.80 sec: 1.01x slower                                                     |
| async_generators | 453 ms                                                                | 457 ms: 1.01x slower                                                       |
| asyncio_tcp      | 488 ms                                                                | 494 ms: 1.01x slower                                                       |
| Geometric mean   | (ref)                                                                 | 1.00x slower                                                               |

Benchmark hidden because not significant (9): async_tree_memoization, async_tree_io_tg, async_tree_io, async_tree_none, asyncio_websockets, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240929-linux-x86_64-python-6f4d64b048133c60d407-3.14.0a0-6f4d64b | bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                | 186 ms: 1.00x faster                                                       |
| float          | 72.0 ms                                                               | 72.3 ms: 1.00x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                               |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240929-linux-x86_64-python-6f4d64b048133c60d407-3.14.0a0-6f4d64b | bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.79 ms                                                               | 3.65 ms: 1.04x faster                                                      |
| regex_compile  | 145 ms                                                                | 143 ms: 1.01x faster                                                       |
| regex_v8       | 24.6 ms                                                               | 24.3 ms: 1.01x faster                                                      |
| regex_dna      | 218 ms                                                                | 222 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240929-linux-x86_64-python-6f4d64b048133c60d407-3.14.0a0-6f4d64b | bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle             | 15.3 us                                                               | 14.7 us: 1.04x faster                                                      |
| unpickle_list        | 5.44 us                                                               | 5.33 us: 1.02x faster                                                      |
| unpickle_pure_python | 214 us                                                                | 213 us: 1.00x faster                                                       |
| xml_etree_iterparse  | 97.8 ms                                                               | 97.5 ms: 1.00x faster                                                      |
| pickle_dict          | 34.7 us                                                               | 34.7 us: 1.00x slower                                                      |
| xml_etree_process    | 54.9 ms                                                               | 55.2 ms: 1.01x slower                                                      |
| xml_etree_generate   | 77.2 ms                                                               | 77.7 ms: 1.01x slower                                                      |
| pickle_pure_python   | 306 us                                                                | 310 us: 1.01x slower                                                       |
| pickle               | 11.4 us                                                               | 11.7 us: 1.02x slower                                                      |
| json_dumps           | 10.1 ms                                                               | 10.3 ms: 1.02x slower                                                      |
| pickle_list          | 4.92 us                                                               | 5.18 us: 1.05x slower                                                      |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                               |

Benchmark hidden because not significant (3): tomli_loads, xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240929-linux-x86_64-python-6f4d64b048133c60d407-3.14.0a0-6f4d64b | bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 7.07 ms                                                               | 7.06 ms: 1.00x faster                                                      |
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                      |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240929-linux-x86_64-python-6f4d64b048133c60d407-3.14.0a0-6f4d64b | bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 36.3 ms                                                               | 36.0 ms: 1.01x faster                                                      |
| mako            | 9.80 ms                                                               | 9.87 ms: 1.01x slower                                                      |
| genshi_text     | 24.7 ms                                                               | 25.3 ms: 1.02x slower                                                      |
| genshi_xml      | 57.3 ms                                                               | 59.2 ms: 1.03x slower                                                      |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                               |

All benchmarks:
===============

| Benchmark               | bm-20240929-linux-x86_64-python-6f4d64b048133c60d407-3.14.0a0-6f4d64b | bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75 |
|-------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| scimark_sparse_mat_mult | 4.55 ms                                                               | 4.37 ms: 1.04x faster                                                      |
| unpickle                | 15.3 us                                                               | 14.7 us: 1.04x faster                                                      |
| regex_effbot            | 3.79 ms                                                               | 3.65 ms: 1.04x faster                                                      |
| scimark_fft             | 317 ms                                                                | 307 ms: 1.03x faster                                                       |
| unpickle_list           | 5.44 us                                                               | 5.33 us: 1.02x faster                                                      |
| dulwich_log             | 69.0 ms                                                               | 67.8 ms: 1.02x faster                                                      |
| scimark_sor             | 119 ms                                                                | 117 ms: 1.02x faster                                                       |
| unpack_sequence         | 110 ns                                                                | 108 ns: 1.02x faster                                                       |
| regex_compile           | 145 ms                                                                | 143 ms: 1.01x faster                                                       |
| sympy_str               | 308 ms                                                                | 305 ms: 1.01x faster                                                       |
| scimark_lu              | 110 ms                                                                | 109 ms: 1.01x faster                                                       |
| regex_v8                | 24.6 ms                                                               | 24.3 ms: 1.01x faster                                                      |
| telco                   | 7.55 ms                                                               | 7.49 ms: 1.01x faster                                                      |
| mdp                     | 2.56 sec                                                              | 2.54 sec: 1.01x faster                                                     |
| create_gc_cycles        | 1.74 ms                                                               | 1.73 ms: 1.01x faster                                                      |
| sympy_expand            | 511 ms                                                                | 508 ms: 1.01x faster                                                       |
| scimark_monte_carlo     | 62.9 ms                                                               | 62.5 ms: 1.01x faster                                                      |
| django_template         | 36.3 ms                                                               | 36.0 ms: 1.01x faster                                                      |
| richards_super          | 45.3 ms                                                               | 45.1 ms: 1.01x faster                                                      |
| bpe_tokeniser           | 4.44 sec                                                              | 4.42 sec: 1.01x faster                                                     |
| unpickle_pure_python    | 214 us                                                                | 213 us: 1.00x faster                                                       |
| sympy_sum               | 177 ms                                                                | 176 ms: 1.00x faster                                                       |
| comprehensions          | 16.8 us                                                               | 16.8 us: 1.00x faster                                                      |
| 2to3                    | 280 ms                                                                | 279 ms: 1.00x faster                                                       |
| crypto_pyaes            | 65.9 ms                                                               | 65.7 ms: 1.00x faster                                                      |
| xml_etree_iterparse     | 97.8 ms                                                               | 97.5 ms: 1.00x faster                                                      |
| meteor_contest          | 107 ms                                                                | 106 ms: 1.00x faster                                                       |
| python_startup_no_site  | 7.07 ms                                                               | 7.06 ms: 1.00x faster                                                      |
| pidigits                | 186 ms                                                                | 186 ms: 1.00x faster                                                       |
| python_startup          | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                      |
| pickle_dict             | 34.7 us                                                               | 34.7 us: 1.00x slower                                                      |
| bench_thread_pool       | 891 us                                                                | 894 us: 1.00x slower                                                       |
| sqlglot_optimize        | 60.3 ms                                                               | 60.5 ms: 1.00x slower                                                      |
| float                   | 72.0 ms                                                               | 72.3 ms: 1.00x slower                                                      |
| coroutines              | 23.2 ms                                                               | 23.3 ms: 1.01x slower                                                      |
| xml_etree_process       | 54.9 ms                                                               | 55.2 ms: 1.01x slower                                                      |
| go                      | 131 ms                                                                | 132 ms: 1.01x slower                                                       |
| sqlite_synth            | 2.72 us                                                               | 2.74 us: 1.01x slower                                                      |
| xml_etree_generate      | 77.2 ms                                                               | 77.7 ms: 1.01x slower                                                      |
| asyncio_tcp_ssl         | 1.79 sec                                                              | 1.80 sec: 1.01x slower                                                     |
| mako                    | 9.80 ms                                                               | 9.87 ms: 1.01x slower                                                      |
| async_generators        | 453 ms                                                                | 457 ms: 1.01x slower                                                       |
| chaos                   | 59.6 ms                                                               | 60.0 ms: 1.01x slower                                                      |
| richards                | 39.7 ms                                                               | 40.0 ms: 1.01x slower                                                      |
| sqlglot_normalize       | 116 ms                                                                | 117 ms: 1.01x slower                                                       |
| fannkuch                | 372 ms                                                                | 376 ms: 1.01x slower                                                       |
| html5lib                | 65.5 ms                                                               | 66.2 ms: 1.01x slower                                                      |
| asyncio_tcp             | 488 ms                                                                | 494 ms: 1.01x slower                                                       |
| pickle_pure_python      | 306 us                                                                | 310 us: 1.01x slower                                                       |
| regex_dna               | 218 ms                                                                | 222 ms: 1.02x slower                                                       |
| pickle                  | 11.4 us                                                               | 11.7 us: 1.02x slower                                                      |
| json_dumps              | 10.1 ms                                                               | 10.3 ms: 1.02x slower                                                      |
| thrift                  | 792 us                                                                | 809 us: 1.02x slower                                                       |
| genshi_text             | 24.7 ms                                                               | 25.3 ms: 1.02x slower                                                      |
| pyflate                 | 450 ms                                                                | 462 ms: 1.02x slower                                                       |
| genshi_xml              | 57.3 ms                                                               | 59.2 ms: 1.03x slower                                                      |
| gc_traversal            | 3.84 ms                                                               | 3.99 ms: 1.04x slower                                                      |
| nqueens                 | 85.1 ms                                                               | 88.6 ms: 1.04x slower                                                      |
| pickle_list             | 4.92 us                                                               | 5.18 us: 1.05x slower                                                      |
| Geometric mean          | (ref)                                                                 | 1.00x slower                                                               |

Benchmark hidden because not significant (38): typing_runtime_protocols, coverage, logging_format, deepcopy_memo, pprint_safe_repr, spectral_norm, bench_mp_pool, async_tree_memoization, sqlglot_parse, deepcopy_reduce, sqlglot_transpile, nbody, deltablue, sympy_integrate, logging_silent, pathlib, async_tree_io_tg, hexiom, docutils, tomli_loads, async_tree_io, pycparser, async_tree_none, logging_simple, asyncio_websockets, json, xml_etree_parse, pprint_pformat, pylint, async_tree_cpu_io_mixed, json_loads, raytrace, async_tree_memoization_tg, generators, async_tree_cpu_io_mixed_tg, tornado_http, async_tree_none_tg, deepcopy

# HPT report

- Reliability score: 90.99% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x