# Results vs. base

- fork: brandtbucher
- ref: hoist
- machine: linux-x86_64
- commit hash: bc99ede
- commit date: 2024-05-08
- overall geometric mean: 1.01x faster
- HPT reliability: 99.92%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240508-linux-x86_64-python-7b0c247f1c176e092777-3.14.0a0-7b0c247 | bm-20240508-linux-x86_64-brandtbucher-hoist-3.14.0a0-bc99ede |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 280 ms                                                                | 279 ms: 1.00x faster                                         |
| chameleon      | 7.20 ms                                                               | 7.07 ms: 1.02x faster                                        |
| html5lib       | 70.7 ms                                                               | 69.7 ms: 1.01x faster                                        |
| tornado_http   | 98.4 ms                                                               | 97.4 ms: 1.01x faster                                        |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                 |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240508-linux-x86_64-python-7b0c247f1c176e092777-3.14.0a0-7b0c247 | bm-20240508-linux-x86_64-brandtbucher-hoist-3.14.0a0-bc99ede |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 632 ms                                                                | 617 ms: 1.02x faster                                         |
| async_tree_none         | 370 ms                                                                | 364 ms: 1.02x faster                                         |
| Geometric mean          | (ref)                                                                 | 1.01x faster                                                 |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none_tg, async_tree_io, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240508-linux-x86_64-python-7b0c247f1c176e092777-3.14.0a0-7b0c247 | bm-20240508-linux-x86_64-brandtbucher-hoist-3.14.0a0-bc99ede |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 84.0 ms                                                               | 86.0 ms: 1.02x slower                                        |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                 |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240508-linux-x86_64-python-7b0c247f1c176e092777-3.14.0a0-7b0c247 | bm-20240508-linux-x86_64-brandtbucher-hoist-3.14.0a0-bc99ede |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_dna      | 228 ms                                                                | 221 ms: 1.03x faster                                         |
| regex_v8       | 25.3 ms                                                               | 24.6 ms: 1.03x faster                                        |
| regex_effbot   | 3.68 ms                                                               | 3.66 ms: 1.01x faster                                        |
| regex_compile  | 140 ms                                                                | 140 ms: 1.01x slower                                         |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240508-linux-x86_64-python-7b0c247f1c176e092777-3.14.0a0-7b0c247 | bm-20240508-linux-x86_64-brandtbucher-hoist-3.14.0a0-bc99ede |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_list          | 5.56 us                                                               | 5.14 us: 1.08x faster                                        |
| pickle               | 12.1 us                                                               | 11.8 us: 1.03x faster                                        |
| pickle_dict          | 34.7 us                                                               | 33.9 us: 1.02x faster                                        |
| xml_etree_process    | 58.9 ms                                                               | 57.9 ms: 1.02x faster                                        |
| unpickle_pure_python | 223 us                                                                | 221 us: 1.01x faster                                         |
| xml_etree_generate   | 83.2 ms                                                               | 82.5 ms: 1.01x faster                                        |
| json_loads           | 28.9 us                                                               | 29.0 us: 1.00x slower                                        |
| json_dumps           | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                        |
| unpickle             | 15.8 us                                                               | 16.2 us: 1.03x slower                                        |
| unpickle_list        | 5.21 us                                                               | 5.40 us: 1.04x slower                                        |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                 |

Benchmark hidden because not significant (4): pickle_pure_python, xml_etree_iterparse, tomli_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240508-linux-x86_64-python-7b0c247f1c176e092777-3.14.0a0-7b0c247 | bm-20240508-linux-x86_64-brandtbucher-hoist-3.14.0a0-bc99ede |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup | 11.1 ms                                                               | 11.1 ms: 1.00x faster                                        |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                 |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240508-linux-x86_64-python-7b0c247f1c176e092777-3.14.0a0-7b0c247 | bm-20240508-linux-x86_64-brandtbucher-hoist-3.14.0a0-bc99ede |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 37.1 ms                                                               | 36.0 ms: 1.03x faster                                        |
| genshi_xml      | 59.9 ms                                                               | 58.5 ms: 1.02x faster                                        |
| mako            | 9.67 ms                                                               | 9.52 ms: 1.02x faster                                        |
| genshi_text     | 25.1 ms                                                               | 24.7 ms: 1.02x faster                                        |
| Geometric mean  | (ref)                                                                 | 1.02x faster                                                 |

All benchmarks:
===============

| Benchmark               | bm-20240508-linux-x86_64-python-7b0c247f1c176e092777-3.14.0a0-7b0c247 | bm-20240508-linux-x86_64-brandtbucher-hoist-3.14.0a0-bc99ede |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_list             | 5.56 us                                                               | 5.14 us: 1.08x faster                                        |
| spectral_norm           | 104 ms                                                                | 99.0 ms: 1.05x faster                                        |
| pycparser               | 1.20 sec                                                              | 1.15 sec: 1.04x faster                                       |
| django_template         | 37.1 ms                                                               | 36.0 ms: 1.03x faster                                        |
| logging_silent          | 109 ns                                                                | 106 ns: 1.03x faster                                         |
| regex_dna               | 228 ms                                                                | 221 ms: 1.03x faster                                         |
| gc_traversal            | 3.94 ms                                                               | 3.84 ms: 1.03x faster                                        |
| coroutines              | 23.3 ms                                                               | 22.7 ms: 1.03x faster                                        |
| pickle                  | 12.1 us                                                               | 11.8 us: 1.03x faster                                        |
| pyflate                 | 460 ms                                                                | 449 ms: 1.03x faster                                         |
| regex_v8                | 25.3 ms                                                               | 24.6 ms: 1.03x faster                                        |
| deltablue               | 3.82 ms                                                               | 3.73 ms: 1.02x faster                                        |
| genshi_xml              | 59.9 ms                                                               | 58.5 ms: 1.02x faster                                        |
| pickle_dict             | 34.7 us                                                               | 33.9 us: 1.02x faster                                        |
| async_tree_cpu_io_mixed | 632 ms                                                                | 617 ms: 1.02x faster                                         |
| richards                | 43.6 ms                                                               | 42.7 ms: 1.02x faster                                        |
| sqlglot_normalize       | 116 ms                                                                | 113 ms: 1.02x faster                                         |
| logging_simple          | 5.85 us                                                               | 5.72 us: 1.02x faster                                        |
| logging_format          | 6.53 us                                                               | 6.41 us: 1.02x faster                                        |
| chameleon               | 7.20 ms                                                               | 7.07 ms: 1.02x faster                                        |
| sqlglot_optimize        | 58.0 ms                                                               | 57.1 ms: 1.02x faster                                        |
| async_tree_none         | 370 ms                                                                | 364 ms: 1.02x faster                                         |
| xml_etree_process       | 58.9 ms                                                               | 57.9 ms: 1.02x faster                                        |
| richards_super          | 49.5 ms                                                               | 48.8 ms: 1.02x faster                                        |
| mako                    | 9.67 ms                                                               | 9.52 ms: 1.02x faster                                        |
| pprint_safe_repr        | 739 ms                                                                | 727 ms: 1.02x faster                                         |
| genshi_text             | 25.1 ms                                                               | 24.7 ms: 1.02x faster                                        |
| html5lib                | 70.7 ms                                                               | 69.7 ms: 1.01x faster                                        |
| create_gc_cycles        | 1.83 ms                                                               | 1.81 ms: 1.01x faster                                        |
| async_generators        | 471 ms                                                                | 465 ms: 1.01x faster                                         |
| comprehensions          | 16.8 us                                                               | 16.6 us: 1.01x faster                                        |
| deepcopy_reduce         | 3.35 us                                                               | 3.31 us: 1.01x faster                                        |
| unpickle_pure_python    | 223 us                                                                | 221 us: 1.01x faster                                         |
| tornado_http            | 98.4 ms                                                               | 97.4 ms: 1.01x faster                                        |
| generators              | 30.0 ms                                                               | 29.7 ms: 1.01x faster                                        |
| xml_etree_generate      | 83.2 ms                                                               | 82.5 ms: 1.01x faster                                        |
| dulwich_log             | 70.7 ms                                                               | 70.1 ms: 1.01x faster                                        |
| regex_effbot            | 3.68 ms                                                               | 3.66 ms: 1.01x faster                                        |
| bench_thread_pool       | 874 us                                                                | 868 us: 1.01x faster                                         |
| scimark_sparse_mat_mult | 4.58 ms                                                               | 4.55 ms: 1.01x faster                                        |
| 2to3                    | 280 ms                                                                | 279 ms: 1.00x faster                                         |
| asyncio_tcp_ssl         | 1.86 sec                                                              | 1.85 sec: 1.00x faster                                       |
| telco                   | 172 ms                                                                | 171 ms: 1.00x faster                                         |
| python_startup          | 11.1 ms                                                               | 11.1 ms: 1.00x faster                                        |
| mdp                     | 2.60 sec                                                              | 2.61 sec: 1.00x slower                                       |
| json_loads              | 28.9 us                                                               | 29.0 us: 1.00x slower                                        |
| sympy_str               | 302 ms                                                                | 304 ms: 1.01x slower                                         |
| regex_compile           | 140 ms                                                                | 140 ms: 1.01x slower                                         |
| sympy_sum               | 173 ms                                                                | 174 ms: 1.01x slower                                         |
| sympy_integrate         | 22.7 ms                                                               | 22.8 ms: 1.01x slower                                        |
| json_dumps              | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                        |
| scimark_fft             | 317 ms                                                                | 321 ms: 1.01x slower                                         |
| nqueens                 | 86.6 ms                                                               | 87.8 ms: 1.01x slower                                        |
| fannkuch                | 362 ms                                                                | 368 ms: 1.02x slower                                         |
| scimark_lu              | 123 ms                                                                | 125 ms: 1.02x slower                                         |
| deepcopy                | 371 us                                                                | 378 us: 1.02x slower                                         |
| asyncio_tcp             | 505 ms                                                                | 515 ms: 1.02x slower                                         |
| raytrace                | 278 ms                                                                | 283 ms: 1.02x slower                                         |
| nbody                   | 84.0 ms                                                               | 86.0 ms: 1.02x slower                                        |
| hexiom                  | 6.56 ms                                                               | 6.73 ms: 1.03x slower                                        |
| unpickle                | 15.8 us                                                               | 16.2 us: 1.03x slower                                        |
| unpickle_list           | 5.21 us                                                               | 5.40 us: 1.04x slower                                        |
| Geometric mean          | (ref)                                                                 | 1.01x faster                                                 |

Benchmark hidden because not significant (38): async_tree_cpu_io_mixed_tg, async_tree_memoization, pickle_pure_python, scimark_monte_carlo, flaskblogging, scimark_sor, sympy_expand, pathlib, float, async_tree_memoization_tg, gunicorn, pylint, dask, async_tree_none_tg, chaos, sqlglot_parse, async_tree_io, meteor_contest, docutils, asyncio_websockets, sqlite_synth, python_startup_no_site, pidigits, typing_runtime_protocols, thrift, async_tree_io_tg, sqlglot_transpile, xml_etree_iterparse, bench_mp_pool, tomli_loads, crypto_pyaes, pprint_pformat, aiohttp, go, coverage, deepcopy_memo, json, xml_etree_parse

# HPT report

- Reliability score: 99.92% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x