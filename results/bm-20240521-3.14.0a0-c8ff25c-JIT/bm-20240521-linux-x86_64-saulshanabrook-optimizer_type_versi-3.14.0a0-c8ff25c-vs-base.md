# Results vs. base

- fork: saulshanabrook
- ref: optimizer_type_versi
- machine: linux-x86_64
- commit hash: c8ff25c
- commit date: 2024-05-21
- overall geometric mean: 1.00x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240520-linux-x86_64-python-642b25b9a82c368b0457-3.14.0a0-642b25b | bm-20240521-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-c8ff25c |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                                | 278 ms: 1.00x faster                                                          |
| docutils       | 2.94 sec                                                              | 2.93 sec: 1.00x faster                                                        |
| html5lib       | 69.4 ms                                                               | 66.3 ms: 1.05x faster                                                         |
| tornado_http   | 96.5 ms                                                               | 97.0 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                  |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20240520-linux-x86_64-python-642b25b9a82c368b0457-3.14.0a0-642b25b | bm-20240521-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-c8ff25c |
|--------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_none_tg | 337 ms                                                                | 330 ms: 1.02x faster                                                          |
| Geometric mean     | (ref)                                                                 | 1.02x faster                                                                  |

Benchmark hidden because not significant (7): async_tree_io_tg, async_tree_memoization, async_tree_io, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240520-linux-x86_64-python-642b25b9a82c368b0457-3.14.0a0-642b25b | bm-20240521-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-c8ff25c |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 84.1 ms                                                               | 81.6 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                  |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240520-linux-x86_64-python-642b25b9a82c368b0457-3.14.0a0-642b25b | bm-20240521-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-c8ff25c |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_v8       | 25.6 ms                                                               | 24.5 ms: 1.05x faster                                                         |
| regex_effbot   | 3.86 ms                                                               | 3.71 ms: 1.04x faster                                                         |
| regex_compile  | 139 ms                                                                | 138 ms: 1.01x faster                                                          |
| regex_dna      | 229 ms                                                                | 231 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark         | bm-20240520-linux-x86_64-python-642b25b9a82c368b0457-3.14.0a0-642b25b | bm-20240521-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-c8ff25c |
|-------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pickle_list       | 5.25 us                                                               | 5.10 us: 1.03x faster                                                         |
| pickle            | 12.0 us                                                               | 11.7 us: 1.03x faster                                                         |
| json_loads        | 28.9 us                                                               | 28.6 us: 1.01x faster                                                         |
| pickle_dict       | 36.3 us                                                               | 36.3 us: 1.00x faster                                                         |
| xml_etree_process | 58.1 ms                                                               | 58.3 ms: 1.00x slower                                                         |
| tomli_loads       | 1.94 sec                                                              | 1.95 sec: 1.01x slower                                                        |
| xml_etree_parse   | 150 ms                                                                | 152 ms: 1.01x slower                                                          |
| unpickle_list     | 5.18 us                                                               | 5.37 us: 1.04x slower                                                         |
| Geometric mean    | (ref)                                                                 | 1.00x faster                                                                  |

Benchmark hidden because not significant (6): unpickle_pure_python, unpickle, json_dumps, xml_etree_generate, pickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240520-linux-x86_64-python-642b25b9a82c368b0457-3.14.0a0-642b25b | bm-20240521-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-c8ff25c |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                               | 10.1 ms: 1.02x faster                                                         |
| genshi_text     | 25.2 ms                                                               | 24.9 ms: 1.01x faster                                                         |
| django_template | 35.8 ms                                                               | 36.2 ms: 1.01x slower                                                         |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                                  |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark          | bm-20240520-linux-x86_64-python-642b25b9a82c368b0457-3.14.0a0-642b25b | bm-20240521-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-c8ff25c |
|--------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| html5lib           | 69.4 ms                                                               | 66.3 ms: 1.05x faster                                                         |
| regex_v8           | 25.6 ms                                                               | 24.5 ms: 1.05x faster                                                         |
| pycparser          | 1.21 sec                                                              | 1.16 sec: 1.04x faster                                                        |
| gc_traversal       | 3.89 ms                                                               | 3.74 ms: 1.04x faster                                                         |
| regex_effbot       | 3.86 ms                                                               | 3.71 ms: 1.04x faster                                                         |
| scimark_fft        | 323 ms                                                                | 313 ms: 1.03x faster                                                          |
| nbody              | 84.1 ms                                                               | 81.6 ms: 1.03x faster                                                         |
| pickle_list        | 5.25 us                                                               | 5.10 us: 1.03x faster                                                         |
| pickle             | 12.0 us                                                               | 11.7 us: 1.03x faster                                                         |
| mako               | 10.4 ms                                                               | 10.1 ms: 1.02x faster                                                         |
| pprint_pformat     | 1.48 sec                                                              | 1.44 sec: 1.02x faster                                                        |
| coroutines         | 23.4 ms                                                               | 22.9 ms: 1.02x faster                                                         |
| async_tree_none_tg | 337 ms                                                                | 330 ms: 1.02x faster                                                          |
| coverage           | 94.8 ms                                                               | 93.0 ms: 1.02x faster                                                         |
| spectral_norm      | 102 ms                                                                | 100.0 ms: 1.02x faster                                                        |
| sqlite_synth       | 2.88 us                                                               | 2.83 us: 1.02x faster                                                         |
| pathlib            | 16.8 ms                                                               | 16.5 ms: 1.02x faster                                                         |
| async_generators   | 469 ms                                                                | 463 ms: 1.01x faster                                                          |
| genshi_text        | 25.2 ms                                                               | 24.9 ms: 1.01x faster                                                         |
| logging_format     | 6.47 us                                                               | 6.40 us: 1.01x faster                                                         |
| json_loads         | 28.9 us                                                               | 28.6 us: 1.01x faster                                                         |
| deepcopy_memo      | 38.1 us                                                               | 37.7 us: 1.01x faster                                                         |
| logging_simple     | 5.76 us                                                               | 5.70 us: 1.01x faster                                                         |
| telco              | 8.30 ms                                                               | 8.22 ms: 1.01x faster                                                         |
| thrift             | 823 us                                                                | 816 us: 1.01x faster                                                          |
| json               | 5.25 ms                                                               | 5.21 ms: 1.01x faster                                                         |
| nqueens            | 86.2 ms                                                               | 85.5 ms: 1.01x faster                                                         |
| regex_compile      | 139 ms                                                                | 138 ms: 1.01x faster                                                          |
| sympy_sum          | 172 ms                                                                | 171 ms: 1.01x faster                                                          |
| asyncio_tcp_ssl    | 1.86 sec                                                              | 1.85 sec: 1.01x faster                                                        |
| 2to3               | 280 ms                                                                | 278 ms: 1.00x faster                                                          |
| docutils           | 2.94 sec                                                              | 2.93 sec: 1.00x faster                                                        |
| sympy_integrate    | 22.5 ms                                                               | 22.5 ms: 1.00x faster                                                         |
| pickle_dict        | 36.3 us                                                               | 36.3 us: 1.00x faster                                                         |
| xml_etree_process  | 58.1 ms                                                               | 58.3 ms: 1.00x slower                                                         |
| tornado_http       | 96.5 ms                                                               | 97.0 ms: 1.01x slower                                                         |
| tomli_loads        | 1.94 sec                                                              | 1.95 sec: 1.01x slower                                                        |
| dulwich_log        | 68.9 ms                                                               | 69.3 ms: 1.01x slower                                                         |
| fannkuch           | 353 ms                                                                | 356 ms: 1.01x slower                                                          |
| regex_dna          | 229 ms                                                                | 231 ms: 1.01x slower                                                          |
| scimark_sor        | 137 ms                                                                | 138 ms: 1.01x slower                                                          |
| go                 | 147 ms                                                                | 149 ms: 1.01x slower                                                          |
| django_template    | 35.8 ms                                                               | 36.2 ms: 1.01x slower                                                         |
| xml_etree_parse    | 150 ms                                                                | 152 ms: 1.01x slower                                                          |
| meteor_contest     | 109 ms                                                                | 111 ms: 1.01x slower                                                          |
| deepcopy           | 369 us                                                                | 375 us: 1.02x slower                                                          |
| chaos              | 59.5 ms                                                               | 60.5 ms: 1.02x slower                                                         |
| pyflate            | 445 ms                                                                | 453 ms: 1.02x slower                                                          |
| unpickle_list      | 5.18 us                                                               | 5.37 us: 1.04x slower                                                         |
| generators         | 30.4 ms                                                               | 36.3 ms: 1.19x slower                                                         |
| Geometric mean     | (ref)                                                                 | 1.00x faster                                                                  |

Benchmark hidden because not significant (46): async_tree_io_tg, async_tree_memoization, async_tree_io, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, dask, typing_runtime_protocols, scimark_monte_carlo, unpickle_pure_python, async_tree_none, pprint_safe_repr, deepcopy_reduce, unpickle, chameleon, logging_silent, float, sqlglot_transpile, scimark_lu, sqlglot_parse, asyncio_websockets, deltablue, asyncio_tcp, sympy_expand, richards_super, sqlglot_optimize, pidigits, sympy_str, python_startup_no_site, bench_mp_pool, python_startup, json_dumps, bench_thread_pool, xml_etree_generate, pylint, pickle_pure_python, comprehensions, xml_etree_iterparse, scimark_sparse_mat_mult, create_gc_cycles, genshi_xml, crypto_pyaes, raytrace, sqlglot_normalize, richards, flaskblogging
Ignored benchmarks (2) of results/bm-20240520-3.14.0a0-642b25b-JIT/bm-20240520-linux-x86_64-python-642b25b9a82c368b0457-3.14.0a0-642b25b.json: hexiom, mdp

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x