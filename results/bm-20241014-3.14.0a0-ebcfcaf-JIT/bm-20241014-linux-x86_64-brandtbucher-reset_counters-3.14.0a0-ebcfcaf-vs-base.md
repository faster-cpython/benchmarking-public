# Results vs. base

- fork: brandtbucher
- ref: reset_counters
- machine: linux-x86_64
- commit hash: ebcfcaf
- commit date: 2024-10-14
- overall geometric mean: 1.005x faster
- HPT reliability: 99.12%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241014-linux-x86_64-python-3fea1d000ef0a74062fd-3.14.0a0-3fea1d0 | bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 277 ms                                                                | 278 ms: 1.00x slower                                                  |
| docutils       | 2.89 sec                                                              | 2.87 sec: 1.01x faster                                                |
| tornado_http   | 94.3 ms                                                               | 93.7 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241014-linux-x86_64-python-3fea1d000ef0a74062fd-3.14.0a0-3fea1d0 | bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf |
|------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| asyncio_tcp_ssl  | 1.80 sec                                                              | 1.80 sec: 1.00x faster                                                |
| async_generators | 452 ms                                                                | 454 ms: 1.00x slower                                                  |
| asyncio_tcp      | 484 ms                                                                | 496 ms: 1.03x slower                                                  |
| Geometric mean   | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241014-linux-x86_64-python-3fea1d000ef0a74062fd-3.14.0a0-3fea1d0 | bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 190 ms                                                                | 185 ms: 1.02x faster                                                  |
| float          | 73.0 ms                                                               | 72.4 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241014-linux-x86_64-python-3fea1d000ef0a74062fd-3.14.0a0-3fea1d0 | bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 25.7 ms                                                               | 24.1 ms: 1.06x faster                                                 |
| regex_dna      | 221 ms                                                                | 209 ms: 1.06x faster                                                  |
| regex_effbot   | 3.66 ms                                                               | 3.61 ms: 1.01x faster                                                 |
| regex_compile  | 141 ms                                                                | 139 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                                 | 1.04x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241014-linux-x86_64-python-3fea1d000ef0a74062fd-3.14.0a0-3fea1d0 | bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf |
|--------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle           | 16.2 us                                                               | 14.8 us: 1.10x faster                                                 |
| pickle_list        | 5.15 us                                                               | 5.17 us: 1.00x slower                                                 |
| xml_etree_generate | 77.5 ms                                                               | 78.4 ms: 1.01x slower                                                 |
| pickle_pure_python | 305 us                                                                | 310 us: 1.01x slower                                                  |
| pickle_dict        | 34.7 us                                                               | 35.2 us: 1.01x slower                                                 |
| unpickle_list      | 5.07 us                                                               | 5.41 us: 1.07x slower                                                 |
| Geometric mean     | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (8): pickle, tomli_loads, json_loads, xml_etree_process, unpickle_pure_python, xml_etree_iterparse, json_dumps, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241014-linux-x86_64-python-3fea1d000ef0a74062fd-3.14.0a0-3fea1d0 | bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                 |
| python_startup_no_site | 7.08 ms                                                               | 7.07 ms: 1.00x faster                                                 |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241014-linux-x86_64-python-3fea1d000ef0a74062fd-3.14.0a0-3fea1d0 | bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 59.0 ms                                                               | 58.0 ms: 1.02x faster                                                 |
| django_template | 36.6 ms                                                               | 36.0 ms: 1.02x faster                                                 |
| mako            | 9.98 ms                                                               | 10.0 ms: 1.01x slower                                                 |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                          |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20241014-linux-x86_64-python-3fea1d000ef0a74062fd-3.14.0a0-3fea1d0 | bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle                | 16.2 us                                                               | 14.8 us: 1.10x faster                                                 |
| mdp                     | 2.76 sec                                                              | 2.55 sec: 1.08x faster                                                |
| regex_v8                | 25.7 ms                                                               | 24.1 ms: 1.06x faster                                                 |
| regex_dna               | 221 ms                                                                | 209 ms: 1.06x faster                                                  |
| pycparser               | 1.20 sec                                                              | 1.15 sec: 1.05x faster                                                |
| scimark_fft             | 323 ms                                                                | 312 ms: 1.03x faster                                                  |
| unpack_sequence         | 115 ns                                                                | 112 ns: 1.03x faster                                                  |
| pidigits                | 190 ms                                                                | 185 ms: 1.02x faster                                                  |
| pprint_pformat          | 1.52 sec                                                              | 1.49 sec: 1.02x faster                                                |
| scimark_lu              | 113 ms                                                                | 110 ms: 1.02x faster                                                  |
| richards_super          | 46.0 ms                                                               | 45.2 ms: 1.02x faster                                                 |
| genshi_xml              | 59.0 ms                                                               | 58.0 ms: 1.02x faster                                                 |
| django_template         | 36.6 ms                                                               | 36.0 ms: 1.02x faster                                                 |
| regex_effbot            | 3.66 ms                                                               | 3.61 ms: 1.01x faster                                                 |
| regex_compile           | 141 ms                                                                | 139 ms: 1.01x faster                                                  |
| logging_simple          | 5.55 us                                                               | 5.48 us: 1.01x faster                                                 |
| crypto_pyaes            | 67.5 ms                                                               | 66.7 ms: 1.01x faster                                                 |
| coverage                | 84.4 ms                                                               | 83.5 ms: 1.01x faster                                                 |
| spectral_norm           | 103 ms                                                                | 101 ms: 1.01x faster                                                  |
| dulwich_log             | 68.2 ms                                                               | 67.5 ms: 1.01x faster                                                 |
| richards                | 41.1 ms                                                               | 40.7 ms: 1.01x faster                                                 |
| sympy_integrate         | 23.4 ms                                                               | 23.2 ms: 1.01x faster                                                 |
| float                   | 73.0 ms                                                               | 72.4 ms: 1.01x faster                                                 |
| docutils                | 2.89 sec                                                              | 2.87 sec: 1.01x faster                                                |
| go                      | 133 ms                                                                | 132 ms: 1.01x faster                                                  |
| sympy_expand            | 502 ms                                                                | 498 ms: 1.01x faster                                                  |
| scimark_monte_carlo     | 64.0 ms                                                               | 63.5 ms: 1.01x faster                                                 |
| pathlib                 | 16.0 ms                                                               | 15.9 ms: 1.01x faster                                                 |
| sqlglot_transpile       | 1.68 ms                                                               | 1.67 ms: 1.01x faster                                                 |
| tornado_http            | 94.3 ms                                                               | 93.7 ms: 1.01x faster                                                 |
| sqlglot_optimize        | 59.7 ms                                                               | 59.3 ms: 1.01x faster                                                 |
| logging_silent          | 100 ns                                                                | 99.8 ns: 1.01x faster                                                 |
| scimark_sor             | 118 ms                                                                | 117 ms: 1.00x faster                                                  |
| chaos                   | 59.4 ms                                                               | 59.1 ms: 1.00x faster                                                 |
| sympy_sum               | 175 ms                                                                | 175 ms: 1.00x faster                                                  |
| asyncio_tcp_ssl         | 1.80 sec                                                              | 1.80 sec: 1.00x faster                                                |
| bench_thread_pool       | 873 us                                                                | 871 us: 1.00x faster                                                  |
| python_startup          | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                 |
| python_startup_no_site  | 7.08 ms                                                               | 7.07 ms: 1.00x faster                                                 |
| pickle_list             | 5.15 us                                                               | 5.17 us: 1.00x slower                                                 |
| bpe_tokeniser           | 4.38 sec                                                              | 4.39 sec: 1.00x slower                                                |
| 2to3                    | 277 ms                                                                | 278 ms: 1.00x slower                                                  |
| async_generators        | 452 ms                                                                | 454 ms: 1.00x slower                                                  |
| hexiom                  | 6.96 ms                                                               | 7.00 ms: 1.01x slower                                                 |
| mako                    | 9.98 ms                                                               | 10.0 ms: 1.01x slower                                                 |
| deepcopy_memo           | 27.2 us                                                               | 27.4 us: 1.01x slower                                                 |
| scimark_sparse_mat_mult | 4.58 ms                                                               | 4.62 ms: 1.01x slower                                                 |
| nqueens                 | 85.6 ms                                                               | 86.5 ms: 1.01x slower                                                 |
| telco                   | 7.54 ms                                                               | 7.62 ms: 1.01x slower                                                 |
| xml_etree_generate      | 77.5 ms                                                               | 78.4 ms: 1.01x slower                                                 |
| sqlite_synth            | 2.79 us                                                               | 2.82 us: 1.01x slower                                                 |
| pickle_pure_python      | 305 us                                                                | 310 us: 1.01x slower                                                  |
| pickle_dict             | 34.7 us                                                               | 35.2 us: 1.01x slower                                                 |
| meteor_contest          | 106 ms                                                                | 107 ms: 1.01x slower                                                  |
| pyflate                 | 437 ms                                                                | 447 ms: 1.02x slower                                                  |
| fannkuch                | 372 ms                                                                | 381 ms: 1.02x slower                                                  |
| asyncio_tcp             | 484 ms                                                                | 496 ms: 1.03x slower                                                  |
| gc_traversal            | 3.78 ms                                                               | 4.01 ms: 1.06x slower                                                 |
| unpickle_list           | 5.07 us                                                               | 5.41 us: 1.07x slower                                                 |
| Geometric mean          | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (30): pylint, thrift, deepcopy, genshi_text, asyncio_websockets, sympy_str, pickle, tomli_loads, json_loads, typing_runtime_protocols, coroutines, sqlglot_parse, generators, create_gc_cycles, json, logging_format, sqlglot_normalize, xml_etree_process, html5lib, bench_mp_pool, unpickle_pure_python, xml_etree_iterparse, json_dumps, deepcopy_reduce, nbody, xml_etree_parse, deltablue, comprehensions, pprint_safe_repr, raytrace

- Geometric mean (including insignificant results): 1.005x faster
# HPT report

- Reliability score: 99.12% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x