# Results vs. base

- fork: saulshanabrook
- ref: optimizer_type_versi
- machine: linux-x86_64
- commit hash: 1eabca9
- commit date: 2024-05-22
- overall geometric mean: 1.01x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240520-linux-x86_64-python-642b25b9a82c368b0457-3.14.0a0-642b25b | bm-20240522-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-1eabca9 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                                | 278 ms: 1.00x faster                                                          |
| chameleon      | 7.07 ms                                                               | 7.00 ms: 1.01x faster                                                         |
| docutils       | 2.94 sec                                                              | 2.95 sec: 1.00x slower                                                        |
| html5lib       | 69.4 ms                                                               | 67.0 ms: 1.04x faster                                                         |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                  |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_memoization, async_tree_io, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_none, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240520-linux-x86_64-python-642b25b9a82c368b0457-3.14.0a0-642b25b | bm-20240522-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-1eabca9 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 84.1 ms                                                               | 81.1 ms: 1.04x faster                                                         |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                  |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240520-linux-x86_64-python-642b25b9a82c368b0457-3.14.0a0-642b25b | bm-20240522-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-1eabca9 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 3.86 ms                                                               | 3.58 ms: 1.08x faster                                                         |
| regex_v8       | 25.6 ms                                                               | 25.0 ms: 1.03x faster                                                         |
| regex_compile  | 139 ms                                                                | 138 ms: 1.01x faster                                                          |
| regex_dna      | 229 ms                                                                | 228 ms: 1.00x faster                                                          |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240520-linux-x86_64-python-642b25b9a82c368b0457-3.14.0a0-642b25b | bm-20240522-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-1eabca9 |
|---------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pickle_pure_python  | 301 us                                                                | 296 us: 1.02x faster                                                          |
| json_dumps          | 10.4 ms                                                               | 10.2 ms: 1.02x faster                                                         |
| json_loads          | 28.9 us                                                               | 28.6 us: 1.01x faster                                                         |
| xml_etree_iterparse | 101 ms                                                                | 101 ms: 1.00x faster                                                          |
| xml_etree_generate  | 82.3 ms                                                               | 83.1 ms: 1.01x slower                                                         |
| xml_etree_process   | 58.1 ms                                                               | 58.6 ms: 1.01x slower                                                         |
| tomli_loads         | 1.94 sec                                                              | 1.96 sec: 1.01x slower                                                        |
| pickle_dict         | 36.3 us                                                               | 36.8 us: 1.01x slower                                                         |
| pickle_list         | 5.25 us                                                               | 5.36 us: 1.02x slower                                                         |
| Geometric mean      | (ref)                                                                 | 1.00x slower                                                                  |

Benchmark hidden because not significant (5): unpickle_pure_python, unpickle, unpickle_list, xml_etree_parse, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240520-linux-x86_64-python-642b25b9a82c368b0457-3.14.0a0-642b25b | bm-20240522-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-1eabca9 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                               | 10.9 ms: 1.00x slower                                                         |
| python_startup_no_site | 7.59 ms                                                               | 7.62 ms: 1.00x slower                                                         |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240520-linux-x86_64-python-642b25b9a82c368b0457-3.14.0a0-642b25b | bm-20240522-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-1eabca9 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                               | 9.99 ms: 1.04x faster                                                         |
| genshi_text     | 25.2 ms                                                               | 24.4 ms: 1.03x faster                                                         |
| genshi_xml      | 57.9 ms                                                               | 56.9 ms: 1.02x faster                                                         |
| django_template | 35.8 ms                                                               | 36.4 ms: 1.02x slower                                                         |
| Geometric mean  | (ref)                                                                 | 1.02x faster                                                                  |

All benchmarks:
===============

| Benchmark               | bm-20240520-linux-x86_64-python-642b25b9a82c368b0457-3.14.0a0-642b25b | bm-20240522-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-1eabca9 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot            | 3.86 ms                                                               | 3.58 ms: 1.08x faster                                                         |
| pycparser               | 1.21 sec                                                              | 1.14 sec: 1.06x faster                                                        |
| scimark_fft             | 323 ms                                                                | 311 ms: 1.04x faster                                                          |
| mako                    | 10.4 ms                                                               | 9.99 ms: 1.04x faster                                                         |
| nbody                   | 84.1 ms                                                               | 81.1 ms: 1.04x faster                                                         |
| html5lib                | 69.4 ms                                                               | 67.0 ms: 1.04x faster                                                         |
| genshi_text             | 25.2 ms                                                               | 24.4 ms: 1.03x faster                                                         |
| scimark_sparse_mat_mult | 4.45 ms                                                               | 4.33 ms: 1.03x faster                                                         |
| coverage                | 94.8 ms                                                               | 92.5 ms: 1.03x faster                                                         |
| gc_traversal            | 3.89 ms                                                               | 3.80 ms: 1.03x faster                                                         |
| regex_v8                | 25.6 ms                                                               | 25.0 ms: 1.03x faster                                                         |
| deepcopy_memo           | 38.1 us                                                               | 37.3 us: 1.02x faster                                                         |
| pickle_pure_python      | 301 us                                                                | 296 us: 1.02x faster                                                          |
| async_generators        | 469 ms                                                                | 460 ms: 1.02x faster                                                          |
| pprint_safe_repr        | 707 ms                                                                | 694 ms: 1.02x faster                                                          |
| genshi_xml              | 57.9 ms                                                               | 56.9 ms: 1.02x faster                                                         |
| json_dumps              | 10.4 ms                                                               | 10.2 ms: 1.02x faster                                                         |
| pathlib                 | 16.8 ms                                                               | 16.5 ms: 1.01x faster                                                         |
| telco                   | 8.30 ms                                                               | 8.19 ms: 1.01x faster                                                         |
| pyflate                 | 445 ms                                                                | 439 ms: 1.01x faster                                                          |
| logging_format          | 6.47 us                                                               | 6.39 us: 1.01x faster                                                         |
| regex_compile           | 139 ms                                                                | 138 ms: 1.01x faster                                                          |
| scimark_monte_carlo     | 62.6 ms                                                               | 61.9 ms: 1.01x faster                                                         |
| logging_silent          | 107 ns                                                                | 106 ns: 1.01x faster                                                          |
| crypto_pyaes            | 67.6 ms                                                               | 66.9 ms: 1.01x faster                                                         |
| chameleon               | 7.07 ms                                                               | 7.00 ms: 1.01x faster                                                         |
| sqlglot_transpile       | 1.64 ms                                                               | 1.63 ms: 1.01x faster                                                         |
| json_loads              | 28.9 us                                                               | 28.6 us: 1.01x faster                                                         |
| sqlglot_parse           | 1.31 ms                                                               | 1.30 ms: 1.01x faster                                                         |
| spectral_norm           | 102 ms                                                                | 101 ms: 1.01x faster                                                          |
| comprehensions          | 16.7 us                                                               | 16.6 us: 1.01x faster                                                         |
| raytrace                | 279 ms                                                                | 277 ms: 1.01x faster                                                          |
| 2to3                    | 280 ms                                                                | 278 ms: 1.00x faster                                                          |
| xml_etree_iterparse     | 101 ms                                                                | 101 ms: 1.00x faster                                                          |
| bench_thread_pool       | 865 us                                                                | 862 us: 1.00x faster                                                          |
| regex_dna               | 229 ms                                                                | 228 ms: 1.00x faster                                                          |
| asyncio_tcp_ssl         | 1.86 sec                                                              | 1.86 sec: 1.00x faster                                                        |
| python_startup          | 10.9 ms                                                               | 10.9 ms: 1.00x slower                                                         |
| docutils                | 2.94 sec                                                              | 2.95 sec: 1.00x slower                                                        |
| python_startup_no_site  | 7.59 ms                                                               | 7.62 ms: 1.00x slower                                                         |
| sqlglot_optimize        | 56.6 ms                                                               | 56.8 ms: 1.00x slower                                                         |
| coroutines              | 23.4 ms                                                               | 23.5 ms: 1.01x slower                                                         |
| create_gc_cycles        | 1.79 ms                                                               | 1.80 ms: 1.01x slower                                                         |
| nqueens                 | 86.2 ms                                                               | 86.9 ms: 1.01x slower                                                         |
| xml_etree_generate      | 82.3 ms                                                               | 83.1 ms: 1.01x slower                                                         |
| xml_etree_process       | 58.1 ms                                                               | 58.6 ms: 1.01x slower                                                         |
| scimark_sor             | 137 ms                                                                | 138 ms: 1.01x slower                                                          |
| thrift                  | 823 us                                                                | 833 us: 1.01x slower                                                          |
| tomli_loads             | 1.94 sec                                                              | 1.96 sec: 1.01x slower                                                        |
| pickle_dict             | 36.3 us                                                               | 36.8 us: 1.01x slower                                                         |
| django_template         | 35.8 ms                                                               | 36.4 ms: 1.02x slower                                                         |
| pickle_list             | 5.25 us                                                               | 5.36 us: 1.02x slower                                                         |
| mdp                     | 2.60 sec                                                              | 2.79 sec: 1.07x slower                                                        |
| Geometric mean          | (ref)                                                                 | 1.01x faster                                                                  |

Benchmark hidden because not significant (45): async_tree_memoization, deltablue, async_tree_io, pprint_pformat, unpickle_pure_python, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, deepcopy, async_tree_none_tg, json, async_tree_none, sqlite_synth, float, dask, unpickle, unpickle_list, typing_runtime_protocols, asyncio_websockets, sympy_str, async_tree_io_tg, go, pidigits, logging_simple, xml_etree_parse, bench_mp_pool, pylint, sympy_sum, sympy_integrate, asyncio_tcp, fannkuch, hexiom, richards, chaos, richards_super, generators, dulwich_log, sympy_expand, tornado_http, flaskblogging, scimark_lu, meteor_contest, sqlglot_normalize, deepcopy_reduce, pickle

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x